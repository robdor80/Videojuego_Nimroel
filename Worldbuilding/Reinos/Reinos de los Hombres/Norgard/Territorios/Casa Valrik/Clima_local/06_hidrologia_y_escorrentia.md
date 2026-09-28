# Territorio de Treskal — hidrología y escorrentía

## Estado

**BORRADOR DE DISEÑO**

Este documento desarrolla el comportamiento cualitativo de la red hidrográfica del territorio de Treskal.

No fija todavía caudales exactos, secciones de cauce, velocidades de corriente ni fórmulas definitivas de simulación.

---

## 1. Principio general

### Estado

**PROPUESTA DE BORRADOR — PENDIENTE DE VALIDACIÓN**

El estado de un curso de agua no debe depender de una única etiqueta como “río”, “arroyo” o “afluente”.

Debe inferirse a partir de:

- tamaño de cuenca;
- altitud de cabecera;
- pendiente;
- tipo de suelo;
- cobertura vegetal;
- lluvia reciente;
- lluvia acumulada;
- nieve;
- deshielo;
- estación;
- temperatura;
- drenaje;
- aportes aguas arriba.

Regla conceptual:

```
cuenca
+ relieve
+ clima
+ tiempo reciente
+ nieve/deshielo
+ suelo
+ vegetación
= comportamiento hidrológico local
```

---

## 2. Sareno y Theleno

Los Sareno y Theleno constituyen los grandes ejes hidrográficos del territorio.

### Régimen general propuesto

Se consideran ríos:

- permanentes;
- de caudal variable;
- alimentados por lluvias;
- alimentados por deshielo;
- alimentados por numerosos afluentes y manantiales.

No presentan un caudal uniforme durante todo el año.

### Estacionalidad

Se propone:

- **primavera:** caudales altos por deshielo + lluvia;
- **verano:** descenso general, aunque con crecidas puntuales por tormentas;
- **otoño:** recuperación progresiva del caudal con el aumento de lluvias;
- **invierno:** caudal sostenido o alto en zonas bajas, mientras parte de la precipitación queda temporalmente almacenada como nieve en montaña.

---

## 3. Cabeceras de montaña

Las cabeceras de Sareno y Theleno se alimentan mediante:

- manantiales;
- arroyos permanentes;
- escorrentía;
- nieve acumulada;
- fusión estacional;
- lluvias orográficas.

No se propone un nacimiento único necesariamente visible como “un punto”.

Puede existir una red de pequeños cursos que convergen progresivamente.

---

## 4. Afluentes permanentes

Serán más probables cuando:

- la cuenca tenga tamaño suficiente;
- exista aporte de manantiales;
- el suelo y la geología permitan alimentación base;
- reciban agua de zonas boscosas o montañosas;
- tengan aportes de nieve o lluvias regulares.

Su caudal puede bajar mucho en verano sin llegar a desaparecer.

---

## 5. Arroyos estacionales

Se consideran normales en:

- piedemonte;
- laderas;
- vaguadas;
- barrancos;
- zonas de deshielo;
- suelos con escorrentía elevada.

Pueden llevar agua durante:

- semanas;
- meses;
- solo después de lluvias;
- solo durante el deshielo.

No necesitan nombre propio.

---

## 6. Cauces efímeros

Pueden aparecer tras:

- tormentas intensas;
- lluvia prolongada;
- deshielo rápido;
- saturación del suelo.

Un cauce seco durante gran parte del año puede transformarse temporalmente en un arroyo activo.

Esto debe ser una posibilidad real del motor.

---

## 7. Bosque Negro y escorrentía

La cobertura forestal tiende a:

- reducir parte de la escorrentía inmediata;
- aumentar infiltración;
- ralentizar el movimiento superficial del agua;
- sostener humedad más tiempo;
- favorecer pequeños manantiales y cursos de respuesta lenta.

Pero si:

- el suelo está saturado;
- la lluvia es intensa;
- coincide con deshielo;

el bosque también puede generar crecidas fuertes.

No se tratará como una “esponja infinita”.

---

## 8. Tierras abiertas

Las tierras abiertas responderán más rápido a lluvias intensas cuando:

- el suelo sea compacto;
- exista pendiente;
- falte cobertura vegetal;
- el terreno esté saturado.

Pueden aparecer:

- regueros;
- erosión;
- barro;
- escorrentía superficial;
- arrastre de sedimentos.

---

## 9. Llanuras aluviales

En torno a Sareno y Theleno pueden existir sectores bajos propensos a:

