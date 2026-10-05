# Nimroel Core — regresión de migración PREG / CHD / AGE / KIN v0.1

## Estado

**REGRESIÓN OBLIGATORIA PARA EL LOTE B1**

## Casos

### CORE-MIG-B1-001 — stable IDs PREG
PREG01–PREG06 conservan identificador y significado.

### CORE-MIG-B1-002 — embarazo sigue siendo causal
PREG no aparece por pareja, convivencia, matrimonio, IA o conveniencia narrativa.

### CORE-MIG-B1-003 — nacimiento persistente
Cada nacimiento vivo crea NPC persistente; un recién nacido no se convierte en prop, inventario o simple contador.

### CORE-MIG-B1-004 — privacidad y conocimiento
La existencia del embarazo y quién lo conoce siguen separados.

### CORE-MIG-B1-005 — particularidad local PREG
Lugar habitual del parto y modelo de asistencia de Treskal no se convierten en ley Core y permanecen como `localOverrides`.

### CORE-MIG-B1-006 — stable IDs CHD
CHD01–CHD06 conservan identificador y significado.

### CORE-MIG-B1-007 — infancia no usa rutina adulta
CHD conserva carga, autonomía y aprendizaje dependientes de desarrollo y contexto.

### CORE-MIG-B1-008 — desarrollo offscreen válido
La etapa infantil no avanza por conveniencia narrativa o por materialización LOD.

### CORE-MIG-B1-009 — stable IDs AGE
AGE01–AGE06 conservan identificador y significado.

### CORE-MIG-B1-010 — edad no equivale a incapacidad
AGE no crea automáticamente dependencia, jubilación, pérdida de habilidad, senilidad o muerte.

### CORE-MIG-B1-011 — continuidad vital
Envejecimiento conserva identidad, memoria, relaciones, reputación, propiedad e historia.

### CORE-MIG-B1-012 — stable IDs KIN
KIN01–KIN07 conservan identificador y significado.

### CORE-MIG-B1-013 — parentesco separado de otros sistemas
KIN no equivale a RES/H, AFF, FRI, CARE, TRUST, OWN ni herencia.

### CORE-MIG-B1-014 — hecho familiar y conocimiento
K, CRED, CONF y STAT siguen gobernando conocimiento, disputa, privacidad y afirmaciones sin reescribir KIN.

### CORE-MIG-B1-015 — derecho y cultura no hardcodeados
Tutela, adopción, afinidad, herencia, mayoría, apellidos y reglas familiares continúan fuera del Core cuando dependen de canon superior.

### CORE-MIG-B1-016 — overrides de Treskal
CHD, AGE y KIN figuran como `migrated_to_core_override` con `localOverrides = {}`; PREG conserva solo las particularidades locales explícitas.

### CORE-MIG-B1-017 — documentación derivada
Las capas 71, 72, 73 y 99 declaran al Core como autoridad normativa.

### CORE-MIG-B1-018 — compatibilidad de saves
Los stable IDs y el significado del World State se conservan; no se requiere migración de saves.

### CORE-MIG-B1-019 — autoridad única
Core es la única fuente normativa de PREG, CHD, AGE y KIN; los overrides locales no duplican semántica universal.

## Resultado esperado

**MIGRATION_BATCH_B1_COMPATIBLE**
