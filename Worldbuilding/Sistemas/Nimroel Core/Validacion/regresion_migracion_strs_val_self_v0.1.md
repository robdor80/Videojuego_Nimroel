# Nimroel Core — regresión de migración STRS / VAL / SELF v0.1

## Estado

**REGRESIÓN OBLIGATORIA PARA EL LOTE A4**

## Casos

### CORE-MIG-A4-001 — stable IDs STRS
STRS01–STRS07 conservan identificador y significado.

### CORE-MIG-A4-002 — presión sigue siendo causal
Migrar STRS no crea carga o recuperación sin causas reales.

### CORE-MIG-A4-003 — STRS mantiene separación de sistemas
Presión, emoción, descanso y salud siguen siendo autoridades distintas.

### CORE-MIG-A4-004 — stable IDs VAL
VAL01–VAL08 conservan identificador y significado.

### CORE-MIG-A4-005 — valores sin alineamiento universal
VAL no crea ejes morales globales ni nuevos valores culturales.

### CORE-MIG-A4-006 — conflicto no borra compromiso
Actuar contra un valor no lo elimina automáticamente.

### CORE-MIG-A4-007 — stable IDs SELF
SELF01–SELF08 conservan identificador y significado.

### CORE-MIG-A4-008 — identidad no crea rol material
SELF no crea empleo, parentesco, relación, autoridad ni permiso.

### CORE-MIG-A4-009 — continuidad identitaria
Perder un rol activo no borra memoria ni identidad de legado.

### CORE-MIG-A4-010 — overrides de Treskal vacíos
STRS, VAL y SELF locales figuran como `migrated_to_core_override` con `localOverrides = {}`.

### CORE-MIG-A4-011 — documentación derivada
Las capas 86, 89 y 90 declaran al Core como autoridad normativa.

### CORE-MIG-A4-012 — autoridad única
Core es la única fuente normativa de STRS, VAL y SELF.

## Resultado esperado

**MIGRATION_BATCH_A4_COMPATIBLE**
