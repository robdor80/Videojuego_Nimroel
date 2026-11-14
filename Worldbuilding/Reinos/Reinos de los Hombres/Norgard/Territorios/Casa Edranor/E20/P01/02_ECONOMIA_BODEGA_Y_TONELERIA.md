# E20-P01 — El tinto como economía humana y verificable

Este documento desarrolla la identidad productiva específica de Dorth, tomando E04 y E15 como requisitos de diseño. No crea existencias, productores efectivos, variedades, cosechas, rendimientos ni precios. **No crea un motor económico nuevo:** declara objetos y transiciones que el Core/Defaults y World State deberán resolver.

## Actores y recursos separados
- **Productor/arrendatario/propietario de parcela:** la identidad y el derecho a cultivarla pueden no coincidir; el título y permiso se comprueban.
- **Conductor/carretillero:** posee una asignación de transporte y contrato de entrega, no necesariamente la uva.
- **Receptor y escribiente:** verifican carga, origen, estado y recibo; no son dueños de todo el lote por firmar.
- **Maestro de elaboración y ayudantes:** operan fases con mano de obra, agua, utensilios y disponibilidad.
- **Custodio de bodega:** controla entrada/salida y condiciones; la propiedad del contenido podría ser ajena.
- **Tonelero y proveedor de tablas:** distinguen madera con derechos válidos, seco/curado, aros, reparación, devolución y reclamación.
- **Mercader y transportista:** contratan expedición sin inventar carretera, paso o tarifa fiscal.
- **Hogar:** trabajador también es persona, depende de descanso, alimentación, salud, cuidado y relaciones, no motor inagotable.

## Recorrido operativo objeto a objeto
| Paso | Entrada material / derecho | Acto y cambio esperado | Prueba negativa obligatoria |
|---|---|---|---|
| E01 Cultivo | Parcela elegible, tenencia y estado ambiental | Labor con recursos/hora y permiso | Viñedo sin parcela/agua autorizada: NO MATERIALIZAR |
| E02 Vendimia | Uva real y personas disponibles | Cosecha vinculada a lote origen con cantidad | Mismo racimo repartido a dos destinos |
| E03 Transporte | Lote, carro, transporte y ruta Gp real | Tránsito/entrega con coste de tiempo comprobable | Gd «necesitamos llegar» no autoriza carretera |
| E04 Recepción | Lote de origen, pesaje, evidencia, responsable | Aceptado / rechazado / en cuarentena, recibo único | Registrar entrada doble ante reintento |
| E05 Elaboración | Uva aceptada, recipientes, agua y equipo | Transformación condicionada; subproductos/mermas contabilizados | Transformación automática sin proceso |
| E06 Fermentación/cuidado | Mosto/mezcla, ambiente y vigilancia | Estado de proceso y riesgo de deterioro | Añejamiento instantáneo y sin consumo de tiempo |
| E07 Barrica | Recipiente con identificación y legitimidad de madera | Asignación reversible de contenido; custodia | Barrica decorativa crea stock por sí sola |
| E08 Guarda | Capacidad real y responsable | Inventario, revisiones, merma, reserva | Reserva mayor que disponible y sin testigo |
| E09 Venta | Derecho de enajenación, precio/regla autorizada | Transferencia de propiedad y obligación | Venta doble por dos interfaces |
| E10 Expedición | Lote vendido, transporte y camino accesible | Salida, recibo, consecuencia y llegada | Entrega teletransportada a Lumina/Hallheim |

## Identidades mínimas del futuro World State (propuestas de contrato)
- parcelId, titleRecordId, licenceId, cropBatchId, harvestEventId, transportJobId, receivingActId y provenanceChainId;
- pressingWorkOrderId, processingBatchId, vesselId, locationId, ownerActorId, keeperActorId y stockMovementId;
- damageCaseId, repairWorkOrderId, disputeCaseId, receiptId y idempotencyKey;
- cada referencia válida apunta a **instancias existentes**; un rol de diseño DOR-Fxx o una etiqueta de uva NO reemplaza un ActorId.

### Conservación y contabilidad
No se impone un rendimiento arbitrario de vino por uva. Cuando exista receta validada, las cantidades entrantes deben reconciliarse con producto, subproductos, desperdicio y mermas, respetando unidades y conversiones autorizadas. La merma no se inventa para cuadrar una contabilidad y el vino «en crianza» no puede venderse como disponibilidad instantánea. Una transferencia tiene origen y destino; no hace aparecer una segunda barrica.

## Escenarios de presión con consecuencias
**Vendimia intensa:** más carros y labores solo si la cosecha existe; capacidad F04 y trabajadores limitan recepción. Cuando se desborda, se genera cola, retraso, almacenaje provisional legal o rechazo. Un hecho conocido por el receptor NO pasa automáticamente a todos los comerciantes.

**Barrica que rezuma:** se detecta una pérdida *solo si hay recipiente y contenido real*. El custodio conserva evidencia; el tonelero comprueba procedencia y reparación; el comprador puede recibir comunicación, reclamar o esperar. El juego debe poder distinguir desgaste, transporte, fallo de fabricación y negligencia SIN declarar culpable antes de la investigación.

**Mal año de uva:** baja la materia disponible; trabajadores ocasionales pueden perder jornadas y hogares enfrentan tensión en sus suministros. Los negocios que conservan reservas y los que no responden de forma diferente. No se fabrica una cosecha de compensación por necesidad de la misión.

**Cierre por incendio:** el fuego afecta a espacios/stock realmente alcanzables; la guardia, servicios y vecinos responden según conocimiento y disponibilidad. La reparación consume recursos y tiempo. El mundo no repone automáticamente inventarios.

## Forestal y tonelería
La madera que usa un tonelero no es permiso de aprovechamiento del Bosque Alto o del Azurios. Requiere procedencia, secado, propietario, derechos, transporte y tratamiento compatible con el vino. Un taller puede comprar madera de otra región si existe cadena de abastecimiento legítima; no se presume monopolio forestal. Evitar que el tinte púrpura de un estandarte indique calidad del vino.
