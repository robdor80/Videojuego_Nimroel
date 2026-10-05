# Treskal — necesidades físicas cotidianas y autocuidado v0.1

## Estado

**DISEÑO DE NPC APROBADO — NECESIDADES REALES SIN CONVERTIR EL JUEGO EN UN SURVIVAL**

## Objetivo

Conectar la vida cotidiana del NPC con necesidades corporales básicas ya implícitas en:

- alimentación;
- agua;
- descanso;
- ropa;
- clima;
- saneamiento.

Sin fijar todavía metabolismo, calorías, litros, frecuencia exacta ni daño fisiológico numérico.

---

# 1. Tipos funcionales

## NEED01 — food_intake

Necesidad cotidiana de ingerir alimento.

## NEED02 — hydration

Necesidad cotidiana de beber agua u otra bebida adecuada.

## NEED03 — thermal_comfort

Necesidad de evitar exposición prolongada incompatible con el bienestar ordinario.

## NEED04 — elimination

Necesidad cotidiana de usar un espacio compatible para eliminación corporal.

## NEED05 — rest_pressure

Necesidad acumulada de descanso y sueño.

REST conserva la autoridad sobre estados concretos de descanso.

---

# 2. Estado cualitativo

Cada necesidad puede encontrarse, cuando sea relevante, en niveles conceptuales como:

- satisfied;
- emerging;
- pressing;
- urgent.

Este documento no fija umbrales temporales universales.

---

# 3. No es una interfaz de supervivencia

El jugador no necesita ver:

- cinco barras;
- porcentajes;
- temporizadores fisiológicos

para que el sistema exista.

La mayoría de necesidades cotidianas pueden resolverse dentro de rutinas normales.

Solo se materializan con detalle cuando:

- falta un recurso;
- una rutina se interrumpe;
- un viaje se prolonga;
- existe enfermedad futura;
- un evento altera acceso;
- la necesidad afecta decisiones.

---

# 4. Comida

NEED01 puede satisfacerse mediante comida real disponible en:

- hogar;
- trabajo;
- posada;
- mercado;
- hospitalidad;
- viaje.

El tipo exacto depende del stock y del canon alimentario.

El sistema no genera comida para satisfacer la necesidad.

---

# 5. Agua

NEED02 requiere bebida disponible.

El agua doméstica:

- debe existir;
- haber sido transportada o captada;
- encontrarse accesible.

No aparece en un hogar porque el NPC tenga sed.

---

# 6. Temperatura

NEED03 puede verse afectada por:

- clima;
- lluvia;
- viento;
- ropa;
- refugio;
- fuego;
- actividad.

CL, ENV y combustible mantienen sus propios estados.

Este documento no define hipotermia, golpe de calor ni mecánicas médicas.

---

# 7. Eliminación

NEED04 conecta al NPC con:

- letrina;
- pozo negro;
- instalación doméstica compatible;
- otra solución preindustrial autorizada.

WASTE y saneamiento siguen controlando infraestructura y residuos.

No hace falta simular cada uso ordinario.

---

# 8. Descanso

NEED05 no sustituye REST.

Representa la presión de necesidad.

REST registra:

- descanso;
- sueño;
- interrupción;
- recuperación.

---

# 9. Prioridad

Una necesidad emergente puede esperar.

Una necesidad urgente puede modificar:

- ruta;
- conversación;
- trabajo;
- ocio;
- decisión.

No anula automáticamente:

- emergencia;
- peligro;
- obligación inmediata.

---

# 10. Niños y dependientes

CHD, DEP y CARE pueden modificar:

- capacidad de autocuidado;
- necesidad de supervisión;
- acceso a comida, bebida o descanso.

No se fijan tasas específicas por edad.

---

# 11. Viaje

Un viaje prolongado necesita permitir:

- comer;
- beber;
- descansar;
- atender necesidades corporales.

El viaje no es movimiento continuo sin vida cotidiana.

---

# 12. IA

La IA puede conocer una necesidad relevante cuando afecta la escena.

Puede expresar:

- hambre;
- sed;
- necesidad de descansar;
- búsqueda de refugio.

No debe mencionar constantemente necesidades ya cubiertas por rutina.

---

## Regla final

**Los habitantes de Treskal tienen cuerpo y necesidades, pero el juego solo las hace visibles cuando importan: la rutina las resuelve hasta que el mundo deja de permitirlo.**
