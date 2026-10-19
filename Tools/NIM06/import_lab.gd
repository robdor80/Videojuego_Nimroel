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
    print("NIM06_EDITOR_IMPORT_OK")
    quit(0)
