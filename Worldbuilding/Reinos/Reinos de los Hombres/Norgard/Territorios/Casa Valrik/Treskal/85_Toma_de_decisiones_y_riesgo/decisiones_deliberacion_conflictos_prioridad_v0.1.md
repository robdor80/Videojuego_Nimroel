# Treskal — decisiones, deliberación y conflictos de prioridad v0.1

## Estado

**DISEÑO DE NPC APROBADO — ELEGIR NO ES OPTIMIZAR UNA TABLA OCULTA**

## Objetivo

Definir cómo un NPC persistente elige entre alternativas usando únicamente aquello que:

- conoce;
- cree;
- desea;
- teme;
- debe hacer;
- puede hacer.

Sin convertir cada decisión en una puntuación matemática universal.

---

# 1. Estados operativos

## DEC01 — choice_pending

Existe una decisión relevante todavía no resuelta.

## DEC02 — options_identified

El NPC reconoce una o varias alternativas plausibles.

## DEC03 — evaluating_tradeoffs

Está valorando costes, beneficios, riesgos u obligaciones incompatibles.

## DEC04 — choice_made

Ha elegido una opción.

## DEC05 — action_started

La elección ha comenzado a convertirse en una acción real.

## DEC06 — reconsidered

Nueva información o circunstancias hacen revisar la decisión.

## DEC07 — abandoned_choice

La opción elegida deja de perseguirse antes de completarse.

## DEC08 — decision_resolved

La decisión ya ha producido un resultado suficiente o ha dejado de ser relevante.

---

# 2. Opciones conocidas

Un NPC no puede elegir deliberadamente una opción que desconoce.

Las alternativas proceden de:

- experiencia;
- K;
- CRED;
- rutas conocidas;
- relaciones;
- profesión;
- consejo recibido;
- observación;
- intentos anteriores.

No consulta el árbol completo de posibilidades del motor.

---

# 3. Objetivos

GOAL aporta qué resultados desea.

Una decisión puede favorecer:

- un objetivo;
- varios;
- ninguno por completo.

El NPC puede aceptar una solución imperfecta.

---

# 4. Obligaciones

Una decisión puede estar condicionada por:

- EMP;
- CARE;
- PLEDGE;
- autoridad;
- seguridad;
- hogar;
- relaciones.

El deseo personal no borra automáticamente obligaciones existentes.

---

# 5. Emoción y ánimo

EMO y MOOD pueden influir en:

- urgencia;
- paciencia;
- riesgo percibido;
- disposición a hablar;
- tolerancia a demora.

No determinan una respuesta única.

---

# 6. Personalidad

La personalidad puede favorecer tendencias como:

- prudencia;
- impulsividad;
- paciencia;
- sociabilidad;
- terquedad;
- flexibilidad.

No convierte al NPC en una función determinista.

---

# 7. Relaciones

La decisión puede valorar el efecto sobre:

- familia;
- amigos;
- pareja;
- compañeros;
- reputación conocida.

Pero una relación fuerte no garantiza sacrificio ilimitado.

---

# 8. Información incompleta

El NPC puede decidir sin disponer de certeza.

Puede:

- esperar;
- preguntar;
- verificar;
- asumir riesgo;
- escoger con información parcial.

CRED permite distinguir confianza de certeza.

---

# 9. Indecisión

No decidir inmediatamente es una opción válida cuando:

- falta información;
- el coste es alto;
- las alternativas están equilibradas;
- existe conflicto de obligaciones;
- el plazo lo permite.

No todo diálogo exige respuesta instantánea.

---

# 10. Urgencia

En emergencia puede reducirse la deliberación.

Eso no autoriza al motor a elegir cualquier cosa.

Las opciones siguen limitadas por:

- percepción;
- conocimiento;
- capacidad;
- contexto.

---

# 11. Jugador

El jugador puede:

- aportar información;
- proponer opciones;
- presionar;
- aconsejar;
- ayudar a desbloquear una alternativa.

No selecciona directamente la decisión interna de otro NPC salvo que exista autoridad legítima sobre la acción correspondiente.

---

# 12. IA

La IA puede razonar sobre alternativas autorizadas y proponer una elección.

No puede inventar:

- recursos;
- rutas;
- permisos;
- conocimientos;
- relaciones

para justificarla.

---

## Regla final

**Un habitante de Treskal elige desde su propia vida y su propio conocimiento; no desde la solución que el diseñador o el jugador saben que sería perfecta.**
