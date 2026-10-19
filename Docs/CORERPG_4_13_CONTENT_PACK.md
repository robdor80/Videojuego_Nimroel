# Acta Nimroel de 4.13 — entrega para auditoría

2026-10-19. Rama `feat/4.13-treskal-villages`, desde main
`35c9d22ca3f688c62c709320b20cba565518669d`. No modifica PR #20/#22/#23,
no cambia el Host ni certifica v0.0.1 jugable. La primera aldea V1 es el único
escenario de esta entrega; Treskal ciudad queda fuera.

Contrato, inventario, fuentes, reproducción y límites:
[ContentPacks/treskal-villages](../ContentPacks/treskal-villages/README.md).

| Incremento | Entrega |
| --- | --- |
| I1 | Selección, identidad y autoridad documental (`95d1be2`) |
| I2 | Proyección y pack con procedencia (`44860ee`) |
| I3 | Schemas y negativos (`ac531f6`) |
| I4 | Integración real en rama coordinada CoreRPG (`d409a17`) |
| I5 | Knowledge, guardado y compatibilidad en CoreRPG (`960a3cf`) |
| I6 | Validación Windows/Linux configurada (`cb5c632`) |
| I7 | Esta acta y manual de distribución/reproducción |

## Evidencia ejecutada inicial

Linux x86_64, Python 3.12/jsonschema 4.26.0: 18 unittest aprobados, extracción
idéntica dos veces y validación de todos los artefactos, fuentes y schemas.
CoreRPG GCC 14.2/C++20, commit de integración `960a3cf`, contra los bytes de esta
publicación: 445/445 CTest aprobados (433 anteriores + 11 C++ Nimroel + preflight).
La CI coordinada se fijará al SHA de publicación de esta rama. Los resultados
remotos y SHAs finales se registran en las dos PR Draft; no se infieren de estos
resultados locales. Sanitizadores y Windows están sujetos a esa evidencia final.

Huella de publicación inicial:
`45c143a8e997e74617ab5bf9d12245ce3f59e023f7d677c299440d73897808af`.
La receta usa semilla 413001 y contexto regional 1; población 50, dos identidades
materializadas, 48 latentes. No sortea servicios ni construye hogares/layout.

## Matriz de alcance V001

| Requisito original | Evidencia 4.13 / límite |
| --- | --- |
| G01 | Rangos del contenido y reserva 50 probados; múltiples instancias completas pendientes |
| G02/G03 | Capacidades/servicios opcionales validados como declaraciones; 100 semillas y hogares reales pendientes |
| G04 | Fixture estructural repetible y carga con orden invertido; generador completo pendiente |
| G05/G06 | Grafo mínimo explícito, sin simulación de cobertura, costes o layout |
| P01–P04 | Proyección parcial estructural probada; exploración, conversación y escenas Godot pendientes |
| Q01–Q08 | Categoría del útil y capacidad identificables; condición, propiedad, espera, reparación y devolución pendientes |
| S01 | Estado estructural, RNG, Knowledge y siguiente ID probados; hogares/calendario pendientes |
| S02–S04 | Codec real y continuidad estructural; progreso/colas/vida autónoma de dominio pendientes |
| S05 | Rechazo previo de huellas/versiones distintas; ninguna migración automática |
| S06 | Fixture, orden, snapshots y contexto deterministas; historia completa pendiente |
| H01–H04 | Harness sin motor y diagnóstico privilegiado; HUD, IA remota y experiencia humana pendientes |

Los documentos V001 originales mantienen `testsExecuted=false` porque describen
la vertical jugable completa. Esta acta acredita sólo las rutas realmente ejecutadas
en 4.13. Los contratos ricos no son ejecución C++ por estar en Datos operativos.

Publicación mediante dos PR Draft coordinadas. No fusionar automáticamente;
la aprobación y cierre corresponden a auditoría humana. Star Trek conserva su
main `577fd1bfda89205f5d8a95e27cde13cadc46f04d`, sin modificaciones.

Incidencia CI de preparación: el primer workflow intentó leer CoreRPG privado
desde el token limitado del repositorio público y falló en checkout antes de
ejecutar tests. Se eliminó esa dependencia de acceso: los schemas privados y
C++ se verifican en CoreRPG, y Nimroel valida su publicación propia. Se fijan LF
para reproducir hashes entre Windows/Linux. No se amplían permisos ni se publican
fuentes o schemas de CoreRPG en Nimroel.
