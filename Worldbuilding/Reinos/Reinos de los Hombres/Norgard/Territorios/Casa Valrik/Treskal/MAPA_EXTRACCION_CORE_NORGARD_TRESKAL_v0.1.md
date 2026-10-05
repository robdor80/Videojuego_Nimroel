# Treskal — mapa de extracción Nimroel Core / Norgard / Treskal v0.1

## Estado

**PLAN DE REFACTORIZACIÓN APROBADO — EJECUCIÓN INICIADA**

## 0. Progreso de ejecución

Primer lote migrado y activo en Nimroel Core:

- MEM — memoria;
- PERS — personalidad;
- EMO / MOOD — emoción y estado de ánimo.

Treskal conserva contratos con los mismos nombres como **overrides de compatibilidad**, sin semántica local duplicada.

Regresión asociada:

`Worldbuilding/Sistemas/Nimroel Core/Validacion/regresion_migracion_mem_pers_emo_v0.1.md`

Estado del lote:

**MIGRATION_BATCH_A1_READY_FOR_REGRESSION**

### Lote A2 migrado

- GOAL — objetivos;
- DEC — decisión;
- TRUST — confianza interpersonal;
- VIEW — opiniones y actitudes.

Estado:

**MIGRATION_BATCH_A2_READY_FOR_REGRESSION**

### Lote A3 migrado

- STAT — integridad de declaraciones;
- CRED — credibilidad y verificación;
- CONF — confidencialidad;
- DIAL — dinámica de conversación;
- ATTN — atención y foco;
- EXP — expectativas y revisión.

Estado:

**MIGRATION_BATCH_A3_READY_FOR_REGRESSION**

### Lote A4 migrado

- STRS — presión acumulada y recuperación;
- VAL — valores y principios personales;
- SELF — identidad y roles personales.

Estado:

**MIGRATION_BATCH_A4_READY_FOR_REGRESSION**

### Lote B1 migrado

- PREG — embarazo, parto y primera infancia;
- CHD — desarrollo infantil y autonomía;
- AGE — envejecimiento y actividad en la vejez;
- KIN — parentesco y red familiar.

Estado:

**MIGRATION_BATCH_B1_READY_FOR_REGRESSION**

Nota de separación: PREG conserva en Treskal un override local explícito para el entorno habitual del parto y el modelo de asistencia de su red sanitaria. Esas particularidades no se universalizan en Core.

### Lote B2 migrado

- DEP / CARE — dependencia y cobertura de cuidados;
- CHORE / DOM — tareas y carga doméstica;
- REST — sueño, descanso y disponibilidad;
- NEED — necesidades físicas cotidianas.

Estado:

**MIGRATION_BATCH_B2_READY_FOR_REGRESSION**

Nota de separación: DEP / CARE conserva en Treskal un override local explícito para la ausencia por defecto de guardería moderna o cuidado residencial institucional. El Core no impone un modelo institucional universal.

### Lote C1 migrado

- EMP — empleo, puestos y vacantes;
- AGEN — agenda personal y uso del tiempo;
- WAIT — espera y capacidad efectiva de servicio.

Estado:

**MIGRATION_BATCH_C1_READY_FOR_REGRESSION**

### Lote C2 migrado

- RES / MOVE — residencia, hogar y mudanzas;
- APR — aprendizaje de oficio;
- FAV — favores y reciprocidad informal;
- REQ — peticiones, consentimiento y límites personales.

Estado:

**MIGRATION_BATCH_C2_READY_FOR_REGRESSION**

Fase C queda completamente extraída al Core.

### Lote D1 migrado

- OWN — propiedad, posesión y objetos;
- COND — condición, desgaste y reparación;
- TOOL / WS — herramientas, estaciones y capacidad productiva.

Estado:

**MIGRATION_BATCH_D1_READY_FOR_REGRESSION**

### Lote D2 migrado

- BUILD — construcción y cambio edificado;
- DOOR — puertas, llaves y acceso físico.

Estado:

**MIGRATION_BATCH_D2_READY_FOR_REGRESSION**

