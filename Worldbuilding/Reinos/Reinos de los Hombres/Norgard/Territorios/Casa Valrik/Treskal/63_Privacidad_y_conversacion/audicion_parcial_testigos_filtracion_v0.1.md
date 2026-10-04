# Treskal — audición parcial, testigos y filtración de información v0.1

## Estado

**DISEÑO DE WORLD STATE APROBADO**

## Objetivo

Conectar conversación con:

- sonido;
- K;
- rumor;
- reputación;
- testimonio.

---

# 1. Registro conceptual de exposición

Una conversación relevante puede registrar:

- conversation_id;
- participant_refs;
- location_ref;
- privacy_context;
- voice_mode;
- start_time;
- end_time;
- listener_candidates;
- exposure_results.

No es necesario persistir todas las conversaciones triviales.

---

# 2. Resultado por oyente

Puede ser:

## HEAR00 — none

No detectó nada relevante.

## HEAR01 — presence_only

Sabe que había conversación.

## HEAR02 — fragments

Oyó fragmentos.

## HEAR03 — substantial

Comprendió parte sustancial.

## HEAR04 — full_content

Comprendió contenido completo relevante.

## HEAR05 — full_content_and_voice

Además identificó al hablante.

---

# 3. Selección de candidatos

Solo se evalúan oyentes plausibles por:

- espacio;
- distancia;
- barreras;
- sonido;
- atención.

No se recorren todos los NPC de la ciudad.

---

# 4. Persistencia

HEAR02+ puede crear conocimiento persistente si:

- contenido importa;
- actor lo recuerda;
- contexto lo justifica.

HEAR01 puede no persistir.

---

# 5. Testimonio

Un testigo puede afirmar:

- lo que oyó;
- lo que cree haber oído;
- quién cree que hablaba.

La confianza puede variar.

No se convierte automáticamente en hecho confirmado.

---

# 6. Contradicción

Dos oyentes pueden haber percibido cosas distintas.

Eso puede generar K5.

No se fuerza consenso.

---

# 7. Eavesdropping y descubrimiento

Si un oyente deliberado es detectado:

puede afectar:

- relación;
- reputación;
- acceso;
- conflicto.

La reacción depende del contexto.

---

# 8. Save/LOD

Una conversación relevante ocurrida fuera de escena puede producir conocimiento solo si:

- los actores estaban presentes;
- el sistema resolvió exposición;
- existía ruta auditiva/social.

No porque el jugador no estuviera mirando.

---

## Regla final

**La conversación produce conocimiento por oyente, no por radio de zona ni por guion.**
