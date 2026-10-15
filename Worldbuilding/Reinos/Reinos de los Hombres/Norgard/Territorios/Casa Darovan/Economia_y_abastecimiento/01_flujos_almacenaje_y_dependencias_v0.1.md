# D04 — Flujos, existencias y abastecimiento v0.1
**Estado:** planificación trazada NO RUNTIME; ningún recorrido es una nueva ruta navegable salvo referencia canónica expresa.

## Capas de cadena
- **Recurso físico** (mineral, metal refinado, combustible, madera, alimento, producto de pesca) distinto de **valor contable** y de **documento**.
- **Operación:** origen → manipulación/extracción → transformación → depósito → movimiento autorizado → destinatario/consumo; cada etapa necesita capacidad y recursos existentes en World State para llegar a gameplay.
- **Puntos de acopio** documentados solo cuando lo indica el canon. Los almacenes, depósitos de mineral/carbón, patios y puerto industrial de Treihord están acreditados, así como los almacenes de Veldora. No se añade un almacén imaginario a Taramin o Syvaris.
- **No se generan lotes gratuitos ni reabastecimiento automático**: las cadenas aquí son descripciones y enlaces de dependencia.

## Flujo M1: mineral precioso / Treihord
`mina(s) Valkram (sin localizar) → carros → punto(s) de carga fluvial (sin localizar) → barcaza de poco calado por Belara → puerto industrial Treihord → patios/depósitos → fundición/refinado/ensaye registrado → lingotes/trabajo especializado → custodia/comercio`.
**AUTHORED:** relación logística, puerto y procesos de Treihord; Crisol es instalación de Casa Darovan, no ceca. **UNKNOWN:** orden exacto de cada tratamiento, capacidad y recorrido de metales desde fundición al Crisol. **La Vena** existe para movimientos de máximo valor entre Crisol y Bóveda bajo custodia, no para transporte general.

## Flujo C1: carbón de Azurios
`Montes Azurios [región fuente AUTHORED] → tramo(s) de transporte UNKNOWN → depósitos importantes de carbón Treihord → uso industrial`.
**No trazar trayecto, lugar de extracción, intermediario, navío ni tiempos.** Dependencia cualitativa: sin combustible suficiente no puede presumirse la misma actividad de fundición. Las reservas son canónicas; el tamaño cuantitativo y días de cobertura no.

## Flujo W1: madera para minería
`Bosque de los Pilares [conjunto único] → aprovechamiento existente sin parcelas acreditadas → suministro a minas Valkram`.
La madera se usa para las minas según fuente; registrar su potencial relación con acondicionamiento minero no equivale a imponer técnica específica. **No** declarar como hecho una tala masiva, un aserradero, un daño ecológico ni una tasa de regeneración. Agujas, Linde, Taramin y Syvaris no son sustitutos industriales automáticos.

## Flujo F1: abastecimiento de alimentos
Treihord posee huertas exteriores y se abastece también de otras zonas: **AUTHORED**. Para alimentos no identificados se reserva un circuito abstracto `producción acreditada → almacenamiento disponible → distribución efectiva → hogares/talleres`, **PROPOSAL**. No atribuir cultivos, rebaños, superávits ni rutas a una zona D01 sin autor/suelos/agua.
Taramin norte/centro y Syvaris requieren evaluación de agua y suelo; verde costero de Syvaris no certifica irrigación. No modelar hambruna o carestía como historia sucedida por vulnerabilidad potencial.

## Flujo P1: litoral y puertos
- **Veldora:** interfaz mercantil/aduana exterior cuando cruce frontera fiscal; carga, almacenes, talleres y servicios acreditados. No implica control aduanero interior sobre otras Grandes Casas.
- **Taramin:** pesca marítima y fluvial, productos marinos, aceite de ballena como función canónica de perfil visual; manejo/conservación y destinos específicos UNKNOWN. No confundir ambos brazos del Thalen con un puerto fluvial navegable probado.
- **Syvaris:** pesca, comercio, productos marinos, puerto seguro y presencia naval; capacidad, autosuficiencia material exacta y rutas de cabotaje UNKNOWN.
El proceso genérico de pesca/embarque/desembarque y mantenimiento **se hereda** de Core acuático y Norgard Defaults E7, sin duplicar el simulador ni establecer cupos o especies.

## Dependencias y escenarios hipotéticos (NO eventos ocurridos)
| Condición hipotética | Efecto a evaluar cuando exista simulación | Dato necesario |
|---|---|---|
| carga de carbón no llega | presión sobre existencias y actividad industrial | stock, demanda y rutas reales |
| barcazas Belara no pueden operar | alternativa terrestre no presumida | calado/estado fluvial, capacidad de carros |
| disminuye madera apta en Pilares | sostenibilidad y suministro de minas a estudiar | inventario, permisos y tiempos |
| estación seca compromete actividad agrícola | revisar balance agua–demanda, no fijar sequía canónica | precipitación/suelo/almacenaje |
| condiciones marítimas restringen faena | operaciones y flota según contratos de navegación | meteo, caladero, barco y tripulación |

### D05 / D07 / D08 / D11
D05 tendrá que **demostrar** conectividad, tipos de ruta y nodos, no convertir flechas conceptuales en carreteras. D07 conserva la definición manual de ciudades y puertos. D08 calculará demandas reales a partir de entidades persistentes. D11 conectará físicamente inventarios, TXN/OBL/LED, navegación, persistencia y ensayos de fallo cuando los motores estén disponibles.
