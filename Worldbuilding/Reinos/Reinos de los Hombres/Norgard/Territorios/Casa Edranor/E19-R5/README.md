# E19-R5 — Asentamientos, habitabilidad y ocupación territorial
**Fecha:** 14-11-2026. **Estado:** B2 documental / hipótesis trazables, NO mapa certificado B3 ni simulación B4. **Autoridad:** diseño delegado dentro del canon existente; no altera cifras, fronteras ni instituciones.

## Objeto
Completar la capa de ocupación del atlas causal de Casa Edranor. Se adopta el estándar **metodológico** de Casa Valrik/Treskal: **esqueleto mínimo → posibilidades → coherencia regional → pesos condicionados → generación de instancia → persistencia**. No se heredan los rangos demográficos 35–100 / 350–900 / 2.000–4.500 de Valrik ni los mínimos de taberna/herrería como obligaciones universales de Edranor: son reglas **territoriales Valrik**, no legislación general de Norgard.

## Alcance real y genealogía
R5 se apila sobre el HEAD de E19-R4 `17664ebd54f9553d1a652c79f4a851c169da629c` (PR #92), precedido por R3 #91, R2 #90, R1 #89 y R0 #87. Se conserva B2. El grafo físico Gp de R4 tiene **cero nodos/aristas certificados**: ninguna vivienda, parcela, recurso o asentamiento nuevo puede declararse accesible gracias a una pregunta CT. E14 ya definió usos y 24 programas de estudio, no 24 lugares; E06 propone arquetipos y elegibilidad; E08 prohíbe censos supuestos; E07 protege cinco lugares; R1–R3 describen contextos y peligros, no terrenos medidos.

## Archivos
| Archivo | Tema |
|---|---|
| 01_JERARQUIA_Y_AUTORIDAD.md | Canon, seis niveles de ocupación, excepciones regias |
| 02_ESQUELETOS_ASENTAMIENTOS.md | Aldea/pueblo/villa, fijos frente a procedurales, indispensables/opcionales |
| 03_ATLAS_OCUPACION_CONTEXTOS.md | MF-01…MF-08; estudios OS, no núcleos |
| 04_HABITABILIDAD_Y_CAPACIDAD.md | Decisiones, agua, saneamiento, suelo, clima, red vial y derechos |
| 05_COBERTURA_REGIONAL_SERVICIOS.md | Grafo demanda/oferta/acceso; interdependencia Valrik |
| 06_ECONOMIA_USOS_Y_PAISAJE.md | Vino, alimento, madera, trabajo estacional y paisaje |
| 07_HOGARES_VIVIENDAS_CENSO.md | Persona, hogar, vivienda, propiedad, empleo, presencia |
| 08_RIESGOS_ESTACIONES_CAMBIO.md | Capacidad dinámica, invierno, vendimia, deterioro y decisiones |
| 09_CONTRATO_B3_B4.md | Promoción cartográfica y runtime, IDs y procedencia |
| 10_PARIDAD_VALRIK_ADVERSARIOS.md | Matriz de paridad y antiejemplos |
| 11_ACTA_Y_TRASPASO_R6.md | Cierre B2 condicionado, brechas y sucesores |
| occupation_v0.6.json | Contrato de hipótesis, vetos y deudas |
| Tools/EdranorE19R5/validate.py | Integridad + mutaciones adversariales |
| .github/workflows/edranor-e19-r5.yml | Regresiones R0–R5 Linux/Windows |

## Semántica irrenunciable
**Programa OS ≠ emplazamiento ≠ asentamiento ≠ World State.** Un paisaje plausible NO es un derecho, un pozo, una calzada, una parcela o un hogar. Toda carencia `UNKNOWN` bloquea promoción real, no equivale a «no existe» ni a «disponible». Las cifras sintéticas sirven para probar balances, nunca para poblar el reino. La instancia futura queda guardada una vez, con referencias entre persona, hogar, inmueble, trabajo, proveedor, ruta y estado; no se multiplica por volver a una escena.

## Anclas
Dorth (sede/tintos), Lumina (blancos, plaza alargada/mercado anual y Bosque Alto), Karsath (producción vinícola escasa, Antela al sur sin ribera urbana acreditada) son **núcleos canónicos de diseño manual**, no candidatos al generador. **Rodas es ALDEA regia de Aethros**: no censo, impuestos, administración ni mando Edranor. Hallheim es exterior. Bosque Alto requiere licencias y regeneración; Bosque Real pertenece a Corona; MF-08/U7 es NO EVALUABLE.

## Criterio de cierre
La prueba de JSON y escenarios sintéticos solo acredita consistencia B2. R6 auditará paridad final y E19-TEC necesitará levantamiento y geometría B3; E28/CoreRPG gestionarán mundo persistido B4 bajo contratos propios. No tocar `main`, ramas parentales, otras Casas, `Game`, `ContentPacks` ni `CoreRPG`.
