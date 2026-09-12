# Adaptación Android de Asset Schema v1

Android representa la ficha canónica mediante `domain.model.Asset` y sus tipos asociados. El modelo no depende de Android, Room, ImageKit ni estado de sincronización.

`AssetJson.codec` usa `kotlinx.serialization`; el serializador de `Asset` selecciona el subtipo sellado de `AssetDetails` a partir de `type`, sin añadir discriminadores Kotlin al JSON. La validación adicional se ejecuta con `AssetValidator.validate` y devuelve los incumplimientos de dominio que no se pueden expresar sólo con tipos Kotlin.

Los tests JVM consumen los recursos directamente desde `../contracts`, incluidos los ejemplos válidos y los fixtures inválidos. El JSON Schema sigue siendo la autoridad para validación estructural completa en tooling; la app no incorpora un motor JSON Schema en runtime.
