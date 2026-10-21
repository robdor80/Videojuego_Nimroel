# D06 — Esqueleto, posibilidades, condiciones y modelos v0.1

**Estado: diseño técnico no canónico; sin localidades nuevas, emplazamientos ni ejecución en CoreRPG/Godot.** Fecha 21-10-2026.

## 1. Autoridad y escala

La autoridad es `Nimroel Core → Norgard Defaults → Casa Darovan → Localidad → World State`. Las doce unidades `d01_*` son áreas cualitativas de estudio, **no** polígonos, municipios ni propiedades. Los nombres de las cuatro ciudades **Treihord, Veldora, Taramin y Syvaris** y su diseño son manuales e inmutables para este generador. Karsath no es Darovan. Arven **sí** pertenece a Darovan por decisión del autor del 21-10-2026.

D06 prepara reglas territoriales y muestras sin publicar canon. Los asentamientos ya aludidos de forma genérica en fuentes Norgard (aldeas costeras de Arven; aldeas/pueblos de los Pilares; aldeas de la península de Taramin) **no adquieren ni número, nombres, emplazamientos ni habitantes por esta fase**. Para todo sitio candidato real aún faltan legitimidad jurisdiccional del lugar concreto, plano de terreno, agua potable, acceso, uso productivo y derechos.

## 2. Esqueleto obligatorio (antes de elegir el modelo)

Una comunidad permanente precisa simultáneamente:

1. `habitable_ground_verified`: suelo seguro y habitable **en ese sitio**, no inferido por color del mapa; riesgos D03 solo como alertas condicionales.
2. `potable_water_verified`: agua utilizable comprobada. Un río cercano sin caudal/calidad conocida, una cala o la lluvia regional **no** bastan.
3. `local_access_verified`: acceso local confirmado según el caso; no significa nueva carretera, puente, vado, ferry o navegación.
4. `livelihood_viable_verified`: base material y suministro de la comunidad; no bastan depósito, mina, mercancía en tránsito o cadena D04 por sí solos.
5. `local_jurisdiction_verified`: potestad de uso y competencia comprobadas **en el emplazamiento**, no determinada automáticamente por el identificador D01.

**Si falta una condición, el candidato se rechaza; UNKNOWN no es TRUE.** Superar el esqueleto no concede generación en mapa: requiere la cartografía, los derechos, las rutas y la decisión de inserción posteriores.

### Categorías y umbrales cualitativos

- **Aldea:** núcleo residente de vida cotidiana con mínimos comunes y medios de subsistencia; no requiere por definición un servicio especializado concreto.
- **Pueblo:** comunidad residente con funciones compartidas demostrables y demanda efectiva para servicios adicionales; no hereda porcentajes ni herreros obligatorios de Treskal.
- **Villa:** centro local más complejo condicionado por red, actividad y aprobación de escala en D08; **no** es ciudad canónica ni capital generada.
- **Enclave especializado:** instalación o agrupación funcional; una mina, almacén, muelle, puesto o campamento **no equivale** a asentamiento. Para existir como asentamiento, además del esqueleto, necesita comunidad residente justificada; instalaciones sin ese hecho continúan como instalaciones de D04/D05.

Estas son clases de diseño, **no umbrales demográficos**. Distribución de hogares, oficios, salarios, propiedad, demanda, inventario, tenencia y residencia pertenecen a CoreRPG con concreción D08/D11.

## 3. Posibilidades, no equipamientos fabricados

Los modelos enumeran **posibilidades** de viviendas, almacenes, patios de labor, establos, graneros, secaderos, lonjas locales, talleres, carpinterías, mercados o posadas. Un edificio no aparece por figurar en una lista. Su activación futura requerirá: modelo, prueba del sitio, demanda, suministro, cobertura regional y disponibilidad económica verificada; financiación, titularidad y estado pertenecerán a CoreRPG.

No se da por supuesto que todo pueblo tenga mercado, molino, boticario, herrero o guardia; los patrones obligatorios de Treskal son **solo referencia de método**. Los puertos de las cuatro ciudades no se replican en el litoral como aldeas portuarias.

