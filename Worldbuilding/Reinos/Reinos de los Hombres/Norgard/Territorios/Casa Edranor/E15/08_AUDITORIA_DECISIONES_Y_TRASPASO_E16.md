# E15 — Auditoría editorial, decisiones delegadas y traspaso

## Decisiones de diseño bajo autorización general
| Código | Decisión delegada | Alternativa descartada y razón |
|---|---|---|
| ED15-DEC-01 | Separar estilo de vino local de receta, marca y stock | «Un tipo de vino = miles de barricas» fabrica cifras |
| ED15-DEC-02 | Trazabilidad de madera y reparación por `containerId` | tratar barrica como consumible infinito |
| ED15-DEC-03 | Balance material + reserva por hogar/negocio | confundir pedido, pago, producto y necesidad |
| ED15-DEC-04 | Estacionalidad relativa por madurez y condiciones | imponer vendimia en un mes terrestre |
| ED15-DEC-05 | Veto legal antes de producir o cobrar | convertir jurisdicción en propiedad o impuesto |
| ED15-DEC-06 | Interfaces logísticas sin aristas | carretera ficticia por cercanía en mapa |
| ED15-DEC-07 | Labores compatibles con edad, cuidados, tiempo | generar trabajadores de aldeas por conveniencia |

Estas decisiones son **propuestas delegadas de diseño**; no ratifican un nuevo hecho histórico, un NPC, una genealogía ni una institución.

## Verificación de suficiencia
- [x] Vino tinto Dorth / blanco Lumina / pequeño y selecto Karsath sin inventar variedades ni litros.
- [x] Tonelería conectada con control forestal y piezas intermedias, prueba y reparación.
- [x] Agricultura, grano, molino/hornos hipotéticos, huerto y abastecimiento cotidiano.
- [x] Contratos y oficios compatibles con protección a menores del E08, sin censos.
- [x] Lotes, reservas, pérdidas, rutas condicionadas y separación de libros.
- [x] Rodas Corona, Hallheim fuera, Bosque Real no adjudicado, sin aduanas interiores.
- [x] 28 escenarios hipotéticos y oráculos para validación sintética.
- [ ] **No cumplido aún:** existencia de parcelas, producción cuantificada, rutas, instalaciones, proveedores o población ejecutable. Corresponden a fases posteriores con evidencias nuevas.

## Deuda editorial viva
- **EDD-01/02:** cierre norte y escala/perímetro E19: no georreferenciar unidades ni viñas.
- **EDD-03:** cauces, captaciones, agua de consumo/bodega E19/E28.
- **EDD-04:** población y capacidad hogar por hogar E26.
- **EDD-05:** sucesión/nombres legales E25; no nombrar bodegueros «de familia» como personajes canónicos.
- **EDD-06:** Rodas **ALDEA** resuelta para diseño, se mantiene.
- **EDD-07:** accesos, caminos, puentes y rutas E16/E19/E28.
- **EDD-08:** cronología/diplomacia regia E27, sin cesión de Rodas.

## Traspaso **a E16**, sin desarrollarla
**Objetivo de E16:** servicio y movilidad desde necesidades productivas, no desde una malla inventada. Se trasladan endpoints Dorth, Lumina, Karsath y contacto externo Rodas; categorías de carga uva/vino, barricas/madera, grano/harina, alimentos, combustible, herramientas, personas y mensajes; ventanas de urgencia y reserva **sin frecuencia, distancia ni tonelaje**. Para cada necesidad pedir `originId`, `destinationId`, `loadRef`, `owner`, `rights`, `routeSurvey`, `carrier`, `capacity`, `seasonWindow`, `receiverAck`. `routeSurvey=UNKNOWN` bloquea el despacho físico.

**Hacia E17:** escenarios de cambio causal hogar-negocio, con bucles para conservación, deuda y mantenimiento.
**Hacia E19/E20–E24:** pruebas espaciales y emplazamiento real; tipos visuales sin auto-instanciación.
**Hacia E26:** censo bottom-up y empleo por persona/hogar.
**Hacia E28:** contratos persistentes, mutación de inventarios verificada, Core y Godot reales.

## Acta técnica
La publicación de documentos/contrato y el éxito de las pruebas sintéticas solo certifican **coherencia documental**. No se declaran activos consumibles en el videojuego, ejecución en Godot, economía persistente o integración de CoreRPG a través de esta fase. La fusión exige GitHub CI verde en SHA exacto para Ubuntu/Windows, revisión de diff, no deriva de main y protección de autoridad.
