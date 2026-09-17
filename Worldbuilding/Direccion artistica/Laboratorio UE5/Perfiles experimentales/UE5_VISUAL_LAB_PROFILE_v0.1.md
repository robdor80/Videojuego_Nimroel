# NIMROEL — UE5 VISUAL LAB PROFILE v0.1

**Proyecto:** Videojuego Nimroel RPG  
**Documento:** Perfil experimental de generación visual para Laboratorio UE5  
**Versión:** 0.1  
**Estado:** EXPERIMENTAL / NO CANÓNICO  
**Fecha:** 2026-09-16  
**Ámbito:** Assets de prueba destinados a evaluar composición dinámica en Unreal Engine 5  
**Sustituye documentos existentes:** NO  
**Modifica canon visual existente:** NO  

---

## 1. Propósito

Este documento define reglas temporales y controladas para crear imágenes base destinadas al **Laboratorio Visual UE5 de Nimroel**.

Su objetivo es comprobar empíricamente qué elementos visuales deben:

1. quedar incorporados de forma permanente dentro del asset base;
2. generarse o modificarse dinámicamente mediante Unreal Engine 5;
3. conservar variantes propias por hora, clima o iluminación;
4. eliminarse del pipeline de generación si UE5 puede resolverlos con suficiente calidad.

Este perfil existe únicamente para pruebas técnicas y artísticas.

No debe utilizarse todavía como norma definitiva de producción de assets del videojuego.

---

## 2. Jerarquía de herencia

Este perfil se aplica siempre **después** de las Biblias y perfiles canónicos correspondientes.

Ejemplo inicial para Arleon:

`NIMROEL_GLOBAL_VISUAL_BIBLE_v0.3`  
→ `SETTLEMENT_VISUAL_BIBLE_v0.1`  
→ `NORGARD_VISUAL_PROFILE_v0.1`  
→ `ARLEON LOCAL PROFILE`  
→ `UE5_VISUAL_LAB_PROFILE_v0.1`  
→ `ARLEON_UE5_TEST_001`

Este documento puede especializar temporalmente variables de escena para facilitar el laboratorio, pero no puede contradecir:

- identidad visual global de Nimroel;
- canon geográfico;
- materiales;
- arquitectura;
- cultura;
- función del asentamiento;
- escala;
- continuidad espacial;
- reglas de plausibilidad física.

---

## 3. Principio rector

> **EL ASSET BASE REPRESENTA EL LUGAR. UE5 REPRESENTA LAS CONDICIONES DINÁMICAS QUE SE DEMUESTRE QUE PUEDE CONTROLAR CON CALIDAD SUFICIENTE.**

Durante el laboratorio se evitará incorporar al asset base cualquier fenómeno temporal que pueda ser candidato a composición dinámica posterior.

La imagen debe seguir siendo visualmente atractiva, coherente y plenamente reconocible como Nimroel.

No se generarán fondos deliberadamente planos, pobres o artificiales solo para facilitar el trabajo técnico.

---

## 4. Objetivos concretos del laboratorio

El laboratorio deberá comprobar, como mínimo, la viabilidad visual de:

- cambio de ambiente despejado a nublado;
- lluvia;
- niebla;
- tormenta;
- relámpagos;
- oscurecimiento atmosférico;
- variaciones de iluminación;
- representación nocturna;
- lunas dinámicas;
- movimiento atmosférico;
- partículas;
- parallax;
- separación aparente por planos;
- integración de audio ambiental;
- integración de efectos visuales sobre un fondo 2D;
- incorporación eventual de pequeños elementos 3D cuando aporten valor real.

---

## 5. Relación de aspecto objetivo

Los assets del laboratorio se diseñarán inicialmente para:

### 16:10

Motivo:

- MSI Raider GE78 HX: `2560 × 1600`
- Samsung Galaxy Tab S9+: `2800 × 1752` aproximadamente 16:10

La prioridad es conservar una composición común válida para ambas plataformas.

La resolución maestra definitiva no queda fijada en esta versión.

Se determinará mediante pruebas reales de:

- calidad visual;
- consumo de memoria;
- compresión;
- tamaño empaquetado;
- tiempo de carga;
- rendimiento;
- comportamiento en Windows;
- comportamiento en Android.

---

## 6. Estructura visual recomendada

Las imágenes exteriores de prueba deberán favorecer una lectura clara de profundidad:

**primer plano → plano medio → fondo → cielo / atmósfera**

Cuando sea posible, la composición debe facilitar una futura separación conceptual o física en capas.

Debe evitarse:

- profundidad falsa;
- desenfoque excesivo;
- composición totalmente plana;
- elementos importantes fusionados entre varios planos;
- exceso de objetos superpuestos que dificulten posibles máscaras o recortes;
- cielo extremadamente pequeño si se pretende probar meteorología o lunas.

