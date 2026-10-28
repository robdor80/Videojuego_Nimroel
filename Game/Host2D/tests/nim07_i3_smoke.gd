extends SceneTree
## Mismo cuerpo que el EXE exportado con --nim07-i3-self-test.
func _initialize() -> void:
	_run.call_deferred()
func _run() -> void:
	var checks := preload("res://tests/nim07_i3_checks.gd").new()
	await checks.run(self)
