# Pendientes y traspaso

Main integrado: `cd1735b1c9a1bb7507a3b1ce42d96c6d103b0977` (NIM-05 / PR #22).
CoreRPG `4f282863737bcd8f5add401202a9e1064c133672`; godot-cpp oficial
`e83fd0904c13356ed1d4c3d09f8bb9132bdc6b77`, API 4.5; Godot **4.7.2 Standard**.
Código verificado: `9924cc38f2fb1162e49ad80779db76c8e5d3f886`.
[CI nativa 39483287563](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39483287563) y
[regresiones 39483287443](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39483287443): success.
Checkout PR automático `7296c1eb43eaf3da96cc9d995f13bcdb9cb9c7eb`, árbol idéntico al HEAD de código.
[Pins](evidence/dependencies.json) · [Evidencia vigente](evidence/ci-summary.json) ·
[Integración NIM-05 y conservación de fuentes](11_INTEGRACION_MAIN_NIM05.md).
No se ha fusionado ninguna PR ni modificado main. Las pruebas físicas no están realizadas.

## Completado con pruebas automatizadas

Puente real, Host2D, sesiones limitadas, conocimiento autorizado, acciones Core,
precondiciones, relaciones, poblaciones, simulación explícita y RNG. Persistencia
Core v3 con recuerdos y continuación de streams; formatos reconocidos por el
codec upstream, sin inventar formato nuevo. I/O propiedad del Host, errores y
restauración segura. Compilación/enlace nativo en ambos destinos; pruebas Godot y
paquete Windows, APK ARM64 firmado e inspeccionado según evidencia 04/05.

Las pruebas de esta fase usan v3. No se declara una ejecución nueva de fixtures
completos v1/v2 upstream ni de toda la suite CoreRPG. No hay cambios al Core.

## Implementado, pendiente de prueba física

- Windows 11 MSI Raider: extraer paquete completo, suite y controles con teclado/ratón,
  guardado entre procesos y distribución limpia.
- Tab S9+: carga real GDExtension ARM64, suite, controles táctiles, save/restart,
  pausa/reanudación, aspecto/icono y logcat. Es criterio específico de aceptación.
- No hay resultado Android runtime en CI, ni se considera suficiente exportar APK.

## Disponible en Core, no implementado en este puente

- Catálogo/definiciones y ContentJson: requiere lectura de assets del Host y
  catálogo explícito en restore. El loader físico upstream no lee res:// de APK.
- Grants temporales administrados, políticas de sensores/secretos del juego,
  Inspector técnico completo y consultas administrativas de tablas.
- Sesiones de NPC/IA actúan como lectores; propuestas y autorizaciones de dominio
  futuras no se simulan con permisos universales.
- Un stream de eventos autorizado: Core publica consecuencias privilegiadas, no
  eventos públicos. Por eso events permanece vacío y las vistas son explícitas.

## Dependencias de fases posteriores

Core todavía no implementa contratos de combate, inventario, diálogo, memoria
episódica, reloj/cola de simulación, iniciativa autónoma ni autoridad/delegación
social. Ninguno se reconstruye en GDScript. Incorporarlos requiere fases futuras
del Core/sistemas reutilizables y políticas propias de Nimroel, con autorización
separada si se debe modificar CoreRPG. No bloquean la vertical estructural entregada.

Interpretación/narración IA y voz no se han integrado. El flujo de texto NIM-02
sigue mostrando un bloqueo honesto; disponer de biblioteca nativa no valida la
cadena conversacional. No se cambia política de modelos, proveedores ni cuotas.

## Próxima sesión

Leer 01, 03, 06 y ci-summary.json; comprobar PR #27 y heads protegidos antes de
trabajar. No fusionar sin revisión humana. Los artefactos caducan a los 30 días;
repetir el workflow sobre un SHA fijado para regenerarlos. Cada firma Android es
temporal: para reinstalar un APK firmado por otro job puede requerirse desinstalar
el paquete anterior, lo cual elimina datos; copiar saves primero si se necesitan.
No diseñar sincronización Windows/Android ni Companion en esta fase.

Antes de ampliar tamaños de mundo: medir coste del candidato, proyección y codec,
establecer presupuestos reales y realizar perfiles de memoria/rendimiento. No se
promete capacidad de producción masiva a partir de esta vertical acotada.

Actualización NIM05: ya integrada desde main cd1735b1. La referencia de partida
para el siguiente trabajo es el HEAD de la misma rama NIM06, con CI de código
9924cc38 y solo documentación posterior. PR23 no se integra por separado; revisar
su estado antes de una ampliación futura, sin modificarla por esta tarea.
