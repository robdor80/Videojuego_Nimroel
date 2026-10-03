# Treskal — conocimiento local, rutinas y memoria de NPC v0.1

## Estado

**DISEÑO DE GAMEPLAY APROBADO — INFORMACIÓN LIMITADA**

## Objetivo

Evitar NPC omniscientes y conectar diálogo con vida, profesión y relaciones reales.

---

# 1. Conocimiento por capas

Un NPC puede conocer información por:

- experiencia personal;
- hogar;
- profesión;
- sector;
- familia;
- amistades;
- reputación;
- noticias;
- acontecimientos presenciados.

No conoce automáticamente toda Treskal.

---

# 2. Conocimiento espacial

Un residente suele conocer mejor:

- su vivienda;
- entorno cercano;
- lugar de trabajo;
- rutas habituales;
- mercados que utiliza;
- tabernas o servicios frecuentes.

Puede conocer peor:

- sectores alejados;
- interior de Astilleros Reales;
- dependencias administrativas restringidas;
- hogares de desconocidos.

---

# 3. Conocimiento profesional

Ejemplos:

## Carpintero

Puede saber:

- quién vende determinada madera;
- reputación de otros artesanos;
- dónde conseguir herramientas;
- talleres importantes;
- encargos recientes conocidos.

## Pescador

Puede saber:

- estado reciente del mar;
- capturas;
- puerto;
- compradores;
- rumores de tripulaciones.

## Posadero

Puede saber:

- viajeros;
- rutas;
- rumores;
- comerciantes;
- personas que preguntaron por algo.

## Guardia

Puede saber:

- incidentes;
- zonas conflictivas;
- procedimientos;
- personas buscadas dentro de su ámbito.

No implica acceso automático a secretos institucionales.

---

# 4. Rumores

Un rumor debe tener:

- fuente;
- contenido;
- antigüedad;
- ámbito de difusión;
- fiabilidad o distorsión.

La IA puede expresarlo como rumor sin convertirlo en hecho verdadero.

---

# 5. Memoria de interacción

Cuando el jugador interactúa de forma significativa con un NPC persistente, el NPC puede registrar:

- encuentros;
- promesas;
- favores;
- conflictos;
- pagos;
- encargos;
- información compartida;
- reputación del jugador.

No todos los detalles necesitan memoria infinita.

Debe priorizarse lo socialmente relevante.

---

# 6. Palabra dada

En Valrik, una promesa importante puede adquirir peso especial.

Un NPC puede recordar:

- cumplimiento;
- incumplimiento;
- demora justificada;
- engaño.

Esto puede afectar:

- confianza;
- precios;
- recomendaciones;
- acceso a encargos;
- reputación familiar o profesional.

---

# 7. Rutina base

Cada NPC persistente debe disponer de una rutina base por:

- hogar;
- trabajo;
- franja horaria.

La rutina no es una vía férrea.

Puede modificarse por:

- clima;
- misión;
- enfermedad;
- evento;
- visita;
- trabajo excepcional;
- relaciones.

---

# 8. Prioridades

Cuando dos reglas compiten, la prioridad conceptual es:

1. evento crítico;
2. necesidad física o seguridad;
3. obligación laboral o institucional;
4. relación social importante;
5. rutina ordinaria.

---

# 9. Preguntar por personas

Un NPC puede responder de forma útil si:

- conoce a la persona;
- conoce el oficio;
- sabe dónde suele estar;
- ha oído algo reciente.

Si no sabe, debe poder decirlo.

No inventa una ubicación exacta.

---

# 10. Preguntar por servicios

La respuesta puede seguir:

`conocimiento propio → recomendación → rumor → no lo sé`

Ejemplo:

“Necesito un buen ebanista” no debería abrir un buscador mágico.

Puede llevar a:

- un taller conocido;
- una recomendación;
- una reputación;
- otro NPC que sabe más.

---

# 11. Información oculta

La IA de un NPC no puede revelar:

- secretos no conocidos;
- estado interno de otros NPC;
- contenido de edificios no visitados;
- hechos del World State fuera de su experiencia.

La respuesta debe limitarse al conocimiento real del NPC.

---

## Regla final

**Un NPC de Treskal sabe cosas porque vive allí, no porque el modelo de IA tenga acceso a todo el juego.**
