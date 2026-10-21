#!/usr/bin/env python3
"""Validación estática D01 Darovan, sin dependencias externas ni runtime."""
from __future__ import annotations
import json
import sys
from pathlib import Path


def run() -> None:
    here = Path(__file__).resolve()
    repo = next((p for p in here.parents if (p / "Worldbuilding").is_dir()), None)
    if repo is None:
        raise AssertionError("No se encuentra la raíz del repositorio")
    base = here.parents[1]
    raw = (base / "Datos operativos" / "darovan_d01_relief_profile_v0.1.json").read_text(encoding="utf-8")
    data = json.loads(raw)
    def check(cond: bool, message: str) -> None:
        if not cond:
            raise AssertionError(message)
    check(data["schemaVersion"] == 1 and data["status"] == "planning_reference_not_runtime", "estado")
    check(data["authorityChain"] == ["nimroel_core", "norgard_defaults", "casa_darovan", "locality", "world_state"], "autoridad")
    check(not any(data[k] for k in ("containsBorders", "containsCoordinates", "containsElevations", "containsRuntimeAssets")), "geometría")
    units = data["physicalUnits"]
    cities = data["cityAnchors"]
    check(len(units) == 12 and len({u["id"] for u in units}) == 12, "IDs unidades")
    check(len(cities) == 4 and {c["id"] for c in cities} == {"treihord", "veldora", "taramin", "syvaris"}, "cuatro ciudades")
    check(all(c["adminOwner"] == "casa_darovan" and c["kind"] == "manually_authored_city" for c in cities), "ciudades manuales")
    a = data["administration"]
    check(a["excludedCity"] == "karsath" and a["arvenIslandOwner"] == "casa_darovan", "Karsath/Arven")
    check(a["syvarisIslandOwner"] == "casa_darovan" and a["redMapMarkupIsLegalBorder"] is False, "Syvaris/línea roja")
    assert next(u for u in units if u["id"] == "d01_arven_contexto")["administrativeOwner"] == "casa_darovan"
    assert next(u for u in units if u["id"] == "d01_syvaris")["administrativeOwner"] == "casa_darovan"
    h = data["lockedHydroAnchors"]
    check(h["belara"]["crossesCity"] is False and h["belara"]["mouth"] == "golfo_de_norgard", "Belara")
    check(h["belara"]["portNearTreihord"] == "industrial_shallow_draft", "puerto Treihord")
    check(h["lhera"]["branchesFrom"] == "belara" and h["lhera"]["mouth"] == "golfo_de_veldora", "Lhera")
    check({"belara", "lhera"} <= set(h["veldora"]["independentOf"]), "Veldora independiente")
    check(h["fhalion"]["independentRiver"] is True and h["fhalion"]["sourceKnown"] is False
          and h["fhalion"]["mainCourseMouth"] is None, "Fhalion de autor, sin boca falsa")
    check(h["thalen"]["terminalArms"] == 2 and h["thalen"]["cityBetweenArms"] == "taramin", "Thalen")
    check(all(u["classification"] == "qualitative_working_area_not_canonical_boundary" for u in units), "unidades no canónicas")
    references = {data["referenceCoreContract"]}
    for u in units:
        references.update(u["sourcePaths"])
    for c in cities:
        references.update(c["sourcePaths"])
    for river in h.values():
        references.add(river["source"])
    check(len(references) >= 12, "fuentes insuficientes")
    for source in sorted(references):
        check((repo / source).is_file(), f"Fuente ausente: {source}")
    for doc in (
        "Geografia_local/01_marco_fisico_y_orografia_v0.1.md",
        "Geografia_local/02_subzonas_y_corredores_cualitativos_v0.1.md",
        "Geografia_local/03_perfil_operativo_del_relieve_v0.1.md",
        "Cartografia/01_dependencias_cartograficas_D01_v0.1.md",
        "Validacion/D01_MATRIZ_INVARIANTES_Y_PRUEBAS_v0.1.md",
        "Auditorias/D01_CIERRE_Y_VALIDACION_2026-10-15.md",
        "00_Control_del_proyecto/TRASPASO_D02.md",
    ):
        check((base / doc).is_file(), f"Documento D01 ausente: {doc}")
    check(data["runtimeIntegration"]["validatedInGame"] is False, "runtime")
    check(data["runtimeIntegration"]["generatedEntities"] == 0, "generación")
    print(f"D01 STATIC OK: 12 unidades, 4 ciudades, {len(references)} fuentes, sin runtime")


if __name__ == "__main__":
    try:
        run()
    except (AssertionError, ValueError, KeyError) as exc:
        print(f"D01 STATIC FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
