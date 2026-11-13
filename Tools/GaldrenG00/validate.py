"""Galdren G00: chequeo documental y pruebas de mutación; NO ejecuta CoreRPG ni Godot."""
import copy
import json
from pathlib import Path

repo = Path(__file__).resolve().parents[2]
n = repo / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard"
base = n / "Territorios/Casa Galdren"
manifest_path = base / "Datos operativos/galdren_g00_manifest_v0.1.json"
d = json.loads(manifest_path.read_text(encoding="utf-8"))

def validate(x):
    assert x["schemaVersion"] == 1 and x["phase"] == "G00"
    assert x["documentId"] == "galdren_g00"
    assert x["runtimeEnabled"] is False and x["status"] == "DOCUMENTARY_PLANNING_ONLY"
    pr = x["provenance"]
    assert pr["redPerimeterIsApproximate"] is True
    for p in ("imageCommittedToRepository","metricGeometryValidated","coordinatesValidated","borderTopologyValidated","scaleForTerritoryValidated"):
        assert pr[p] is False, p
    assert x["inheritance"] == ["nimroel_core","norgard_defaults","casa_galdren","localidad","world_state"]
    h = x["house"]
    assert h["id"] == "casa_galdren" and h["seatId"] == "arleon" and h["polityId"] == "norgard"
    assert h["sovereign"] is False
    assert h["heraldry"] == {"figure":"toro","metal":"hierro_ennegrecido_acero_oscuro_envejecido","field":"dorado_trigo_envejecido"}
    assert set(h["economy"]) == {"agricultura","ganaderia","mineria_zanthir","armas_y_herramientas_zanthir"}
    loc = {p["id"]:p for p in x["locations"]}
    assert len(loc) == len(x["locations"]) and len(loc) == 6
    assert set(x["protectedIds"]) == {"arleon","zanthir","forja_estelar","treskal","hallheim","dorth"}
    assert all(loc[p]["procedural"] is False for p in loc)
    assert loc["arleon"]["jurisdictionOwner"] == "casa_galdren"
    assert loc["zanthir"]["jurisdictionOwner"] == "casa_galdren"
    assert loc["zanthir"]["settlementScale"] == "UNKNOWN"
    forge = loc["forja_estelar"]
    assert forge["role"] == "INSTALACION_ESTRATEGICA"
    assert forge["jurisdictionOwner"] == "UNKNOWN"
    assert forge["ownershipTitle"] == "UNKNOWN"
    assert forge["peacetimeTerritorialAdministration"] == "casa_galdren"
    assert forge["wartimeStrategicCommand"] == "crown_aethros_hallheim"
    assert forge["settlementScale"] == "NOT_A_SETTLEMENT"
    for k,owner in (("treskal","casa_valrik"),("hallheim","crown_aethros"),("dorth","casa_edranor")):
        assert loc[k]["jurisdictionOwner"] == owner and loc[k]["insideGaldrenPerimeter"] is False
    gov = x["government"]
    assert gov == {"singleCrown":True,"singleLaw":True,"houseSovereign":False,"ownCurrency":False,"internalCustoms":False,"independentWarPower":False,"crownWartimeForgeCommand":True,"royalJustice":True}
    p = x["toponymPolicy"]
    assert p == {"newNamesRequireRatification":True,"fictionalEtymologyWithoutSourceForbidden":True,"legalBordersNotDerivedFromNaturalFeatures":True,"unverifiedProposalsCount":0}
    topo = x["canonToponyms"]
    assert len(topo) >= 18 and len(set(t["id"] for t in topo)) == len(topo)
    assert all(t["canonStatus"] == "CANON_REPO" and t["galdrenJurisdiction"] == "NOT_INFERRED" and t["newlyCoined"] is False for t in topo)
    names={t["name"] for t in topo}
    for needle in ("Río Caleran","Río Vornarsk","Río Keldarsk","Montes Azurios","Montes Invernos","Bahía de Zanthir","Bosque Quebrado","Los Gemelos de Treskal"):
        assert needle in names,needle
    assert x["plannedPhases"] == ["G"+str(i).zfill(2) for i in range(13)]
    assert all(isinstance(v,str) and v for v in x["unknown"])
    assert "BORDER_VALRIK" in x["unknown"] and "FORGE_OWNERSHIP_TITLE" in x["unknown"]
    assert len(x["sourceRegistry"]) >= 18 and len(set(x["sourceRegistry"])) == len(x["sourceRegistry"])
    assert pr["baselineMainSha"] == "b3edd92ab164ad4b4c2ee0c67e8048386a3d950f"

