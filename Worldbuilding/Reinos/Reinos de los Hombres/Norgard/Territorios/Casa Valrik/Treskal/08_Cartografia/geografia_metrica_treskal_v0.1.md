# Treskal — geografía métrica v0.1

## Estado

**PLANO MÉTRICO — PUNTO 3 CERRADO**

Marcador:

`TRESKAL_METRIC_PLAN_POINT_3_GEOGRAPHY_CLOSED`

Contrato operativo:

`../Datos operativos/treskal_metric_geography_contract_v0.1.json`

---

## 1. Objetivo

Punto 3 fija la geometría física sobre la que se encajará Treskal.

Quedan congelados:

- trazado del río dentro de la envolvente;
- anchura y profundidad por tramos;
- desembocadura;
- forma de costa;
- cotas y pendientes;
- zonas inundables;
- posición y geometría del Puente de los Gemelos;
- necesidad o no de pasos menores;
- relación exacta agua–T01–T07–T08.

Punto 3 **no** coloca todavía:

- polígonos exactos T01–T12;
- parcelas S01–S13;
- calles;
- muelles detallados;
- gradas;
- dársenas;
- manzanas.

---

## 2. Sistema local de coordenadas

Se adopta:

`TRESKAL_LOCAL_METRIC_V1`

Unidades:

**metros**.

Origen:

**centro del thalweg en la desembocadura, al cortar la línea media de costa.**

Ejes:

- +X = este;
- +Y = norte;
- Z = cota sobre datum local de nivel medio del mar;
- Z=0 no pretende ser una referencia geodésica global de Nimroel.

Ventana métrica de control:

- X: **−450 a +2.050 m**;
- Y: **−120 a +1.380 m**;
- control total: **2.500 × 1.500 m**.

Esta ventana **no** es el perímetro urbano.

La envolvente terrestre sigue siendo irregular y debe respetar las **250 ha objetivo** del Punto 2.

---

## 3. Orientación regional

La geometría local queda fijada de modo compatible con el mapa regional:

- el río llega desde **N/NO**;
- desagua hacia **S/SE**;
- el mar abre al **sur y sudeste**;
- la masa urbana principal ocupa la **margen oriental**;
- hidrológicamente esa margen es la **margen izquierda mirando aguas abajo**.

Treskal no se convierte en una ciudad simétrica a dos márgenes.

La orilla occidental queda principalmente como:

- aproximación territorial;
- vega;
- terreno de transición;
- área de riesgo fluvial.

---

# 4. Río

## 4.1 Modelo

El río urbano es un **cauce principal único de carácter estuarino en su tramo final**.

No se crea:

- delta urbano;
- isla permanente en la propia boca;
- segundo cauce urbano equivalente.

Puede existir hidrografía regional fuera de la ventana métrica, pero no altera la boca canónica de Treskal.

---

## 4.2 Eje del cauce

Cadena desde la desembocadura aguas arriba:

| Punto | PK desde boca | X | Y |
|---|---:|---:|---:|
| R00 | 0 m | 0 | 0 |
| R01 | 164 m | -35 | 160 |
| R02 | 340 m | -80 | 330 |
| R03 | 525 m | -125 | 510 |
| R04 | 706 m | -145 | 690 |
| R05 | 886 m | -105 | 865 |
| R06 | 1.063 m | -155 | 1.035 |
| R07 | 1.247 m | -225 | 1.205 |
| R08 | 1.424 m | -250 | 1.380 |

Longitud del cauce dentro de la ventana:

**~1.424 m**.

La curva es suave.

No se permiten meandros exagerados destinados a alargar artificialmente el frente urbano.

---

## 4.3 Anchura y profundidad

Se fija la siguiente sección de diseño:

| PK | ancho normal | ancho a cauce lleno | profundidad normal del thalweg |
|---|---:|---:|---:|
| 0 m | 100 m | 118 m | 4,5 m |
| 200 m | 82 m | 98 m | 4,0 m |
| 400 m | 72 m | 88 m | 3,5 m |
| 600 m | 64 m | 80 m | 3,1 m |
| 850 m | 58 m | 72 m | 2,6 m |
| 1.100 m | 54 m | 68 m | 2,2 m |
| 1.424 m | 50 m | 64 m | 1,9 m |

Resultado funcional:

- T01 recibe embarcaciones fluviales mercantes pequeñas;
- la pesca fluvial puede operar;
- el río no se convierte en puerto marítimo profundo;
- los grandes buques marítimos y navales no deben remontarlo de forma ordinaria.

---

## 4.4 Niveles de agua de referencia

Nivel alto ordinario:

- boca: **Z +0,9 m**;
- Puente de los Gemelos: **Z +1,6 m**;
- límite norte de control: **Z +2,0 m**.

