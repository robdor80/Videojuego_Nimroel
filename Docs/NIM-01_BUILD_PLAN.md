# NIM-01 BUILD — arquitectura y arranque del juego 2D conversacional

**Estado:** arquitectura y planificación en PR Draft; sin juego compilado ni pruebas de ejecución.
**Rama:** feat/nim-01-build
**Base:** lore de la primera aldea V1 y «La herramienta rota» integrado mediante PR #12.
**Definición de experiencia:** [NIM-01_EXPERIENCIA_CONVERSACIONAL.md](NIM-01_EXPERIENCIA_CONVERSACIONAL.md).
**Generación espacial:** [NIM-01_GENERACION_ESPACIAL_PROCEDURAL.md](NIM-01_GENERACION_ESPACIAL_PROCEDURAL.md).
**Auditoría de riesgos Android y voz:** [NIM-01_AUDITORIA_ANDROID_CORERPG_VOZ.md](NIM-01_AUDITORIA_ANDROID_CORERPG_VOZ.md).
**Contrato de conversación y sherpa:** [NIM-01_CONTRATO_CONVERSACION_Y_VOZ.md](NIM-01_CONTRATO_CONVERSACION_Y_VOZ.md).

## 1. Propósito

Preparar el ejecutable de **Nimroel RPG v0.0.1 — primera aldea V1 de Treskal** sin modificar el canon, duplicar CoreRPG ni presentar simulaciones visuales como mecánicas verdaderas.

## 2. Decisiones de dirección jugable

- Windows y Android, **solo 2D**: imágenes de fondo para ambientación y retratos en interacciones, sin modelos 3D.
- Exploración **conversacional por lenguaje natural**: el jugador habla o escribe «qué veo», «avanzo», «pregunto», «busco», «llevo la herramienta» y otras intenciones.
- Sin desplazamiento obligatorio de un avatar 2D, ni búsqueda de hotspots/clics obligatorios sobre una imagen; la ilustración puede omitir objetos, edificios o NPC existentes.
- La IA interpreta y narra como Máster; el motor determina qué se ve, qué se sabe, qué sucede y si una acción está autorizada.
- **También se genera proceduralmente el plano lógico de cada aldea:** edificios, hogares, espacios productivos, caminos, conexiones y posiciones; no se diseñan planos individuales a mano ni se exige mostrarlos gráficamente. El layout generado es estable y persistente.
- **Modelos de IA ya decididos por el autor:** Gemini 3.5 Flash-Lite habitual y Gemini 3.8 Flash para trabajo más exigente. Requisito de explotación indicado: servicio gratuito en el EEE. No reabrir comparación de proveedores; integración/API y condiciones efectivas quedan sujetas a comprobación durante las pruebas.
- CoreRPG mantiene el WorldState; Nimroel añade las reglas de su mundo y el Host solo solicita/representa. No permitir que una narración cree hechos.
- Windows: teclado y ratón; Android: pantalla táctil con aplicación independiente del PC.
- El encargo «La herramienta rota» sigue siendo opcional, emergente y persistente, nunca una misión obligatoria ni una excusa para fijar la aldea.
- Placeholders 2D permitidos para pruebas; no tratar arte provisional como asset final NAP.

## 3. Experiencia e interfaz

El Host presentará un escenario ilustrado de contexto, panel narrativo con historial, entrada libre, y retrato pertinente al mantener conversación con un NPC. Los elementos opcionales de UI (menús, sugerencias, accesibilidad) no deben impedir órdenes libres ni condicionar la existencia de objetos/servicios.

Ruta lógica futura: texto/voz transcrita -> intérprete de intención -> consulta o solicitud estructurada -> CoreRPG y reglas Nimroel -> resultado y contexto autorizado -> narración IA -> Host 2D.

Preguntas descriptivas no mutan el mundo. Las acciones con varios pasos requieren validación y resultados por etapa. Ante órdenes ambiguas, aclarar antes de efectos no deseados. Nunca revelar conocimiento que no corresponde al observador.

**Distinción de modo:** la aplicación puede arrancar sin IA remota y ofrecer un modo técnico limitado para probar la interfaz y el Core; ello **no implica experiencia conversacional libre equivalente sin IA**. Evaluar interpretación local/remota/híbrida y ASR/TTS antes de prometer operación offline plena en Windows o Android.

## 4. Tecnología candidata, pendiente de spike

- Primera candidata: **Godot estable estándar**, como interfaz y Host 2D, por exportación Windows/Android, paneles gráficos y posible integración de núcleo C++ mediante GDExtension.
- Contingencia: SDL3 + C++ si las pruebas reales demuestran inconvenientes materiales para el Host de conversación.
- Ninguna elección es definitiva hasta una prueba técnica de interfaz y compatibilidad. No afirmar que CoreRPG está enlazado, que Android funciona o que la voz está integrada antes de probarlos.

## 5. Estructura propuesta (crear progresivamente)

