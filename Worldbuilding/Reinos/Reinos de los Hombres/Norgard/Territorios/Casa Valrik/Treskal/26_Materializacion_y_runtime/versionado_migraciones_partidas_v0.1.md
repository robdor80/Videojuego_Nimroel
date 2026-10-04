# Treskal — versionado, migraciones y compatibilidad de partidas v0.1

## Estado

**DISEÑO TÉCNICO-CONCEPTUAL APROBADO**

## Objetivo

Permitir evolucionar el diseño de Treskal durante desarrollo sin romper automáticamente partidas persistentes.

---

# 1. Identidades estables

Los IDs técnicos T/Z/L/S/U/G/C/A/D/P/K/O/H/V/ST son contratos.

Cambiar nombre visible no cambia ID.

---

# 2. Versiones

Cada contrato operativo debe disponer de:

- schemaVersion;
- documentId;
- version;
- status.

Los datos guardados deben conocer la versión de esquema con la que fueron creados.

---

# 3. Cambio compatible

Ejemplos:

- añadir campo opcional;
- añadir alias visible;
- ampliar regla sin invalidar estado previo.

Puede migrarse automáticamente.

---

# 4. Cambio estructural

Ejemplos:

- dividir una subzona;
- mover landmark;
- cambiar significado de ID;
- alterar geometría ya persistida.

Necesita migración explícita.

---

# 5. Nunca reutilizar ID con otro significado

Si un elemento se retira:

- queda deprecated;
- se migra;
- se crea ID nuevo cuando corresponda.

No se recicla su ID para otra cosa.

---

# 6. Materialización existente

Una actualización de reglas no debe rerollear:

- NPC ya conocidos;
- hogares;
- interiores visitados;
- negocios persistentes.

La nueva regla se aplica a:

- materializaciones futuras;
- o mediante migración controlada.

---

# 7. Geometría futura

Cuando llegue el plano métrico:

los IDs abstractos actuales deben mapearse a geometría.

La geometría concreta no sustituye:

- T;
- Z;
- L;
- C.

Los referencia.

---

# 8. Error de migración

Si una partida no puede migrarse con seguridad:

- no inventar estado;
- marcar incompatibilidad;
- ofrecer mecanismo técnico definido por la aplicación.

No se resuelve silenciosamente eliminando entidades.

---

# 9. Canon y partida

El canon puede evolucionar durante desarrollo.

Una partida representa además su propia historia.

La migración debe distinguir:

- cambio de diseño;
- consecuencia ocurrida en esa partida.

No sobrescribir el segundo con el primero.

---

## Regla final

**Actualizar Treskal significa migrar su representación; nunca hacer como si la partida anterior no hubiera ocurrido.**
