# Nimroel RPG — juego ejecutable 2D

**Estado:** carpeta reservada para el desarrollo del videojuego. Todavía no contiene un build jugable.

## Alcance de este árbol

Este directorio alojará el Host 2D de Nimroel para Windows y Android, el puente hacia CoreRPG, los datos de instancia y las pruebas. Su existencia no modifica el canon ni los contratos de Worldbuilding.

La interfaz utilizará fondos ilustrados y retratos durante conversaciones e interacciones. No se admiten modelos 3D. El patrón de desplazamiento por escenas o mapa 2D está pendiente de decisión del autor.

## Separación obligatoria

- **Worldbuilding/**: reglas, canon, biblias, perfiles, contenidos autorizados y fuentes de assets.
- **Game/Host2D/** (futuro): presentación, input, navegación visual y HUD; ninguna autoridad sobre hechos del mundo.
- **Game/BridgeCoreRPG/** (futuro): adaptador al núcleo de lógica portable C++20, sin estado autoritativo paralelo.
- **Game/Content/TreskalV001/** (futuro): datos de prueba y fixture regional versionado, diferenciados de lore permanente y de Content Packs aceptados.
- **Game/Tests/** (futuro): smoke tests y matriz V001 ejecutada con resultados y evidencias.

Los subdirectorios se materializarán conforme se implemente cada incremento, no con esqueletos falsamente completos.

## Plan de trabajo

Ver Docs/NIM-01_BUILD_PLAN.md. La PR de NIM-01 se mantendrá en estado Draft hasta completar el paquete aprobado y su auditoría. No se declarará soporte Android sin una prueba en dispositivo.

## Registro de trazabilidad

- Canon de prueba: PR #12 de Videojuego_Nimroel.
- Fases CoreRPG de referencia: 4.5–4.8 estructurales; 4.9–4.13 integraciones posteriores.
- Norma Git: Docs/NIMROEL_GIT_COMMIT_CONVENTIONS.md.
