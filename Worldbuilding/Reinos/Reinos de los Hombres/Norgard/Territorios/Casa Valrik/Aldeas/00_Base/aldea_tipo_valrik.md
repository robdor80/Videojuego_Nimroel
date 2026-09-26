# Aldea tipo — territorio de Treskal

## Estado

**CANON BASE EN DESARROLLO**

## Función

Este documento define los límites mínimos de una **aldea interior típica del territorio de Treskal**.

No describe una aldea concreta y no fija un plano único.

Su función es proporcionar al sistema de generación un marco suficientemente claro para producir aldeas distintas entre sí sin abandonar la identidad regional de Treskal.

---

## Principio de generación

Una aldea del territorio de Treskal debe ser **generada dentro de límites**, no diseñada previamente edificio por edificio.

La generación puede decidir, según el modelo utilizado y el contexto territorial:

- número exacto de viviendas;
- posición relativa de las casas;
- uno o varios caminos;
- presencia o ausencia de determinados oficios;
- número y variante de talleres;
- presencia de posada;
- número de plantas de determinados edificios;
- distribución de huertos, corrales y anexos;
- familias y NPC;
- pequeños elementos ambientales.

Estas decisiones no forman parte del canon estable mientras no exista una razón concreta para fijarlas.

Una vez generada una aldea para una partida, su resultado debe persistir.

---

## Rasgos obligatorios comunes

Una aldea del territorio de Treskal debe sentirse:

- pequeña y claramente rural;
- funcional antes que ornamental;
- formada principalmente por familias y explotaciones locales;
- conectada a otras aldeas mediante caminos y servicios compartidos;
- integrada en la economía territorial de Valrik;
- suficientemente distinta de una villa o de la ciudad de Treskal.

Las viviendas son generalmente **bajas y familiares**, agrupadas con lógica orgánica y sin una trama urbana rígida.

El entorno inmediato puede incluir, según el modelo:

- campos;
- huertos;
- corrales;
- pequeñas explotaciones ganaderas;
- espacios de trabajo;
- almacenes;
- caminos hacia otros núcleos.

---

## Servicios compartidos

Las aldeas del territorio de Treskal no son autosuficientes por defecto.

Un herrero, molino, carretero, carpintero, posada u otro servicio puede:

- existir en una aldea;
- faltar por completo;
- dar servicio a varias aldeas cercanas.

La generación debe favorecer una **red rural interdependiente**, no una repetición de aldeas idénticas y autosuficientes.

Esto permite generar de forma natural:

- desplazamientos;
- tránsito de mercancías;
- relaciones entre NPC;
- encargos;
- motivos para viajar entre asentamientos.

---

## Escala canónica

En el territorio de Treskal, una **aldea** tiene entre **35 y 100 habitantes**.

Este es el límite canónico del tipo de asentamiento. La distribución de probabilidades dentro de ese rango se definirá más adelante.

Los modelos concretos podrán sesgar la población hacia determinadas zonas del rango, pero no salir de él salvo que el asentamiento deje de clasificarse como aldea.

El número de viviendas debe derivarse de la población y de las unidades familiares generadas, no de una cifra fija independiente.

---

## Coherencia sistémica

Los edificios y NPC deben generarse de forma coherente entre sí.

Ejemplos:

- si existe herrería, debe existir al menos un NPC que pueda operarla;
- si existe molino, debe existir una razón física y económica para su presencia;
- si existe una posada, su tamaño debe guardar relación con el tránsito de la ruta;
- un taller no debe aparecer sin acceso razonable a materia prima, clientes o transporte;
- los campos, corrales y almacenes deben corresponderse con las actividades del asentamiento.

---

## Sorpresa y persistencia

La generación debe producir descubrimiento para el jugador.

El lore no debe revelar por adelantado la configuración concreta de una aldea ordinaria.

La aldea puede generarse:

- al crear el mundo;
- al iniciar una partida;
- o al determinar por primera vez esa zona.

Pero una vez fijada debe conservar:

- edificios;
- servicios;
- familias;
- NPC;
- relaciones;
- distribución general.

La semilla o los datos de la instancia pertenecen al **World State / partida**, no al canon general.

---

## Uso

Los modelos concretos derivados de esta base se guardan en:

`../01_Modelos/`

Las aldeas canónicas que necesiten fijarse expresamente se guardarán en:

`../02_Instancias/`


---

## Cobertura regional de servicios

La generación local debe estar subordinada a una comprobación regional.

Un servicio especializado puede faltar en una aldea si existe acceso razonable a ese servicio en otro asentamiento próximo.

A medida que aumenta la distancia o escasez de un servicio, debe aumentar también la probabilidad de que una aldea apta lo genere.

Cuando una necesidad mínima de la zona no pueda quedar cubierta por azar, el sistema debe **forzar una solución entre los candidatos plausibles**, no añadir el servicio de forma arbitraria a cualquier núcleo.

Ejemplo conceptual:

- una aldea cercana a un pueblo con herrero tendrá baja probabilidad de generar otra herrería;
- una aldea alejada de cualquier herrero tendrá una probabilidad mayor;
- si al terminar de generar una pequeña red rural ninguna localización cubre ese servicio dentro del límite permitido, el sistema elegirá el candidato más coherente y lo añadirá antes de cerrar la región.

Las distancias, tiempos máximos, probabilidades y capacidades exactas se definirán más adelante como datos operativos.

Este principio deberá extenderse también a futuros modelos de **pueblos y villas**, de modo que la red territorial completa se genere de forma coordinada.