## 4. Condiciones económicas específicas

| Modelo técnico | Pruebas adicionales obligatorias | Posibilidades subordinadas | Bloqueo particular |
|---|---|---|---|
| `agricola` | cultivo/suelo viable + derecho de uso | huertos, granero, molienda condicional | sequedad o suelo visual no prueban regadío, rendimiento ni cultivos |
| `ganadera` | pastos viables + derecho de pasto | corrales, forraje, intercambio | no crear praderas/cabezas de ganado por clima |
| `pesquera` | medio pesquero, desembarco seguro y derecho de pesca | secadero, redes, lonja condicional | costa ≠ caladero, puerto, barco, permiso o conexión marítima |
| `minera_auxiliar` | explotación concreta autorizada, acceso e identidad del titular | útiles, cobertizos, alojamiento solo justificado | Valkram con mineral no prueba mina nueva; Elyra Darovan UNKNOWN |
| `metalurgica_auxiliar` | función legal, combustible e insumos reales, acceso de suministros | taller, depósitos condicionales | El Crisol de Treihord **no** se duplica; carbón de Azurios no inventa itinerario |
| `forestal_sostenible` | parcela gestionada, derechos y extracción compatible con regeneración | carpintería, útiles | no industrias nuevas en Linde; Taramin uso tradicional, Syvaris y Arven sin tala intensiva |
| `servicio_camino` | camino comprobado **en ese sitio** y demanda local | posada/refugio/reparación condicional | D05 solo certifica Veldora–Treihord cualitativamente; ni estaciones ni trazado |
| `insular_mixta` | isla y derecho local, base alimentaria/suministro propio | espacios comunes y servicios locales | Arven/Syvaris no reciben ruta, embarcadero o acuífero implícito |
| `enclave_especializado` | función autorizada + comunidad residente justificada | instalación y residencia condicional | no convertir cada obra, mina, almacén o puesto en pueblo |

La versión operativa define cada modelo, las clases admisibles y pruebas legibles por máquina en `Datos operativos/darovan_d06_settlement_rules_v0.1.json`.

## 5. Incompatibilidades transversales

- **Bosque de las Agujas:** no existen asentamientos permanentes interiores. Sin geometría para separar interior/exterior, toda la unidad `d01_aguja_litoral` se bloquea preventivamente para muestras.
- **Bosque de los Pilares:** sistema único con claros; no fragmentarlo ni permitir extracción sin regeneración.
- **Bosque de Taramin:** sistema único con transición ecológica; no autorizar tala industrial; las aldeas descritas en la costa no autorizan trazar costa nueva.
- **Syvaris:** vegetación discontinua; no bosque uniforme, mina nueva o superávit hídrico inventado.
- **Arven:** Casa Darovan y aldeas costeras en el canon; Manto Verde muy extenso y aprovechamiento maderero limitado. Ningún ferry o puerto nuevo acreditado.
- **Treihord:** Belara pasa a su lado, no lo cruza; solo barcazas someras industriales en relación demostrada.
- **Ríos:** Belara+Lhera una red; Veldora, Fhalion y Thalen otras tres; no inferir navegación fluvial a partir de la existencia del cauce.
- **Rutas:** D05 conserva tres conexiones físicas y cuatro relaciones logísticas **no rutas**. Nada de distancias, puentes, horas o caminos nuevos.
- **Instituciones:** no aduana entre Grandes Casas, no nueva Casa soberana ni armada Darovan. Jurisdicción y seguridad se remiten a Defaults y D09.

## 6. Referencias

Fuentes jerárquicas: `Geografía/bosques.md`, `rios_y_lagos.md` del Norgard original; anexos canónicos D05 del 21-10-2026; perfiles D01–D05 del directorio `Datos operativos`; Core geografía; Default fiscal. La metodología Valrik/Treskal inspira **secuencia y estabilidad**, no estadísticas, tiempos, mínimos numéricos ni servicios universales.
