# Treskal — limpieza doméstica, colada y estado visual persistente v0.1

## Estado

**DISEÑO DE GAMEPLAY/VISUAL APROBADO**

## Objetivo

Relacionar:

- hogar;
- agua;
- ropa;
- actividad;
- clima;
- presentación visual

sin simular cada cubo o cada camisa de 15.000 habitantes.

---

# 1. Resolución agregada

En LOD-L/M, el hogar puede mantener variables agregadas:

- water_access_state;
- laundry_load;
- dry_clothing_availability;
- household_cleaning_state.

No se individualiza cada prenda ordinaria.

---

# 2. Prenda persistente

Una prenda se individualiza cuando es:

- visualmente distintiva;
- regalo;
- uniforme;
- evidencia;
- objeto de encargo;
- narrativamente relevante.

Entonces conserva:

- item_id;
- propietario;
- pátina;
- suciedad contextual;
- humedad;
- daño;
- reparación.

---

# 3. Estado de ropa

Puede separar:

## base_patina

Uso acumulado A–D.

## contextual_soiling

Estado temporal 1–5.

## wetness

Humedad actual.

## repair_state

Remiendos o daño.

## presentation_use

Trabajo / cotidiano / salida / ceremonial si procede.

---

# 4. Lavado

El lavado puede reducir:

- suciedad contextual;
- olor;
- determinados residuos.

No reduce automáticamente:

- pátina;
- desgaste;
- reparaciones.

---

# 5. Secado y clima

Si una prenda sigue mojada:

no debe aparecer seca porque el NPC cambió de LOD.

El secado puede avanzar fuera de escena según:

- tiempo;
- ventilación;
- lluvia;
- calor disponible.

---

# 6. Rutina NPC

La posibilidad de aseo puede depender de:

- hogar;
- posada;
- jornada;
- viaje;
- disponibilidad de agua;
- tiempo.

Un viajero de varios días puede acumular más estado contextual que un residente que volvió a casa.

---

# 7. Clase social

La posición económica puede afectar:

- número de prendas;
- facilidad para cambiarse;
- calidad del tejido;
- acceso a ayuda doméstica.

No define automáticamente limpieza.

---

# 8. Trabajo físico

La actividad puede añadir marcas contextualizadas.

Ejemplos:

- tierra en bajos;
- hollín en delantal;
- humedad/salitre en marinero;
- serrín en carpintero.

La distribución importa.

---

# 9. Guardado

No es necesario guardar la suciedad de cada NPC latente.

Para NPC persistentes o visibles relevantes sí puede guardarse:

- presentation_state;
- last_major_activity;
- last_hygiene_opportunity;
- clothing_state.

---

# 10. IA

El contexto visual/narrativo puede recibir:

- estado visible;
- actividad reciente;
- clima;
- ropa actual.

No debe inventar suciedad adicional para “hacer medieval” la escena.

---

## Regla final

**Nimroel no simula mugre genérica: simula huellas de actividad, y permite que desaparezcan cuando el mundo ofrece tiempo, agua y cambio de ropa.**
