# NIM-08 P04 — Resultado y ejecución reproducible

Fecha: 12-11-2026. Estado: **entrega de arquitectura + contratos + CI estática superada**. No existe una aldea funcional nueva en NIM-08.

## Commits y base de referencia

- Nimroel main examinada: 0130ed95f27d6d450c962fa2557f56b6b569e4a0.
- CoreRPG main observado: 76a7b7b485616d8c4994f384a90f123bf333591d (solo lectura).
- CoreRPG realmente fijado: 4f282863737bcd8f5add401202a9e1064c133672.
- Plan de NIM-08–19 heredado: 40f2df20d72e92810379ed21f04b1ec609df9f4e.
- P01/P02: 808649422588d18948bd18539ba10f8fc6992d10 (auditoría, decisiones y escenarios).
- P03: fdea1c260a8b66e3a59986013eff62a1669b6357 (tres esquemas + manifiesto ejemplo).
- P04: c168269c8f62ecee3ec5008899bb87f6abdae85f (validador, 18 tests, CI).
- PR Draft: https://github.com/robdor80/Videojuego_Nimroel/pull/50. Los commits posteriores de informe/cierre se revisan en esta misma PR; jamás se deduce un SHA de documentación aún no confirmado.

## Evidencia obtenida

Workflow **NIM-08 contractual static validation**, run https://github.com/robdor80/Videojuego_Nimroel/actions/runs/43217324339 sobre c168269c8f62ecee3ec5008899bb87f6abdae85f:

| Entorno | Job ID | Validación contractual | Unit tests | Conclusión |
| --- | --- | --- | --- | --- |
| Ubuntu latest / Python 3.12 | 131179765902 | PASS_STATIC_ONLY, 28/28, 3 schemas, provenance | Ran 18 tests — OK | SUCCESS |
| Windows latest / Python 3.12 | 131179766385 | PASS_STATIC_ONLY, 28/28, 3 schemas, provenance | Ran 18 tests — OK | SUCCESS |

Logs examinados directamente. El resultado también contiene physical_pass=0 y v001_behavioural_pass=0 **por diseño**. Un test documental no valida una mecánica, ni acredita Windows EXE, Android APK, ni física Samsung Tab S9+.

Casos ejercitados: conservación de 6 G + 4 P + 8 Q + 6 S + 4 H y estados PENDIENTE; estructura y referencias de JSON Schema; manifiesto técnico válido; source-lock SHA Git Blob/revisión, pack ID/versión/release hash y pin Core verificados; negativos de clave desconocida, fuente omitida, seeds inválidas, SHA corrupto, versión inesperada, subsistema ausente o duplicado, fase operativa ficticia, hash de release erróneo, plataforma inválida y acciones no admitidas; campos de resultado inválidos.

## Cómo repetir sin red ni Codex (una vez descargada rama)

Desde la raíz del checkout del commit auditado:

    python Tools/NIM08/check_contracts.py --json
    python -m unittest discover -s Tools/NIM08 -p 'test_*.py' -v

Solo Python 3.12 estándar. Para recuperar mismo resultado, conservar bytes de Worldbuilding, ContentPacks y CMake pins, además de los propios esquemas/ejemplo del commit. Los cambios a cualquiera de estas entradas deben generar revisión y nueva evidencia, no corregirse silenciosamente.

## Qué se creó y qué NO se creó

Se añadieron documentos dentro de Docs/NIM-08-19/NIM-08/, tres contratos JSON Schema Draft 2020-12 de **diseño**, manifiesto ilustrativo, validador y pruebas Tools/NIM08 y workflow .github/workflows/nim08-contracts.yml. La documentación original de planificación no se duplica.

**No** se ha alterado Game/, CoreRPG, Worldbuilding, ContentPacks, el contrato Content Pack Core 0.1.0, las versiones de Godot/CPP, ni Star Trek. No hay nuevo scheduler, WorldState, AI endpoint, GDExtension ejecutable, tool repair o guardado integral de aldea.

## Incidencias y mitigación

- Diferencia Core main/pin: documentada; no se usó la API más nueva como si ya estuviera disponible en Nimroel.
- Confusión contención/propiedad/posición: contratos los separan y declaran dependencias nativas futuras.
- Certificación Android I4 ausente en evidencia: no se ha marcado PASS; la prueba se mantiene pendiente.
- Referencia histórica a Terra frente a política IA vigente: se conserva la política Sol/Luna con consentimiento, con modo local obligatorio.
- El validador incluido soporta solo los keywords JSON Schema utilizados aquí: NIM-09 debe emplear un validador integral para packs de producción.
- Errores de CI en run documentada: **ninguno**. Sin correcciones improvisadas ni regresiones funcionales ejecutadas.

## PDF maestro de proyecto

Archivo fuente externo al repositorio consultado: NIMROEL RPG — PROYECTO MAESTRO.pdf, SHA-256 127d5707d0fdf7c285c155dc0714bee7788a16ee5fab701c8f2f7d54f4fa625a. Se registra la huella para identificación, **no se considera incorporado a Git**; ante cambios, deberá fijarse una fuente accesible al proceso de autoría y validarse su aprobación.

**Cierre técnico de NIM-08:** contratos/auditoría/plan de ejecución listos; pendiente autorización del propietario para fusionar PR, y nunca equivale a NIM-09–19 implementadas.
