extends SceneTree
func _initialize() -> void:
	_run.call_deferred()
func _run() -> void:
	var phase := "write" if OS.get_cmdline_user_args().has("--nim07-i4-write") else "read"
	await preload("res://tests/nim07_i4_checks.gd").new().run(self, phase)
