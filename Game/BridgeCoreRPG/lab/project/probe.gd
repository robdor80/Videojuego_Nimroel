extends RefCounted

static func verify() -> String:
    if not ClassDB.class_exists("CoreRPGLab"):
        return "FAIL: CoreRPGLab not registered"
    var bridge = ClassDB.instantiate("CoreRPGLab")
    if bridge == null or not bridge.has_method("parse_core_version"):
        return "FAIL: native method unavailable"
    for item in [["4.7.2", 4, 7, 2], ["12.34.56", 12, 34, 56], ["0.0.0", 0, 0, 0]]:
        var result: Dictionary = bridge.call("parse_core_version", item[0])
        if result != {"valid": true, "major": item[1], "minor": item[2], "patch": item[3]}:
            return "FAIL: CoreRPG parse mismatch: " + str(result)
    for text in ["01.2.3", "bad", "4294967296.0.0", "1.2.3.4", ""]:
        if bridge.call("parse_core_version", text) != {"valid": false}:
            return "FAIL: CoreRPG accepted invalid input: " + text
    return "NIM06_CORE_OPERATION_OK cases=8"
