# NIMROEL RPG — Auditoría técnica del borrador climático del territorio de Treskal

**Documento de trabajo para revisión futura del lore**  
**Estado:** auditoría técnica / no canon / no especificación de implementación  
**Objetivo:** evaluar si el borrador ambiental actual de Treskal proporciona una base útil para que el futuro motor de Nimroel RPG pueda **inferir, generar y mantener estados ambientales coherentes** sin que el autor tenga que definir manualmente cada arroyo, camino, ladera, campo o accidente menor.

---

# 1. Material revisado

Esta auditoría se ha realizado sobre los siguientes bloques del repositorio:

## Clima local de Treskal

Ruta:

`Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Valrik/Clima_local/`

Documentos revisados:

- `README.md`
- `00_encuadre_y_subzonas.md`
- `01_temperatura.md`
- `02_lluvias.md`
- `03_nieve_y_deshielo.md`
- `04_viento.md`
- `05_humedad_nieblas_y_visibilidad.md`
- `06_hidrologia_y_escorrentia.md`
- `07_suelos_y_drenaje.md`
- `08_vegetacion_y_microclimas.md`
- `09_reglas_de_inferencia_para_juego.md`

## Montes Invernos

Ruta regional:

`Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Geografía/Montes Invernos/cotas_y_altitudes_borrador.md`

Aplicación local al territorio Valrik/Treskal:

`Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Valrik/Geografia_local/montes_invernos_cotas_y_altitudes.md`

---

# 2. Conclusión general

El bloque climático actual es **muy útil para el futuro motor del juego**.

No es todavía una especificación ejecutable ni debe convertirse ahora en JSON o código, pero sí constituye una **excelente especificación conceptual de relaciones ambientales**.

El avance más importante no es que el lore describa cómo es Treskal, sino que empieza a describir **por qué ocurren las cosas en Treskal**.

Esto es exactamente lo que necesita un sistema de inferencia.

Antes se podía decir:

> Treskal tiene clima oceánico suave al sur y mayor continentalidad hacia el interior.

Ahora se dispone de relaciones conceptuales del tipo:

```text
subzona
+ latitud
+ altitud
+ distancia al mar
+ orientación
+ relieve
+ vegetación
+ estación
+ meteorología reciente
= estado térmico local
```

o:

```text
cuenca
+ pendiente
+ lluvia acumulada
+ nieve/deshielo
+ suelo
+ vegetación
+ aportes aguas arriba
= estado de un curso de agua
```

o:

```text
agua acumulada
+ tipo de suelo
+ drenaje
+ compactación
+ tránsito
+ pendiente
= barro
```

Este enfoque es mucho más valioso para un motor procedural que fijar miles de datos aislados.

---

# 3. Lo que está especialmente bien orientado

## 3.1. Uso de causas en lugar de resultados prefijados

El borrador no cae en la trampa de definir:

```text
arroyo X:
profundidad = 1,27 m
corriente = 2,4 m/s
```

En su lugar define causas como:

```text
piedemonte
+ primavera
+ invierno nivoso
+ lluvia prolongada
+ suelo saturado
```

y permite que el futuro sistema derive consecuencias.

Este enfoque es correcto porque unos pocos hechos pueden producir muchas consecuencias:

- caudal de arroyos;
- dificultad de vados;
- barro;
- estado de caminos;
- niebla;
- vegetación;
- inundaciones;
- agricultura;
- transitabilidad;
- narración ambiental.

---

## 3.2. Separación entre subzona base y modificadores locales

`00_encuadre_y_subzonas.md` establece una estructura muy adecuada:

### Capa regional

- costa meridional;
- corredor aluvial;
- tierras interiores;
- Bosque Negro;
- piedemonte;
- Montes Invernos;
- tierras septentrionales;
- costa septentrional.

### Modificadores locales

- altitud;
- orientación;
- valle;
- depresión;
- ribera;
- bosque;
- exposición;
- drenaje;
- distancia al mar.

Esto evita un error muy común: convertir el mapa en polígonos climáticos rígidos.

