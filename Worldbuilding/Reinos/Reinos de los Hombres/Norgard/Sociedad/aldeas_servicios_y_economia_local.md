# NORGARD — SERVICIOS RURALES Y ECONOMÍA LOCAL

**Proyecto:** Videojuego Nimroel RPG  
**Ámbito:** Reino de Norgard  
**Fecha:** 2026-09-27  
**Estado:** CANON DE GAMEPLAY / BASE PARA DATOS  
**Objetivo:** fijar cómo funcionan los servicios, oficios, infraestructuras y producción cotidiana de aldeas y núcleos rurales de Norgard de forma directamente trasladable a datos de juego.

---

## 1. Principio rector

Las aldeas de Norgard **no deben funcionar como pequeños centros comerciales autosuficientes**.

No todas las aldeas deben contener el mismo conjunto de negocios, profesionales o edificios. La población obtiene una parte importante de lo que necesita mediante:

- producción doméstica;
- producción comunitaria;
- intercambio entre vecinos;
- especialistas presentes solo en determinados núcleos;
- desplazamientos a aldeas cercanas;
- mercados;
- comerciantes;
- pueblos, villas y ciudades.

Esto debe generar dependencia real entre asentamientos y favorecer que el jugador pregunte, investigue y se desplace.

### Regla de gameplay

Cuando el jugador necesita un bien o servicio, la respuesta no debe ser siempre “ve a la tienda”.

La resolución normal puede seguir cadenas como:

`hogar local -> vecino -> especialista local -> aldea cercana -> mercado -> núcleo mayor`

Los NPC deben poder informar de quién produce, vende o presta un servicio, incluso cuando esa persona se encuentre en otro asentamiento.

---

## 2. Escala de asentamientos usada por este documento

IDs de rango recomendados para futura serialización:

- `village` = aldea;
- `town` = pueblo;
- `villa` = villa;
- `city` = ciudad.

La presencia de un servicio nunca debe inferirse únicamente por tamaño cuando el canon indique otra cosa.

---

## 3. Modelo de datos recomendado

Cada servicio, oficio o infraestructura debería poder convertirse posteriormente en una entidad de datos con campos equivalentes a:

- `feature_id`: identificador estable;
- `scope`: reino, región o localidad donde aplica;
- `feature_type`: infraestructura, oficio, actividad doméstica, comercio, etc.;
- `settlement_tiers`: rangos donde puede existir;
- `availability_mode`: base, común, opcional, especialista, no estándar;
- `placement_rules`: requisitos geográficos o funcionales;
- `provider_model`: comunidad, hogar, profesional, establecimiento;
- `service_radius`: local, varias aldeas, regional;
- `provider_mobility`: fijo, desplazable, doméstico;
- `inputs`: materias primas necesarias;
- `outputs`: bienes o servicios generados;
- `trade_modes`: autoconsumo, venta local, encargo, mercado, trueque, etc.;
- `gameplay_hooks`: diálogo, compra, encargo, rumor, misión, viaje;
- `regional_overrides`: excepciones por territorio o cultura.

No fijar porcentajes artificiales de aparición mientras no exista un sistema de generación que los necesite.

---

# 4. Infraestructuras y servicios

## 4.1. Punto de agua

**feature_id:** `norgard.rural.water_source`  
**feature_type:** infraestructura básica  
**availability_mode:** base  
**settlement_tiers:** village, town, villa, city

### Canon

Toda aldea debe disponer de una fuente de agua plausible determinada por la geografía.

Formas normales:

- pozo;
- fuente o manantial natural acondicionado;
- arroyo cercano cuando la geografía lo permita.

No colocar automáticamente una fuente ornamental construida en todas las aldeas.

El agua debe proceder de la lógica física del lugar.

### Gameplay

Puede actuar como:

- punto de encuentro;
- lugar de conversaciones espontáneas;
- referencia para localizar NPC;
- zona de tareas domésticas;
- punto de abastecimiento de personas y animales.

---

## 4.2. Horno comunal

**feature_id:** `norgard.rural.communal_oven`  
**feature_type:** infraestructura comunitaria  
**availability_mode:** común / característica rural  
**settlement_tiers:** village, town

### Canon

En las aldeas de Norgard es habitual disponer de un horno comunal.

Debe concebirse como una construcción sencilla y sólida, principalmente de piedra, con un horno grande compartido por la comunidad.

Las familias pueden utilizarlo:

