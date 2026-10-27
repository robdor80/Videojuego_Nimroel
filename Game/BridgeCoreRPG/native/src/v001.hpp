// Included inside bridge namespace after Campaign. Only immutable release metadata.
namespace v001 {
namespace cj = core::content_json;
constexpr auto lock_hash = "669891e25821b36a431d0af940aed02c4d40be6b6972cd9466179b686a2cc370";
constexpr auto release_hash = "45c143a8e997e74617ab5bf9d12245ce3f59e023f7d677c299440d73897808af";
constexpr auto definition_hash = "6f90b0f7780d2568eb8060e77da6b94d4347e727f0f95e0a31707da7ff0322f5";
constexpr size_t document_limit = 65536, bundle_limit = 131072;
std::string bytes(const Dictionary &files, const std::string &name) {
    const String key(name.c_str());
    require(files.has(key), "CONTENT_FILE_SET");
    require(files[key].get_type() == Variant::PACKED_BYTE_ARRAY, "CONTENT_BYTES_REQUIRED");
    const PackedByteArray data = files[key];
    require(data.size() > 0 && data.size() <= document_limit, "CONTENT_LIMIT");
    return {reinterpret_cast<const char *>(data.ptr()), static_cast<size_t>(data.size())};
}
String digest(const std::string &data) {
    Ref<HashingContext> hash; hash.instantiate();
    PackedByteArray input; input.resize(data.size());
    std::copy(data.begin(), data.end(), input.ptrw());
    require(hash->start(HashingContext::HASH_SHA256) == OK && hash->update(input) == OK, "CONTENT_HASH_FAILURE");
    return hash->finish().hex_encode();
}
Dictionary metadata(const Dictionary &files) {
    // Canonical UTF-8 ASCII recipe, LF including final LF; fixture hash binds ALL
    // generation parameters, relation kinds, region and upstream recipe versions.
    const std::string recipe = "nimroel-v001-generation-context/1\n"
        "recipe=nim07-v001-bootstrap-1\n"
        "fixture_sha256=" + std::string(digest(bytes(files,"integration-fixture.json")).utf8().get_data()) +
        "\nworld_seed=413001\nobserver=first-materialized\nrng_bootstrap_draws=0\n";
    Dictionary out;
    out["save_schema"] = "1"; out["pack_id"] = "nimroel.treskal.villages";
    out["pack_version"] = "0.1.0"; out["content_contract"] = "0.1.0";
    out["release_sha256"] = release_hash; out["definition_set_sha256"] = definition_hash;
    out["lock_sha256"] = lock_hash; out["generation_context_sha256"] = digest(recipe);
    return out;
}
std::unique_ptr<Campaign> prepare(const Dictionary &files, bool bootstrap = true) {
    require(files.size() == 9, "CONTENT_FILE_SET");
    const auto lock_bytes = bytes(files, "content-lock.json");
    require(digest(lock_bytes) == lock_hash, "CONTENT_UNTRUSTED_RELEASE");
    const auto lock = jsoncons::json::parse(lock_bytes);
    require(lock.at("release_sha256").as<std::string>() == release_hash &&
            lock.at("definition_set_sha256").as<std::string>() == definition_hash, "CONTENT_UNTRUSTED_RELEASE");
    size_t total = lock_bytes.size();
    std::set<std::string> expected{"content-lock.json"};
    for (const auto &entry : lock.at("files").object_range()) {
        const std::string name(entry.key()); expected.insert(name);
        const auto data = bytes(files, name); total += data.size();
        require(total <= bundle_limit, "CONTENT_LIMIT");
        require(digest(data) == String(entry.value().as<std::string>().c_str()), "CONTENT_HASH_MISMATCH");
        require(cj::read_json_document(data, {document_limit}).succeeded(), "CONTENT_INVALID_JSON");
    }
    const Array keys = files.keys();
    for (int64_t i = 0; i < keys.size(); ++i) {
        require(keys[i].get_type() == Variant::STRING, "CONTENT_FILE_SET");
        const String key = keys[i]; const auto utf8 = key.utf8();
        require(expected.contains(std::string(utf8.get_data(), utf8.length())), "CONTENT_FILE_SET");
    }
    // Exact pinned bytes are a stricter acceptance rule than the specific Nimroel
    // schemas checked by stage_pack. Core still performs its real schema decodes.
    auto document = cj::read_json_document(bytes(files,"manifest.json"), {document_limit});
    require(document.succeeded(), "CONTENT_INVALID_JSON");
    const auto manifest = cj::decode_content_pack_manifest(*document.document());
    require(manifest.succeeded(), "CONTENT_INVALID_MANIFEST");
    std::vector<core::ContentDefinitionInput> definitions;
    for (const auto &locator : manifest.decoded_manifest()->resource_locators()) {
        auto resource = cj::read_json_document(bytes(files,locator), {document_limit});
        require(resource.succeeded(), "CONTENT_INVALID_JSON");
        const auto decoded = cj::decode_resource_definition(*resource.document());
        require(decoded.succeeded(), "CONTENT_INVALID_DEFINITION");
        definitions.push_back(*decoded.definition());
    }
    const auto built = core::ContentCatalog::create({core::ContentPackInput{manifest.decoded_manifest()->manifest(), std::move(definitions)}});
    require(built.succeeded() && built.catalog()->size() == 4, "CONTENT_INVALID_CATALOG");
    const auto config = jsoncons::json::parse(bytes(files,"integration-fixture.json"));
    auto candidate = std::make_unique<Campaign>(std::stoull(config.at("world_seed").as<std::string>()));
    candidate->catalog = std::make_shared<const core::ContentCatalog>(*built.catalog());
    if (!bootstrap) return candidate; // Catalog only: NEVER generate a world on resume.
    auto &world = candidate->world;
    const auto village = world.create_entity(), smith = world.create_entity(), tavern = world.create_entity(),
        external = world.create_entity(), tool = world.create_entity();
    const core::RelationKind service{config.at("relation_kinds").at("service").as<uint64_t>()},
        connection{config.at("relation_kinds").at("external_connection").as<uint64_t>()},
        association{config.at("relation_kinds").at("population_association").as<uint64_t>()};
    auto bound = [&](core::EntityId entity, const char *local) {
        const auto definition = core::DefinitionId::parse(std::string("nimroel.treskal.villages:") + local);
        require(definition && world.bind_definition(entity,*candidate->catalog,*definition) == core::DefinitionBindingChange::applied,"CONTENT_BOOTSTRAP_FAILED");
    };
    bound(village,"models/v1"); bound(smith,"capabilities/basic-blacksmithing");
    bound(tavern,"capabilities/local-tavern"); bound(tool,"objects/ordinary-agricultural-tool");
    for (const auto pair : {std::pair{smith,village}, {tavern,village}, {tool,smith}})
        require(world.place_entity(pair.first,pair.second) == core::ContainmentChange::applied,"CONTENT_BOOTSTRAP_FAILED");
    for (const auto relation : {core::EntityRelation{village,service,smith}, {village,service,tavern}, {village,connection,external}})
        require(world.add_relation(relation) == core::RelationChange::applied,"CONTENT_BOOTSTRAP_FAILED");
    require(world.declare_population(village,config.at("population").as<uint64_t>()) == core::PopulationChange::applied,"CONTENT_BOOTSTRAP_FAILED");
    const auto issued = world.materialize_population(village,config.at("materialized").as<uint64_t>(),config.at("max_batch").as<uint64_t>());
    require(issued.status == core::MaterializationStatus::applied && issued.count == 2,"CONTENT_BOOTSTRAP_FAILED");
    const auto first = issued.first, second = core::EntityId{first.value()+1};
    for (const auto observer : {first,second})
        require(world.add_relation({observer,association,village}) == core::RelationChange::applied,"CONTENT_BOOTSTRAP_FAILED");
    auto learn = [&](core::EntityId observer, core::FactKey key) {
        require(world.learn_fact(observer,key) == core::KnowledgeChange::applied,"CONTENT_BOOTSTRAP_FAILED");
    };
    for (const auto entity : {village,smith,tool,first}) learn(first,{entity});
    for (const auto entity : {village,tavern}) learn(second,{entity});
    for (const auto entity : {village,smith,tool}) learn(first,{entity,core::FactKind::definition});
    for (const auto key : {core::FactKey{tool,core::FactKind::containment}, {village,core::FactKind::population},
            {smith,core::FactKind::population}, {village,core::FactKind::relation,service,smith}, {first,core::FactKind::population_origin}})
        learn(first,key);
    require(core::Inspector{world}.diagnose().valid() &&
        core::Persistence::validate(core::Persistence::capture(world,candidate->random),persistence_limits()) == core::PersistenceStatus::success,"CONTENT_BOOTSTRAP_FAILED");
    return candidate;
}
} // namespace v001