El futuro motor debería trabajar precisamente así:

```text
contexto regional
+ modificadores locales
+ estado meteorológico actual
= situación ambiental concreta
```

---

## 3.3. Persistencia y memoria ambiental

Este es uno de los puntos más importantes de todo el borrador.

Los documentos de nieve, humedad, suelo, hidrología y vegetación repiten correctamente que el mundo debe conservar memoria.

Ejemplo:

```text
humedad previa
+ lluvia
+ deshielo
- drenaje
- evaporación
= humedad actual
```

Esto evita comportamientos artificiales como:

```text
ayer llovió durante tres días
hoy deja de llover
→ todo aparece seco inmediatamente
```

La persistencia ambiental encaja directamente con el futuro `WorldState`.

Un camino, río, bosque o campo conserva su identidad, pero cambia de estado.

---

# 4. Principio técnico fundamental que ya está bien expresado

El documento `09_reglas_de_inferencia_para_juego.md` contiene una idea especialmente importante:

> **El lugar permanece; su estado cambia.**

Esto encaja perfectamente con CoreRPG.

Ejemplo:

```text
Camino #X
```

puede encontrarse:

```text
verano seco:
firme y polvoriento

otono húmedo:
blando

primavera excepcional:
barro profundo

invierno:
helado
```

El camino no cambia de identidad.

Cambia su estado.

Lo mismo debe aplicarse a:

- ríos;
- arroyos;
- vados;
- puentes;
- bosques;
- campos;
- laderas;
- costas;
- caminos.

Esta separación será esencial cuando se diseñe el WorldState real.

---

# 5. Utilidad actual para inferencia ambiental

Con el borrador actual ya es posible justificar inferencias coherentes para una localización nunca diseñada manualmente.

Ejemplo hipotético:

```text
subzona:
piedemonte meridional de Montes Invernos

altitud:
1.050 m

relieve:
fondo de valle

vegetación:
borde forestal

estación:
primavera

meteorología reciente:
10 días húmedos

nieve:
presente en cotas superiores

deshielo:
activo
```

A partir del lore actual sería razonable que el futuro sistema derivase:

```text
temperatura:
más fría que las tierras bajas

humedad:
alta

suelo:
muy húmedo o saturado

niebla matinal:
plausible

escorrentía:
elevada

arroyos:
caudal alto

barro:
probable

vados:
potencialmente comprometidos

vegetación:
húmeda y activa

riesgo de crecida:
elevado si continúa lloviendo
```

Ninguno de esos detalles necesita estar previamente escrito para esa localización concreta.

Ese es precisamente el objetivo correcto.

---

# 6. Montes Invernos: valoración

La estructura altitudinal propuesta es útil para generación.

Rangos actuales:

```text
Piedemonte meridional:        400–900 m
Valles y laderas bajas:       800–1.500 m
Laderas medias y altas:       1.500–2.300 m
Crestas principales:          2.200–2.800 m
Cumbres habituales:           2.600–3.200 m
Cumbres más elevadas:         3.200–3.500 m
Picos excepcionales:          hasta ~3.600 m
Pasos principales:            1.500–2.100 m
Cabeceras Sareno/Theleno:     aprox. 1.600–2.600 m
```

## Lo positivo

Los rangos:

- permiten nieve estacional;
- permiten deshielo prolongado;
- justifican nacimientos de ríos;
- generan gradientes vegetales;
- permiten pasos montañosos;
- crean diferencias claras entre piedemonte, valle, ladera y cumbre;
- evitan fijar todavía cientos de cotas individuales innecesarias.

## Solapamiento entre rangos

No se considera un problema.

De hecho, es preferible evitar fronteras artificiales como:

```text
899 m = piedemonte
900 m = montaña
```

Las categorías deberán convertirse en gradientes y perfiles, no en cortes bruscos.

## Decisión especialmente correcta

No asignar todavía la cumbre máxima a Galdren o Valrik es acertado.

Evita que el desarrollo local de Treskal imponga accidentalmente decisiones geográficas sobre un territorio todavía no desarrollado.

---