- por días;
- por turnos;
- por tandas;
- o mediante una persona que se encargue de hornear para varias familias.

Usos principales:

- pan cotidiano;
- empanadas;
- preparaciones horneadas;
- panes y comidas especiales durante fiestas de la aldea.

No requiere la existencia de una panadería profesional.

### Provider model

`community`

Puede existir una persona que gestione o domine especialmente el horno, pero el edificio sigue siendo de función comunitaria.

### Gameplay

Puede generar:

- horarios o tandas;
- encuentros entre vecinos;
- venta ocasional de pan;
- encargos;
- escasez de leña;
- preparativos festivos;
- rumores y conversaciones.

---

## 4.3. Molino

**feature_id:** `norgard.rural.mill`  
**feature_type:** infraestructura productiva  
**availability_mode:** opcional  
**settlement_tiers:** village, town, villa

### Canon

No toda aldea debe disponer de molino.

Un molino puede servir a varias aldeas cercanas.

Su presencia depende de:

- necesidad regional;
- producción de cereal;
- disponibilidad de agua o de la fuente de energía correspondiente;
- geografía;
- rutas de acceso.

La tecnología general permite molinos hidráulicos.

Los molinos no implican la existencia de aserraderos hidráulicos.

### Service radius

`multi_village`

### Gameplay

Puede provocar desplazamientos para:

- llevar grano;
- recoger harina;
- realizar encargos;
- intercambiar noticias con habitantes de otras aldeas.

---

## 4.4. Herrería básica

**feature_id:** `norgard.rural.basic_smithy`  
**feature_type:** oficio + taller  
**availability_mode:** regional

### Canon general

La presencia exacta de herrerías fuera de las regiones ya definidas debe resolverse por localidad.

### Override canónico — Treskal

**scope:** `Norgard/Treskal`

En toda aldea y pueblo de Treskal debe existir una herrería básica.

Su función es cubrir necesidades cotidianas como:

- reparación de herramientas;
- herrajes;
- clavos;
- piezas sencillas;
- mantenimiento agrícola;
- pequeñas reparaciones metálicas.

Un herrero avanzado o especialista es independiente del tamaño del asentamiento.

Puede existir en una aldea y no existir en un pueblo.

No asumir que toda herrería básica fabrica armamento o piezas complejas.

---

## 4.5. Taberna

**feature_id:** `norgard.rural.tavern`  
**feature_type:** establecimiento social  
**availability_mode:** base social  
**settlement_tiers:** village, town, villa, city

### Canon

Las aldeas deben disponer de algún lugar donde los vecinos puedan reunirse y tomar algo, aunque sea extremadamente humilde.

La taberna no es solo un punto de compra de bebida.

Su función principal es comunitaria:

- beber;
- conversar;
- conocer rumores;
- preguntar por personas;
- preguntar quién vende un producto;
- localizar oficios;
- realizar pequeños intercambios;
- encontrar posibles trabajos o encargos.

Puede ser desde una estancia sencilla hasta un establecimiento mucho más trabajado.

### Gameplay

La taberna debe actuar como nodo de información humana.

Ejemplos de consultas naturales:

- quién tiene ajos;
- quién vende unto;
- quién dispone de miel;
- dónde vive el carpintero;
- dónde está la curandera;
- quién necesita ayuda;
- qué ocurrió recientemente en la zona.

No debe funcionar como un “menú universal de misiones”.

---

## 4.6. Posada

**feature_id:** `norgard.rural.inn`  
**feature_type:** alojamiento + hostelería  
**availability_mode:** opcional con override regional  
**settlement_tiers:** village, town, villa, city

### Canon

La posada es más elaborada que una taberna.

Su función está orientada a viajeros y puede incluir:

- alojamiento;
- comida;
- bebida;
- estabulación o espacio para monturas cuando proceda;
- información para viajeros.

Puede incorporar una taberna o cumplir también su función social.

No todas las aldeas de Norgard necesitan una posada.

### Override canónico — Valrik

En las tierras de Valrik, incluso las aldeas suelen disponer de posada debido a su tradición de hospitalidad.

---

## 4.7. Carpintero

**feature_id:** `norgard.rural.carpenter`  
**feature_type:** oficio + taller  
**availability_mode:** opcional / especialista local  
**settlement_tiers:** village, town, villa

### Canon

No debe existir un carpintero en todas las aldeas.

Puede haber uno en una aldea concreta o en un pueblo y prestar servicio a varios núcleos cercanos.

