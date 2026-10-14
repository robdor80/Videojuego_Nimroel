# Nimroel RPG — Host 2D conversacional

**Estado:** raíz de desarrollo reservada; sin build ni pruebas ejecutadas.

## Experiencia objetivo

Nimroel es un juego de rol narrativo con fondos 2D ilustrados, retratos de NPC y conversación libre por escrito o por voz. Su interfaz no exige seleccionar objetos/edificios dibujados, pulsar hotspots ni mover un avatar por un mapa. Las imágenes ambientan, sin representar exhaustivamente la realidad del mundo.

La IA actuará como **intérprete de intención y Máster narrativo**, con narración autorizada. **CoreRPG sigue siendo el árbitro y estado autoritativo**; las reglas Nimroel definen contenido específico. La IA no puede crear, reparar, entregar o revelar hechos saltándose validaciones del motor.

Se prepararán Windows y Android como aplicaciones independientes. El soporte real de IA/voz/offline se verificará explícitamente; un parser limitado usado en pruebas no equivale a conversación libre.

## Límites de responsabilidad

- **Worldbuilding/**: canon, biblias, perfiles y activos de producción; no se modifica en NIM-01.
- **Game/Host2D/** (futuro): escenas de fondo, retratos, historial narrativo e inputs adaptados a cada pantalla.
- **Game/Interaction/** (futuro): interpretación de intenciones, narración basada en resultados y adaptadores de voz.
- **Game/BridgeCoreRPG/** (futuro): adaptador al motor portable C++20, sin WorldState alternativo.
- **Game/Content/TreskalV001/** (futuro): fixture regional, configuración V1 y futuro mapping a Content Pack.
- **Game/Tests/** (futuro): pruebas técnicas y matriz V001 con evidencias.

Los directorios aparecen únicamente cuando los incrementos correspondientes estén implementados. Los assets fuentes permanecerán en sus ubicaciones existentes, referenciados desde el juego.

## Referencias

- Plan: [Docs/NIM-01_BUILD_PLAN.md](../Docs/NIM-01_BUILD_PLAN.md).
- Contrato de experiencia: [Docs/NIM-01_EXPERIENCIA_CONVERSACIONAL.md](../Docs/NIM-01_EXPERIENCIA_CONVERSACIONAL.md).
- Canon de prueba: Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Valrik/Aldeas/03_Prueba_v0.0.1/ (PR #12).
- Commits: Docs/NIMROEL_GIT_COMMIT_CONVENTIONS.md.
- PR NIM-01: permanecerá Draft hasta cierre real; no se declara soporte Android ni funcionamiento de la IA sin pruebas.
