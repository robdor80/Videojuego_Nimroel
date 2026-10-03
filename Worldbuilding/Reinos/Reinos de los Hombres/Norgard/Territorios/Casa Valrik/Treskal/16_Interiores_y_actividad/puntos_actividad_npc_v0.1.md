# Treskal — puntos de actividad NPC v0.1

## Estado

**DISEÑO DE GAMEPLAY APROBADO — ANCLAJES DE COMPORTAMIENTO**

## Objetivo

Permitir rutinas creíbles sin obligar a programar manualmente cada acción de cada NPC.

---

# 1. Activity Anchors

Un punto de actividad es una posición funcional del mundo que permite acciones coherentes.

Ejemplos:

- banco de trabajo;
- puesto de mercado;
- mesa de taberna;
- cama;
- pozo;
- muelle;
- punto de carga;
- puesto de guardia;
- zona de juego infantil;
- escritorio;
- fogón.

---

# 2. Tipos A

## A01 — Hogar

Acciones:

- dormir;
- comer;
- conversar;
- tareas domésticas;
- descanso.

## A02 — Trabajo artesanal

- fabricar;
- reparar;
- preparar material;
- enseñar aprendiz.

## A03 — Comercio

- atender;
- vender;
- reponer;
- negociar;
- registrar encargo.

## A04 — Mercado

- montar puesto;
- vender;
- comprar;
- cargar;
- desmontar.

## A05 — Puerto

- descargar;
- reparar;
- preparar redes;
- amarrar;
- mover mercancía.

## A06 — Logística

- cargar carro;
- apilar;
- clasificar;
- mover mercancía.

## A07 — Administración

- escribir;
- registrar;
- recibir;
- archivar.

## A08 — Guardia

- vigilar;
- patrullar;
- recibir denuncia;
- custodiar acceso.

## A09 — Social

- beber;
- conversar;
- esperar;
- observar;
- jugar.

## A10 — Agua

- recoger agua;
- limpiar;
- abastecer hogar o negocio.

## A11 — Alimentación

- cocinar;
- servir;
- comer.

## A12 — Descanso laboral

- sentarse;
- comer;
- hablar;
- esperar.

---

# 3. Anclas no exclusivas

Un mismo espacio puede contener varias anclas.

Ejemplo:

una taberna puede tener:

- A03 comercio;
- A09 social;
- A11 alimentación;
- A12 descanso.

---

# 4. Ocupación

Las anclas tienen capacidad.

No pueden ser usadas simultáneamente por una cantidad arbitraria de NPC.

La densidad debe respetar:

- tamaño;
- mobiliario;
- hora;
- actividad.

---

# 5. Elección

Un NPC elige actividad según:

- rutina;
- profesión;
- necesidad;
- relaciones;
- horario;
- clima;
- evento;
- disponibilidad del ancla.

No selecciona una animación aleatoria sin contexto.

---

# 6. Sustitución

Si una ancla está ocupada o inaccesible, el NPC puede:

- esperar;
- elegir alternativa;
- cambiar de tarea;
- marcharse.

Esto evita acumulaciones absurdas.

---

# 7. Anclas y diálogo

La actividad debe informar al diálogo.

Ejemplo:

un carpintero trabajando puede:

- responder brevemente;
- pedir que esperes;
- seguir trabajando;
- interrumpir si el asunto es importante.

No todo NPC abandona su tarea para mirar al jugador.

---

# 8. Anclas y eventos

World State puede desactivar o modificar anclas.

Ejemplos:

- incendio bloquea taller;
- lluvia vacía parte del mercado;
- temporal reduce muelles;
- juicio aumenta espera en T06;
- mercado de ganado activa más anclas en T10.

---

# 9. Persistencia de ocupación relevante

No es necesario guardar cada segundo de animación.

Sí deben persistir:

- trabajo asignado;
- horario;
- evento;
- posición lógica cuando sea importante;
- estado de viaje;
- cierre o daño de lugar.

---

# 10. Población latente

Los NPC de Nivel C pueden resolverse agregadamente mediante demanda de anclas.

Ejemplo:

“actividad de mercado requiere 80–120 personas visibles/agregadas” sin materializar identidad completa de todas.

Si el jugador interactúa con una persona concreta, se promociona a Nivel B.

---

# 11. Rendimiento

La simulación puede reducir:

- animación;
- frecuencia de actualización;
- precisión de recorrido

según distancia del jugador.

Nunca debe cambiar:

- identidad;
- hogar;
- trabajo;
- estado persistente;
- relaciones relevantes.

---

## Regla final

**Las rutinas de Treskal deben parecer conducta humana porque los NPC eligen actividades posibles en lugares reales, no porque repitan un guion horario rígido.**
