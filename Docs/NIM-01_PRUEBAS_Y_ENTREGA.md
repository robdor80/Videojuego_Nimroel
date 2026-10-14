# NIM-01 — evidencia técnica, entrega de prototipos y comprobación humana

**Estado:** NIM-01 en PR Draft; no fusionar hasta revisión. La versión es un **laboratorio de interfaz**, no Nimroel RPG v0.0.1 jugable.

## Resultado automático acreditado

- Versión: Godot **4.7.2.stable.official.ed1daf0bf**.
- CI de Godot: importación de SVG, análisis de scripts y escena, pruebas de intención demo sin mutación de WorldState.
- Primer run verde: https://github.com/robdor80/Videojuego_Nimroel/actions/runs/38554044808 (commit 8d69b039).
- Exportación Windows **.exe + .pck** y Android **.apk**: run verificado https://github.com/robdor80/Videojuego_Nimroel/actions/runs/38554703350 (commit d41e943a).
- En los runs siguientes, la CI comprueba además bocadillos separados, puertos Core/voz que responden error en lugar de inventar funciones, formato de librerías ARM64 del APK y hashes SHA-256 de paquetes.

**Importante:** que Godot exporte a Windows/Android acredita el empaquetado, NO acredita que el binario haya sido ejecutado en el MSI o que el APK haya sido instalado/probado en la Tab S9+.

## Paquete descargable sin instalar Godot

