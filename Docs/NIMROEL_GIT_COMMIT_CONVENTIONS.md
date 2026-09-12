# NIMROEL — CONVENCIÓN OBLIGATORIA DE COMMITS

**Proyecto:** `Videojuego_Nimroel`  
**Estado:** Norma oficial del repositorio  
**Aplicación:** Obligatoria para todos los commits del proyecto  
**Responsable de control de convención:** ChatGPT, dentro del flujo de trabajo dirigido del proyecto Nimroel

---

## 1. Objetivo

El repositorio `Videojuego_Nimroel` contendrá durante años múltiples sistemas, herramientas y áreas de trabajo que pueden evolucionar de forma independiente.

La convención de commits existe para garantizar:

- historial legible;
- separación clara entre subsistemas;
- trazabilidad;
- búsquedas sencillas;
- depuración histórica;
- reversión de cambios;
- identificación rápida del origen de cada modificación;
- versionado independiente de aplicaciones y herramientas;
- mantenimiento a largo plazo.

No se aceptarán mensajes genéricos como:

```text
cambios
varios cambios
fix
update
cosas nuevas
pruebas
actualización
```

---

## 2. Formato obligatorio

Todos los commits ordinarios seguirán esta estructura:

```text
tipo(ámbito): descripción breve
```

Ejemplos:

```text
feat(asset-manager-android): crear proyecto base con Compose
feat(asset-manager-android): añadir importación de imágenes
fix(asset-manager-android): corregir pérdida de estado al rotar pantalla
feat(asset-schema): definir Asset Schema v1
docs(asset-schema): documentar campos obligatorios
feat(asset-manager-windows): añadir importación batch
fix(asset-manager-windows): corregir detección de duplicados
feat(game): añadir carga inicial de partida
docs(project): actualizar arquitectura general de Nimroel
```

---

## 3. Tipos permitidos

El `tipo` indica la naturaleza principal del cambio.

| Tipo | Uso |
|---|---|
| `feat` | Nueva funcionalidad |
| `fix` | Corrección de un error |
| `refactor` | Reestructuración sin cambio funcional principal |
| `test` | Creación o modificación de tests |
| `docs` | Documentación |
| `chore` | Mantenimiento, configuración o tareas auxiliares |
| `build` | Gradle, dependencias, compilación o sistema de build |
| `ci` | Automatización, pipelines o GitHub Actions |
| `perf` | Mejora de rendimiento |
| `style` | Formato o cambios puramente visuales de código sin cambio funcional |
| `release` | Preparación explícita de una versión |

No se crearán nuevos tipos sin una razón clara.

---

## 4. Ámbitos

El `ámbito` identifica qué subsistema del repositorio modifica el commit.

Ámbitos iniciales oficiales:

```text
asset-manager-android
asset-manager-windows
asset-schema
asset-catalog
asset-prompts
asset-visual-profiles
game
game-save
game-ai
lore
lore-tools
map
docs
project
build
```

La lista podrá ampliarse cuando aparezcan nuevos sistemas reales.

Reglas:

1. El ámbito debe ser estable y reconocible.
2. No crear variantes innecesarias para el mismo sistema.
3. No cambiar de nombre un ámbito sin una decisión explícita.
4. Si un commit afecta principalmente a un único subsistema, debe usar su ámbito.
5. Si afecta a arquitectura general del repositorio, puede utilizar `project`.
6. Si afecta exclusivamente a documentación general, puede utilizar `docs`.
7. Si afecta principalmente al sistema de compilación general, puede utilizar `build`.

---

## 5. Descripción del commit

La descripción debe:

- ser breve;
- ser específica;
- explicar qué cambia;
- comenzar en minúscula;
- evitar información redundante;
- evitar fechas;
- evitar números de versión salvo en commits `release`;
- evitar frases vagas.

Correcto:

```text
feat(asset-manager-android): añadir selección de imagen desde galería
```

Incorrecto:

```text
feat(asset-manager-android): cambios
```

Correcto:

```text
fix(asset-manager-android): conservar lote activo tras reinicio
```

Incorrecto:

```text
fix(asset-manager-android): arreglo bug
```

---

## 6. Fechas

No se incluirá la fecha dentro del mensaje ordinario del commit.

Git ya registra automáticamente:

- fecha;
- hora;
- autor;
- hash;
- posición en el historial.

Por tanto, mensajes como este no deben utilizarse:

```text
feat(asset-manager-android): 12-09-2026 crear pantalla inicial
```

Debe usarse:

```text
feat(asset-manager-android): crear pantalla inicial
```

---

## 7. Versionado

Cada aplicación o subsistema que tenga ciclo de versiones podrá evolucionar de forma independiente.

Se utilizará Semantic Versioning:

```text
MAJOR.MINOR.PATCH
```

Ejemplos:

```text
0.1.0
0.1.1
0.2.0
1.0.0
```

Interpretación general:

- `MAJOR`: cambios incompatibles o grandes hitos de estabilidad.
- `MINOR`: nuevas funcionalidades compatibles.
- `PATCH`: correcciones compatibles.

Durante desarrollo temprano es normal permanecer en `0.x.y`.

---

## 8. Commits de versión

Cuando un componente alcance una versión identificable, se utilizará:

```text
release(ámbito): vMAJOR.MINOR.PATCH
```

Ejemplos:

```text
release(asset-manager-android): v0.1.0
release(asset-manager-windows): v0.1.0
release(game): v0.1.0
```

---

## 9. Git tags

Las versiones importantes deberán acompañarse de un Git tag específico del subsistema.