---

## 7. Regla de neutralidad del asset base

El asset base debe contener el lugar y su identidad permanente.

Debe evitar incorporar fenómenos temporales que sean objeto de prueba en UE5.

### No incorporar por defecto

- lluvia;
- nieve cayendo;
- granizo;
- tormenta;
- relámpagos;
- niebla circunstancial intensa;
- nubes dramáticas de tormenta;
- partículas decorativas;
- ceniza circunstancial;
- polvo atmosférico dramático;
- hojas volando por viento circunstancial;
- lunas;
- auroras;
- efectos mágicos temporales;
- halos;
- rayos de luz irreales;
- dramatización meteorológica artificial.

Las excepciones requerirán que el fenómeno forme parte **permanente e inseparable de la localización**, no de las condiciones temporales.

---

## 8. Estado del terreno

El terreno debe ser coherente con la localización y la estación, pero no debe introducir señales visuales de un fenómeno temporal que se pretende añadir después mediante UE5.

Para una base neutra:

- evitar charcos recientes si se quiere probar lluvia posteriormente;
- evitar nieve recién caída si la nieve será una capa dinámica;
- evitar barro extremo provocado por una tormenta concreta;
- evitar reflejos húmedos generalizados si la lluvia no forma parte del asset;
- conservar humedad natural cuando sea propia del entorno.

La finalidad es no crear contradicciones entre el fondo y los efectos posteriores.

---

## 9. Cielo

El cielo debe diseñarse de manera controlada.

Para `DAY_NEUTRAL`:

- luz natural;
- nubosidad moderada o discreta;
- ausencia de nubes de tormenta;
- ausencia de fenómenos espectaculares;
- suficiente espacio visual para probar capas atmosféricas.

Para `OVERCAST_NEUTRAL`:

- cielo cubierto coherente;
- sin lluvia;
- sin rayos;
- sin niebla intensa;
- sin dramatización de tormenta.

Para `NIGHT_NEUTRAL`:

- noche físicamente creíble;
- sin lunas visibles;
- sin auroras;
- sin meteorología dramática;
- estrellas solo si no interfieren con la prueba;
- suficiente lectura del cielo para añadir posteriormente las lunas de Nimroel.

---

## 10. Iluminación

La iluminación debe ser naturalista y físicamente coherente con la Biblia Global.

El laboratorio necesita conservar suficiente neutralidad para que UE5 pueda modificar la percepción atmosférica sin luchar contra una iluminación demasiado extrema ya horneada.

Evitar como base:

- golden hour extrema;
- puesta de sol espectacular;
- contraluces extremos;
- rayos solares dramáticos;
- iluminación fuertemente coloreada;
- noches excesivamente luminosas;
- sombras imposibles;
- fuentes de luz no justificadas.

Esto no implica crear una imagen aburrida.

La escena debe seguir teniendo dirección fotográfica, belleza y lectura espacial.

---

## 11. Lunas

Para cualquier variante `NIGHT_NEUTRAL` del laboratorio:

### NO deben aparecer lunas horneadas en el asset.

La finalidad es comprobar si UE5 puede representar dinámicamente:

- presencia o ausencia;
- posición;
- tamaño aparente;
- fase;
- identidad visual;
- intensidad;
- contribución lumínica.

Las tres lunas deberán respetar posteriormente la definición vigente de la `NIMROEL_GLOBAL_VISUAL_BIBLE_v0.3`.

El laboratorio no modifica su canon astronómico.

---

## 12. Meteorología

La meteorología variable se considera candidata prioritaria a representación dinámica.

El asset base debe evitar incorporar permanentemente:

- lluvia;
- tormenta;
- niebla temporal;
- relámpagos;
- nieve cayendo;
- viento visible mediante partículas circunstanciales.

El laboratorio determinará qué fenómenos pueden trasladarse definitivamente a UE5 y cuáles siguen necesitando variantes gráficas específicas.

---

## 13. Variantes iniciales obligatorias

Para la primera localización se prepararán, como máximo, tres variantes controladas.

### A — DAY_NEUTRAL

- día;
- luz natural neutra;
- sin lluvia;
- sin tormenta;
- sin niebla circunstancial;
- sin relámpagos;
- sin lunas;
- suelo sin señales meteorológicas extremas;
- composición base principal.

### B — OVERCAST_NEUTRAL

- misma localización;
- mismo encuadre;
- misma geografía;
- misma arquitectura;
- mismo estado estructural;
- cielo cubierto;
- iluminación coherentemente más plana y fría;
- sin lluvia;
- sin rayos;
- sin niebla intensa.

### C — NIGHT_NEUTRAL