Quien necesite:

- una puerta;
- ventanas;
- un arcón;
- mobiliario;
- reparar un carro;
- piezas de madera;
- otros encargos;

puede tener que desplazarse hasta otra aldea para contratarlo o recoger el trabajo.

El taller suele ser pequeño y puede integrarse en la vivienda o disponer de un cobertizo o patio de trabajo.

### Service radius

`multi_village`

### Override — Treskal

Treskal posee una concentración y especialización extraordinarias en trabajos de madera.

La presencia de carpinteros, ebanistas, tallistas y otros artesanos de la madera es mayor que en una región normal.

---

## 4.8. Aserradero

**feature_id:** `norgard.wood.sawmill`  
**feature_type:** infraestructura productiva mayor  
**availability_mode:** restringido por rango  
**settlement_tiers:** villa, city

### Canon

Los aserraderos grandes no pertenecen a la escala normal de aldea.

Deben reservarse para villas y núcleos mayores con:

- demanda suficiente;
- suministro estable de troncos;
- capacidad logística;
- acceso adecuado para transporte.

Una aldea puede participar en tala, preparación básica o transporte de madera sin disponer de un aserradero.

La base tecnológica del mundo permite serrado manual y no presupone aserraderos hidráulicos.

---

# 5. Salud rural

## 5.1. Remedios domésticos

**feature_id:** `norgard.rural.household_remedies`  
**feature_type:** conocimiento doméstico  
**availability_mode:** común  
**settlement_tiers:** todos

### Canon

Es habitual que habitantes rurales conozcan remedios sencillos transmitidos por experiencia familiar.

Pueden saber:

- preparar infusiones;
- limpiar heridas;
- aplicar cataplasmas o emplastos;
- tratar molestias menores;
- reconocer determinadas plantas útiles o perjudiciales.

Esto no convierte a esas personas en curanderas profesionales.

---

## 5.2. Curandera formada

**feature_id:** `norgard.rural.trained_healer`  
**feature_type:** especialista  
**availability_mode:** especialista regional  
**settlement_tiers:** village, town, villa

### Canon

No debe existir una curandera formada en todas las aldeas.

Una curandera puede vivir en una aldea o pueblo y atender varios asentamientos cercanos.

Sus conocimientos se han adquirido durante años y suelen proceder de transmisión de otras curanderas anteriores.

Campos posibles de conocimiento:

- plantas medicinales;
- ungüentos;
- emplastos;
- infusiones;
- heridas;
- fiebres;
- dolencias comunes;
- asistencia a partos.

No debe tratarse como una médica moderna ni como alguien capaz de curarlo todo.

### Tradición cultural

En Norgard, la curandería especializada es predominantemente femenina.

La transmisión histórica del oficio se produce principalmente de mujer a mujer.

No se establece una prohibición biológica o legal absoluta para los hombres; se fija una tradición cultural dominante.

### Provider mobility

`travels_to_client`

Cuando el enfermo no puede desplazarse, existe la posibilidad de que la curandera viaje hasta otra aldea.

### Service radius

`multi_village`

### Gameplay

El jugador puede:

- preguntar dónde vive la curandera;
- descubrir que está atendiendo a alguien en otra localidad;
- llevarle plantas o materiales;
- solicitar tratamiento;
- acompañarla;
- recibir información sobre quién conoce determinados remedios.

---

# 6. Producción doméstica y comercio no especializado

## 6.1. Carne y animales domésticos

**feature_id:** `norgard.rural.household_meat_production`  
**feature_type:** producción doméstica  
**availability_mode:** común

### Canon

La carne rural no depende de una carnicería estable en cada aldea.

Las familias pueden criar según región, riqueza y recursos:

- vacas;
- cerdos;
- ovejas;
- gallinas;
- conejos;
- otros animales domésticos permitidos por el canon regional.

El sacrificio y aprovechamiento pueden realizarse en el ámbito doméstico o con ayuda de vecinos experimentados.

### Regla negativa

**No generar carnicería profesional como servicio estándar de aldea.**

Las carnicerías permanentes pertenecen con mayor naturalidad a núcleos con suficiente población y demanda no autosuficiente.

---

## 6.2. Alfarería y bienes duraderos

**feature_id:** `norgard.rural.pottery_supply`  
**feature_type:** abastecimiento externo / comercio  
**availability_mode:** no requiere especialista local

### Canon

