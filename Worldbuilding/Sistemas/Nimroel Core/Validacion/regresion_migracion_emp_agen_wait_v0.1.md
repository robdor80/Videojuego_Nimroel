# Nimroel Core — regresión de migración EMP / AGEN / WAIT v0.1

## Estado

**REGRESIÓN OBLIGATORIA PARA EL LOTE C1**

## Casos

### CORE-MIG-C1-001 — stable IDs EMP
EMP01–EMP08 conservan identificador y significado.

### CORE-MIG-C1-002 — profesión y puesto separados
Cambiar o perder un puesto no borra oficio, experiencia, relaciones ni reputación.

### CORE-MIG-C1-003 — vacante causal
Una vacante no materializa ni contrata automáticamente a un NPC.

### CORE-MIG-C1-004 — sustitución compatible
Un sustituto sólo cubre tareas compatibles con su capacidad real.

### CORE-MIG-C1-005 — ausencia persistente
EMP03/EMP04 afectan capacidad y disponibilidad sin teletransportar al actor.

### CORE-MIG-C1-006 — contratación offscreen
Cubrir un puesto fuera de cámara exige candidato plausible y tiempo transcurrido.

### CORE-MIG-C1-007 — stable IDs AGEN
AGEN01–AGEN09 conservan identificador y significado.

### CORE-MIG-C1-008 — tiempo no duplicable
Un NPC no ejecuta actividades incompatibles simultáneamente.

### CORE-MIG-C1-009 — agenda no usurpa autoridad
AGEN coordina sistemas fuente sin reescribir sus estados propios.

### CORE-MIG-C1-010 — viaje y tiempo
Una agenda no permite presencia consecutiva incompatible sin ruta y duración válidas.

### CORE-MIG-C1-011 — retraso y reprogramación causales
AGEN05 requiere causa; AGEN06 requiere nueva ventana plausible y acuerdo/disponibilidad cuando afecta a terceros.

### CORE-MIG-C1-012 — stable IDs WAIT
WAIT01–WAIT08 conservan identificador y significado.

### CORE-MIG-C1-013 — capacidad efectiva
La atención depende de actores presentes, capacidad, estaciones, recursos, espacio y estado operativo; no de plantilla teórica.

### CORE-MIG-C1-014 — jugador sin prioridad metafísica
Abrir diálogo o interfaz no cancela esperas, otros clientes ni ocupación del proveedor.

### CORE-MIG-C1-015 — persistencia de solicitudes
Las solicitudes relevantes sobreviven LOD y save/load.

### CORE-MIG-C1-016 — contratos locales
EMP, AGEN y WAIT quedan como `migrated_to_core_override` con `localOverrides = {}`.

### CORE-MIG-C1-017 — documentación derivada
Las capas 50, 64 y 97 declaran al Core como autoridad normativa.

### CORE-MIG-C1-018 — compatibilidad de saves
Stable IDs y significado de World State se conservan; no se requiere migración de saves.

### CORE-MIG-C1-019 — autoridad única
Core es la única fuente normativa de EMP, AGEN y WAIT.

## Resultado esperado

**MIGRATION_BATCH_C1_COMPATIBLE**
