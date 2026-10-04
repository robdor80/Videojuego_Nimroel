# Treskal — contrato de contexto del narrador y Percepción v0.1

## Estado

**DISEÑO DE IA APROBADO — MODO MÁSTER / OFF STORY**

## Objetivo

Garantizar que la IA narrativa describa únicamente lo que el jugador puede percibir o lo que una mecánica haya autorizado descubrir.

La IA no recibe libertad para inspeccionar el World State oculto y decidir qué revelar.

---

# 1. Separación fundamental

El sistema distingue:

## Verdad del mundo

Todo lo que realmente existe o ha ocurrido.

## Contexto perceptible

La parte de esa verdad que el personaje jugador puede percibir ahora.

## Contexto descubierto

Información adicional que una acción o tirada válida ha permitido conocer.

## Narración

La formulación lingüística de los datos anteriores.

La narración **no crea la verdad**.

---

# 2. Canal normal

Por defecto:

**World State → filtro de percepción → contexto autorizado → IA narrativa → texto**

La IA narrativa no necesita recibir:

- secretos;
- contenidos ocultos;
- identidades desconocidas;
- intenciones internas;
- objetos tras superficies opacas;
- trampas no detectadas;
- información de habitaciones no observables.

---

# 3. Perceptible sin tirada

Puede incluir, según contexto:

- formas visibles;
- personas visibles;
- actividad;
- sonidos audibles;
- olores;
- temperatura percibida;
- lluvia;
- barro;
- luz;
- humo visible;
- objetos expuestos;
- señales evidentes.

Siempre condicionado por:

- distancia;
- iluminación;
- clima;
- obstáculos;
- orientación;
- ruido;
- estado ambiental.

---

# 4. Información oculta

No debe enviarse a la IA narrativa normal.

Ejemplos:

- una bolsa escondida bajo tablas;
- contenido de una caja cerrada;
- identidad real de un desconocido;
- intención de un NPC;
- conversación inaudible;
- persona detrás de una puerta;
- documento dentro de un archivo cerrado;
- trampa no detectada.

Incluso decir:

“no ves la trampa escondida”

sería una filtración.

---

# 5. Acción de fijarse

Cuando el jugador expresa intención de examinar algo concreto, el sistema puede activar una resolución de **Percepción** u otra mecánica apropiada.

Secuencia:

1. jugador declara foco;
2. motor identifica objetivo;
3. motor resuelve mecánica;
4. motor calcula hechos descubiertos;
5. solo esos hechos se añaden al contexto narrativo;
6. IA describe el resultado.

La IA no realiza la tirada de forma implícita por su cuenta.

---

# 6. Resultado de Percepción

La tirada no devuelve “éxito narrativo” genérico.

Debe devolver un conjunto explícito de hechos autorizados.

Ejemplo conceptual:

- arañazos recientes en cerradura;
- barro húmedo en el umbral;
- olor tenue a aceite;
- ninguna otra anomalía perceptible.

La IA puede redactarlos con naturalidad.

No puede añadir:

“alguien entró anoche”

si ese hecho no fue autorizado como inferencia.

---

# 7. Inferencia

Debe separarse:

## Hecho percibido

“Hay arañazos recientes.”

## Inferencia autorizada

“Parecen compatibles con manipulación reciente.”

## Conclusión oculta

“Fue X quien forzó la cerradura.”

La última solo puede aparecer si el sistema dispone de una vía real de conocimiento.

---

# 8. Estado ambiental

El contexto debe usar el estado ambiental actual.

Ejemplo:

si la calle sigue embarrada por lluvia de días anteriores, la IA describe barro aunque ahora no llueva.

No debe recuperar la descripción genérica de “calle seca” por identidad base del lugar.

---

# 9. Continuidad

El narrador debe recibir cambios persistentes relevantes:

- puerta rota;
- puesto cerrado;
- edificio quemado;
- calle bloqueada;
- mercancía retirada;
- persona ausente.

No debe describir la versión inicial del lugar si el World State cambió.

---

# 10. Descripciones no omniscientes

Evitar formulaciones como:

- “sin que lo sepas…”;
- “ignorando que…”;
- “oculto bajo…”;
- “el hombre, que en realidad es…”;
- “nadie sospecha que…”.

Ese lenguaje pertenece a narrador omnisciente y viola Off Story.

---

# 11. Incertidumbre perceptiva

Cuando algo se percibe mal, la IA debe expresar incertidumbre.

Ejemplos:

- “parece”;
- “dirías”;
- “no distingues bien”;
- “desde aquí no puedes asegurarlo”.

No debe resolver la incertidumbre con información del estado real oculto.

---

# 12. Preguntas directas del jugador

Si el jugador pregunta:

“¿qué hay dentro de esa caja?”

y la caja sigue cerrada, el narrador no responde con su contenido.

Debe responder desde lo disponible:

- aspecto exterior;
- peso si se manipula;
- sonido si se mueve;
- olor si existe;
- imposibilidad de saber más todavía.

---

# 13. Ámbito de escena

La IA recibe solo la porción del mundo necesaria para la escena.

No se entrega el estado completo de Treskal “por si acaso”.

Esto reduce:

- filtraciones;
- contradicciones;
- coste de contexto.

---

# 14. Autoridad

La salida narrativa describe.

No puede por sí sola:

- crear un NPC persistente;
- mover un objeto;
- abrir una puerta;
- cambiar stock;
- matar a alguien;
- registrar un crimen;
- alterar clima.

Los cambios deben pasar por el sistema.

---

## Regla final

**La IA narra lo que el juego ha permitido conocer; nunca utiliza lo que sabe el motor para hacer al jugador omnisciente.**
