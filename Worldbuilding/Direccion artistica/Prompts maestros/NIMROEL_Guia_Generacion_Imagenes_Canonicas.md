# Nimroel — Conclusiones sobre generación de imágenes canónicas

## Objetivo de este documento

Recoger las conclusiones prácticas obtenidas durante las pruebas de generación de imágenes de Arleon, especialmente al intentar:

- mantener continuidad visual y espacial;
- generar variantes nocturnas;
- cambiar el punto de vista de cámara;
- preservar identidad arquitectónica, geográfica y ambiental;
- evitar deriva creativa del generador.

Este documento debe servir como guía operativa para futuras ciudades y localizaciones de Nimroel.

---

# 1. Principio principal

## La imagen de referencia pesa más que el texto

Cuando se proporciona una panorámica canónica completa, el generador tiende a conservar:

- la ciudad;
- la distribución visual;
- la composición;
- el eje del río;
- la posición relativa de los edificios;
- el encuadre;
- el punto de vista.

Esto es muy útil para generar variantes de una misma vista, pero dificulta mucho un cambio real de cámara.

### Consecuencia práctica

Si queremos:

- misma ciudad;
- misma composición;
- distinta hora;
- distinta estación;
- distinta meteorología;

la imagen canónica completa es la mejor referencia posible.

Si queremos:

- otro ángulo;
- otro punto de observación;
- otra composición;

la imagen canónica completa puede convertirse en un ancla excesivamente fuerte.

---

# 2. Un prompt más largo no siempre resuelve el problema

Las pruebas demostraron que añadir:

- grados de rotación;
- instrucciones de paralaje;
- posiciones relativas;
- reglas de cámara;
- prohibiciones;
- referencias negativas;
- croquis de desplazamiento;

mejora el control, pero no garantiza que el modelo abandone la composición visual de la referencia principal.

## Conclusión

Llega un punto en que el problema deja de ser de prompt y pasa a ser de representación visual.

El generador no está trabajando con un modelo 3D real de Arleon.

Está interpretando una imagen 2D.

---

# 3. Caso ideal: variantes de la misma vista canónica

Para imágenes ingame de ambientación, la estrategia recomendada es:

## Una ciudad = una vista canónica principal

A partir de esa vista se generan variantes de:

- día;
- noche;
- amanecer;
- atardecer;
- primavera;
- verano;
- otoño;
- invierno;
- lluvia;
- nieve;
- niebla ligera;
- cielo cubierto;
- situaciones especiales;
- crisis;
- guerra;
- evento narrativo.

## Ventajas

- reconocimiento inmediato;
- continuidad visual fuerte;
- menor deriva creativa;
- mejor coherencia entre escenas;
- pipeline más estable;
- menor necesidad de correcciones manuales.

---

# 4. Regla operativa para el juego

## Misma ciudad + distinta hora, clima o estación

Usar la misma cámara canónica.

## Otra cámara

Tratarla como un caso especial, no como el flujo estándar.

Las vistas alternativas pueden reservarse para:

- cinemáticas;
- escenas especiales;
- material de lore;
- momentos narrativos importantes;
- ilustraciones secundarias.

No deben sustituir a la vista canónica como fuente principal de identidad espacial.

---

# 5. Por qué funciona mejor la vista canónica nocturna

Durante las pruebas con Arleon se observó que una versión nocturna casi idéntica a la referencia diurna:

- preservaba mejor el río;
- preservaba mejor los puentes;
- conservaba el complejo administrativo;
- mantenía el distrito logístico;
- mantenía la escala;
- seguía siendo inmediatamente reconocible como Arleon.

Aunque el encuadre fuese casi idéntico, para uso ingame esto no suponía un problema.

## Motivo

La imagen no necesita demostrar variedad de cámara.

Necesita comunicar:

> “Es Arleon, pero ahora es de noche.”

Para una imagen de ambientación, esa función es más importante que buscar una composición novedosa.

---

# 6. Qué ocurre cuando eliminamos la referencia global

Al retirar la panorámica completa y usar únicamente recortes de:

- arquitectura;
- paisaje;
- distrito logístico;
- horizonte;

el generador adquiere más libertad de cámara.

Esto permite:

- perspectivas más diferentes;
- composiciones nuevas;
- mayor sensación de desplazamiento físico del observador.

Pero también aumenta el riesgo de:

- alterar la topología del río;
- cambiar relaciones espaciales;
- inventar zonas urbanas;
- reorganizar puentes;
- desplazar edificios;
- reinterpretar la ciudad.

## Conclusión

Se gana libertad de cámara, pero se pierde certeza espacial.

---

# 7. Límite fundamental detectado

No es realista exigir simultáneamente:

- continuidad espacial perfecta;
- fidelidad absoluta a una única referencia 2D;
- cambio fuerte de cámara;
- ausencia total de invención.

## Razón

Una imagen 2D no contiene:

- fachadas traseras;
- calles ocultas;
- relaciones exactas fuera de plano;
- geometría completa de los ramales;
- profundidad métrica real;
- disposición tridimensional completa.

Cuando el generador cambia de cámara, debe inferir o inventar parte de esa información.

---

# 8. Uso de recortes como anclas visuales

Los recortes funcionan muy bien para fijar identidad sin fijar tanto la composición global.

## Recortes útiles

### Arquitectura principal
- complejo administrativo;
- torres funcionales;
- materiales;
- cubiertas;
- proporciones.

### Distrito logístico
- almacenes;
- graneros;
- corrales;
- establos;
- muelles pequeños;
- patios de carga.

