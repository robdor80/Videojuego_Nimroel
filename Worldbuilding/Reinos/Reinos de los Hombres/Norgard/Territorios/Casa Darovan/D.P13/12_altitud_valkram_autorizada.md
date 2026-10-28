# D.P13 — Altimetría canónica aprobada: Montes Valkram

**Fecha de aprobación:** 25-10-2026 · **Autoridad:** decisión expresa del autor en la conversación D.P13 · **Fase:** D.P13 · **Estado:** AUTHORED (nuevas decisiones), sin cartografía métrica ni runtime.

## Resolución autoral de altitud — 25 de octubre de 2026

**DAR-DP13-ALT-01 (APROBADA):** Montes Valkram, **opción B**: cordillera muy alta. Rango orientativo de **3.600–4.200 m para las grandes cumbres**, no para la totalidad del macizo ni cada montaña individual. Es una escala de diseño expresamente aprobada por el autor; las cotas de valles, cumbres secundarias, pasos, cabeceras y localidades permanecen sin definir.

**DAR-DP13-ALT-02 (APROBADA):** una cumbre excepcional situada en el **sector norte de Valkram**, representada en el mapa del autor **entre la N y la O del rótulo «NORGARD»**, es **la mayor elevación de todo Norgard** y alcanza **aproximadamente 4.200 metros sobre el nivel del mar**. Su nombre propio **ha sido aprobado posteriormente como «la Viuda»** (DAR-DP13-ALT-03). Las coordenadas, laderas exactas, jurisdicción precisa, etimología, extensión nival y existencia de glaciares permanecen **UNKNOWN**. «Cumbre septentrional de Valkram» es una descripción, NO un topónimo nuevo.

**Compatibilidad transversal pendiente:** `Geografía/montanas.md` define los Montes Azurios como más altos, anchos y abruptos en términos generales. La elección más reciente del autor fija una **excepción puntual de altura máxima absoluta** para Valkram, compatible con un sistema Azurios globalmente más elevado/abrupto, pero se requiere armonización editorial futura a escala de Norgard para eliminar ambigüedades. **No se cambia la ficha superior en D.P13.**

**Registro operativo:** `Datos operativos/darovan_dp13_valkram_altitude_authorial_v0.1.json`. Esta nueva decisión autoral no contradice la protección del perfil antiguo `darovan_dp13_physical_profiles_v0.1.json`, cuyos campos nulos corresponden a zonas de estudio sin cota única, no a las nuevas anclas individuales aprobadas.


## Resolución posterior de toponimia — 25/10/2026

**DAR-DP13-ALT-03 (APROBADA):** la cumbre de aproximadamente **4.200 m**, ubicada en el **norte de los Montes Valkram** entre las letras N y O del rótulo del mapa, recibe el nombre oficial exacto de **la Viuda**. Es la montaña más alta de Norgard. No se ha aprobado todavía una etimología, leyenda o coordenada métrica. Los registros anteriores que indican «nombre UNKNOWN» son **históricos y han quedado superados** por esta decisión expresa del autor.

## Justificación y empleo físico

1. La escala de las **grandes cumbres** permite establecer un marco para gradientes térmicos, retención de nieve, deshielo y cabeceras, pero **no fija** espesores, lluvias, umbrales de nieve ni número de arroyos.
2. La cumbre de referencia solo queda localizada **aproximadamente en la ilustración**, no mediante latitud/longitud, coordenadas de píxel como GIS o contornos de cuenca.
3. La diferencia entre **altura máxima absoluta** y **altura/prominencia/abruptidad media de una cordillera** debe mantenerse explícita en toda comparación Valkram/Azurios.
4. El nombre aprobado es **la Viuda**. No asignar etimología ni adscripción política por proximidad a una Casa concreta.
5. No trasladar alturas de los Montes Invernos a Valkram; Invernos conserva sus propias escalas de borrador.
6. La ubicación aproximada del pico no certifica el nacimiento de ningún río bajo él, ni un glaciar permanente. Conservar la vertiente occidental septentrional canónica como origen general del Belara.

