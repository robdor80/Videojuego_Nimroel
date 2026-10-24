#!/usr/bin/env python3
"""D04 Darovan — regresión de economía territorial. Datos de PLANIFICACIÓN, NO RUNTIME."""
from __future__ import annotations
import copy
import json
import sys
from pathlib import Path

CITIES = ["treihord", "veldora", "taramin", "syvaris"]
CHAINS = {
    "d04_mineral_valkram_treihord", "d04_elyra_precious_metals_context",
    "d04_azurios_coal_import", "d04_pilares_wood_to_valkram_mining",
    "d04_treihord_food_supply", "d04_veldora_port_commerce",
    "d04_taramin_fisheries", "d04_syvaris_fisheries_commerce",
}
REFS = ("d01", "d02", "d03", "coreLedger", "norgardFiscal")

def check(yes: bool, message: str) -> None:
    if not yes:
        raise AssertionError(message)

def read(repo: Path, rel: str) -> dict:
    return json.loads((repo / rel).read_text(encoding="utf-8"))

def validate(d: dict, repo: Path) -> None:
    check(d["schemaVersion"] == 1 and d["documentId"] == "darovan_d04_resources_production_economy"
          and d["phase"] == "D04" and d["status"] == "planning_reference_not_runtime", "phase / status")
    check(d["canonStatus"] == "source_traced_no_new_canon", "canon status")
    check(d["authorityChain"] == ["nimroel_core", "norgard_defaults", "casa_darovan", "locality", "world_state"], "authority")
    check(d["sourceHierarchy"] == ["AUTHORED", "DERIVED", "GENERATED", "DYNAMIC", "UNKNOWN"], "source hierarchy")
    check(d["evidenceLabels"] == ["AUTHORED", "DERIVED", "PROPOSAL", "UNKNOWN"], "provenance classes")
    check(all(v is False for k, v in d.items() if k.startswith("contains")), "invented data / features")

    refs = d["sourceRefs"]
    check(len(refs) >= 19, "insufficient original reference paths")
    check(all(p.startswith("Worldbuilding/") and (repo / p).is_file() for p in refs.values()), "missing source on checkout")
    check(d["referenceD01Relief"] == refs["d01"] and d["referenceD02Hydro"] == refs["d02"]
          and d["referenceD03Climate"] == refs["d03"] and d["referenceCoreLedger"] == refs["coreLedger"]
          and d["referenceFiscalDefault"] == refs["norgardFiscal"], "broken reference links")
    relief, hydro, climate, ledger, fiscal = (read(repo, refs[n]) for n in REFS)
    check(ledger["status"] == "active_core_contract", "Core ledger not active")
    check(fiscal["fiscalUnity"]["customsBetweenGreatHouseTerritories"] is False
          and fiscal["fiscalUnity"]["crossingGreatHouseBoundaryAloneCreatesCustomsDuty"] is False, "Norgard default customs")
    check(fiscal["portRules"]["localFishingCatchIsNotExternalCustomsImport"] is True, "port fiscal policy")
    check(ledger["immutableRules"]["ledgerEntryDoesNotCreatePayment"] is True, "Core physical transaction")

    ids = [x["id"] for x in d["studyUnits"]]
    check(len(ids) == len(set(ids)) == 12, "unique D01 study zones")
    check(set(ids) == {x["id"] for x in relief["physicalUnits"]}
          == {x["id"] for x in climate["zones"]}, "D01/D03 cross-phase unit IDs")
    for unit in d["studyUnits"]:
        check(unit["classification"] == "qualitative_study_unit_not_polygon", "fake zone polygons")
        check(all(unit[n] is None for n in (
            "newExtractiveSites", "agriculturalYield", "livestockCount", "stockVolume",
            "harvestRate", "agriculturalLandArea", "waterAvailable")), "invented quantitative zone")
    chains = d["resourceChains"]
    check(len(chains) == len(CHAINS) and {c["id"] for c in chains} == CHAINS, "resource chains")
    for chain in chains:
        check(chain["provenance"] == "AUTHORED" and bool(chain["sourceRefIds"])
              and all(k in refs for k in chain["sourceRefIds"]), "chain provenance")
        check(bool(chain["documentedSteps"]) and set(chain["zoneIds"]).issubset(ids), "chain zone IDs")
        check(chain["producerIds"] == [] and all(chain[n] is None for n in (
            "quantity", "capacity", "annualYield", "geometry")), "invented producers, yields or route")
        check(bool(chain["explicitUnknowns"]), "missing uncertainties")
    plants = {x["id"]: x for x in d["facilityAnchors"]}
    check(set(plants) == {"treihord_industrial_port", "treihord_industrial_stores", "crisol",
                          "vena", "veldora_commercial_port", "taramin_fishing_port", "syvaris_safe_port"}, "invented facility")
    check(all(v["city"] in CITIES and v["provenance"] == "AUTHORED" for v in plants.values()), "facility provenance")
    check(plants["crisol"]["coinMint"] is False and plants["vena"]["publicCargoRoute"] is False, "Crisol / Vena")
    ports = {x["city"]: x for x in d["marineFunctions"]}
    check(set(ports) == {"veldora", "taramin", "syvaris"}, "ports/cities")
    check("whale_oil_function" in ports["taramin"]["identity"]
          and ports["taramin"]["thalenNavigability"] is None, "Taramin authored function or Thalen invented")
    check(ports["syvaris"]["freshwaterSufficiency"] is None, "Syvaris water invent")
    check(all(p["newFishingSpecies"] is None for p in ports.values()), "species invent")

    f = d["forestProtection"]
    check(f["agujasPermanentInteriorSettlementsAllowed"] is False
          and f["pilaresSingleForest"] is True and f["taraminSingleForest"] is True
          and f["taraminIndustrialLoggingAllowed"] is False
          and f["syvarisForestDiscontinuous"] is True
          and f["syvarisIntensiveForestryAllowed"] is False
          and f["lindeMajorIndustrialLoggingAuthored"] is False
          and f["arvenAdministrativeOwner"] == "casa_darovan", "forest / Arven")
    g = d["geographyProtection"]
    check(g["manualCities"] == CITIES and g["excludedCity"] == "karsath"
          and g["arvenOwner"] == "casa_darovan", "city or ownership regression")
    check(g["belaraAdjacentCity"] == "treihord" and g["belaraCrossesCity"] is False
          and g["belaraNavigation"] == "industrial_shallow_draft_only", "Belara navigability")
    check(g["lheraBranchesFrom"] == "belara"
          and g["veldoraRiverIndependentOf"] == ["belara", "lhera"]
          and g["thalenTerminalArms"] == 2
          and g["thalenCityBetween"] == "taramin" and g["thalenPerennialStatus"] == "UNKNOWN"
          and g["newMinorRivers"] is False
          and g["namedRivers"] == ["belara", "lhera", "veldora", "fhalion", "thalen"]
          and g["fhalionMouthNamed"] is False, "D02 hydro protection")
    check([r["id"] for r in hydro["rivers"]] == ["belara", "lhera", "veldora", "fhalion", "thalen"]
          and hydro["rivers"][0]["crossesCity"] is False
          and hydro["rivers"][1]["branchesFrom"] == "belara"
          and hydro["rivers"][4]["terminalArms"] == 2, "D02 source regression")
    check(climate["regionalAnchors"]["pilaresOneForest"]
          and climate["regionalAnchors"]["taraminOneForest"]
          and climate["regionalAnchors"]["arvenOwner"] == "casa_darovan", "D03 source regression")

    r = d["resourceSourceProtection"]
    check(r["treihordCoalSource"] == "montes_azurios"
          and r["valkramCoalDepositAuthored"] is False
          and r["treihordPreciousMetalMinesSource"] == "montes_valkram"
          and r["elyraHasPreciousMetals"] is True
          and r["elyraDarovanMineConfirmed"] is False
          and r["pilaresTimberSuppliesValkramMines"] is True, "coal / mineral / wood")
    check(all(r[n] is None for n in (
        "coalRouteGeometry", "siteCoordinates", "metalMineCounts", "coalInventoryAmount",
        "harvestYield", "forestRegenerationTime", "fishingQuota")), "unsupported numbers or sites")
    econ = d["fiscalCompatibility"]
    check(econ["internalCustomsBetweenGreatHouses"] is False
          and econ["universalRetailSalesTax"] is False
          and econ["crownSupremeFiscalAuthority"] is True
          and econ["crownOnlyOfficialMint"] is True and econ["crisolIsMint"] is False, "fiscal sovereignty / mint")
    check(econ["accountingUnit"] == "clavo" and econ["clavosPerLuna"] == 24
          and econ["clavosPerCorona"] == 480 and econ["specificLocalTaxRates"] is None, "currency or rates")
    check(econ["authorizedPortServiceFeesRequireActualService"]
          and econ["localCatchIsForeignImport"] is False
          and econ["assetMovementRequiresRealHoldings"]
          and econ["ledgerDoesNotCreatePayment"], "transaction semantics")
    check(len(d["hypotheticalDependencies"]) == 5 and all(
        s["status"] == "hypothetical_not_historical_event"
        and s["neededData"] for s in d["hypotheticalDependencies"]), "fictitious disasters")

    a, runtime = d["approvals"], d["runtimeIntegration"]
    check(a["newCanonApproved"] is False and set(a["pendingAuthor"]) ==
          {"DAR-P04", "DAR-P08", "DAR-P09", "DAR-P10", "DAR-P11"}, "author approval")
    check(runtime == {"status":"not_implemented", "validatedInGodot":False,
                      "validatedWithCoreRPG":False, "generatedProductionEntities":0,
                      "executedTransactions":0, "persistedStockLedger":False}, "runtime claim")

