// Host-owned authority boundary. No Godot types are stored in the Core world.
#include <corerpg/action.hpp>
#include <corerpg/content_catalog.hpp>
#include <corerpg/content_json/content_document_decoder.hpp>
#include <corerpg/inspector.hpp>
#include <jsoncons/json.hpp>
#include <godot_cpp/classes/hashing_context.hpp>
#include <corerpg/context_builder.hpp>
#include <corerpg/persistence.hpp>
#include <corerpg/simulation.hpp>
#include <corerpg/version.hpp>
#include <godot_cpp/classes/ref_counted.hpp>
#include <godot_cpp/core/class_db.hpp>
#include <godot_cpp/godot.hpp>
#include <godot_cpp/variant/array.hpp>
#include <godot_cpp/variant/dictionary.hpp>
#include <godot_cpp/variant/packed_byte_array.hpp>
#include <algorithm>
#include <charconv>
#include <climits>
#include <stdexcept>
#include <string_view>
#include <chrono>
#include <limits>
#include <memory>
#include <mutex>
#include <set>
#include <string>
#include <thread>
#include <vector>

namespace bridge {
using namespace godot;
namespace core = corerpg;
constexpr int64_t api = 1, max_entities = 4096, max_records = 4096;
struct Fault { const char *code; };
void require(bool condition, const char *code = "INVALID_ARGUMENT") {
    if (!condition) throw Fault{code};
}
Dictionary result(const char *code = "OK") {
    Dictionary d; d["api_version"] = api; d["error_code"] = code;
    d["status"] = std::string_view(code) == "OK" ? "ok" : "rejected";
    return d;
}
template<class F> Dictionary boundary(F &&function) noexcept {
    try { return function(); }
    catch (const Fault &e) { return result(e.code); }
    catch (const std::bad_alloc &) { return result("ALLOCATION_FAILURE"); }
    catch (const std::length_error &) { return result("CAPACITY_FAILURE"); }
    catch (...) { return result("NATIVE_FAILURE"); }
}
void schema(const Dictionary &d, std::initializer_list<const char *> required,
            std::initializer_list<const char *> optional = {}) {
    require(d.size() <= 16, "REQUEST_LIMIT");
    for (const auto *key : required) require(d.has(key), "MISSING_FIELD");
    const Array keys = d.keys();
    for (int64_t i = 0; i < keys.size(); ++i) {
        require(keys[i].get_type() == Variant::STRING, "UNKNOWN_FIELD");
        const String key = keys[i];
        auto matches = [&](const char *allowed) { return key == allowed; };
        require(std::any_of(required.begin(), required.end(), matches) ||
                std::any_of(optional.begin(), optional.end(), matches), "UNKNOWN_FIELD");
    }
}
int64_t integer(const Dictionary &d, const char *key, int64_t minimum = 0,
                int64_t maximum = std::numeric_limits<int64_t>::max()) {
    require(d.has(key) && d[key].get_type() == Variant::INT, "INVALID_TYPE");
    const int64_t n = d[key]; require(n >= minimum && n <= maximum, "OUT_OF_RANGE"); return n;
}
String text(const Dictionary &d, const char *key) {
    require(d.has(key) && d[key].get_type() == Variant::STRING, "INVALID_TYPE");
    const String s = d[key]; require(s.length() <= 64, "REQUEST_LIMIT"); return s;
}
Array array(const Dictionary &d, const char *key, int64_t maximum) {
    require(d.has(key) && d[key].get_type() == Variant::ARRAY, "INVALID_TYPE");
    const Array a = d[key]; require(a.size() <= maximum, "REQUEST_LIMIT"); return a;
}
Dictionary object(const Variant &v) { require(v.get_type() == Variant::DICTIONARY, "INVALID_TYPE"); return v; }
void version(const Dictionary &d) { require(integer(d, "api_version") == api, "UNSUPPORTED_VERSION"); }
uint64_t unsigned_text(const Dictionary &d, const char *key) {
    const auto utf8 = text(d, key).utf8(); const std::string s(utf8.get_data(), utf8.length());
    require(!s.empty() && (s.size() == 1 || s[0] != '0'));
    uint64_t n{}; const auto p = std::from_chars(s.data(), s.data() + s.size(), n);
    require(p.ec == std::errc{} && p.ptr == s.data() + s.size()); return n;
}
String u64(uint64_t n) { return String(std::to_string(n).c_str()); }
core::EntityId id(const Dictionary &d, const char *key) { return core::EntityId(integer(d, key, 1, max_entities)); }
core::PersistenceLimits persistence_limits() {
    core::PersistenceLimits p;
    p.max_bytes = 1024 * 1024; p.max_links = p.max_streams = p.max_definitions = max_records;
    p.max_relations = p.max_populations = p.max_memberships = p.max_knowledge = max_records;
    return p;
}
struct Campaign {
    std::shared_ptr<const core::ContentCatalog> catalog;
    core::WorldState world;
    core::RandomStreams random;
    explicit Campaign(uint64_t seed) : random(seed) {}
};
#include "v001.hpp"
struct Runtime {
    const std::thread::id owner = std::this_thread::get_id();
    std::mutex mutex;
    std::unique_ptr<Campaign> campaign;
    uint64_t epoch = 1;
    size_t sessions{};
    void thread() const { require(owner == std::this_thread::get_id(), "WRONG_THREAD"); }
    void live() const { require(bool(campaign), "NOT_INITIALIZED"); }
    void replace(std::unique_ptr<Campaign> candidate) {
        require(epoch != UINT64_MAX, "GENERATION_EXHAUSTED");
        campaign.swap(candidate); ++epoch; sessions = 0;
    }
};
core::FactKey fact_key(const Dictionary &d) {
    core::FactKey key{id(d, "subject"), static_cast<core::FactKind>(integer(d, "kind", 1, 6)), {}, {}};
    if (key.kind == core::FactKind::relation) {
        key.relation_kind = core::RelationKind(integer(d, "relation_kind", 1)); key.target = id(d, "target");
    } else require(!d.has("target") && !d.has("relation_kind"), "UNEXPECTED_FIELD");
    return key;
}
const char *rejection(core::ActionRejection code) {
    static const char *names[] = {"none", "precondition_limit_exceeded", "actor_not_found", "stale_revision",
        "precondition_failed", "entity_not_found", "target_not_found", "self_containment", "cycle_detected",
        "revision_exhausted", "invalid_relation_kind", "invalid_range", "invalid_operation"};
    return names[static_cast<unsigned>(code)];
}
core::ActionRequest decode_action(const Dictionary &d, std::vector<core::RuleCheck> &checks) {
    const String op = text(d, "operation");
    core::ActionRequest request; request.actor = id(d, "actor");
    if (op == "place") {
        schema(d, {"operation","actor","entity","target"}, {"expected_revision","preconditions"});
        request.operation = core::PlaceEntityAction{id(d,"entity"),id(d,"target")};
    } else if (op == "remove_containment") {
        schema(d, {"operation","actor","entity"}, {"expected_revision","preconditions"});
        request.operation = core::RemoveContainmentAction{id(d,"entity")};
    } else if (op == "add_relation" || op == "remove_relation") {
        schema(d, {"operation","actor","entity","target","relation_kind"}, {"expected_revision","preconditions"});
        const core::EntityRelation relation{id(d,"entity"),core::RelationKind(integer(d,"relation_kind",1)),id(d,"target")};
        if (op == "add_relation") request.operation = core::AddRelationAction{relation};
        else request.operation = core::RemoveRelationAction{relation};
    } else if (op == "roll") {
        schema(d, {"operation","actor","stream","minimum","maximum"}, {"expected_revision","preconditions"});
        request.operation = core::StreamRollAction{static_cast<uint64_t>(integer(d,"stream")),
            static_cast<uint64_t>(integer(d,"minimum")),static_cast<uint64_t>(integer(d,"maximum"))};
    } else throw Fault{"OPERATION_UNAVAILABLE"};
    if (d.has("expected_revision")) request.expected_revision = unsigned_text(d,"expected_revision");
    if (d.has("preconditions")) {
        const Array a = array(d,"preconditions",64); checks.reserve(a.size());
        for (int64_t i = 0; i < a.size(); ++i) {
            const Dictionary c = object(a[i]); schema(c,{"kind","subject"},{"related"});
            core::RuleCheck check{static_cast<core::RuleCheckKind>(integer(c,"kind",0,2)),id(c,"subject"),{}};
            if (check.kind == core::RuleCheckKind::direct_container_is) check.related = id(c,"related");
            else require(!c.has("related"),"UNEXPECTED_FIELD");
            checks.push_back(check);
        }
    }
    request.preconditions = checks; return request;
}
Dictionary visible_fact(const core::VisibleFact &f) {
    Dictionary d; d["subject"] = static_cast<int64_t>(f.key.subject.value());
    d["kind"] = static_cast<int64_t>(f.key.kind); d["present"] = f.present;
    d["reference"] = static_cast<int64_t>(f.reference.value());
    d["relation_kind"] = u64(f.key.relation_kind.value()); d["target"] = static_cast<int64_t>(f.key.target.value());
    d["total"] = u64(f.total); d["latent"] = u64(f.latent);
    const std::string definition(f.definition_id()); d["definition_id"] = String(definition.c_str());
    d["provenance"] = f.provenance() == core::FactProvenance::remembered ? "remembered" : "temporary_grant";
    return d;
}

class CoreRPGHost;
class CoreRPGSession : public RefCounted {
    GDCLASS(CoreRPGSession, RefCounted)
    friend class CoreRPGHost;
    std::weak_ptr<Runtime> runtime_;
    uint64_t epoch_{}, ticket_{}, revision_{};
    int64_t last_request_{};
    core::EntityId actor_;
    String audience_;
    std::set<uint64_t> destinations_;
    bool place_{}, remove_{}, closed_{}, active_ticket_{};
    std::chrono::steady_clock::time_point deadline_;
    std::shared_ptr<Runtime> live() const {
        auto r = runtime_.lock(); require(bool(r),"SESSION_EXPIRED"); r->thread();
        require(!closed_ && r->campaign && epoch_ == r->epoch,"SESSION_EXPIRED"); return r;
    }
protected:
    static void _bind_methods() {
        ClassDB::bind_method(D_METHOD("context","request"), &CoreRPGSession::context);
        ClassDB::bind_method(D_METHOD("availability"), &CoreRPGSession::availability);
        ClassDB::bind_method(D_METHOD("submit","request"), &CoreRPGSession::submit);
        ClassDB::bind_method(D_METHOD("close"), &CoreRPGSession::close);
    }
public:
    Dictionary availability() { return boundary([&] { auto r = live(); std::lock_guard lock(r->mutex); return result(); }); }
    Dictionary context(const Dictionary &d) {
        return boundary([&] {
            auto r = live(); std::lock_guard lock(r->mutex);
            schema(d,{"api_version"},{"subject","kind","max_selected","max_content_bytes"}); version(d);
            core::ContextRequest request;
            if (d.has("subject")) request.subject = core::EntityId(integer(d,"subject",0,max_entities));
            if (d.has("kind")) request.kind = static_cast<core::FactKind>(integer(d,"kind",1,6));
            core::ContextLimits limits; limits.max_examined = max_records;
            if (d.has("max_selected")) limits.max_selected = integer(d,"max_selected",0,256);
            if (d.has("max_content_bytes")) limits.max_content_bytes = integer(d,"max_content_bytes",0,65536);
            const auto view = core::Visibility::project(r->campaign->world,actor_);
            std::vector<core::VisibleFact> storage(limits.max_selected);
            const auto built = core::ContextBuilder::build(view,request,storage,limits);
            auto out = result(); Array facts;
            for (size_t i = 0; i < built.emitted; ++i) facts.push_back(visible_fact(storage[i]));
            out["facts"] = facts; out["context_contract_version"] = int64_t(built.contract_version);
            static const char *names[] = {"complete","examination_limit","selection_limit","output_capacity",
                "content_limit","unsupported_version","invalid_request","invalid_limits"};
            out["context_status"] = names[static_cast<unsigned>(built.status)];
            out["examined"] = int64_t(built.examined); out["emitted"] = int64_t(built.emitted);
            out["content_bytes"] = int64_t(built.content_bytes);
            require(ticket_ < INT64_MAX,"CONTEXT_EXHAUSTED");
            out["context_id"] = int64_t(ticket_ + 1); out["audience"] = audience_;
            ++ticket_; active_ticket_ = true; revision_ = r->campaign->world.revision();
            deadline_ = std::chrono::steady_clock::now() + std::chrono::seconds(60); return out;
        });
    }
    Dictionary submit(const Dictionary &d) {
        return boundary([&] {
            auto r = live(); std::lock_guard lock(r->mutex);
            schema(d,{"api_version","context_id","request_id","operation"},{"target"}); version(d);
            const auto request_id = integer(d,"request_id",1);
            require(request_id > last_request_,"REQUEST_REPLAYED");
            require(active_ticket_ && ticket_ && integer(d,"context_id",1) == int64_t(ticket_) &&
                std::chrono::steady_clock::now() <= deadline_,"CONTEXT_EXPIRED");
            require(audience_ == "player","OPERATION_DENIED");
            const String op = text(d,"operation");
            const auto view = core::Visibility::project(r->campaign->world,actor_);
            require(view.knows(actor_),"OPERATION_DENIED");
            core::ActionRequest request; request.actor = actor_; request.expected_revision = revision_;
            if (op == "place") {
                const auto target = id(d,"target");
                require(place_ && destinations_.contains(target.value()) && view.knows(target),"OPERATION_DENIED");
                request.operation = core::PlaceEntityAction{actor_,target};
            } else if (op == "remove_containment") {
                require(remove_ && !d.has("target"),"OPERATION_DENIED");
                request.operation = core::RemoveContainmentAction{actor_};
            } else throw Fault{"OPERATION_UNAVAILABLE"};
            auto candidate = std::make_unique<Campaign>(*r->campaign);
            const auto action = core::ActionEngine::process(candidate->world,candidate->random,request);
            auto out = result(action.outcome == core::ActionOutcome::rejected ? "ACTION_REJECTED" : "OK");
            // Deliberately omit privileged reasons, revisions, old/new endpoints and RNG.
            out["request_id"] = request_id;
            out["outcome"] = action.outcome == core::ActionOutcome::accepted ? "accepted" :
                action.outcome == core::ActionOutcome::no_change ? "no_change" : "rejected";
            out["events"] = Array(); // Core has consequences, no authorized event stream yet.
            r->campaign.swap(candidate); last_request_ = request_id; active_ticket_ = false; return out;
        });
    }
    Dictionary close() {
        return boundary([&] { auto r = live(); std::lock_guard lock(r->mutex); closed_ = true;
            if (r->sessions) --r->sessions; return result(); });
    }
    ~CoreRPGSession() override {
        if (auto r = runtime_.lock()) {
            std::lock_guard lock(r->mutex);
            if (!closed_ && epoch_ == r->epoch && r->sessions) --r->sessions;
        }
    }
};

class CoreRPGHost : public RefCounted {
    GDCLASS(CoreRPGHost, RefCounted)
    // Trusted Host object: never pass it or its persistence bytes to a provider.
    std::shared_ptr<Runtime> runtime_ = std::make_shared<Runtime>();
protected:
    static void _bind_methods() {
        ClassDB::bind_method(D_METHOD("initialize","request"), &CoreRPGHost::initialize);
        ClassDB::bind_method(D_METHOD("initialize_v001","request"), &CoreRPGHost::initialize_v001);
        ClassDB::bind_method(D_METHOD("prepare_v001_restore","request"), &CoreRPGHost::prepare_v001_restore);
        ClassDB::bind_method(D_METHOD("admin","request"), &CoreRPGHost::admin);
        ClassDB::bind_method(D_METHOD("step","request"), &CoreRPGHost::step);
        ClassDB::bind_method(D_METHOD("open_session","request"), &CoreRPGHost::open_session);
        ClassDB::bind_method(D_METHOD("capture"), &CoreRPGHost::capture);
        ClassDB::bind_method(D_METHOD("restore","bytes"), &CoreRPGHost::restore);
        ClassDB::bind_method(D_METHOD("diagnostics"), &CoreRPGHost::diagnostics);
        ClassDB::bind_method(D_METHOD("close"), &CoreRPGHost::close);
    }
public:
    Dictionary initialize_v001(const Dictionary &d) {
        return boundary([&] {
            auto r = runtime_; r->thread(); std::lock_guard lock(r->mutex);
            schema(d,{"api_version","files"}); version(d);
            auto candidate = v001::prepare(object(d["files"]));
            auto out = result(); out["observer"] = int64_t(6);
            out["metadata"] = v001::metadata(object(d["files"]));
            r->replace(std::move(candidate)); return out;
        });
    }
    Dictionary prepare_v001_restore(const Dictionary &d) {
        return boundary([&] {
            auto r = runtime_; r->thread(); std::lock_guard lock(r->mutex);
            schema(d,{"api_version","files"}); version(d);
            const auto files = object(d["files"]);
            auto candidate = v001::prepare(files, false);
            auto out = result(); out["metadata"] = v001::metadata(files);
            out["observer"] = int64_t(6); // First materialized identity in pinned recipe.
            r->replace(std::move(candidate)); return out;
        });
    }
    Dictionary initialize(const Dictionary &d) {
        return boundary([&] {
            auto r = runtime_; r->thread(); std::lock_guard lock(r->mutex);
            schema(d,{"api_version","seed","entities"}); version(d);
            const auto seed = unsigned_text(d,"seed"); const auto count = integer(d,"entities",1,256);
            auto candidate = std::make_unique<Campaign>(seed); Array entities;
            for (int64_t i=0; i<count; ++i) {
                const auto entity = candidate->world.create_entity(); require(entity.is_valid(),"CORE_REJECTED");
                entities.push_back(int64_t(entity.value()));
            }
            auto out = result(); out["entities"] = entities; r->replace(std::move(candidate)); return out;
        });
    }
    Dictionary admin(const Dictionary &d) {
        return boundary([&] {
            auto r = runtime_; r->thread(); std::lock_guard lock(r->mutex); r->live(); version(d);
            const String op = text(d,"operation"); auto candidate = std::make_unique<Campaign>(*r->campaign);
            auto &world = candidate->world; auto out = result(); int code = 0;
            if (op == "create_entity") {
                schema(d,{"api_version","operation"}); require(world.entity_count() < max_entities,"WORLD_LIMIT");
                const auto entity = world.create_entity(); require(entity.is_valid(),"CORE_REJECTED"); out["entity"] = int64_t(entity.value());
            } else if (op == "declare_population") {
                schema(d,{"api_version","operation","entity","total"});
                code = int(world.declare_population(id(d,"entity"),integer(d,"total",0,max_entities)));
            } else if (op == "materialize") {
                schema(d,{"api_version","operation","entity","count"});
                const auto count = integer(d,"count",0,256);
                require(world.entity_count() + count <= max_entities,"WORLD_LIMIT");
                const auto materialized = world.materialize_population(id(d,"entity"),count);
                code = int(materialized.status); out["first"] = int64_t(materialized.first.value()); out["count"] = int64_t(materialized.count);
            } else if (op == "learn" || op == "revoke") {
                schema(d,{"api_version","operation","observer","subject","kind"},{"target","relation_kind"});
                const auto key = fact_key(d);
                code = int(op == "learn" ? world.learn_fact(id(d,"observer"),key) : world.revoke_fact(id(d,"observer"),key));
            } else if (op == "revoke_knowledge") {
                schema(d,{"api_version","operation","observer"}); code = int(world.revoke_knowledge(id(d,"observer")));
            } else throw Fault{"OPERATION_UNAVAILABLE"};
            // These Core enums all start with applied=0, no_change=1.
            if (code > 1) { out["status"] = "rejected"; out["error_code"] = "CORE_REJECTED"; }
            out["core_status"] = int64_t(code); out["revision"] = u64(world.revision());
            // Enforce the same bounded campaign policy for live operations and restore.
            require(core::Persistence::validate(core::Persistence::capture(world,candidate->random),persistence_limits()) ==
                core::PersistenceStatus::success,"WORLD_LIMIT");
            r->campaign.swap(candidate); return out;
        });
    }
    Dictionary step(const Dictionary &d) {
        return boundary([&] {
            auto r = runtime_; r->thread(); std::lock_guard lock(r->mutex); r->live();
            schema(d,{"api_version","actions"}); version(d); const Array input = array(d,"actions",64);
            std::vector<std::vector<core::RuleCheck>> checks(input.size());
            std::vector<core::ActionRequest> actions; actions.reserve(input.size());
            for (int64_t i=0; i<input.size(); ++i) actions.push_back(decode_action(object(input[i]),checks[i]));
            std::vector<core::ActionResult> outputs(actions.size()); auto candidate = std::make_unique<Campaign>(*r->campaign);
            const auto stepped = core::Simulation::step(candidate->world,candidate->random,actions,outputs);
            auto out = result(stepped.status == core::SimulationStatus::completed ? "OK" : "SIMULATION_INTERRUPTED");
            Array receipts;
            for (size_t i=0; i<stepped.processed; ++i) {
                const auto &action = outputs[i]; Dictionary receipt;
                receipt["outcome"] = action.outcome == core::ActionOutcome::accepted ? "accepted" :
                    action.outcome == core::ActionOutcome::no_change ? "no_change" : "rejected";
                receipt["rejection"] = rejection(action.rejection); receipt["revision_before"] = u64(action.revision_before);
                receipt["revision_after"] = u64(action.revision_after);
                receipt["precondition_status"] = int64_t(action.precondition_status); receipt["precondition_index"] = int64_t(action.precondition_index);
                if (const auto *roll = std::get_if<core::RollConsequence>(&action.consequence)) {
                    receipt["roll_value"] = u64(roll->value); receipt["consumed_random"] = roll->consumed_random;
                }
                receipts.push_back(receipt);
            }
            require(core::Persistence::validate(core::Persistence::capture(candidate->world,candidate->random),persistence_limits()) ==
                core::PersistenceStatus::success,"WORLD_LIMIT");
            out["processed"] = int64_t(stepped.processed); out["simulation_status"] = int64_t(stepped.status); out["results"] = receipts;
            r->campaign.swap(candidate); return out;
        });
    }
    Dictionary open_session(const Dictionary &d) {
        return boundary([&] {
            auto r = runtime_; r->thread(); std::lock_guard lock(r->mutex); r->live();
            schema(d,{"api_version","observer","audience"},{"allow_place","allow_remove","destinations"}); version(d);
            require(r->sessions < 64,"SESSION_LIMIT"); const auto actor = id(d,"observer");
            require(r->campaign->world.contains(actor),"INVALID_OBSERVER"); const auto audience = text(d,"audience");
            require(audience == "player" || audience == "npc" || audience == "ai","INVALID_AUDIENCE");
            Ref<CoreRPGSession> session; session.instantiate(); session->actor_ = actor;
            session->audience_ = audience; session->epoch_ = r->epoch;
            for (const char *key : {"allow_place","allow_remove"}) {
                if (d.has(key)) require(d[key].get_type() == Variant::BOOL,"INVALID_TYPE");
            }
            session->place_ = d.has("allow_place") && bool(d["allow_place"]);
            session->remove_ = d.has("allow_remove") && bool(d["allow_remove"]);
            require(audience == "player" || (!session->place_ && !session->remove_),"OPERATION_DENIED");
            if (d.has("destinations")) {
                const Array destinations = array(d,"destinations",256);
                for (int64_t i=0; i<destinations.size(); ++i) {
                    require(destinations[i].get_type() == Variant::INT,"INVALID_TYPE");
                    const int64_t target = destinations[i]; require(target > 0 && target <= max_entities);
                    require(r->campaign->world.contains(core::EntityId(target)),"INVALID_TARGET");
                    session->destinations_.insert(target);
                }
            }
            auto out = result(); out["session"] = session;
            session->runtime_ = r; ++r->sessions; return out;
        });
    }
    Dictionary capture() {
        return boundary([&] {
            auto r = runtime_; r->thread(); std::lock_guard lock(r->mutex); r->live();
            const auto encoded = core::Persistence::serialize(core::Persistence::capture(r->campaign->world,r->campaign->random),persistence_limits());
            require(encoded.status == core::PersistenceStatus::success,"SAVE_REJECTED");
            PackedByteArray bytes; bytes.resize(encoded.bytes.size());
            std::copy(encoded.bytes.begin(),encoded.bytes.end(),bytes.ptrw()); auto out = result(); out["bytes"] = bytes; return out;
        });
    }
    Dictionary restore(const PackedByteArray &bytes) {
        return boundary([&] {
            auto r = runtime_; r->thread(); std::lock_guard lock(r->mutex);
            require(bytes.size() <= int64_t(persistence_limits().max_bytes),"SAVE_LIMIT");
            const auto decoded = core::Persistence::deserialize({bytes.ptr(),static_cast<size_t>(bytes.size())},persistence_limits());
            auto out = result("LOAD_REJECTED"); out["core_status"] = int64_t(decoded.status);
            if (decoded.status != core::PersistenceStatus::success) return out;
            require(decoded.snapshot && decoded.snapshot->last_entity_id <= max_entities,"WORLD_LIMIT");
            auto candidate = std::make_unique<Campaign>(0);
            candidate->catalog = r->campaign ? r->campaign->catalog : nullptr;
            const auto loaded = core::Persistence::restore(*decoded.snapshot,candidate->world,candidate->random,persistence_limits(),candidate->catalog.get());
            if (loaded != core::PersistenceStatus::success) { out["core_status"] = int64_t(loaded); return out; }
            out = result(); r->replace(std::move(candidate)); return out;
        });
    }
    Dictionary diagnostics() {
        return boundary([&] {
            auto r = runtime_; r->thread(); std::lock_guard lock(r->mutex); auto out = result();
            out["initialized"] = bool(r->campaign); out["core_version"] = String(core::library_version().data());
            out["core_commit"] = "4f282863737bcd8f5add401202a9e1064c133672";
            if (r->campaign) { out["catalog_size"] = int64_t(r->campaign->catalog ? r->campaign->catalog->size() : 0);
                out["definition_bindings"] = int64_t(core::Persistence::capture(r->campaign->world,r->campaign->random).definitions.size());
                out["revision"] = u64(r->campaign->world.revision()); out["entities"] = int64_t(r->campaign->world.entity_count()); }
            return out;
        });
    }
    Dictionary close() {
        return boundary([&] { auto r = runtime_; r->thread(); std::lock_guard lock(r->mutex);
            auto out = result(); r->replace(nullptr); return out; });
    }
};
} // namespace bridge

static void initialize_bridge(godot::ModuleInitializationLevel level) {
    if (level == godot::MODULE_INITIALIZATION_LEVEL_SCENE) {
        godot::ClassDB::register_class<bridge::CoreRPGSession>();
        godot::ClassDB::register_class<bridge::CoreRPGHost>();
    }
}
static void uninitialize_bridge(godot::ModuleInitializationLevel) {}
extern "C" GDExtensionBool GDE_EXPORT nimroel_core_init(GDExtensionInterfaceGetProcAddress address,
    GDExtensionClassLibraryPtr library, GDExtensionInitialization *initialization) {
    godot::GDExtensionBinding::InitObject init(address,library,initialization);
    init.register_initializer(initialize_bridge); init.register_terminator(uninitialize_bridge);
    init.set_minimum_library_initialization_level(godot::MODULE_INITIALIZATION_LEVEL_SCENE); return init.init();
}