## Lo todavía pendiente

Cotas típicas de valle/piedemonte, altura de collados, cima secundaria, relieve de Taramin/Syvaris/Arven, modelado de laderas y cuencas; rosas de viento y régimen de nieve. **Elyra ya tiene aprobado un techo orientativo de cumbres de ~2.600 m**, documentado en `13_altitud_elyra_autorizada.md`. Resolver mediante decisiones posteriores individualizadas.

## Enlace de fuente

- [Montañas de Norgard](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/montanas.md): anterior definición comparativa.
- Referencia autoral primaria: intervención directa del autor en la conversación D.P13 del **25/10/2026**, acompañada de recorte del mapa de Norgard. El archivo original de imagen no se publica como recurso por el mero hecho de usar su contenido como referencia.

## Decisión autoral DAR-DP13-SNOW-01 — Neveros permanentes en la Viuda (25/10/2026)

**APROBADA — opción B.** En **la Viuda**, cumbre septentrional de los Montes Valkram (~4.200 m), **existen acumulaciones de nieve (neveros) que sobreviven al verano en sectores altos y protegidos**. Se confirma la persistencia localizada de nieve de un año a otro; **no** se afirma que todo el pico permanezca nevado ni que exista un límite altitudinal de nieve uniforme para el conjunto de Valkram.

**No se han aprobado glaciares** con esta decisión. Su existencia real sigue **UNKNOWN**, no debe darse por demostrada ni descartada definitivamente sin otra decisión autoral. No se fijan tamaños, volúmenes, espesores, cotas de aparición, localización métrica de neveros, fechas de deshielo ni caudales. La aportación hídrica por fusión es una **posibilidad causal derivada**, no un nuevo nacimiento de río ni una cuantificación.

**Fuente autoral:** elección expresa de opción B a la pregunta 3 de D.P13, 25 de octubre de 2026.

**Registro estructurado:** `Datos operativos/darovan_dp13_valkram_altitude_authorial_v0.1.json` → `worldHighestSummit.snowPersistence` y `snowPersistenceDetail`. Referencias anteriores a «nieve permanente UNKNOWN» en registros históricos quedan parcialmente superadas **solo para la Viuda**; el régimen del resto de Valkram/Elyra permanece por definir.


## DAR-DP13-PASS-01 — Altitudes orientativas de los principales pasos de Valkram (25/10/2026)

**Decisión expresa del autor: OPCIÓN B (APROBADA).** Los principales **pasos naturales** practicables de los Montes Valkram tendrán un **rango de referencia aproximado de 1.400 a 2.200 metros sobre el nivel del mar**.

Este intervalo describe la **categoría general de los pasos principales**, no la cota de todos los collados, ni una obligación de distribuirlos uniformemente en esas alturas. Pueden existir relieves menores o collados más altos si el canon y la futura topografía lo permiten; la decisión **no autoriza** afirmar nombres, cantidad, emplazamientos, rutas, pasos abiertos durante todo el año, infraestructuras, puentes ni caminos nuevos.

**Comportamiento plausible (DERIVED_CONDITIONAL, no hecho local decretado):** a esas alturas, algunos pasos pueden sufrir nieve, hielo, viento o dificultades de circulación durante episodios fríos. No se aprueban cierres regulares, fechas, duraciones ni cotas de nieve de pasos individuales. **La Viuda (≈4.200 m) y sus neveros de verano permanecen intactos**.

**Dato operativo:** `Datos operativos/darovan_dp13_valkram_altitude_authorial_v0.1.json` → `principalNaturalPasses`. Esta nueva autorización sustituye el UNKNOWN anterior referido al **rango general de pasos principales**, pero no resuelve la altitud individual de ningún paso ni la cartografía métrica. Fuentes: aprobación expresa del autor en conversación D.P13, 25/10/2026, y canon de `Geografía/montanas.md`.

