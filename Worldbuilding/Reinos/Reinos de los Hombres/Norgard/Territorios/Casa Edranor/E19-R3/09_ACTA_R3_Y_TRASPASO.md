# E19-R3.09 — Acta de entrega y dependencias de cierre

## Hecho en esta fase
Se documenta el modelo territorial completo B2 de suelos, infiltración, respuesta de lluvia/helada, microclimas, coberturas, aprovechamientos y persistencia. Se liga explícitamente a las **siete familias HC** de R2 y los **siete contextos MF** evaluables de R1. Incluye 12 prototipos de suelo, 11 reglas de microclima, 10 mosaicos vegetales, 10 cadenas de recurso y 8 ciclos ambientales. No se añade geometría ni canon material.

## Pendiente con autoridad explícita
- **EDR-01/02:** norte real y geografía métrica, sin dibujar cierre artificial. `MF-08` no evaluable.
- **EDR-03:** receptores individuales, nivel freático, captaciones, flujo y estiaje: R2 ofrece hipótesis, no red localizada.
- **Suelos:** materiales, perfiles, pH, textura, infiltración, profundidad, estabilidad, parcelas y erosión observada.
- **Clima:** meteorología, calendario regional, heladas, días de nieve, grados-día y fenología por zona.
- **Cubierta:** polígonos, individuos, historia de gestión, tasas de regeneración, especies concretas y caza autorizada.
- **Derecho y economía:** títulos, concesiones de agua, licencias de Bosque Alto, cuotas, mano de obra, stocks y rendimientos.
- **Tecnología:** geometría y CRS si se precisan para motor, generador Godot 2D, identidad persistente, integración de CoreRPG y pruebas runtime.

## Traspaso
**R4 — Pasos y corredores:** solo diseñar trazados sujetos a pendientes verificadas, suelos transitables en estación crítica, cruces de cauces existentes, permisos y mantenimiento; no hay caminos reales en esta PR.

**R5 — Asentamientos y usos de suelo:** conectar R1–R4 con Dorth, Lumina, Karsath, Rodas (Corona) y tramas económicas, siempre con agua y saneamiento probados; ninguna aldea, finca o infraestructura se da por existente por este contrato.

**R6 — Auditoría de paridad Valrik:** contrastar estas capas documentales, resolver dependencias y dictaminar madurez real sin ascender B2 a B3/B4.

**E19-TEC — Motor 2D:** posterior a B3 y sin tocar en R3; no se declara una primera aldea jugable.

## Estrategia de PR
R3 apilada sobre R2 #90, R2 sobre R1 #89 y R1 sobre R0 #87. Solo nuevos documentos, contrato, validador y workflow de esta fase. Mantener Draft mientras falten integración ordenada, revisión de diff y CI del HEAD exacto en Ubuntu/Windows. No fusionar R3 directamente a `main`.