Nota de separación: Treskal conserva únicamente la protección de sus namespaces/instalaciones urbanas concretas y la referencia a su sistema local de clases de acceso P.

### Lote D3 migrado

- WASTE / WST — residuos, saneamiento y ciclo de retirada.

Estado:

**MIGRATION_BATCH_D3_READY_FOR_REGRESSION**

Nota de separación: Core no universaliza la tecnología sanitaria. Treskal conserva como override su modelo sin alcantarillado moderno y su organización sanitaria preindustrial.

### Lote D4 migrado

- HAZ / ACC — riesgos y accidentes;
- FIRE — incendio, propagación y respuesta;
- ERSP — respuesta personal ante emergencias.

Estado:

**MIGRATION_BATCH_D4_READY_FOR_REGRESSION**

**Fase D — material y riesgo: COMPLETA.**

Nota de separación: la normativa/equipamiento de seguridad y la organización concreta contra incendios no se universalizan. Treskal conserva sus particularidades explícitas.

### Lote U1 migrado — relaciones universales restantes

- FRI — amistad y círculos sociales;
- AFF — relación afectiva y pareja;
- RIFT — conflicto interpersonal y reparación;
- GIFT — regalos y significado social.

Estado:

**MIGRATION_BATCH_U1_READY_FOR_REGRESSION**

### Lote U2 migrado — comunicación y aprendizaje

- CONV / VOICE / HEAR — privacidad, voz y audición;
- MSG — mensajería y entrega;
- ED — aprendizaje y transmisión de saber.

Estado:

**MIGRATION_BATCH_U2_READY_FOR_REGRESSION**

Nota de separación: Core no universaliza servicio postal ni estructura educativa. Treskal conserva sus supuestos institucionales concretos.

### Lote U3 migrado — K y separación de reputación

- K — conocimiento y procedencia.

El antiguo contrato mixto información/reputación queda dividido:

- **K** → Nimroel Core;
- **reputación** → contrato local separado de Treskal hasta una extracción futura explícita;
- canales concretos de información de Treskal → override local.

Estado:

**MIGRATION_BATCH_U3_READY_FOR_REGRESSION**

**TODOS LOS NAMESPACES DE ALTA CONFIANZA PARA NIMROEL CORE HAN SIDO EXTRAÍDOS.**

### Fase E1 — funeral y luto de Norgard

Extraído como default activo de Reino:

- cremación en pira;
- retorno de restos al territorio;
- luto formal de tres jornadas;
- duelo personal sin duración fija;
- prohibición de inventar rito religioso, color o vestimenta universal.

Treskal conserva como local:

- piras comunales periféricas;
- terreno comunal de retorno;
- variante marítima opcional ligada al Mar de Suthiros;
- IDs MORT / ASH y su world state actual.

Estado:

**NORGARD_DEFAULT_E1_READY_FOR_REGRESSION**

### Fase E2 — autoridad monetaria

Extraído como default parcial activo de Reino:

- solo la Corona puede acuñar moneda oficial;
- poseer o producir oro/plata no concede derecho de acuñación;
- falsificación y acuñación ilícita son delitos graves;
- moneda completa, precios, salarios, impuestos, ceca y penas concretas siguen pendientes.

Estado:

**NORGARD_DEFAULT_E2_READY_FOR_REGRESSION**

### Fase E3 — convención toponímica

Extraída como default activo de Reino:

- sistema mixto de nombres;
- base histórica/cultural obligatoria para nombres antiguos;
- no pseudo-nórdico decorativo;
- microtoponimia descriptiva válida;
- nombre visible separado del ID técnico.

Treskal conserva sus nombres concretos y sus IDs T/Z/L/S/C/A/APP.

Estado:

**NORGARD_DEFAULT_E3_READY_FOR_REGRESSION**

**Todos los candidatos de Norgard marcados READY por la auditoría inicial han sido extraídos.**

### Fase E0 — auditoría de Norgard Defaults

Creada la capa `Worldbuilding/Sistemas/Norgard Defaults/` y auditados los candidatos culturales.

Listos con canon de Reino:

