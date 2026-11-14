# E20-P01 — Suficiencia, comparación con Treskal y exigencias posteriores

## Qué hereda Dorth del catálogo de Treskal
La lista 00–99 es **un catálogo de capacidades, no una cuota de directorios**. Dorth necesita responder a estas familias de problemas, adaptadas a vida vinícola:

| Capacidad comparable Valrik | Concreción Dorth P01 | Próxima evidencia |
|---|---|---|
| Estructura urbana, edificios, viajes, accesos | DOR-F01…F12 y vínculos causales NO MÉTRICOS | P02/P03: mapa, edificios, puertas, grafo real |
| Producción y mercado | E01–E10 del tinto, origen y custodia, tonelería | P04: productores, viñas, barricas, inventarios reales |
| Población, trabajo y vivienda | Hogares diversos, oficios y demandas, servicios | P05: conciliación personas–hogares–viviendas–empleos |
| Emociones, reputación, conocimiento, IA, memoria | Consecuencias de fallos, escenas A/B/C, información parcial | P06/P08: biografías legitimadas, estados y memoria |
| Ley, honor, disputas, seguridad, fiscalidad | Separación de competencias, Justicia del Rey, E4 | P07: cargos, sedes, permisos, incidentes efectivos |
| Clima, agua, salud, saneamiento, incendios | Dependencias cruzadas y vetos a agua no demostrada | E19-R/P03/P07: servicios y capas de riesgo |
| Integración, persistencia y simulación | Contrato de programa no materializado, IDs de diseño | P09: GeoJSON, escenas Godot y pruebas World State |

## Criterio de aceptación de P01
P01 puede declararse **DISEÑO FUNCIONAL SUSTANTIVO** cuando: doce ámbitos tienen papel/justificación, economía de tinto enlaza a oficios y hogares, instituciones distinguen jurisdicción, se trazan tres conflictos con condiciones y estados, y los vetos impiden resultados inventados. **No** puede declararse B3 ni B4 por ello.

La prueba computacional aquí solo detecta afirmaciones y estructuras improcedentes en un contrato editorial. No prueba que un habitante habite una casa o que Godot cargue un mercado.

## Dependencias ordenadas
- **E19-R1–R6:** perímetro, escala, cuencas, accesos y fuente espacial; bloqueantes de mapas/parcelas/vías definitivas.
- **P02:** huella urbana y sectores con puertas y caminos transitables; geometría y acceso separados de rol de diseño.
- **P03:** catálogos de inmuebles/interiores no genéricos, capacidades y parcelas con tenencia válida.
- **P04:** circuito físico de tintos, proveedor y tonelero con fuente, lotes y movimientos testeables.
- **P05:** residencia, censo, jornadas, servicios y capacidad, sin duplicar PersonaId ni vivienda.
- **P06:** biografías locales y relaciones con legitimación E25; E10 es propuesta.
- **P07:** instituciones, guardia, cuidados, correo, saneamiento, transporte, mantenimiento.
- **P08:** escenas con causas, versiones, investigaciones, consecuencias y persistencia.
- **P09:** importadores 2D, datos espaciales, navegación y guardado/carga en Godot/CoreRPG; B4 sólo con test de ejecución.
- **P10:** auditoría por capacidad equivalente a Treskal, adaptada a Dorth. Si no pasa, nuevas subfases sin cierre artificial.

## Invariantes que CI no puede resolver sola
Una prueba verde sobre este JSON comprueba clasificación y coherencia **del programa**. El cambio de B2 a B3 exige datos concretos y verificables; B4 exige que el juego los use y persista. La falta de fuente no se resuelve añadiendo más escenarios, campos vacíos o pruebas sintéticas.
