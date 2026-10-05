# Treskal — propagación de información y rumores v0.1

> **AUTORIDAD K MIGRADA A NIMROEL CORE.** La autoridad normativa de K reside en `Worldbuilding/Sistemas/Nimroel Core/06_Comunicacion_y_saber/conocimiento_procedencia_v0.1.md`. Este archivo conserva canales y ejemplos propios de Treskal; reputación queda separada y no forma parte de K.

## Estado

**DISEÑO DE GAMEPLAY APROBADO — INFORMACIÓN NO OMNISCIENTE**

## Objetivo

Definir cómo se extiende una noticia por Treskal sin asumir que todos los NPC conocen inmediatamente cualquier acontecimiento.

---

# 1. Estados de conocimiento

Una persona puede conocer un hecho como:

## K0 — Desconocido

No sabe nada.

## K1 — Presenciado

Lo vio u oyó directamente.

## K2 — Confirmado por fuente directa

No lo presenció, pero lo recibió de alguien con conocimiento directo o mediante comunicación institucional fiable.

## K3 — Rumor

Ha oído una versión no confirmada.

## K4 — Aviso oficial

La información ha sido comunicada públicamente por autoridad competente.

## K5 — Versión dudosa o contradictoria

Ha recibido versiones incompatibles o información de fiabilidad baja.

---

# 2. Un evento no se publica globalmente

Cuando ocurre algo:

1. existen testigos;
2. los testigos lo incorporan a su conocimiento;
3. algunos lo cuentan;
4. la información viaja por relaciones y lugares;
5. puede deformarse;
6. quizá llegue a una institución;
7. quizá exista después una versión oficial.

No existe un “broadcast” automático a todos los NPC.

---

# 3. Canales principales

## Hogar

Muy eficaz para información personal y cotidiana.

## Trabajo

Difunde rápido dentro de:

- talleres;
- puerto;
- Astilleros;
- administración;
- mercados.

## Familia y amistades

Puede conectar subzonas distintas.

## Mercado

Gran amplificador de rumores urbanos.

## Tabernas y posadas

Difunden:

- viajes;
- comercio;
- sucesos;
- rumores exteriores.

## Puerto

Difunde información procedente de:

- barcos;
- tripulaciones;
- comerciantes;
- otras tierras.

## Guardia

Difunde internamente:

- incidentes;
- personas buscadas;
- riesgos.

## Administración y justicia

Difunden información formal según necesidad.

---

# 4. Velocidad relativa

## Muy rápida

- incendio visible;
- gran pelea en Plaza del Abasto;
- accidente importante en puerto;
- llegada excepcional de un barco;
- cierre del Puente de los Gemelos.

## Media

- nuevo comerciante;
- disputa entre talleres;
- condena judicial;
- gran encargo.

## Lenta

- conflictos familiares;
- reputación artesanal;
- pequeñas deudas;
- acontecimientos en sectores alejados.

## Restringida

- archivos;
- investigación;
- decisiones de La Casa;
- asuntos internos de Astilleros Reales.

---

# 5. Distancia social

La propagación depende más de redes que de metros.

Un rumor portuario puede llegar antes a:

- taberna del Abasto;
- proveedor de aparejos;
- familiar de marinero

que a una vivienda físicamente más próxima pero socialmente desconectada.

---

# 6. Distorsión

Cada transmisión puede:

- conservar;
- simplificar;
- exagerar;
- mezclar;
- omitir.

La distorsión aumenta con:

- número de intermediarios;
- emoción;
- falta de pruebas;
- prejuicios;
- interés personal.

No todo rumor debe deformarse obligatoriamente.

---

# 7. Fuente

El sistema debe conservar cuando sea relevante:

- quién originó;
- quién contó;
- dónde se oyó;
- cuándo;
- grado de confianza.

Esto permite que un NPC diga:

- “lo vi”;
- “me lo dijo mi hermano”;
- “eso dicen en los Muelles”;
- “lo anunció la guardia”.

---

# 8. Secretos

Un hecho secreto tiene:

- círculo inicial;
- reglas de acceso;
- riesgo de filtración.

No se convierte en rumor público salvo que alguien:

- lo cuente;
- lo descubra;
- lo presencie;
- acceda a documentación;
- lo infiera con base suficiente.

---

# 9. Falsedad

Un rumor puede ser falso.

Debe poder existir:

- información inventada;
- error honesto;
- interpretación equivocada;
- mentira deliberada.

La IA del NPC debe distinguir entre:

**“sé”** y **“he oído”.**

---

# 10. Rumores y eventos dinámicos

D01–D12 pueden generar información visible.

Ejemplos:

- temporal → conocimiento general rápido;
- mercante recién llegado → rumores en puerto primero;
- juicio → información en Z08, luego T03/posadas;
- falta de cereal → comerciantes lo saben antes que muchos hogares.

---

# 11. Memoria

La información puede perder relevancia.

No debe borrarse si fue:

- personalmente importante;
- traumática;
- contractual;
- familiar;
- judicial;
- relacionada con promesa.

Los rumores triviales pueden decaer.

---

# 12. Actualización de diálogo

La IA recibe para cada NPC:

- hechos conocidos;
- nivel K;
- fuente;
- antigüedad;
- confianza;
- posibles contradicciones.

No recibe el World State completo como conocimiento verbalizable.

---

## Regla final

**En Treskal la información viaja de persona en persona y de lugar en lugar; saber algo debe tener una historia.**
