# TRESKAL — City Visual Profile v0.1

## Estado

**APROBADO COMO PERFIL VISUAL LOCAL DE CIUDAD**

## Propósito

Definir la identidad visual específica de **Treskal ciudad**.

Debe combinarse con:

**GLOBAL VISUAL BIBLE → SETTLEMENT VISUAL BIBLE → NORGARD PROFILE → TRESKAL CITY VISUAL PROFILE → SCENE VARIABLES**

Este documento no sustituye al lore urbano de Treskal.

Su función es impedir que una imagen visualmente atractiva contradiga la ciudad ya diseñada.

---

# 1. Identidad visual esencial

Treskal debe sentirse como una ciudad:

- humana;
- marítima;
- fluvial;
- artesanal;
- productiva;
- sobria;
- bien mantenida;
- orgánica;
- de tamaño medio dentro de Norgard.

Su prestigio nace principalmente de:

- madera;
- ebanistería;
- carpintería;
- mobiliario;
- actividad portuaria;
- Astilleros Reales y Base Naval Principal;
- mercados;
- administración Valrik.

No debe sentirse como:

- capital imperial;
- ciudad monumental;
- fortaleza;
- metrópolis gigantesca;
- puerto industrial moderno;
- ciudad religiosa;
- ciudad fantástica genérica.

---

# 2. Geografía canónica

Treskal se sitúa:

- en costa abierta del Mar de Suthiros;
- junto a la desembocadura integrada de un río;
- con muelles fluviales;
- con puerto civil marítimo;
- con el Complejo Naval Real T08 — Astilleros Reales + Base Naval Principal — en **tierra firme de la costa oriental**, separado del puerto civil por zona litoral T04 y controles de acceso, **no separado del continente por agua**;
- con relieve inmediato suave o abierto.

## 2A. Referencia cartográfica canónica

Toda vista general, aérea o urbana que requiera posición espacial debe respetar:

- `Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Valrik/Treskal/08_Cartografia/exports/treskal_canonical_spatial_export_v1.0.geojson`;
- `Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Valrik/Treskal/08_Cartografia/mapas/treskal_plano_tecnico_canonico_v1.0.svg`.

La cartografía canónica prevalece sobre interpretaciones visuales anteriores cuando exista conflicto de:

- costa;
- río;
- puente;
- posición de sectores;
- puerto;
- Astilleros Reales;
- Base Naval Principal;
- red viaria;
- escala urbana.

No recolocar elementos para mejorar una composición visual.

## 2B. Regla INNEGOCIABLE — T08 pertenece a tierra firme

**Los Astilleros Reales (S08) y la Base Naval Principal (S13) NO ESTÁN EN UNA ISLA.**

Este requisito prevalece sobre cualquier composición artística, plano narrativo, ilustración isométrica o prompt. La superficie terrestre de T08 es parte continua del continente de Treskal. Su costa marítima y su rompeolas **no deben convertirse en un canal por detrás**, ni separar el complejo del territorio.

**Puede representarse como un saliente o península costera SOLO cuando exista una continuidad física, amplia y visualmente inequívoca con tierra firme.** No se admite una isla, islote artificial, plataforma naval independiente, canal de aislamiento, puente como único acceso, transbordador obligatorio ni un istmo tan fino que imposibilite el transporte por carros de vigas y troncos voluminosos.

- La **C05** entra por tierra desde la red de abastecimiento continental y llega a las puertas navales restringidas.
- La **C16** enlaza por tierra Astilleros (S08) y Base Naval (S13) y sirve para mover troncos, grandes maderas, materiales de construcción, carros, obreros, tripulaciones y suministros.
- Los **260 m de separación T07–T08** son **costa intermedia del sector T04**, NO un estrecho o brazo de mar que aísle T08.
- El agua está en el frente operativo marítimo, con muelles, gradas y rompeolas. Hacia la retaguardia debe verse **tierra conectada** y las rutas terrestres de suministro.
- Un recinto cerrado por murallas o vallados y controles navales **no equivale** a un recinto cercado por mar.
- **Prohibido corregir el error inventando un gran puente, un canal, una calzada sobre el agua, una fortaleza o un nuevo acceso** que no exista en el GeoJSON canónico.

### Prueba visual obligatoria para cualquier mapa o escena de Treskal

Antes de autorizar un asset:

1. Identificar el acceso terrestre **C05** y comprobar que alcanza T08 **sin cruzar agua**.
2. Comprobar que **C16** conecta S08 y S13 sobre **suelo continuo**.
3. Comprobar que el sector T08 comparte continente con la ciudad y el territorio, aunque el recinto naval sea restringido.
4. Verificar que río, costa, puente, T07, franja T04 y T08 conservan la relación espacial del export GeoJSON.
5. Preguntar visualmente: **«¿Parece una isla o un recinto al que solo se llega en barco?»**. Si la respuesta es sí, o no puede distinguirse claramente la unión terrestre, **RECHAZAR**, aunque el mapa sea espectacular.

