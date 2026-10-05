# Treskal — secuelas, evacuación y recuperación tras incendio v0.1

> **MIGRADO A NIMROEL CORE — documentación derivada con override local explícito.** La autoridad normativa de FIRE reside en `Worldbuilding/Sistemas/Nimroel Core/04_Material_y_riesgo/incendio_propagacion_respuesta_v0.1.md`. Treskal conserva únicamente su organización concreta de respuesta y la capacidad particular de los Astilleros Reales; ante conflicto prevalece el Core.

## Estado

**DISEÑO DE WORLD STATE APROBADO**

## Objetivo

Cerrar correctamente la secuencia:

**detección → respuesta → contención → extinción → secuelas → reparación/retorno**

---

# 1. Fase de secuelas

FIRE08 puede incluir:

- edificio COND03–07;
- herramientas dañadas;
- stock perdido;
- agua acumulada;
- humo;
- objetos desplazados;
- residentes RES05;
- negocio BIZ03/04/07;
- empleo afectado;
- rutas bloqueadas.

---

# 2. Reentrada

Extinguir fuego no autoriza reentrada automática.

Puede depender de:

- estabilidad;
- calor;
- humo;
- acceso;
- daño.

El sistema de edificio decide habitabilidad.

---

# 3. Alojamiento

Si un hogar pierde vivienda:

usa RES05 y capacidad real de:

- familia;
- amistades;
- posadas;
- otro alojamiento disponible.

No aparece una vivienda gratuita.

---

# 4. Bienes salvados

Los objetos evacuados deben:

- cambiar location_ref;
- conservar owner_ref;
- poder quedar bajo custodia.

No se teletransportan al inventario del propietario.

---

# 5. Pérdidas

Los bienes destruidos:

- dejan de estar disponibles;
- pueden conservar referencia histórica si eran relevantes.

No reaparecen al reparar edificio.

---

# 6. Reparación o reconstrucción

Según daño:

- COND/repair;
- BUILD.

La extinción no restaura función.

---

# 7. Negocio

Puede:

- reabrir parcialmente;
- mudarse;
- permanecer cerrado;
- desaparecer.

Depende de:

- local;
- stock;
- herramientas;
- trabajadores;
- capital futuro.

---

# 8. Causa e investigación

Puede quedar:

- conocida;
- probable;
- desconocida;
- disputada.

No se inventa culpable para cerrar narrativa.

---

# 9. Rumor

Un gran incendio puede propagarse rápidamente como información.

Los detalles pueden:

- cambiar;
- exagerarse;
- contradecirse.

El hecho físico base permanece independiente del rumor.

---

# 10. Memoria urbana

Un incendio importante puede dejar:

- edificio reconstruido;
- cicatriz;
- solar;
- reputación;
- memoria de NPC;
- cambio de rutina.

Puede convertirse en historia de esa partida.

---

## Regla final

**Apagar el fuego salva lo que queda; recuperar la vida anterior es otro proceso distinto.**