# 7. Principal hueco detectado: existencia y trazado de hidrografía menor

Este es el punto más importante pendiente desde la perspectiva del futuro generador.

Actualmente `06_hidrologia_y_escorrentia.md` responde muy bien a:

> **Si existe un arroyo, ¿cómo debería comportarse?**

Pero todavía no responde completamente a:

> **¿Por qué existe precisamente un arroyo ahí?**

El futuro motor necesitará poder responder, al menos de forma simplificada:

```text
¿existe aquí un curso de agua?
↓
¿dónde nace?
↓
¿por qué dirección fluye?
↓
¿qué cuenca recoge?
↓
¿recibe afluentes?
↓
¿a qué río o cuenca termina conectado?
```

## Necesidad futura

Será necesario desarrollar una capa de:

**microrelieve + drenaje + cuencas + red hidrográfica menor**

Conceptualmente:

```text
campo de elevaciones
↓
pendientes
↓
direcciones de drenaje
↓
acumulación de agua
↓
cuencas
↓
cauces
↓
red hidrográfica menor
```

No se necesita una simulación geológica real.

Pero sí debe existir una causa espacial que evite absurdos como:

- arroyos que suben laderas;
- cursos sin cuenca;
- ríos que aparecen en divisorias;
- cauces inconexos sin explicación.

---

# 8. Recomendación futura: desarrollar microrelieve e hidrografía menor

Cuando se retome la geografía local de Treskal, sería útil responder cualitativamente a preguntas como:

- ¿qué zonas tienen mayor densidad de pequeños cursos?
- ¿dónde son frecuentes los manantiales?
- ¿qué áreas generan arroyos estacionales?
- ¿qué zonas presentan vaguadas?
- ¿qué partes son llanuras suaves?
- ¿dónde aparecen colinas bajas?
- ¿dónde comienzan barrancos?
- ¿qué sectores tienen drenaje hacia Sareno?
- ¿qué sectores drenan hacia Theleno?
- ¿qué zonas costeras drenan directamente al mar?
- ¿qué áreas del piedemonte concentran escorrentía?
- ¿qué sectores tienen pequeñas cuencas cerradas o encharcables?

El objetivo no es dibujar cada arroyo.

El objetivo es definir **dónde es razonable que puedan aparecer**.

---

# 9. Diferencia necesaria entre clima del Content Pack y tiempo de la partida

El lore actual describe correctamente **lo que puede ocurrir normalmente**.

El futuro juego deberá separar eso de **lo que está ocurriendo en una partida concreta**.

Ejemplo:

## Content Pack / canon climático

```text
primavera:
lluvias frecuentes
deshielo relevante
tormentas posibles
```

## WorldState de una partida

```text
Año 15374

últimos 18 días:
precipitación muy superior a lo normal

temperatura:
suave

deshielo:
rápido

suelo:
saturado
```

Otra partida podría tener, en la misma estación:

```text
primavera excepcionalmente seca
```

Ambas situaciones serían compatibles con el mismo canon.

La separación futura deberá ser:

```text
CONTENT PACK
Qué condiciones son propias del territorio

+

WORLDSTATE
Qué está ocurriendo en esta partida

+

RULES
Qué consecuencias produce esa combinación

=

REALIDAD ACTUAL
```

---

# 10. Lo que NO debe hacerse ahora

No conviene convertir todavía estos documentos en:

- JSON definitivo;
- porcentajes;
- probabilidades cerradas;
- fórmulas;
- coeficientes;
- tablas numéricas exhaustivas;
- simulación física.

Términos actuales como:

- moderado;
- abundante;
- frecuente;
- ocasional;
- fuerte;
- buen drenaje;
- mal drenaje;
- alta humedad;

son apropiados en esta fase.

Más adelante podrán traducirse a categorías estructuradas y rangos.

---

# 11. Necesidad futura de una taxonomía operativa

Cuando llegue la fase técnica, habrá que convertir términos de lore en vocabulario operativo controlado.

Ejemplos conceptuales:

