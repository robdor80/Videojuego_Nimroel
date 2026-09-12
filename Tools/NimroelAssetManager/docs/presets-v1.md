# Presets de producción v1

Un preset es configuración reutilizable; no es un Asset ni estado de lote/sesión. Tiene ID y versión propios, referencia un único Vocabulary Set mediante `vocabularySetId/vocabularySetVersion` y precarga valores sin duplicar bindings de vocabulario.

Cada selección declara:

- `fixed`: el preset impone el valor al aplicarse; el flujo normal no lo cambia salvo acción explícita de abandonar o modificar el preset.
- `suggested`: valor inicial preseleccionado que el operador puede cambiar normalmente.

Un campo sin definir se omite. Los bloques `classification`, `subject`, `details`, `visual` y `provenance` no pueden aparecer vacíos. `visualProfileId/visualProfileVersion` y `promptTemplateId/promptTemplateVersion` son parejas inseparables; los campos de versión usan la sintaxis de versión del contrato, no la de un ID.

Los presets contienen referencias a perfiles visuales y prompt templates, nunca sus reglas o prompts completos. Esos contratos aún no tienen registros canónicos.

`npc-portrait-pilot.example.json` es un ejemplo no productivo limitado a `adult` y `neutral`. No existe todavía información suficiente para un preset productivo con reino/cultura, especie, género, profesión, clase social, perfil visual y prompt template.

## Jerarquía

```text
Vocabulary JSON       define valores
Vocabulary Set JSON   enlaza ruta → Vocabulary/version
Preset JSON           precarga valores mediante un Vocabulary Set
Asset JSON            describe una imagen concreta
Lote/sesión            estado operativo futuro, fuera de este hito
Kotlin                 consume y valida los contratos anteriores
```

Android usa modelos JVM puros, `VocabularyRegistry`, `VocabularySetRegistry`, `PresetRegistry` y `ProductionContractValidator`. La validación cruza preset → set → vocabulary/version → valor sin mantener una tabla editorial de IDs en Kotlin.
