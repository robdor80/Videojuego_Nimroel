#!/usr/bin/env python3
"""E19-TEC: compila R1–R5 en un catálogo causal *NO materializado*.

No genera aldeas, ríos, caminos, coordenadas, World State ni permisos.
La capa estructural se puede leer en Godot sin otorgarle autoridad de CoreRPG.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from spatial import ROOT, SpatialError, require, read_json

EDR = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
INPUTS = {
    "R1": "E19-R1/natural_features_v0.2.json",
    "R2": "E19-R2/hydrology_v0.3.json",
    "R3": "E19-R3/environment_v0.4.json",
    "R4": "E19-R4/routes_v0.5.json",
    "R5": "E19-R5/occupation_v0.6.json",
}
MFS = [f"MF-{i:02d}" for i in range(1, 8)]
PARENTS = {
    "R1": "REGIONAL_DESIGN_NOT_RUNTIME",
    "R2": "REGIONAL_CAUSAL_DESIGN_B2_NOT_RUNTIME",
    "R3": "REGIONAL_CAUSAL_DESIGN_B2_NOT_RUNTIME",
    "R4": "REGIONAL_CAUSAL_DESIGN_B2_NOT_RUNTIME",
    "R5": "REGIONAL_CAUSAL_OCCUPATION_B2_NOT_RUNTIME",
}
AUTH = "VALRIK_CAUSAL_METHOD_ONLY_NOT_GEOMETRY"
ITEM_TYPES = {
    "soilPrototypes": "soils",
    "microclimateRules": "microclimate",
    "coverMosaics": "cover",
    "resourceChains": "resources",
}


def require_unique(ids: list[str], desc: str) -> None:
    require(len(ids) == len(set(ids)), f"IDs duplicados: {desc}")


def read_inputs() -> dict:
    return {key: read_json(EDR / filename) for key, filename in INPUTS.items()}


def verify_parents(data: dict) -> None:
    require(set(data) == set(INPUTS), "Faltan fases parentales")
    for phase, state in PARENTS.items():
        require(data[phase].get("status") == state, f"Estado alterado {phase}")
    r1, r2, r3, r4, r5 = (data[f"R{i}"] for i in range(1, 6))
    expected = MFS + ["MF-08"]
    for phase, collection in [("R1", r1["physicalRegions"]), ("R3", r3["contexts"]),
                              ("R5", r5["contexts"])]:
        require([x["id"] for x in collection] == expected,
                f"{phase} contexto inconsistente")
    require(r1["physicalRegions"][-1]["evaluable"] is False and
            r3["contexts"][-1]["status"] == "NON_EVALUABLE" and
            r5["contexts"][-1]["nonEvaluable"] is True, "Norte evaluado indebidamente")
    require(r1["geometry"] is None and r1["worldStateEntities"] == 0,
            "R1 no debe materializar")
    require(r2["materialization"]["geometry"] is None and
            r2["materialization"]["worldStateEntities"] == 0 and
            r2["graphContract"]["minorGraphEdges"] == [], "R2 no debe materializar")
    require(r3["maturity"]["b3Mapped"] is False and
            r3["maturity"]["b4Runtime"] is False and
            r3["maturity"]["actualParcels"] == 0, "R3 no debe materializar")
    require(r4["networks"]["acceptedPhysicalGraph"] == {"nodes": [], "edges": []} and
            r4["networks"]["pathfindingEnabled"] is False and
            r4["maturity"]["actualRoads"] == 0, "R4 Gp no acreditada")
    require(r5["maturity"]["actualSettlements"] == 0 and
            r5["maturity"]["actualResidents"] == 0 and
            r5["coverage"]["providerNodeIds"] == [] and
            r5["worldState"]["enabled"] is False, "R5 no debe materializar")
    require(r1["jurisdiction"]["rodas"] == "crown_aethros" and
            r1["jurisdiction"]["rodasType"] == "ALDEA" and
            r1["jurisdiction"]["hallheim"] == "OUTSIDE_EDRANOR" and
            r1["jurisdiction"]["bosqueAltoHarvest"] == "PERMIT_REQUIRED" and
            r1["jurisdiction"]["bosqueReal"] == "crown_aethros",
            "Jurisdicciones R1 alteradas")
    require([x["id"] for x in r2["basinFamilies"]] ==
            [f"HC-{i:02d}" for i in range(1, 8)],
            "Familias hidrológicas inesperadas")
    for i, mf in enumerate(MFS):
        basin = r2["basinFamilies"][i]
        require(basin["contextId"] == mf and basin["status"] == "DESIGN_FAMILY_UNLOCATED"
                and basin["geometry"] is None and basin["receiver"] == "UNKNOWN",
                "Cuenca imaginaria: " + mf)
        require(r3["contexts"][i]["basinId"] == basin["id"],
                "Relación R2-R3 inválida: " + mf)
        require(r5["contexts"][i]["hydrology"] == basin["id"],
                "Relación R2-R5 inválida: " + mf)
    for group in ("soilPrototypes", "microclimateRules", "coverMosaics",
                  "resourceChains", "seasonalRules"):
        require(len(r3[group]) > 0, "R3 carece de " + group)
    require(len(r4["corridorQuestions"]) == 12 and
            all(q["actualRoute"] is False for q in r4["corridorQuestions"]),
            "R4 CT son preguntas, no rutas")
    require(len(r5["studies"]) == 19 and
            all(s["studyOnly"] is True and s["actualSettlement"] is False
                for s in r5["studies"]), "R5 OS son estudios, no aldeas")
    require(all(a["proceduralSpawn"] is False for a in r5["anchors"]),
            "No generar Dorth/Lumina/Karsath/Rodas/Hallheim")
    require({a["id"]: a["jurisdiction"] for a in r5["anchors"]}["rodas"] ==
            "crown_aethros", "Rodas fuera del gobierno Edranor")


def build_catalog(data: dict) -> dict:
    verify_parents(data)
    r1, r2, r3, r4, r5 = (data[f"R{i}"] for i in range(1, 6))
    contexts = []
    for i, mf in enumerate(MFS):
        regions = [x["id"] for x in r1["selectedDesignNames"]
                   if x.get("status") == "SELECTED_DESIGN_NOT_MAPPED"]
        classified: dict = {}
        for parent_field, field in ITEM_TYPES.items():
            possible = []
            for entry in r3[parent_field]:
                membership = entry.get("contextIds")
                if membership is None:
                    membership = [entry["contextId"]] if entry.get("contextId") else []
                if mf in membership:
                    possible.append(entry["id"])
            require_unique(possible, field)
            classified[field] = sorted(possible)
        questions = sorted(q["id"] for q in r4["corridorQuestions"]
                           if mf in q["contextIds"] and q.get("gqOnly") is True)
        studies = sorted(s["id"] for s in r5["studies"]
                         if s["contextId"] == mf and s["studyOnly"] is True)
        contexts.append({
            "contextId": mf,
            "name": r3["contexts"][i]["name"],
            "parentReliefName": r1["physicalRegions"][i]["name"],
            "basinStudyId": r2["basinFamilies"][i]["id"],
            "potentialRuleIds": classified,
            "routeQuestionIds": questions,
            "occupationStudyIds": studies,
            "status": "B2_CAUSAL_STUDY_NOT_PLACED",
            "geometry": None, "area": None,
            "physicalGraphEdges": [], "actualPlaces": [],
            "approvedLandUse": False, "eligibleForWorldState": False,
            "provenance": {
                "relief": "E19-R1/natural_features_v0.2.json",
                "hydrology": "E19-R2/hydrology_v0.3.json",
                "environment": "E19-R3/environment_v0.4.json",
                "roads": "E19-R4/routes_v0.5.json",
                "occupation": "E19-R5/occupation_v0.6.json",
            },
        })
    require(len(contexts) == 7 and
            len(set(c["contextId"] for c in contexts)) == 7,
            "Catálogo no evaluable o incompleto")
    names = sorted({n["id"] for n in r1["selectedDesignNames"]
                    if n["id"] in regions})
    require(len(names) == 6, "Topónimos de diseño alterados")
    payload = {
        "schemaVersion": 1,
        "documentId": "edranor_e19_tec_causal_catalog",
        "method": AUTH,
        "status": "NONMETRIC_B2_CATALOG_NO_RUNTIME",
        "layers": ["RELIEF", "HYDROLOGY", "SOIL_CLIMATE_COVER",
                   "ROUTE_QUESTIONS", "OCCUPATION_STUDIES"],
        "seed": None, "coordinates": None, "worldState": None,
        "unknownRegionIds": ["MF-08"],
        "physicalRouteCount": 0,
        "actualSettlementCount": 0,
        "sourceNameIdsOnlyNotMapped": names,
        "anchors": [
            {"id": a["id"], "kind": a["kind"],
             "jurisdiction": a["jurisdiction"],
             "manual": True, "location": None}
            for a in r5["anchors"]
        ],
        "contexts": contexts,
    }
    raw = json.dumps(payload, sort_keys=True, ensure_ascii=False,
                     separators=(",", ":"), allow_nan=False).encode("utf-8")
    payload["sha256"] = hashlib.sha256(raw).hexdigest()
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Ruta local del catálogo no métrico")
    args = parser.parse_args()
    result = build_catalog(read_inputs())
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    print(f"E19-TEC causal: {len(result['contexts'])} contextos B2, "
          "0 rutas, 0 aldeas, 0 objetos World State.", file=__import__("sys").stderr)


if __name__ == "__main__":
    try:
        main()
    except (SpatialError, KeyError, TypeError, OSError, ValueError) as exc:
        raise SystemExit("E19-TEC catálogo BLOQUEADO: " + str(exc))
