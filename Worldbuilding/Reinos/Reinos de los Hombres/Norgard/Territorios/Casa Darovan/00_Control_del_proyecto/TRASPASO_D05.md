# Darovan 6 — Traspaso a D05 (Rutas y comunicaciones)
**D05 NO INICIADA.** No abrir rama D05 desde main hasta que la PR #20 D04 se fusione con permiso del autor.

1. Verificar PR #20 `merged=true` y HEAD real de main; leer D04 acta, validación, decisiones y plan. Crear rama y PR propia, sin merge automático.
2. Heredar D01 12 unidades sin fronteras métricas; D02 Belara/Lhera/Veldora/Thalen; D03 riesgos condicionales; D04 ocho cadenas y relaciones de suministro **NO equivalentes a rutas**.
3. Tramo conocido: camino principal Veldora–Treihord, con Bosque de la Linde próximo; no afirmar que atraviesa el bosque.
4. Relación logística mineral Valkram→carros→carga fluvial→barcazas Belara someras→puerto industrial Treihord; ninguna carga/intercambiador con nombre o coordenadas nuevos.
5. Carbón Montes Azurios→Treihord confirmado, pero **itinerario, modo y nodos desconocidos**. No imponer que venga por Belara.
6. Puertos: Veldora comercial y fiscal externo según reglas; Taramin pesquero entre dos brazos Thalen, sin atribuirles calado navegable; Syvaris puerto seguro en bahía principal, calas y circuitos sin inventar.
7. No crear aranceles inter-Casas, rutas sobre Arven bajo Darovan (DAR-P01) o nombres de puentes/estaciones/destinos nuevos. Controles GIS y tiempo de viaje solo tras cartografía, nivel de agua y escala autorizados.
8. D05 puede diseñar grafo **cualitativo** y clases de arista AUTHORED/DERIVED/UNKNOWN, pero ningún movimiento o world state queda implementado por tener JSON.

**Pendientes:** DAR-P01/P04/P07/P08/P09/P10/P11; cartografía métrica, regímenes fluviales, rutas del carbón, pozos, caladeros y capacidades. D01–D03 Python MSI ya superados el 15/10/2026. Nuevo `validate_d04.py` pendiente de ejecutar en MSI; no llamarlo aprobado sin salida real. D11 queda responsable de integración CoreRPG/Godot y persistencia.
