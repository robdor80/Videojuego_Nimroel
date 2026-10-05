# Treskal — regalos, obsequios y transferencia social v0.1

> **MIGRADO A NIMROEL CORE — documentación derivada.** La autoridad normativa de GIFT reside en `Worldbuilding/Sistemas/Nimroel Core/05_Relaciones_sociales/regalos_significado_social_v0.1.md`. Este archivo conserva ejemplos de Treskal; ante conflicto prevalece el Core.

## Estado

**DISEÑO SOCIAL/JUGABLE APROBADO — UN REGALO ES UN OBJETO REAL CON SIGNIFICADO CONTEXTUAL**

## Objetivo

Definir regalos entre NPC y jugador sin convertirlos en:

- botón de afinidad;
- compra de romance;
- duplicación de inventario;
- acceso mágico a gustos ocultos.

---

# 1. Un regalo necesita existir

Para regalar algo:

- el objeto o lote debe existir;
- quien lo ofrece debe poseerlo o tener autoridad para transferirlo;
- el objeto debe poder transferirse.

OWN valida el cambio de propiedad.

Decir “te regalo esto” no crea un objeto.

---

# 2. Estados operativos

## GIFT01 — gift_offered

Existe una oferta real de entrega.

## GIFT02 — gift_accepted

La persona acepta recibirlo.

## GIFT03 — gift_refused

La persona no lo acepta.

## GIFT04 — transfer_completed

OWN ha completado la transferencia.

## GIFT05 — gift_retained_with_meaning

El objeto permanece vinculado a una memoria o significado social relevante.

## GIFT06 — gift_returned_or_relinquished

El objeto fue devuelto, rechazado posteriormente o abandonado de forma válida.

## GIFT07 — gift_disputed_or_misinterpreted

Existe desacuerdo sobre intención, significado o legitimidad de la entrega.

---

# 3. Oferta y transferencia son distintas

Aceptar verbalmente puede preceder a la entrega física.

La transferencia real solo ocurre cuando el sistema de objetos puede completarla.

Si el objeto:

- se pierde;
- es robado;
- no pertenece al oferente;
- deja de existir

el regalo no se completa mágicamente.

---

# 4. Rechazar es válido

Un NPC puede rechazar un regalo porque:

- no lo desea;
- no confía en la intención;
- considera excesivo el valor;
- el contexto le incomoda;
- no quiere deber nada;
- la relación no lo justifica.

Rechazar no implica automáticamente hostilidad.

---

# 5. Regalo y relación

Un regalo puede ser:

- amable;
- significativo;
- íntimo;
- cotidiano;
- incómodo;
- sospechoso;
- inapropiado.

La interpretación depende de la relación y la situación.

---

# 6. No compra amistad

Entregar objetos repetidamente no obliga a crear FRI.

Una persona puede:

- agradecer;
- aceptar;
- rechazar;
- desconfiar;
- sentirse incómoda.

El valor económico no determina amistad.

---

# 7. No compra romance

Un regalo puede formar parte de un cortejo si el vínculo ya lo hace plausible.

No genera:

- atracción;
- reciprocidad;
- pareja

por superar un valor determinado.

AFF mantiene su autoridad.

---

# 8. Preferencias

Un regalo puede encajar mejor con la persona si quien regala conoce realmente sus gustos.

Ese conocimiento puede proceder de:

- conversación;
- convivencia;
- observación;
- amistad;
- información compartida.

PREF oculto no se expone como tabla mágica al jugador.

---

# 9. Regalo equivocado

Un regalo poco adecuado no tiene por qué provocar una penalización.

Puede ser:

- neutro;
- divertido;
- extraño;
- incómodo.

La reacción depende de personalidad, relación e intención percibida.

---

# 10. Precio y significado

Un objeto caro no es automáticamente más significativo.

Un objeto sencillo puede tener enorme valor personal si está ligado a:

- memoria;
- esfuerzo;
- necesidad;
- procedencia;
- relación.

La economía y el significado social son dimensiones distintas.

---

# 11. Favor y regalo

Un regalo puede también funcionar como FAV cuando resuelve una necesidad real.

Ejemplo conceptual:

entregar comida a un hogar con escasez puede ser simultáneamente:

- transferencia OWN;
- ayuda FAV;
- hecho social recordable.

Los sistemas no se sustituyen.

---

# 12. Préstamo

Un préstamo no es un regalo.

Si se espera devolución del mismo objeto:

OWN02 y el sistema de préstamo son la autoridad.

---

# 13. Pago

Un pago por trabajo o mercancía no es un regalo por defecto.

Puede existir un obsequio adicional, pero debe distinguirse de la transacción económica.

---

# 14. Memoria

Un regalo importante puede persistir como memoria:

- quién lo dio;
- cuándo;
- por qué;
- qué ocurrió alrededor.

No todos los objetos recibidos requieren memoria fuerte.

---

## Regla final

**En Treskal un regalo importa por quién lo da, qué entrega realmente y lo que significa para quien lo recibe; su precio no compra una relación.**
