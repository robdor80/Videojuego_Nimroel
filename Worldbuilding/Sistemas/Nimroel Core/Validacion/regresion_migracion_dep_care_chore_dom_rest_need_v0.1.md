# Nimroel Core — regresión de migración DEP / CARE / CHORE / DOM / REST / NEED v0.1

## Estado

**REGRESIÓN OBLIGATORIA PARA EL LOTE B2**

## Casos

### CORE-MIG-B2-001 — stable IDs DEP / CARE
DEP01–DEP05 y CARE01–CARE07 conservan identificador y significado.

### CORE-MIG-B2-002 — dependencia no equivale a edad
Edad avanzada no crea DEP automáticamente; el desarrollo infantil tampoco convierte al niño en adulto funcional.

### CORE-MIG-B2-003 — cuidado consume capacidad real
CARE exige actores, tiempo, presencia, capacidad y recursos reales.

### CORE-MIG-B2-004 — particularidad local de cuidado
La ausencia por defecto de guardería moderna o cuidado residencial institucional en Treskal permanece en `localOverrides` y no se convierte en regla Core.

### CORE-MIG-B2-005 — stable IDs CHORE / DOM
CHORE01–CHORE09 y DOM01–DOM07 conservan identificador y significado.

### CORE-MIG-B2-006 — tareas con causalidad material
Agua, combustible, comida, lavado, residuos, cuidados, recados y mantenimiento continúan dependiendo de los sistemas propietarios.

### CORE-MIG-B2-007 — asignación no hardcodeada por sexo
CHORE mantiene asignación contextual sin imponer reparto universal por sexo.

### CORE-MIG-B2-008 — backlog persistente
DOM no borra retrasos o sobrecarga al cambiar de LOD, guardar o cargar.

### CORE-MIG-B2-009 — stable IDs REST
REST01–REST07 conservan identificador y significado.

### CORE-MIG-B2-010 — disponibilidad no 24/7
Migrar REST no convierte a NPC, comercios o servicios en permanentemente disponibles.

### CORE-MIG-B2-011 — interrupción y emergencia causales
Despertar o interrumpir sueño requiere percepción, mensaje, proximidad u otra causa válida.

### CORE-MIG-B2-012 — stable IDs NEED
NEED01–NEED05 conservan identificador y significado.

### CORE-MIG-B2-013 — necesidad no crea recurso
NEED no genera comida, bebida, calor, saneamiento o descanso sin los sistemas y recursos correspondientes.

### CORE-MIG-B2-014 — agregación LOD segura
Necesidades ordinarias pueden agregarse sólo cuando la rutina es plausible; una necesidad relevante sin resolver persiste.

### CORE-MIG-B2-015 — overrides de Treskal
CHORE/DOM, REST y NEED figuran como `migrated_to_core_override` con `localOverrides = {}`; DEP/CARE conserva sólo su particularidad institucional local.

### CORE-MIG-B2-016 — documentación derivada
Las capas 59, 65, 67 y 94 declaran al Core como autoridad normativa.

### CORE-MIG-B2-017 — compatibilidad de saves
Stable IDs y significado del World State se conservan; no se requiere migración de saves.

### CORE-MIG-B2-018 — autoridad única
Core es la única fuente normativa universal de DEP/CARE, CHORE/DOM, REST y NEED.

## Resultado esperado

**MIGRATION_BATCH_B2_COMPATIBLE**
