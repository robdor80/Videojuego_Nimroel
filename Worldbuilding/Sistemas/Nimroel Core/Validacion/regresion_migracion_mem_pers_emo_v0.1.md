# Nimroel Core — regresión de migración MEM / PERS / EMO-MOOD v0.1

## Estado

**REGRESIÓN OBLIGATORIA PARA LA PRIMERA EXTRACCIÓN CORE**

## Objetivo

Comprobar que extraer sistemas desde Treskal no cambia su comportamiento ni crea dos autoridades activas.

## Casos

### CORE-MIG-001 — stable IDs MEM

Debe cumplirse:

- MEM01–MEM08 conservan exactamente su identificador y significado;
- un save de Treskal no necesita remapeo por esta migración.

### CORE-MIG-002 — stable IDs PERS

Debe cumplirse:

- PERS01–PERS10 conservan identificador y significado;
- un perfil autoral o procedural existente sigue interpretándose igual.

### CORE-MIG-003 — stable IDs EMO/MOOD

Debe cumplirse:

- EMO01–EMO10 y MOOD01–MOOD07 conservan identificador y significado;
- episodios emocionales existentes continúan válidos.

### CORE-MIG-004 — autoridad única

Debe cumplirse:

- el contrato Core figura como `active_core_contract`;
- el contrato Treskal figura como `migrated_to_core_override`;
- Treskal no redefine estados universales en `localOverrides`.

### CORE-MIG-005 — herencia completa

Con `localOverrides = {}`:

- Treskal utiliza exactamente la semántica Core;
- no cambia resultado por pertenecer a Norgard o Casa Valrik.

### CORE-MIG-006 — personalidad y cultura

Debe cumplirse:

- Norgard puede aportar normas culturales futuras;
- esas normas no modifican automáticamente PERS de cada individuo;
- la migración no convierte cultura en personalidad.

### CORE-MIG-007 — emoción y conocimiento

Debe cumplirse:

- un hecho oculto sigue sin poder provocar EMO sin vía de conocimiento;
- el narrador externo sigue sin recibir estado emocional interno como hecho perceptible.

### CORE-MIG-008 — memoria y pasado

Debe cumplirse:

- MEM no se convierte en verdad objetiva;
- olvidar no borra consecuencias del World State;
- no se rellenan detalles ausentes durante migración.

### CORE-MIG-009 — documentación local

Debe cumplirse:

- los documentos 83, 87 y 88 de Treskal están marcados como derivados;
- ante conflicto documental prevalece la ruta Core indicada.

### CORE-MIG-010 — no doble autoridad

Debe cumplirse:

- ningún sistema migrado tiene dos contratos activos con semántica independiente;
- cualquier futura excepción local debe existir únicamente como override explícito.

## Resultado esperado

Si los diez casos son verdaderos:

**MIGRATION_BATCH_A1_COMPATIBLE**

## Regla final

**Extraer un sistema al Core cambia dónde vive su autoridad, no cómo funciona una partida existente.**
