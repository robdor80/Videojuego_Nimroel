# NIM-01 BUILD — arquitectura y arranque del juego 2D

**Estado:** planificación técnica en rama de desarrollo; sin juego compilado ni pruebas de ejecución.
**Rama:** feat/nim-01-build
**Repositorio:** robdor80/Videojuego_Nimroel
**Base de alcance y canon:** Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Valrik/Aldeas/03_Prueba_v0.0.1/ (PR #12 fusionada).

## 1. Propósito

Preparar el proyecto ejecutable de **Nimroel RPG v0.0.1 — la primera aldea V1 de Treskal**, sin modificar el lore cerrado y sin crear un segundo motor RPG.

Este documento organiza únicamente trabajo técnico. No es un Content Pack de CoreRPG ni una prueba superada.

## 2. Decisiones de producto confirmadas

- Juego **estrictamente 2D** para **Windows y Android**. Ningún modelo, escenario o personaje 3D.
- Escenarios y ambientes ilustrados como **imágenes de fondo**.
- **Retratos de NPC durante las interacciones** y diálogos.
- Interacción local y jugabilidad sin depender de una IA o servicio de red.
- Windows: ratón y teclado; Android: controles táctiles, aplicación autónoma sin depender del PC.
- CoreRPG (otro repositorio) es la única autoridad del estado lógico; presentación y gráficos no son entidades ni hechos del mundo.
- En el primer ensayo se permite utilizar material gráfico provisional compatible con el estilo, sin atribuirle aprobación NAP ni categoría de asset final.
- La prueba sigue siendo libre: «La herramienta rota» se descubre opcionalmente y no gobierna la generación de la aldea.

## 3. Decisión de interacción pendiente (único bloqueo de UX)

Confirmar con el autor cómo se recorre el espacio:
- A: **escenas ilustradas conectadas**; seleccionar caminos, puertas y NPC, sin avatar caminando.
- B: **mapa 2D transitable**, avatar bidimensional caminando sobre escenarios dibujados y retratos solo al conversar.

No implementar movimiento, hotspots, cámara o navegación definitiva hasta confirmar A/B. La arquitectura debe poder conservar entidades, hotspots/contextos y acciones sin acoplar el WorldState al renderizado.

## 4. Tecnologías candidatas: recomendación, no aprobación definitiva

**Candidata principal: Godot 4.7.2 estable, versión estándar sin .NET.**

Justificación: flujo 2D e interfaz adaptable, manejo de imágenes/retratos, exportación Windows/Android, entrada de ratón/táctil y posibilidad de conectar código C++ a través de GDExtension. Godot es presentación, no motor de reglas. GDScript se limitaría a la interfaz y adaptación; todo hecho persistente deberá resolverlo CoreRPG o las reglas específicas Nimroel autorizadas a través de su integración.

**Alternativa contingente: SDL3 + C++**, si un spike real desaconseja Godot/GDExtension por coste o incompatibilidad. No diseñar un renderizador ni UI custom antes de medir la opción preferente.

La decisión final exige prueba de arranque Windows, validación de exportación Android y comprobación posterior del enlace de CoreRPG. No inferir soporte Android a partir de compilar Windows.

## 5. Estructura futura propuesta (a crear solo cuando se necesite)

- Game/ — raíz del juego ejecutable, distinta del canon.
- Game/Host2D/ — escenas, interfaz, HUD, retratos y manejo de controles.
- Game/BridgeCoreRPG/ — integración C++20 y adaptador que NO conserva otro WorldState.
- Game/Content/TreskalV001/ — fixture regional versionado, datos de generación V1 y mapeos futuros a Content Pack.
- Game/Tests/ — smoke tests y matriz de aceptación V001 con evidencias.
- Worldbuilding/ — canon, biblias visuales y assets fuente (no mutar ni duplicar sin necesidad).

Los nombres son provisionales hasta crear la implementación real. Los assets visuales aprobados se referenciarán con manifest o IDs, evitando mover la biblioteca original.

## 6. Orden de ejecución NIM-01

1. Registrar las invariantes y resolver el tipo de exploración (A/B).
2. Tomar la decisión de Host con una prueba acotada: arranque 2D Windows, imagen de fondo, overlay de retrato y entrada local.
3. Crear estructura mínima de proyecto, configuración reproducible y README de compilación.
4. Comprobar tamaño, escalado y navegación para pantalla Windows y diseño táctil Android (sin proclamar builds ejecutados).
5. Realizar smoke Android real cuando sea viable (SDK/export templates y dispositivo); registrar plataforma y resultado separado del de Windows.
6. Definir el puerto mínimo futuro hacia CoreRPG: identidad/consulta, presentación, solicitudes estructuradas y snapshots sin introducir APIs ficticias.
7. Ejecutar los checks disponibles, documentar evidencias y preparar la PR para revisión.

## 7. Contratos y autoridad

- Leer los documentos de PR #12 como origen de alcance y matriz V001-G/P/Q/S/H.
- Nunca escribir desde diálogos o scripts visuales directamente el estado lógico ni la propiedad, reparación, tiempo o conocimiento.
- CoreRPG 4.5–4.8 permite infraestructura estructural; 4.9–4.13 incorpora progresivamente conocimiento, acciones/simulación, inspector, contexto y primer Content Pack Nimroel.
- No introducir nombres, NPC ni edificios específicos predefinidos como canon; los fixtures de prueba serán explícitos y versionados.
- No simular un motor completo solo para declarar el encargo superado.

## 8. Política de desarrollo y GitHub

- Cada paquete NIM se desarrolla en rama propia desde main actualizado, mediante commits pequeños con la norma oficial Docs/NIMROEL_GIT_COMMIT_CONVENTIONS.md.
- Para NIM-01: rama feat/nim-01-build, PR inicialmente Draft; no fusionar sin validación y revisión.
- No mezclar trabajo de CoreRPG ni NAP, ni modificar su repositorio/canon.
- Cada prueba debe identificar commit de Nimroel, commit de CoreRPG si aplica, plataformas realmente comprobadas y resultado observado.
- No interpretar documentación redactada, código sin compilar o una PR abierta como evidencia de juego funcional.

## 9. Criterios mínimos de salida de NIM-01

- [ ] Tipo de exploración aprobado.
- [ ] Tecnología de Host elegida tras evaluación técnica.
- [ ] Proyecto arrancable y escena 2D básica funcionando en Windows.
- [ ] Fondo y retrato provisionales en una interacción de prueba.
- [ ] Input local y escalado inicial comprobados.
- [ ] Android planificado desde el inicio; smoke exportación/instalación probado y anotado, o aplazamiento explícito con motivo.
- [ ] Integración futura CoreRPG documentada sin segundo WorldState.
- [ ] Archivos, commits y PR auditados; build/tests reportados con precisión.

**No forman parte del cierre de NIM-01:** aldea V1 completa, población viva, Content Pack operativo, reparación simulada, matriz V001 completa ni lanzamiento de Nimroel v0.0.1.