def run() -> None:
    file = Path(__file__).resolve()
    repo = next((p for p in file.parents if (p / "Worldbuilding").is_dir()), None)
    check(repo is not None, "repository root not found")
    document = file.parents[1] / "Datos operativos/darovan_d04_resources_production_v0.1.json"
    d = json.loads(document.read_text(encoding="utf-8"))
    validate(d, repo)
    mutations = [
        ("arven_owner_erased", lambda x: x["geographyProtection"].update(arvenOwner=None)),
        ("unknown_mine", lambda x: x["studyUnits"][0].update(newExtractiveSites=["mine1"])),
        ("production_yield", lambda x: x["resourceChains"][0].update(annualYield=250)),
        ("coal_from_valkram", lambda x: x["resourceSourceProtection"].update(treihordCoalSource="montes_valkram")),
        ("fhalion_mouth_invented", lambda x: x["geographyProtection"].update(fhalionMouthNamed=True)),
        ("belara_through_city", lambda x: x["geographyProtection"].update(belaraCrossesCity=True)),
        ("lhera_wrong_source", lambda x: x["geographyProtection"].update(lheraBranchesFrom="veldora")),
        ("veldora_join", lambda x: x["geographyProtection"].update(veldoraRiverIndependentOf=[])),
        ("thalen_one_arm", lambda x: x["geographyProtection"].update(thalenTerminalArms=1)),
        ("pilares_two_forests", lambda x: x["forestProtection"].update(pilaresSingleForest=False)),
        ("industrial_taramin_logging", lambda x: x["forestProtection"].update(taraminIndustrialLoggingAllowed=True)),
        ("inside_agujas", lambda x: x["forestProtection"].update(agujasPermanentInteriorSettlementsAllowed=True)),
        ("crisol_mints", lambda x: x["fiscalCompatibility"].update(crisolIsMint=True)),
        ("interhouse_customs", lambda x: x["fiscalCompatibility"].update(internalCustomsBetweenGreatHouses=True)),
        ("species_invent", lambda x: x["marineFunctions"][0].update(newFishingSpecies=["invented"])),
        ("route_geometry", lambda x: x["resourceSourceProtection"].update(coalRouteGeometry={"km":15})),
        ("runtime_claim", lambda x: x["runtimeIntegration"].update(validatedInGodot=True)),
    ]
    for name, change in mutations:
        candidate = copy.deepcopy(d)
        change(candidate)
        try:
            validate(candidate, repo)
        except (AssertionError, KeyError, TypeError):
            continue
        raise AssertionError("UNDETECTED NEGATIVE TEST: " + name)
    print(f"D04 STATIC OK: {len(d['studyUnits'])} zones, "
          f"{len(d['resourceChains'])} chains, {len(d['sourceRefs'])} sources, "
          f"{len(mutations)} negative tests; NOT RUNTIME")

if __name__ == "__main__":
    try:
        run()
    except (AssertionError, KeyError, TypeError, ValueError, OSError) as exc:
        print("D04 STATIC FAIL: " + str(exc), file=sys.stderr)
        sys.exit(1)
