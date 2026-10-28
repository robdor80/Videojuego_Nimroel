# NIM-07 / I3 — Encargo Codex: consultas comprensibles del primer observador de Treskal V001

**Autorizado tras auditoría I2, 27/10/2026.** Trabajo limitado a I3; el documento `07_AUDITORIA_ACEPTACION_I2.md` es la referencia de partida. No completar I4, fusionar ni abrir PR final.

## Propósito visible al jugador

La pantalla principal ya consulta un mundo auténtico pero responde de modo técnico. I3 debe permitir a una persona formular unas pocas preguntas naturales y obtener **respuestas breves en español, comprensibles y completamente verificables** a partir de los hechos de `CoreRPGSession.context`. No convertir el fixture en una aldea viva que no se ha generado.

### Antes de cambiar nada

- Confirmar rama `feat/nim-07-first-rpg-experience`, conservar I1/I2 y consultar HEAD; no intervenir en `main`. Leer `Docs/NIM-07/01_AUDITORIA_ALCANCE_Y_HOJA_DE_RUTA.md`, `06_RESULTADO_I2.md` y `07_AUDITORIA_ACEPTACION_I2.md`.
- Leer `Game/Host2D/scripts/{main.gd,native_conversation.gd,native_world_controller.gd,v001_pack.gd}` y `Game/Host2D/tests/{nim07_smoke.gd,nim07_i2_checks.gd}`. Conservar el pack, Core, C++ y pines intactos salvo necesidad estrictamente demostrada.
- Tener presente que el modo V001 no conoce taberna, frontera exterior ni segundo observador; ausencia de conocimiento no significa ausencia del mundo.

## Alcance funcional concreto

1. Incorporar una **interpretación cerrada, offline y determinista**, sin regex de extracción libre ni llamadas IA, para un pequeño repertorio de frases y variantes ortográficas seguras, por ejemplo:
   - `estado`, `¿qué sé?`, `¿qué conozco de la aldea?`.
   - `¿qué servicios conozco?`, `¿qué sé de la herrería?`.
   - `¿cuántos habitantes hay?` / `¿qué población conozco?`.
   - `¿qué sé de la herramienta?` / `¿dónde está la herramienta?` (responder **contención estructural autorizada**, no ubicación espacial).
   - `¿de dónde procede mi personaje?` (origen poblacional conocido, **no** ubicación actual, vivienda o procedencia biográfica).
   - `¿qué puedo preguntar?`: ayuda clara con los comandos realmente disponibles, sin anunciar acciones RPG inexistentes.
   No es obligatorio conservar estos textos exactos; mantener cobertura reducida y consistente y documentar el conjunto final.
2. **Una sola fuente de hechos:** cada respuesta deriva del `session.context` autorizado, con versiones de contrato revisadas; no leer catálogo privilegiado, JSON del pack ni listas fijas de entidades para contestar. El mapa estático de *etiquetas documentales* V001 solo puede aplicarse si Core acredita por conocimiento el hecho de existencia/definición; no asignar sentido nuevo a IDs arbitrarios.
3. Redactar respuestas agradables pero precisas: «Conoces una capacidad de herrería básica asociada a la aldea» solo si el contexto efectivamente aporta definición/relación autorizadas; «El agregado de aldea conocido declara 50 habitantes y 48 pendientes de materializar» solo si Core aporta el hecho de población. No afirmar **estar físicamente en esa aldea**.
4. Distinguir rigurosamente conocimiento positivo, ausencia explícita, desconocimiento y contexto truncado. Cuando el dato específico no está autorizado, decir que **no consta entre lo que conoce este observador**, sin dar detalles ocultos o números de otras entidades. No inferir de una ausencia de hechos que el mundo carezca de eso.
5. `¿Qué veo?`, `voy a la herrería`, `hablo con el herrero`, `reparo la herramienta` deben indicar límites verdaderos, no improvisar escenarios, eventos, acciones ni NPC. Para «¿dónde estoy?» distinguir origen poblacional de ubicación presente; la ubicación actual **no está modelada**.
6. Reutilizar `native_conversation.gd` y UI actual: los caminos I1 neutral, I2 V001, demo, diagnóstico independiente y control del teclado deben seguir funcionando. No crear un laboratorio ni pantalla paralela. Simplificar etiquetas técnicas en el modo V001 si ayuda, sin ocultar su carácter de **fixture estructural**.
7. En I3 **no se habilitan acciones con consecuencias por el mero hecho de reconocer lenguaje**. El único `submit` de sesión existente permite contención propia bajo autorizaciones: no equivale a caminar, viajar, recoger, entregar, reparar, conversar ni cumplir una misión. Si no existe una acción RPG semánticamente fiel, registrar esa brecha para posteriores fases en vez de simularla.
8. Mantener los proveedores Gemini/Sol/Luna, voz y APIs facturables fuera del camino V001. No modificar CoreRPG, canonical worldbuilding, Content Pack ni política de IA.

## Pruebas y entregables

- Crear **una smoke focalizada I3** que ejerza el texto de entrada de la pantalla principal, respuestas realmente leídas del contexto Core, versiones, seguridad en límites, ocultación de taberna/identidades desconocidas, truncamiento, no mutación de mundo/RNG y cambio de modo sin destruir la sesión. No generar una matriz de cientos de casos.
- Una prueba negativa de «solicitud de acción no soportada» y una de «ubicación/percepción no modelada» deben asegurar ausencia de alucinación; la respuesta no debe incluir «estás en», NPC, edificios específicos o misiones inexistentes.
- Ejecutar I3 con extensión real en Windows GitHub Actions y control Linux, mantener **I2 37/37, I1 48/48, NIM06 129/129**, regresiones NIM01–05. Android ARM64 compilar/exportar y verificar (CI no cuenta como ejecución Android física). Si el flujo I3 debe validarse en EXE exportado, usar el patrón seguro de argumento explícito corregido en I2; no repetir el problema de `--script`.
- Comprobar que las definiciones, los nueve archivos de publicación y el catálogo no cambian. Conservar prueba física final para I4 y evitar compilar repetidamente por cambios documentales.
- Publicar en esta rama `Docs/NIM-07/09_RESULTADO_I3.md` con: frases soportadas, ejemplos anclados a tipos de hechos Core, limitaciones, SHAs, enlaces CI y pruebas verificadas. Anotar explícitamente las dependencias para una interacción RPG real y para I4.
- Sin PR ni fusión, sin rebase con `main` en I3. El reencuentro con los avances recientes de `main` y las regresiones posteriores deberán tratarse antes de la PR final I4, con auditoría previa.

**Aceptación I3:** desde la pantalla principal, con Treskal V001 verificado y sesión de observador anónimo, se pueden hacer preguntas concretas en lenguaje cotidiano y recibir respuestas correctas, comprensibles y limitadas al conocimiento Core, sin mutaciones por consulta ni ficciones jugables.
