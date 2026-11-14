# E19-R1.05 — Perfiles físicos y transiciones causales para mundo 2D
**No representa un itinerario probado ni un perfil altimétrico de metros medidos.** Se inspira en la relación relieve → drenaje → uso humano del atlas Valrik, adaptada a Edranor.

## 1. Perfiles sin distancia: cuatro cortes cualitativos
### Corte A — Oeste (Valkram) al centro (Karsath y campiña)
`DIVISORIA VALKRAM → LADERA EDRANOR → CABECERAS → BARRANCOS → PIEDEMONTE → RELLANOS KARSATH → LOMAS INTERIORES`

- **Cresta y cabecera:** alto contraste de pendientes, exposición al viento, nieve eventual según estación y altitud; no corresponde fijar cota exacta.
- **Valles de salida:** secciones más concentradas, carga de sedimento y posibilidad de escorrentía rápida; no adjudicar Lurien a todos.
- **Piedemonte:** redistribución de gravas/finos, nacimientos de manantiales condicionales en contactos litológicos, cambios de acceso.
- **Rellanos:** paisaje discontinuo de agricultura/viña selectiva, relieve más amable y pequeñas divisorias.
- **Antela**: ancla situada al sur de Karsath a escala regional; no convertir el corte en una ruta directa al lago.

**Prueba adversarial:** un cauce menor que abandona el pie de monte y reaparece cuesta arriba en una cresta distinta sin continuidad hidráulica invalida la generación.

### Corte B — Centro hacia Lumina/Bosque Alto
`CAMPIÑA ONDULADA → PIE DE ESCALÓN → GRADAS DE LUMINA → CORONACIÓN DE MESETA → UMBRÍAS/CLAROS DEL BOSQUE ALTO`

- La subida no debe ser una pared vertical uniforme.
- La meseta no es horizontal ni idéntica en todas las direcciones.
- La coronación puede contener lomas bajas y drenajes de poca pendiente; **no** se crea río grande frente a la plaza de Lumina.
- Las umbrías pueden conservar humedad relativa y vegetación diferente; no se asigna niebla permanente por título.
- El paisaje de blancos se limita a superficies compatibles con clima, insolación, suelo y derecho; no invade automáticamente el bosque protegido.

**Prueba adversarial:** insertar un viñedo sobre una ladera boscosa abrupta y sin autorización debe fallar aunque esté cerca del mercado anual.

### Corte C — Desde Dorth hacia la divisoria Azurios
`SECTOR HABITADO DORTH → BORDE BOSQUE AZURIOS → PIEDEMONTE → RESALTES → LADERA FORESTAL ESCALONADA → ESPOLONES → DIVISORIA AZURIOS`

- La parte occidental de la cordillera es Edranor; tras la divisoria, **Galdren**.
- Dorth puede tener patio de recepción de uva y bodegas sin estar atravesada por río navegable.
- No convertir el Bosque Real de Hallheim en recurso ordinario de Dorth.
- Las quebradas y fuentes de la ladera solo existen si el terreno y la recarga las respaldan.

**Prueba adversarial:** un desvío de montaña que cruza la divisoria y cobra «aduana interior de Dorth» es incompatible con la jurisdicción y el contrato de caminos.

### Corte D — Centro habitado hacia Rodas y el norte abierto
`CAMPIÑA CENTRAL → BOSQUE/CLAROS DE TRANSICIÓN → FRÍO CRECIENTE → ENTORNO FÍSICO DE RODAS → HORIZONTE NORTE DESCONOCIDO`

- El frío puede intensificarse sin aumento monótono de altura.
- El hielo, el barro y la nieve afectan tránsito solo por condiciones climáticas/edáficas concretas.
- Rodas es **ALDEA** de Corona Aethros; una diferencia de arquitectura o vegetación no cambia competencias.
- Ni océano septentrional, ni tundra propia, ni borde artificial entre las líneas rojas.
- U7 no se rellena con una zona jugable por completar el dibujo.

**Prueba adversarial:** generar un camino/poblado en U7, o un mercado Edranor imponiendo impuestos en Rodas, debe fallar.