```text
drainage:
good
moderate
poor

rainfall_regime:
low
moderate
high

snow_persistence:
short
medium
long

current_strength:
weak
moderate
strong
```

Esto NO debe diseñarse ahora.

Pero será necesario antes de que el motor pueda evaluar reglas.

---

# 12. Necesidad futura de un orden de dependencias

Los documentos humanos repiten correctamente muchos conceptos:

- lluvia;
- nieve;
- viento;
- deshielo;
- humedad;
- drenaje;
- caudal;
- barro;
- vegetación.

En software no deben existir varios sistemas calculando el mismo concepto de forma independiente.

Será necesario definir una cadena de autoridad.

Ejemplo conceptual:

```text
meteorología regional
↓
temperatura / precipitación / viento
↓
nieve / hielo
↓
humedad del suelo
↓
escorrentía
↓
caudal
↓
barro / inundación / transitabilidad
↓
vegetación / gameplay / narración
```

Esta dependencia deberá diseñarse técnicamente más adelante.

---

# 13. UNKNOWN debe seguir siendo una opción válida

No todo elemento debe recibir una respuesta inventada.

La futura inferencia debería distinguir:

```text
AUTHORED
dato escrito explícitamente

DERIVED
dato deducido de reglas

GENERATED
detalle concretado proceduralmente

DYNAMIC
estado que cambia en WorldState

UNKNOWN
información insuficiente
```

Si no hay base suficiente para conocer algo, el motor debe poder mantener:

```text
unknown
```

Esto es preferible a generar falsa precisión.

---

# 14. Procedencia de datos: recomendación importante

Para depuración y futuro Inspector sería muy útil que las propiedades importantes pudieran conservar conceptualmente su procedencia.

Ejemplo:

```text
current = strong
source = derived
```

o:

```text
soil_drainage = poor
source = authored
```

o:

```text
stream_width = medium
source = generated
```

Esto permitiría inspeccionar por qué el motor ha producido una situación concreta.

No es necesario guardar literalmente estas cadenas en todos los casos, pero el diseño debe contemplar trazabilidad suficiente.

---

# 15. Relación con el futuro Inspector

La futura fase de Inspector debería permitir comprobar estados como:

```text
RiverSegment #184

current:
STRONG
source: derived

Factors:
- spring
- recent heavy rain
- active snowmelt
- moderate slope

soil:
SATURATED

ford:
DANGEROUS

state:
materialized / persistent
```

Esto será muy útil para detectar errores de inferencia.

---

# 16. IA narrativa: valoración

El borrador es ya una buena fuente para el futuro Context Builder.

La IA no debería decidir:

- cuánto ha llovido;
- si el río está crecido;
- si el camino está embarrado;
- si hay nieve;
- si el vado es peligroso.

Eso debe resolverlo el mundo.

La IA recibirá el estado ya determinado y lo expresará en lenguaje natural.

Ejemplo estructurado:

```text
location_type: river_bank
current: strong
water_visibility: poor
bank_depth: shallow
floating_debris: fast
perception_quality: good
```

Narración posible:

> La corriente baja con fuerza. Cerca de la orilla el agua parece poco profunda, pero hacia el centro el fondo desaparece y algunas ramas pasan arrastradas con rapidez.

El borrador climático actual proporciona una base muy buena para alimentar esa capa narrativa.

---

# 17. Errores y desajustes documentales detectados

No se han detectado problemas graves de diseño.

Sí existen algunos **desajustes de evolución documental** que conviene corregir en la futura revisión de consolidación.

## 17.1. Barlovento / sotavento

En documentos iniciales como:

- `00_encuadre_y_subzonas.md`
- `02_lluvias.md`

todavía aparece la cautela de que no se fija qué vertiente de los Montes Invernos queda a barlovento o sotavento hasta desarrollar el bloque de viento.

Sin embargo, `04_viento.md` ya desarrolla una tendencia:

- en otoño/invierno son frecuentes flujos húmedos desde sur/sureste;
- estos ascienden por la vertiente meridional;
- aumentan precipitación al sur de los Montes Invernos;
- determinados sectores al norte pueden quedar temporalmente en sotavento parcial.

