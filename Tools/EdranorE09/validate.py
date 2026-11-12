"""Casa Edranor E09: canon guard, cross-phase consistency and synthetic negative tests.
NO RUNTIME: this is not Godot/CoreRPG, not legal engine, and not game content.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
DATA = BASE / "Datos operativos"
def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))

doc = load("edranor_e09_governance_v0.1.json")
lab = load("edranor_e09_synthetic_cases_v0.1.json")
e08 = load("edranor_e08_population_services_v0.1.json")
e07 = load("edranor_e07_canonical_nuclei_v0.1.json")
e05 = load("edranor_e05_roads_communications_v0.1.json")
NAMES = ["dorth", "lumina", "karsath", "rodas"]
OWNERS = {"dorth":"casa_edranor","lumina":"casa_edranor","karsath":"casa_edranor","rodas":"crown_aethros"}
TYPES = ["city", "small_compact_settlement", "small_lakeside_visual_settlement", "village"]
EMPTY = ["instantiatedOfficerIds","issuedPermitIds","issuedTaxObligationIds","activeMilitaryUnitIds",
         "courtCaseIds","physicalRoadIds","assignedBuildingIds"]
DOCS = [
 "E09_INDICE.md","Administracion/E09_COMPETENCIAS_Y_REGISTROS.md",
 "Administracion/E09_MATRIZ_POR_LOCALIDAD.md","Justicia/E09_JUSTICIA_DEL_REY_Y_GARANTIAS.md",
 "Fiscalidad/E09_TRIBUTOS_ADUANAS_Y_CUENTAS.md",
 "Autorizaciones/E09_MERCADOS_BODEGAS_BOSQUE_SERVICIOS.md",
 "Defensa_y_seguridad/E09_FUERZAS_MANDO_Y_PROTECCION.md",
 "Defensa_y_seguridad/E09_PROTOCOLO_INCIDENTES_Y_RODAS.md",
 "Auditorias/E09_FUENTES_Y_DEUDA.md","Auditorias/E09_ACTA.md",
 "00_Control_del_proyecto/TRASPASO_E10.md"
]
def check(d):
    assert type(d["schemaVersion"]) is int and d["schemaVersion"] == 1
    assert (d["documentId"],d["date"],d["phase"],d["version"],d["status"],d["runtimeEnabled"]) == (
        "edranor_e09_governance","2026-11-13","E09","0.1","DOCUMENTAL_DESIGN_ONLY",False)
    assert d["sourceAuthorities"] == ["CANON_REPO","VISUAL_APROBADO","AUTOR_2026_11_12",
                                     "OBSERVACION_MAPA","PROPUESTA","UNKNOWN"]
    assert d["inheritance"] == ["nimroel_core","norgard_defaults","casa_edranor_or_crown_aethros","localidad","world_state"]
    assert d["protectedIds"] == NAMES + ["hallheim"]
    s=d["scope"]
    assert s["territory"]=="casa_edranor" and type(s["designedNuclei"]) is int and s["designedNuclei"]==4
    for k in ["physicalGraphValidated","demographicCensusApproved","officeBuildingsValidated","crownDelegationsInstantiated"]:
        assert s[k] is False,k
    for k in ["activeOfficeInstances","appointedPeople","createdUnits","createdGuardPosts","createdCourts",
              "issuedPermits","leviedTaxes","realCourtCases"]:
        assert type(s[k]) is int and s[k]==0,k
    for k in ["effectivePopulation","territorialRevenueClavos","edranorTaxRate","remittancePercentage",
              "guardCount","territorialForceCount","reserveCount","forestExtractionQuota"]:
        assert s[k] is None,k
    locs=d["localityModels"]
    assert len(locs)==4 and [x["id"] for x in locs]==NAMES
    for i,x in enumerate(locs):
        n=NAMES[i]
        assert x["geographicContextHouse"]=="casa_edranor"
        assert all(x[k]==OWNERS[n] for k in
                   ["jurisdictionOwner","justiceOwner","fiscalOwner","securityOwner"])
        assert x["militaryOwner"]==("crown_aethros" if n=="rodas" else "crown_supreme_house_subordinate")
        assert x["berserkerCommandOwner"]==("crown_aethros" if n=="rodas" else None)
        assert x["legalCategory"]==TYPES[i]
        assert x["protectedCanonicalAnchor"] is True and x["proceduralSpawnAllowed"] is False
        for k in ["administratorPersonId","judicialOfficerId","taxOfficerId","guardPersonnelCount",
                  "territorialForceCount","mobilizableCount","licensedBusinessCount","approvedTariffRef"]:
            assert x[k] is None,(n,k)
        for k in EMPTY: assert x[k]==[],(n,k)
    ro=d["institutionRoleCatalog"]
    assert len(ro)==10 and len({r["id"] for r in ro})==len(ro)
    for r in ro:
        assert r["id"].startswith("edr_e09_role_")
        assert r["authorityOwner"] in {"casa_edranor","crown_aethros"}
        assert r["coverage"] in {"kingdom","edranor_only","rodas_only"}
        assert r["evidence"] in {"CANON_REPO","PROPUESTA"}
        assert r["instantiatedByE09"] is False
        assert r["staffCount"] is None
        assert r["appointedPersonIds"]==r["assignedBuildingIds"]==r["emittedOrderIds"]==[]
        assert (r["coverage"]!="rodas_only") or r["authorityOwner"]=="crown_aethros"
    auth=d["authorizationCatalog"]
    assert len(auth)==11 and len({a["id"] for a in auth})==len(auth)
    for a in auth:
        assert a["id"].startswith("edr_e09_permission_")
        assert a["issuer"] in {"casa_edranor","crown_aethros","territorial_owner"}
        assert a["requiresVerifiedActor"] is a["requiresLegalBasis"] is True
        assert a["issuedIds"]==[] and a["operational"] is False
        assert a["evidence"]=="PROPUESTA"
    assert d["fiscalPolicy"]==dict(d["fiscalPolicy"]) and len(d["fiscalPolicy"])>=14
    f=d["fiscalPolicy"]
    for k in ["royalSupremacy","oneInternalFiscalArea","noInternalCustoms","externalCustomsCrownLawOnly",
              "noEdranorMint","territorialContributionRequiresAuthorizedObligation",
              "serviceFeeRequiresServiceAndAuthorizedTariff","crownRemittanceRequiresRegisteredShare",
              "extraordinaryLevyRequiresSpecificCrownOrder"]:
        assert f[k] is True,k
    assert (f["accountUnit"],f["clavosPerLuna"],f["clavosPerCorona"],f["coinMintLocation"])==(
        "Clavo",24,480,"hallheim")
    for k in ["actualTariffs","actualReceipts","actualPayments","actualRemittances"]: assert f[k]==[]
    j=d["justicePolicy"]
    for k in ["oneRoyalLaw","territorialRoyalJusticeDelegable","crownExtraordinaryReview",
              "judgeMustBeCompetent","guardCannotSentence","publicProceedingDefault",
              "defendantCanRespondAndPresentWitnesses","noModernJuryOrProsecutor","noTortureForConfession",
              "noReligiousOath","noOmniscientEvidence","nonTypifiedNotPunishable",
              "capitalConfirmationRequired","noOrdinaryLongPrisonSentence",
              "under12NoCriminalSentence","juvenileLimitsRequired"]:
        assert j[k] is True,k
    assert type(j["adultAge"]) is int and j["adultAge"]==18
    for k in ["actualJudges","actualHearings","actualSentences"]: assert j[k]==[]
    m=d["defencePolicy"]
    for k in ["crownSupremeCommand","houseGuardSeparateFromUrbanGuard","urbanGuardSeparateFromMilitary",
              "professionalForceSeparateFromReserve","houseMayDefendOwnTerritory",
              "noIndependentForeignWar","noHouseSovereignNavy","crownMustAuthorizeCampaignMobilization",
              "minorsNeverArmedCombatants","noEdranorCommandOverRodasBerserkers"]:
        assert m[k] is True,k
    assert type(m["minimumArmedAge"]) is int and m["minimumArmedAge"]==18
    for k in ["unitsInstantiated","recruitsInstantiated","armedIncidentsInstantiated","suppliesInstantiated"]:
        assert m[k]==[]
    p=d["protocol"]
    assert p["royalReceptionSeatReserved"] is p["royalApartmentsReserved"] is p["seatHigherPrecedenceWhenMonarchPresent"] is True
    assert p["roomsLocationVerified"] is p["royalVisitScheduled"] is False and p["royalProtocolStaffCount"] is None
    assert d["outsideScope"]=={"id":"hallheim","insideEdranor":False,"designed":False,"jurisdictionOwner":"crown_aethros"}
    assert len(d["hardConstraints"])==16 and all(v is True for v in d["hardConstraints"].values())
    assert "EDD-05_lord_and_heirs" in d["unresolved"] and "EDD-04_census" in d["unresolved"]
    assert "EDD-06" not in str(d["unresolved"])
    assert len(d["unresolved"])>=10 and len(set(d["unresolved"]))==len(d["unresolved"])
    assert set(d["instanceRegistry"])=={"officials","guardPersonnel","militaryPersonnel","units",
      "courts","taxObligations","taxReceipts","licenses","orders","cases","buildings"}
    assert all(v==[] for v in d["instanceRegistry"].values())
    assert d["runtimeClaims"]==[]

def authorized(e):
    if not isinstance(e,dict): return False
    if e.get("locality") not in OWNERS or e.get("actorOwner") not in {"casa_edranor","crown_aethros"}: return False
    action=e.get("action")
    def positive(*keys): return all(e.get(k) is True for k in keys)
    if not positive("authorityDocument","legalBasis","evidenceVerified","orderAuthentic"): return False
    owner=OWNERS[e["locality"]]
    if action in ("internal_customs","coin_mint"): return False
    if action=="royal_mobilization_review":
        return (e["actorOwner"]=="crown_aethros" and e["locality"]!="rodas" and
                positive("crownOrder","unitsSupplied"))
    if e["actorOwner"]!=owner: return False
    if action=="territorial_contribution":
        return positive("rightsVerified")
    if action=="service_fee":
        return positive("actualService","authorizedTariff")
    if action=="annual_wine_market":
        return e["locality"]=="lumina" and positive("annualEventVerified","rightsVerified")
    if action=="forest_timber_permit":
        return e["locality"]=="lumina" and positive("rightsVerified","forestSustainabilityVerified")
    if action=="public_inspection":
        return positive("mandateVerified","providerVerified")
    if action=="druid_house_access":
        return e["locality"]=="rodas" and positive("mandateVerified")
    if action=="berserker_order_review":
        return e["locality"]=="rodas" and positive("crownOrder","emergencyVerified")
    if action=="royal_justice_hearing":
        return positive("judgeDelegationVerified","accusedHeard") and (
            e.get("capitalSentence") is False or positive("capitalConfirmation"))
    if action=="armed_recruitment":
        return (type(e.get("legalAge")) is int and e["legalAge"]>=18
                and positive("personVerified","voluntary"))
    if action=="royal_reception":
        return e["locality"]=="dorth" and positive("royalVisitVerified","protocolObserved")
    return False

# Cross-phase regression against immutable canon anchors.
assert [x["id"] for x in e08["localityModels"]]==NAMES
assert [x["id"] for x in e07["settlements"]]==NAMES
assert e05["scope"]["physicalGraphValidated"] is False
for l in e08["localityModels"]:
    assert OWNERS[l["id"]]==l["jurisdictionOwner"]==l["fiscalOwner"]
    assert l["population"] is None and l["actualProviders"]==l["actualResidents"]==[]
assert e08["scope"]["demographicCensusApproved"] is False
for relative in DOCS:
    file=BASE/relative
    assert file.is_file() and file.stat().st_size>=500,relative
assert (ROOT/".github/workflows/edranor-e09.yml").is_file()
check(doc)

# Contract mutation safety: each tamper MUST fail.
mutations=[]
def mutate(path,value): mutations.append((path,value))
for k,value in [("schemaVersion",2),("documentId","false"),("date","2020"),("phase","E11"),
                ("version","1.0"),("status","ACTIVE"),("runtimeEnabled",True),
                ("inheritance",[]),("sourceAuthorities",[]),("protectedIds",[]),
                ("localityModels",[]),("institutionRoleCatalog",[]),
                ("authorizationCatalog",[]),("unresolved",[]),
                ("instanceRegistry",{}),("runtimeClaims",["loaded"])]:
    mutate([k],value)
for k in ["physicalGraphValidated","demographicCensusApproved","officeBuildingsValidated","crownDelegationsInstantiated"]:
    mutate(["scope",k],True)
for k in ["activeOfficeInstances","appointedPeople","createdUnits","createdGuardPosts","createdCourts",
          "issuedPermits","leviedTaxes","realCourtCases"]: mutate(["scope",k],1)
for k in ["effectivePopulation","edranorTaxRate","remittancePercentage","guardCount"]:
    mutate(["scope",k],100)
for i in range(4):
    for k in ["jurisdictionOwner","justiceOwner","fiscalOwner","securityOwner"]:
        mutate(["localityModels",i,k],"casa_edranor" if i==3 else "crown_aethros")
    mutate(["localityModels",i,"guardPersonnelCount"],10)
    mutate(["localityModels",i,"instantiatedOfficerIds"],["fictional_officer"])
mutate(["localityModels",3,"berserkerCommandOwner"],"casa_edranor")
mutate(["localityModels",3,"legalCategory"],"city")
mutate(["localityModels",1,"proceduralSpawnAllowed"],True)
mutate(["institutionRoleCatalog",8,"authorityOwner"],"casa_edranor")
mutate(["institutionRoleCatalog",5,"staffCount"],100)
mutate(["authorizationCatalog",0,"operational"],True)
mutate(["authorizationCatalog",1,"issuedIds"],["actual"])
for k in ["noInternalCustoms","noEdranorMint","crownRemittanceRequiresRegisteredShare"]:
    mutate(["fiscalPolicy",k],False)
mutate(["fiscalPolicy","clavosPerCorona"],20)
mutate(["fiscalPolicy","actualTariffs"],[2])
mutate(["justicePolicy","guardCannotSentence"],False)
mutate(["justicePolicy","capitalConfirmationRequired"],False)
mutate(["defencePolicy","minimumArmedAge"],15)
mutate(["defencePolicy","noEdranorCommandOverRodasBerserkers"],False)
mutate(["protocol","royalVisitScheduled"],True)
mutate(["hardConstraints","rodasIsCrown"],False)
mutate(["instanceRegistry","courts"],["real_court"])
for path,value in mutations:
    altered=copy.deepcopy(doc)
    target=altered
    for part in path[:-1]: target=target[part]
    target[path[-1]]=value
    try: check(altered)
    except (AssertionError,KeyError,TypeError): pass
    else: raise AssertionError(f"Mutation accepted: {path}")

assert lab["schemaVersion"]==1 and lab["documentId"]=="edranor_e09_synthetic_cases"
assert lab["phase"]=="E09" and lab["laboratoryOnly"] is lab["noCanonEvents"] is True
cases=lab["cases"]
assert len(cases)>=30 and len({c["id"] for c in cases})==len(cases)
passed=rejected=0
for case in cases:
    assert case["syntheticOnly"] is True and type(case["expected"]) is bool
    actual=authorized(case)
    assert actual is case["expected"],(case["id"],case["expected"],actual)
    passed+=actual
    rejected+=not actual

# Adversarial event mutations and authority leakage checks.
base=next(x for x in cases if x["id"]=="s02")
for field,value in [("actorOwner","crown_aethros"),("locality","rodas"),
                    ("authorityDocument",False),("legalBasis",False),("evidenceVerified",False),
                    ("orderAuthentic",False),("annualEventVerified",False),("rightsVerified",False)]:
    changed=dict(base,**{field:value})
    assert not authorized(changed),(field,value)
for name in NAMES:
    # Illegal customs always rejected independently of boundary.
    assert not authorized(dict(base,locality=name,actorOwner=OWNERS[name],action="internal_customs"))
for action in ["druid_house_access","berserker_order_review"]:
    assert not authorized(dict(base,locality="rodas",actorOwner="casa_edranor",action=action,crownOrder=True))
assert not authorized(dict(base,locality="dorth",actorOwner="casa_edranor",action="armed_recruitment",legalAge=17))
print(f"E09 PASS: {len(DOCS)} docs, {len(mutations)} contract mutations rejected, "
      f"{len(cases)} synthetic cases ({passed} accepted, {rejected} denied), "
      "cross-phase E05/E07/E08 anchors and hostile permission tests.")
