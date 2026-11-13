"""GALDREN G05: validación documental y mutaciones negativas sin runtime.
Los contratos G00-G04 son históricos: sus valores anteriores de Forja NO
definen la jurisdicción vigente tras la ratificación autoral de G05.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
N = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard"
H = N / "Territorios/Casa Galdren"
D = H / "Datos operativos"


def load(filename: str) -> dict:
    return json.loads((D / filename).read_text(encoding="utf-8"))


G0 = load("galdren_g00_manifest_v0.1.json")
G1 = load("galdren_g01_geography_v0.1.json")
G2 = load("galdren_g02_hydrology_v0.1.json")
G3 = load("galdren_g03_climate_soils_ecosystems_v0.1.json")
G4 = load("galdren_g04_agriculture_livestock_food_v0.1.json")
G5 = load("galdren_g05_mining_industry_forge_v0.1.json")

RESOURCES = ["pizarra", "hierro", "carbon", "cobre", "metal_estelar"]
FOCUS = [
    "SOURCE_REGION_ONLY", "SHARED_NO_GRANT", "GOVERNS_ZANTHIR_NOT_FORGE",
    "ICE_REGION_NO_PORT", "NO_MINES_INFERRED", "TOOLS_DEMAND_STUDY",
    "NO_NAVIGATION_INFERRED", "NO_MINE_FOREST", "NO_MINE_FOREST",
    "NO_MINE_RIPARIAN", "OUTSIDE_HOUSE", "NO_NEW_RIGHTS",
]
PROCESSES = [
    "EXTRACTION_STUDY", "SORTING_AND_STOCK_STUDY", "FUEL_HEAT_STUDY",
    "ORDINARY_SMELTING_STUDY", "TOOL_MANUFACTURING_STUDY",
    "WEAPON_MANUFACTURING_STUDY", "ROYAL_FORGE_INTERFACE_STUDY",
]
FLOWS = [
    ("montes_azurios", "zanthir", "ORDINARY_MATERIALS_STUDY"),
    ("arleon", "zanthir", "FOOD_FOR_WORKERS_STUDY"),
    ("zanthir", "arleon", "TOOLS_FOR_RURAL_STUDY"),
    ("zanthir", "hallheim", "ORDINARY_ARMS_STUDY"),
    ("montes_azurios", "forja_estelar", "STELLAR_METAL_PROVENANCE_STUDY"),
    ("forja_estelar", "zanthir", "ROYAL_SERVICE_INTERFACE_STUDY"),
]
RISKS = [
    "VORNARSK_FREEZE", "KELDARSK_FREEZE", "ZANTHIR_BAY_ICE",
    "MINE_ACCIDENT_HYPOTHESIS", "INDUSTRIAL_FIRE_HYPOTHESIS",
    "POLLUTION_HYPOTHESIS", "FUEL_INTERRUPTION_HYPOTHESIS",
    "FOOD_SUPPLY_INTERRUPTION_HYPOTHESIS", "STELLAR_METAL_THEFT_HYPOTHESIS",
    "ROYAL_FORGE_ACCESS_BREACH_HYPOTHESIS",
]
QUESTIONS = [
    "EXACT_AZURIOS_MINE_SITES", "AZURIOS_PROPERTY_AND_LICENCES",
    "ZANTHIR_WORKSHOP_LOCATIONS", "GEOLEGAL_FORGE_PERIMETER",
    "FORGE_ROYAL_ACQUISITION_HISTORY", "FORGE_ACCESS_AND_SECURITY_PROTOCOL",
    "FORGE_OPERATION_AND_RECIPES", "DWARF_WARS_CANON_RECONCILIATION",
    "REAL_INVENTORIES_AND_CAPACITIES", "VERIFIED_ROUTES_AND_FLOWS",
    "COAL_SUPPLY_CONTRACTS", "PERMIT_AND_TAX_RATES",
]


def ordered_ids(rows: list, prefix: str, size: int) -> None:
    assert isinstance(rows, list)
    assert [row["id"] for row in rows] == [
        f"{prefix}{i:02d}" for i in range(1, size + 1)
    ]


def fields_equal(obj: dict, fields: list[str], value: object) -> None:
    for key in fields:
        assert key in obj, "Campo ausente: " + key
        assert obj[key] == value and type(obj[key]) is type(value), (
            f"Alteración del contrato: {key}: {obj[key]!r}"
        )


def validate(x: dict) -> None:
    assert x["schemaVersion"] == 1
    assert x["documentId"] == "galdren_g05_mining_industry_forge"
    assert x["phase"] == "G05" and x["version"] == "0.1.0"
    assert x["date"] == "2026-11-13"
    assert x["baselineMainSha"] == "b003eaf5a9a4eaeaf5d952b4929db5b439ff99ac"
    assert x["baseDocumentId"] == G4["documentId"] == "galdren_g04_agriculture_livestock_food"
    assert x["status"] == "DOCUMENTARY_PLANNING_ONLY"
    assert x["runtimeEnabled"] is False
    assert x["authorApproval"] == "G05_ROYAL_FORGE_DOMAIN_CANON_RATIFIED_REST_STUDY"
    assert x["inheritance"] == G4["inheritance"] == G0["inheritance"]

    # Regresión referencial sin reescribir los archivos fuente ya fusionados.
    assert G0["locations"][2]["id"] == "forja_estelar"
    assert G0["locations"][2]["jurisdictionOwner"] == "UNKNOWN"
    assert G0["locations"][2]["peacetimeTerritorialAdministration"] == "casa_galdren"
    assert G4["guardrails"]["forjaOwner"] == "UNKNOWN"
    assert G4["guardrails"]["forjaPeacetimeAdmin"] == "casa_galdren"
    assert G4["guardrails"]["forjaWartimeCommand"] == "crown_aethros_hallheim"
    assert len(G1["reliefUnits"]) == len(G3["reliefProfiles"]) == 12
    assert G2["caleran"]["westToEastLink"] == "TOPOGRAPHIC_ROUTE_UNRESOLVED"

    s = x["scope"]
    assert s["territory"] == "casa_galdren"
    fields_equal(s, [
        "georeferenced", "activeMining", "activeIndustry", "activeForge",
        "contentPackLoaded", "worldStateMutated"
    ], False)
    fields_equal(s, ["newSettlements", "newMines", "newRoads", "newJurisdictions"], 0)
    fields_equal(s, [
        "mineCoordinates", "industrialSiteCoordinates", "routes", "minesVerified"
    ], [])
    fields_equal(s, ["siteCapacities", "outputTonnages"], None)

    c = x["canon"]
    assert c["regionalCenterZanthir"] == "zanthir"
    assert c["administrationZanthir"] == "casa_galdren"
    assert c["royalSeat"] == "hallheim" and c["crownHouse"] == "casa_aethros"
    assert c["crownIdentifier"] == "crown_aethros"
    assert c["metalEstelarOnly"] == "montes_azurios"
    assert c["metalEstelarColor"] == "gris_azulado"
    assert c["azuriosNameOrigin"] == "enano" and c["azuriosNameMeaning"] == "Piedra Azul"
    assert c["zanthirManufactures"] == ["minerales", "armas", "herramientas"]
    fields_equal(c, [
        "vornarskKeldarskWinterFreeze", "zanthirBayIce",
        "noHouseBorderCustoms", "royalMintExclusive"
    ], True)
    assert c["treskalOwner"] == "casa_valrik"
    assert c["dorthOwner"] == "casa_edranor"
    assert c["hallheimOwner"] == "crown_aethros"

    r = x["region"]
    assert r["id"] == "zanthir"
    assert r["geographicHouse"] == r["ordinaryTerritorialAdministration"] == "casa_galdren"
    fields_equal(r, [
        "miningRegionalConfirmed", "toolsRegionalProductionConfirmed",
        "weaponsRegionalProductionConfirmed"
    ], True)
    fields_equal(r, [
        "specificMinesMapped", "specificWorkshopsMapped", "specificSmeltersMapped",
        "portsConfirmed", "localMiningPermitIssued", "transportLinksVerified"
    ], False)
    fields_equal(r, ["localProductionAmounts"], None)

    f = x["forge"]
    assert f["id"] == "forja_estelar" and f["placeContext"] == "zanthir"
    assert f["kind"] == "ROYAL_STRATEGIC_INSTALLATION"
    assert f["geographicContextHouse"] == "casa_galdren"
    fields_equal(f, [
        "institutionalDomain", "jurisdictionOwner", "directAdministrationPeace",
        "directAdministrationWar", "directCommandPeace", "directCommandWar"
    ], "crown_aethros")
    fields_equal(f, ["crownAuthorizationRequired"], True)
    fields_equal(f, [
        "settlement", "galdrenOwnsFacility", "galdrenAdministersFacility",
        "galdrenMayAuthorizeActivation", "wartimeTransferOfCommand",
        "activeStateConfirmed", "activationMethodKnown", "royalCustodianNamed",
        "exactPerimeterMapped"
    ], False)
    fields_equal(f, ["legalAcquisitionDate", "technicalRecipe", "manaType"], "UNKNOWN")
    fields_equal(f, ["physicalInventory", "workerCount", "guardsCount"], None)
    fields_equal(f, ["artifactsConfirmed"], [])

    o = x["canonOverride"]
    assert o["id"] == "G05-D01" and o["authorDecisionDate"] == "2026-11-13"
    assert o["scope"] == "FORJA_INSTITUTIONAL_AUTHORITY"
    assert o["priority"] == "AUTHOR_CANON_OVERRIDES_G00_G04"
    fields_equal(o, [
        "rodasAnalogy", "previousStatesAreHistoricalOnly", "appliesPeaceAndWar",
        "superiorCanonDocumentsUpdated"
    ], True)
    fields_equal(o, ["priorJsonRewritten"], False)
    assert o["previousDocumentStates"] == [
        "UNKNOWN", "casa_galdren", "crown_aethros_hallheim"
    ]

    resources = x["resources"]
    ordered_ids(resources, "G05-M", 5)
    for i, material in enumerate(resources):
        assert material["name"] == RESOURCES[i]
        assert material["sourceRegion"] == "montes_azurios"
        assert material["sourceEvidence"] == "CANON_REPO"
        fields_equal(material, ["exceptional", "exclusiveToAzurios"], i == 4)
        fields_equal(material, [
            "localDepositInZanthirVerified", "specificMineVerified",
            "extractionAuthorized", "usageProcessConfirmed"
        ], False)
        fields_equal(material, ["productionQuantity"], None)
        fields_equal(material, ["siteCoordinates"], [])

    units = x["unitStudies"]
    ordered_ids(units, "G05-U", 12)
    for i, item in enumerate(units):
        assert item["reliefUnitId"] == G1["reliefUnits"][i]["id"]
        assert item["reliefKind"] == G1["reliefUnits"][i]["kind"]
        assert item["focus"] == FOCUS[i] and item["status"] == "STUDY_ONLY"
        fields_equal(item, [
            "jurisdictionResolved", "exploitativeClaim", "mineValidated",
            "industrySiteValidated", "outputValidated"
        ], False)
        fields_equal(item, ["mineCoordinates"], [])
        fields_equal(item, ["productionTonnes"], None)

    procs = x["industrialProcesses"]
    ordered_ids(procs, "G05-P", 7)
    for i, item in enumerate(procs):
        assert item["kind"] == PROCESSES[i] and item["status"] == "MODEL_ONLY"
        fields_equal(item, ["ordinaryIndustrial"], i < 6)
        fields_equal(item, ["royalFacilityInterface"], i == 6)
        fields_equal(item, [
            "facilityConfirmed", "workersAssigned", "inventoryRecorded",
            "massBalanceValidated"
        ], False)
        fields_equal(item, ["manufacturedArtifacts"], [])
        fields_equal(item, ["outputCount"], None)

    flows = x["flowStudies"]
    ordered_ids(flows, "G05-F", 6)
    for i, item in enumerate(flows):
        assert (item["from"], item["to"], item["kind"]) == FLOWS[i]
        assert item["status"] == "STUDY_ONLY"
        fields_equal(item, [
            "routeVerified", "contractVerified", "shipmentRecorded",
            "royalForgeAccessGranted"
        ], False)
        fields_equal(item, ["routeGeometry"], [])
        fields_equal(item, ["distanceKm", "quantity"], None)

    legal = x["legal"]
    assert legal["sovereign"] == "crown_aethros"
    fields_equal(legal, ["crownControlsForgeContinuously", "noInternalCustoms"], True)
    fields_equal(legal, [
        "galdrenIndependentLaw", "galdrenIndependentCoin", "feesFixed"
    ], False)
    fields_equal(legal, ["miningConcessionForm", "royalForgeAccessPermitForm"], "UNKNOWN")
    fields_equal(legal, ["permitsGranted", "newTaxRates", "newLegalTitles"], [])

    risks = x["climateRisks"]
    ordered_ids(risks, "G05-R", 10)
    for i, item in enumerate(risks):
        assert item["kind"] == RISKS[i]
        assert item["evidence"] == ("CANON_QUALITATIVE" if i < 3 else "STUDY_ONLY")
        fields_equal(item, ["factConfirmed"], i < 3)
        fields_equal(item, ["eventOccurred", "materialDamageConfirmed", "automaticDamage"], False)
        fields_equal(item, ["fatalities"], None)
        fields_equal(item, ["frequency"], "UNKNOWN")

    lore = x["lore"]
    assert lore["dwarfPriorToHumanAzurios"] == "CANON_REPO"
    assert lore["dwarvenForgeConstruction"] == "AUTHORIAL_NOTE_TO_RECONCILE"
    assert lore["threeDwarfHumanWars"] == "AUTHORIAL_NOTE_TO_RECONCILE"
    assert lore["forgeDormantCenturies"] == "NARRATIVE_DRAFT_NOT_RUNTIME"
    fields_equal(lore, ["dwarfPopulationNow"], None)
    fields_equal(lore, ["warDates", "newLegendaryWeapons"], [])
    fields_equal(lore, ["forgeActiveTodayConfirmed", "newMagicSystem"], False)

    assert x["openQuestions"] == QUESTIONS
    sources = x["sourcePaths"]
    assert len(sources) == 16 and len(set(sources)) == len(sources)
    for path in sources:
        assert not Path(path).is_absolute() and ".." not in Path(path).parts
        assert (ROOT / path).is_file(), f"Fuente no encontrada: {path}"

    # La edición superior debe reflejar la ratificación; los documentos G00-G04
    # no se actualizan de forma retroactiva porque preservan la auditoría.
    for path in [
        N / "NORGARD.md",
        N / "Grandes Casas/grandes_casas.md",
        N / "Gobierno y leyes/sistema_militar_norgard_v0.1.md",
    ]:
        text = path.read_text(encoding="utf-8")
        assert "Forja Estelar" in text and "Aethros" in text
        assert "paz" in text and "guerra" in text


def mutation_tests() -> int:
    mutations = [
        ("runtimeEnabled", True),
        ("status", "RUNTIME_ACTIVE"),
        ("baselineMainSha", "c" * 40),
        ("scope.activeForge", True),
        ("scope.activeIndustry", True),
        ("scope.activeMining", True),
        ("scope.contentPackLoaded", True),
        ("scope.newMines", 1),
        ("scope.newRoads", 2),
        ("scope.mineCoordinates", [{"x": 1, "y": 2}]),
        ("scope.outputTonnages", 300),
        ("canon.metalEstelarOnly", "zanthir"),
        ("canon.zanthirManufactures", ["armas"]),
        ("canon.noHouseBorderCustoms", False),
        ("canon.treskalOwner", "casa_galdren"),
        ("region.specificMinesMapped", True),
        ("region.portsConfirmed", True),
        ("region.localProductionAmounts", 8),
        ("forge.kind", "CITY"),
        ("forge.jurisdictionOwner", "casa_galdren"),
        ("forge.institutionalDomain", "UNKNOWN"),
        ("forge.directAdministrationPeace", "casa_galdren"),
        ("forge.directAdministrationWar", "casa_galdren"),
        ("forge.directCommandPeace", "casa_galdren"),
        ("forge.directCommandWar", "crown_aethros_hallheim"),
        ("forge.galdrenAdministersFacility", True),
        ("forge.galdrenOwnsFacility", True),
        ("forge.galdrenMayAuthorizeActivation", True),
        ("forge.wartimeTransferOfCommand", True),
        ("forge.activeStateConfirmed", True),
        ("forge.technicalRecipe", "RITUAL_DE_FIN"),
        ("forge.guardsCount", 24),
        ("canonOverride.rodasAnalogy", False),
        ("canonOverride.previousStatesAreHistoricalOnly", False),
        ("canonOverride.priorJsonRewritten", True),
        ("resources.4.sourceRegion", "zanthir"),
        ("resources.4.exclusiveToAzurios", False),
        ("resources.4.specificMineVerified", True),
        ("resources.0.localDepositInZanthirVerified", True),
        ("unitStudies.2.jurisdictionResolved", True),
        ("unitStudies.0.exploitativeClaim", True),
        ("industrialProcesses.6.royalFacilityInterface", False),
        ("industrialProcesses.5.inventoryRecorded", True),
        ("flowStudies.4.royalForgeAccessGranted", True),
        ("flowStudies.0.routeVerified", True),
        ("legal.crownControlsForgeContinuously", False),
        ("legal.permitsGranted", ["LIC-0001"]),
        ("legal.newTaxRates", [10]),
        ("climateRisks.3.eventOccurred", True),
        ("climateRisks.0.evidence", "STUDY_ONLY"),
        ("lore.threeDwarfHumanWars", "CANON_REPO"),
        ("lore.forgeActiveTodayConfirmed", True),
        ("lore.newMagicSystem", True),
        ("openQuestions.0", "NONE"),
        ("sourcePaths.0", "../outside_repo"),
    ]
    for dotted, invalid in mutations:
        y = copy.deepcopy(G5)
        obj = y
        parts = dotted.split(".")
        for key in parts[:-1]:
            obj = obj[int(key)] if isinstance(obj, list) else obj[key]
        key = parts[-1]
        obj[int(key) if isinstance(obj, list) else key] = invalid
        try:
            validate(y)
        except (AssertionError, KeyError, TypeError, ValueError):
            pass
        else:
            raise AssertionError(f"Mutation accepted: {dotted} -> {invalid!r}")
    return len(mutations)


if __name__ == "__main__":
    validate(G5)
    count = mutation_tests()
    print(f"GALDREN G05 PASS: 5 materiales, 12 unidades, 7 procesos, "
          f"6 flujos, 10 riesgos, ratificación Corona/Aethros paz-guerra, "
          f"{count} mutaciones negativas. DOCUMENTARY_PLANNING_ONLY.")
