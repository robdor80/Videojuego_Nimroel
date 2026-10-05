# Nimroel Core — regresión de migración STAT / CRED / CONF / DIAL / ATTN / EXP v0.1

## Estado

**REGRESIÓN OBLIGATORIA PARA EL LOTE A3**

## Objetivo

Comprobar que la extracción al Core mantiene exactamente los stable IDs, la autoridad causal y los límites de conocimiento definidos en Treskal.

## Casos

### CORE-MIG-A3-001 — stable IDs STAT
STAT01–STAT08 conservan identificador y significado.

### CORE-MIG-A3-002 — declaración no reescribe realidad
Migrar STAT no permite que una frase modifique el World State.

### CORE-MIG-A3-003 — stable IDs CRED
CRED01–CRED08 conservan identificador y significado.

### CORE-MIG-A3-004 — credibilidad no equivale a verdad
Ningún actor obtiene acceso a la verdad oculta por migración.

### CORE-MIG-A3-005 — stable IDs CONF
CONF01–CONF07 conservan identificador y significado.

### CORE-MIG-A3-006 — conocimiento y permiso siguen separados
Conocer una información no autoriza su divulgación.

### CORE-MIG-A3-007 — stable IDs DIAL
DIAL01–DIAL08 conservan identificador y significado.

### CORE-MIG-A3-008 — el diálogo no congela el mundo
Los actores mantienen tiempo, obligaciones y capacidad de terminar la interacción.

### CORE-MIG-A3-009 — stable IDs ATTN
ATTN01–ATTN08 conservan identificador y significado.

### CORE-MIG-A3-010 — perceptible no equivale a notado
La migración no concede detección retroactiva ni supera límites físicos.

### CORE-MIG-A3-011 — stable IDs EXP
EXP01–EXP08 conservan identificador y significado.

### CORE-MIG-A3-012 — expectativa no equivale a futuro
Los actores siguen anticipando desde conocimiento y experiencia, nunca desde World State futuro oculto.

### CORE-MIG-A3-013 — overrides de Treskal vacíos
Los seis contratos locales figuran como `migrated_to_core_override` con `localOverrides = {}`.

### CORE-MIG-A3-014 — documentación derivada
Las capas 80, 81, 82, 92, 93 y 95 indican que la autoridad normativa reside en Nimroel Core.

### CORE-MIG-A3-015 — autoridad única
Core es la única fuente normativa de STAT, CRED, CONF, DIAL, ATTN y EXP.

## Resultado esperado

**MIGRATION_BATCH_A3_COMPATIBLE**

## Regla final

**La migración cambia la ubicación de la autoridad; no cambia lo que un actor dijo, creyó, ocultó, atendió, esperó o podía conversar.**
