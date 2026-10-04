# Treskal — persistencia ambiental, secado y recuperación v0.1

## Estado

**DISEÑO DE WORLD STATE APROBADO**

## Objetivo

Mantener coherencia entre clima y estado material sin simular meteorología a escala científica.

---

# 1. Variables agregadas locales

Una zona o superficie relevante puede mantener:

- env_state;
- recent_precipitation;
- exposure;
- drainage_quality;
- traffic_pressure;
- drying_conditions;
- last_update_time.

---

# 2. Transiciones

Ejemplo conceptual:

ENV01 → ENV02 → ENV03 → ENV04/ENV05

si persisten agua y tránsito.

Tras mejora:

ENV05/04 → ENV06 → ENV02 → ENV01

según condiciones.

No es obligatorio pasar por todos los estados.

---

# 3. Secado

Depende de:

- cese de lluvia;
- viento;
- temperatura;
- sol/luz disponible;
- ventilación;
- superficie;
- drenaje.

No se fija fórmula exacta.

---

# 4. Interiores

Un interior puede permanecer:

- seco;
- húmedo;
- afectado por filtración

de forma distinta al exterior.

No se propaga ENV exterior directamente a toda habitación.

---

# 5. Charcos y barro visual

Solo aparecen cuando:

- superficie;
- agua;
- drenaje;
- tránsito

lo justifican.

No son decoración aleatoria.

---

# 6. Persistencia

Un save/load conserva estado ambiental suficiente o lo reconstruye determinísticamente desde:

- tiempo;
- clima reciente;
- superficie;
- último estado.

No debe resetear a seco.

---

# 7. LOD

En bajo detalle:

se conserva ENV agregado por zona/superficie.

En alto detalle:

se materializan:

- barro;
- humedad;
- huellas;
- charcos

compatibles.

---

# 8. Huellas

El barro puede dejar:

- marcas en calzado;
- bajos de ropa;
- ruedas;
- suelo interior próximo a entradas.

Su persistencia depende de:

- limpieza;
- secado;
- nuevo tránsito.

---

# 9. Recuperación tras temporal

Resolver D01 no implica:

- muelles secos;
- rutas limpias;
- ropa seca;
- daños reparados.

Cada sistema recupera por separado.

---

## Regla final

**El clima cambia rápido; la materia tarda más. El World State debe recordar esa diferencia.**