Superficie de inundación de diseño:

- boca: **Z +3,2 m**;
- puente: **Z +3,9 m**;
- límite norte: **Z +4,4 m**.

No se asigna una recurrencia estadística moderna.

Es una referencia física de diseño para:

- inundabilidad;
- edificios sensibles;
- puente;
- cotas de trabajo.

---

# 5. Desembocadura

La desembocadura principal queda en:

**X=0 / Y=0**.

Bordes de boca:

- margen occidental: **(-45, -20)**;
- margen oriental: **(+45, +20)**.

Abertura efectiva aproximada:

**100 m**.

Profundidad normal del thalweg:

**4,5 m**.

La boca:

- no forma un delta urbano;
- no contiene una isla permanente;
- integra el tránsito entre río y costa;
- deja a T01 aguas arriba;
- deja a T07 en la costa civil oriental;
- mantiene T08 más al este.

---

# 6. Costa

## 6.1 Morfología

El litoral urbano es:

- bajo;
- laborable;
- sin acantilado operativo;
- suavemente curvo;
- más protegido junto a la boca;
- progresivamente más abierto hacia el frente naval oriental.

La costa oriental asciende en dirección ENE.

---

## 6.2 Línea de costa al este de la boca

| Punto | PK costa | X | Y |
|---|---:|---:|---:|
| CE0 | 0 m | 45 | 20 |
| CE1 | 178 m | 220 | 50 |
| CE2 | 383 m | 420 | 95 |
| CE3 | 575 m | 610 | 120 |
| CE4 | 731 m | 760 | 165 |
| CE5 | 874 m | 900 | 190 |
| CE6 | 1.064 m | 1.090 | 185 |
| CE7 | 1.257 m | 1.280 | 220 |
| CE8 | 1.459 m | 1.480 | 250 |
| CE9 | 1.682 m | 1.700 | 285 |
| CE10 | 1.874 m | 1.890 | 315 |
| CE11 | 2.036 m | 2.050 | 340 |

Longitud de costa oriental controlada:

**~2.036 m**.

---

## 6.3 Costa occidental inmediata

Control mínimo:

- CW0: (-450, -90);
- CW1: (-280, -65);
- CW2: (-150, -40);
- CW3: (-45, -20).

Esta parte no debe convertirse en otro puerto urbano equivalente.

---

# 7. Batimetría costera

## 7.1 Frente civil

Tramo costero de referencia:

**PK 80–620 m**.

Profundidades naturales de diseño:

- cota -3 m a **70–110 m** mar adentro;
- cota -5 m a **150–220 m**.

Es una costa suficiente para:

- pesca;
- mercantes civiles compatibles;
- carga;
- reparación;

sin convertir T07 en una gran base naval.

---

## 7.2 Frente naval

Tramo:

**PK 880–1.820 m**.

Profundidades:

- cota -4 m a **60–90 m**;
- cota -6 m a **120–170 m**.

Por tanto T08 dispone de un frente naturalmente más apto para:

- atraque militar;
- botadura;
- mantenimiento;
- maniobra naval.

Punto 3 no fija todavía:

- muelles;
- espigones;
- rompeolas;
- dársenas;
- gradas.

Eso queda para Punto 7.

---

# 8. Relieve

## 8.1 Bandas de cota

### Z0 — borde activo

**+1,5 a +3,5 m**

Apto para:

- muelles;
- bordes de trabajo;
- actividad tolerante a inundación.

### Z1 — terraza baja de trabajo

**+3,5 a +6,0 m**

Apta para:

- patios;
- apoyo portuario;
- actividades de ribera.

### Z2 — terraza urbana principal

**+6 a +16 m**

Es la base preferente de:

- tejido residencial;
- comercio;
- administración;
- justicia;
- red urbana ordinaria.

### Z3 — terraza interior alta

**+16 a +30 m**

Domina el norte/nordeste interior.

### Z4 — borde alto

**+30 a +42 m**

Solo aparece en zonas exteriores.

No crea una ciudad de laderas extremas.

---

## 8.2 Puntos topográficos de control

| Punto | X | Y | Z |
|---|---:|---:|---:|
| E01 | 90 | 180 | 3,8 |
| E02 | 30 | 420 | 4,5 |
| E03 | -70 | 790 | 7,0 |
| E04 | 350 | 700 | 9,5 |
| E05 | 520 | 960 | 14,0 |
| E06 | 900 | 1.200 | 24,0 |
| E07 | 1.250 | 1.150 | 27,0 |
| E08 | 1.350 | 520 | 10,0 |
| E09 | 1.850 | 700 | 15,0 |
| E10 | -250 | 500 | 2,5 |
| E11 | -320 | 1.200 | 4,5 |