Formato recomendado:

```text
<ámbito>-vMAJOR.MINOR.PATCH
```

Ejemplos:

```text
asset-manager-android-v0.1.0
asset-manager-windows-v0.1.0
game-v0.1.0
```

Esto permite que distintos componentes del monorepo tengan versiones independientes sin colisiones.

---

## 10. Un commit = una unidad lógica de cambio

Regla fundamental:

> Un commit debe representar una unidad lógica coherente y reversible.

No se deben mezclar cambios no relacionados simplemente porque se realizaron en la misma sesión.

Ejemplo incorrecto:

```text
feat(project): añadir importación de imágenes, modificar lore y arreglar mapa
```

Debe dividirse en commits separados.

Ejemplo:

```text
feat(asset-manager-android): añadir importación de imágenes
docs(lore): actualizar documentación de culturas
fix(map): corregir referencia de región
```

---

## 11. Commits pequeños y trazables

Se prefieren varios commits pequeños y correctamente identificados frente a un único commit gigantesco.

Ventajas:

- permite localizar regresiones;
- facilita revertir cambios;
- facilita comparar versiones;
- mejora `git bisect`;
- mejora revisión;
- permite recuperar cambios concretos;
- mantiene comprensible el historial.

Un commit no debe dividirse artificialmente si sus cambios forman una única unidad funcional inseparable.

---

## 12. Cambios en múltiples carpetas

El repositorio puede contener muchas herramientas independientes.

No se utilizará la carpeta física como única referencia para nombrar el commit: se utilizará el subsistema lógico.

Por ejemplo, cambios dentro de:

```text
Tools/NimroelAssetManager/...
```

relacionados con la aplicación Android usarán:

```text
asset-manager-android
```

Los contratos comunes del Asset Manager podrán utilizar ámbitos como:

```text
asset-schema
asset-catalog
asset-prompts
asset-visual-profiles
```

Esto permite filtrar el historial por función real y no únicamente por ruta.

---

## 13. Codex

Codex deberá respetar esta convención en todas las intervenciones del proyecto.

Cuando Codex no tenga autorización para crear commits automáticamente, al terminar deberá proponer el mensaje exacto que corresponde según esta norma.

No deberá proponer mensajes libres o genéricos.

Ejemplo esperado:

```text
feat(asset-manager-android): crear estructura inicial de la aplicación
```

No:

```text
Initial Android project
```

Si una intervención contiene varias unidades lógicas suficientemente independientes, Codex deberá proponer varios commits separados y especificar qué archivos corresponde incluir en cada uno.

---

## 14. Control antes del commit

Antes de consolidar un commit se comprobará:

1. qué archivos han cambiado;
2. a qué subsistema pertenecen;
3. si todos forman una única unidad lógica;
4. qué `tipo` corresponde;
5. qué `ámbito` corresponde;
6. que la descripción sea clara;
7. que no se mezclen cambios ajenos;
8. que build/tests relevantes estén en estado conocido;
9. que no se incluyan secretos, archivos temporales o artefactos locales;
10. que el mensaje final cumpla exactamente esta convención.

---

## 15. Responsabilidad de control

Dentro del flujo dirigido del proyecto Nimroel, ChatGPT será responsable de revisar la nomenclatura propuesta antes de cada commit cuando el usuario le presente el resultado de Codex o solicite el siguiente paso.

ChatGPT deberá:

- detectar mensajes incorrectos;
- corregirlos;
- decidir el tipo;
- decidir el ámbito;
- decidir si corresponde uno o varios commits;
- proporcionar al usuario el mensaje exacto cuando el commit se haga manualmente;
- indicar a Codex la convención obligatoria cuando Codex vaya a gestionar el commit;
- vigilar que las versiones y tags respeten esta norma.

El usuario podrá realizar materialmente el commit y el push mediante GitHub Desktop, pero la convención deberá mantenerse de forma consistente.

---

## 16. Ejemplos oficiales

### Asset Manager Android

```text
feat(asset-manager-android): crear estructura inicial de la aplicación
build(asset-manager-android): configurar Gradle y dependencias base
feat(asset-manager-android): añadir previsualización de imágenes
feat(asset-manager-android): añadir sesiones de producción
fix(asset-manager-android): recuperar operaciones pendientes tras reinicio
test(asset-manager-android): cubrir generación de assetId
refactor(asset-manager-android): separar procesamiento de imágenes de la UI
release(asset-manager-android): v0.1.0
```

### Contratos de assets

```text
feat(asset-schema): definir Asset Schema v1
docs(asset-schema): documentar campos opcionales y obligatorios
feat(asset-catalog): añadir formato inicial de manifest
feat(asset-prompts): añadir plantilla maestra para retratos NPC
feat(asset-visual-profiles): añadir perfil visual de Valemar
```

### Videojuego

```text
feat(game): crear sistema inicial de nueva partida
feat(game-save): persistir assetId de NPC
feat(game-ai): añadir contrato del AI Budget Manager
fix(game-save): corregir restauración de personaje persistente
```

### Proyecto general

```text
docs(project): documentar arquitectura del ecosistema de assets
chore(project): reorganizar archivos técnicos del repositorio
build(project): actualizar configuración global de compilación
```

---

## 17. Regla final

El historial Git de Nimroel debe poder entenderse dentro de varios años sin conocer de memoria qué ocurrió en cada sesión de desarrollo.

Por tanto:

> Ningún commit del proyecto debe considerarse un simple punto de guardado.

Cada commit debe ser una pieza identificable, coherente y útil de la historia técnica de Nimroel.
