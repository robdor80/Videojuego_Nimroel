# Treskal — temas, interrupción y cierre de conversación v0.1

> **MIGRADO A NIMROEL CORE — documentación derivada.** La autoridad normativa de DIAL reside en `Worldbuilding/Sistemas/Nimroel Core/01_Cognicion_y_conducta/dinamica_de_conversacion_v0.1.md`. Este archivo conserva explicación y ejemplos de Treskal; ante conflicto prevalece el Core.


## Estado

**DISEÑO DE WORLD STATE APROBADO — UNA CONVERSACIÓN PUEDE TERMINAR SIN QUE EL JUGADOR LO DECIDA**

## Objetivo

Definir continuidad temática, interrupciones y cierre natural de diálogo.

---

# 1. Tema activo

Una conversación puede mantener uno o varios temas relevantes.

El sistema no necesita persistir cada frase.

Puede conservar:

- tema;
- pregunta pendiente;
- petición;
- dato compartido;
- decisión;
- compromiso;
- conflicto.

---

# 2. Cambio de tema

Cualquiera de los participantes puede cambiar de tema.

Puede ocurrir por:

- asociación;
- objetivo;
- incomodidad;
- nueva información;
- interrupción;
- intento de evitar una cuestión.

El cambio no borra automáticamente el tema anterior.

---

# 3. Persistencia temática

Un asunto importante puede continuar en un encuentro posterior si:

- sigue pendiente;
- los participantes lo recuerdan;
- tiene relevancia.

MEM determina continuidad.

No existe memoria automática de cada línea pronunciada.

---

# 4. Interrupción

DIAL06 necesita causa.

Puede producirse por:

- cliente;
- compañero;
- incendio;
- mensaje;
- cuidado;
- trabajo;
- peligro;
- necesidad física;
- otra persona.

Una interrupción no equivale necesariamente a cierre definitivo.

---

# 5. Reanudación

Una conversación interrumpida puede:

- continuar inmediatamente;
- reanudarse después;
- quedar pendiente;
- perder relevancia.

No vuelve exactamente al mismo punto por obligación.

---

# 6. Cierre voluntario

DIAL07 permite al NPC indicar que quiere terminar.

Puede deberse a:

- falta de tiempo;
- cansancio;
- desinterés;
- incomodidad;
- obligación;
- conflicto;
- necesidad de privacidad.

No necesita hostilidad.

---

# 7. Ignorar el cierre

Si el jugador insiste tras un cierre claro:

puede provocar:

- REQ08;
- RIFT;
- menor TRUST;
- rechazo;
- intervención de autoridad si el contexto futuro lo justifica.

No fuerza la continuidad de la conversación.

---

# 8. Fin de conversación

DIAL08 puede terminar por:

- acuerdo;
- despedida;
- salida física;
- interrupción definitiva;
- negativa;
- emergencia;
- pérdida de posibilidad de oírse.

El motor registra consecuencias relevantes antes del cierre.

---

# 9. Privacidad

CONV sigue definiendo contexto de privacidad.

Terminar una conversación privada no vuelve público su contenido.

CONF conserva reglas de divulgación.

---

# 10. Frases importantes

Una conversación puede crear:

- STAT;
- REQ;
- PLEDGE;
- CONF;
- FAV;
- RIFT;
- conocimiento;
- MEM.

Solo cuando el contenido y el sistema correspondiente lo justifican.

---

# 11. Repetición de preguntas

Preguntar varias veces no garantiza respuesta distinta.

Puede cambiar si aparecen:

- nueva confianza;
- información;
- evidencia;
- estado emocional;
- contexto;
- permiso.

La repetición por sí sola no desbloquea contenido.

---

# 12. Offscreen

Conversaciones relevantes pueden ocurrir fuera de cámara solo si:

- los participantes podían encontrarse;
- existía tiempo;
- había motivo;
- el contenido derivado se resuelve mediante sistemas autorizados.

No se inventan diálogos completos invisibles para justificar cambios arbitrarios.

---

# 13. IA

La IA puede cerrar una conversación cuando el contexto lo sostenga.

No debe permanecer en bucle de respuestas ilimitadas si el NPC ya necesita irse.

---

## Regla final

**En Treskal una conversación tiene principio, continuidad y final porque ocurre dentro de una vida real; el jugador participa en ella, pero no posee su duración ni sus temas.**
