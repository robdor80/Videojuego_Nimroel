extends Control

func _ready() -> void:
    var result: String = preload("res://probe.gd").verify()
    $Result.text = result + "\nLaboratorio nativo; sin sistemas de juego."
    print(result)
