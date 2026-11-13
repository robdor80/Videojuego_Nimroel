# G03 — Fuentes, decisiones y deuda verificable
**Base cerrada antes de trabajar:** `main` SHA `1ad65cb5eb5dd449c6dd981cba3b63d96435d69f` (G02 PR #67 fusionada). La fase añade documentación ambiental de Galdren exclusivamente, sin cambios en Norgard superior, Edranor, Valrik, CoreRPG ni Godot.

## Trazabilidad de las decisiones
| Fuente versionada | Aporta | Regla G03 |
|---|---|---|
| `Norgard/Clima/clima_general.md` | Costa oceánica oriental, interior continental, norte frío y polar; hielo Vornarsk/Keldarsk | Franjas regionales, **NO** temperatura de Arleon/Zanthir extrapolada |
| `Norgard/Geografía/regiones_naturales.md` | Llanura oriental fértil y frontera natural no política | Fertilidad regional ≠ aptitud de cada parcela |
| `Norgard/Geografía/bosques.md` | Quebrado, Camino Real, Riberas, Gemelos, composición y caballos | Bosques y especies existentes, sin otros nombres/taxones ni ocupación política |
| `Norgard/Geografía/mares_y_costas.md` | Bahía Zanthir y hielo septentrional; Suthiros | Riesgo litoral cualitativo; sin puertos ni límites costeros |
| `Norgard/Geografía/montanas.md` | Azurios, Invernos, Velaris | Microclima por relieve solo investigable |
| `Norgard/Geografía/Montes Invernos/cotas_y_altitudes_borrador.md` | Deshielo y nieve regional; glaciares pendientes | Sin cota Galdren ni glaciar ratificado |
| G01 atlas y contrato | Doce unidades, seis interfaces, límites no georreferenciados | Correspondencia uno-a-uno de los doce perfiles |
| G02 atlas, riesgos, contrato y traspaso | Caleran uno, dos brazos; dos ríos helados; cuencas sin límites | No dibujar afluentes, canales, crecidas ni bocas |
| Edranor E03 (precedente) | Método de incertidumbres suelo/clima | No importar clima, viticultura, parcelas o bosques propios de Edranor |

## Registro de decisiones
- **G03-D01:** la *tipología de estudio* no es mapa de clima local: medidas de lluvia/temperatura, viento, helada y humedad faltan.
- **G03-D02:** la fertilidad oriental **CANON** y la aptitud de cada parcela **UNASSESSED** coexisten legítimamente.
- **G03-D03:** Bosque Quebrado como región caballar **CANON**, pero raza, censo, rendimiento y titularidad **UNKNOWN**.
- **G03-D04:** Zanthir no comparte régimen agrícola uniforme con Arleon; se conserva hielo norteño cualitativo.
- **G03-D05:** la franja polar es **REGIONAL**; pertenencia concreta a Galdren sin cartografiar.
- **G03-D06:** no glaciares permanentes, humedales con nombre, puertos, especies nuevas ni polígonos de bioma.
- **G03-D07:** los riesgos no medidos siguen `STUDY_ONLY`; no se convierten en eventos por redactarlos.
- **G03-D08:** las referencias de Treskal/Gemelos son Valrik y de Dorth/Edranor y Hallheim/Corona no se alteran.

## Deuda heredada y deuda nueva
Heredada: `GDD-01/02/03/07`, `G02-D01..08`, transición occidental→oriental Caleran, alturas/vertientes Invernos, titularidad Forja, delimitaciones jurídicas, cursos secundarios, red viaria y calendario. Nueva: series de observación regionales, perfiles y muestras de suelo, parcelario y derechos, mapas de exposición al riesgo, pertenencia de biomas al territorio, censo de fauna y especies, inventario de recursos y rendimiento, estacionalidad local de cultivos/ganadería.

## Pruebas exigidas para cierre
1. JSON que preserve 12 perfiles de G01, fuentes existentes, estados de evidencia y restricciones cardinales.
2. Mutaciones negativas que fallen al intentar promover hipótesis, georreferenciar, anexionar vecinos, inventar ríos/hábitats, suelos o datos numéricos.
3. G00/G01/G02/G03 en **Windows 2022 y Ubuntu 24.04** para el mismo HEAD; diff solo Galdren, Tools/GaldrenG03 y workflow.
4. El acta debe decir expresamente **documental**, no runtime, y dejar G04 sin iniciar.