extends SceneTree
## Export control: mount actual Windows PCK, or APK content-only ZIP extracted by driver.
func _initialize() -> void:
	var args := OS.get_cmdline_user_args()
	if args.size() != 1 or not ProjectSettings.load_resource_pack(args[0], true):
		quit(1)
		return
	var loaded: Dictionary = preload("res://scripts/v001_pack.gd").read_bundle()
	if loaded.status != "ok":
		quit(1)
		return
	var host: RefCounted = ClassDB.instantiate("CoreRPGHost")
	var initialized: Dictionary = host.call("initialize_v001", {"api_version": 1, "files": loaded.files})
	print("NIM07_PACK_REPORT " + JSON.stringify({"ok": initialized.status == "ok", "files": loaded.files.size(), "source": args[0].get_file(), "android_device_execution": false}))
	quit(0 if initialized.status == "ok" else 1)
