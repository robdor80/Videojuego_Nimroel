# NIM-08 — Arquitectura, auditoría, contratos y fábrica reutilizable

Fecha: 12-11-2026. Versión de diseño: NIM08-ARCH-0.1.0. Rama exclusiva: design/nim08-arquitectura-contratos-20261112.

Esta carpeta **desarrolla** NIM-08 dentro de la planificación ya publicada en Docs/NIM-08-19/. No reemplaza el Plan Maestro 01, la matriz de 28 criterios 02, el playbook 03 ni el reparto 04. No contiene mundo ejecutable ni modifica CoreRPG, Godot, canones, pins o políticas IA.

## Índice de trabajo

- 00_ESTADO_Y_FUENTES.md — P01: baseline Git, evidencia I4, APIs implementadas/ausentes y riesgos.
- 01_CONTRATOS_Y_DISENO.md — P02/P03: ADRs, autoridad, dominios, IDs, acciones y extensibilidad.
- 02_FIXTURES_Y_ACEPTACION.md — P03/P04: protocolo de trazabilidad V001 28/28 y escenarios A/B/C.
- 03_ENCARGO_CODEX.md — NIM-08 no requiere ni autoriza Codex; futuro modelo de cesión.
- 04_RESULTADO.md — publicación, verificación ejecutada y límites.
- 05_AUDITORIA_INDEPENDIENTE.md — dictamen del diseño y límites de evidencia.
- 06_TRASPASO.md — requisitos de entrada de NIM-09, y puertas para NIM-10–19.
- contracts/ — esquemas de diseño 0.1.0 y manifiesto ejemplo **no operativo**, nunca nuevos formatos Core ya soportados.
- Tools/NIM08/ — comprobaciones estáticas y pruebas de contrato; no simulación nativa.

Fuentes de verdad: Worldbuilding (canon) -> ContentPacks versionados (datos) -> CoreRPG (estado y operaciones) -> Host autorizado -> Godot 2D (presentación). Consultar antes de interpretar un contrato: Docs/NIM-08-19/01_PLAN_MAESTRO_V001.md.

**Prohibiciones:** no elevar fixtures a canon; no fingir que un esquema JSON es una API C++; no asignar PASS funcional V001 sin ejecutar el sistema correspondiente; no autocerrar/auto-fusionar PR ni iniciar NIM-09.