Estos puntos son **control de relieve**, no ubicaciones automáticas de sectores o edificios.

---

# 9. Pendientes

Se congelan las siguientes bandas:

- explanadas de muelle/trabajo: **0,5–2 %**;
- terraza urbana principal: **1,5–4 %**;
- trasera de T08 hacia el mar: **1,5–3 %**;
- ascenso interior N/NE: **3–6 %**;
- pendiente local no principal admisible: hasta **8 %**;
- ningún corredor esencial de carros debe quedar forzado por encima de **8 %**;
- accesos al Puente de los Gemelos: máximo **4,5 %**.

El drenaje superficial dominante:

- terraza urbana → sur/suroeste;
- terraza naval → sur/sudeste.

Esto permite saneamiento preindustrial por:

- pendiente;
- cuneta;
- canal;
- drenaje simple.

---

# 10. Inundabilidad

## 10.1 F1 — borde activo

Riesgo ordinario alto.

### Río

PK **0–700 m**:

- margen oriental: hasta **25 m** más allá del borde de cauce;
- margen occidental: hasta **80 m**;
- mientras la cota sea **≤ +3,0 m**.

### Costa civil

PK costa **0–650 m**:

- hasta **25 m** tierra adentro;
- cota **≤ +2,8 m**.

No admite edificios sensibles permanentes.

---

## 10.2 F2 — llanura de inundación excepcional

### Río

PK **0–900 m**:

- margen oriental: hasta **80 m** desde el borde;
- margen occidental: hasta **180 m**;
- cota inferior a **+4,8 m**.

### Costa civil

PK **0–850 m**:

- hasta **90 m** tierra adentro;
- cota inferior a **+4,5 m**.

### Costa naval

PK **880–1.820 m**:

- hasta **50 m** tierra adentro;
- cota inferior a **+4,2 m**.

No se sitúan en F2 las funciones cívicas/militares críticas.

---

## 10.3 F3 — terraza segura

Criterio:

- cota **≥ +6,0 m**;
- fuera de F2.

Deben ir en F3:

- T06 / S03 / S04 / S05;
- T12 / S11 / S12.

T05 también debe preferir esta terraza.

---

## 10.4 Sectores de agua y riesgo

### T01

El borde operativo puede ocupar F1/F2.

Los apoyos permanentes sensibles se retrasan hacia cotas superiores.

### T07

La primera línea portuaria puede inundarse.

Almacenes sensibles, documentación y funciones que no toleren agua deben retrasarse o elevarse.

### T08

Gradas y atraques pueden ocupar borde bajo.

Mando, archivo, almacenamiento crítico y funciones equivalentes se colocarán en terraza segura o trasera equivalente.

---

# 11. Puente de los Gemelos

## 11.1 Posición

Único puente permanente principal.

PK fluvial:

**820 m desde la boca**.

Centro:

**(-120, 801)**.

Estribos:

- oeste: **(-158, 810)**;
- este: **(-82, 792)**.

Eje:

**~103° desde norte**, aproximadamente O-E con ligera oblicuidad.

Queda:

- aguas arriba de T01;
- fuera de la zona portuaria inmediata;
- conectado de forma natural con la margen urbana oriental.

---

## 11.2 Geometría

Longitud estructural:

**78 m**.

Anchura útil:

**6,2 m**.

Anchura total:

**7,2 m**.

Cota de tablero:

- estribos: **+7,0 m**;
- corona: **+7,3 m**.

Intrados central:

**+6,1 m**.

---

## 11.3 Estructura

Solución cerrada:

- estribos de piedra;
- tres pilas de piedra;
- tajamares;
- superestructura de madera;
- tablero de madera con superficie sustituible;
- sin torres;
- sin fortificación por defecto.

Cuatro vanos:

- 14 m;
- 17 m;
- 17 m;
- 14 m.

Los dos centrales son los principales vanos navegables.

El nombre **Puente de los Gemelos** no obliga a inventar una etimología.

No se deduce que el nombre proceda de esos dos vanos.

---

## 11.4 Navegación

Altura libre bajo los vanos centrales con agua alta ordinaria:

**~4,5 m**.

Con la inundación de diseño:

**~2,2 m**.

En inundación de diseño:

**navegación cerrada**.

Las embarcaciones fluviales pequeñas compatibles pueden continuar aguas arriba cuando:

- calado;
- manga;
- altura;

lo permitan.

---

## 11.5 Accesos

Reserva geométrica:

- acceso oeste: **85 m**;
- acceso este: **65 m**;
- pendiente máxima: **4,5 %**.

El trazado exacto de las vías se resuelve en Punto 6.

