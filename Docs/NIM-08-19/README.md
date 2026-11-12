# NIM-08 a NIM-19 — Primera aldea jugable y fábrica reproducible de mundos

**Fecha:** 12 de noviembre de 2026. **Estado:** planificación documentada, pendiente autorización de ejecución. **No hay implementación de estas fases, PR de cierre ni fusión en main.**

**Objetivo:** convertir la aldea procedural V1 de Casa Valrik/Treskal y el encargo opcional «La herramienta rota» en una aventura **real**, con edificios, hogares, población, movimientos, percepciones, objetos, oficios, tiempo, decisiones, conversaciones y persistencia que operan en CoreRPG y se presentan mediante Godot 2D en Windows/Android. Su éxito valida un método para escalar al resto de Treskal, Casa Valrik, Casa Darovan y los otros territorios aprobados.

## Documentos de referencia

1. [01_PLAN_MAESTRO_V001.md](01_PLAN_MAESTRO_V001.md) — árbol de **12 fases NIM-08–19**, P01–P04 por fase, responsables ChatGPT/Codex, riesgos, dependencias y puertas de salida.
2. [02_MATRIZ_TRAZABILIDAD_V001.md](02_MATRIZ_TRAZABILIDAD_V001.md) — **28 criterios canónicos** V001-G/P/Q/S/H, estados pendientes, fase responsable, evidencias y los tres itinerarios A/B/C.
3. [03_PLAYBOOK_FABRICA_MUNDOS.md](03_PLAYBOOK_FABRICA_MUNDOS.md) — protocolo repetible **Lore -> fuentes -> Content Pack -> mundo CoreRPG -> GDExtension -> Godot -> guardado -> escala territorial**.
4. [04_REPARTO_CUOTA_Y_BACKLOG.md](04_REPARTO_CUOTA_Y_BACKLOG.md) — tareas que ChatGPT puede preparar **sin Codex**, encargos nativos realmente necesarios y prioridades para compartir cuota con Star Trek.

## Responsabilidad primaria por fase

| Fase | Trabajo | Responsable |
| --- | --- | --- |
| NIM-08 | Arquitectura, auditoría, contratos | **ChatGPT** |
| NIM-09 | Fábrica declarativa de contenido | **ChatGPT** (Codex solo bloqueo nativo) |
| NIM-10 | Aldeas, edificios, layout | **Codex** implementación; ChatGPT especifica/audita |
| NIM-11 | Hogares, población, NPC | **Codex** implementación; ChatGPT prepara/audita |
| NIM-12 | Movimiento, ubicación, percepción | **Codex** implementación; ChatGPT prepara/audita |
| NIM-13 | Herramientas, estado, propiedad, custodia | **Codex** implementación; ChatGPT prepara/audita |
| NIM-14 | Calendario, cola de trabajos, autonomía | **Codex** implementación; ChatGPT prepara/audita |
| NIM-15 | Diálogos y conocimiento individual | **Mixto**: ChatGPT contenido/contratos + Codex runtime |
| NIM-16 | Misión opcional A/B/C | **Mixto**: ChatGPT diseño + Codex runtime |
| NIM-17 | Godot 2D, presentación y narración opcional | **Mixto**: ChatGPT UX/arte + Codex integración |
| NIM-18 | Persistencia integral y regresiones | **Codex** implementación; ChatGPT audita |
| NIM-19 | Certificación completa y guía de réplica | **ChatGPT + propietario**; Codex defectos complejos |

## Baseline

- Rama de documentación creada desde main **0130ed95f27d6d450c962fa2557f56b6b569e4a0**, sin modificar la rama principal.
- CoreRPG verificado sobre main **76a7b7b485616d8c4994f384a90f123bf333591d**.
- Los commits de la antigua rama NIM-07 están ya incorporados al historial de main, aunque no existe en estas comprobaciones una certificación física adicional de I4 en MSI/Tab S9+.
- Los 28 criterios V001 completos **NO se consideran ejecutados** solo por las validaciones estructurales NIM-07.

## Primera acción futura

Cuando el propietario dé autorización a **NIM-08**, ChatGPT debe auditar HEADs actuales y completar los contratos/ADRs **sin consumir cuota Codex**. Solo después, NIM-09 producirá el primer paquete reproducible de datos y validadores. No se trabaja en CoreRPG ni se lanza compilación alguna por la mera existencia de este documento.

**No convertir la misión en un script cerrado: construir primero las mecánicas y demostrar que pueden reutilizarse.**
