# Nimroel Core — regresión de migración RES / MOVE / APR / FAV / REQ v0.1

## Estado

**REGRESIÓN OBLIGATORIA PARA EL LOTE C2**

## Casos

### CORE-MIG-C2-001 — stable IDs RES/MOVE
RES01–RES05 y MOVE01–MOVE06 conservan identificador y significado.

### CORE-MIG-C2-002 — continuidad de identidad
Cambiar de hogar, residencia o categoría visitante/residente no crea un NPC nuevo ni reinicia memoria, relaciones o reputación.

### CORE-MIG-C2-003 — residencia causal
Una estancia prolongada por sí sola no convierte a un visitante en residente.

### CORE-MIG-C2-004 — mudanza material
MOVE exige origen, destino, causa y proceso; no teletransporta hogar, bienes o negocio.

### CORE-MIG-C2-005 — desplazamiento
RES05 requiere causa real y no crea vivienda de sustitución automática.

### CORE-MIG-C2-006 — stable IDs APR
APR01–APR06 conservan identificador y significado.

### CORE-MIG-C2-007 — progreso por evidencia
Tiempo transcurrido sin práctica válida no avanza competencia.

### CORE-MIG-C2-008 — límites de tarea
Aprendices no ejecutan trabajo fuera de estado, herramientas, supervisión y riesgo válidos.

### CORE-MIG-C2-009 — continuidad formativa
Cambio o pérdida de mentor e interrupciones no borran progreso acumulado.

### CORE-MIG-C2-010 — IA y saber técnico
Diálogo no concede instantáneamente dominio de un oficio complejo.

### CORE-MIG-C2-011 — stable IDs FAV
FAV01–FAV07 conservan identificador y significado.

### CORE-MIG-C2-012 — favor no monetizado
FAV no se convierte en moneda, deuda legal, pledge automático ni derecho ilimitado.

### CORE-MIG-C2-013 — ayuda causal
Un favor requiere actor, oportunidad, capacidad y acción reales, también offscreen.

### CORE-MIG-C2-014 — conocimiento social
Un favor no se vuelve conocimiento público automáticamente.

### CORE-MIG-C2-015 — stable IDs REQ
REQ01–REQ08 conservan identificador y significado.

### CORE-MIG-C2-016 — petición no es orden
Una relación o tono imperativo no crea autoridad.

### CORE-MIG-C2-017 — rechazo válido
REQ05 puede existir sin hostilidad automática; repetir no fuerza aceptación.

### CORE-MIG-C2-018 — alcance del permiso
Aceptar una acción no concede acceso, propiedad, permiso o disponibilidad fuera del alcance validado.

### CORE-MIG-C2-019 — contratos locales
RES/MOVE, APR, FAV y REQ quedan como `migrated_to_core_override` con `localOverrides = {}`.

### CORE-MIG-C2-020 — documentación derivada
Las capas 51, 68, 77 y 79 declaran al Core como autoridad normativa.

### CORE-MIG-C2-021 — compatibilidad de saves
Los stable IDs y el significado del World State se conservan; no se requiere migración de saves.

### CORE-MIG-C2-022 — autoridad única
Core es la única fuente normativa de RES, MOVE, APR, FAV y REQ.

## Resultado esperado

**MIGRATION_BATCH_C2_COMPATIBLE**
