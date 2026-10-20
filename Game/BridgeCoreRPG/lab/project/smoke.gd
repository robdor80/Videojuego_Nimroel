extends SceneTree

func _initialize() -> void:
    var result: String = preload("res://probe.gd").verify()
    print(result)
    quit(0 if result.begins_with("NIM06_CORE_OPERATION_OK") else 1)
