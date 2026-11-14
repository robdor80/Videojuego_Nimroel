# E19-R3.01 — Suelo como sistema físico con memoria

## Regla heredada de Valrik
El suelo superficial **no se decide por una etiqueta de bioma**. Material parental/deposición + posición en ladera + pendiente + textura y profundidad + cobertura + humedad anterior + tránsito + estación permiten **inferir**, nunca certificar sin datos, drenaje, barro, erosión y capacidad de carga. La infiltración inicial, el almacenamiento profundo, la salida lateral y la evapotranspiración son magnitudes diferentes. Un suelo de gravas puede absorber rápido pero guardar poca agua útil; uno fino puede retener agua y asfixiar raíces. No son ecuaciones numéricas todavía.

## Doce prototipos de contexto
| ID | Familia condicional | Contextos R1 | Mecanismo/limitación |
|---|---|---|---|
| SO-01 | Roca de divisoria y cresta | MF-01, MF-06 | BAJA_RETENCION_POSIBLE; Riesgo de erosión y suelo fino; nunca asignar cultivo |
| SO-02 | Derrubio de ladera | MF-01, MF-06 | DRENAJE_VARIABLE; Material móvil y poco fondo útil donde se compruebe |
| SO-03 | Coluvión de pie de monte | MF-02, MF-06 | VARIABLE_EN_LATERAL; Aireación/atascos según textura y posición |
| SO-04 | Terraza o grava de depósito | MF-02, MF-03 | INFILTRACION_ALTA_POSIBLE; Pérdida de humedad o acuífero somero: alternativas |
| SO-05 | Loma de tierra interior | MF-03, MF-04 | MIXTO_CONDICIONAL; Aptitud agrícola no automática |
| SO-06 | Bajo fino o compactable | MF-03, MF-04 | INFILTRACION_LENTA_POSIBLE; Barro y encharcamiento si hay agua y drenaje lento |
| SO-07 | Fondo aluvial no urbano | MF-03, MF-04 | NIVEL_FREATICO_CONDICIONAL; No inventar ribera, río o huerta |
| SO-08 | Horizonte forestal Bosque Alto | MF-05 | ALMACENAMIENTO_SUPERFICIAL_POSIBLE; Hojarasca y raíz no garantizan manantial |
| SO-09 | Claro forestal intervenido | MF-05, MF-06 | VARIABLE_POR_TRANSITO; Compactación; no convertir tala hipotética en hecho |
| SO-10 | Resalte del Azurios | MF-06 | MOSAICO_ROCA_COLUVION; No extender Bosque Real a la Casa |
| SO-11 | Transición fría con suelo estacional | MF-07 | SATURACION_EN_DESHIELO_POSIBLE; Sin permafrost o tundra local presumidos |
| SO-12 | Margen húmedo de curso validado | MF-02, MF-03, MF-04, MF-05, MF-06, MF-07 | VARIABLE_RIBERA; Prohibido materializarlo sin hidrografía R2 acreditada |

## Perfil vertical y balance
Definir en el futuro: roca/material de base; horizonte orgánico si lo hay; profundidad radicular útil; continuidad de poros; lentes de finos; fracturación; nivel saturado; superficie pisada. Por cada capa debe distinguirse **observación** y **modelo**. Una cata de suelo requiere fecha, estación, instrumento, autoridad y perímetro. No hay análisis de pH, mineralogía, textura porcentual, hectáreas ni rendimientos locales acreditados.

### Balance cualitativo con histéresis
1. **Entrada:** lluvia efectiva y deshielo **si** están acreditados.
2. **Reparto:** infiltración frente a escorrentía condicionado por intensidad, cubierta, pendiente, compactación y saturación anterior.
3. **Reserva:** retención superficial y profunda; humedad del subsuelo y aportes laterales.
4. **Salida:** evapotranspiración, drenaje gravitatorio, aporte a receptor existente y consumo **legal** si se conoce.
5. **Memoria:** humedad previa, hielo, rodadas, suelo expuesto, erosión histórica y regeneración; no desaparecen al cesar la lluvia.

Las referencias HC-01..07 de R2 **no son captaciones ni arroyos ya localizados**. SO-12 exige evidencia positiva de un curso y de su receptor. Nunca se deriva una nueva ribera de un nombre como Antela.

## Transiciones físicas y efectos
| Condición compuesta | Evolución plausible | Consecuencia de juego futura |
|---|---|---|
| Suelo fino + tránsito + lluvia acumulada + salida lenta | roderas/barro persistente | retraso de carros solo si existe camino |
| Ladera desnuda + lluvia intensa + material suelto | erosión/surcos y arrastre | inestabilidad y sedimento aguas abajo |
| Bosque con hojarasca + lluvia ordinaria + suelo no saturado | infiltración amortiguada posible | escorrentía tardía, no garantía de manantial |
| Grava + loma ventilada + sequedad previa | secado superficial rápido posible | estrés hídrico si hay cultivo verificado |
| Bajo frío + drenaje lento + deshielo | encharcamiento estacional posible | riesgo para cimientos si se emplazan |
| Terraza con suelo suficiente + aireación + agua + derechos | candidato agronómico | nunca `APTO` automático |

## Aptitud productiva y constructiva — puerta exigente
El orden es: jurisdicción y título → geometría y estabilidad → material, textura, profundidad y capacidad portante → disponibilidad y calidad del agua → clima y exposición → protección ecosistémica → acceso y mano de obra → evaluación aprobada. El resultado inicial de **todas** las parcelas es `UNASSESSED`; la elección final `APTO / CONDICIONAL / NO_APTO` pertenece a un expediente futuro trazable, no a R3.

Riesgos: ni toda la campiña es fértil ni toda montaña improductiva; fondos pueden helar o inundarse, lomas sufrir sequedad, claros compactarse y bosques tener suelos someros. No crear derechos de extracción por encontrar agua. La erosión puede afectar al viñedo, al bosque regulado y a un camino de forma distinta.
