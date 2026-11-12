"""Casa Edranor E08: static social design audit and synthetic negative tests.

No Godot, CoreRPG, actual census, NPC generation or runtime simulation is claimed.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
DATA = BASE / "Datos operativos"

def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

doc = load(DATA / "edranor_e08_population_services_v0.1.json")
fixtures = load(DATA / "edranor_e08_synthetic_fixtures_v0.1.json")
e07 = load(DATA / "edranor_e07_canonical_nuclei_v0.1.json")
e06 = load(DATA / "edranor_e06_settlement_rules_v0.1.json")
e05 = load(DATA / "edranor_e05_roads_communications_v0.1.json")
NAMES = ["dorth", "lumina", "karsath", "rodas"]
CATEGORIES = ["city", "small_compact_settlement", "small_lakeside_visual_settlement", "village"]
EXPECTED_OWNERS = dict.fromkeys(NAMES[:3], "casa_edranor")
EXPECTED_OWNERS["rodas"] = "crown_aethros"
INST_KEYS = ["personIds", "householdIds", "residenceIds", "dwellingIds", "tenureIds",
             "jobAssignmentIds", "providerIds", "buildingIds", "inventoryIds"]
NUM_KEYS = ["population", "householdCount", "meanPersonsPerHousehold", "permanentJobsCount", "temporaryWorkersCount"]
CAP_KEYS = ["residentialBeds", "visitorBeds", "safeWaterPersonDays", "foodPersonDays", "sanitationPersonDays", "availableWorkHours"]
DOCS = ["E08_INDICE.md", "Poblacion_y_hogares/E08_MODELO_HOGAR_RESIDENCIA.md",
        "Poblacion_y_hogares/E08_CENSO_CARGA_ESTACIONAL.md",
        "Poblacion_y_hogares/E08_OFICIOS_Y_EMPLEO.md",
        "Servicios/E08_RED_SERVICIOS_Y_ABASTECIMIENTO.md",
        "Servicios/E08_MATRIZ_LOCALIDADES_Y_PUERTAS.md",
        "Auditorias/E08_FUENTES_Y_DEUDA.md", "Auditorias/E08_ACTA.md",
        "00_Control_del_proyecto/TRASPASO_E09.md"]

def check(d):
    assert d["schemaVersion"] == 1 and d["documentId"] == "edranor_e08_population_services"
    assert d["phase"] == "E08" and d["date"] == "2026-11-13" and d["version"] == "0.1"
    assert d["status"] == "DOCUMENTAL_DESIGN_ONLY" and d["runtimeEnabled"] is False
    assert d["protectedIds"] == NAMES + ["hallheim"]
    assert d["inheritance"] == ["nimroel_core", "norgard_defaults", "casa_edranor_or_crown_aethros", "localidad", "world_state"]
    assert set(d["sourceAuthorities"]) == {"CANON_REPO", "VISUAL_APROBADO", "AUTOR_2026_11_12", "OBSERVACION_MAPA", "PROPUESTA", "UNKNOWN"}
    s = d["scope"]
    assert s["territory"] == "casa_edranor" and type(s["designedNuclei"]) is int and s["designedNuclei"] == 4
    for field in ["georeferenced", "demographicCensusApproved", "physicalRoadsValidated", "localWaterVerified"]:
        assert s[field] is False, field
    for field in ["instantiatedNuclei", "peopleInstantiated", "householdsInstantiated", "dwellingsInstantiated",
                  "jobsInstantiated", "serviceProvidersInstantiated", "stocksInstantiated"]:
        assert type(s[field]) is int and s[field] == 0, field
    assert s["totalTerritorialPopulation"] is s["totalHouseholds"] is None
    law = d["law"]
    assert law["adulthoodAge"] == 18 and law["formalApprenticeshipMinAge"] == 12
    assert law["ordinaryYouthEmploymentMinAge"] == 15
    assert [(b["min"], b["max"], b["employment"], b["formalApprenticeship"]) for b in law["ageBands"]] == [
        (0,7,False,False),(8,11,False,False),(12,14,False,True),(15,17,True,True),(18,None,True,True)]
    for k in ["marriageMustBeValidCivilAct", "coResidenceDoesNotCreateMarriage",
              "occupationDoesNotConferOwnership", "juvenilesRequireConsentAndSafeguards", "apprenticesRequireMentor"]:
        assert law[k] is True, k
    identity = d["identityPolicy"]
    assert len(identity) >= 7 and all(v is True for v in identity.values())
    assert d["presenceAccounting"] == ["residentIds", "visitorIds", "seasonalWorkerIds", "lodgerIds", "workerPersonIds"]
    assert d["requiredCapacityEvidence"] == ["housingBeds", "visitorBeds", "safeWaterPersonDays",
                                              "foodPersonDays", "sanitationPersonDays", "availableWorkHours"]
    svcs = d["serviceCatalog"]
    assert len(svcs) == 15
    assert len({svc["id"] for svc in svcs}) == len(svcs)
    svc_ids = {svc["id"] for svc in svcs}
    for svc in svcs:
        assert svc["id"].startswith("edr_e08_service_")
        assert svc["evidence"] in {"CANON_REPO", "VISUAL_APROBADO", "PROPUESTA"}
        assert len(svc["preconditions"]) >= 3 and len(set(svc["preconditions"])) == len(svc["preconditions"])
        assert svc["operational"] is False and svc["providerInstances"] == []
    roles = d["occupationCatalog"]
    assert len(roles) == 16 and len({r["id"] for r in roles}) == len(roles)
    role_ids = {r["id"] for r in roles}
    for role in roles:
        assert role["id"].startswith("edr_e08_role_")
        assert role["evidence"] == "PROPUESTA" and role["requiresVerifiedDemand"] is True
        assert type(role["hazardousTasksPossible"]) is bool
        assert type(role["filledPositions"]) is int and role["filledPositions"] == 0
        assert role["workerPersonIds"] == [] and role["applicableLocalities"]
        assert set(role["applicableLocalities"]) <= set(NAMES)
    locs = d["localityModels"]
    assert len(locs) == 4 and [x["id"] for x in locs] == NAMES
    for i,loc in enumerate(locs):
        name = NAMES[i]
        assert loc["geographicContextHouse"] == "casa_edranor"
        assert loc["jurisdictionOwner"] == loc["fiscalOwner"] == EXPECTED_OWNERS[name]
        assert loc["militaryOwner"] == ("crown_aethros" if name == "rodas" else "crown_supreme_house_subordinate")
        assert loc["berserkerCommandOwner"] == ("crown_aethros" if name == "rodas" else None)
        assert loc["legalCategory"] == CATEGORIES[i]
        assert all(loc[x] is None for x in NUM_KEYS), name
        assert set(loc["capacity"]) == set(CAP_KEYS)
        assert all(v is None for v in loc["capacity"].values()), name
        assert set(loc["instantiated"]) == set(INST_KEYS)
        assert all(v == [] for v in loc["instantiated"].values()), name
        assert loc["onMapPhysicalCoordinates"] is None and loc["physicalRoads"] == []
        assert loc["actualProviders"] == loc["actualResidents"] == []
        assert loc["evidenceStatus"] == "PROPOSAL_UNVERIFIED_OPERATION"
        assert loc["classifiedAsProtectedCanonicalAnchor"] is True and loc["proceduralSpawnAllowed"] is False
        assert loc["serviceProgramIds"] and set(loc["serviceProgramIds"]) <= svc_ids
        assert len(set(loc["serviceProgramIds"])) == len(loc["serviceProgramIds"])
        assert loc["roleProgramIds"] and set(loc["roleProgramIds"]) <= role_ids
        assert len(set(loc["roleProgramIds"])) == len(loc["roleProgramIds"])
        assert all(name in next(r for r in roles if r["id"] == rid)["applicableLocalities"]
                   for rid in loc["roleProgramIds"])
        assert len(loc["knownVisualTypes"]) >= 2
    by_id = {loc["id"]: loc for loc in locs}
    assert "main_inn_visual_type" in by_id["lumina"]["knownVisualTypes"]
    assert "annual_wine_market" in by_id["lumina"]["knownVisualTypes"]
    assert "guarded_two_storey_nonreligious_druid_house" in by_id["rodas"]["knownVisualTypes"]
    assert "edr_e08_service_druid_house" in by_id["rodas"]["serviceProgramIds"]
    assert all("edr_e08_service_druid_house" not in by_id[x]["serviceProgramIds"] for x in NAMES[:3])
    assert d["outsideScope"] == {"id":"hallheim","insideEdranor":False,"designed":False,"jurisdictionOwner":"crown_aethros"}
    assert len(d["hardConstraints"]) >= 11 and all(x is True for x in d["hardConstraints"].values())
    assert "EDD-04_census" in d["unresolved"] and len(d["unresolved"]) >= 12
    assert set(d["instanceRegistry"]) == {"people","households","dwellings","residences","tenures","jobs","providers","buildings","stocks"}
    assert all(v == [] for v in d["instanceRegistry"].values())
    assert d["runtimeClaims"] == []

def apply_changes(case,changes):
    item = copy.deepcopy(case)
    for change in changes:
        target = item
        path = change["path"]
        assert isinstance(path, list) and path
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = change["value"]
    return item

def evaluate(c):
    if c["locality"] not in EXPECTED_OWNERS or c["jurisdictionOwner"] != EXPECTED_OWNERS[c["locality"]]:
        return False
    if any(c[f] is not False for f in
           ["unlawfulInternalCustoms","edranorTaxesInRodas","edranorCommandsBerserkers"]):
        return False
    groups = ("residentIds", "visitorIds", "seasonalWorkerIds", "lodgerIds")
    if any(not isinstance(c[x],list) or len(set(c[x])) != len(c[x])
           or any(not isinstance(p,str) or not p for p in c[x]) for x in groups):
        return False
    residents, visitors = set(c["residentIds"]), set(c["visitorIds"])
    if residents & visitors: return False
    present = residents | visitors
    if not set(c["seasonalWorkerIds"]) <= present: return False
    if not set(c["lodgerIds"]) <= visitors: return False
    for x in ["housingBeds","visitorBeds","safeWaterPersonDays","foodPersonDays",
              "sanitationPersonDays","availableWorkHours"]:
        if type(c[x]) is not int or c[x] < 0: return False
    if c["housingBeds"] < len(residents) or c["visitorBeds"] < len(c["lodgerIds"]):
        return False
    if any(c[x] < len(present) for x in ["safeWaterPersonDays","foodPersonDays","sanitationPersonDays"]):
        return False
    workers = c["workers"]
    if not isinstance(workers,list): return False
    worker_ids = [w["personId"] for w in workers]
    if len(set(worker_ids)) != len(worker_ids) or not set(worker_ids) <= present: return False
    if any(type(w["hours"]) is not int or w["hours"] < 0 or w["hours"] > c["availableWorkHours"]
           for w in workers): return False
    if sum(w["hours"] for w in workers) > c["availableWorkHours"]: return False
    adults = {w["personId"] for w in workers if type(w["age"]) is int and w["age"] >= 18}
    for w in workers:
        if type(w["age"]) is not int or w["age"] < 0 or w["ownConsent"] is not True or w["safeTask"] is not True: return False
        if w["age"] < 12: return False
        if 12 <= w["age"] <= 14:
            if (w["engagement"] != "apprenticeship" or w["mentorId"] not in adults
                or w["guardianConsent"] is not True or w["supervised"] is not True): return False
        elif w["age"] < 18:
            if (w["engagement"] not in {"employment","apprenticeship"}
                or w["guardianConsent"] is not True or w["supervised"] is not True): return False
        else:
            if w["engagement"] not in {"employment","apprenticeship"}: return False
    service_ids = set(doc["localityModels"][NAMES.index(c["locality"])]["serviceProgramIds"])
    for s in c["requestedServices"]:
        if s["id"] not in service_ids: return False
        if not (s["providerVerified"] is True and s["inputsVerified"] is True
                and s["rightsVerified"] is True): return False
    return True

assert e07["scope"]["householdsInstantiated"] == 0 and e07["scope"]["npcInstantiated"] == 0
assert [loc["id"] for loc in e07["settlements"]] == NAMES
assert all(loc["jurisdictionOwner"] == EXPECTED_OWNERS[loc["id"]] for loc in e07["settlements"])
assert e06["scope"]["syntheticLabOnly"] is True and e06["scope"]["proceduralSettlementsInstantiated"] == 0
assert e05["scope"]["physicalGraphValidated"] is False
for relative in DOCS:
    f = BASE / relative
    assert f.is_file() and f.stat().st_size > 500, relative
assert (ROOT / ".github/workflows/edranor-e08.yml").is_file()
check(doc)

# Each mutated guard must be rejected by a fresh contract check; no silent promotions.
mutations = []
def mutation(path,value): mutations.append((path,value))
for key,value in [("documentId","false"),("schemaVersion",2),("version","9"),
  ("phase","E11"),("date","2020"),("status","ACTIVE"),("runtimeEnabled",True),
  ("protectedIds",[]),("sourceAuthorities",[]),("inheritance",[]),
  ("localityModels",[]),("occupationCatalog",[]),("serviceCatalog",[]),
  ("unresolved",[]),("hardConstraints",{}),("instanceRegistry",{}),("runtimeClaims",["active"])]:
    mutation([key],value)
for k in ["georeferenced","demographicCensusApproved","physicalRoadsValidated","localWaterVerified"]:
    mutation(["scope",k],True)
for k in ["peopleInstantiated","householdsInstantiated","dwellingsInstantiated","jobsInstantiated",
          "serviceProvidersInstantiated","stocksInstantiated","instantiatedNuclei"]:
    mutation(["scope",k],1)
for k in ["totalTerritorialPopulation","totalHouseholds"]:
    mutation(["scope",k],42)
for k,value in [("adulthoodAge",16),("formalApprenticeshipMinAge",10),
                ("ordinaryYouthEmploymentMinAge",12),("ageBands",[])]:
    mutation(["law",k],value)
for k in ["marriageMustBeValidCivilAct","coResidenceDoesNotCreateMarriage","occupationDoesNotConferOwnership",
          "juvenilesRequireConsentAndSafeguards","apprenticesRequireMentor"]:
    mutation(["law",k],False)
for k in doc["identityPolicy"]: mutation(["identityPolicy",k],False)
for k in doc["hardConstraints"]: mutation(["hardConstraints",k],False)
for i,loc in enumerate(doc["localityModels"]):
    for k,value in [("id","other"),("geographicContextHouse","other"),("jurisdictionOwner","other"),
        ("fiscalOwner","other"),("militaryOwner","other"),("berserkerCommandOwner","other"),
        ("legalCategory","OTHER"),("onMapPhysicalCoordinates",[2,3]),("physicalRoads",["imaginary"]),
        ("actualProviders",["x"]),("actualResidents",["x"]),("evidenceStatus","ACTIVE"),
        ("classifiedAsProtectedCanonicalAnchor",False),("proceduralSpawnAllowed",True),
        ("serviceProgramIds",[]),("roleProgramIds",[]),("knownVisualTypes",[])]:
        mutation(["localityModels",i,k],value)
    for k in NUM_KEYS: mutation(["localityModels",i,k],123)
    for k in CAP_KEYS: mutation(["localityModels",i,"capacity",k],42)
    for k in INST_KEYS: mutation(["localityModels",i,"instantiated",k],["x"])
for i,svc in enumerate(doc["serviceCatalog"]):
    mutation(["serviceCatalog",i,"operational"],True)
    mutation(["serviceCatalog",i,"providerInstances"],["provider"])
    mutation(["serviceCatalog",i,"preconditions"],[])
for i,role in enumerate(doc["occupationCatalog"]):
    mutation(["occupationCatalog",i,"filledPositions"],1)
    mutation(["occupationCatalog",i,"workerPersonIds"],["person"])
    mutation(["occupationCatalog",i,"requiresVerifiedDemand"],False)
for k in doc["instanceRegistry"]:mutation(["instanceRegistry",k],["fake"])
for n,(path,val) in enumerate(mutations,1):
    mutant = copy.deepcopy(doc)
    target = mutant
    for node in path[:-1]: target = target[node]
    target[path[-1]] = val
    try:check(mutant)
    except (AssertionError, KeyError, TypeError, ValueError, StopIteration): pass
    else:raise AssertionError(f"E08 unsafe mutation survived #{n}: {path}")

assert fixtures["schemaVersion"] == 1 and fixtures["documentId"] == "edranor_e08_synthetic_fixtures"
assert fixtures["phase"] == "E08" and fixtures["syntheticOnly"] is True
assert fixtures["canonPopulation"] is False and fixtures["runtimeEnabled"] is False
scenarios = fixtures["scenarios"]
assert len(scenarios) == 13 and len({x["id"] for x in scenarios}) == 13
positive = negative = 0
for case in scenarios:
    checked = apply_changes(fixtures["baseCase"], case["changes"])
    actual = evaluate(checked)
    assert actual is case["expected"], f"E08 synthetic case failed {case['id']} expected {case['expected']} got {actual}"
    if actual:positive += 1
    else:negative += 1
assert (positive,negative) == (4,9)
print(f"E08 OK | 4 nuclei | 15 candidate services | 16 candidate occupations | {positive} positive / {negative} negative synthetic | {len(mutations)} blocked structural mutations | no runtime")