- misma localización;
- mismo encuadre;
- misma geografía;
- misma arquitectura;
- sin lunas visibles;
- sin tormenta;
- sin lluvia;
- sin niebla circunstancial intensa;
- fuentes de luz locales coherentes con el mundo;
- suficiente oscuridad para ser claramente noche;
- suficiente lectura visual para conservar materiales y espacio.

---

## 14. Continuidad entre variantes

Las variantes de una misma localización deben conservar de forma estricta:

- encuadre;
- punto de vista;
- distancia;
- perspectiva;
- geografía;
- edificios;
- carreteras;
- puentes;
- ríos;
- hitos;
- materiales;
- estructura urbana;
- escala;
- elementos permanentes;
- distribución espacial.

Solo pueden variar las condiciones expresamente sometidas a prueba.

No debe aceptarse una variante que parezca una reinterpretación nueva del lugar.

---

## 15. Primera localización recomendada

### ARLEON

Motivos:

- ciudad relevante y bien definida;
- arquitectura y materiales establecidos;
- región agrícola;
- ríos;
- puentes;
- carreteras;
- llanuras;
- profundidad visual;
- mezcla de ciudad y entorno rural;
- oportunidades claras para probar atmósfera;
- suficiente cielo;
- suficientes planos de profundidad;
- buena variedad de materiales.

Arleon deberá conservar su identidad como:

- centro administrativo y logístico del este de Norgard;
- ciudad no amurallada;
- arquitectura de piedra y madera;
- tejados de pizarra;
- gran peso de almacenes, graneros, establos y logística;
- entorno agrícola extenso;
- geografía coherente con su perfil local.

---

## 16. Nombre inicial del benchmark

Se propone:

`ARLEON_UE5_TEST_001`

Variantes:

- `ARLEON_UE5_TEST_001_DAY_NEUTRAL`
- `ARLEON_UE5_TEST_001_OVERCAST_NEUTRAL`
- `ARLEON_UE5_TEST_001_NIGHT_NEUTRAL`

Este sistema de nombres es provisional y pertenece al laboratorio.

---

## 17. Regla de imagen maestra

La primera imagen aprobada de la serie debe actuar como **referencia espacial maestra**.

Las variantes posteriores deberían generarse mediante edición o transformación de esa imagen siempre que sea posible.

No se recomienda regenerar desde cero cada variante si eso altera:

- composición;
- edificios;
- relieve;
- caminos;
- proporciones;
- posición de puentes;
- identidad urbana.

La continuidad es más importante que obtener tres imágenes individualmente espectaculares.

---

## 18. Parallax y 2.5D

El laboratorio evaluará si una imagen puede beneficiarse de separación en capas como:

1. primer plano;
2. plano medio;
3. ciudad o sujeto principal;
4. fondo;
5. montañas o horizonte;
6. cielo.

No todas las imágenes deberán terminar separadas físicamente en seis capas.

El objetivo es comprobar:

- ganancia visual;
- dificultad técnica;
- artefactos;
- necesidad de retoque;
- comportamiento en movimiento;
- coste de producción;
- rendimiento.

---

## 19. Elementos 3D

Los elementos 3D no son obligatorios.

Solo se incorporarán si aportan una mejora visual clara respecto a una solución 2D o 2.5D.

Candidatos posibles:

- lunas;
- pequeños objetos móviles;
- mecanismos;
- puertas;
- ruedas;
- elementos de primer plano;
- aves o criaturas lejanas;
- elementos arquitectónicos concretos;
- objetos que necesiten volumen o rotación real.

No se utilizará 3D por demostrar que UE5 puede hacerlo.

---

## 20. Regla de coste artístico

> **UTILIZAR LA TÉCNICA MÁS BARATA QUE PRODUZCA EL RESULTADO VISUAL DESEADO.**

Orden preferente de evaluación:

1. asset 2D puro;
2. asset 2D + efectos UE5;
3. asset 2D + parallax / 2.5D;
4. asset 2D + efectos + pequeño elemento 3D;
5. soluciones más complejas solo si existe una justificación clara.

---

## 21. Criterio de éxito

Una capacidad de UE5 se considerará candidata a producción real si:

- mejora claramente la escena;
- no parece un filtro barato;
- mantiene la identidad de Nimroel;
- funciona de forma reutilizable;
- puede automatizarse o parametrizarse;
- no exige trabajo artístico manual excesivo;
- puede ser implementada y mantenida con ayuda de Codex;
- funciona satisfactoriamente en MSI;
- funciona satisfactoriamente en Samsung Galaxy Tab S9+;
- no obliga a degradar de forma importante la experiencia.

---

## 22. Criterio de fracaso

Una técnica se rechazará si:

