# Treskal — desarrollo infantil, autonomía y supervisión v0.1

## Estado

**DISEÑO SOCIAL/JUGABLE APROBADO — CRECER SIN SALTOS DE EDAD ARBITRARIOS**

## Objetivo

Definir cómo un niño de Treskal pasa gradualmente de dependencia casi total a una autonomía creciente sin fijar todavía edades numéricas exactas.

La edad cronológica existirá en el futuro sistema de ciclo vital, pero este documento usa etapas funcionales para que el comportamiento dependa de capacidades reales y no de etiquetas rígidas.

---

# 1. Identidad continua

El niño conserva el mismo npc_id desde su nacimiento.

Crecer no regenera:

- personalidad;
- familia;
- memoria;
- amistades;
- hogar;
- historia;
- procedencia.

Las etapas cambian capacidades y necesidades, no la identidad.

---

# 2. Estados funcionales

## CHD01 — early_dependence

Dependencia muy alta.

La movilidad y autonomía son mínimas.

DEP01/CARE dominan la rutina.

## CHD02 — mobile_dependence

Existe movilidad creciente, pero requiere vigilancia cercana y entorno compatible.

## CHD03 — supervised_childhood

Puede participar en juego, aprendizaje doméstico y desplazamientos cortos bajo supervisión adecuada.

## CHD04 — growing_autonomy

Puede asumir mayor autonomía cotidiana en espacios conocidos y de riesgo bajo.

## CHD05 — guided_contribution

Puede realizar tareas sencillas y aprendizaje práctico guiado de forma más consistente.

No equivale a trabajo adulto.

## CHD06 — transition_to_youth

Etapa de transición hacia mayor independencia, aprendizaje profesional más serio y futuras responsabilidades.

No fija mayoría de edad.

---

# 3. Sin edades inventadas

Este documento no establece que CHD03 empiece a los X años ni que CHD06 termine a los Y.

Los umbrales pertenecen al futuro sistema de ciclo vital.

La simulación debe respetar ese sistema cuando exista.

---

# 4. Supervisión

La necesidad de supervisión depende de:

- etapa;
- salud;
- lugar;
- tráfico;
- agua;
- fuego;
- herramientas;
- animales;
- hora;
- eventos activos.

Un niño no recibe la misma libertad en un patio doméstico que junto a un muelle en plena descarga.

---

# 5. Movilidad urbana

La autonomía espacial puede crecer desde:

- interior del hogar;
- patio;
- entorno inmediato;
- calle conocida;
- plaza cercana;
- rutas sencillas;
- desplazamientos mayores.

No se desbloquea toda Treskal de golpe.

---

# 6. Conocimiento de rutas

Los niños pueden aprender:

- dónde viven familiares;
- plaza cercana;
- mercado;
- taller familiar;
- casa de amistades;
- referencias del barrio.

WAYFINDING y conocimiento siguen siendo adquiridos.

Un niño no posee mapa mental completo de la ciudad por ser residente.

---

# 7. Riesgo

La infancia no convierte a un NPC en inmune a:

- accidentes;
- fuego;
- tráfico;
- agua;
- enfermedades;
- violencia del mundo.

Pero el juego tampoco debe generar peligro constante solo para producir drama.

La exposición depende de situaciones reales.

---

# 8. Cuidado variable

La intensidad de DEP01 suele cambiar con el crecimiento.

No tiene por qué disminuir siempre de forma lineal.

Enfermedad, lesión u otra necesidad pueden aumentar temporal o permanentemente CARE.

---

# 9. Juego

LEIS05 es una parte normal de la infancia.

El juego puede:

- desarrollar habilidad;
- crear amistades;
- producir rivalidad;
- enseñar reglas sociales;
- explorar el entorno.

No es tiempo vacío sin efecto.

---

# 10. Pares

Las relaciones entre niños pueden persistir y evolucionar.

Pueden existir:

- amistad;
- familiaridad;
- rivalidad;
- conflicto;
- reconciliación.

No se aplican mecánicas románticas durante estas etapas infantiles.

---

# 11. Conversación e IA

Un niño puede ser:

- tímido;
- curioso;
- observador;
- impulsivo;
- serio;
- ingenioso.

Ser niño no significa hablar de forma caricaturesca.

Pero la IA debe respetar:

- desarrollo;
- vocabulario plausible;
- conocimiento real;
- experiencia;
- personalidad.

No puede usar al niño como portavoz omnisciente del lore.

---

# 12. Apariencia y crecimiento

El crecimiento puede requerir cambios visuales progresivos.

La apariencia debe conservar continuidad reconocible cuando el NPC ya está materializado.

No se genera una cara nueva sin relación con su identidad previa.

---

# 13. Ropa y objetos

Crecer puede volver inadecuados:

- prendas;
- calzado;
- mobiliario;
- herramientas adaptadas a tamaño.

GAR, OWN y economía pueden absorber esas necesidades cuando sean relevantes.

---

# 14. LOD

En LOD bajo se conserva al menos:

- etapa CHD;
- hogar;
- CARE;
- relaciones relevantes;
- aprendizaje;
- salud;
- progresión temporal.

Al volver el jugador, el niño aparece en una situación coherente con el tiempo realmente transcurrido.

---

## Regla final

**En Treskal la infancia es un proceso continuo: un niño aprende a moverse, conocer, ayudar y decidir poco a poco, sin convertirse de repente en un adulto porque el guion necesite otro trabajador.**
