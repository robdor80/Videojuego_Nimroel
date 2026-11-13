# E13 — Auditoría de suficiencia y acta de entrega
**Dictamen de contenido, 13-11-2026.** No reemplaza evidencia GitHub Actions de HEAD ni prueba del motor.

## Matriz de objetivos de E13
| Entregable exigido | Archivo/evidencia | Alcance |
|---|---|---|
| Atlas ampliado y subzonas | 01_ATLAS_REGIONES_Y_SUBZONAS | siete unidades, seis interfaces y lectura por paisaje |
| Relieve, bandas de referencia | 02_ALTIMETRIA_Y_MICRORRELIEVE | diseño delegado, no medición |
| Cordilleras, valles, toponimia | 03_MONTANAS_VALLES_Y_TOPONIMIA | nombres canónicos recuperados + 8 propuestas no mapeadas |
| Cuencas y drenaje | 04_CUENCAS_RIOS_DRENAJE | 6 expedientes; sin cursos nuevos falsos |
| Clima y riesgos | 05_CLIMA_ESTACIONES_Y_RIESGOS | siete filas y 10 escenarios condicionales |
| Suelos/ecosistemas | 06_SUELOS_ECOSISTEMAS_Y_APROVECHAMIENTO | 7 fichas UNASSESSED y protección forestal |
| Contratos/motores | 07_CARTOGRAFIA_2D_Y_FABRICA_DE_MUNDO y JSON | estructura y validación, no runtime |
| Comparativa | 08_MATRIZ_PARIDAD_DAROVAN_VALRIK_EDRANOR | 12 ámbitos comparados |
| Plan | 09_PLAN_MAESTRO_E13_E29 | 17 fases y puertas |
| Deuda/decisiones | 10_GOBIERNO_DEUDA_Y_DECISIONES | 7 EDD abiertas con fase y evidencia; EDD-06 resuelta |
| Traspaso | 11_TRASPASO_E14 | entradas y 10 criterios |
| Procedencia y PR | 00_AUTORIDAD_FUENTES_Y_AUDITORIA, README y PR GitHub | trazabilidad reproducible |

## Invariantes materiales
No se editan E00–E12, Canon Norgard, Valrik, Darovan, Norgard Defaults, CoreRPG, Game ni packs. Rodas sigue Corona/Aethros y aldea; Hallheim fuera; no puertos en Lumina, puentes hipotéticos, personajes E10 ratificados, impuestos propios, recursos forestales ilimitados ni rutas confirmadas. Un mapa esquemático no puede usarse como mapa de colisiones.

## Pruebas mínimas antes de fusionar
- Ejecución de validadores E00–E12 en Ubuntu/Windows, y E13 con mutaciones adversariales.
- Revisión de JSON nuevo, IDs, decisiones EDD y consistencia contra E01/E02/E07/E10.
- HEAD exacto de PR y comprobación de main sin deriva; diff limitado a nuevos ficheros E13/Tools/workflow.
- Revisión del contenido para detectar trasplantes de otra Casa y canon inventado.
- No declarar runtime ni decir SUCCESS sin informe real de Actions.

## Lo que esta fase NO cierra
EDD-01/02/03/04/05/07/08, geometría, población, personajes materializados, cuencas verificadas, vías reales, cultivos instanciados, Godot 2D, CoreRPG Edranor productivo. E13 da profundidad conceptual y gobierno, no un territorio completo ya jugable.

## Estado de acta
**CERTIFICADA Y FUSIONADA — E13 cerrada documentalmente el 13/11/2026.**

- **PR:** #76, https://github.com/robdor80/Videojuego_Nimroel/pull/76; 21 archivos nuevos revisados, ningún archivo histórico E00–E12 alterado.
- **HEAD exacto probado:** `34bd83efc0c2d460f649560f2a6f36d37e56ecb8`.
- **GitHub Actions E13:** [run #43492160274](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/43492160274), **SUCCESS** en **Ubuntu 24.04** y **Windows 2022**.
- En ambos sistemas PASS de regresión E00–E10, cruce E12, reglas E13, los contratos y SHA E11 contra CoreRPG fijado, compilación del consumidor C++20 y CTest; **56 mutaciones negativas E13 rechazadas**; CTest **1/1 PASS** en cada plataforma.
- Otros **13 workflows históricos** activados sobre el mismo HEAD terminaron SUCCESS, para un total de **14/14 ejecuciones** exitosas.
- `main` avanzó durante E13 a `fb766afa8965cf3890f3792bff373d6ba7757e05`, incorporando tres biblias visuales Edranor; reconciliadas en `13_RECONCILIACION_BIBLIAS_VISUALES_MAIN.md` sin tocar sus archivos.
- **Fusión PR #76:** squash commit `18bb0fe2f971aa89f843991fa704491421c80499`, comprobado como HEAD de `main` inmediatamente tras fusionar.
- **Alcance de la certificación:** consistencia documental/contractual, validador estático y consumidor sintético C++ E11. **NO** certifica geometría métrica Edranor, Godot 2D, población, caminos, hidrología local ni World State territorial real.

**Las deudas EDD-01/02/03/04/05/07/08 siguen ABIERTAS con destino y prueba de cierre asignados; EDD-06 RESUELTA como aldea regia.** La Casa no queda declarada exhaustivamente profundizada. E14 se abordará en una conversación nueva.
