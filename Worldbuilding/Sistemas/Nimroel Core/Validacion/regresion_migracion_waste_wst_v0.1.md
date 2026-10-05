# Nimroel Core — regresión de migración WASTE / WST v0.1

## Estado

**REGRESIÓN OBLIGATORIA PARA EL LOTE D3**

## Casos

### CORE-MIG-D3-001 — stable IDs
WASTE01–WASTE08 y WST01–WST07 conservan identificador y significado.

### CORE-MIG-D3-002 — residuos causales
Generar, contener, recoger, transportar y eliminar residuos requiere cambios reales de World State.

### CORE-MIG-D3-003 — retirada material
La retirada exige actor, manipulación o recipiente, ruta y destino.

### CORE-MIG-D3-004 — persistencia
LOD, lluvia y save/load no borran acumulaciones problemáticas.

### CORE-MIG-D3-005 — salud separada
La suciedad puede generar presión sanitaria, pero no enfermedad automática sin sistema de salud.

### CORE-MIG-D3-006 — tecnología no universalizada
Core no fija alcantarillado, letrinas, pozos negros ni organización municipal universal.

### CORE-MIG-D3-007 — override Treskal
Treskal conserva explícitamente su ausencia de alcantarillado moderno, uso posible de letrinas/pozos negros y ausencia de departamento municipal moderno.

### CORE-MIG-D3-008 — compatibilidad
Stable IDs y significado del World State se conservan; no se requiere migración de saves.

### CORE-MIG-D3-009 — autoridad única
Core es autoridad de WASTE/WST; Treskal sólo aporta tecnología y organización local.

## Resultado esperado

**MIGRATION_BATCH_D3_COMPATIBLE**