## 2. Matriz relieve → agua → suelo → vegetación → usos
| Relieve | Tendencia hidrológica (condicional) | Suelo/vegetación | Uso humano a evaluar | Freno |
|---|---|---|---|---|
| cresta montana | escorrentía superficial rápida | suelo somero, expuesto | observación, paso si collado real | nieve, pendiente, seguridad |
| media ladera convexa | pérdida de agua/erosión | suelos variables, vegetación resistente | viña solo si aptitud y tenencia | degradación de suelo |
| concavidad forestal | acumulación/recarga | humedad, frondosas según clima | protección, manantial si acuífero | riesgo de saturación/tala |
| pie de monte | aporte sedimentario/agua | depósitos heterogéneos | campos, caminos de valle | abanicos activos/avenidas |
| rellano ondulado | menor energía hidráulica relativa | perfiles de suelo variados | vivienda o viñedo si derecho/agua | helada, drenaje insuficiente |
| meseta arbolada | cabeceras locales según divisoria | bosque mixto por altura | manejo forestal regulado | fragmentación y erosión |
| fondo húmedo | concentración/retención | pradera húmeda eventual | pasto con carga limitada | inundación, sanidad |
| claro septentrional | deshielo/escorrentía variables | vegetación baja/forestal mixta | cultivo rural solo en ventana viable | frío, acceso, abastecimiento |

**Nunca** invertir la causalidad: no escoger «regato junto a molino» y dibujar después una ladera para justificarlo, ni crear lagar, propietario o molino por nombre del lugar.

## 3. Algoritmo de worldbuilding compatible con Valrik
1. Congelar anclas mayores de Norgard y decisiones del autor sobre vertientes.
2. Elegir la **familia geomorfológica** de cada sector, que debe ser coherente con sistemas adyacentes.
3. Formar continuidad de pendientes y depresiones razonables; sin saltos arbitrarios entre módulos 2D.
4. R2: derivar divisorias, área aportante, receptores y densidad de red menor.
5. R3: derivar microclima a partir de altura relativa, exposición, suelo, cobertura y clima regional.
6. R3/R5: derivar aptitud de uso y bosques preservados, sin convertir probabilidad en permiso.
7. R4: proponer corredores por topografía, cruzar con hidrología y verificar jurisdicción/servidumbres.
8. R5: situar hogares, parcelas y oficios solo tras viabilidad y capacidad real.
9. E19-TEC/E28: materializar entidades con IDs persistentes; World State guarda estado variable (lluvia, paso abierto, cauce activo), no reescribe accidente o propiedad.
10. IA narrativa lee entidad existente + estado + contexto de conocimiento; nunca crea un río, una mina o un puente porque el guion lo necesite.

## 4. Contratos de persistencia futura
Todo accidente materializado exige como mínimo:
`featureId, physicalType, parentRegion, sourceClass, evidenceRefs, terrainVersion, relations, jurisdiction, coordinatesOrGeometryWhenAvailable, editorialStatus`.

Los cursos necesitan `basinId, sourceCause, permanence, upstreamDownstream, receiver`; las rutas `accessRight, crossingEvidence, slopeClass, seasonalCondition`. No introducir ahora esos campos con valores inventados: **null/UNKNOWN** es la respuesta correcta. No cargar ningún elemento de R1 al World State.

## 5. Secuencias jugables futuras, sin hechos consumados
**Viñedo en loma:** terreno → insolación/drenaje → dueño/licencia → cepa y manejo → vendimia → bodega → barrica autorizada → transportista. **Barrica de Bosque Alto:** cubierta → plan forestal → corte legal → secado y tonelería → inspección → expedición. **Encuentro en montaña:** cabecera/valle → meteorología → estado del paso → derecho de tránsito → actor con motivos → escena, no al revés.

Las escenas no implican que ya se hayan creado viñas, guardias, puentes, mercados, transportistas o propiedades. Cada una es una especificación de causalidad para E20–E28.

## 6. Lista de control de arte 2D
- Paisajes coherentes en escala visual y orientación: rocas, estratos, masa vegetal, pendientes, sombras, no paralelismo artificial de laderas.
- Los cambios de bioma se explican por altura/exposición/latitud/suelo, no por fronteras políticas.
- Bosque Alto, bosque de Azurios, viñas centrales y piedemonte occidental mantienen identidades reconocibles.
- El mapa del mundo no sustituye la topografía del área jugable ni obliga a posiciones exactas prematuras.
- Si el atlas y la capa técnica discrepan, se revisa la representación; **no** se reescribe silenciosamente el canon de montañas, río o jurisdicción.

**Limitación cuantitativa:** las bandas numéricas E13 son ilustrativas, no mediciones. R1 no entrega pendientes en %, tiempos de viaje, DEM ni distancias.
