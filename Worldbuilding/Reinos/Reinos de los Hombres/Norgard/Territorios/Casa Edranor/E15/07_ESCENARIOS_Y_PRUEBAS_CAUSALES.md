# E15 — Laboratorio de economía vivida: escenarios, no sucesos

La matriz JSON registra **28 casos hipotéticos**, todos `HYPOTHETICAL_NOT_OCCURRED`, repartidos entre vino, madera, alimentación, hogares y comercio. Los casos no crean misiones, recompensas, incidentes ni estados del mundo. Sirven para probar en E17/E28 causalidad y capacidad de recuperación de información.

## Familias de conflicto
| Familia | Casos | Pregunta causal |
|---|---:|---|
| WINE | 8 | ¿puede crecer, transformarse, reservarse y entregarse el lote con derechos, gente y capacidad? |
| WOOD | 6 | ¿puede convertirse madera autorizada en barrica o repararse sin duplicación? |
| FOOD | 5 | ¿puede el hogar comer/moler/conservar realmente sin crear grano o agua? |
| HOUSEHOLD | 5 | ¿cabe el trabajo en la vida de las personas con cuidados y requisitos de edad? |
| TRADE | 4 | ¿se mueve una mercancía con ruta real, consentimiento y autoridad correcta? |

## Ejemplos legibles
- **ED15-W01, vendimia sin parcela aprobada:** la notoriedad vitícola no sustituye título, clima y suelo. Resultado: `PENDING_EVIDENCE`; ninguna cosecha añadida.
- **ED15-W04, vino dos veces vendido:** un pedido reserva unidades existentes; otro pedido no puede gastar esa misma reserva.
- **ED15-M01, permiso forestal pendiente:** la necesidad de barrica no transforma Bosque Alto en propiedad comercial libre. Resultado: BLOQUEADO.
- **ED15-M04, aros inexistentes:** un montón de duelas no se cuenta como barrica terminada.
- **ED15-F02, molino no localizado:** el grano no se convierte en harina por proximidad dibujada.
- **ED15-H03, temporeros sin camas:** trabajo adicional no se activa sin alojamiento digno y disponibilidad.
- **ED15-T02, venta a Rodas:** el acuerdo comercial no cede impuestos ni mando de Aethros.
- **ED15-T03, acceso a Karsath:** contexto lacustre no permite carga por muelle inexistente.

## Oráculos técnicos
1. Si `rights` no está confirmado: `PENDING_EVIDENCE`; si está denegado: `BLOCKED`.
2. Una cantidad reclamada que excede `available = onHand - reserved` produce `INSUFFICIENT_STOCK`; nunca negativo.
3. Un lote con procedencia inválida, recipiente no apto, capacidad insuficiente o servicio sin responsable queda en `HOLD`.
4. `transfer` exige ruta validada por futura autoridad cartográfica; `route=UNKNOWN` **no** equivale a `true`.
5. Rodas con autoridad `casa_edranor` se rechaza sin negociación; Hallheim queda fuera de dominio.
6. Una pérdida se deduce del lote padre y queda trazada; nunca se reintegra sin una devolución realmente existente.

El laboratorio Python incluido verifica el contrato, usa entradas sintéticas y mutaciones adversariales. Sus pruebas no ejecutan ni sustituyen el motor CoreRPG ni las escenas Godot 2D. Los escenarios más complejos serán entrada a E17, no ejecuciones declaradas en E15.
