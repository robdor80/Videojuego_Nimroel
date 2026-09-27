# Convención de nombres y empaquetado de assets visuales — Nimroel

## Objetivo

A partir de este momento, todos los assets visuales creados para Nimroel deben seguir una convención estable de:

- nombre de archivo
- nombre del ZIP
- estructura interna del ZIP
- metadatos mínimos
- criterios de búsqueda y organización

El objetivo es evitar caos futuro, facilitar búsquedas, permitir automatización posterior y preparar el material para su futura integración en el videojuego.

---

## 1. Principio general

Cada asset debe tener un **nombre base único y estable**.

Ese mismo nombre base debe usarse en:

- el archivo `.zip` (si se utiliza)
- el archivo de imagen (en retratos: PNG maestro externo y WebP de producción)
- el archivo `.md` del prompt
- el archivo `.md` de información

Ejemplo:

```text
portrait_treskal_farmer_male_001
```

Se utilizará así:

```text
portrait_treskal_farmer_male_001.zip
portrait_treskal_farmer_male_001.webp
portrait_treskal_farmer_male_001_prompt.md
portrait_treskal_farmer_male_001_info.md
```

---

## 2. Regla principal de nomenclatura

La estructura general del nombre será:

```text
<asset_type>_<culture-or-place>_<subject>_<sex-or-variant>_<number>
```

---

## 3. Tipos de asset

### 3.1. Retratos

Para retratos adultos, la forma normal es:

```text
portrait_<culture-or-origin>_<role>_<sex>_<NNN>
```

Ejemplos:

```text
portrait_treskal_farmer_male_001
portrait_treskal_farmer_female_001
portrait_treskal_blacksmith_male_001
portrait_morgar_noble_female_001
```

#### 3.1.1. Excepción válida para menores

En menores se permiten los identificadores semánticos `boy` / `girl` cuando formen parte del rol o de la etapa vital.

Son válidas estas formas:

```text
portrait_<culture-or-origin>_<boy|girl>_<NNN>
portrait_<culture-or-origin>_<role>_<boy|girl>_<NNN>
```

Ejemplos canónicos ya aprobados:

```text
portrait_treskal_boy_001
portrait_treskal_girl_001
portrait_treskal_girl_002
portrait_treskal_girl_003
portrait_treskal_farmer_boy_001
portrait_treskal_farmer_boy_002
```

Estos IDs son estables y **no deben migrarse** a `male` / `female`.

En todos los retratos, el `asset_id`, la carpeta definitiva, el WebP de producción, `_prompt.md` y `_info.md` deben compartir exactamente el mismo nombre base. El PNG maestro externo conserva ese mismo nombre base.

Se mantienen las reglas de minúsculas, ASCII, underscores y numeración final de tres dígitos.

### 3.2. Escenas

Para escenas:

```text
scene_<place-or-culture>_<subject>_<variant-or-context>_<NNN>
```

Ejemplos:

```text
scene_treskal_farmland_harvest_001
scene_treskal_village_market_001
scene_morgar_coast_storm_001
scene_norgar_mountain_pass_winter_001
```

---

## 4. Reglas obligatorias de escritura

Todos los nombres deben cumplir estas normas:

- usar **minúsculas**
- usar sólo **ASCII**
- **sin espacios**
- **sin tildes**
- usar **underscore `_`** como separador
- numeración final con **3 dígitos**: `001`, `002`, `003`...

Correcto:

```text
portrait_treskal_farmer_male_001.webp
```

Incorrecto:

```text
Retrato Treskal Campesino Hombre FINAL.png
portrait-treskal-farmer-male-1.png
portrait_treskal_farmer_male_final.png
```

---

## 5. Numeración

La numeración final identifica **variantes diferentes del asset**, no revisiones accidentales.

Correcto:

```text
portrait_treskal_farmer_male_001
portrait_treskal_farmer_male_002
portrait_treskal_farmer_male_003
```

No usar:

```text
portrait_treskal_farmer_male_final
portrait_treskal_farmer_male_final2
portrait_treskal_farmer_male_bueno
portrait_treskal_farmer_male_definitivo
```

Si existe una nueva variante real, se crea un nuevo número.

---

## 6. ZIP y contenido interno

El ZIP de transferencia, cuando se utilice, debe compartir el nombre base. En retratos puede contener el PNG maestro original y su documentación; ese PNG se archiva externamente en TeraBox.

Estructura de transferencia con PNG maestro:

```text
<base_name>.zip
│
├── <base_name>.png
├── <base_name>_prompt.md
└── <base_name>_info.md
```

Ejemplo:

```text
portrait_treskal_farmer_male_001.zip
│
├── portrait_treskal_farmer_male_001.png
├── portrait_treskal_farmer_male_001_prompt.md
└── portrait_treskal_farmer_male_001_info.md
```

---

## 6.1. Almacenamiento definitivo en GitHub

Si se utiliza, el ZIP es el **paquete de transferencia** utilizado para entregar el asset al usuario.

Para retratos, el PNG maestro se convierte antes de subirlo a WebP 768x960, relación 4:5, Q90. El almacenamiento definitivo en GitHub es una carpeta con el mismo nombre base:

```text
portrait_treskal_farmer_female_003/
├── portrait_treskal_farmer_female_003.webp
├── portrait_treskal_farmer_female_003_prompt.md
└── portrait_treskal_farmer_female_003_info.md
```

Flujo operativo:

