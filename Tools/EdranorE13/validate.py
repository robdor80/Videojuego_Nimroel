#!/usr/bin/env python3
"""Edranor E13: atlas de diseño, autoridad y pruebas adversariales; NO gameplay."""
from __future__ import annotations
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TERR = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
DATA = TERR / "Datos operativos"
JSON_E13 = DATA / "edranor_e13_physical_design_v0.1.json"
IDS = [
    "edr_e01_west_valkram_interface",
    "edr_e01_karsath_central_west",
    "edr_e01_lumina_bosque_alto",
    "edr_e01_central_wine_context",
    "edr_e01_dorth_azurios_west",
    "edr_e01_north_cold_transition",
    "edr_e01_far_north_unclosed",
]
PLACENAMES = ["dorth", "lumina", "karsath", "rodas", "hallheim"]
OWNERS = ["casa_edranor", "casa_edranor", "casa_edranor", "crown_aethros", "crown_aethros"]
SITE_BANDS = [(300,650),(650,900),(300,550),(400,950),None]
UNIT_BANDS = [(600,1600),(300,650),(650,1100),(200,650),(350,1500),(350,1150),None]
DEBTS = {
    "EDD-01": ("E19","OPEN"),
    "EDD-02": ("E19","OPEN"),
    "EDD-03": ("E19/E28","OPEN"),
    "EDD-04": ("E26","OPEN"),
    "EDD-05": ("E25","OPEN"),
    "EDD-06": ("E07/E12","RESOLVED_FOR_DESIGN"),
    "EDD-07": ("E16/E19/E28","OPEN"),
    "EDD-08": ("E27","OPEN"),
}
DOCS = [
    "00_AUTORIDAD_FUENTES_Y_AUDITORIA.md",
    "01_ATLAS_REGIONES_Y_SUBZONAS.md",
    "02_ALTIMETRIA_Y_MICRORRELIEVE_DE_DISENO.md",
    "03_MONTANAS_VALLES_Y_TOPONIMIA.md",
    "04_CUENCAS_RIOS_DRENAJE.md",
    "05_CLIMA_ESTACIONES_Y_RIESGOS.md",
    "06_SUELOS_ECOSISTEMAS_Y_APROVECHAMIENTO.md",
    "07_CARTOGRAFIA_2D_Y_FABRICA_DE_MUNDO.md",
    "08_MATRIZ_PARIDAD_DAROVAN_VALRIK_EDRANOR.md",
    "09_PLAN_MAESTRO_E13_E29.md",
    "10_GOBIERNO_DEUDA_Y_DECISIONES.md",
    "11_TRASPASO_E14.md",
    "12_AUDITORIA_SUFFICIENCIA_Y_ACTA.md",
    "README.md",
    "atlas_relaciones_esquematico_no_metrico.svg",
]

class AuditError(ValueError):
    pass

def require(condition, message):
    if not condition:
        raise AuditError(message)

def no_duplicates(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"clave duplicada JSON: {key}")
        result[key] = value
    return result

