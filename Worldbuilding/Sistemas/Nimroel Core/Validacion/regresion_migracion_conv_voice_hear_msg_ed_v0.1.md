# Nimroel Core — regresión de migración CONV / VOICE / HEAR / MSG / ED v0.1

## Estado

**REGRESIÓN OBLIGATORIA PARA EL LOTE U2**

## Casos

### CORE-MIG-U2-001 — stable IDs conversación
CONV01–CONV05, VOICE01–VOICE05 y HEAR00–HEAR05 conservan significado.

### CORE-MIG-U2-002 — privacidad física
Declarar privacidad no elimina exposición acústica real.

### CORE-MIG-U2-003 — conocimiento parcial
HEAR parcial produce conocimiento parcial y oír una afirmación no la vuelve verdadera.

### CORE-MIG-U2-004 — IA limitada
La IA sólo recibe contenido realmente oído por el actor.

### CORE-MIG-U2-005 — stable IDs MSG
MSG01–MSG05 conservan identificador y significado.

### CORE-MIG-U2-006 — entrega no es conocimiento
Entregar, leer y conocer son eventos diferentes.

### CORE-MIG-U2-007 — comunicación causal
Urgencia no elimina viaje, portador, ruta ni posibilidad de pérdida/intercepción.

### CORE-MIG-U2-008 — infraestructura postal no universal
Core no presupone servicio postal moderno; Treskal conserva su ausencia como override.

### CORE-MIG-U2-009 — stable IDs ED
ED01–ED07 conservan identificador y significado.

### CORE-MIG-U2-010 — saber con procedencia
Lore disponible al motor no se convierte automáticamente en conocimiento del NPC.

### CORE-MIG-U2-011 — aprendizaje no instantáneo
Diálogo y paso de tiempo sin práctica compatible no conceden competencia.

### CORE-MIG-U2-012 — educación no universalizada
Core no fija red escolar, vivienda de aprendices ni ventaja educativa de una ciudad concreta.

### CORE-MIG-U2-013 — compatibilidad
Stable IDs y significado de World State se conservan; no se requiere migración de saves.

### CORE-MIG-U2-014 — autoridad única
Core es autoridad de CONV, VOICE, HEAR, MSG y ED; overrides sólo conservan contexto local explícito.

## Resultado esperado

**MIGRATION_BATCH_U2_COMPATIBLE**
