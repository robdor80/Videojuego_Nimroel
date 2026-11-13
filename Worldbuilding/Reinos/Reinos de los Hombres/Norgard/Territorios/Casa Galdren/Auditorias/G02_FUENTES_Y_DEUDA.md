# G02 — Trazabilidad y deuda explícita
**Baseline:** `db49fde947463a7305b9ae453aa1c844740f6dda` (`main` tras PR #66, G01 fusionada). Se reutiliza el registro de fuentes de G00/G01; ninguna ilustración se ha interpretado como levantamiento topográfico.

| Fuente versionada | Evidencia aportada | Decisión G02 |
|---|---|---|
| `Geografía/rios_y_lagos.md` | Caleran, bifurcaciones, Suthiros, Gemelos de Treskal, Vornarsk/Keldarsk | Conservar los cinco cursos y no crear otro |
| `Geografía/montanas.md` | Azurios, Invernos, Velaris | Separar vertiente occidental Azurios de llanuras orientales sin inventar paso |
| `Geografía/mares_y_costas.md` | Bahía Zanthir, Mar del Norte y Suthiros | Sin atribuir a los ríos norteños desembocaduras desconocidas |
| `Geografía/bosques.md` | Quebrado y bosques ligados a brazos del Caleran | Proximidad forestal ≠ afluente nuevo |
| `Montes Invernos/cotas_y_altitudes_borrador.md` | Gradientes regionales aprobados, nieve/deshielo y cabeceras Gemelos | No convertir cotas regionales en alturas exactas Galdren |
| G01 atlas, límites y JSON | Perímetro aproximado, vecinos, 12 unidades, 6 bordes, TOP pendientes | Respetar separación drenaje/jurisdicción |
| G01 traspaso | G1-C01 y ausencia de cauces secundarios | Estudiar sin corregir unilateralmente canon |
| Edranor E02 | Dorth y vertiente occidental Azurios aún sin traza hidrográfica adjudicada | No secuestrar cuencas del vecino |

## Registros que siguen abiertos
`G02-D01` trazado occidental→oriental del Caleran, requiere mapa autoral; `G02-D02` geometría y número final de bocas del Caleran; `G02-D03` nacimientos, recepción y relación mutua Vornarsk/Keldarsk; `G02-D04` divisorias Invernos, cabeceras y margen de Gemelos; `G02-D05` régimen estacional cuantitativo, nevadas/glaciares, hielos; `G02-D06` navegabilidad, puentes, vados y puertos; `G02-D07` altimetría, riesgo de inundación, derechos y captación de agua; `G02-D08` costas y titularidad de boca/vegas; GDD-01/02/03/07 permanecen.

## Auditoría negativa
Especial atención a: Caleran dividido en nuevos ríos; trasvasar los Gemelos a Galdren; atribuir a Zanthir dos desembocaduras en la bahía por simple cercanía; afirmar glaciar permanente; convertir traza roja en divisoria, y convertir un riesgo posible en suceso canónico. La validación JSON comprueba **la representación** y las fuentes; no mide una realidad física.
