# Treskal — palabra dada, compromisos y honor social v0.1

## Estado

**CANON URBANO APROBADO — HONOR VALRIK COMO MECÁNICA SOCIAL**

## Base cultural

En Valrik, dar la palabra implica un compromiso de gran peso moral.

Cumplir lo prometido fortalece reputación.

Faltar deliberadamente a la palabra puede dañarla gravemente.

La palabra dada **no sustituye a la Ley del Rey**.

---

# 1. Compromiso persistente

Una promesa relevante puede materializarse como un compromiso persistente.

Campos mínimos:

- pledge_id;
- promisor_ref;
- recipient_ref;
- content;
- created_time;
- deadline_if_any;
- conditions_if_any;
- witnesses_if_any;
- state;
- known_by;
- outcome;
- explanation_if_breached.

---

# 2. Estados

## offered

La persona ha ofrecido comprometerse, pero todavía no existe aceptación suficiente.

## active

La palabra ha sido dada y el compromiso está vigente.

## fulfilled

Se cumplió de forma suficiente.

## fulfilled_late

Se cumplió, pero fuera de plazo.

## impossible

Cumplir se volvió objetivamente imposible.

## released

La persona receptora liberó al prometiente del compromiso.

## breached

No se cumplió sin una justificación aceptada.

## disputed

Existe desacuerdo real sobre:

- qué se prometió;
- plazo;
- condiciones;
- cumplimiento.

---

# 3. No toda frase es una promesa

El sistema debe distinguir entre:

- intención;
- posibilidad;
- cortesía;
- negociación;
- palabra formal o claramente comprometida.

Ejemplos:

“intentaré traerlo” no equivale necesariamente a:

“te doy mi palabra de que lo tendrás mañana”.

La IA no debe convertir automáticamente cualquier futuro verbal en pledge.

---

# 4. Contenido claro

Un compromiso necesita contenido razonablemente entendible.

Puede referirse a:

- entregar;
- pagar;
- acudir;
- guardar;
- reparar;
- devolver;
- no hacer;
- ayudar.

Los compromisos vagos pueden existir socialmente, pero deben registrar incertidumbre si se materializan.

---

# 5. Plazo

Puede ser:

- explícito;
- aproximado;
- condicionado;
- inexistente.

No se inventa una fecha si nadie la acordó.

---

# 6. Condiciones

Ejemplo:

“Si llega la madera antes del anochecer, tendré la pieza preparada.”

Si la condición no se cumple, no debe marcarse automáticamente como ruptura.

---

# 7. Testigos

Una promesa puede ser:

- privada;
- presenciada;
- conocida después por terceros.

Los testigos afectan:

- credibilidad;
- propagación;
- reputación.

No transforman el compromiso en ley automática.

---

# 8. Cumplimiento

Cumplir puede afectar positivamente:

- confianza personal;
- reputación familiar;
- profesional;
- comercial.

El efecto depende de:

- importancia;
- dificultad;
- quién lo sabe;
- historial.

No existe bonificación global universal.

---

# 9. Incumplimiento

Debe distinguirse:

## deliberado

La persona podía cumplir y decide no hacerlo.

## negligente

No actuó con cuidado razonable.

## inevitable

Una causa real impidió cumplimiento.

## ambiguo

No está claro qué ocurrió.

La cultura Valrik juzga especialmente mal el incumplimiento deliberado de la palabra.

---

# 10. Causa externa

Un evento puede impedir cumplimiento:

- temporal;
- accidente;
- enfermedad;
- muerte;
- ruta bloqueada;
- robo;
- incendio.

El World State debe conservar la causa.

Eso permite que otros NPC valoren si la explicación es creíble.

---

# 11. Explicación

Una persona puede explicar el incumplimiento.

La reacción depende de:

- relación;
- evidencia;
- reputación;
- historial;
- importancia.

La explicación no borra automáticamente el daño.

---

# 12. Mentira sobre cumplimiento

Alguien puede afirmar:

“ya lo hice”.

La afirmación no cambia el estado del pledge.

El motor comprueba el hecho real.

---

# 13. Pledge comercial

Puede coexistir con:

- encargo;
- pago;
- entrega.

La palabra dada puede elevar el peso social de un acuerdo.

No sustituye el futuro sistema jurídico contractual.

---

# 14. Pledge familiar

Puede tener enorme peso dentro de hogar o familia.

Su ruptura puede afectar:

- relación;
- confianza;
- reputación familiar.

---

# 15. Pledge profesional

Puede afectar:

- clientes;
- recomendaciones;
- maestros;
- aprendices;
- proveedores.

Especialmente en un territorio donde la reputación personal importa.

---

# 16. Pledge institucional

Un funcionario o representante puede dar una palabra personal o funcional.

No debe confundirse con:

- orden oficial;
- resolución judicial;
- autorización formal.

---

# 17. Muerte del prometiente

Si una persona muere:

el compromiso no se transfiere automáticamente a familia o negocio.

Puede quedar:

- imposible;
- asumido voluntariamente por otro;
- sujeto a futura regla legal si corresponde.

---

# 18. Memoria

Los pledges relevantes deben persistir como memoria fuerte en quienes participaron.

Un compromiso trivial y cumplido hace años puede reducir relevancia narrativa sin desaparecer del historial técnico si todavía importa.

---

# 19. IA

La IA de diálogo puede recibir:

- pledges activos relevantes;
- estado;
- memoria;
- explicación;
- conocimiento.

No decide por sí sola que una promesa se cumplió.

---

## Regla final

**En Treskal la palabra tiene peso porque la gente recuerda quién la dio y qué hizo después; el honor nace de hechos, no de una barra abstracta.**