### Acción futura

Actualizar los documentos anteriores para que no parezca que la cuestión sigue completamente abierta.

Debe mantenerse, eso sí, el matiz correcto:

> barlovento y sotavento dependen dinámicamente de la dirección del viento; existe una tendencia estacional, no una orientación universal permanente.

---

## 17.2. Cotas todavía marcadas como pendientes en documentos antiguos

Algunos textos iniciales indican que todavía no existen cotas suficientemente definidas para los Montes Invernos.

Posteriormente se creó:

`Geografía/Montes Invernos/cotas_y_altitudes_borrador.md`

con rangos aprobados en borrador.

### Acción futura

Durante la consolidación final, revisar referencias antiguas para distinguir:

- cotas regionales generales: ya existen como rangos de borrador;
- cotas exactas de accidentes individuales: siguen pendientes.

---

## 17.3. Estado de glaciares / nieve permanente

La documentación actual es coherente en dejar pendiente:

- glaciares;
- nieve permanente extensa;
- grandes campos de hielo.

Se permiten:

- neveros persistentes;
- nieve estacional prolongada;
- hielo local.

### Acción futura

No resolver hasta disponer de:

- cartografía suficiente;
- desarrollo del sector Galdren;
- orientación concreta de cumbres;
- exposición;
- latitud efectiva.

No es necesario para la v0.0.1.

---

# 18. Elementos que aún faltan para una inferencia ambiental robusta

No todos pertenecen al lore inmediato.

## 18.1. Microrelieve local

Pendiente futuro:

- lomas;
- vaguadas;
- pequeños valles;
- barrancos;
- depresiones;
- terrazas fluviales;
- piedemonte;
- pendientes.

Necesario para:

- drenaje;
- hidrografía;
- caminos;
- niebla;
- heladas;
- agricultura;
- asentamientos.

---

## 18.2. Red hidrográfica menor

Pendiente futuro:

- densidad de arroyos;
- manantiales;
- cauces estacionales;
- cuencas;
- conexiones con Sareno/Theleno;
- drenaje directo al mar.

Necesario para generar cursos no diseñados manualmente.

---

## 18.3. Meteorología dinámica

No es un hueco de lore.

Será software.

Necesitará generar:

- frentes;
- periodos húmedos;
- sequías;
- temporales;
- olas de frío;
- episodios cálidos;
- tormentas.

Siempre dentro de los límites del Content Pack.

---

## 18.4. Estado persistente ambiental

Será parte del WorldState.

Necesitará conservar, según el nivel de simplificación final:

- humedad;
- nieve;
- hielo;
- caudal;
- barro;
- inundación;
- estado vegetal;
- daños ambientales;
- transitabilidad.

---

## 18.5. Modelos de escalas

El documento 09 ya distingue acertadamente:

### Regional
clima, estación y grandes patrones.

### Local
valle, bosque, suelo, ribera, orientación.

### Inmediata
charco, barro, nieve residual, estado de un arroyo.

La implementación deberá conservar esa jerarquía para no simular todo con la misma precisión.

---

# 19. Riesgo a evitar: sobre-simulación

El objetivo del juego no debe convertirse en:

> simulador científico completo de clima e hidrología.

La regla correcta es:

> simular lo suficiente para que las consecuencias jugables sean plausibles, coherentes y persistentes.

Por ejemplo, no es necesario calcular hidráulica real para saber que:

```text
lluvia intensa
+ deshielo
+ suelo saturado
+ cauce pequeño
= riesgo alto de crecida
```

---

# 20. Riesgo a evitar: reglas independientes contradictorias

No debe ocurrir:

```text
sistema de lluvia:
dice suelo saturado

sistema de caminos:
ignora el suelo

sistema de río:
calcula caudal sin mirar deshielo

IA:
describe camino seco
```

La arquitectura deberá resolver primero un estado coherente y compartirlo con los sistemas consumidores.

---

# 21. Riesgo a evitar: generación aleatoria no condicionada

No debe utilizarse:

```text
river_depth = random()