**Referencia autoritativa:** `treskal_canonical_spatial_export_v1.0.geojson` y contratos métricos de geografía, sectores, viario y waterfront. Esta regla **no cambia** los polígonos ni la red ya cerrados: impide dibujarlos mal.

### Ilustraciones rechazadas por este error (8 de octubre de 2026)

Quedan **NO APTAS PARA CANON NI PARA PRODUCCIÓN NAP** las ilustraciones generadas anteriormente tituladas:

- **Plano Oficial de la Ciudad de Treskal**;
- **Plano Mercantil y de Tránsito de Treskal**;
- **Plano Reservado del Complejo Naval Real de Treskal**.

Motivo común: sugieren T08 como isla o masa naval segregada por agua. Sus archivos previos y ZIP no deben considerarse assets aprobados, aunque se conserve una copia para revisión histórica. Cualquier sustituto necesitará **nuevo visto bueno visual antes de generar su ZIP NAP**.

## Prohibido por defecto

- grandes montañas inmediatas;
- picos alpinos;
- acantilados espectaculares no autorizados;
- fiordos;
- grandes cascadas;
- islas dramáticas;
- valles cerrados.

El fondo debe respetar la geografía real del mapa.

---

# 3. Relación río-mar

Una vista general debe poder sugerir, cuando el ángulo lo permita:

**interior → río → muelles fluviales → desembocadura → puerto civil → mar**

No es necesario mostrar todos estos elementos en la misma imagen.

La mayor masa urbana ocupa una margen principal del cauce próximo a la desembocadura.

---

# 4. Puente principal

Existe un puente principal permanente aguas arriba de los muelles fluviales.

Puede funcionar como:

- punto de orientación;
- entrada desde interior;
- elemento compositivo secundario.

No debe dominar todas las vistas de Treskal.

No se añaden múltiples grandes puentes sin autorización.

---

# 5. Puerto civil

Debe mostrar:

- embarcaciones civiles;
- pesca;
- carga y descarga;
- almacenes;
- talleres;
- calles portuarias;
- posadas y tabernas próximas cuando proceda.

No convertirlo automáticamente en:

- enorme puerto internacional;
- base naval;
- bosque de cientos de mástiles;
- ciudad mercante mediterránea colorida.

---

# 6. Complejo Naval Real T08

Debe transmitir escala mediante:

- gradas;
- muelles militares y atraques;
- presencia ocasional de grandes navíos de las clases IV y V;
- cascos en construcción;
- madera;
- talleres;
- patios;
- trabajadores;
- marineros y tripulaciones;
- embarque de tropas o suministros cuando proceda;
- movimiento de materiales.

S08 representa los Astilleros Reales y S13 la Base Naval Principal. Ambas instalaciones pertenecen a la Corona / Casa Aethros, no a Casa Valrik.

Su carácter institucional puede mostrar heráldica real de forma funcional.

No debe parecer:

- fortaleza costera;
- palacio naval;
- base artillera de pólvora;
- complejo industrial moderno.

La escala procede del trabajo, no de monumentalidad gratuita.

---

# 7. Madera como identidad

La madera debe ser visualmente importante, pero no significa que toda Treskal esté construida exclusivamente en madera.

Debe aparecer en:

- estructuras;
- vigas;
- puertas;
- ventanas;
- talleres;
- patios;
- carros;
- almacenes;
- mobiliario;
- astilleros;
- mercancías.

La calidad del oficio debe sentirse en detalles constructivos.

---

# 8. Materiales urbanos

Base:

- piedra;
- madera;
- pizarra.

Variación según:

- función;
- edad;
- riqueza;
- humedad;
- proximidad al puerto;
- uso.

No imponer una mezcla idéntica a todos los edificios.

---

# 9. Altura

Lectura general:

- una planta: periferias, talleres, almacenes;
- dos plantas: muy común en tejido central;
- tres plantas: minoritario y justificado;
- más de tres: no tejido ordinario.

No crear skyline de torres urbanas.

---

# 10. Densidad

Treskal debe leerse como más densa que una Villa, pero con:

- patios;
- talleres;
- muelles;
- espacios de carga;
- transiciones;
- edificios de distinta altura;
- calles irregulares.

No llenar cada metro de edificación.

---

# 11. Administración Valrik

La sede Valrik debe ser:

- sobria;
- claramente bien construida;
- reconocible;
- institucional;
- integrada en la ciudad.

No debe parecer:

- castillo;
- ciudadela;
- palacio imperial;
- torre dominante.

La riqueza se expresa mediante calidad de piedra y carpintería.

---

# 11A. Recinto militar Valrik

Treskal posee un recinto militar territorial **T12** en el borde norte/nordeste interior.

Visualmente debe distinguirse de:

- S01 / sede de Casa Valrik;
- S05 / Guardia urbana;
- T08 / Astilleros Reales de la Corona.