- inundación temporal;
- meandros;
- brazos secundarios;
- charcas residuales;
- suelos muy húmedos;
- depósito de sedimentos.

No toda la llanura fluvial debe inundarse cada año.

Las inundaciones deben depender de:

- caudal;
- duración del episodio;
- altura local del terreno;
- drenaje;
- defensas o modificaciones humanas si las hubiera.

---

## 10. Crecidas

### Crecidas lentas

Pueden producirse por:

- varios días de lluvia;
- saturación progresiva;
- deshielo sostenido.

Tienden a afectar:

- grandes ríos;
- llanuras bajas;
- vados;
- terrenos agrícolas.

### Crecidas rápidas

Pueden producirse por:

- tormentas intensas;
- cuencas pequeñas;
- barrancos;
- pendientes fuertes.

Tienden a afectar:

- arroyos;
- pasos estrechos;
- zonas de montaña;
- cauces efímeros.

---

## 11. Coincidencia lluvia + deshielo

Se considera uno de los escenarios de mayor riesgo hidrológico.

Puede provocar:

- aumento rápido del caudal;
- desbordamientos;
- desaparición de vados;
- daños en puentes menores;
- erosión;
- corrimientos;
- caminos cortados;
- aislamiento temporal.

---

## 12. Estiaje

En verano puede producirse un descenso notable de caudal.

Más marcado en:

- arroyos pequeños;
- tierras interiores;
- sectores con poca alimentación subterránea.

Menos marcado en:

- grandes cauces;
- cursos alimentados por montaña;
- manantiales;
- sectores húmedos del Bosque Negro.

No se propone que Sareno y Theleno se sequen.

---

## 13. Manantiales

Serán especialmente plausibles en:

- piedemonte;
- contactos entre materiales permeables e impermeables;
- laderas;
- zonas boscosas;
- valles de montaña.

Pueden alimentar:

- fuentes;
- arroyos;
- abrevaderos;
- pequeños humedales.

No todos tendrán nombre propio.

---

## 14. Humedales y zonas encharcables

Pueden aparecer localmente donde coincidan:

- relieve plano;
- drenaje lento;
- proximidad a río;
- nivel freático alto;
- lluvias;
- deshielo.

No se propone por ahora un gran sistema pantanoso regional salvo decisión posterior.

---

## 15. Vados

La utilidad de un vado no debe ser fija durante todo el año.

Puede ser:

- practicable en verano;
- difícil en otoño;
- peligroso o imposible en primavera;
- inutilizable durante una crecida.

Esto tiene mucho valor para gameplay y rutas dinámicas.

---

## 16. Puentes

Los puentes principales deben situarse donde:

- la ruta lo justifique;
- el cauce sea estable;
- exista valor estratégico;
- la profundidad o corriente hagan poco fiable un vado.

Puentes menores pueden sufrir:

- daños;
- bloqueo por troncos;
- socavación;
- cierre temporal.

---

## 17. Erosión y transporte de sedimentos

La red hidrográfica puede transportar:

- tierra;
- arena;
- grava;
- ramas;
- troncos;
- materia orgánica.

Esto aumenta durante:

- tormentas;
- deshielo;
- crecidas.

Puede modificar localmente:

- vados;
- márgenes;
- barras de grava;
- pequeños brazos del cauce.

---

## 18. Persistencia del estado hidrológico

Un curso no debe volver inmediatamente a su estado normal cuando deja de llover.

Debe existir memoria ambiental.

Ejemplo:

```
caudal previo
+ lluvia acumulada
+ deshielo
+ aportes aguas arriba
- drenaje
- infiltración
- evaporación
= estado actual del cauce
```

---

## 19. Inferencia para cursos no diseñados

Un arroyo desconocido puede inferirse mediante:

```
posición
+ cuenca
+ pendiente
+ altitud
+ lluvia reciente
+ estación
+ nieve/deshielo
+ suelo
+ vegetación
= estado del arroyo
```

Ejemplos:

- arroyo de bosque tras varios días húmedos → caudal sostenido;
- barranco interior en verano seco → casi seco;
- cauce de piedemonte en primavera → fuerte caudal;
- vaguada tras tormenta → curso efímero activo.

---

## 20. Aplicación jugable

La hidrología puede afectar:

- rutas;
- puentes;
- vados;
- pesca;
- agricultura;
- inundaciones;
- barro;
- acceso a zonas;
- sonido ambiental;
- riesgo de ahogamiento;
- escenas narrativas;
- persistencia del mundo.

La prioridad no es simular hidráulica real completa, sino producir consecuencias plausibles y coherentes.
