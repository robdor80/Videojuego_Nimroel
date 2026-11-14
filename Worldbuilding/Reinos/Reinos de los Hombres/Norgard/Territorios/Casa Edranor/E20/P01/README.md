# E20-P01 — Dorth, monografía urbana y diseño operacional profundo

**Fecha:** 14/11/2026. **Alcance:** profundidad de diseño funcional con referencias al canon, NON_METRIC / NO_RUNTIME / SIN INSTANCIAS. **Precedente:** Casa Valrik/Treskal, en particular estructura funcional 01, simulación social 10–99 y 10 puertas métricas; se adopta el método, nunca su geometría ni inventarios.

## Objetivo de esta subfase
Hacer de Dorth una ciudad comprensible por sus actividades y conflictos propios: sede administrativa, tinta y prestigio vinícola, recepción de vendimia, casas mercantiles, bodegas de guarda, tonelería regulada, circuitos domésticos, justicia del Rey ejercida localmente y borde forestal de Azurios. Desarrollar unidades relacionadas y sus condiciones de funcionamiento; no cambiar el rótulo de Treskal y copiar un puerto maderero.

## Qué se entrega
1. [Monografía e identidad](00_MONOGRAFIA_URBANA.md).
2. [Sistema de ámbitos y dependencias](01_TEJIDO_Y_ENLACES_FUNCIONALES.md).
3. [Cadena vinícola completa, control y fallos](02_ECONOMIA_BODEGA_Y_TONELERIA.md).
4. [Vida cotidiana, hogares y servicios](03_POBLACION_SERVICIOS_Y_RITMOS.md).
5. [Instituciones, memoria, personajes y escenas](04_GOBIERNO_RELACIONES_Y_NARRATIVA.md).
6. [Comparación exigible con Treskal y traspaso](05_ACEPTACION_Y_HOJA_DE_RUTA.md).
7. [Contrato JSON del programa no métrico](dorth_program_v0.1.json), validador y CI Windows/Linux.

## Qué NO se entrega
No hay censo, calle situada, parcela, mapa métrico, edificio instanciado, viñedo, NPC efectivo, lote existente, sentencia o suceso ocurrido. Sin World State ni Godot integrados. E19-R0 (#87) investiga fuentes, pero los bloques métricos requieren E19-R1–R6. E20-P00 (#85) permanece auditoría en otra PR; no se fusiona con esta rama.

**Regla de calidad:** programar un edificio exige saber para qué sirve, qué necesita y qué lo bloquea; afirmar que existe exige además huella/puerta/geometría, titular y prueba. El programa y los casos de esta fase son propuestas accionables, NO instancias.
