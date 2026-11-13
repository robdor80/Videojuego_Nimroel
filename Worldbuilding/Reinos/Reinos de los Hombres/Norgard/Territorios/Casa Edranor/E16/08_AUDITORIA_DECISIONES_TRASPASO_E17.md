# E16 — Auditoría de alcance, decisiones delegadas y traspasos

## Registro de decisiones (no canon nuevo)
| ID | Decisión adoptada por delegación | Alternativa descartada |
|---|---|---|
| ED16-DEC-01 | Separar grafo de necesidades Gd, preguntas Gq y físico Gp vacío | carreteras por unir ciudades |
| ED16-DEC-02 | Requerir pruebas completas antes de despachar y conservar inventario E15 | carrito despachado al recibir pedido |
| ED16-DEC-03 | Acuse real para conocimiento y entrega | NPC omniscientes y correspondencia instantánea |
| ED16-DEC-04 | Cadena escalonada de prestación E08 | todos los servicios en cada aldea |
| ED16-DEC-05 | Mantenimiento con titular, defecto y verificación de reapertura | reparación gratuita o sin activo real |
| ED16-DEC-06 | Trato con Rodas solo a través de autoridad competente | fiscalidad o mando de Edranor en enclave regio |
| ED16-DEC-07 | Atlas de necesidades sin emplazar infraestructura | mapas ficticios con kilómetros y postas |
| ED16-DEC-08 | Estados sintéticos triádicos con NO RUNTIME | confundir pruebas con juego funcional |

## Suficiencia editorial y límites
Diseñados: 5 anclas, 7 unidades, 4 preguntas E05, 8 clases de carga, 13 clases de servicio, 5 canales candidatos, 8 tipos de mantenimiento y 30 escenarios hipotéticos. Todos son inventario **de clases y obligaciones**. Materializados: **cero** caminos, instalaciones, rutas, vehículos, mensajes, obras y servicios. Este cierre es de diseño verificable, no de infraestructura física ni gameplay.

## Deudas abiertas
EDD-01 norte y EDD-02 georreferencia → E19; EDD-03 agua/cauces → E19/E28; EDD-04 censo → E26; EDD-05 linaje → E25; **EDD-06 Rodas aldea regia resuelta para diseño**; **EDD-07 accesos/servidumbres** sigue ABIERTA para E19/E28; EDD-08 cronología y diplomacia → E27. No se cierra una EDD por haber descrito condiciones.

## Traspaso a E17 (sin ejecutarla)
Simular conceptualmente cadenas **hogar → encargo → disponibilidad → transporte → recepción → consumo/servicio → mantenimiento → registro** con escenarios de escasez, demora, autoridad y recuperación, sin activar World State, rutas ni IA. E18 auditará madurez intermedia; E19 levantará geometría; E20–E24 detallarán asentamientos; E26 hará censo real; E28 integrará CoreRPG/Godot tras evidencia técnica.

## Condiciones de fusión
Python E16 y mutaciones negativas correctos; regresiones previas E00–E15 y consumidor Core E11 pinneado, Ubuntu/Windows en SHA exacto; diff sin tocar main, canon, motor o Content Packs; sin atribuir infraestructura real y sin cerrar EDD-07. Si la CI falla, mantener PR en Draft. **E17 no se inicia en esta PR.**
