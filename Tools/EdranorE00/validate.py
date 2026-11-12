"""Prueba estática E00. No implementa ni ejecuta el RPG."""
import copy
import json
from pathlib import Path

repo=Path(__file__).resolve().parents[2]
n=repo/"Worldbuilding/Reinos/Reinos de los Hombres/Norgard"
base=n/"Territorios/Casa Edranor"
doc=base/"Datos operativos/edranor_e00_manifest_v0.1.json"
data=json.loads(doc.read_text(encoding="utf-8"))

def check(x):
    assert x["schemaVersion"]==1 and x["phase"]=="E00"
    assert x["runtimeEnabled"] is False
    assert x["provenance"]["metricGeometryValidated"] is False
    assert x["provenance"]["northernLimitClosedInCrop"] is False
    assert x["inheritance"]==["nimroel_core","norgard_defaults","casa_edranor","localidad","world_state"]
    assert x["house"]["id"]=="casa_edranor" and x["house"]["seatId"]=="dorth"
    assert x["house"]["emblem"]["figure"]=="ciervo_gran_cornamenta"
    assert "vino" in x["house"]["economy"]
    loc={p["id"]:p for p in x["locations"]}
    assert len(loc)==len(x["locations"])
    assert set(x["protectedIds"])=={"dorth","lumina","karsath","rodas","hallheim"}
    for k in ("dorth","lumina","karsath"):
        assert loc[k]["jurisdictionOwner"]=="casa_edranor" and loc[k]["procedural"] is False
    assert loc["rodas"]["geographicContextHouse"]=="casa_edranor"
    for prop in ("jurisdictionOwner","militaryOwner","fiscalOwner"):
        assert loc["rodas"][prop]=="crown_aethros"
    assert loc["rodas"]["procedural"] is False
    assert loc["rodas"]["settlementClassification"].startswith("ALDEA_AUTHOR_")
    assert loc["hallheim"]["jurisdictionOwner"]=="crown_aethros"
    assert loc["hallheim"]["insideEdranorPerimeter"] is False
    assert x["government"]=={"singleCrown":True,"singleLaw":True,"houseSovereign":False,"houseControlsRodas":False,"houseCommandsBerserkers":False,"internalCustoms":False}
    assert next(e for e in x["ecosystems"] if e["id"]=="far_north")["viticultureByDefault"] is False

check(data)
sources=[
 n/"Grandes Casas/grandes_casas.md",n/"NORGARD.md",
 n/"Geografía/bosques.md",n/"Geografía/regiones_naturales.md",
 n/"Geografía/montanas.md",n/"Clima/clima_general.md",
 n/"Territorios/README.md",repo/"Worldbuilding/Sistemas/Nimroel Core/README.md",
 repo/"Worldbuilding/Sistemas/Norgard Defaults/README.md",
 repo/"Worldbuilding/Direccion artistica/Biblia visual/Culturas/Norgard/Datos operativos/norgard_regions_v0.1.json"
]
for src in sources:
    assert src.is_file(), f"Fuente ausente: {src}"
for relative in (
 "README.md","PLAN_DESARROLLO_EDRANOR_v0.1.md",
 "Cartografia/E00_MAPA_Y_LIMITES.md","Auditorias/E00_AUDITORIA.md",
 "Auditorias/E00_ACTA.md","Identidad_y_politica/E00_IDENTIDAD.md",
 "00_Control_del_proyecto/TRASPASO_E01.md"
):
    assert (base/relative).is_file(), relative

mutations=[
 lambda x:x.update(runtimeEnabled=True),
 lambda x:x["provenance"].update(metricGeometryValidated=True),
 lambda x:x["provenance"].update(northernLimitClosedInCrop=True),
 lambda x:x["locations"][3].update(jurisdictionOwner="casa_edranor"),
 lambda x:x["locations"][3].update(militaryOwner="casa_edranor"),
 lambda x:x["locations"][3].update(fiscalOwner="casa_edranor"),
 lambda x:x["locations"][3].update(procedural=True),
 lambda x:x["locations"][4].update(insideEdranorPerimeter=True),
 lambda x:x["locations"][0].update(procedural=True),
 lambda x:x["house"].update(seatId="hallheim"),
 lambda x:x["government"].update(houseControlsRodas=True),
 lambda x:x["government"].update(internalCustoms=True),
 lambda x:x["ecosystems"][2].update(viticultureByDefault=True),
 lambda x:x["protectedIds"].remove("rodas")
]
for i,mut in enumerate(mutations,1):
    bad=copy.deepcopy(data);mut(bad)
    try:check(bad)
    except AssertionError:pass
    else:raise AssertionError(f"Mutación incorrecta aceptada: {i}")
print(f"EDRANOR E00 STATIC PASS | {len(sources)} fuentes verificadas | {len(mutations)} casos negativos rechazados")
