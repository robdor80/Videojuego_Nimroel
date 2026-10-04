# Treskal — ciclo de vida de eventos y causalidad urbana v0.1

## Estado

**DISEÑO DE WORLD STATE APROBADO — EVENTOS CAUSALES**

## Objetivo

Definir cómo nace, evoluciona y termina un evento urbano sin convertir Treskal en una secuencia de incidentes arbitrarios.

---

# 1. Diferencia entre estado y evento

Los IDs D01–D12 representan **tipos de estado dinámico**.

Un evento concreto es una instancia.

Ejemplo:

- D01 = temporal marítimo;
- EVT_... = el temporal concreto que afecta a Treskal durante una partida.

---

# 2. Ciclo de vida

Una instancia puede estar en:

## proposed

Existe una causa candidata, pero todavía no se ha confirmado el evento.

## scheduled

El evento está previsto por una causa real.

## triggered

Se cumplen condiciones de inicio.

## active

Produce efectos.

## resolving

La causa principal termina, pero quedan consecuencias inmediatas.

## resolved

El evento terminó; pueden quedar consecuencias persistentes.

## cancelled

La causa desapareció antes de iniciarse.

---

# 3. Fuentes de evento

Un evento puede proceder de:

## Sistema ambiental

- temporal;
- crecida;
- sequedad;
- incendio.

## World State económico

- stock crítico;
- convoy;
- retraso;
- llegada de mercante.

## Acción de NPC

- accidente;
- delito;
- disputa;
- decisión institucional.

## Acción del jugador

- incendio provocado;
- mercancía entregada;
- puerta abierta;
- denuncia;
- robo.

## Historia autoral

- evento narrativo escrito;
- misión;
- acontecimiento político.

## Consecuencia de otro evento

- temporal → retraso de barco;
- retraso → escasez;
- escasez → aumento de precio;
- incendio → desplazamiento de hogar.

---

# 4. Evento necesita causa

Toda instancia persistente debe poder responder:

- qué la originó;
- cuándo;
- dónde;
- qué afecta.

No se genera un “incendio aleatorio” únicamente porque hace tiempo que no ocurre nada.

---

# 5. Condiciones

Antes de activar un evento, el sistema puede comprobar:

- localización;
- clima;
- material;
- personas;
- horarios;
- rutas;
- stock;
- actividad;
- probabilidad causal;
- cooldown;
- conflictos.

Ejemplo:

un incendio de almacén de madera es más plausible si existen:

- material combustible;
- fuente de ignición;
- condiciones compatibles.

---

# 6. Consecuencias

Una consecuencia puede ser:

## Inmediata

- cierre;
- daño;
- alarma;
- bloqueo.

## Temporal

- menor producción;
- desvío;
- aumento de guardia;
- falta de stock.

## Persistente

- edificio quemado;
- NPC herido;
- deuda;
- reputación;
- desplazamiento de hogar.

## Derivada

Crea condición para otro evento.

---

# 7. Cadena causal

El World State debe conservar, cuando sea relevante:

`causa → evento → efecto → nueva condición → nuevo evento`

No solo una lista cronológica.

---

# 8. Conflictos

Dos eventos pueden coexistir.

Ejemplo:

- temporal + juicio importante;
- incendio + escasez;
- convoy + calle bloqueada.

El sistema debe resolver interacciones.

No escoger arbitrariamente uno y borrar el otro.

---

# 9. Prioridad funcional

Cuando eventos compiten por recursos:

1. vida y seguridad;
2. emergencia;
3. obligación institucional;
4. continuidad económica importante;
5. actividad ordinaria.

Esto puede reasignar:

- guardia;
- trabajadores;
- transporte;
- espacios.

---

# 10. Evento visible vs evento real

Un evento puede existir sin que el jugador lo conozca.

Debe distinguirse:

- ocurrió;
- el jugador lo percibió;
- un NPC lo sabe;
- se convirtió en rumor;
- se anunció oficialmente.

El conocimiento sigue las reglas K0–K5.

---

# 11. Eventos fuera de escena

Pueden avanzar en LOD-L/M.

Al volver el jugador, la ciudad refleja:

- consecuencias;
- rumores;
- daños;
- ausencias;
- stocks.

No se congela porque el jugador esté en otra zona.

---

# 12. Eventos autorales

Un evento narrativo escrito puede usar el mismo sistema de consecuencias.

La autoría determina:

- causa;
- condiciones;
- personajes;
- resultado permitido.

La infraestructura de World State asegura que el resto de la ciudad reaccione de forma coherente.

---

# 13. Baseline

D12 — día urbano ordinario es válido y frecuente.

El sistema debe permitir largos periodos sin evento extraordinario.

No existe cuota de incidentes por hora de juego.

---

# 14. Repetición

Un mismo tipo D puede repetirse.

Pero cada instancia debe tener:

- causa;
- fecha;
- lugar;
- actores;
- efectos propios.

No se copia el evento anterior cambiando solo un número.

---

# 15. Registro

Campos mínimos recomendados:

- event_id;
- archetype;
- source;
- state;
- start_time;
- location_refs;
- actor_refs;
- cause_refs;
- effect_refs;
- visibility_state;
- resolution;
- persistent_consequences.

---

# 16. Limpieza

Un evento resuelto puede salir de simulación activa.

Pero se conserva referencia histórica si afecta a:

- memoria;
- reputación;
- daño;
- investigación;
- contrato;
- historia.

---

## Regla final

**En Treskal un evento ocurre porque algo lo causó, y deja huella solo en aquello que realmente alcanzó.**
