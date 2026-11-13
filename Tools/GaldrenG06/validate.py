"""GALDREN G06: contrato documental y pruebas negativas, sin runtime."""
from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NORGARD = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard"
H = NORGARD / "Territorios/Casa Galdren"
DATA = H / "Datos operativos"


def read(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


G1 = read("galdren_g01_geography_v0.1.json")
G2 = read("galdren_g02_hydrology_v0.1.json")
G4 = read("galdren_g04_agriculture_livestock_food_v0.1.json")
G5 = read("galdren_g05_mining_industry_forge_v0.1.json")
G6 = read("galdren_g06_communications_economic_networks_v0.1.json")

CORRIDOR_KINDS = [
    "TERRESTRIAL_STUDY",
    "TERRESTRIAL_OR_RIVER_UNPROVEN",
    "TERRESTRIAL_OR_COASTAL_UNPROVEN",
    "TERRESTRIAL_INTERHOUSE_STUDY",
    "MOUNTAIN_ACCESS_UNPROVEN",
    "CROSSKINGDOM_CONTEXT_ONLY",
]
CORRIDOR_LIMITATIONS = [
    "SLOPE_AND_COLD_UNKNOWN",
    "CALERAN_SPLITS_AND_FLOODPLAIN_UNKNOWN",
    "ZANTHIR_BAY_WINTER_ICE",
    "VALRIK_BORDER_AND_INVERNOS_UNKNOWN",
    "AZURIOS_WEST_EAST_LINK_UNRESOLVED",
    "VARETH_REGION_ALLOCATION_UNRESOLVED",
]
MODES = [
    ("TERRESTRIAL", "REQUIRES_SURVEY", False),
    ("CALERAN_FLUVIAL", "NAVIGABILITY_UNKNOWN", False),
    ("NORTHERN_RIVERS", "ICE_CANON_NO_NAVIGATION", True),
    ("ZANTHIR_COASTAL", "ICE_CANON_NO_PORT", True),
    ("INTERHOUSE", "NO_INTERNAL_CUSTOMS", False),
    ("ROYAL_FORGE_ACCESS", "CROWN_AUTHORIZATION_REQUIRED", False),
]
INFO = [
    "HOUSEHOLD_NEIGHBOR_SPECIALIST",
    "TAVERN_SOCIAL_REFERENCE",
    "RURAL_MARKET_REFERENCE",
    "TRAVELING_MERCHANT_EXTERNAL_EXAMPLE",
    "COURIER_POSTAL_SERVICE_HYPOTHESIS",
    "ROYAL_NOTICE_AUTHORITY_MODEL",
]
RISKS = [
    ("VORNARSK_WINTER_FREEZE", "CANON_QUALITATIVE", True),
    ("KELDARSK_WINTER_FREEZE", "CANON_QUALITATIVE", True),
    ("ZANTHIR_BAY_ICE", "CANON_QUALITATIVE", True),
    ("INVERNOS_THAW", "REGIONAL_DRAFT_QUALITATIVE", False),
    ("CALERAN_FLOOD_DELAYS", "STUDY_ONLY", False),
    ("MOUNTAIN_ROUTE_DISRUPTION", "STUDY_ONLY", False),
    ("TRADE_THEFT_OR_LOSS", "STUDY_ONLY", False),
    ("MESSENGER_DELAY_OR_INTERCEPTION", "STUDY_ONLY", False),
]
SCOPE_ZERO = [
    "newRoads", "newBridges", "newPorts", "newRiverRoutes", "newPostStations",
    "newTolls", "newCustoms", "newSettlements",
]
SCOPE_FALSE = [
    "georeferenced", "transportRuntimeActive", "economyRuntimeActive",
    "communicationsRuntimeActive", "contentPackLoaded", "worldStateMutated",
]
SCOPE_EMPTY = [
    "roadGeometry", "bridgeCoordinates", "portCoordinates",
    "verifiedNavigationSegments", "runtimeLinks",
]
CANON_OWNER = {
    "arleonOwner": "casa_galdren", "zanthirOwner": "casa_galdren",
    "hallheimOwner": "crown_aethros", "treskalOwner": "casa_valrik",
    "dorthOwner": "casa_edranor",
    "forjaOwner": "crown_aethros",
    "forjaAdministrationPeace": "crown_aethros",
    "forjaAdministrationWar": "crown_aethros",
    "forjaCommandPeace": "crown_aethros",
    "forjaCommandWar": "crown_aethros",
    "metalEstelarOnly": "montes_azurios",
}
CANON_TRUE = [
    "noHouseBorderCustoms", "royalMintExclusive", "caleranOneRiver",
    "vornarskWinterFreeze", "keldarskWinterFreeze", "zanthirBayIce",
    "roadsDoNotFollowPlaceNames",
]
AUTH_TRUE = [
    "forgeSpecialCargoNeedsCrownAuthority",
    "geographicAccessDoesNotAuthorizeForge",
    "noGaldrenForgePermit",
    "royalMovementsExemptHouseTerritorialTax",
    "commercialPurchaseStillRealTransaction",
    "internalTradeDoesNotAutomaticallyChargeCustoms",
    "serviceFeesRequireRealServiceAndAuthorization",
    "foreignCustomsOnlyWhereApplicable",
    "clavoAccountingUnit",
    "royalMintInHallheim",
]
HANDOFF_TRUE = [
    "requireSurveyBeforeInstantiatingRoutes",
    "requireAuthorApprovalForNamedInfrastructure",
    "requireActualWorldStateForTrade",
    "requireProofOfServiceBeforeFees",
    "requireAuthorizationForRoyalForge",
    "noProceduralCityCreation",
]


def eq(obj: dict, key: str, expected: object) -> None:
    assert key in obj, f"Campo ausente: {key}"
    actual = obj[key]
    assert type(actual) is type(expected) and actual == expected, (
        f"{key}: {actual!r} != {expected!r}"
    )


def ordered(rows: list, prefix: str, size: int) -> None:
    assert isinstance(rows, list) and len(rows) == size
    assert [x["id"] for x in rows] == [
        f"{prefix}{i:02d}" for i in range(1, size + 1)
    ]


def validate(x: dict) -> None:
    eq(x, "schemaVersion", 1)
    eq(x, "documentId", "galdren_g06_communications_economic_networks")
    eq(x, "phase", "G06")
    eq(x, "version", "0.1.0")
    eq(x, "date", "2026-11-13")
    eq(x, "baselineMainSha", "8610affd134d3134b8cba17b2b43c483331b127a")
    eq(x, "baseDocumentId", G5["documentId"])
    eq(x, "status", "DOCUMENTARY_PLANNING_ONLY")
    eq(x, "runtimeEnabled", False)
    eq(x, "authorApproval", "G06_START_AUTHORIZED_NO_NEW_CANON_RATIFIED")
    eq(x, "inheritance", G5["inheritance"])
    assert x["inheritance"] == G4["inheritance"] == G1["inheritance"]

    # Invariantes heredadas: la decisión G05 sustituye la lectura G00–G04,
    # pero nunca se reescriben sus JSON históricos para borrar la trazabilidad.
    eq(G5["forge"], "institutionalDomain", "crown_aethros")
    eq(G5["forge"], "directAdministrationPeace", "crown_aethros")
    eq(G5["forge"], "directAdministrationWar", "crown_aethros")
    eq(G5["forge"], "directCommandPeace", "crown_aethros")
    eq(G5["forge"], "directCommandWar", "crown_aethros")
    eq(G2["caleran"], "westToEastLink", "TOPOGRAPHIC_ROUTE_UNRESOLVED")
    eq(G2["caleran"], "navigationStatus", "UNKNOWN")
    eq(G4["guardrails"], "noHouseBorderCustoms", True)
    eq(G5["canon"], "metalEstelarOnly", "montes_azurios")

    scope = x["scope"]
    eq(scope, "territory", "casa_galdren")
    for key in SCOPE_ZERO:
        eq(scope, key, 0)
    for key in SCOPE_FALSE:
        eq(scope, key, False)
    for key in SCOPE_EMPTY:
        eq(scope, key, [])
    for key in ("transportTimeDays", "tradeVolumes"):
        eq(scope, key, None)

    canon = x["canon"]
    for key, expected in CANON_OWNER.items():
        eq(canon, key, expected)
    for key in CANON_TRUE:
        eq(canon, key, True)
    eq(canon, "caleranWestEastRouteResolved", False)

    c = x["corridorStudies"]
    ordered(c, "G06-C", 6)
    for index, row in enumerate(c):
        prev = G1["corridorStudies"][index]
        eq(row, "sourceCorridorId", prev["id"])
        eq(row, "originContext", prev["origin"])
        eq(row, "destinationContext", prev["destination"])
        eq(row, "kind", CORRIDOR_KINDS[index])
        eq(row, "topographicCondition", CORRIDOR_LIMITATIONS[index])
        eq(row, "status", "STUDY_ONLY")
        for key in ("routeVerified", "contactValidated", "legalRightOfWayVerified",
                    "bridgeVerified", "portVerified", "fluvialVerified",
                    "allSeasonAvailableVerified", "createsJurisdiction"):
            eq(row, key, False)
        for key in ("geometry", "verifiedNodes"):
            eq(row, key, [])
        for key in ("distanceKm", "travelTimeDays"):
            eq(row, key, None)

    modes = x["transportModeStudies"]
    ordered(modes, "G06-M", 6)
    for i, row in enumerate(modes):
        kind, limitation, ice = MODES[i]
        eq(row, "kind", kind)
        eq(row, "limitation", limitation)
        eq(row, "iceEvidenceRelevant", ice)
        eq(row, "status", "STUDY_ONLY")
        for key in ("serviceVerified", "routeVerified", "infrastructureVerified",
                    "seasonalAvailabilityVerified"):
            eq(row, key, False)
        eq(row, "throughput", None)
        eq(row, "travelTimeDays", None)
        eq(row, "geometry", [])

    flow_sources = (
        [("G04", row) for row in G4["tradeFlowStudies"]]
        + [("G05", row) for row in G5["flowStudies"]]
    )
    e = x["economicLinkStudies"]
    ordered(e, "G06-E", 12)
    assert len(flow_sources) == 12
    for index, row in enumerate(e):
        phase, prev = flow_sources[index]
        eq(row, "sourcePhase", phase)
        eq(row, "sourceFlowId", prev["id"])
        eq(row, "from", prev["from"])
        eq(row, "to", prev["to"])
        eq(row, "kind", prev["kind"])
        eq(row, "status", "STUDY_ONLY")
        for key in ("shipmentRecorded", "tradeContractConfirmed", "routeVerified",
                    "stockConfirmed", "priceConfirmed",
                    "interHouseCustomsCharged", "forjaRoyalAccessGranted"):
            eq(row, key, False)
        eq(row, "routeGeometry", [])
        for key in ("distanceKm", "quantity", "tariffAmount"):
            eq(row, key, None)

    information = x["informationServiceStudies"]
    ordered(information, "G06-I", 6)
    for i, row in enumerate(information):
        eq(row, "kind", INFO[i])
        eq(row, "status", "NORGARD_REFERENCE_ONLY" if i < 4 else "MODEL_ONLY")
        for key in ("galdrenInstanceVerified", "routeVerified",
                    "relayStationConfirmed", "npcAssigned",
                    "universalInformationAccess"):
            eq(row, key, False)
        eq(row, "localCoordinates", [])
        eq(row, "deliveryTimeDays", None)
        eq(row, "realMessagesRecorded", 0)

    risks = x["seasonRiskStudies"]
    ordered(risks, "G06-R", 8)
    for i, row in enumerate(risks):
        kind, evidence, confirmed = RISKS[i]
        eq(row, "kind", kind)
        eq(row, "evidence", evidence)
        eq(row, "regionalFactConfirmed", confirmed)
        for key in ("specificTransportFailureConfirmed", "routeClosureRecorded",
                    "worldEventRecorded", "automaticBlockade"):
            eq(row, key, False)
        eq(row, "probability", None)
        eq(row, "durationDays", None)
        eq(row, "affectedVerifiedRoutes", [])

    auth = x["authorization"]
    eq(auth, "ordinaryZanthirAdmin", "casa_galdren")
    eq(auth, "royalForgeDomain", "crown_aethros")
    for key in AUTH_TRUE:
        eq(auth, key, True)
    for key in ("interHouseCustoms", "forgeAccessCredentialsDefined",
                "forgePerimeterVerified", "galdrenMintExists"):
        eq(auth, key, False)
    eq(auth, "lunaInClavos", 24)
    eq(auth, "coronaInClavos", 480)

    handoff = x["g07Handoff"]
    for key in HANDOFF_TRUE:
        eq(handoff, key, True)
    eq(handoff, "excludeCanonical", [
        "arleon", "zanthir", "forja_estelar", "treskal", "hallheim", "dorth"
    ])

    refs = x["sourceRefs"]
    eq(refs, "g01Corridors", [row["id"] for row in G1["corridorStudies"]])
    eq(refs, "g04Flows", [row["id"] for row in G4["tradeFlowStudies"]])
    eq(refs, "g05Flows", [row["id"] for row in G5["flowStudies"]])
    assert isinstance(x["unknown"], list) and len(x["unknown"]) == 18
    assert len(set(x["unknown"])) == len(x["unknown"])
    assert isinstance(x["sourcePaths"], list) and len(x["sourcePaths"]) >= 9
    for path in x["sourcePaths"]:
        assert isinstance(path, str) and path.startswith("Worldbuilding/")
        assert (ROOT / path).is_file(), f"Falta fuente real: {path}"


def mutation_negative_tests() -> int:
    cases: list[tuple[tuple, object]] = []
    def add(path: tuple, invalid: object) -> None:
        cases.append((path, invalid))

    for path, bad in [
        (("schemaVersion",), 2), (("documentId",), "wrong"),
        (("phase",), "G07"), (("baseDocumentId",), "g04"),
        (("status",), "OPERATIVE"), (("runtimeEnabled",), True),
        (("authorApproval",), "NEW_ROUTES_CANON"),
        (("baselineMainSha",), "wrong"),
        (("scope", "territory"), "casa_valrik"),
        (("canon", "forjaOwner"), "casa_galdren"),
        (("canon", "treskalOwner"), "casa_galdren"),
        (("canon", "noHouseBorderCustoms"), False),
        (("canon", "caleranWestEastRouteResolved"), True),
        (("canon", "roadsDoNotFollowPlaceNames"), False),
        (("authorization", "royalForgeDomain"), "casa_galdren"),
        (("authorization", "interHouseCustoms"), True),
        (("authorization", "forgeAccessCredentialsDefined"), True),
        (("authorization", "serviceFeesRequireRealServiceAndAuthorization"), False),
        (("authorization", "royalMovementsExemptHouseTerritorialTax"), False),
        (("authorization", "lunaInClavos"), 25),
        (("authorization", "galdrenMintExists"), True),
        (("g07Handoff", "requireSurveyBeforeInstantiatingRoutes"), False),
        (("g07Handoff", "excludeCanonical"), ["arleon"]),
        (("sourceRefs", "g01Corridors"), []),
        (("sourceRefs", "g04Flows"), []),
        (("sourceRefs", "g05Flows"), []),
        (("unknown",), []),
        (("sourcePaths",), []),
    ]:
        add(path, bad)
    for key in SCOPE_ZERO:
        add(("scope", key), 1)
    for key in SCOPE_FALSE:
        add(("scope", key), True)
    for key in SCOPE_EMPTY:
        add(("scope", key), [{"fake": "map"}])
    for key in ("transportTimeDays", "tradeVolumes"):
        add(("scope", key), 4)

    for i in range(6):
        for key, bad in [
            ("sourceCorridorId", "wrong"), ("originContext", "wrong"),
            ("destinationContext", "wrong"), ("kind", "VERIFIED_ROAD"),
            ("status", "VERIFIED"), ("routeVerified", True),
            ("contactValidated", True), ("legalRightOfWayVerified", True),
            ("bridgeVerified", True), ("portVerified", True),
            ("fluvialVerified", True), ("allSeasonAvailableVerified", True),
            ("createsJurisdiction", True), ("geometry", [[0, 0], [1, 1]]),
            ("verifiedNodes", ["port"]), ("distanceKm", 11),
            ("travelTimeDays", 2),
        ]:
            add(("corridorStudies", i, key), bad)
        for key, bad in [
            ("kind", "UNLIMITED_ROUTE"), ("limitation", "NONE"),
            ("iceEvidenceRelevant", not MODES[i][2]),
            ("serviceVerified", True), ("routeVerified", True),
            ("infrastructureVerified", True),
            ("seasonalAvailabilityVerified", True),
            ("throughput", 100), ("geometry", ["line"]),
            ("travelTimeDays", 1),
        ]:
            add(("transportModeStudies", i, key), bad)
        for key, bad in [
            ("kind", "POSTAL_SERVICE_ACTIVE"),
            ("status", "INSTALLED"), ("galdrenInstanceVerified", True),
            ("routeVerified", True), ("relayStationConfirmed", True),
            ("npcAssigned", True), ("universalInformationAccess", True),
            ("localCoordinates", [1, 2]), ("deliveryTimeDays", 1),
            ("realMessagesRecorded", 1),
        ]:
            add(("informationServiceStudies", i, key), bad)

    for i in range(12):
        for key, bad in [
            ("sourcePhase", "G03"), ("sourceFlowId", "wrong"),
            ("from", "wrong"), ("to", "wrong"), ("kind", "CREATED"),
            ("status", "ACTIVE"), ("shipmentRecorded", True),
            ("tradeContractConfirmed", True), ("routeVerified", True),
            ("stockConfirmed", True), ("priceConfirmed", True),
            ("interHouseCustomsCharged", True),
            ("forjaRoyalAccessGranted", True),
            ("routeGeometry", ["road"]), ("distanceKm", 2),
            ("quantity", 99), ("tariffAmount", 1),
        ]:
            add(("economicLinkStudies", i, key), bad)

    for i in range(8):
        for key, bad in [
            ("kind", "FAKE"), ("evidence", "CANON_RUNTIME_EVENT"),
            ("regionalFactConfirmed", not RISKS[i][2]),
            ("specificTransportFailureConfirmed", True),
            ("routeClosureRecorded", True), ("worldEventRecorded", True),
            ("automaticBlockade", True), ("probability", 1.0),
            ("durationDays", 20), ("affectedVerifiedRoutes", ["fake"]),
        ]:
            add(("seasonRiskStudies", i, key), bad)

    count = 0
    for path, invalid in cases:
        value = copy.deepcopy(G6)
        target = value
        for step in path[:-1]:
            target = target[step]
        target[path[-1]] = invalid
        try:
            validate(value)
        except (AssertionError, KeyError, TypeError, IndexError):
            count += 1
        else:
            raise AssertionError(f"Mutación indebidamente aceptada: {path}")
    return count


if __name__ == "__main__":
    validate(G6)
    negatives = mutation_negative_tests()
    for required in [
        "G06_INDICE.md",
        "Comunicaciones/G06_CORREDORES_Y_PRIORIDADES.md",
        "Comunicaciones/G06_MODALIDADES_Y_ESTACIONALIDAD.md",
        "Comunicaciones/G06_MENSAJERIA_Y_CONOCIMIENTO.md",
        "Economia/G06_MATRIZ_DE_INTERCAMBIO.md",
        "Economia/G06_CONTROL_Y_TRAZABILIDAD.md",
        "Forja_Estelar/G06_LOGISTICA_REGIA.md",
        "Riesgos/G06_RIESGOS.md",
        "Auditorias/G06_FUENTES_Y_DEUDA.md",
        "Auditorias/G06_ACTA.md",
        "00_Control_del_proyecto/TRASPASO_G07.md",
    ]:
        assert (H / required).is_file(), f"Falta expediente G06: {required}"
    print(
        f"GALDREN G06 PASS: 6 corredores + 6 modos + 12 vínculos "
        f"+ 6 modelos información + 8 riesgos; {negatives} negativas rechazadas; "
        "runtime OFF"
    )
