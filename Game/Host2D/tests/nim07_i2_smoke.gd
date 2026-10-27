extends SceneTree
## Editor/runtime entry; exported template uses --nim07-i2-self-test.
func _initialize() -> void:
	_run.call_deferred()
func _run() -> void:
	var checks := preload("res://tests/nim07_i2_checks.gd").new()
	await checks.run(self)
