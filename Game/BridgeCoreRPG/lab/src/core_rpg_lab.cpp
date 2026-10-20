#include <corerpg/semantic_version.hpp>
#include <godot_cpp/classes/ref_counted.hpp>
#include <godot_cpp/core/class_db.hpp>
#include <godot_cpp/godot.hpp>
#include <godot_cpp/variant/dictionary.hpp>
#include <godot_cpp/variant/char_string.hpp>
#include <string_view>

// Translation only: CoreRPG owns validation and parsing. No world state or rules here.
class CoreRPGLab : public godot::RefCounted {
    GDCLASS(CoreRPGLab, godot::RefCounted)
protected:
    static void _bind_methods() {
        godot::ClassDB::bind_method(godot::D_METHOD("parse_core_version", "text"),
                                   &CoreRPGLab::parse_core_version);
    }
public:
    godot::Dictionary parse_core_version(const godot::String &text) const {
        const auto utf8 = text.utf8();
        const auto parsed = corerpg::SemanticVersion::parse(
            std::string_view(utf8.get_data(), static_cast<std::size_t>(utf8.length())));
        godot::Dictionary result;
        result["valid"] = parsed.has_value();
        if (parsed) {
            result["major"] = static_cast<int64_t>(parsed->major());
            result["minor"] = static_cast<int64_t>(parsed->minor());
            result["patch"] = static_cast<int64_t>(parsed->patch());
        }
        return result;
    }
};

static void initialize_lab(godot::ModuleInitializationLevel level) {
    if (level == godot::MODULE_INITIALIZATION_LEVEL_SCENE) {
        godot::ClassDB::register_class<CoreRPGLab>();
    }
}
static void uninitialize_lab(godot::ModuleInitializationLevel) {}

extern "C" GDExtensionBool GDE_EXPORT nimroel_core_lab_init(
    GDExtensionInterfaceGetProcAddress get_proc_address,
    GDExtensionClassLibraryPtr library, GDExtensionInitialization *initialization) {
    godot::GDExtensionBinding::InitObject init(get_proc_address, library, initialization);
    init.register_initializer(initialize_lab);
    init.register_terminator(uninitialize_lab);
    init.set_minimum_library_initialization_level(godot::MODULE_INITIALIZATION_LEVEL_SCENE);
    return init.init();
}
