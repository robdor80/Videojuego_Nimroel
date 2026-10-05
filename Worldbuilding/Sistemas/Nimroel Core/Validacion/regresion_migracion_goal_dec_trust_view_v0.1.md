# Nimroel Core — regresión de migración GOAL / DEC / TRUST / VIEW v0.1

## Estado

**REGRESIÓN OBLIGATORIA PARA EL LOTE A2**

## Objetivo

Comprobar que la extracción al Core mantiene la semántica de Treskal y evita doble autoridad.

## Casos

### CORE-MIG-A2-001 — stable IDs GOAL
GOAL01–GOAL08 conservan identificador y significado.

### CORE-MIG-A2-002 — objetivos no se convierten en quests
Un objetivo NPC sigue pudiendo existir, avanzar o resolverse sin exponerse como contenido del jugador.

### CORE-MIG-A2-003 — stable IDs DEC
DEC01–DEC08 conservan identificador y significado.

### CORE-MIG-A2-004 — decisión limitada por conocimiento
Migrar DEC no concede acceso a opciones, rutas, hechos o resultados ocultos.

### CORE-MIG-A2-005 — stable IDs TRUST
TRUST01–TRUST08 conservan identificador y significado por dominio.

### CORE-MIG-A2-006 — confianza sigue separada
FRI, AFF, reputación, CRED y competencia siguen sin convertirse en TRUST.

### CORE-MIG-A2-007 — stable IDs VIEW
VIEW01–VIEW08 conservan identificador y significado.

### CORE-MIG-A2-008 — opinión sigue siendo subjetiva
VIEW no se transforma en verdad objetiva ni se propaga sin información.

### CORE-MIG-A2-009 — overrides de Treskal vacíos
Los cuatro contratos locales figuran como `migrated_to_core_override` con `localOverrides = {}`.

### CORE-MIG-A2-010 — autoridad única
Core es la única fuente normativa de GOAL, DEC, TRUST y VIEW; la documentación local queda marcada como derivada.

## Resultado esperado

**MIGRATION_BATCH_A2_COMPATIBLE**

## Regla final

**La migración cambia la ubicación de la autoridad, no las decisiones, metas, confianza u opiniones ya existentes en la partida.**
