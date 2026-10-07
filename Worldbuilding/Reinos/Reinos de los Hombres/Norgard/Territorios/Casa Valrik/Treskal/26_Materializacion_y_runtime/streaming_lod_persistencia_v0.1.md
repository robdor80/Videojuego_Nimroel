# Treskal — streaming, LOD lógico y persistencia fuera de escena v0.1

## Estado

**DISEÑO TÉCNICO-CONCEPTUAL APROBADO**

## Objetivo

Simular una ciudad de 12.000–18.000 residentes sin mantener miles de NPC, interiores y objetos a máxima resolución de forma continua.

---

# 1. Tres niveles lógicos

## LOD-L — agregado

Mantiene:

- conteos;
- hogares;
- capacidad laboral;
- stock agregado;
- actividad;
- estado de viaje;
- eventos;
- daños importantes.

No necesita:

- animación;
- pathfinding detallado;
- diálogo.

## LOD-M — simulado

Mantiene:

- NPC o grupos relevantes;
- rutinas;
- rutas aproximadas;
- apertura de negocios;
- ocupación;
- stock;
- eventos locales.

## LOD-H — escena

Mantiene:

- individuos;
- posiciones precisas;
- interiores;
- percepción;
- diálogo;
- objetos relevantes;
- interacción.

---

# 2. La distancia no es el único criterio

El nivel depende de:

- proximidad al jugador;
- relevancia narrativa;
- evento;
- misión;
- peligro;
- conversación;
- seguimiento;
- persistencia necesaria.

Un NPC lejano importante puede conservar simulación M.

---

# 3. Promoción de LOD

Cuando una entidad sube de nivel:

- no se regenera;
- se materializa desde su estado actual;
- respeta tiempo transcurrido;
- respeta ruta, daño, inventario y relaciones.

Ejemplo:

un comerciante viajando en LOD-L no reaparece en su tienda al cargar el barrio.

---

# 4. Descenso de LOD

Al abandonar una zona:

se conservan hechos relevantes y se simplifican:

- posiciones;
- animaciones;
- acciones triviales.

No se borran:

- identidad;
- propiedad;
- muerte;
- lesión relevante;
- promesa;
- stock significativo;
- crimen;
- viaje;
- cambio de hogar;
- daño.

---

# 5. Resolución fuera de escena

El sistema puede avanzar mediante simulación agregada:

- producción;
- consumo;
- entregas;
- viajes;
- horarios;
- recuperación;
- reparación;
- eventos.

No necesita recrear cada paso físico.

---

# 6. Viaje fuera de escena

Debe conservar:

- origen;
- destino;
- ruta;
- hora de salida;
- progreso;
- incidencias.

Si el jugador intercepta el trayecto, el NPC se materializa en una posición compatible con el progreso real.

---

# 7. Negocios fuera de escena

Pueden:

- producir;
- vender agregado;
- recibir mercancía;
- cerrar;
- sufrir retraso.

La resolución debe respetar:

- horario;
- trabajadores;
- stock;
- demanda;
- World State.

---

# 8. Eventos críticos

Un evento crítico puede forzar aumento de simulación.

Ejemplos:

- incendio;
- combate;
- persecución;
- juicio relevante;
- accidente portuario.

Después puede volver a LOD inferior conservando consecuencias.

---

# 9. Histeresis

Para evitar cambios constantes al cruzar una frontera:

el sistema debe usar margen temporal/espacial antes de degradar o elevar repetidamente una zona.

No se fija todavía un valor numérico.

---

# 10. Interiores

Un interior no visible puede descargarse gráficamente.

Su estado lógico permanece:

- ocupantes;
- puertas;
- objetos persistentes;
- stock;
- daños;
- actividad.

---

# 11. Tiempo

El paso de tiempo debe ser coherente entre niveles.

No existe un “tiempo de fondo” distinto que produzca resultados incompatibles.

La precisión puede reducirse, pero no la causalidad.

---

# 12. Aleatoriedad

Los resultados agregados pueden usar aleatoriedad controlada.

Debe estar:

- seedada;
- acotada;
- condicionada por estado real.

No puede utilizarse para reescribir hechos ya materializados.

---

# 13. Carga de partida

Al cargar:

1. se restaura World State;
2. se reconstruye nivel lógico necesario;
3. se materializa escena;
4. se aplica continuidad ambiental;
5. se activa percepción/IA solo con contexto autorizado.

No se vuelve a generar la ciudad.

---

# 14. Guardado

Debe priorizar deltas y estado persistente frente a guardar cada detalle efímero.

Guardar:

- identidades;
- cambios;
- relaciones;
- stock relevante;
- eventos;
- ubicaciones lógicas;
- materializaciones.

No es necesario guardar cada animación o posición de cada transeúnte latente.

---

## Regla final

**Treskal puede simplificarse cuando nadie la mira, pero no puede cambiar de historia porque nadie la esté mirando.**


---

## Personalidad persistente y LOD

Para humanos de Norgard:

- `personality_seed` sobrevive a cualquier cambio de LOD;
- un perfil B/A resuelto conserva `personality_profile_id`;
- materializar o desmaterializar no rerollea PERS;
- la simulación off-screen puede usar una versión compacta del perfil;
- una promoción C→B conserva cualquier firma conductual previamente observada;
- B→A no genera una persona nueva.

La personalidad se comporta como identidad persistente, no como decoración de escena.
