# E20-P01 — Dorth no son bodegas: son personas que viven en ellas y alrededor

## Principio de población
No existe censo ratificado de Dorth, ni parcelas ni número de hogares materializados. Por tanto, este documento establece **la estructura y las comprobaciones necesarias** para crear la población más adelante (E20-P05 y E26) y no inventa un solo habitante. El diseño parte de las capacidades sociales de Treskal y las hereda de Core/Norgard, no las copia como pseudomotores locales.

## Ecología de hogares y ocupaciones
**Hogar vinculado a bodega:** un adulto puede trabajar en elaboración, otro atender comercio, una persona mayor cuidar menores y otra aprender oficio; sus responsabilidades pueden cambiar por salud o estación. El mismo individuo no ocupa dos turnos incompatibles. El taller y la vivienda no son obligatoriamente misma propiedad.

**Hogar de transportista:** el conductor pasa jornadas fuera si existe viaje; familiares gestionan provisiones, cuidados, recados y seguridad sin volver invisible el trabajo doméstico. Un viaje no aparece de inmediato si la ruta no existe.

**Hogar comercial:** almacena bienes propios y de terceros con referencias separadas. Puede vender vino comprado, no ser productor. Los rumores de pérdida no equivalen a acusación confirmada.

**Hogar artesano:** tonelero, herrero de aros, carpintero o reparador usa herramientas y mantiene encargos; sus aprendizajes consumen tiempo y espacio. La reputación crece por hechos, no por etiqueta profesional.

**Hogares no vinícolas:** cocineras, posaderos, cuidadores, personal de limpieza, curtidores donde proceda, albañiles, sanadores, proveedores de agua/combustible y vecinos sin empleo remunerado son imprescindibles. La diversidad de vínculos impide una ciudad donde todo NPC existe para vender vino al jugador.

## Servicios exigidos y errores frecuentes
| Servicio | Necesidad verificable | Fallo si se simula mal |
|---|---|---|
| Agua y evacuación | Captación, acceso, higiene en F05, consumo y residuos, derecho | Pozo de decorado tratado como agua infinita |
| Alimentación | Compras, conservación, hogares, mercado y reservas | Familia alimentada sin alimentos ni desplazamiento |
| Salud y cuidados | Prestador o red efectiva, capacidad, distancia, descanso | Curación disponible 24/7 por una fachada |
| Hospedaje | Cama, permiso, registro, alimentación, capacidad | Cada visitante tiene habitación inexistente |
| Herrería y reparación | Herramientas, repuestos, turnos, combustible | Barrica/carro reparado sin trabajo |
| Guardia y mediación | Competencia, aviso, presencia, investigación, custodia | Guardia omnisciente o sentencia instantánea |
| Aprendizaje | Maestro, alumno, lugar, práctica, tiempo | Aprendiz adquiere oficio al recibir nombre |
| Residuos/incendio | Recogida, almacenaje, ruta y respuesta | Carga de vendimia sin suciedad, efluentes o riesgo |

## Calendario relativo y una jornada de prueba
No se fijan meses, horas universales ni festividades nuevas. Las actividades se condicionan por estación, disponibilidad, jornada, carga, luz y normas compartidas del Reino.

**Escena ordinaria hipotética:** una casa prepara alimento, una aprendiz va al taller, un receptor organiza el patio, un mercader consulta un libro y una cuidadora se ocupa de un dependiente. Cada desplazamiento usa lugares accesibles; si falta camino o edificio, la escena queda no ejecutable. El jugador ve procesos; no todos los NPC conversan sobre su encargo.

**Escena de afluencia:** llegan varios envíos; receptor y ayudantes priorizan según capacidad y reglas; comercio y guardia conocen retrasos solo mediante avisos. La posada no duplica camas por la llegada.

**Escena adversa:** una persona enferma reduce trabajo, la reparación se pospone, una familia atiende deudas y cambian expectativas. El sistema permite resolver por cooperación, posponer, subcontratar legítimamente o dejar fallo persistente.

## Percepción y vida sensorial
Bajo ventana de vecino: pasos, conversaciones parciales, utensilios, olor de cocina. Cerca de patio de cosecha: ruedas, voz de receptor, material descargado, limpieza y líquidos de trabajo. En zona de guarda: silencio relativo, acceso vigilado, humedad/temperatura a resolver. En torno a sede de Casa: visitantes con encargos y registros; nada de multitudes o estandartes sin motivo.

La percepción debe estar limitada a distancia, línea de visión, audición e información disponible. Un secreto comercial no se revela por estar cerca del jugador.

## Contrato social
PersonaId estable; hogarId, viviendaId, tenenciaId, puestoId y empleadorId son relaciones diferentes. Un NPC debe conservar identidad, nacimiento/edad cuando acreditados, conocimiento, relación, horario, disponibilidad, carácter y memoria tras guardado y recarga. El diseño no fija genealogías que E10 declara hipotéticas.