Debe transmitir:

- disciplina;
- mantenimiento;
- uso cotidiano;
- patios de instrucción;
- barracones sobrios;
- almacenes militares;
- establos ligeros;
- movimiento de tropas y suministros cuando proceda.

Materiales:

- piedra;
- madera;
- pizarra.

Puede tener un perímetro funcional propio, pero **no debe parecer una ciudadela ni justificar una muralla urbana**.

La heráldica Valrik puede aparecer de forma funcional en escudos, accesos y dependencias militares. No llenar el recinto ni la ciudad de estandartes ambientales.

---

# 12. Mercados

Los mercados deben mostrar:

- mercancías reales;
- puestos;
- carros;
- compradores;
- espacio para circular;
- especialización contextual.

No concentrar visualmente en una única plaza:

- ganado;
- pescado;
- madera;
- alimentos;
- comercio portuario.

El sistema comercial está distribuido.

---

# 13. Tejido residencial

Debe mostrar vida ordinaria:

- viviendas;
- casas-taller;
- tiendas con vivienda;
- patios;
- ropa;
- niños cuando proceda;
- vecinos;
- pequeños trabajos;
- mantenimiento.

Treskal no es solo puerto + talleres.

---

# 14. Calles

## Principales

Pueden ser:

- más anchas;
- drenadas;
- parcialmente empedradas;
- aptas para carros.

## Secundarias

Pueden ser:

- irregulares;
- más estrechas;
- de tierra compactada;
- grava;
- pavimento parcial.

No toda la ciudad está empedrada.

---

# 15. Clima

Clima marítimo húmedo.

Visualmente puede producir:

- piedra húmeda;
- madera oscurecida por lluvia;
- bruma localizada en río/puerto;
- cielos cubiertos;
- lluvia;
- barro contextual;
- viento costero;
- claros luminosos.

No usar niebla constante como filtro estético.

---

# 16. Limpieza y mantenimiento

Treskal debe sentirse usada y mantenida.

Puede haber:

- barro;
- serrín;
- restos de trabajo;
- humedad;
- desgaste;
- reparaciones;
- suciedad localizada.

No representar:

- calles cubiertas de basura;
- fachadas ennegrecidas indiscriminadamente;
- pobreza visual universal.

---

# 17. Actividad humana

La densidad visible depende de sector y hora.

## Mercado

Más peatones y comerciantes.

## Madera

Trabajadores, aprendices, carros, materiales.

## Puerto

Marineros, pescadores, cargadores, comerciantes.

## Residencial

Familias, vecinos, actividades ordinarias.

## Administración

Mensajeros, escribanos, guardias, visitantes.

No poblar todas las vistas con multitudes.

---

# 18. Fantasía

No añadir automáticamente:

- runas;
- luces mágicas;
- estatuas gigantes;
- torres imposibles;
- cristales;
- criaturas;
- arquitectura sobrenatural.

Treskal puede verse extraordinaria por su realidad y oficio.

---

# 19. Religión

No generar:

- iglesias;
- catedrales;
- capillas;
- templos;
- campanarios;
- cruces;
- santuarios.

Nimroel no posee dioses.

---

# 20. Murallas

Treskal no posee muralla urbana general.

No añadir:

- cinturón amurallado;
- puertas monumentales de ciudad;
- torres defensivas repetidas.

Puede haber cerramientos funcionales en instalaciones concretas.

---

# 21. Heráldica

Uso contextual:

- Casa Valrik en su sede;
- Corona en Astilleros Reales;
- elementos oficiales.

No usar estandartes como decoración urbana genérica.

---

# 22. Vistas generales recomendadas

Útiles:

- ciudad desde aproximación terrestre;
- relación río-desembocadura-puerto;
- vista costera desde mar;
- ciudad desde puente principal;
- panorámica elevada moderada sin montañas inventadas.

Debe leerse:

- escala;
- agua;
- trabajo;
- tejido urbano;
- relación con territorio.

---

# 23. Vistas de calle recomendadas

Útiles:

- mercado;
- casas-taller;
- eje de carpinteros;
- muelles fluviales;
- puerto civil;
- acceso exterior al Complejo Naval Real T08;\n- muelles de la Base Naval Principal cuando la escena lo requiera;
- calles residenciales;
- administración Valrik;
- acceso o patio exterior del recinto militar T12;
- periferia de abastecimiento.

---

# 24. Referencia visual histórica

La referencia visual anterior de Treskal puede conservarse por:

- atmósfera;
- materiales;
- integración de río y actividad;
- sensación de ciudad artesanal.

Pero cualquier montaña dramática o relieve no compatible con el mapa debe considerarse **no canónico**.

---

## Regla final

**Treskal debe impresionar porque parece una ciudad real que sabe construir, comerciar y trabajar la madera junto al mar; no porque el paisaje o la arquitectura intenten ser épicos a la fuerza.**
