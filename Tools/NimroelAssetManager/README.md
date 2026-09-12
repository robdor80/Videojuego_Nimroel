# Nimroel Asset Manager

Base local-first para la futura biblioteca visual de Nimroel. La aplicación Android es la primera interfaz de producción; `contracts/` contiene los acuerdos de datos que deberán poder consumir también futuras herramientas Windows.

## Estructura

- `android/`: aplicación nativa Kotlin, Jetpack Compose y Material 3.
- `contracts/`: contratos compartibles, independientes de plataforma.
- `docs/`: decisiones y evolución del producto.

La app se abre en una pantalla identificable y contiene límites iniciales de dominio, UI y almacenamiento remoto. No guarda ni sincroniza assets todavía.

## Verificación

Desde esta carpeta: `./gradlew.bat build` y `./gradlew.bat test`.

## Seguridad

No hay credenciales ni integración de subida a ImageKit. Cualquier integración futura debe usar un servicio autenticado; una clave privada nunca pertenece al APK.
