# Nimroel Core — regresión de migración BUILD / DOOR v0.1

## Estado

**REGRESIÓN OBLIGATORIA PARA EL LOTE D2**

## Casos

### CORE-MIG-D2-001 — stable IDs BUILD
BUILD01–BUILD10 conservan identificador y significado.

### CORE-MIG-D2-002 — construcción causal
Ningún edificio aparece sin emplazamiento, materiales, trabajo, tiempo, acceso y razón compatible.

### CORE-MIG-D2-003 — persistencia
Seeds y LOD no sustituyen ni rerrollean construcción ya materializada.

### CORE-MIG-D2-004 — canon y partida
Cambios construidos en una partida no reescriben automáticamente el canon global.

### CORE-MIG-D2-005 — protección local
Core define la regla de protección; Treskal conserva qué namespaces/instalaciones concretas están protegidas.

### CORE-MIG-D2-006 — stable IDs DOOR
DOOR01–DOOR07 conservan identificador y significado.

### CORE-MIG-D2-007 — acceso y permiso
Poder atravesar físicamente un acceso no equivale a tener permiso, y tener permiso no abre físicamente una puerta.

### CORE-MIG-D2-008 — llaves
Poseer una llave no transfiere propiedad ni autorización.

### CORE-MIG-D2-009 — validación del motor
IA, diálogo o interfaz no pueden abrir accesos ni conceder permisos inexistentes.

### CORE-MIG-D2-010 — acceso local
Treskal conserva como override únicamente la referencia a su sistema local de clases P.

### CORE-MIG-D2-011 — compatibilidad
Stable IDs y World State conservan significado; no se requiere migración de saves.

### CORE-MIG-D2-012 — autoridad única
Core es autoridad normativa de BUILD y DOOR; Treskal sólo conserva overrides locales explícitos.

## Resultado esperado

**MIGRATION_BATCH_D2_COMPATIBLE**