---

# 12. Pasos menores

Resultado:

**NO son necesarios.**

Se fija:

- 1 puente permanente;
- 0 puentes menores permanentes;
- 0 ferris necesarios para que funcione la ciudad.

Motivo:

- la ciudad principal está en una sola margen;
- T01, T03, T07 y T08 no necesitan cruzar el río para relacionarse;
- el Puente de los Gemelos absorbe la conexión territorial transversal.

Solo se reabrirá esta decisión si:

- aparece una necesidad funcional nueva;
- o existe canon autoral nuevo.

---

# 13. Relación río–T01–T07–T08

## 13.1 T01

Ubicación:

**margen oriental del tramo inferior del río**.

Frente operativo:

**PK fluvial 200–580 m**.

Longitud:

**380 m**.

Cumple la banda del Punto 2:

**300–450 m**.

Distancias:

- extremo inferior a boca: **200 m**;
- extremo superior a puente: **240 m**.

T01 no invade la boca marítima.

---

## 13.2 T07

Ubicación:

**costa oriental inmediata a la desembocadura**.

Frente:

**PK costa 80–620 m**.

Longitud:

**540 m**.

Cumple la banda del Punto 2:

**450–650 m**.

Extremos aproximados:

- (124, 34);
- (654, 133).

---

## 13.3 Separación T07–T08

Entre ambos se mantiene:

**PK costa 620–880 m**.

Longitud:

**260 m**.

Función:

- separación física;
- seguridad;
- impedir una explanada portuaria civil-militar continua.

No se fija todavía a qué polígono terrestre T pertenece cada metro.

Eso corresponde al Punto 4.

---

## 13.4 T08

Ubicación:

**frente marítimo oriental más profundo y abierto**.

Frente:

**PK costa 880–1.820 m**.

Longitud:

**940 m**.

Cumple la banda del Punto 2:

**850–1.050 m**.

Extremos aproximados:

- (907, 190);
- (1.837, 307).

T08:

- no usa el río como frente principal;
- no comparte muelle continuo con T07;
- dispone de fondo suficiente para las **36 ha objetivo** sin comprimirlo en una franja absurda.

---

## 13.5 Transición T01–T07

Existe en la esquina oriental de la boca.

Debe permitir:

- pescado;
- carros;
- transferencia río-mar-tierra;
- futura colocación S07.

Punto 3 fija **dónde existe**.

Punto 4 fijará el polígono.

Punto 5 fijará S07.

---

# 14. Compatibilidad con Punto 2

La geografía mantiene:

- caja de control: **2,5 × 1,5 km**;
- envolvente terrestre objetivo: **250 ha**;
- huella funcional: **185 ha**;
- tejido principal: **110 ha**;
- T01: **5–8 ha**;
- T07: **18 ha objetivo**;
- T08: **36 ha objetivo**;
- T12: **15 ha objetivo**.

El agua sigue sin contabilizarse como suelo urbano.

---

# 15. Consecuencias para Punto 4

El encaje T01–T12 deberá respetar:

1. masa urbana principal al este del río;
2. T01 sobre PK 200–580 del río;
3. T07 sobre PK 80–620 de costa;
4. T08 sobre PK 880–1.820;
5. separación T07/T08 de 260 m;
6. T06 y T12 en F3;
7. T12 en la terraza N/NE;
8. ningún sector crítico obligado a pendientes >8 %;
9. Puente de los Gemelos en PK 820;
10. ninguna necesidad de segundo puente.

---

# 16. Elementos deliberadamente aplazados

No quedan abiertos dentro de Punto 3:

- curso del río;
- anchos;
- profundidades;
- boca;
- litoral;
- cotas;
- pendiente general;
- inundabilidad;
- puente;
- cruces menores;
- relación T01/T07/T08 con el agua.

Sí quedan para después:

### Punto 4

- polígonos T01–T12.

### Punto 5

- S01–S13.

### Punto 6

- calles y corredores;
- acceso viario exacto al puente.

### Punto 7

- muelles;
- dársenas;
- gradas;
- rompeolas si técnicamente se necesitan;
- geometría interna T07/T08.

---

## Certificación

**TRESKAL_METRIC_GEOGRAPHY_VALIDATED**

La geografía natural ya es suficientemente precisa para encajar los doce sectores sin alterar la escala cerrada en Punto 2.

Siguiente:

**Punto 4 — Encaje métrico T01–T12.**

---

## Regla final

**Desde este punto, el río, la costa, las cotas, la inundabilidad y el Puente de los Gemelos dejan de ser dibujos aproximados: son geometría canónica de control.**

`TRESKAL_METRIC_PLAN_POINT_3_GEOGRAPHY_CLOSED`
