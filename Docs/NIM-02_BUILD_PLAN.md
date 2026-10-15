# NIM-02 BUILD — Plan y límites de aceptación

Fecha: 2026-10-15. Base inicial: main @ 191bcd5ea11308952f567f9e7e15f4f6ed2cf54a. PR #13 NIM-01 ya fusionada.

## Objetivo
Transformar el laboratorio Godot 4.7.2 Standard en un Host de conversación con fronteras explícitas y comprobables. Preparar integración real sin fingir partida, NPC, mutación ni llamadas a servicios ausentes. Mantener la UI 2D en MSI Windows x64 y Galaxy Tab S9+ Android ARM64.

## Pasos
1. P01: verificar rama main, PR NIM-01, escenas, código, CI y estado independiente de CoreRPG.
2. P02: normalizar/validar texto, identificar turnos y separar simulador visual de integración, con estados de error claros.
3. P03: preservar puerto CoreRPG de disponibilidad negativa hasta GDExtension real y un contrato común C++20.
4. P04: introducir contrato Gemini sin llamadas de red ni credenciales; nunca narrar hechos no autorizados.
5. P05: preservar contrato sherpa-onnx local ASR/TTS sin modelos descargados ni prometer audio.
6. P06: CI: regresión NIM-01, prueba NIM-02, exportación y hashes Windows/Android. Revisión humana por PR; no fusionar automáticamente.

## Dos modos de interacción
- Demo por defecto: respuestas deterministas etiquetadas SIMULADOR, ningún NPC real y mundo sin cargar.
- Integración: fallar con código explícito si falta CoreRPG. No llamar a Gemini ni introducir mundo alternativo. La ausencia de backend no se convierte en éxito.

## Garantías
- Un solo WorldState autoritativo, futuro CoreRPG; GDScript no simula reglas ni cambios de mundo.
- Worldbuilding y canon sin modificaciones; Godot para Nimroel, Unreal solo para Star Trek.
- Jugador escribe y lee bocadillos; narración hablada futura solo para NPCs con identidad autorizada; jamás atribuir voz a simulador.
- No almacenar claves API ni perfiles vocales binarios en repositorio o APK.
- No afirmar probados GDExtension, IA, ASR, TTS o ejecutables físicos si solo pasa CI.

## Fuera de este paquete
Enlace nativo C++ CoreRPG real, Gemini autenticado y funcionando, sherpa-onnx enlazado y modelos reales, mundo procedural cargado, Content Pack V001, NPC vivos, motor de acciones, guardado real y pruebas prolongadas físicas.

## Cierre
El alcance de software se considera terminado cuando el smoke de NIM-01 y NIM-02 y ambos exports pasan la CI. La verificación física MSI / Tab S9+ es otra puerta, pendiente hasta que el usuario la ejecute. PR Draft en revisión sin merge.
