# Treskal — dinámica de conversación, disponibilidad y continuidad v0.1

> **MIGRADO A NIMROEL CORE — documentación derivada.** La autoridad normativa de DIAL reside en `Worldbuilding/Sistemas/Nimroel Core/01_Cognicion_y_conducta/dinamica_de_conversacion_v0.1.md`. Este archivo conserva explicación y ejemplos de Treskal; ante conflicto prevalece el Core.


## Estado

**DISEÑO SOCIAL/JUGABLE APROBADO — HABLAR CON UN NPC NO DETIENE SU VIDA**

## Objetivo

Definir el estado de una conversación como interacción real entre personas persistentes.

La conversación debe respetar:

- presencia;
- atención;
- actividad;
- privacidad;
- conocimiento;
- límites;
- tiempo;
- eventos.

---

# 1. Estados operativos

## DIAL01 — available_for_conversation

El NPC puede conversar de forma razonable en ese momento.

## DIAL02 — engaged

La conversación está activa y ambas partes participan.

## DIAL03 — guarded

El NPC conversa, pero limita contenido, confianza o exposición.

## DIAL04 — topic_refused

Rechaza tratar un tema concreto.

## DIAL05 — hurried_or_limited

Puede hablar, pero solo durante un tiempo o alcance reducido.

## DIAL06 — interrupted

La conversación se interrumpe por una causa externa o prioritaria.

## DIAL07 — closing

El NPC intenta terminar la interacción.

## DIAL08 — ended

La conversación ha finalizado.

---

# 2. Disponibilidad

Un NPC puede no estar disponible porque:

- trabaja;
- duerme;
- atiende a alguien;
- está viajando;
- afronta una emergencia;
- tiene una necesidad urgente;
- no desea hablar.

El jugador no convierte automáticamente al NPC en disponible al iniciar diálogo.

---

# 3. Conversar mientras se hace otra cosa

Una conversación puede ser compatible con:

- trabajo sencillo;
- caminar;
- comer;
- esperar;
- tareas domésticas.

Otras actividades pueden exigir ATTN02 suficiente para limitar el diálogo.

No toda conversación congela animación, tarea o World State.

---

# 4. Atención

DIAL02 normalmente necesita atención suficiente de los participantes.

ATTN determina:

- foco;
- distracción;
- interrupción;
- atención dividida.

Una persona puede seguir oyendo parcialmente mientras hace otra cosa.

---

# 5. Conocimiento

La conversación solo usa información que el NPC posee.

K, MEM, CRED y EXP continúan limitando:

- qué sabe;
- qué recuerda;
- qué cree;
- qué espera.

DIAL no concede conocimiento nuevo por sí solo.

---

# 6. Lo que sabe y lo que cuenta

CONF, TRUST, REQ, VAL, personalidad y contexto pueden hacer que una persona:

- responda;
- responda parcialmente;
- evite;
- calle;
- cambie de tema;
- rechace.

Participar en una conversación no obliga a contestar todas las preguntas.

---

# 7. Tema rechazado

DIAL04 se aplica al tema concreto.

La persona puede seguir conversando sobre otra cosa.

Rechazar un tema no equivale automáticamente a terminar toda interacción.

---

# 8. Conversación limitada

DIAL05 puede surgir porque:

- el NPC tiene trabajo;
- espera a alguien;
- debe marcharse;
- está cansado;
- existe otra prioridad.

La IA puede expresarlo de forma natural.

---

# 9. Iniciativa NPC

Un NPC puede:

- preguntar;
- pedir algo;
- cambiar de tema;
- mencionar un objetivo;
- proponer terminar.

No existe solo para responder al jugador.

---

# 10. Conversación y objetivos

GOAL puede influir en qué temas inicia o acepta el NPC.

La conversación puede ser una acción dentro de un objetivo.

Eso no convierte el objetivo automáticamente en quest.

---

# 11. Conversación y emoción

EMO, MOOD y STRS pueden cambiar:

- tono;
- paciencia;
- disposición;
- longitud de respuesta.

No dictan todas las palabras.

---

# 12. IA

La IA interpreta el diálogo dentro de DIAL.

No controla:

- posición;
- acceso;
- transferencia;
- resultados materiales;
- estado final de acciones.

Las acciones propuestas vuelven al motor para validación.

---

## Regla final

**Hablar con alguien en Treskal es ocupar parte de su atención y de su tiempo; el NPC puede participar sin dejar de tener trabajo, límites, prioridades y voluntad propia.**
