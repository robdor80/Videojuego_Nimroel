# Darovan D01–D03 — Reproducción Python aislada, 15-10-2026

> **ACTUALIZACIÓN POSTERIOR:** la repetición pendiente sobre **checkout real de MSI ya se ejecutó y pasó el 15-10-2026**. Véase `D03_VALIDACION_MSI_CHECKOUT_2026-10-15.md`. Los estados PENDIENTE que aparecen más abajo documentan la situación histórica anterior a esa ejecución y ya no son vigentes para la suite Python.

**Ámbito:** ejecución real de validadores estáticos originales recuperados desde la rama `feat/darovan-d03-clima-ecosistemas`, dentro de un entorno Python aislado sin acceso de red. Esta acta complementa las auditorías D01–D03. **No es un checkout íntegro ni prueba runtime.**

## Integridad del código ejecutado

Se recuperaron los tres archivos `Validacion/validate_d01.py`, `validate_d02.py` y `validate_d03.py` mediante el conector GitHub, se reprodujeron como archivos ejecutables UTF-8 y se calculó `git hash-object` localmente. Los hashes coinciden **exactamente** con los blobs de GitHub:

| Script | SHA Git local = SHA GitHub |
|---|---|
| `validate_d01.py` | `732a884d16cb96bdb2c00623f88a06b09b4d3ef2` |
| `validate_d02.py` | `8b6d616e331188d3b7bf5d241edc1c7931e53418` |
| `validate_d03.py` | `06b777a25121607ad31f87b37a707cbb34115e57` |

## Datos y reconstrucción controlada

El acceso a GitHub se hizo **mediante el conector**, no desde Python. Se verificaron los archivos JSON originales de D01, D02, D03 y Nimroel Core en la rama. Por no disponer de un checkout descargable desde Python:
- **D03:** se reconstruyó el objeto JSON publicado, conservando todos sus campos. Comparación de serializaciones canónicas ordenadas: ambas con **10.768 caracteres** y firma FNV-1a de 64 bits **`1172922043d07674`**. Igualdad semántica de D03 comprobada. Blob GitHub `1a5827fde41e750b4726085aa8baaebf62ebcd17`.
- **D01:** se reprodujeron exclusivamente los campos consumidos por su validador con valores obtenidos del JSON original (blob `3a2e2fa903754be225742ab5a5a51393f188fe62`). No se reconstruyó el resto del JSON D01.
- **D02:** se reprodujeron exclusivamente los campos consumidos por su validador (incluidos grafo, fuentes, ciudades, cauces y cuencas) con valores obtenidos del JSON original (blob `367001edee154abce11a4a6c109846d331d746d5`). No se reconstruyó el resto del JSON D02.
- **Core:** se reprodujeron los campos consultados por estos scripts; `status=active_core_contract` se confirmó contra el archivo original (blob `126de944733641eeb582ec6bc028ad0893e467ec`).
- Los documentos y rutas de referencia se **consultaron y confirmaron en GitHub**; cuando el Python verificaba solamente `Path.is_file()`, se creó un archivo de presencia local en la misma ruta. No se presenta ese archivo de presencia como copia del contenido original.

## Ejecuciones obtenidas (salidas literales)

```text
D01 STATIC OK: 12 unidades, 4 ciudades, 12 fuentes, sin runtime
D02 STATIC OK: 4 ríos, 3 redes, 13 nodos, 10 aristas, 8 pruebas negativas; NO runtime
D03 STATIC OK: 12 qualitative units, 13 references, 10 negative tests; NOT RUNTIME
```

Se ejecutó Python con código original, no una reimplementación de las reglas. En D02 se superaron ocho mutaciones negativas y en D03 diez. Los datos empleados fueron una reconstrucción local semántica contrastada, **no una descarga byte a byte de la totalidad del repositorio**. Se mantienen anteriores comprobaciones JavaScript sobre los JSON efectivos publicados.

## Estado y pendientes

- **SUPERADO:** ejecución Python aislada de D01, D02, D03 con proyecciones de sus datos efectivamente consultados y cotejados; integridad exacta de scripts; igualdad semántica completa de JSON D03; pruebas negativas D02/D03.
- **PENDIENTE — CHECKOUT ÍNTEGRO:** repetir los tres scripts en el repositorio real descargado, con todos los archivos fuente originales. Esto certificará la prueba integral de filesystem y evitará depender de archivos de presencia. No se puede certificar todavía CI/GitHub Actions.
- **PENDIENTE — GODOT y GIS:** tests reales del motor, medidas espaciales y simulación hidrológica/climática, fuera del alcance de la validación documental.
- **Control de rama:** esta evidencia se incorpora únicamente en la PR #17, sin fusionarla y sin iniciar D04.

**Conclusión:** se han eliminado como pendientes las **ejecuciones Python aisladas** de D01–D03; no se han eliminado las **ejecuciones en checkout íntegro** ni pruebas de juego. No confundir ambas evidencias.
