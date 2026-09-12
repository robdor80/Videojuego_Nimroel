# Vocabularios y Vocabulary Sets v1

Los JSON bajo `contracts/` son la fuente de verdad compartida. Kotlin y futuras herramientas Windows son consumidores, no fuentes de taxonomía.

## Vocabulary

Un Vocabulary define los valores admitidos para un concepto editorial. Cada documento tiene `vocabularyId`, `version` y `values`; la versión no forma parte del ID. Un valor requiere ID estable y label, y puede incluir descripción, estado `active`/`deprecated` y orden de presentación.

Para añadir o cambiar valores se publica una versión nueva, se valida contra `vocabulary-v1.schema.json` y se conserva la anterior mientras esté referenciada. JSON Schema valida la estructura; `VocabularyRegistry` valida además la unicidad semántica de `values[].id`.

## Vocabulary Set

Un Vocabulary Set es un manifiesto versionado. Su mapa `bindings` relaciona rutas canónicas del asset con un Vocabulary concreto y su versión exacta. Por ejemplo:

```text
subject.ageBandId → nimroel-age-bands 1.0
visual.expressionId → nimroel-expressions 1.0
```

El par `Asset.classification.vocabularyId/vocabularyVersion` referencia el ID y versión del Vocabulary Set. Así un asset puede usar múltiples vocabularios con trazabilidad sin incorporar una pareja de versión a cada campo.

Asset Schema v1 conserva la pareja como opcional para compatibilidad con fichas técnicas o aún no gobernadas. Todo asset de producción creado desde un preset versionado deberá copiar el ID y versión de su Vocabulary Set; hacer obligatoria esa política para todos los assets existentes queda fuera de este ajuste documental.

El set inicial `nimroel-npc-pilot` 1.0 sólo enlaza los campos para los que ya existen valores inequívocos. `VocabularySetRegistry` resuelve bindings y `ProductionContractValidator` comprueba que cada vocabulario/version exista.

## Revisión de valores piloto

La Biblia Visual NPC confirma inequívocamente `adult` como rango de edad y `neutral` como expresión base; son los únicos datos incluidos actualmente.

No se han promovido `rural_worker` ni `humble`: la Biblia los usa como grupo profesional visual y descriptor de estatus de un pool, no como profesión y clase social canónicas. Tampoco se promueven aún `valemar`, `human` o `female` a los roles exactos de realm/culture, species y gender: la fuente los presenta respectivamente como eje combinado cultura/reino, raza y sexo. `farmer`, `soldier`, `commoner` y `norgard` siguen siendo valores de fixtures técnicos, no canon editorial.

La validación AJV reproducible se ejecuta mediante `scripts/validate-production-contracts-v1.ps1`; no se incorpora ningún motor JSON Schema a la APK.
