# Treskal — red viaria métrica v0.1

## Estado

**PLANO MÉTRICO — PUNTO 6 CERRADO**

Marcador:

`TRESKAL_METRIC_PLAN_POINT_6_ROAD_NETWORK_CLOSED`

Contrato operativo:

`../Datos operativos/treskal_metric_road_network_contract_v0.1.json`

---

## 1. Alcance

Punto 6 fija:

- jerarquía viaria;
- anchos funcionales;
- trazados métricos;
- accesos regionales;
- aproximaciones al Puente de los Gemelos;
- rutas de carros;
- rutas pesadas;
- ganado;
- peatones;
- accesos a S01–S13;
- reglas de pavimento y drenaje.

No fija todavía:

- muelles y dársenas;
- gradas y atraques;
- manzanas;
- parcelación ordinaria;
- callejones menores ligados a parcelas.

---

## 2. Principio urbano

Treskal no utiliza una cuadrícula perfecta.

La red responde a:

- río;
- costa;
- Puente de los Gemelos;
- mercado;
- puerto;
- talleres;
- administración;
- recinto militar;
- Complejo Naval Real;
- crecimiento histórico.

El tráfico pesado puede evitar T03.

---

## 3. Clases viarias

### R1 — arterial principal

- calzada: **5,8–6,5 m**;
- referencia: **6,2 m**;
- reserva total: **8,5–11 m**;
- dos carros en sentidos opuestos;
- peatones;
- drenaje prioritario.

### R2 — logística pesada

- calzada: **5,2–6,0 m**;
- referencia: **5,6 m**;
- reserva total: **7,5–10 m**;
- apta para madera y suministros navales.

### R3 — calle urbana principal

- calzada: **4,8–5,6 m**;
- referencia: **5,2 m**;
- reserva total: **6,5–8,5 m**.

### R4 — secundaria

- calzada: **3,4–4,4 m**;
- referencia: **4,0 m**;
- ensanches puntuales para cruce.

### R5 — acceso local

- calzada: **2,4–3,2 m**;
- referencia: **2,8 m**;
- sin tráfico pesado de paso.

### P1 — paso peatonal

- **1,5–2,4 m**;
- carros de mano o tránsito restringido.

### DR1 — vía de ganado

- útil: **5,5–7 m**;
- referencia: **6 m**;
- reserva: **8–11 m**;
- no atraviesa T03.

---

## 4. Red principal

Se fijan **18 ejes técnicos**, con aproximadamente **12,98 km** de trazado controlado.

No son nombres oficiales de calles.

### C01 — eje oeste / puente

Territorio occidental → Puente de los Gemelos → T02/T03.

Longitud: **~875 m**.

### C02 — abastecimiento rural norte

Norte → T10 → T02/T03.

Longitud: **~815 m**.

### C03 — bosque / madera

Rutas forestales → T04 → trasera T08.

Longitud: **~1.203 m**.

### C04 — militar / institucional

Nordeste → T12 → T05/T06.

Longitud: **~1.352 m**.

El tráfico militar pesado evita T03.

### C05 — suministro naval oriental

Acceso regional oriental → puertas controladas de T08.

Longitud: **~1.034 m**.

### C06 — puerto civil / mercado

T07 → interior → T03.

### C07 — río / mercado

T01 → T03.

### C08 — eje cívico

T06 → T05 y entorno institucional.

### C09 — arco residencial oriental

Distribuye T09 sin penetrar T08.

### C10 — talleres de madera

T02/T04 → enlace con C03.

### C11 — vía trasera del puerto civil

Distribuye carga sin obligarla a circular por primera línea de costa.

### C12 — pescado

S07 → mercado/interior.

### C13 — patios de madera

Une S09A y S09B.

### C14 — desvío de ganado

S10 → borde urbano.

No atraviesa T03.

### C15 — circuito militar T12

Sirve S11 y S12.

### C16 — espina interna T08

Sirve S08 y S13 bajo control naval.

### C17 — residencial N–S

Conecta T02/T09/T10.

### C18 — urbano E–O

Conecta núcleo comercial, justicia y zona institucional.

---

## 5. Puente de los Gemelos

C01 utiliza el puente ya fijado en Punto 3.

Tablero útil:

**6,2 m**.

Distribución funcional:

- calzada: **5,2 m**;
- franja peatonal protegida/elevada: **1,0 m**.

Dos carros pueden cruzarse con precaución.

En convoyes pesados puede aplicarse:

- prioridad;
- espera;
- paso dirigido por guardias.

No se crea un segundo puente.

---

## 6. Acceso a S01–S13

Las trece instalaciones quedan conectadas.

Especialmente:

- S01/S02 → C08/C09;
- S03/S04/S05 → C08/C18;
- S06 → C18/C07;
- S07 → C12;
- S08 → C05/C16;
- S09 → C13;
- S10 → C14;
- S11/S12 → C04/C15;
- S13 → C05/C16.

Los accesos internos controlados de T08 no se convierten en calles públicas.

---

## 7. Tráfico pesado

### Madera

Preferencia:

C03 → C10/C13 → C05/T08.

### Ganado

Preferencia:

C02 → C14 → S10 / borde urbano.

No atraviesa T03 por defecto.

### Militar

C04 → T12/C15.

### Naval

C05 → C16.

### Puerto civil

C11 → C06 → red interior.

### Río

C07 → C01/C02.

---

## 8. Pavimento

No todas las calles están pavimentadas.

Prioridad de piedra:

- accesos al Puente;
- mercado;
- lonja;
- frentes cívicos T05/T06;
- puertas T08.

Prioridad de grava/piedra triturada:

- grandes rutas regionales;
- madera;
- militar;
- naval;
- ganado donde el barro sea crítico.

Calles menores pueden usar:

- tierra compactada;
- grava;
- piedra local en puntos de desgaste.

---

## 9. Drenaje

Se utilizan:

- pendiente transversal;
- cunetas;
- canales;
- drenajes simples.

Pendiente transversal:

**2–4 %**.

No existe alcantarillado pluvial moderno.

Se prioriza drenaje en:

- C01;
- C06;
- C08;
- C11;
- S06;
- S07;
- accesos T08.

---

## 10. Peatones

El centro es caminable.

La red pública peatonal principal utiliza:

- C01;
- C02;
- C06;
- C07;
- C08;
- C09;
- C11;
- C12;
- C17;
- C18.

Punto 8 podrá añadir:

- pasos;
- callejones;
- accesos de parcela;

sin alterar los ejes ya fijados.

---

## 11. Seguridad y autoridad

T08:

- acceso controlado por autoridad naval de la Corona;
- C05/C16 no convierten el recinto en espacio público.

T12:

- accesos militares separados.

Guardia urbana:

- puede ordenar tránsito urbano;
- no adquiere autoridad ordinaria dentro de T08.

---

## 12. Emergencias

La red reserva acceso de respuesta especialmente a:

- S06;
- S07;
- S08;
- S09;
- S13;
- T03/T04 densos.

Se reconoce que el Puente de los Gemelos es un punto único de vulnerabilidad.

No se resuelve inventando otro puente.

---

## Certificación

**TRESKAL_METRIC_ROAD_NETWORK_VALIDATED**

La red conecta todos los sectores y S01–S13 sin recolocar nada de Puntos 3–5.

Siguiente:

**Punto 7 — Puerto civil y Complejo Naval Real.**

---

## Regla final

**Las calles sirven a la ciudad ya definida: no se mueve la ciudad para facilitar las calles.**

`TRESKAL_METRIC_PLAN_POINT_6_ROAD_NETWORK_CLOSED`
