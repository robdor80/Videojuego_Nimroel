# Treskal — encuentros sociales y formación de familiaridad v0.1

## Estado

**DISEÑO DE WORLD STATE APROBADO**

## Objetivo

Conectar ocio con:

- relaciones;
- conocimiento;
- rumores;
- descanso;
- negocios;
- visitantes.

---

# 1. Encuentro relevante

Puede registrar:

- social_event_id;
- participant_refs;
- location_ref;
- leisure_context;
- start_time;
- end_time;
- conversation_refs_if_any;
- relation_deltas_if_any;
- knowledge_deltas_if_any.

No se persisten todos los encuentros triviales.

---

# 2. Familiaridad

La repetición de encuentros puede aumentar:

- reconocimiento;
- comodidad;
- conocimiento superficial.

No crea automáticamente amistad.

---

# 3. Amistad

Requiere interacciones compatibles.

No se genera solo por proximidad o número de encuentros.

---

# 4. Rivalidad

Puede surgir de:

- conflicto;
- competencia;
- historia;
- repetición negativa.

No aparece por azar decorativo.

---

# 5. Nodo social

Un lugar puede tener probabilidad mayor de encuentros porque existe actividad real.

Ejemplos:

- taberna;
- mercado;
- plaza;
- posada;
- muelle en pausa.

Eso no convierte el lugar en fuente universal de rumores.

---

# 6. Rutina social

Un NPC puede tener preferencia habitual por:

- hogar;
- local;
- plaza;
- conocidos.

No debe aparecer siempre en el mismo punto si su vida cambia.

---

# 7. Visitante

La exposición social de un visitante puede aumentar con:

- duración;
- trabajo;
- alojamiento;
- ocio;
- relaciones.

No equivale a RES.

---

# 8. LOD

Un encuentro offscreen puede resolverse solo si:

- participantes estaban disponibles;
- compartían lugar/actividad plausible;
- había tiempo.

No se crean relaciones mientras NPC estaban en sitios incompatibles.

---

## Regla final

**Las relaciones sociales emergen de encuentros que realmente pudieron ocurrir.**