- Game/ — ejecutable Nimroel, separado de Worldbuilding.
- Game/Host2D/ — pantalla, fondo, retratos, historial, texto/voz y controles; sin autoridad de hechos.
- Game/BridgeCoreRPG/ — futuro adaptador a C++20, con contratos de consulta/acción y sin WorldState duplicado.
- Game/Interaction/ — intérprete de intenciones, narración controlada y adaptadores de voz/IA; sin mutación directa.
- Game/Content/TreskalV001/ — datos V1, fixture regional versionado, grafo interno/layout procedural persistible y mapping al futuro Content Pack. El fixture regional **no** es un plano prehecho de la aldea.
- Game/Tests/ — pruebas de UI, contratos, generador e integración V001, con evidencia.
- Worldbuilding/ — canon, biblias visuales, prompts y assets de origen, no mover ni reescribir sin necesidad.

## 6. Ejecución incremental NIM-01

1. Registrar la modalidad conversacional y su autoridad (realizado en documentación).
2. Probar una interfaz 2D mínima para Windows: fondo ilustrado, historial, caja de texto, retrato contextual y respuesta estructurada de ejemplo.
3. Estructurar Host e interfaz en un proyecto compilable; no implementar acciones falsas.
4. Documentar contratos y pruebas del conducto petición -> respuesta, usando fixtures temporales claramente etiquetados, sin inventar APIs de CoreRPG.
5. Probar diseño adaptativo Windows/Android y evaluar exportación Android de forma independiente.
6. Definir la integración de los modelos Gemini elegidos y la ruta de voz sherpa-onnx (ASR local como preferencia a probar y TTS con voz por NPC), sin exigir una API activa al primer arranque técnico ni declarar que ya funciona. Entrada del jugador escrita/hablada en su bocadillo, **nunca reproducida con TTS**; intervención del NPC en bocadillo y salida por voz. Narración general como texto por defecto.
7. Registrar evidencia real, incidencias y decisiones; mantener PR Draft hasta revisión y validación.

## 7. Dependencias

- CoreRPG 4.5–4.8: identidad, relaciones, RNG, población agregada, snapshots estructurales (no simulan ya toda la aldea).
- 4.9: conocimiento/percepción por observador.
- 4.10: acciones, tiempo, simulación causal y continuidad fuera de escena.
- 4.11: inspector.
- 4.12: Context Builder y paso seguro a IA.
- 4.13: primer Content Pack Nimroel.
- NAP: assets finales cuando proceda; placeholders autorizados.
- Android: verificación independiente Windows + NDK/export y dispositivo.
- 4.14 Unreal/Star Trek: NO bloquea Nimroel.

## 8. GitHub y pruebas

- Rama de paquete feat/nim-01-build desde main; PR Draft; commits de unidad lógica conformes con Docs/NIMROEL_GIT_COMMIT_CONVENTIONS.md.
- No modificar el canon de PR #12 para resolver un problema del Host.
- No fusionar sin auditoría humana del paquete aprobado.
- Evidencias de cada prueba: commit Nimroel, commit CoreRPG si aplica, plataforma, pasos, observado, incidencia y estado.
- No convertir mock, documentación o código no compilado en test «aprobado».

## 9. Criterios de salida NIM-01 — ejecución real

- [x] Modalidad definida: RPG conversacional, sin clics obligatorios ni avatar móvil.
- [x] Frontera técnica de autoridad descrita, junto con contratos de Core/voz que NO fingen capacidades activas.
- [x] Regla de layout procedural persistente documentada; implementación pendiente en paquetes posteriores.
- [x] Godot 4.7.2 Standard seleccionado y **validado por CI oficial Godot en Linux headless**.
- [x] Proyecto importable y escena 2D básica comprobados en CI; bocadillos de jugador/respuesta, fondo, retrato provisional, teclado y respuesta de prueba sin mutaciones.
- [x] Exportación del prototipo **Windows x64 (exe+pck) y Android ARM64 (APK)** por GitHub Actions, sin credenciales ni IA remota.
- [x] Comprobación del tipo ARM64 del APK y SHA-256 de artefactos en CI.
- [x] Contrato de integración futura CoreRPG y sherpa/Gemini documentado; ni Core ni sherpa integrados aún.
- [x] Plan de pruebas, limitaciones de demo y protocolo para MSI/Tab S9+ documentados.
- [ ] **Ejecución real en MSI Windows**: requiere abrir el exe exportado en el equipo objetivo.
- [ ] **Instalación/ejecución en Galaxy Tab S9+**: requiere prueba táctil sobre el dispositivo objetivo.
- [ ] Auditoría humana de la PR y autorización para fusionar.

**Evidencia de CI:** https://github.com/robdor80/Videojuego_Nimroel/actions/runs/38554823204 (dos jobs correctos; artefacto Windows+Android). Véase [NIM-01_PRUEBAS_Y_ENTREGA.md](NIM-01_PRUEBAS_Y_ENTREGA.md) para límites y procedimientos. No existe evidencia de ejecución física, llamadas Gemini, CoreRPG real o voz sherpa.

**No forman parte del cierre técnico de NIM-01:** aldea V1 completa, NPC vivos, reconocimiento o síntesis de voz real, encargo ejecutable, Content Pack definitivo, guardado integral ni lanzamiento v0.0.1. Su implementación se programará en paquetes posteriores manteniendo la experiencia conversacional definida.

**Estado de entrega:** paquete técnico de cimentación compilado y exportado para ambas plataformas, **pendiente de smoke en MSI/Tab S9+ y merge autorizado**.
