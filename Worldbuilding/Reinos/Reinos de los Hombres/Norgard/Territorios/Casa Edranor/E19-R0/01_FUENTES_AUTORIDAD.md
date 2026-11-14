# E19-R0 — Fuentes leídas, precedencia y trazabilidad

## Qué puede probar cada referencia
| ID | Fuente inspeccionada | Hecho soportado | Uso prohibido |
|---|---|---|---|
| SRC-01 | Worldbuilding/Nimroel.jpg y adjunto Mapa de Nimroel (1).jpg; el adjunto de 4096×2048 se examinó visualmente | Situaciones relativas de Karsath, Lumina, Dorth y Hallheim; mapa general Norgard con barra ilustrada 400 millas | Cerrar el dominio Edranor, extraer metros/píxel o situar Rodas con X ausente |
| SRC-02 | Edranor/Cartografia/E00_MAPA_Y_LIMITES.md (referencia recorte 1000024893.jpg) | E00 describe dos límites rojos y X azul de Rodas; el borde norte se halla cortado | Trazar vértices desde el texto; afirmar que se han comprobado los bytes del recorte |
| SRC-03 | Edranor/Cartografia/E01_LIMITES_Y_VERTIENTES.md | Septentrión abierto; Hallheim fuera; Rodas bajo Corona | Inventar cierre norte, frontera por cumbres o costa |
| SRC-04 | Edranor/Cartografia/E01_ATLAS_RELIEVE.md y E01_CORREDORES.md | Siete unidades cualitativas; cuatro interrogantes de conexión | Suponer caminos efectivos o cotas reales |
| SRC-05 | Norgard/Geografía/montanas.md | Valkram, Azurios, Velaris, Vareth a escala de reino | Adjudicar pasos o vertientes completas a Edranor |
| SRC-06 | Norgard/Geografía/bosques.md | Bosque Alto en meseta próxima a Lumina; Azurios linda con Dorth; sector meridional Bosque Real de Aethros | Derecho de tala o dominio de toda la masa forestal |
| SRC-07 | Norgard/Geografía/rios_y_lagos.md | Lurien nace en Valkram oriental, alimenta Antela al sur de Karsath, continúa por Hallheim | Ríos/puertos, puentes o riego de Dorth sin prueba local |
| SRC-08 | Norgard/NORGARD.md y Grandes Casas/grandes_casas.md | Edranor subordinada, sede Dorth; Rodas directa de Corona Aethros | Cambiar por cercanía geográfica su jurisdicción |
| SRC-09 | Edranor/E07 y contrato edranor_e07_canonical_nuclei | Dorth, Lumina, Karsath y Rodas son anclas protegidas; sin entidades materializadas | Inventar edificios, hogares y carreteras |
| SRC-10 | Edranor/E13/07_CARTOGRAFIA_2D_Y_FABRICA_DE_MUNDO.md y E18/03_HALLAZGOS_DEUDA_Y_PRIORIDAD.md | Secuencia técnica y EDD-01/02/03/07 abiertas | Promover diseño conceptual a mapa B3 |
| SRC-11 | Valrik/Treskal/08_Cartografia/mapa_canonico_definitivo_treskal_v1.0.md, GeoJSON, SVG | Método de geometría consistente e IDs persistentes (2.404 entidades, 2.175 parcelas) | Copiar geometrías, números de parcela o distancias |
| SRC-12 | PDF TODO NIMROEL 10.09.26 y Cuaderno de Lore (adjuntos de proyecto) | Contexto narrativo potencial, no autoridad espacial | Convertir un trayecto relatado en vía cartografiada |
| SRC-13 | PR #84 DESCARTADA — E19 cartografía preliminar | Rechazo documental verificable | Reutilizar calco, SVG, JSON o contrato de la PR |

## Origen que falta
El archivo original 1000024893.jpg es citado y descrito por E00. **No está disponible como archivo íntegro verificable en los adjuntos montados de esta conversación ni se localizó como fuente de main**. El mapa general visible **no contiene las dos líneas rojas de Edranor ni la X azul**. La información derivada del recorte se atribuye a la transcripción de E00, no a una inspección directa del JPEG original.

## Cadena de custodia necesaria para R1
ID fuente, bytes originales inmutables, SHA-256, fecha, autor cuando conste, dimensiones, elementos representados, relación entre recorte y global, decisión de aprobación de linderos, entidad topológica afectada, incertidumbre, transformación y prueba. Un archivo rechazado no puede figurar como fuente geométrica aprobada.