def read(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"), object_pairs_hook=no_duplicates)

def ids(rows, field="id"):
    return [row[field] for row in rows]

def safe_range(band, expected, *, with_geo=False):
    if expected is None:
        require(band is None, "norte no cerrado o Hallheim tienen cota ficticia")
        return
    require(isinstance(band, dict), "banda no es objeto")
    require(band.get("minM") == expected[0] and band.get("maxM") == expected[1],
            "banda de referencia delegada deriva o se invierte")
    require(band["minM"] <= band["maxM"] and band["minM"] >= 0, "intervalo de cota invalido")
    require(band.get("authority") == "ASSISTANT_DELEGATED_DESIGN"
            and band.get("measured") is False, "se falsea autoridad de banda")
    if with_geo:
        require(band.get("georeferenced") is False, "cota de unidad simulada como GIS")

def check(design, sources):
    e01,e02,e07,e10 = sources
    require(design.get("schemaVersion") == 1
            and design.get("phase") == "E13"
            and design.get("documentId") == "edranor_e13_physical_design"
            and design.get("status") == "DELEGATED_DESIGN_NOT_CANON"
            and design.get("runtimeEnabled") is False
            and design.get("worldStateEntitiesCreated") == 0
            and design.get("authority") == "ASSISTANT_DELEGATED_DESIGN",
            "contrato E13 se presenta como canon o runtime")
    require(design.get("sourceBaseMain") == "660fcf13b45916cb5df062303f40ef5168558af0"
            and design.get("inheritance") ==
               ["nimroel_core","norgard_defaults","casa_edranor","localidad","world_state"],
            "fuente base o jerarquia adulterada")
    require(design.get("sourceContractIds") == [
        "edranor_e01_relief","edranor_e02_hydrology",
        "edranor_e03_climate_soils_ecosystems","edranor_e07_canonical_nuclei",
        "edranor_e10_lore"], "falta precedencia contractual")
    require(e01.get("phase") == "E01" and e02.get("phase") == "E02"
            and e07.get("phase") == "E07" and e10.get("phase") == "E10",
            "contratos previos equivocados")
    require(ids(e01["reliefUnits"]) == IDS and len(IDS) == len(set(IDS)) == 7,
            "siete unidades canonicas E01")
    require(all(x["elevation"] == "UNKNOWN" for x in e01["reliefUnits"]),
            "E01 no debe convertir bandas E13 en cotas medidas")
    require(e01["cartography"]["northBoundaryClosed"] is False
            and e01["cartography"]["georeferenced"] is False,
            "E01 deja de proteger el recorte incompleto")
    m=design.get("map", {})
    require(m.get("sourceAuthorCrop") == "1000024893.jpg"
            and m.get("northBoundaryClosed") is False
            and m.get("metricGeometryValidated") is False
            and m.get("georeferenced") is False
            and m.get("coordinateSystem") is None
            and m.get("scaleMetersPerPixel") is None
            and m.get("polygonGeometry") == []
            and m.get("riverPolylines") == []
            and m.get("roadEdges") == []
            and m.get("heightfield") is None
            and m.get("svgIsOnlySchematic") is True,
            "georreferenciacion o geometria falsa")
    places=design.get("protectedPlaces", [])
    require(len(places) == 5 and ids(places)==PLACENAMES
            and ids(places,"owner")==OWNERS, "anclas y propietarios E13")
    require(ids(e07["settlements"]) == PLACENAMES[:4]
            and ids(e07["settlements"],"jurisdictionOwner")==OWNERS[:4],
            "E07 propiedad no coincide")
    require([x["kind"] for x in places] ==
            [x["type"] for x in e07["settlements"]] + ["outside"],
            "tipologia local, Rodas ALDEA")
    for i, p in enumerate(places):
        require(p.get("instantiated") is False
                and p.get("insideEdranor") is (i!=4), "localidad instanciada o Hallheim dentro")
        safe_range(p.get("siteReference"), SITE_BANDS[i])
    require(e07["settlements"][3]["berserkerCommandOwner"] == "crown_aethros"
            and e07["rights"]["rodasCommandedByEdranor"] is False,
            "mando berserker usurpado")
    units=design.get("physicalUnits",[])
    require(len(units)==7 and ids(units,"unitId")==IDS, "unidades E13 no reproducen E01")
    for i, u in enumerate(units):
        require(isinstance(u.get("landform"),str) and len(u["landform"])>7,
                "relieve sin caracterizacion")
        safe_range(u.get("altimetry"), UNIT_BANDS[i],with_geo=True)
        require(u.get("insideHouseTerritoryConfirmed") is (False if i==6 else None)
                and u.get("physicalGeometryValidated") is False
                and u.get("hydroReceiver")=="UNKNOWN"
                and u.get("soilSuitability")=="UNASSESSED"
                and u.get("climateLocalMeasured") is False
                and u.get("ecosystemMapped") is False
                and u.get("landUseInstantiated") is False,
                "unidad E13 indebidamente materializada")
    rh=design.get("regionalHydrology",[])
    require(ids(rh)==["lurien","antela"]
            and all(x.get("authority")=="CANON_REPO"
                    and x.get("membershipInEdranor")=="UNKNOWN"
                    and x.get("localGeometryValidated") is False
                    and x.get("localPolyline") is None for x in rh),
            "curso Lurien o lago Antela localizados sin evidencia")
    require([x["membershipInEdranor"] for x in e02["regionalCanonicalFeatures"]]
            == ["UNKNOWN","UNKNOWN"]
            and e02["scope"]["localHydrographyValidated"] is False,
            "E02 no certifica hidro local")
    catch=design.get("catchmentStudies",[])
    require(len(catch)==6 and ids(catch)==[f"ED13-H{i:02d}" for i in range(1,7)],
            "expedientes hidro E13")
    require(all(x.get("status")=="UNDELIMITED_STUDY_ONLY"
                and isinstance(x.get("question"),str)
                and x.get("receiverId") is None
                and x.get("polygon")==[]
                and x.get("localCourseCreated") is False for x in catch),
            "cuenca o receptor creados sin geometria")
    names=design.get("toponymCandidates",[])
    require(len(names)==8 and ids(names)==[f"ED13-T{i:02d}" for i in range(1,9)],
            "toponimia E13 faltante")
    require(len(set(x.get("candidateName") for x in names))==8
            and all(x.get("status")=="NAME_PROPOSAL_NOT_MAPPED"
                    and x.get("canonRatified") is False
                    and x.get("geometry") is None
                    and x.get("existingPlaceCreated") is False for x in names),
            "toponimo propuesto convertido a canon o lugar")
    require(design.get("hazardScenarioIds")==
            [f"ED13-F{i:02d}" for i in range(1,11)], "riesgos condicionales")
    routes=design.get("routeQuestions",[])
    require(len(routes)==4
            and ids(routes)==[
               "edr_e01_corridor_karsath_lumina",
               "edr_e01_corridor_lumina_dorth",
               "edr_e01_corridor_rodas",
               "edr_e01_corridor_valkram"]
            and all(x.get("status")=="STUDY_ONLY"
                    and x.get("roadConfirmed") is False for x in routes),
            "rutas fisicas no verificadas")
    require(len(e10["characters"])==11
            and e10["dynasty"]["legalSuccessionEstablished"] is False
            and e10["instantiatedNpcIds"]==[], "E10 no ratificado ni instanciado")
    debts=design.get("debts",[])
    require(len(debts)==8 and ids(debts)==list(DEBTS), "deudas EDD incompletas")
    require(all((x.get("responsiblePhase"),x.get("status"))==DEBTS[x["id"]]
                and x.get("evidenceRequired") is True for x in debts),
            "deuda no resuelta aparece cerrada o sin propietario")
    require(design.get("phases")==[f"E{i}" for i in range(13,30)],
            "E13-E29 no completos o avanzados")
    require(all(design.get(key) is True for key in (
               "noLocalHydrologyInstantiated","noNPCInstantiated",
               "noPopulationInstantiated","noNewRoadInstantiated",
               "noCanonSuperiorChanged","noNewHouseSovereignty")),
            "se inventa gameplay o soberania")
    require(design.get("generatedAssets")==["E13/atlas_relaciones_esquematico_no_metrico.svg"],
            "ausencia del plano esquematico")
    require(design.get("limitations")==[
            "EDD-01","EDD-02","EDD-03","EDD-04","EDD-05","EDD-07",
            "EDD-08","NOT_GODOT_TESTED","NOT_CORERPG_EDRANOR_RUNTIME"],
            "ocultacion de deudas")
    for name in DOCS:
        target=TERR/"E13"/name
        require(target.is_file() and target.stat().st_size>120,
                f"entregable E13 ausente o vacio: {name}")
    for name in ["E13_INDICE.md","PLAN_DESARROLLO_EDRANOR_E13_E29.md"]:
        require((TERR/name).is_file(),f"falta documento de gobierno: {name}")

def inject(obj, path, value):
    node=obj
    for item in path[:-1]:
        node=node[item]
    node[path[-1]]=value

def negative_cases(document):
    changes=[
        ("activa runtime",["runtimeEnabled"],True),
        ("materializa WorldState",["worldStateEntitiesCreated"],1),
        ("canoniza nivel",["status"],"CANON_REPO"),
        ("autoridad inventada",["authority"],"AUTOR_EXPRESO"),
        ("altera jerarquia",["inheritance",0],"casa_edranor"),
        ("desplaza fuente",["sourceBaseMain"],"0"*40),
        ("cierra norte",["map","northBoundaryClosed"],True),
        ("geometria verificada",["map","metricGeometryValidated"],True),
        ("coordenadas verificadas",["map","georeferenced"],True),
        ("CRS sin mapa",["map","coordinateSystem"],"EPSG:4326"),
        ("escala falsa",["map","scaleMetersPerPixel"],20),
        ("poligono falso",["map","polygonGeometry"],[[[0,0],[1,0],[0,1]]]),
        ("rio trazado",["map","riverPolylines"],[{"id":"lurien"}]),
        ("red viaria inventada",["map","roadEdges"],[["dorth","lumina"]]),
        ("heightfield inventado",["map","heightfield"],[[0,1]]),
        ("SVG cartografia exacta",["map","svgIsOnlySchematic"],False),
        ("Rodas pasa a Casa",["protectedPlaces",3,"owner"],"casa_edranor"),
        ("Rodas elevada a ciudad",["protectedPlaces",3,"kind"],"city"),
        ("Rodas fuera",["protectedPlaces",3,"insideEdranor"],False),
        ("Hallheim dentro",["protectedPlaces",4,"insideEdranor"],True),
        ("Hallheim recibe altitud",["protectedPlaces",4,"siteReference"],{"minM":0,"maxM":20,"authority":"ASSISTANT_DELEGATED_DESIGN","measured":False}),
        ("lugar instanciado",["protectedPlaces",0,"instantiated"],True),
        ("cota urbana medida",["protectedPlaces",1,"siteReference","measured"],True),
        ("cota urbana alterada",["protectedPlaces",0,"siteReference","maxM"],750),
        ("unidad duplicada",["physicalUnits",1,"unitId"],IDS[0]),
        ("unidad cota invertida",["physicalUnits",0,"altimetry","minM"],1700),
        ("unidad cota georeferenciada",["physicalUnits",2,"altimetry","georeferenced"],True),
        ("unidad cota canonica",["physicalUnits",0,"altimetry","authority"],"AUTOR_EXPRESO"),
        ("norte con cota",["physicalUnits",6,"altimetry"],{"minM":0,"maxM":100}),
        ("norte propiedad confirmada",["physicalUnits",6,"insideHouseTerritoryConfirmed"],True),
        ("suelo declarado apto",["physicalUnits",3,"soilSuitability"],"APTO"),
        ("receptor local inventado",["physicalUnits",4,"hydroReceiver"],"caleran"),
        ("clima medido falsamente",["physicalUnits",0,"climateLocalMeasured"],True),
        ("ecosistema cartografiado",["physicalUnits",2,"ecosystemMapped"],True),
        ("cultivo instanciado",["physicalUnits",3,"landUseInstantiated"],True),
        ("Antela dentro",["regionalHydrology",1,"membershipInEdranor"],"TRUE"),
        ("Lurien dibujado",["regionalHydrology",0,"localPolyline"],[[0,0],[1,1]]),
        ("cuenca delimitada",["catchmentStudies",0,"polygon"],[[0,0],[1,1]]),
        ("cuenca con receptor",["catchmentStudies",2,"receiverId"],"lurien"),
        ("cuenca convertida en hecho",["catchmentStudies",1,"status"],"CANON"),
        ("crea curso local",["catchmentStudies",0,"localCourseCreated"],True),
        ("nombre canonizado",["toponymCandidates",0,"canonRatified"],True),
        ("nombre con sitio",["toponymCandidates",1,"existingPlaceCreated"],True),
        ("nombre mapeado",["toponymCandidates",2,"geometry"],{"x":1,"y":2}),
        ("nombre presentado como canon",["toponymCandidates",3,"status"],"CANON_REPO"),
        ("ruta confirmada",["routeQuestions",0,"roadConfirmed"],True),
        ("desaparece EDD-01",["debts",0,"status"],"RESOLVED"),
        ("sucesion confirmada",["debts",4,"status"],"RESOLVED"),
        ("Rodas vuelve a deuda",["debts",5,"status"],"OPEN"),
        ("deuda sin prueba",["debts",6,"evidenceRequired"],False),
        ("se omite E29",["phases",16],"E28"),
        ("riesgo duplicado",["hazardScenarioIds",9],"ED13-F09"),
        ("se elimina limitacion",["limitations",0],"NOT_OPEN"),
        ("se usurpa soberania",["noNewHouseSovereignty"],False),
        ("se activa NPC",["noNPCInstantiated"],False),
        ("activo cartografico falso",["generatedAssets",0],"E13/terrain_metric.geojson"),
    ]
    return changes

def main():
    sources=[read(DATA/n) for n in (
        "edranor_e01_relief_v0.1.json","edranor_e02_hydrology_v0.1.json",
        "edranor_e07_canonical_nuclei_v0.1.json","edranor_e10_lore_v0.1.json")]
    design=read(JSON_E13)
    check(design,sources)
    negatives=negative_cases(design)
    for title,path,value in negatives:
        mutated=copy.deepcopy(design)
        inject(mutated,path,value)
        try:
            check(mutated,sources)
        except AuditError:
            pass
        else:
            raise AuditError("mutacion adversarial NO rechazada: "+title)
    print(f"E13 PASS | 7 unidades | 5 anclas | 6 expedientes hidro | 8 nombres no canonicos | 8 EDD | 17 fases | {len(negatives)} mutaciones negativas PASS")
    return 0

if __name__=="__main__":
    try:
        sys.exit(main())
    except (AuditError,ValueError,KeyError,IndexError,TypeError,FileNotFoundError) as exc:
        print(f"E13 FAIL: {exc}",file=sys.stderr)
        sys.exit(1)