En el run de CI que haya terminado verde, sección **Artifacts**, elegir \`NIM01-Godot-Prototype-Windows-Android\`; contiene:
- \`Nimroel_NIM01_Windows.exe\` (para MSI).
- \`Nimroel_NIM01_Windows.pck\` (debe permanecer junto al exe).
- \`Nimroel_NIM01_TabS9Plus.apk\` (instalación Android ARM64 de depuración).
- \`SHA256SUMS.txt\` cuando provenga del workflow actualizado.

Los artefactos se conservan 14 días. No son distribución final, están firmados con clave de depuración temporal y **no deben publicarse como v0.0.1 ni instalarse sobre otras compilaciones sin precaución**.

## Protocolo MSI Windows

1. Descargar desde la sección Artifacts, extraer el ZIP, y poner .exe y .pck en la **misma carpeta**.
2. Ejecutar \`Nimroel_NIM01_Windows.exe\` directamente (no hay instalador).
3. Comprobar ilustración de fondo, cabecera «MODO MAQUETA», bocadillos e input por teclado/ratón.
4. Probar las frases: «¿Qué veo desde donde estoy?», «Avanzo por la aldea», «Hablo con un aldeano», «Guardo la partida».
5. Verificar que las respuestas describen **un simulador sin mundo cargado**, que el retrato solo es provisional y que la acción «guardo» **no** afirma haber guardado.
6. Probar redimensionar la ventana y mantener texto legible; reiniciar demo.
7. Anotar sistema operativo, resolución, comportamiento, capturas y fallos.

No introducir claves Gemini en esta build; no hay cliente de API incorporado.

## Protocolo Samsung Galaxy Tab S9+ Android

1. Descargar el ZIP del run verde, extraer e instalar el APK \`Nimroel_NIM01_TabS9Plus.apk\` mediante el gestor de archivos en la **Tab S9+**, autorizando instalaciones de esa fuente solo si se desea ejecutar este prototipo de confianza.
2. Si existe una versión de prueba previa con el mismo identificador y distinto certificado, puede requerirse desinstalarla (se perderán datos locales de esa app). Los builds CI emplean keystore temporal.
3. Iniciar sin MSI conectado. Comprobar pantalla horizontal, orientación, legibilidad, panel narrativo, botones táctiles, teclado del sistema, envío y reinicio.
4. Probar texto largo, retorno del teclado, pausa/reanudación, cambio de apps y rotación no admitida si se ha fijado apaisado.
5. El APK **NO contiene** CoreRPG, sherpa-onnx, micrófono ni Gemini: no esperar voz ni gameplay real.
6. Registrar versión Android, resolución/escala (opcional), latencias/fallos y capturas.

La prueba real de CoreRPG mediante NDK + GDExtension es una tarea **diferente** y pendiente; un APK que abre sin Core no acredita ese enlace.

## Semáforo de aceptación y responsabilidades

| Requisito | Resultado |
|---|---|
| Interfaz Godot carga y scripts pasan smoke en Linux CI | **VERIFICADO** |
| Windows x64 exporta ejecutable de demo | **VERIFICADO** |
| APK Android ARM64 exportable | **VERIFICADO** |
| Windows MSI ejecuta y UI responde | **PENDIENTE prueba en MSI** |
| Galaxy Tab S9+ instala APK y UI táctil funciona | **PENDIENTE prueba en tablet** |
| Gemini responde libremente | **NO INTEGRADO** (posterior) |
| CoreRPG enlazado con GDExtension y mundo real | **NO INTEGRADO** (posterior) |
| sherpa-onnx ASR/TTS local | **NO INTEGRADO** (posterior) |
| Voces femeninas/masculinas castellanas por NPC | **NO PROBADO** (posterior) |
| Generador procedural completo + aldea viva V001 | **NO IMPLEMENTADO** (fases posteriores) |
| Tests de lore V001 G/P/Q/S/H completos | **NO EJECUTADOS** |

## Criterios de revisión de la PR

- [ ] Último commit con CI verde y ambos artefactos publicados.
- [ ] Verificación manual del MSI y de la S9+ (o aplazamiento formal si solo se aprueba la cimentación técnica).
- [ ] PR #13 inspeccionada: no modificar lore/worldbuilding ni CoreRPG, y commits conforme a convención.
- [ ] Verificar continuidad de contratos de Core, voz, intención y visualización.
- [ ] Guardar resultado de pruebas e incidencias antes de decidir el merge.

## Fuentes de producto

- \`Docs/NIM-01_BUILD_PLAN.md\`
- \`Docs/NIM-01_DECISION_GODOT_WINDOWS_TAB_S9_PLUS.md\`
- \`Docs/NIM-01_CONTRATO_CONVERSACION_Y_VOZ.md\`
- \`Docs/NIM-01_AUDITORIA_ANDROID_CORERPG_VOZ.md\`

No se ha alterado el canon de \`Worldbuilding\`.


## Informe de prueba real — Samsung Galaxy Tab S9+ (14/10/2026)

**Origen de evidencia:** capturas remitidas por el usuario desde su Samsung Galaxy Tab S9+, instalando el paquete NIM-01 generado en GitHub Actions. La evidencia visual no es un test instrumentado de Android ni valida micrófono, Gemini o biblioteca CoreRPG.

### Incidencia detectada en primer APK
- La interfaz de inicio se mostraba en horizontal, con el paisaje y el panel de relato, pero **el campo de escritura quedaba oculto** fuera del área visible.
- Causa localizada en el layout inicial de la conversación; el historial podía desplazar las acciones de la parte inferior.
- Corrección realizada en `Game/Host2D/scripts/main.gd`: barra de entrada anclada abajo y historial con espacio variable, más prueba automática contra desbordamiento de controles de escritura.
- CI de APK corregido: https://github.com/robdor80/Videojuego_Nimroel/actions/runs/38593322081 (success).

### Segunda captura después de instalar el APK corregido
- **Verificado por captura:** aplicación iniciada en Tab S9+ apaisada.
- **Verificado por captura:** campo de escritura y botón «Enviar» visibles en el panel inferior.
- **Verificado por captura:** el jugador envió «Qué veo desde aquí?»; aparece bocadillo de jugador.
- **Verificado por captura:** aparece respuesta del **simulador**, que informa que CoreRPG no está conectado; el historial tiene barra visible de desplazamiento.
- **Verificado por captura:** botón «Reiniciar demo» visible, pero su funcionamiento táctil no ha sido probado expresamente.
- **No evaluado:** uso prolongado, rotación/pantalla completa, retorno del teclado, reinicio, audio, instalación en MSI Windows ni consumo/estabilidad bajo carga.

**Resultado:** smoke de pantalla e interacción textual **APROBADO visualmente para la Galaxy Tab S9+**; el problema de controles ocultos quedó corregido. Se mantiene pendiente la prueba Windows MSI y las integraciones funcionales posteriores. No confundir este resultado con una partida Nimroel conectada a CoreRPG, Gemini o sherpa.
