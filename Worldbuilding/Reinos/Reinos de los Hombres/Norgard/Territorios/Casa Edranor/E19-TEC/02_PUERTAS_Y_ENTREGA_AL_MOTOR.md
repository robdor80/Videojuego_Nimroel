# E19-TEC.02 — Puertas de promoción y transferencia

| Puerta | Evidencia exigida | Estado |
| --- | --- | --- |
| TEC-01 | Atlas, fuentes, autoridad y reglas R0–R6 revisadas | OK documental |
| TEC-02 | Sistema local métrico, transformación reversible y tolerancia publicada | PENDIENTE |
| TEC-03 | Geometría espacial real con fuente y aprobación por sector | PENDIENTE |
| TEC-04 | Red de agua/receptores y derechos de uso probados | PENDIENTE |
| TEC-05 | Grafo Gp legal, medido y transitable; Gq no convertible | PENDIENTE |
| TEC-06 | Parcelas, viviendas, núcleos, censos y servicios auditados | PENDIENTE |
| TEC-07 | Godot 4.7.2 Standard 2D carga un sector real estable | PENDIENTE |
| TEC-08 | CoreRPG C++20 guarda, recarga y conserva estado/identidad | PENDIENTE |

## Fases materiales verificables
1. **TEC-A — Infraestructura (esta entrega):** aceptar únicamente input validado, probar geometría y rechazos, emitir paquete versionado de sector; resultados sintéticos no son mundo real.
2. **TEC-B — Sector piloto acreditado:** seleccionar zona con fuente suficiente y autoridad. Sin inventar escala, rutas, hidrografía ni topología del norte. Obtener geometría real y QA de derechos; aceptar B3 **sólo ese sector**.
3. **TEC-C — Integración runtime:** adaptador Godot 2D de lectura, CoreRPG/World State, persistencia de entidades y generación determinista sin duplicación. Aceptar B4 **sólo con pruebas reales**.
4. **TEC-D — Extensión progresiva:** repetir por zonas; convertir los expedientes CT/OS sólo con evidencia local, no por equivalencias a Valrik. MF-08/U7 sigue NO EVALUABLE sin fuente.

## Invariantes para cada revisión
- Incluir test de frontera norte abierta y laderas correctas; no asumir cierre.
- Distinguir red de preguntas CT y red física Gp; si Gp está vacía, no hay viajes confirmados.
- No importar caminos, altitudes, poblaciones, censos, escala, edificios o modelos de Treskal.
- Rodas no tributa a Edranor. Bosque Alto sin tala automática. Bosque Real regio.
- El Lurien sólo es parcialmente límite sur; no asignar Caleran a Dorth ni puerto urbano a Karsath.
- Sin materialización no hay claims B3/B4, incluso si pasan CI o un validador JSON.

## Integración de Git
Esta rama es hija de R6 #94 (a su vez R5 #93 → ... → R0 #87). No fusionar directamente a main: primero integrar R0–R6 con revisión independiente. E20-P00 #85 necesita reconciliar su viejo requisito métrico B2 antes de integrarlo. Mantener intactos Game, CoreRPG, otras Casas y canon.
