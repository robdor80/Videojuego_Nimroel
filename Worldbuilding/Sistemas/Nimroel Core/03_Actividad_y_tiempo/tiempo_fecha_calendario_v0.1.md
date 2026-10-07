# Nimroel Core — tiempo, fecha y calendario civil v0.1

## Autoridad

**CORE UNIVERSAL — namespace TIME**

Este sistema define:

- paso físico del tiempo;
- fecha civil estándar;
- hora;
- día de la semana;
- aritmética temporal;
- franjas narrativas;
- anclas para agendas, contratos y eventos.

---

## 1. Principio

Nimroel utiliza un calendario deliberadamente simple y familiar para el jugador.

La estructura civil estándar es:

- 12 meses;
- 365 días por año;
- 7 días por semana;
- 24 horas por día;
- 60 minutos por hora;
- 60 segundos por minuto.

No existen años bisiestos en el calendario estándar.

---

## 2. Meses

Orden y duración:

1. enero — 31 días;
2. febrero — 28 días;
3. marzo — 31 días;
4. abril — 30 días;
5. mayo — 31 días;
6. junio — 30 días;
7. julio — 31 días;
8. agosto — 31 días;
9. septiembre — 30 días;
10. octubre — 31 días;
11. noviembre — 30 días;
12. diciembre — 31 días.

Total: **365 días**.

---

## 3. Semana

La semana tiene siete días:

1. lunes;
2. martes;
3. miércoles;
4. jueves;
5. viernes;
6. sábado;
7. domingo.

La semana comienza en lunes.

Los nombres se utilizan como etiquetas civiles canónicas en castellano.

No implican en el lore:

- dioses terrestres;
- etimologías romanas;
- religión histórica de la Tierra.

---

## 4. Hora

Un día tiene:

- 24 horas;
- cada hora 60 minutos;
- cada minuto 60 segundos.

Formato interno recomendado:

`HH:mm:ss`

Formato corriente suficiente:

`HH:mm`

Ejemplo:

`16:37`

---

## 5. Medianoche

El día civil cambia a las:

`00:00:00`

La fecha anterior termina en:

`23:59:59`

No existe horario de verano ni cambio estacional de reloj.

---

## 6. Tiempo absoluto

El motor debe poder mantener una referencia temporal absoluta monotonically increasing.

Forma conceptual:

`world_second_index`

o equivalente de precisión compatible.

La fecha civil se deriva de ese tiempo.

El cambio de:

- escena;
- LOD;
- mapa;
- conversación;
- guardado/carga

no reinicia el tiempo.

---

## 7. Época técnica

Para resolver días de la semana de forma determinista:

**1 de enero del año 1 = lunes.**

No se define todavía un acontecimiento histórico ocurrido en el año 1.

La época técnica existe para cálculo.

No obliga a que los personajes sepan por qué el cómputo comienza allí.

---

## 8. Año cero

No existe año 0 en la representación civil estándar.

La cronología positiva comienza en año 1.

Si en el futuro se necesitan fechas anteriores, se definirá una extensión histórica compatible.

---

## 9. Año de referencia actual

El año de referencia para la fase actual del proyecto es:

**15375**

Las fechas narrativas previas situadas en 15374 siguen siendo válidas.

15375 no borra ni migra eventos históricos de 15374.

Una campaña debe declarar su fecha inicial concreta.

---

## 10. Fecha

Formato interno recomendado:

`YYYY-MM-DD`

Fecha/hora:

`YYYY-MM-DDTHH:mm:ss`

Ejemplo:

`15375-10-18T16:37:00`

Formato visible en castellano:

`18 de octubre de 15375`

Formato numérico:

`18/10/15375`

---

## 11. Día de la semana

El día de la semana se deriva de:

- época técnica;
- número de días transcurridos.

No se almacena como verdad independiente cuando pueda reconstruirse.

Esto evita contradicciones del tipo:

- fecha = lunes;
- registro paralelo = martes.

---

## 12. Franjas narrativas

Además de la hora exacta, el motor puede exponer una franja narrativa.

Default:

- madrugada — 00:00–05:59;
- mañana — 06:00–11:59;
- mediodía — 12:00–13:59;
- tarde — 14:00–19:59;
- noche — 20:00–23:59.

Son etiquetas narrativas.

No sustituyen:

- luz ambiental;
- amanecer real;
- ocaso real;
- clima;
- visibilidad.

---

## 13. Amanecer y ocaso

Amanecer y ocaso no son horas fijas universales.