### Paisaje
- horizonte;
- llanura agrícola;
- vegetación;
- caminos;
- campos.

### Infraestructura
- puentes;
- arquitectura fluvial;
- bordes de ribera.

## Función

Los recortes responden mejor a:

> “Así es Arleon.”

La panorámica completa responde más a:

> “Así se ve Arleon desde este punto.”

---

# 9. Prohibiciones concretas funcionan mejor que reglas abstractas

Las restricciones visuales deben formularse de forma directa.

## Ejemplos eficaces

- no castillos;
- no murallas;
- no fortalezas;
- no catedrales;
- no grandes barcos;
- no puertos monumentales;
- no montañas;
- no lagos;
- no tercera luna;
- no farolas eléctricas;
- no iluminación moderna;
- no runas luminosas;
- no magia ambiental decorativa;
- no grandes monumentos;
- no skyline vertical incompatible.

## Regla

Cuanto más visual y concreto sea el veto, mejor.

---

# 10. Iluminación nocturna

Nimroel no tiene electricidad.

Una ciudad nocturna debe iluminarse únicamente mediante:

- luz lunar;
- velas;
- lámparas de aceite;
- hogares;
- braseros;
- faroles preindustriales puntuales.

## Reglas recomendadas

- la mayoría de ventanas deben permanecer oscuras;
- evitar líneas regulares de luces;
- evitar calles excesivamente iluminadas;
- reducir actividad urbana;
- incluir pocos viajeros;
- pocos guardias;
- carros mayoritariamente estacionados;
- logística casi detenida;
- humo doméstico ligero en algunas chimeneas.

El humo debe ser:

- tenue;
- irregular;
- doméstico;
- físicamente plausible.

No debe parecer contaminación industrial.

---

# 11. Estaciones y clima

Las variantes estacionales deben modificar principalmente:

- vegetación;
- color del terreno;
- presencia o ausencia de hojas;
- nieve;
- humedad;
- estado de caminos;
- nubosidad;
- luz ambiental;
- actividad humana;
- humo;
- ropa visible si procede.

## Pero deben conservar

- cámara;
- edificios principales;
- río;
- puentes;
- masa urbana;
- skyline;
- topografía;
- relaciones espaciales.

---

# 12. Jerarquía recomendada de referencias

Para una ciudad importante de Nimroel:

## Nivel 1 — Fuente visual principal
Imagen canónica diurna.

## Nivel 2 — Variantes derivadas
- nocturna;
- primavera;
- verano;
- otoño;
- invierno;
- lluvia;
- nieve;
- crisis / guerra / evento.

## Nivel 3 — Referencias secundarias
- recortes arquitectónicos;
- recortes de paisaje;
- recortes de infraestructura;
- posibles vistas alternativas.

---

# 13. Vistas alternativas

Las vistas alternativas pueden considerarse válidas si:

- mantienen la identidad;
- respetan arquitectura;
- respetan paisaje general;
- conservan lenguaje visual;
- no contradicen el canon.

Pero no deben asumirse automáticamente como fuente exacta de cartografía.

## Regla

Una vista alternativa puede ser:

- visualmente canónica;
- atmosféricamente canónica;
- arquitectónicamente canónica;

sin convertirse necesariamente en una fuente métrica exacta del trazado urbano.

---

# 14. Fuente de verdad espacial futura

Si en el futuro se desean múltiples perspectivas exactas de una misma ciudad, será necesario crear una referencia espacial independiente.

## Recomendación

Un plano cenital simplificado por ciudad con:

- río;
- ramales;
- puentes;
- barrios;
- centro administrativo;
- distrito logístico;
- edificios principales;
- carreteras;
- límites urbanos;
- orientación general.

## Ventaja

Permite separar:

- identidad visual;
- geometría espacial;
- composición fotográfica.

Esto sería mucho más útil que intentar deducir toda la ciudad tridimensional a partir de una única panorámica.

---

# 15. Regla maestra de generación

## Para variantes canónicas

**Usar imagen completa + prompt de transformación controlada.**

Ejemplos:

- noche;
- lluvia;
- nieve;
- estaciones;
- humo;
- actividad;
- iluminación.

## Para perspectivas nuevas

**Reducir el peso de la panorámica global y usar recortes + descripción espacial.**

Aceptar que la geometría exacta puede desviarse.

---

# 16. Regla de prioridad

Cuando exista conflicto entre:

1. continuidad visual;
2. variedad estética;
3. espectacularidad;
4. novedad de cámara;

debe ganar:

## CONTINUIDAD VISUAL

Para imágenes de ambientación ingame, la ciudad debe reconocerse inmediatamente.

---

# 17. Recomendación final para Nimroel

Pipeline recomendado:

1. Crear una vista canónica principal por ciudad.
2. Validarla.
3. Convertirla en fuente de verdad visual.
4. Generar todas las variantes climáticas y temporales sobre esa misma composición.
5. Mantener vistas alternativas como material secundario.
6. Crear en el futuro planos espaciales simplificados si se requieren perspectivas múltiples realmente coherentes.

---

# Resumen ejecutivo

## La regla más importante

**Misma ciudad + distinta hora / clima / estación = misma cámara canónica.**

## Segunda regla

**Otra cámara = uso excepcional.**

## Tercera regla

**La imagen canónica manda sobre la variedad visual.**

## Cuarta regla

**No exigir a una sola imagen 2D que funcione como un modelo 3D completo.**

## Quinta regla

**Si algún día necesitamos múltiples vistas exactas, habrá que añadir una fuente de verdad espacial independiente.**