validate(d)
for src in d["sourceRegistry"]:
    assert (repo / src).is_file(), "Fuente ausente: "+src
for f in (
    "README.md","PLAN_MAESTRO_GALDREN_v0.1.md","Auditorias/G00_AUDITORIA.md",
    "Cartografia/G00_CARTOGRAFIA.md","Identidad_y_politica/G00_IDENTIDAD.md",
    "Toponimia/G00_REGISTRO_TOPONIMIA.md","Auditorias/G00_ACTA.md",
    "00_Control_del_proyecto/TRASPASO_G01.md"
):
    assert (base / f).is_file(), "Documento G00 ausente: "+f
plan=(base/"PLAN_MAESTRO_GALDREN_v0.1.md").read_text(encoding="utf-8")
assert all("**G"+str(i).zfill(2)+"**" in plan for i in range(13))
assert "PROPUESTA_NO_CANON" in plan
assert "Treskal" in (base/"Cartografia/G00_CARTOGRAFIA.md").read_text(encoding="utf-8")
mutations = [
    lambda x:x.update(runtimeEnabled=True),
    lambda x:x["provenance"].update(metricGeometryValidated=True),
    lambda x:x["provenance"].update(coordinatesValidated=True),
    lambda x:x["provenance"].update(borderTopologyValidated=True),
    lambda x:x["house"].update(sovereign=True),
    lambda x:x["house"].update(seatId="treskal"),
    lambda x:x["house"]["heraldry"].update(figure="ciervo"),
    lambda x:x["locations"][0].update(procedural=True),
    lambda x:x["locations"][1].update(settlementScale="CIUDAD_CANONICA"),
    lambda x:x["locations"][2].update(peacetimeTerritorialAdministration="casa_valrik"),
    lambda x:x["locations"][2].update(wartimeStrategicCommand="casa_galdren"),
    lambda x:x["locations"][2].update(jurisdictionOwner="casa_galdren"),
    lambda x:x["locations"][2].update(role="SEDE"),
    lambda x:x["locations"][3].update(jurisdictionOwner="casa_galdren"),
    lambda x:x["locations"][3].update(insideGaldrenPerimeter=True),
    lambda x:x["locations"][4].update(insideGaldrenPerimeter=True),
    lambda x:x["government"].update(houseSovereign=True),
    lambda x:x["government"].update(ownCurrency=True),
    lambda x:x["government"].update(internalCustoms=True),
    lambda x:x["government"].update(independentWarPower=True),
    lambda x:x["government"].update(crownWartimeForgeCommand=False),
    lambda x:x["toponymPolicy"].update(newNamesRequireRatification=False),
    lambda x:x["toponymPolicy"].update(unverifiedProposalsCount=1),
    lambda x:x["canonToponyms"][0].update(newlyCoined=True),
    lambda x:x["canonToponyms"][0].update(galdrenJurisdiction="casa_galdren"),
    lambda x:x["canonToponyms"].append(copy.deepcopy(x["canonToponyms"][0])),
    lambda x:x["plannedPhases"].pop(),
    lambda x:x["sourceRegistry"].append(x["sourceRegistry"][0])
]
for i,mut in enumerate(mutations,1):
    bad=copy.deepcopy(d)
    mut(bad)
    try:
        validate(bad)
    except (AssertionError,KeyError,TypeError):
        pass
    else:
        raise AssertionError(f"Mutación indebida aceptada: {i}")
print(f"GALDREN G00 STATIC PASS | {len(d['sourceRegistry'])} fuentes | {len(mutations)} mutaciones negativas rechazadas | {len(d['canonToponyms'])} topónimos previos")
