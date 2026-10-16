# NIM-03 BUILD — Cierre y traspaso a la fase siguiente

Fecha: 16/10/2026. Repo: robdor80/Videojuego_Nimroel. PR #19. Cierre solicitado explícitamente por el propietario, aceptando pendientes diferenciados.

## Validado y aprobado

1. Godot 4.7.2 Standard 2D: Windows x64, APK Android ARM64, tests de regresión NIM-01/02/03, inferencia real TTS y exportaciones en tres jobs verdes. CI anterior al cierre documental: https://github.com/robdor80/Videojuego_Nimroel/actions/runs/38856792436 (head 8f9bed5).
2. MSI Windows: modo demostración con bocadillos, simulador y retrato, scroll de historial; modo integración sin autoridad CoreRPG (bloqueo correcto), fallo seguro sin proxy. Comprobado por el usuario mediante capturas.
3. MSI Godot con proxy Python localhost, credencial solo en variables de entorno de PowerShell: Google Gemini 3.5 Flash-Lite realmente conectado en modo diagnóstico de intenciones. Clasificaciones dialogar y desplazarse confirmadas en pantallas. No es narrativa real de NPC, no modifica WorldState.
4. TTS sherpa-onnx en Windows CI: dos WAV castellanos generados auténticamente, reproducidos **fuera de Godot** y aprobados auditivamente por el usuario. Son claros y relativamente naturales con matiz ligeramente mecánico. No hay TTS dinámico en juego.
5. Galaxy Tab S9+: el usuario confirma pruebas funcionales del APK original. Realme GT Neo 2 ARM64: pruebas de arranque, entrada, modos y reapertura correctas, con optimización móvil pendiente.

## Pendientes expresamente NO validados

- Teclado Samsung virtual/Bluetooth: el ajuste está implementado y pasó smoke geométrico, pero **no se ha probado la APK corregida físicamente en Tab S9+**. Excepción del cierre, trasladada a fase sucesora y a tratar con prioridad. Deben probarse teclados virtual y Bluetooth, scroll, Enviar, recuperación de panel tras cerrar IME.
- Gemini 3.8 Flash: el catálogo API devuelve HTTP 200 y generateContent true; peticiones reales mínimas devuelven HTTP 503 UNAVAILABLE incluso sin nuestro proxy ni JSON schema. No validado, reintentar separadamente, no asumir que es fallo de Godot ni saturación transitoria garantizada.
- Mistral Medium 3.5: **aún no se ha creado API key ni adaptador seguro ni existe soporte Mistral en Nimroel**. Mañana verificar disponibilidad, cuenta, cuotas, privacidad y coste; crear clave sin divulgarla, implementar proxy/adaptador protegido y probar diagnóstico desde Godot MSI. No confundir tener clave con tener integración funcional; preservar estabilidad de la rama principal.
- TTS dinámico en Godot, STT/ASR por micrófono, CoreRPG GDExtension y motor narrativo real siguen pendientes. No son logros de esta fase.
- Cabecera visual muestra texto heredado v0.0.1. Corrección cosmética futura; no confundir con versión de paquetes.
- API externa Free: no presumir bolsas promocionales ni capacidad ilimitada. No poner claves en EXE, APK, repositorio ni capturas; proteger canon privado. CoreRPG es la autoridad de mundo.

## Orden sugerido después de cerrar

1. Confirmar CI verde del HEAD final de PR #19, fusionar a main con la autorización de finalización y verificar estado real en GitHub.
2. Abrir nueva fase desde main, previa definición de objetivos. Probar pronto el ajuste IME/Bluetooth en Tab S9+ corregida.
3. Otro día: reintento acotado de Gemini 3.8; evaluación Mistral Medium 3.5 con control de coste, privacidad, validaciones y fallback. Un proveedor alternativo NO debe influir en WorldState ni inventar hechos.
4. Estudiar integración dinámica de sherpa-onnx en Godot Windows y Android en la fase que corresponda, separada del banco WAV.

La solicitud de finalizar NIM-03 acepta el traslado de reservas como trabajo futuro, pero NO las convierte en pruebas superadas.