1. Se aprueba el PNG maestro y se le asigna el nombre base canónico.
2. El PNG maestro se conserva externamente en TeraBox; si se entrega en un ZIP, se extrae para preparar la producción.
3. Se convierte el maestro a WebP 768x960, relación 4:5, Q90.
4. En la carpeta `<base_name>/` se colocan el WebP, `_prompt.md` y `_info.md`.
5. El ZIP de transferencia se elimina del almacenamiento definitivo.
6. GitSync sincroniza la carpeta de producción con GitHub.

Por tanto, **GitHub no conserva el ZIP ni el PNG maestro como almacenamiento definitivo del retrato**. El nombre base no cambia: solo cambia el formato del binario de producción.

---

## 7. Organización en carpetas

Las carpetas sirven para ayudar a navegar, pero **el nombre del archivo debe ser autosuficiente**.

Ejemplo de almacenamiento definitivo:

```text
Assets/
└── portraits/
    └── Norgard/
        └── Treskal/
            └── <role>/
                └── <sex-or-life-stage>/
                    └── <asset_id>/
                        ├── <asset_id>.webp
                        ├── <asset_id>_prompt.md
                        └── <asset_id>_info.md
```

Ejemplo real:

```text
Assets/
└── portraits/
    └── Norgard/
        └── Treskal/
            └── farmer/
                └── male/
                    └── portrait_treskal_farmer_male_001/
                        ├── portrait_treskal_farmer_male_001.webp
                        ├── portrait_treskal_farmer_male_001_prompt.md
                        └── portrait_treskal_farmer_male_001_info.md
```

El ZIP aparece **únicamente como paquete temporal de transferencia** y nunca como contenido definitivo del repositorio.

La carpeta ayuda, pero la identidad principal sigue estando en el nombre base.

---

## 8. Qué NO debe ir en el nombre

El nombre debe ser útil, corto y estable.

No deben meterse detalles demasiado específicos o variables visuales menores, por ejemplo:

- color exacto de ropa
- suciedad
- expresión facial concreta
- detalles de iluminación
- notas de calidad
- estados como `final`, `ok`, `bueno`, etc.

Evitar:

```text
portrait_treskal_farmer_male_dirty_white_shirt_middle_aged_brown_hair_001
```

Esas características pertenecen a los metadatos.

---

## 9. Contenido recomendado de `_info.md`

El archivo `<base_name>_info.md` debe guardar la información descriptiva del asset.

Campos recomendados:

```text
Asset ID provisional
Tipo
Cultura / procedencia
Lugar asociado
Rol / profesión / categoría
Sexo
Variante
Estado
Fecha de creación
Resolución
Formato
Uso previsto
Notas visuales
Relación con lore
Observaciones
```

---

## 10. Contenido recomendado de `_prompt.md`

El archivo `<base_name>_prompt.md` debe guardar el prompt realmente usado para generar el asset.

Formato recomendado:

```md
# Prompt

## Base name
portrait_treskal_farmer_male_001

## Prompt usado
[Aquí el prompt completo]

## Notas
[Opcional: ajustes, correcciones o contexto]
```

---

## 11. Compatibilidad futura con el videojuego

El **nombre físico del WebP de producción no será necesariamente la identidad lógica definitiva dentro del juego**.

Más adelante podrá existir un sistema de IDs lógicos estables, por ejemplo:

```text
nimroel.assets:portraits/treskal/farmer/male/001
```

que apunte al archivo físico:

```text
portrait_treskal_farmer_male_001.webp
```

Principio importante:

```text
DefinitionId != filesystem path
```

y, de forma equivalente:

```text
AssetId != WebP filename
```

Por tanto:

- el nombre actual debe ser ordenado, estable y útil;
- no debe confundirse con una identidad lógica definitiva del motor.

---

## 12. Convención oficial aprobada

### Retratos

Adultos, forma normal:

```text
portrait_<culture-or-origin>_<role>_<sex>_<NNN>
```

Menores, cuando corresponda:

```text
portrait_<culture-or-origin>_<boy|girl>_<NNN>
portrait_<culture-or-origin>_<role>_<boy|girl>_<NNN>
```

### Escenas

```text
scene_<place-or-culture>_<subject>_<variant-or-context>_<NNN>
```

Ejemplos válidos:

```text
portrait_treskal_farmer_male_001
portrait_treskal_farmer_female_001
portrait_treskal_blacksmith_male_001
portrait_morgar_noble_female_001

scene_treskal_farmland_harvest_001
scene_treskal_village_market_001
scene_morgar_coast_storm_001
scene_norgar_mountain_pass_winter_001
```

---

## 13. Regla operativa definitiva

A partir de ahora, **todo asset nuevo debe seguir esta convención**:

1. se asigna un **nombre base canónico**;
2. si se utiliza un `.zip` de transferencia, usa ese nombre;
3. la carpeta definitiva del repositorio usa ese nombre;
4. el PNG maestro externo de un retrato conserva ese nombre;
5. el WebP de producción de un retrato usa ese nombre;
6. el `_prompt.md` usa ese nombre;
7. el `_info.md` usa ese nombre.

No deben crearse assets nuevos fuera de esta norma salvo decisión expresa posterior.

---

## 14. Conclusión

Esta convención queda fijada como estándar de trabajo para los assets visuales de Nimroel.

Su objetivo es:

- facilitar búsqueda;
- facilitar clasificación;
- evitar caos futuro;
- permitir automatización;
- preparar integración posterior en el videojuego.

Queda aprobada como convención vigente hasta nueva revisión explícita.