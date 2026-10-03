# Villas de Treskal — población, hogares y edificios

## Estado

**CANON DE GENERACIÓN — BASE DEMOGRÁFICA FUNCIONAL**

## Objetivo

Definir cómo convertir los **2.000–4.500 residentes** de una Villa en hogares, unidades residenciales, edificios y población flotante sin fijar familias concretas.

---

# 1. Población residente

La cifra canónica de población se refiere a **residentes habituales**.

No incluye automáticamente:

- viajeros de paso;
- comerciantes temporales;
- marineros no residentes;
- trabajadores estacionales;
- aldeanos que acuden al mercado;
- convoyes;
- funcionarios visitantes.

Por tanto, la población presente durante el día puede superar de forma notable la población residente.

---

# 2. Unidades domésticas

La Villa utiliza la misma lógica familiar básica del territorio.

Pueden existir:

- parejas con o sin hijos;
- familias extensas;
- viudos;
- personas solas;
- hermanos adultos;
- aprendices residentes;
- trabajadores integrados en hogares;
- sirvientes cuando el nivel económico lo justifique.

No existe una familia urbana estándar obligatoria.

---

# 3. Ocupación de vivienda

Como referencia inicial se conserva la franja regional usada para Pueblos:

- **2–8 residentes** por unidad residencial como intervalo común;
- **4–6** como núcleo frecuente;
- casos mayores cuando exista familia extensa, aprendices, servicio o trabajadores.

La generación de Villa añade una diferencia:

**edificio residencial != hogar**

Un edificio puede contener:

- una vivienda familiar;
- vivienda + taller;
- vivienda + comercio;
- más de una unidad doméstica claramente separada cuando la arquitectura lo permita.

Esto no equivale a bloques modernos de apartamentos.

---

# 4. Edificios mixtos

En zonas centrales son frecuentes:

- tienda abajo + vivienda arriba;
- taller + vivienda;
- taberna + vivienda;
- posada + vivienda del propietario;
- almacén pequeño + vivienda;
- despacho o actividad administrativa + dependencias residenciales.

El generador debe distinguir:

- edificio;
- unidad residencial;
- hogar.

---

# 5. Viviendas de trabajadores

Determinadas actividades pueden concentrar mano de obra.

Puede existir alojamiento asociado a:

- astilleros;
- grandes almacenes;
- talleres;
- servicio de una Casa menor;
- trabajos temporales.

No se genera por defecto un barracón masivo.

El alojamiento puede resolverse mediante:

- hogares locales;
- alquiler de habitaciones;
- posadas;
- viviendas próximas;
- dependencias laborales cuando exista razón funcional.

---

# 6. Población flotante

Debe modelarse por separado de la población residente.

Puede aumentar por:

- mercado;
- puerto;
- llegada de barcos;
- convoyes;
- temporadas de trabajo;
- ferias o eventos;
- administración;
- cosechas.

La población flotante afecta a:

- tráfico;
- consumo;
- ocupación de posadas;
- densidad visual;
- demanda temporal.

No debe alterar el censo persistente salvo que una persona se establezca realmente.

---

# 7. Edificios funcionales

Además de viviendas deben generarse edificios o espacios para:

- administración;
- justicia;
- comercio;
- posadas;
- tabernas;
- talleres;
- almacenes;
- graneros;
- establos;
- mercados;
- funciones propias del perfil.

Muchos pueden compartir estructura con viviendas.

---

# 8. Capacidad antes que conteo

El generador debe priorizar la **capacidad funcional necesaria** y después decidir cuántos edificios la proporcionan.

Ejemplo:

una Villa puede resolver determinada capacidad de panificación mediante:

- varias panaderías pequeñas;
- menos panaderías de mayor capacidad;
- combinación con hornos y producción doméstica.

Por tanto:

**capacidad necesaria != número fijo de edificios**

---

# 9. Perfil V1

La Villa costera debe generar población vinculada a:

- construcción naval;
- puerto;
- almacenes;
- transporte;
- comercio;
- pesca;
- servicios.

La llegada de barcos y trabajadores puede elevar mucho la población flotante.

---

# 10. Perfil V2

La Villa forestal debe generar población vinculada a:

- logística;
- madera;
- carros;
- animales de tiro;
- almacenamiento;
- administración;
- reparación;
- comercio.

Convoyes y trabajadores forestales pueden aumentar temporalmente la población presente.

---

# 11. Perfil V3

La Villa agroganadera debe generar población vinculada a:

- mercado;
- almacenamiento;
- transporte;
- ganadería;
- alimentación;
- molienda;
- comercio.

El mercado diario provoca una población flotante elevada y variable, especialmente en épocas de cosecha o grandes movimientos de ganado.

---

# 12. Persistencia

Deben persistirse:

- población residente;
- hogares;
- unidades residenciales;
- edificios;
- profesiones;
- ocupaciones;
- capacidad de servicios.

La población flotante se resuelve mediante sistemas dinámicos y no se almacena como residentes permanentes salvo cambio real de estado.

---

## Principio final

**La Villa se genera a partir de residentes y capacidades; los edificios alojan hogares y funciones; la población flotante explica por qué algunos días la Villa parece mucho mayor que su censo.**
