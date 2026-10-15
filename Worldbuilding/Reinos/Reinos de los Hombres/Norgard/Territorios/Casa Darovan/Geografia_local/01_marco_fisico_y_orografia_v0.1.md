# DAROVAN D01 — Marco físico y orografía v0.1

**Estado:** documentación de diseño NO CANÓNICA. La autoridad se mantiene en las fuentes de Norgard y en las decisiones del autor.

## Alcance y método
D01 describe las unidades naturales del occidente de Norgard relacionadas con Casa Darovan: montaña, piedemonte, costa, península, islas, transiciones y restricciones geográficas. NO crea fronteras, topónimos, altitudes, distancias, coordenadas, puentes, pasos concretos, ríos menores, asentamientos, biomas parametrizados ni geometría jugable. La línea roja del recorte de D00 es área de estudio, nunca frontera aprobada.

**Jerarquía:** Nimroel Core → Norgard Defaults → Casa Darovan → Localidad → World State. Diferenciar:
- CANON / AUTHORED: hechos explícitos en documentos originales o decisión expresa del autor.
- INFERENCIA / DERIVED: lectura cualitativa explicable, sin fuerza normativa.
- PROPUESTA TÉCNICA: organización de capas, códigos, interfaces y pruebas; no runtime.
- UNKNOWN / PENDIENTE AUTOR: no decidir por proximidad visual.

## Anclas orográficas documentadas

### Montes Valkram
**CANON:** gran cordillera del occidente orientada principalmente de norte a sur; separa occidente de región central de Norgard; rica en oro y plata. En algunos tramos actúa de referencia política, pero **no** se iguala automáticamente toda la cresta con el límite de Darovan. El Belara nace en la vertiente occidental del sector septentrional de Valkram; el Lurien nace en la vertiente oriental y pertenece a la gran red central. Fuentes: Geografía/montanas.md §§1,8; Geografía/rios_y_lagos.md §§1,3; Geografía/regiones_naturales.md §§4,9.
**DERIVED:** existen transiciones esperables de crestas a laderas y pie de monte; sus límites locales, cotas y posibles pasos son UNKNOWN.

### Montañas Elyra
**CANON:** cadena occidental meridional, situada al sur de Valkram y prolongada hacia el sur por la península; minerales preciosos. Fuente: Geografía/montanas.md §2.
**UNKNOWN:** continuidad geométrica de crestas con Valkram, pasos, altitudes, minas individuales y límite de administración de sus laderas.

### Región occidental y norte frío
**CANON:** región occidental más accidentada que el centro; aproximadamente la mitad de **la región natural occidental**, no del territorio Darovan medido, es montañosa. A lo largo del norte de Norgard existe franja fría/polar supraterritorial con bosques boreales y una transición gradual al sur. Fuentes: Geografía/regiones_naturales.md §§2,5; Geografía/bosques.md §4; Clima/clima_general.md §§2,4.
**UNKNOWN:** límite de la franja sobre Darovan, nieve permanente, morfología de valles y proporciones de cada clase.

### Península de Taramin
**CANON:** al norte/centro terreno semiárido de transición con colinas ocres, piedra, matorral, breñas, pastos duros y barrancos/cauces estacionales. Hacia el sur aumenta progresivamente la humedad, enlazando con el Bosque de Taramin longitudinal: coníferas → mixto → subtropical húmedo. Nunca convertir la península en un desierto uniforme ni el bosque en tres bosques distintos. Fuentes: Geografía/geografia_general.md §8; Geografía/regiones_naturales.md §7; Geografía/bosques.md §1.5.
**UNKNOWN:** límites cuantitativos de franjas, posición de cabeceras y cursos menores, pendientes, clima local D03.

### Isla de Syvaris
**CANON:** isla de Norgard administrada por Casa Darovan; lomas secas, roquedos, matorral, bosques dispersos, calas y sectores resguardados más verdes. La ciudad de Syvaris está junto a una bahía principal. El perfil visual de Norgard precisa sur relativamente verde y húmedo frente a centro/norte más áridos. No es desierto ni selva uniforme. Fuentes: Geografía/geografia_general.md §7; Geografía/regiones_naturales.md §6; Geografía/mares_y_costas.md §11; Direccion artistica/Biblia visual/Culturas/Norgard/Datos operativos/norgard_regions_v0.1.json.
**UNKNOWN:** extensión de la bahía, ubicación exacta de calas, elevaciones, gradientes medidos.

