#!/usr/bin/env python3
"""E20-P00: audita que NO se declare paridad falsa con Valrik/Treskal.

Valida la coherencia de un acta de preflight. No acredita por sí mismo
mapa métrico, calidad narrativa, NPC, contenido cargado ni runtime.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
T = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios"
E = T / "Casa Edranor"
V = T / "Casa Valrik"
A = E / "Datos operativos/edranor_e20_parity_gate_v0.1.json"
V_MAP = V / "Treskal/Datos operativos/treskal_canonical_map_contract_v1.0.json"
E18 = E / "Datos operativos/edranor_e18_maturity_audit_v0.1.json"
E07 = E / "Datos operativos/edranor_e07_canonical_nuclei_v0.1.json"

class GateError(ValueError):
    pass

def require(ok: bool, what: str) -> None:
    if not ok:
        raise GateError(what)

def unique_pairs(pairs: list) -> dict:
    d = {}
    for k, v in pairs:
        require(k not in d, "clave JSON duplicada: " + k)
        d[k] = v
    return d

def read(path: Path) -> dict:
    with path.open(encoding="utf-8-sig") as f:
        return json.load(f, object_pairs_hook=unique_pairs)

def verify(g: dict, v: dict, e18: dict, e07: dict) -> None:
    require(g.get("schemaVersion") == 1 and
            g.get("documentId") == "edranor_e20_valrik_parity_preflight" and
            g.get("version") == "0.1" and g.get("phase") == "E20-P00",
            "identidad del registro")
    require(g.get("date") == "2026-11-14" and
            g.get("referenceMainSha") == "223f1e49adfbc73be6a80c6ce36e7aab506450c2",
            "fecha/commit de corte")
    require(g.get("authority") == "AUTHOR_2026_11_14_QUALITY_MANDATE" and
            g.get("scope") == "NON_CANONICAL_QUALITY_GATE_NO_RUNTIME" and
            g.get("status") == "PARITY_NOT_ACCREDITED",
            "autoridad y dictamen")
    for k, val in {
        "parityCertified": False,
        "cityDorthCompleted": False,
        "metricMapAccepted": False,
        "rejectedE19ReuseForbidden": True,
        "noRuntimeChanges": True,
        "noCoreChanges": True,
    }.items():
        require(type(g.get(k)) is type(val) and g[k] == val, "promoción falsa: " + k)
    require(type(g.get("rejectedE19PR")) is int and
            g["rejectedE19PR"] == 84, "E19 #84 debe seguir descartada")

    require(v["cityId"] == "treskal" and
            v["coordinateReference"] == "TRESKAL_LOCAL_METRIC_V1" and
            v["spatialExport"]["featureCount"] == 2404 and
            v["spatialExport"]["layers"]["ordinary_parcel"] == 2175 and
            v["parcelMaterialization"]["geometryNowCanonical"] is True,
            "referencia Valrik/Treskal alterada")
    require(e18["phase"] == "E18" and len(e18["dimensions"]) == 10 and
            all(d["level"] == "B2" and
                d["materialEvidenceValidated"] is False and
                d["runtimeValidated"] is False for d in e18["dimensions"]),
            "evidencia E18, no B3 ni B4")
    require(e07["scope"]["designedCanonicalNuclei"] == 4 and
            e07["scope"]["instantiatedCanonicalNuclei"] == 0 and
            e07["scope"]["georeferenced"] is False and
            e07["scope"]["physicalRoadGraphValidated"] is False and
            e07["scope"]["householdsInstantiated"] == 0 and
            e07["scope"]["buildingsInstantiated"] == 0 and
            e07["scope"]["npcInstantiated"] == 0,
            "materialización E07 distinta del corte auditado")

    se = g["sourceEvidence"]
    require(se["valrikTreeSha"] == "fe9795fd68b71dc5c7c9989266ec08e33d4520bd" and
            se["edranorTreeSha"] == "f0f5472c4d24de6544632fc70a969fdf52b67911",
            "árboles Git de referencia")
    require(se["valrik"] == {"totalFiles": 437, "md": 298, "json": 135,
                             "geojson": 1, "svg": 3} and
            se["edranor"] == {"totalFiles": 202, "md": 180, "json": 21,
                              "geojson": 0, "svg": 1},
            "inventario de evidencia de referencia")
    require(se["treskal"] == {"coordinateReference": "TRESKAL_LOCAL_METRIC_V1",
                               "geojsonFeatureCount": 2404, "urbanBlocks": 110,
                               "ordinaryParcels": 2175, "metricsPlanPointsClosed": 10},
            "referencia cartográfica incompleta")
    require(se["edranorMaturity"] == {"dimensionsAtB2": 10,
                                      "dimensionsAtB3": 0,
                                      "dimensionsAtB4": 0},
            "madurez no acreditada")

    actual = {x["id"]: x["jurisdictionOwner"] for x in e07["settlements"]}
    declared = {x["id"]: x["authority"] for x in g["canonicalAnchors"]}
    require(len(g["canonicalAnchors"]) == 5 and
            len(declared) == 5 and
            list(declared) == ["dorth", "lumina", "karsath", "rodas", "hallheim"],
            "orden y cardinalidad anclas")
    for id in ["dorth", "lumina", "karsath", "rodas"]:
        require(declared[id] == actual[id], "jurisdicción ancla: " + id)
    require(declared["rodas"] == "crown_aethros" and
            declared["hallheim"] == "outside_edranor",
            "Rodas Corona y Hallheim exterior")

    expected_debts = [f"EDD-{i:02d}" for i in [1,2,3,4,5,7,8]]
    require(g["blockedDebts"] == expected_debts and
            g["designOnlyDebt"] == ["EDD-06"], "deuda EDD alterada")
    source_debts = {x["id"]: x["status"] for x in e18["debts"]}
    require(all(source_debts[x] == "OPEN" for x in expected_debts) and
            source_debts["EDD-06"] == "RESOLVED_FOR_DESIGN",
            "deuda contradice E18")

    gates = g["gates"]
    require(len(gates) == 16 and
            [x.get("id") for x in gates] == [f"P20-{n:02d}" for n in range(1, 17)],
            "16 puertas de aceptación")
    require(all(x.get("achieved") is False and x.get("requirement") and
                x.get("scope") and x.get("blocks") for x in gates),
            "ninguna puerta P20 puede declararse superada en este preflight")
    require(set(x for y in gates for x in y["blocks"]) == {"B3", "B4"},
            "distinción entre B3 y B4")
    require(g["nextPhases"]["E19_R"] == "REQUIRED_NEW_WORK_NOT_E19_84" and
            g["nextPhases"]["E20_Dorth"] == "P00_ONLY_NOT_ACCEPTED" and
            g["nextPhases"]["E30_PLUS"] == "CONDITIONAL_NO_FORCED_END",
            "plan E19-R y E20 bloqueados")
    require(set(g["falseClaimsForbidden"]) >= {
        "rejected_e19_reuse", "fictitious_georeference",
        "physical_road_edge_from_need_graph", "rodas_edranor_tax_or_berseker_command",
        "hallheim_within_house", "lumina_monthly_fair",
        "karsath_urban_harbor_without_source",
        "bosque_alto_unlicensed_logging", "u7_viticulture_certified",
        "synthetic_event_as_occurred", "core_smoke_as_godot_playability",
    }, "prohibiciones esenciales")
    require(g["conclusion"] == "BLOCKED_MATERIAL_PARITY; NO_CLAIM_OF_EDRANOR_TERRITORIAL_COMPLETION",
            "conclusión engañosa")
    docs = [
        "E20/00_AUDITORIA_COMPARADA_VALRIK_EDRANOR.md",
        "E20/01_CONTRATO_DE_CALIDAD_Y_ACEPTACION_DORTH.md",
        "E20/02_REPLANIFICACION_SIN_CIERRE_FORZADO.md",
    ]
    require(g["docs"] == docs and all((E / p).is_file() for p in docs),
            "documentación de preflight ausente")
    for p in docs:
        txt = (E / p).read_text(encoding="utf-8")
        require("Valrik" in txt and len(txt) > 1500,
                "documento de paridad incompleto: " + p)
    require(not (E / "E19").exists(),
            "E19 descartada no puede materializarse en este árbol")

def negatives(g: dict, v: dict, e18: dict, e07: dict) -> int:
    def expect_reject(mutator, label):
        bad = copy.deepcopy(g)
        mutator(bad)
        try:
            verify(bad, v, e18, e07)
        except GateError:
            return
        raise GateError("caso adversarial aceptado: " + label)

    cases = [
        ("falsa paridad", lambda x: x.update(parityCertified=True)),
        ("cierre falso de Dorth", lambda x: x.update(cityDorthCompleted=True)),
        ("aceptación del mapa rechazado", lambda x: x.update(metricMapAccepted=True)),
        ("reusar E19 #84", lambda x: x.update(rejectedE19ReuseForbidden=False)),
        ("alterar PR E19", lambda x: x.update(rejectedE19PR=85)),
        ("inflar madurez", lambda x: x["sourceEvidence"]["edranorMaturity"].update(dimensionsAtB3=1)),
        ("forzar dato geográfico", lambda x: x["sourceEvidence"]["edranor"].update(geojson=1)),
        ("Rodas subordinada a la Casa", lambda x: x["canonicalAnchors"][3].update(authority="casa_edranor")),
        ("Hallheim dentro", lambda x: x["canonicalAnchors"][4].update(authority="casa_edranor")),
        ("cerrar EDD-01", lambda x: x["blockedDebts"].remove("EDD-01")),
        ("P20-01 falsa", lambda x: x["gates"][0].update(achieved=True)),
        ("suprimir B4", lambda x: x["gates"][13].update(blocks=["B3"])),
        ("fingir E20 terminado", lambda x: x["nextPhases"].update(E20_Dorth="DONE")),
        ("perder rechazo a E19", lambda x: x["falseClaimsForbidden"].remove("rejected_e19_reuse")),
        ("cambiar SHA de fuente", lambda x: x.update(referenceMainSha="0"*40)),
        ("quitar doc", lambda x: x["docs"].pop()),
    ]
    for name, callback in cases:
        expect_reject(callback, name)
    return len(cases)

def main() -> None:
    v, e18, e07, g = (read(p) for p in (V_MAP, E18, E07, A))
    verify(g, v, e18, e07)
    n = negatives(g, v, e18, e07)
    print(f"E20-P00 PASS: acta bloqueada, 16 puertas no acreditadas; {n} mutaciones rechazadas.")
    print("IMPORTANTE: esto NO certifica E20, geometría, NPC ni runtime.")

if __name__ == "__main__":
    main()
