# Treskal — validación de salida IA y mutación de estado v0.1

## Estado

**DISEÑO DE IA APROBADO — CONTROL POSTERIOR A GENERACIÓN**

## Objetivo

Evitar que una respuesta lingüísticamente convincente rompa el canon o el World State.

---

# 1. Tipos de salida

La IA debe distinguir conceptualmente:

## Texto

Lo que se muestra o dice.

## Intención

Lo que NPC quiere hacer.

## Propuesta de acción

Acción que requiere validación del motor.

## Propuesta de hecho

Información nueva que no debe convertirse en verdad automáticamente.

---

# 2. Texto descriptivo

Debe validarse contra:

- contexto autorizado;
- estado visible;
- canon;
- continuidad.

Si contiene un hecho oculto no autorizado:

- se rechaza;
- se regenera;
- o se elimina el fragmento.

No se añade el hecho al conocimiento del jugador.

---

# 3. Diálogo

Debe comprobar:

- conocimiento disponible;
- secreto;
- personalidad;
- relación;
- contradicciones.

Un NPC puede mentir, pero la mentira debe quedar identificada como afirmación del NPC, no como verdad del mundo.

---

# 4. Acción

Ejemplo:

“te entrega la llave”.

Antes de ocurrir, el motor debe comprobar:

- ¿posee la llave?;
- ¿puede entregarla?;
- ¿quiere hacerlo?;
- ¿está físicamente allí?;
- ¿existe restricción?

Solo después actualiza inventarios y World State.

---

# 5. Movimiento

La IA no teletransporta.

Si un NPC decide ir a La Casa:

- crea intención/ruta;
- grafo urbano calcula recorrido;
- tiempo avanza;
- bloqueos pueden afectar;
- posición se actualiza.

---

# 6. Creación de entidades

Una mención casual no crea:

- nueva tienda;
- nuevo hermano;
- barco;
- cargo;
- calle.

Las entidades persistentes deben ser creadas por sistemas autorizados o proceso autoral.

---

# 7. Hechos efímeros

Sí pueden existir detalles no persistentes cuando no contradicen nada y no alteran el mundo.

Ejemplos:

- tono de voz;
- gesto;
- pausa;
- formulación verbal.

No necesitan registro completo.

---

# 8. Error de IA

Si la IA contradice el contexto:

- el World State no cambia;
- la salida se corrige/regenera;
- no se “arregla” el mundo para que la IA tenga razón.

---

# 9. Registro

Para depuración puede conservarse:

- contexto enviado;
- modelo/proveedor;
- salida;
- validación;
- corrección;
- hechos aceptados;
- acciones aplicadas.

Esto será especialmente útil en las pruebas comparativas de diálogos.

---

# 10. Proveedores de IA

El contrato debe ser independiente de:

- OpenAI;
- Gemini;
- Mistral;
- otros modelos.

Todos reciben el mismo conjunto semántico de contexto para poder comparar calidad.

---

# 11. Tests comparativos

Las pruebas deben usar exactamente:

- mismo NPC;
- misma escena;
- mismo conocimiento;
- mismos secretos;
- misma memoria;
- misma pregunta;
- mismo World State visible.

Se compara:

- personalidad;
- subtexto;
- coherencia;
- memoria;
- mentira;
- conocimiento limitado;
- naturalidad;
- disciplina ante secretos.

---

## Regla final

**Una buena frase de la IA nunca tiene autoridad suficiente para reescribir la realidad del juego.**
