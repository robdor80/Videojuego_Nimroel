# Treskal — motivaciones, objetivos e intención personal v0.1

## Estado

**DISEÑO DE NPC APROBADO — LOS HABITANTES QUIEREN COSAS AUNQUE EL JUGADOR NO ESTÉ MIRANDO**

## Objetivo

Dar a cada NPC persistente la capacidad de mantener objetivos propios sin convertirlos en misiones del jugador.

---

# 1. Objetivo personal

Un objetivo representa un estado futuro que el NPC desea intentar alcanzar.

Puede afectar:

- hogar;
- trabajo;
- aprendizaje;
- relaciones;
- cuidado;
- economía;
- viaje;
- reputación;
- seguridad;
- vida cotidiana.

---

# 2. Estados operativos

## GOAL01 — desired_outcome

Existe un resultado deseado, todavía sin decisión clara de perseguirlo.

## GOAL02 — adopted_goal

La persona ha decidido intentar conseguirlo.

## GOAL03 — planned_goal

Existe una estrategia o siguiente paso razonable.

## GOAL04 — in_progress

Se están realizando acciones reales relacionadas.

## GOAL05 — blocked_or_deferred

El objetivo sigue vigente, pero una condición impide o retrasa el avance.

## GOAL06 — achieved

El resultado se ha conseguido de forma suficiente.

## GOAL07 — abandoned

La persona deja de perseguirlo.

## GOAL08 — superseded

Otro objetivo o cambio de circunstancias lo sustituye.

---

# 3. Objetivo no es preferencia

PREF expresa inclinación.

GOAL expresa intención orientada a un futuro.

“Le gusta trabajar la madera” no equivale a “quiere abrir su propio taller”.

---

# 4. Objetivo no es quest

Un objetivo puede existir sin generar contenido jugable para el jugador.

Muchos objetivos se resuelven mediante:

- rutina;
- relaciones;
- trabajo;
- decisiones offscreen;
- tiempo.

El jugador no posee la agenda de los NPC.

---

# 5. Prioridad

Un NPC puede mantener varios objetivos.

La prioridad puede variar por:

- urgencia;
- seguridad;
- cuidado;
- plazo;
- recursos;
- relación;
- oportunidad;
- emoción;
- obligación.

No se exige una puntuación universal.

---

# 6. Conflicto entre objetivos

Dos objetivos pueden competir.

Ejemplo conceptual:

- aceptar más trabajo;
- pasar más tiempo cuidando a un familiar.

El NPC debe poder:

- posponer;
- escoger;
- buscar ayuda;
- abandonar;
- renegociar.

---

# 7. Recursos

Adoptar un objetivo no crea:

- dinero;
- herramientas;
- permisos;
- vivienda;
- empleo;
- rutas;
- tiempo.

Los sistemas propietarios siguen mandando.

---

# 8. Información

Un NPC solo puede planear con conocimiento disponible.

No puede elegir una solución basada en:

- lugar desconocido;
- persona que no conoce;
- stock oculto;
- hecho secreto.

K y CRED limitan la planificación.

---

# 9. Emoción

EMO y MOOD pueden alterar:

- urgencia percibida;
- paciencia;
- disposición;
- apetito de riesgo.

No sustituyen el objetivo ni deciden automáticamente la conducta.

---

# 10. Relaciones

Un objetivo puede incluir a otras personas.

Eso no obliga a esas personas a colaborar.

REQ, FAV, EMP, HOSP, AFF y FRI conservan su autonomía.

---

# 11. Jugador

El jugador puede:

- descubrir objetivos;
- ayudar;
- obstaculizar;
- ignorar;
- proponer alternativas.

No obtiene automáticamente una misión.

---

# 12. IA

La IA puede recibir objetivos relevantes del NPC para decidir:

- qué pregunta;
- qué evita;
- qué acepta;
- qué prioriza.

No puede inventar un nuevo objetivo persistente únicamente para que una conversación resulte interesante.

---

## Regla final

**Un habitante de Treskal no espera inmóvil a que aparezca el jugador: tiene asuntos propios, decide cuáles importan y persigue aquello que puede perseguir.**
