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
