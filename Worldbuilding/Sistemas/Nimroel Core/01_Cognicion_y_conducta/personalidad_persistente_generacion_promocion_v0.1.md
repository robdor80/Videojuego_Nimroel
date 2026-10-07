# Nimroel Core — personalidad persistente, generación y promoción v0.1

## Estado

**CORE MECÁNICO ACTIVO — PRODUCCIÓN ACTIVADA SOLO PARA HUMANOS DE NORGARD**

Marcador: `PERSISTENT_PERSONALITY_SYSTEM_NORGARD_HUMANS_ACTIVE`

---

## 1. Objetivo

Dar a cada NPC relevante una identidad psicológica persistente sin convertir la personalidad en:

- clase rígida;
- copia de un personaje de ficción;
- resultado de profesión;
- resultado de sexo;
- resultado de rango;
- resultado de cultura;
- reroll por conversación.

La personalidad debe hacer que un personaje siga siendo reconocible durante años de juego aunque cambien:

- emociones;
- relaciones;
- trabajo;
- residencia;
- edad;
- estatus;
- objetivos;
- circunstancias.

---

## 2. Autoridad

`PERS` conserva autoridad sobre tendencias relativamente estables.

No sustituye:

- `EMO/MOOD/STRS` — estado actual;
- `VAL` — valores;
- `SELF` — autoconcepto;
- `MEM` — memoria;
- `TRUST/AFF/FRI/RIFT` — relación;
- `GOAL/DEC` — objetivos y decisión;
- `CHD/AGE` — desarrollo y ciclo vital.

---

## 3. Dimensiones

Se conservan **PERS01–PERS10** sin cambio de significado.

Se añaden **PERS11–PERS28**:

- PERS11 warmth;
- PERS12 humor_frequency;
- PERS13 empathy_expression;
- PERS14 directness;
- PERS15 tact;
- PERS16 rule_orientation;
- PERS17 authority_deference;
- PERS18 ambition;
- PERS19 competitiveness;
- PERS20 initial_trust_speed;
- PERS21 intimacy_openness;
- PERS22 optimism;
- PERS23 self_confidence;
- PERS24 forgiveness_tendency;
- PERS25 teaching_instinct;
- PERS26 autonomy_need;
- PERS27 status_sensitivity;
- PERS28 pride.

Los saves/perfiles antiguos siguen siendo válidos.

---

## 4. Niveles de profundidad

### A — autoral

NPC muy importante.

La personalidad se escribe específicamente para él.

### B — procedural persistente

NPC importante o convertido en persistente.

Recibe un perfil completo generado una sola vez.

### C — latente

NPC de fondo/random.

Puede conservar únicamente semilla y firma conductual ligera.

---

## 5. C→B

Cuando un random se vuelve relevante:

1. ya existe `npc_id`;
2. existe `personality_seed` determinista;
3. se recupera cualquier conducta previamente observada;
4. se elige una receta compatible;
5. se generan las 28 dimensiones;
6. se añaden estilos cualitativos;
7. se crea `personality_profile_id`;
8. se guarda;
9. nunca se rerollea.

Una interacción trivial no obliga a promoción.

Una interacción con consecuencias persistentes sí puede hacerlo.

---

## 6. B→A

Un NPC B puede convertirse en muy importante.

No recibe otra personalidad.

La autoría:

- profundiza;
- añade matices;
- puede fijar historia psicológica;
- puede definir contradicciones deliberadas;

pero debe respetar la persona ya observada.

---

## 7. Generación procedural

Una receta no es una personalidad terminada.

Para Norgard:

- 80 recetas base;
- variación determinista por semilla;
- dimensiones no ancladas también varían;
- exact profile reuse prohibido.

Dos NPC pueden usar la misma receta y ser personas diferentes.

---

## 8. Investigación

El corpus de referencia sirve solo para descubrir dimensiones y combinaciones plausibles.

Fuentes actuales:

- Game of Thrones;
- House of the Dragon;
- Vikings;
- The Last Kingdom;
- The Witcher;
- The Lord of the Rings;
- A Knight of the Seven Kingdoms.

**Alcance actual: referencias humanas/humanas de origen para Norgard.**

Las muestras no humanas quedan excluidas de producción y de este corpus activo.

Nunca se crea:

- personalidad Jon Snow;
- personalidad Ragnar;
- personalidad Geralt;
- personalidad Dunk;

ni equivalente.

---

## 9. Cultura, profesión y clase

Ninguna de estas variables elige la personalidad:

- Gran Casa;
- oficio;
- riqueza;
- sexo;
- rango;
- nobleza;
- localidad.

Pueden modificar:

- registro;
- hábitos;
- expectativas;
- vocabulario;
- formalidad;
- normas aprendidas.

No reescriben PERS.

---

## 10. Evolución

PERS puede cambiar lentamente.

Todo cambio estable:

- necesita causa;
- registra procedencia;
- es acotado;
- persiste.

Un mal día no cambia personalidad.

Una relación concreta normalmente cambia TRUST/AFF/FRI antes que PERS global.

---

## 11. IA

La IA recibe un bloque compacto.

Puede expresar:

- tono;
- humor;
- directness;
- tact;
- reserva;
- iniciativa;
- reacción al estrés;
- afecto;
- desacuerdo.

No puede:

- crear rasgos permanentes;
- cambiar valores PERS;
- cambiar profile_id;
- inventar pasado psicológico;
- promocionar C→B por sí sola;
- alterar relaciones o emociones directamente.

---

## 12. Alcance actual

La mecánica está en Core.

La producción procedural está habilitada **únicamente para humanos de Norgard**.

No se implementan todavía:

- elfos;
- enanos;
- otros pueblos;
- otras especies.

Cada pueblo recibirá su capa propia cuando se desarrolle.

---

## Regla final

**La IA interpreta al personaje; el motor conserva quién es. Un NPC puede crecer, pero nunca se convierte en otra persona porque el juego lo haya vuelto a cargar.**

`PERSISTENT_PERSONALITY_SYSTEM_NORGARD_HUMANS_ACTIVE`