Cuando exista modelo de luz/latitud suficiente pueden derivarse de:

- fecha;
- ubicación;
- estación;
- geografía.

Hasta entonces:

- la hora civil sigue siendo exacta;
- las etiquetas de franja siguen siendo válidas;
- la IA no inventa una hora solar exacta.

---

## 14. Duraciones

Debe distinguirse:

### duración transcurrida

Ejemplo:

`72 horas`

Significa exactamente 72 × 60 × 60 segundos.

### duración civil

Ejemplo:

`3 días civiles`

Opera sobre fechas.

### periodo de calendario

Ejemplo:

`1 mes`

Avanza un mes conservando el día cuando existe.

---

## 15. Suma de meses

Al sumar meses:

- se conserva el número de día si existe en el mes destino;
- si no existe, se usa el último día del mes destino.

Ejemplo:

`31 de enero + 1 mes = 28 de febrero`

Esta regla sirve para:

- alquileres;
- cuotas;
- contratos;
- reservas;
- otros vencimientos mensuales.

---

## 16. Suma de años

Al no existir años bisiestos:

`28 de febrero + 1 año = 28 de febrero del año siguiente`

Toda fecha válida existe cada año.

---

## 17. Edad

La edad civil se calcula por fecha de nacimiento.

Una persona cumple N años al comenzar el mismo día y mes del año correspondiente.

Ejemplo:

nacido el 14 de mayo de 15357 alcanza 18 años el:

`14 de mayo de 15375 a las 00:00`

La mayoría de edad no depende de haber celebrado el cumpleaños.

---

## 18. Plazos y vencimientos

Un sistema propietario puede definir:

- fecha exacta;
- fecha + hora;
- duración transcurrida;
- número de días civiles;
- meses/años de calendario;
- ventana aproximada.

El contrato debe declarar cuál utiliza.

No se convierten automáticamente todos los plazos a horas exactas.

---

## 19. Agenda

AGEN puede usar:

- timestamp exacto;
- fecha;
- franja del día;
- ventana;
- secuencia relativa.

No toda actividad cotidiana necesita minuto exacto.

Cuando hay conflicto temporal, el motor puede resolver con tiempo exacto.

---

## 20. Off-screen

El tiempo sigue avanzando fuera de escena.

LOD puede agregar:

- trabajo rutinario;
- sueño;
- viaje;
- producción;
- deterioro;
- espera.

Pero respeta la misma línea temporal.

No existe “tiempo congelado” para NPC no visibles salvo modo de juego explícito.

---

## 21. Guardado y carga

Guardar y cargar conserva exactamente:

- fecha;
- hora;
- eventos pendientes;
- vencimientos;
- agendas.

Cargar una partida no vuelve al inicio del día.

---

## 22. Velocidad de simulación

El juego puede:

- pausar;
- acelerar;
- saltar tiempo mediante una acción válida;
- resolver periodos off-screen.

Cambiar velocidad no cambia la cronología.

Un salto temporal debe procesar consecuencias relevantes.

---

## 23. IA

La IA puede:

- conocer la fecha/hora que el contexto le proporcione;
- usar expresiones relativas coherentes;
- decir «mañana», «el lunes», «a las seis» cuando proceda.

No puede:

- cambiar la hora;
- crear días;
- mover un vencimiento;
- declarar que pasó una semana;
- resolver una agenda;
- hacer avanzar el calendario.

---

## 24. Relatividad lingüística

Expresiones como:

- hoy;
- mañana;
- ayer;
- esta tarde;
- esta noche;
- dentro de dos días;
- el próximo lunes

se resuelven desde el timestamp del World State.

No se almacenan como texto ambiguo cuando generan una obligación persistente.

---

## 25. Sin zonas horarias

El calendario estándar no utiliza zonas horarias.

Nimroel emplea una hora civil común para la simulación.

Esto evita relojes regionales distintos en la misma campaña.

La posición solar local puede diferir visualmente sin crear husos civiles.

---

## 26. Calendario frente a cultura

Este Core fija la estructura temporal estándar.

Una cultura puede añadir:

- celebraciones;
- ferias;
- aniversarios;
- periodos de luto;
- costumbres estacionales.

No puede alterar silenciosamente:

- duración del día;
- orden de fechas;
- tiempo físico.

---

## Regla final

**Nimroel utiliza un calendario intencionadamente familiar: la complejidad debe estar en lo que ocurre durante el tiempo, no en obligar al jugador a aprender a contarlo.**
