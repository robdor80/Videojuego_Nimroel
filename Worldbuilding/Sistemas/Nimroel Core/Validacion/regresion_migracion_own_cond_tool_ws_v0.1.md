# Nimroel Core — regresión de migración OWN / COND / TOOL / WS v0.1

## Estado

**REGRESIÓN OBLIGATORIA PARA EL LOTE D1**

## Casos

### CORE-MIG-D1-001 — stable IDs OWN
OWN01–OWN07 conservan identificador y significado.

### CORE-MIG-D1-002 — posesión no equivale a propiedad
Recoger, transportar o custodiar un objeto no cambia owner_ref sin transferencia válida.

### CORE-MIG-D1-003 — persistencia material
Un objeto promocionado a persistente no se rerrollea al materializar de nuevo.

### CORE-MIG-D1-004 — propiedad y ley separadas
Core conserva relaciones materiales; derecho exacto de propiedad, herencia o confiscación queda fuera.

### CORE-MIG-D1-005 — stable IDs COND
COND01–COND07 conservan identificador y significado.

### CORE-MIG-D1-006 — desgaste causal
No existe deterioro arbitrario sin uso, ambiente, daño, accidente, negligencia u otra causa válida.

### CORE-MIG-D1-007 — reparación material
Reparar requiere materiales, trabajo, tiempo y acceso; LOD no crea progreso sin inputs.

### CORE-MIG-D1-008 — estado visual
Apariencia, accesibilidad y sonidos deben ser compatibles con el estado material real.

### CORE-MIG-D1-009 — stable IDs TOOL/WS
TOOL01–TOOL07 y WS01–WS05 conservan identificador y significado.

### CORE-MIG-D1-010 — equipo físico
Habilidad no reemplaza una herramienta crítica ausente y una herramienta excelente no reemplaza habilidad.

### CORE-MIG-D1-011 — capacidad productiva
La capacidad deriva de trabajadores, equipo, estaciones, materiales, tiempo y estado operativo.

### CORE-MIG-D1-012 — propiedad de herramientas
Usar, prestar o autorizar por rol no transfiere automáticamente la propiedad.

### CORE-MIG-D1-013 — contratos locales
OWN, COND, TOOL y WS quedan como `migrated_to_core_override` con `localOverrides = {}`.

### CORE-MIG-D1-014 — documentación derivada
Las capas 42, 43 y 57 declaran al Core como autoridad normativa.

### CORE-MIG-D1-015 — compatibilidad
Stable IDs y significado del World State se conservan; no se requiere migración de saves.

### CORE-MIG-D1-016 — autoridad única
Core es la única fuente normativa de OWN, COND, TOOL y WS.

## Resultado esperado

**MIGRATION_BATCH_D1_COMPATIBLE**