### Arven, solo contexto físico
**CANON:** isla mediana frente al Golfo de Veldora; Bosque del Manto Verde de coníferas cubre aproximadamente el 90 %; aldeas principalmente en la costa interior orientada al golfo. Fuentes: Geografía/mares_y_costas.md §10; Geografía/bosques.md §1.2.
**UNKNOWN:** autoridad administrativa. **PROHIBIDO asignar Arven a Casa Darovan** sin ratificación explícita, aunque quede frente a Veldora.

## Litoral y entornos protegidos
- **Golfo de Veldora:** en costa occidental, abierto al Mar del Crepúsculo / Ishalien; asociado a puerto comercial Veldora. Desembocan el Lhera y el Veldora, cursos independientes salvo bifurcación Lhera desde Belara.
- **Golfo de Norgard:** masa de agua entre península Taramin, costa meridional de Norgard y península Elandor; la línea exterior Taramin–Elandor es convención marítima, no frontera Darovan. Recibe Belara, Thalen y Lurien.
- **Acantilados de la Agonía:** costa occidental junto al entorno del Bosque de las Agujas. Ni altura, ni longitud ni peligros precisos están documentados.
- **Syvaris:** bahía principal y calas menores todavía sin nombres individuales.
Fuentes: Geografía/mares_y_costas.md §§3–5,8–12.

## Ciudades protegidas por canon
1. **Treihord**, capital interior Darovan; minería Valkram, Belara **adyacente sin atravesar casco urbano**, puerto industrial con barcazas de poco calado. Cota urbana, terrazas, orillas y pasos son UNKNOWN. El Crisol no es ceca; carbón industrial procede de Azurios, no de Valkram. Fuente: Ciudades/Casa Darovan/Treihord.md.
2. **Veldora**, gran puerto del Golfo de Veldora. Perfil visual Norgard v0.2: montañas hacia interior, río detrás de la ciudad, bosque cercano e isla forestal frente a costa. **No se identifica automáticamente el río detrás de Veldora con un curso concreto** sin comprobación adicional.
3. **Taramin**, ciudad pesquera en la península, **entre dos brazos finales del mismo río Thalen**, que desemboca en Golfo de Norgard.
4. **Syvaris**, ciudad insular manual en bahía principal.
**Karsath excluida**: ciudad Edranor / región central, sin inferencias por proximidad cartográfica.
Fuentes: Grandes Casas/grandes_casas.md §§6–7; Geografía/rios_y_lagos.md §§3–6; norgard_settlements_v0.2.json.

## Capas separadas y precedencia
- Física: relieve, vertientes, bosques, litoral, transiciones, barreras.
- Hidrográfica: solo anclas y relaciones canónicas D01; afluentes, cuencas, permanencia, manantiales e inundabilidad quedan para D02.
- Administrativa: cuatro ciudades y Syvaris pertenecen a Darovan; no asumir que cada masa natural o península completa es una demarcación confirmada.
- Cartográfica: sin malla de elevación, georreferenciación ni límites aprobados; D01 no declara un mapa de producción.

**Nimroel Core:** contrato universal activo Worldbuilding/Sistemas/Nimroel Core/Datos operativos/nimroel_physical_geography_drainage_contract_v0.1.json. Orden: anclas authored → macrorelieve → microrelieve → pendientes → divisorias → cuencas → red de cauces → capa humana. Tipos (ladera, vaguada, valle, collado, terraza, piedemonte, litoral) son **posibilidades genéricas**, no accidentes locales ya descubiertos.

## Pendientes
DAR-P01 adscripción Arven; DAR-P04 fronteras/cotas/distancias/nombres menores; contacto Elyra/Valkram y pasos; cartografía métrica, trazado de costa y microrelieve; identidad exacta del río tras Veldora en el perfil visual; detalle de drenaje D02 y variaciones climáticas D03. Ningún pendiente se resuelve por generación.