- rompe la coherencia del fondo;
- parece superpuesta artificialmente;
- produce artefactos difíciles de corregir;
- exige demasiado trabajo manual por asset;
- requiere conocimientos artísticos o 3D especializados por parte de Roberto;
- funciona bien solo en una escena concreta;
- degrada en exceso el rendimiento de la S9+;
- exige duplicar innecesariamente el volumen de assets;
- produce una mejora visual demasiado pequeña para su coste.

---

## 23. Dispositivos objetivo del laboratorio

### Principal

**MSI Raider GE78 HX**

La versión Windows deberá servir como referencia de máxima calidad visual razonable.

### Secundario

**Samsung Galaxy Tab S9+**

La versión Android deberá conservar la misma realidad visual general aunque pueda utilizar:

- menos partículas;
- materiales más simples;
- menor complejidad de efectos;
- ajustes gráficos específicos;
- diferentes niveles internos de calidad.

El teléfono móvil no forma parte actualmente de los requisitos del laboratorio.

---

## 24. Variables que deben medirse

Durante el benchmark deberán registrarse, cuando proceda:

- FPS;
- estabilidad;
- uso de RAM;
- uso de VRAM cuando pueda medirse;
- temperatura;
- tiempo de carga;
- tamaño del proyecto;
- tamaño de la build;
- tamaño de texturas;
- consumo de almacenamiento;
- comportamiento de efectos;
- calidad perceptual;
- diferencias Windows / Android;
- dificultad de implementación;
- dificultad de mantenimiento;
- facilidad de reutilización.

---

## 25. Preguntas que debe responder el laboratorio

1. ¿Basta un único fondo diurno neutro?
2. ¿Necesitamos una variante específica de cielo cubierto?
3. ¿Necesitamos una variante nocturna separada?
4. ¿Puede UE5 añadir lluvia convincente?
5. ¿Puede UE5 añadir niebla convincente?
6. ¿Puede UE5 crear tormentas convincentes?
7. ¿Puede UE5 representar relámpagos sin romper la imagen?
8. ¿Puede UE5 añadir las tres lunas dinámicamente?
9. ¿Puede UE5 modificar suficientemente la iluminación del fondo?
10. ¿Qué parte del cielo debe venir ya integrada?
11. ¿Qué elementos necesitan 2.5D?
12. ¿Qué elementos necesitan 3D real?
13. ¿Hasta qué resolución merece la pena conservar la textura?
14. ¿Conviene un único asset por plataforma o un máster común?
15. ¿Qué diferencias de calidad necesita la S9+?
16. ¿Qué debe cambiar en la Biblia Visual?
17. ¿Qué debe cambiar en Asset Manager?
18. ¿Qué debe quedar definitivamente bajo responsabilidad del Director de Escena?

---

## 26. Consecuencias posibles después del laboratorio

### Si UE5 NO aporta suficiente valor

- este perfil se archiva;
- las Biblias canónicas permanecen intactas;
- se mantiene o revisa el pipeline gráfico anterior;
- no se introducen cambios estructurales por haber realizado el experimento.

### Si UE5 aporta valor parcial

Se documentará exactamente:

- qué fenómenos pasan al motor;
- qué variantes siguen siendo necesarias;
- qué nuevos requisitos deben tener los assets.

### Si UE5 resulta claramente viable

Los resultados podrán justificar:

- nueva versión de la Biblia Visual General;
- revisión de Biblias de categoría;
- redefinición del pipeline de assets;
- revisión de Asset Manager;
- especificación formal de assets base;
- separación entre capas permanentes y dinámicas;
- perfiles gráficos Windows / Android;
- diseño del Dynamic Scene Layer.

Ningún cambio canónico se realizará automáticamente.

---

## 27. Regla de versionado

`UE5_VISUAL_LAB_PROFILE_v0.1` debe conservarse sin sobrescritura.

Cualquier modificación relevante producirá:

- `v0.2`
- `v0.3`
- etc.

Si el laboratorio termina y sus conclusiones pasan a producción, las reglas consolidadas deberán trasladarse a los documentos canónicos correspondientes mediante nuevas versiones.

Este perfil permanecerá como registro histórico del experimento.

---

## 28. Regla final

> **NO DISEÑAR LOS ASSETS PARA DEMOSTRAR QUE UE5 FUNCIONA. DISEÑARLOS PARA DESCUBRIR HONESTAMENTE QUÉ PARTE DE NIMROEL DEBE VIVIR EN LA IMAGEN Y QUÉ PARTE DEBE VIVIR EN EL MOTOR.**

El laboratorio debe producir evidencia.

Las decisiones definitivas se tomarán después de ver el resultado real en:

- MSI;
- Samsung Galaxy Tab S9+.

---

## 29. ADN resumido del laboratorio

### CONTROLADO — NEUTRO — REPRODUCIBLE — COMPARABLE — REVERSIBLE — MEDIBLE
