# Nimroel Core — regresión de migración K y separación de reputación v0.1

## Estado

**REGRESIÓN OBLIGATORIA PARA EL LOTE U3**

## Casos

### CORE-MIG-U3-001 — stable IDs K
K0–K5 conservan identificador y significado.

### CORE-MIG-U3-002 — conocimiento no es verdad
K1–K5 describen cómo conoce/interpreta un actor; no reescriben el hecho del World State.

### CORE-MIG-U3-003 — procedencia obligatoria
Conocimiento nuevo requiere percepción, comunicación, documento, aprendizaje, descubrimiento o vía válida.

### CORE-MIG-U3-004 — rumor
K3 puede ser falso y su repetición no lo convierte automáticamente en verdadero.

### CORE-MIG-U3-005 — aviso oficial
K4 refleja recepción de una comunicación oficial, no infalibilidad.

### CORE-MIG-U3-006 — contradicción
K5 conserva conflicto entre versiones sin resolverlo por conveniencia narrativa.

### CORE-MIG-U3-007 — integración CONV/MSG/ED
Audición parcial, mensajería y aprendizaje sólo actualizan K cuando existe exposición o adquisición real.

### CORE-MIG-U3-008 — separación MEM
MEM puede retener, degradar o priorizar conocimiento existente; no crea una fuente inicial inexistente.

### CORE-MIG-U3-009 — separación STAT/CRED
Integridad de declaración y credibilidad no sustituyen K ni modifican automáticamente el hecho objetivo.

### CORE-MIG-U3-010 — reputación separada
Los campos de reputación del antiguo contrato no se trasladan a K y quedan en `treskal_reputation_network_contract_v0.1.json`.

### CORE-MIG-U3-011 — canales locales
Puerto, mercado, guardia y demás canales concretos de Treskal permanecen como override local, no como taxonomía universal.

### CORE-MIG-U3-012 — contrato mixto retirado
`treskal_information_and_reputation_contract_v0.1.json` queda sólo como bridge y no conserva autoridad normativa duplicada.

### CORE-MIG-U3-013 — compatibilidad
K0–K5 y el significado del World State se conservan; no se requiere migración de saves.

### CORE-MIG-U3-014 — cobertura completa
Todos los namespaces listados como `highConfidenceCoreNamespaces` están presentes en el manifest de Nimroel Core.

## Resultado esperado

**MIGRATION_BATCH_U3_COMPATIBLE_AND_HIGH_CONFIDENCE_CORE_COMPLETE**
