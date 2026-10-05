# Treskal — visitante, residente y continuidad de identidad v0.1

> **MIGRADO A NIMROEL CORE — documentación derivada.** La autoridad normativa de RES / MOVE reside en `Worldbuilding/Sistemas/Nimroel Core/03_Actividad_y_tiempo/residencia_hogar_mudanzas_v0.1.md`. Este archivo conserva explicación y ejemplos de Treskal; ante conflicto prevalece el Core.

## Estado

**DISEÑO DE WORLD STATE APROBADO**

## Objetivo

Evitar que el mismo personaje sea tratado como:

- visitante anónimo;
- NPC nuevo;
- residente distinto

simplemente porque cambió la duración de su estancia.

---

# 1. Identidad única

Si un visitante materializado posee npc_id:

ese ID se conserva al convertirse en residente.

No se genera un reemplazo B.

---

# 2. Cambio de categoría

La transición actualiza:

- resident_state;
- household;
- home;
- visitor fields;
- routine;
- workplace si procede.

No reinicia:

- relaciones;
- memoria;
- reputación;
- conocimientos.

---

# 3. Estancia prolongada

RES02 puede ser útil para:

- trabajador temporal largo;
- comerciante con temporada extensa;
- persona alojada con familia;
- especialista visitante.

No equivale a residencia definitiva.

---

# 4. Hogar estable

Establecer home_location_id en Treskal es una señal fuerte de residencia.

Pero el futuro sistema legal puede distinguir:

- residencia de hecho;
- derechos legales de propiedad/tenencia.

---

# 5. Ausencia temporal del residente

Un residente puede viajar fuera de Treskal sin convertirse en former_resident.

Debe conservar:

- hogar;
- pertenencia;
- intención de regreso

cuando sea coherente.

---

# 6. Abandono permanente

Para RES04 debe existir cambio real:

- mudanza;
- salida;
- decisión;
- otra causa.

No se marca por no haber sido visto durante varios días.

---

# 7. Población latente

Los conteos agregados deben actualizarse al cambiar categoría.

No se debe contar simultáneamente a la misma persona como:

- visitante;
- residente.

---

# 8. Guardado

Cambios de residencia relevantes deben persistir.

Una partida cargada no puede devolver al personaje a su categoría inicial de generación.

---

## Regla final

**Cambiar dónde vive una persona modifica su situación, no su identidad.**
