# D.P26/03 — Deuda real, puertas de implementación y traspaso a desarrollo

La profundización literaria no es una deuda por falta de imaginación: es una capa de autoría acabada. El futuro trabajo se divide por condiciones verificables; no debe abrirse otra ronda de matrices genéricas que reproduzca D.P14–D.P25.

## A. Geografía, terreno y emplazamiento

Faltan polígonos urbanos y de asentamientos, geometría de costa/islas, relieve construido, nacimientos y desembocaduras precisas, puentes, vados, muelles y caminos con capacidad y distancia. Las altitudes de referencia D.P13 no sustituyen un modelo digital de terreno. Cualquier `RUR-S01…S09` sigue siendo **comunidad candidata**, nunca una aldea existente por el hecho de tener nombre. Prioridad: terrenos verificables → agua y acceso → tenencia/derechos → D06 puertas → permiso de materialización.

## B. Economía y servicios

Cadenas de carbón, mineral, madera, pesca, alimentos y documentos requieren proveedores, inventarios finitos, almacenamiento, propiedad, permisos, tiempos y fallos posibles. La Casa y la Corona no comparten atribuciones por conveniencia; no se crean tasas interiores ni una nueva ceca. Prioridad: datos CoreRPG de bienes, derechos y lugar físico → transacciones → contingencias → simulación económica.

## C. Personas, privacidad y narrativa

Convertir perfiles de autoría en NPC requiere IDs estables, edad/atributos autorizados, residencia, oficio existente, agenda realizable, necesidades, contactos posibles, conocimiento privado y capacidades. Las relaciones asimétricas exigen evidencia para cada sentido, memoria individual y procedencia. Los conflictos requieren precondiciones cumplidas por hechos de WorldState y varios desenlaces posibles. Narración multirrol: protagonista no omnisciente, mensajes privados no públicos, actos ilegales con rechazos/autoridades reales, imposibilidad de viajes sin caminos o transporte validado.

## D. Mundo y ejecución

**CoreRPG es la única autoridad sobre el estado**; Godot 2D es la capa de presentación. D11 y los JSON D.P13–D.P25 no equivalen a poblaciones, mapas, actores, eventos, agendas, inventarios o persistencia ejecutados. Integrar requiere validación Windows x64 y Android ARM64, regresiones de guardado/carga y pruebas físicas en MSI y Galaxy Tab S9+. Una CI documental verde no certifica la jugabilidad.

## E. Autoría reservada, conscientemente no inventada en D.P26

Quedan sin fijar el/la titular actual de Darovan, linajes y sucesión formal, jueces/comandantes individuales, fechas históricas públicas, derechos parcelarios, ubicaciones oficiales, conexiones marítimas nuevas, roles efectivos y reuniones entre personas. Ni las ocho decisiones de D.P25 ni la delegación creativa de D.P26 son un poder para crear estos hechos retroactivamente. **No impiden** cerrar el diseño editorial; sí impiden decir que ya están en el mundo.

## F. Traspaso recomendado

1. **Integración editorial controlada:** PR #46 → #47 → #48 → D.P26, autorización separada y CI postmerge.
2. **Inventario de unidades concretas para un vertical slice:** elegir **un** asentamiento o zona urbana autorizada con fuente de agua, derechos y acceso; demostrar end-to-end actividad diaria, stock, necesidad y persistencia sin fingir que todo Darovan funciona.
3. **Primera cohorte de NPC:** activar sólo personas autorizadas y emplazadas; relaciones que nazcan de contactos verificables y conocimiento.
4. **Eventos y conflictos:** incorporar uno de los diez arcos como caso condicional sin inicio forzoso; estados/guardado gestionados por CoreRPG.
5. **Escalado:** extender a cuatro ciudades y nueve candidatos rurales sólo después de auditoría de rendimiento, persistencia, geografía y control de información.

El trabajo próximo es **materializar selectivamente, no rehacer Lore**.
