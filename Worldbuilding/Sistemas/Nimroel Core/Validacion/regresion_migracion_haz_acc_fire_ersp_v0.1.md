# Nimroel Core — regresión de migración HAZ / ACC / FIRE / ERSP v0.1

## Estado

**REGRESIÓN OBLIGATORIA PARA EL LOTE D4**

## Casos

### CORE-MIG-D4-001 — stable IDs HAZ/ACC
HAZ01–HAZ07 y ACC01–ACC08 conservan identificador y significado.

### CORE-MIG-D4-002 — riesgo no es accidente
Detectar un riesgo no fuerza automáticamente un incidente.

### CORE-MIG-D4-003 — accidente causal
Incidentes conservan causas, actores, objetos, testigos y consecuencias persistentes.

### CORE-MIG-D4-004 — salud separada
La gravedad fisiológica la resuelve salud, no HAZ/ACC.

### CORE-MIG-D4-005 — regulación no universalizada
Core no inventa normativa moderna de seguridad ni catálogo universal de EPI.

### CORE-MIG-D4-006 — stable IDs FIRE
FIRE01–FIRE08 conservan identificador y significado.

### CORE-MIG-D4-007 — ignición y propagación
Fuego necesita causa y su propagación depende de condiciones materiales reales.

### CORE-MIG-D4-008 — percepción de incendio
Nadie recibe conocimiento omnisciente de un fuego sin señal o comunicación.

### CORE-MIG-D4-009 — extinción material
Agua y respuesta requieren recursos, personas y acceso; lluvia no resuelve automáticamente incendios protegidos.

### CORE-MIG-D4-010 — organización local
Treskal conserva su ausencia de brigada moderna y la mayor capacidad interna de los Astilleros Reales sin convertirla en regla Core.

### CORE-MIG-D4-011 — stable IDs ERSP
ERSP01–ERSP08 conservan identificador y significado.

### CORE-MIG-D4-012 — respuesta informada
Amenaza oculta no genera reacción; evacuación y ayuda requieren conocimiento, capacidad y rutas válidas.

### CORE-MIG-D4-013 — IA limitada
La IA no puede declarar rescate, extinción, curación o seguridad sin validación del sistema propietario.

### CORE-MIG-D4-014 — compatibilidad
Stable IDs y significado de World State se conservan; no se requiere migración de saves.

### CORE-MIG-D4-015 — autoridad única
Core es autoridad de HAZ, ACC, FIRE y ERSP; Treskal sólo conserva organización/tecnología local explícita.

## Resultado esperado

**MIGRATION_BATCH_D4_COMPATIBLE**