- cremación y retorno de restos al territorio;
- luto formal de tres jornadas;
- monopolio de la Corona sobre la acuñación oficial;
- convención toponímica de Norgard.

No se promueve a Norgard:

- peso especial de la palabra dada: candidato de **Casa Valrik**.

Bloqueados por canon insuficiente o pendiente:

- sistema militar final;
- familia/matrimonio/tutela;
- mayoría de edad/derecho laboral;
- propiedad/herencia/alquiler;
- economía completa;
- curandería general;
- marco naval/terminología;
- gastronomía;
- nombres personales/apellidos;
- calendario detallado;
- cultura material común.

Estado:

**NORGARD_DEFAULTS_AUDIT_COMPLETE**

---

## Objetivo

Separar el trabajo acumulado en Treskal en tres niveles de autoridad:

1. **Nimroel Core** — reglas universales de simulación;
2. **Norgard defaults** — cultura, instituciones y normas compartidas del reino;
3. **Treskal overrides** — geografía, economía, identidad urbana y excepciones locales.

Hasta que la migración se ejecute y valide:

**Treskal sigue siendo la autoridad actual de sus contratos.**

---

# 1. Nimroel Core — candidatos de alta confianza

Los siguientes sistemas son conceptualmente reutilizables en cualquier territorio, aunque sus parámetros concretos puedan variar.

## Mundo, persistencia y objetos

- K — conocimiento;
- OWN — propiedad/posesión;
- COND — condición material;
- DOOR — acceso físico;
- BUILD — construcción/cambio;
- TOOL / WS — herramientas y puestos;
- WASTE / WST — residuos;
- FIRE — ciclo de incendio;
- HAZ / ACC — riesgos y accidentes.

## Actividad, tiempo y capacidad

- EMP — empleo;
- RES / MOVE — residencia y mudanza;
- REST — descanso;
- WAIT — espera;
- AGEN — agenda;
- NEED — necesidades físicas cualitativas;
- ERSP — respuesta personal a emergencia.

## Hogar y ciclo vital

- DEP / CARE — dependencia y cuidado;
- CHORE / DOM — tareas domésticas;
- APR — aprendizaje de oficio;
- PREG — embarazo;
- CHD — desarrollo infantil;
- AGE — envejecimiento;
- KIN — parentesco persistente.

## Relaciones sociales

- FRI — amistad;
- AFF — relación afectiva;
- RIFT — conflicto interpersonal;
- FAV — favores;
- GIFT — regalos;
- REQ — peticiones y límites;
- TRUST — confianza;
- VIEW — actitudes/opiniones.

## Cognición e IA

- CONF — confidencialidad;
- STAT — integridad de declaraciones;
- CRED — credibilidad;
- EMO / MOOD — emociones y ánimo;
- GOAL — objetivos;
- DEC — decisión;
- STRS — presión;
- PERS — personalidad;
- MEM — memoria;
- VAL — valores personales;
- SELF — identidad personal;
- EXP — expectativas;
- ATTN — atención;
- DIAL — dinámica de conversación.

## Comunicación y percepción

- CONV / VOICE / HEAR — privacidad y audición;
- MSG — mensajes;
- ED — aprendizaje/saber.

Estos sistemas deben extraerse como **contratos genéricos**, no copiarse literalmente con nombres Treskal.

---

# 2. Norgard defaults — candidatos

Norgard debe aportar valores por defecto compartidos por sus territorios cuando exista canon suficiente.

Candidatos claros:

- tradición funeraria y cremación;
- tres días de luto formal;
- peso cultural de la palabra dada;
- tradición de curandería;
- formas familiares y matrimonio cuando se definan;
- mayoría de edad y reglas laborales;
- derecho de propiedad/herencia;
- moneda y marco económico;
- organización militar y guardia;
- marco naval real;
- terminología marítima;
- gastronomía;
- calendario y ritmos oficiales;
- convenciones de nombre/apellido;
- cultura material común.

Treskal no debe fijar estas reglas por su cuenta si deben ser heredadas por todo Norgard.

---

# 3. Treskal — debe permanecer local

Alta confianza de contenido exclusivamente local:

