# Treskal — modelo de población NPC v0.1

## Estado

**DISEÑO DE GAMEPLAY APROBADO — POBLACIÓN URBANA PERSISTENTE**

## Objetivo

Permitir una ciudad de **12.000–18.000 residentes** sin exigir simulación completa y continua de miles de NPC.

---

# 1. Principio rector

Los habitantes de Treskal deben parecer personas que:

- viven en algún lugar;
- pertenecen a un hogar;
- trabajan o cumplen una función;
- conocen parte de la ciudad;
- mantienen relaciones;
- siguen rutinas;
- pueden cambiar por eventos.

La simulación técnica puede usar niveles de detalle, pero el mundo no debe contradecir esa realidad.

---

# 2. Tres niveles de identidad

## Nivel A — NPC autorales

Personajes definidos manualmente por:

- historia;
- misión;
- familia;
- institución;
- lore.

Tienen identidad completa desde el inicio.

Nunca deben ser sustituidos o alterados por generación procedural.

## Nivel B — residentes persistentes generados

Habitantes creados proceduralmente a partir de:

- hogar;
- edad;
- profesión;
- sector;
- relaciones;
- seed estable.

Cuando se materializan como persona concreta reciben:

- ID estable;
- nombre;
- apariencia;
- hogar;
- trabajo;
- relaciones;
- conocimientos;
- rasgos necesarios.

Persisten desde ese momento.

## Nivel C — población latente

Representa habitantes que existen estadísticamente en la ciudad pero todavía no necesitan identidad completa.

Se conserva suficiente información para mantener:

- número de residentes;
- hogares;
- ocupaciones;
- capacidad laboral;
- distribución por sectores.

Cuando uno de estos habitantes debe entrar en interacción significativa, se **promociona a Nivel B** mediante generación determinista.

---

# 3. Promoción irreversible

Una vez un residente latente recibe identidad concreta:

- no se rerollea;
- no cambia de nombre;
- no cambia de familia arbitrariamente;
- no cambia de profesión sin evento;
- no vuelve a ser anónimo.

El World State conserva la promoción.

---

# 4. Identidad técnica

Cada NPC persistente debe disponer de:

- `npc_id`;
- `origin_seed`;
- `household_id`;
- `home_location_id`;
- `occupation_id` cuando proceda;
- `workplace_id` cuando proceda;
- `relationship_refs`;
- `status`.

El nombre visible no es el ID.

---

# 5. Hogares antes que peatones

La población se estructura primero en hogares.

Cada hogar determina:

- residentes;
- vivienda;
- economía doméstica;
- posibles vínculos de oficio;
- familiares;
- dependientes.

No se generan peatones independientes y después se intenta inventar dónde viven.

---

# 6. Trabajo

Los adultos pueden estar vinculados a:

- taller;
- comercio;
- puerto;
- mercado;
- administración;
- guardia;
- Astilleros Reales;
- transporte;
- servicios;
- hogar;
- trabajo temporal.

No todos los adultos necesitan empleo asalariado moderno.

Puede existir:

- trabajo familiar;
- aprendizaje;
- ayuda doméstica;
- actividad ocasional;
- trabajo por encargo.

---

# 7. Niños

Los niños pertenecen a hogares concretos.

Pueden:

- ayudar;
- aprender;
- hacer recados;
- acompañar;
- jugar.

No se generan como fuerza laboral adulta por defecto.

---

# 8. Ancianos

Los mayores pueden conservar:

- trabajo parcial;
- experiencia;
- enseñanza;
- administración doméstica;
- papel social.

No se retiran automáticamente de toda actividad.

---

# 9. Visitantes

Los visitantes no se cuentan como residentes.

Pueden proceder de:

- Aldeas;
- Pueblos;
- Villas;
- otros territorios;
- barcos.

Necesitan:

- origen;
- motivo;
- duración estimada;
- alojamiento o punto de actividad;
- estado de salida.

Un visitante puede convertirse en residente por un cambio real de World State.

---

# 10. Población visible

La cantidad de NPC visibles se decide por:

- sector;
- hora;
- clima;
- mercado;
- puerto;
- evento;
- rendimiento.

No por porcentaje fijo de la población total.

Una calle tranquila no debe llenarse solo porque la ciudad tenga 15.000 habitantes.

---

# 11. Muerte y cambio

Un NPC persistente puede:

- morir;
- trasladarse;
- cambiar de oficio;
- formar familia;
- abandonar la ciudad;
- quedar herido;
- perder negocio;
- prosperar.

Esos cambios pertenecen al World State.

No se corrigen automáticamente para volver al estado inicial.

---

# 12. Ausencia

Si un NPC no está donde el jugador espera, debe existir una explicación compatible con:

- horario;
- trabajo;
- visita;
- clima;
- evento;
- enfermedad;
- viaje.

No debe teletransportarse al mostrador solo porque el jugador entra.

---

## Regla final

**La ciudad puede simular menos personas de las que existen, pero nunca debe fingir que una persona conocida deja de existir cuando deja de ser necesaria para la escena.**
