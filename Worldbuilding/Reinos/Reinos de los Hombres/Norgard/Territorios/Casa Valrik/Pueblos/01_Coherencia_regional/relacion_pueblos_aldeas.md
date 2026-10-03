# Pueblos de Treskal — relación funcional con las aldeas

## Estado

**REGLA DE COHERENCIA REGIONAL APROBADA**

## Función

Este documento fija cómo debe interpretarse la relación territorial entre un Pueblo y las Aldeas de su entorno.

No asigna Pueblos o Aldeas concretos ni radios o distancias geométricas fijas. Las probabilidades se resuelven en la capa `02_Probabilidades/` y las relaciones concretas se generan mediante la coordinación regional y el estado persistente de la partida.

---

## 1. Área de servicio funcional

Un Pueblo actúa normalmente como **centro de referencia para varias aldeas**, pero su área de servicio no debe definirse mediante un círculo o radio geométrico fijo.

La relación debe derivarse de la **accesibilidad territorial real**.

Entre los factores relevantes se encuentran:

- red de caminos;
- relieve;
- ríos;
- puentes y vados;
- distancia;
- tiempo de viaje;
- condiciones climáticas y ambientales que afecten temporalmente al tránsito.

Por tanto, dos aldeas situadas a distancia similar pueden depender de pueblos distintos si sus conexiones reales son diferentes.

---

## 2. Pueblo de referencia principal

La mayoría de las aldeas puede disponer de un **Pueblo de referencia principal** para funciones que no necesita resolver localmente.

Entre ellas pueden encontrarse:

- mercado periódico;
- herrería de nivel 2;
- especialistas concretos;
- intercambio de mercancías;
- contacto con autoridad territorial itinerante;
- otros servicios que el propio Pueblo haya generado.

Esta relación no implica que la aldea quede aislada de otros núcleos.

---

## 3. Solapamiento de áreas de servicio

Una aldea situada entre dos pueblos, o conectada razonablemente con ambos, puede utilizar **más de un Pueblo**.

La elección puede variar según:

- servicio buscado;
- ruta disponible;
- mercado;
- relaciones económicas;
- condiciones temporales de tránsito.

El sistema no debe forzar una división territorial artificial en zonas exclusivas cuando la red real permita solapamiento.

---

## 4. Dependencia directa de una Villa

Una aldea remota o situada en una red concreta puede depender directamente de una **Villa** para determinados servicios si esa Villa resulta más accesible que un Pueblo.

La jerarquía:

**Aldea → Pueblo → Villa → Treskal**

describe una tendencia funcional, no una obligación geométrica absoluta para cada desplazamiento.

---

## 5. Tiempo de viaje y mercado

En condiciones normales, muchas aldeas vinculadas a un Pueblo deberían poder realizar un desplazamiento al mercado y regresar **dentro de la misma jornada**.

Las aldeas más periféricas pueden:

- viajar con menor frecuencia;
- necesitar una estancia nocturna;
- utilizar una posada si existe;
- combinar el viaje con transporte de mercancías u otras gestiones.

No se fija todavía una distancia universal en kilómetros.

---

## 6. Accesibilidad dinámica

La relación territorial estructural puede mantenerse aunque una ruta concreta quede temporalmente degradada o bloqueada.

Factores ya definidos en el borrador ambiental del territorio pueden alterar la accesibilidad, por ejemplo:

- barro;
- crecidas;
- nieve;
- hielo;
- vados impracticables;
- daños en caminos o puentes.

Esto puede provocar que durante un periodo:

- se utilice una ruta alternativa;
- aumente el tiempo de viaje;
- una aldea recurra temporalmente a otro Pueblo;
- se reduzca la frecuencia de intercambio.

El Pueblo de referencia principal no tiene por qué cambiar por una interrupción temporal.

---

## 7. Principio de generación

El motor no debe distribuir aldeas alrededor de los pueblos mediante círculos regulares.

Debe interpretar la red territorial como una **red de accesibilidad**.

Regla conceptual:

**posición + caminos + relieve + pasos fluviales + tiempo de viaje + servicios disponibles + estado temporal de las rutas = relación funcional plausible entre asentamientos**

La asignación concreta se realizará en fases posteriores de generación regional y persistirá en el estado del mundo cuando corresponda.

---

## Regla final

**La proximidad física importa, pero la accesibilidad real decide la relación funcional.**
