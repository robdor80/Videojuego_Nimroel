@tool
extends SceneTree

# A frame limit starts before the first scan finishes. Wait for the actual editor
# filesystem instead, then drain deferred documentation while classes still exist.
func _initialize() -> void:
    finish_import.call_deferred()

func finish_import() -> void:
    var filesystem := EditorInterface.get_resource_filesystem()
    var deadline := Time.get_ticks_msec() + 120000
    var quiet_frames := 0
    while quiet_frames < 30:
        await process_frame
        quiet_frames = 0 if filesystem.is_scanning() else quiet_frames + 1
        if Time.get_ticks_msec() > deadline:
            printerr("NIM06_EDITOR_IMPORT_TIMEOUT")
            quit(1)
            return
    # Public editor API: opening native help joins EditorHelp's documentation
    # worker (go_to_help -> _wait_for_thread). Drain its queued extension-doc
    # callbacks before teardown; a completed filesystem scan alone is insufficient.
    EditorInterface.get_script_editor().goto_help("class_name:RefCounted")
    await process_frame
    await process_frame
    print("NIM06_EDITOR_IMPORT_OK")
    quit(0)