- sectores T;
- subzonas Z;
- landmarks L;
- instalaciones singulares S;
- corredores C;
- activity anchors A;
- accesos APP;
- grafo urbano;
- distribución espacial;
- ciudad principalmente en una orilla;
- puente principal;
- desembocadura integrada;
- puerto civil;
- Astilleros Reales en T08;
- identidad de la madera;
- flujos económicos locales;
- capacidad y posición de mercados;
- tejido residencial/comercial;
- arquitectura urbana local;
- rutas de tráfico;
- topónimos;
- historia urbana;
- cartografía;
- stock y población concretos materializados.

---

# 4. Capas mixtas que deben dividirse

No todo archivo actual puede moverse entero.

## Salud

Core:

- capacidad;
- desplazamiento de cuidador;
- disponibilidad;
- separación de conocimiento y privacidad.

Norgard:

- tradición de curandería predominantemente femenina;
- formación cultural;
- remedios autorizados.

Treskal:

- número/capacidad derivada local;
- distribución urbana de atención.

## Funeral

Core:

- muerte;
- persistencia;
- duelo personal;
- consecuencias.

Norgard:

- cremación;
- tres días de luto;
- tratamiento cultural de cenizas.

Treskal:

- espacios locales;
- rutas;
- capacidad.

## Alimentación

Core:

- consumo;
- stock;
- necesidad;
- preparación y acceso.

Norgard:

- cocina y productos culturales.

Treskal:

- abastecimiento real;
- procedencias;
- mercados;
- disponibilidad local.

## Hospitalidad

Core:

- huésped;
- acceso;
- capacidad;
- tiempo;
- propiedad.

Norgard:

- expectativas culturales de hospitalidad.

Treskal:

- red concreta de posadas/hogares y capacidad.

## Cultura marítima y madera

Pueden contener:

- reglas Core de trabajo/material;
- defaults Valrik/Norgard;
- identidad específica de Treskal.

Requieren separación manual.

---

# 5. Regla de migración

No copiar y dejar dos fuentes activas.

Para cada contrato:

1. identificar reglas universales;
2. crear contrato Core;
3. identificar defaults culturales;
4. crear override/default de Norgard;
5. dejar en Treskal únicamente referencias y excepciones locales;
6. ejecutar regresiones;
7. retirar o marcar como migrado el origen duplicado.

---

# 6. Orden recomendado

## Fase A — Cognición y relaciones

Primero extraer:

- K;
- MEM;
- PERS;
- EMO/MOOD;
- GOAL;
- DEC;
- TRUST;
- VIEW;
- STAT;
- CRED;
- CONF;
- DIAL;
- ATTN;
- EXP;
- STRS;
- VAL;
- SELF.

K se extraerá en un lote específico tras separar conocimiento de reputación. Estos sistemas tienen poca dependencia de geometría local y máxima reutilización.

## Fase B — Ciclo vital y hogar

- PREG;
- CHD;
- AGE;
- KIN;
- DEP/CARE;
- CHORE/DOM;
- REST;
- NEED.

## Fase C — Actividad y tiempo

- EMP;
- AGEN;
- WAIT;
- RES/MOVE;
- APR;
- FAV;
- REQ.

## Fase D — Material y riesgo

- OWN;
- COND;
- TOOL/WS;
- HAZ/ACC;
- FIRE;
- WASTE/WST;
- BUILD;
- DOOR;
- ERSP.

## Fase E — separar defaults culturales

Solo cuando exista canon suficiente de Norgard.

---

# 7. Compatibilidad

Durante la migración debe mantenerse:

- stable ID o equivalencia explícita;
- migración de saves;
- referencias entre contratos;
- pruebas IA;
- pruebas de integración;
- ausencia de doble autoridad.

---

# 8. Resultado objetivo

La arquitectura deseada es:

**Nimroel Core → Norgard Defaults → Casa/Territorio → Treskal Override → World State de partida**

No todos los niveles tienen que aportar datos a cada sistema.

---

## Regla final

**Treskal ha servido como laboratorio; la refactorización correcta consiste en extraer sus leyes universales sin arrancarle aquello que la hace Treskal.**