Una aldea no necesita disponer de alfarero propio.

La población puede obtener:

- ollas;
- jarras;
- cuencos;
- cántaros;
- otros recipientes;

mediante:

- mercados;
- comerciantes;
- desplazamientos a otros asentamientos;
- especialistas situados en lugares con tradición o materias primas adecuadas.

Puede existir excepcionalmente un alfarero en una aldea, pero no debe generarse como servicio estándar.

---

# 7. Apicultura

## 7.1. Producción apícola doméstica

**feature_id:** `norgard.rural.beekeeping`  
**feature_type:** actividad rural complementaria  
**availability_mode:** común pero no universal  
**settlement_tiers:** village, town, villa

### Canon

La apicultura puede formar parte de la economía doméstica de determinadas familias.

No es necesario que exista un “apicultor profesional” como establecimiento independiente.

Un vecino puede mantener unas pocas colmenas para autoconsumo.

Otro, con mayor experiencia, puede mantener más colmenas y ser conocido en varias aldeas por su producción.

### Outputs

- miel;
- cera;
- productos derivados que posteriormente defina el sistema de objetos;
- miel destinada a producción de hidromiel.

### Trade modes

- autoconsumo;
- venta directa;
- intercambio entre vecinos;
- suministro a tabernas o posadas;
- venta en mercado;
- producción para otros elaboradores.

### Hidromiel

La hidromiel puede elaborarse:

- de forma doméstica;
- por tabernas;
- por productores más especializados.

No asumir una industria centralizada en la escala de aldea.

### Gameplay

La apicultura permite:

- localizar proveedores concretos mediante diálogo;
- comprar miel o cera directamente a un hogar;
- encargos relacionados con colmenas;
- abastecimiento de tabernas;
- variaciones locales de hidromiel;
- rutas económicas entre aldeas.

---

# 8. Reglas negativas de generación

Al generar o diseñar una aldea de Norgard, evitar automáticamente:

- una tienda general que venda de todo;
- una carnicería en cada aldea;
- un alfarero en cada aldea;
- un carpintero en cada aldea;
- una curandera en cada aldea;
- un molino en cada aldea;
- un aserradero en una aldea;
- un conjunto idéntico de servicios en todos los asentamientos;
- NPC profesionales creados únicamente porque el jugador pueda necesitarlos.

La ausencia de un servicio **es contenido de gameplay**, porque obliga a:

- preguntar;
- conocer la zona;
- viajar;
- recurrir a vecinos;
- esperar un mercado;
- localizar a un especialista;
- crear relaciones entre asentamientos.

---

# 9. Regla para generación procedural o asistida

Una futura herramienta de generación de asentamientos deberá resolver los servicios en este orden:

1. **Geografía y recursos:** qué puede existir físicamente.
2. **Rango del asentamiento:** aldea, pueblo, villa o ciudad.
3. **Reglas regionales:** por ejemplo Treskal o Valrik.
4. **Necesidades de la población:** agricultura, ganadería, rutas, producción.
5. **Servicios compartidos:** comprobar si una aldea cercana ya cubre la necesidad.
6. **Especialización local:** añadir oficios solo cuando exista una causa.
7. **Red económica:** determinar de dónde llegan los bienes que no se producen localmente.

La generación debe poder producir de forma válida dos aldeas vecinas con perfiles distintos.

Ejemplo conceptual:

- Aldea A: taberna, horno comunal, pozo, herrería básica.
- Aldea B: taberna, horno comunal, manantial, molino y curandera.
- Ambas: comparten carpintero situado en un tercer núcleo.
- La alfarería llega mediante mercado.
- El aserradero se encuentra en una villa.

Esto no es una plantilla fija, sino una demostración de dependencia entre asentamientos.

---

# 10. Preparación para JSON

Este documento debe considerarse **fuente canónica humana**.

Cuando el RPG Core necesite estos datos, deberán extraerse a uno o varios archivos estructurados sin cambiar las reglas de canon.

Separación recomendada:

- definiciones de características;
- reglas de disponibilidad;
- overrides regionales;
- catálogo de bienes y servicios;
- relaciones entre asentamientos;
- proveedores NPC concretos;
- estado dinámico de cada partida.

No mezclar en un único JSON:

- canon estático;
- instancia concreta de una aldea;
- NPC individual;
- inventario dinámico;
- estado de misión.

Los IDs definidos en este documento deben conservarse estables cuando se cree la capa de datos.
