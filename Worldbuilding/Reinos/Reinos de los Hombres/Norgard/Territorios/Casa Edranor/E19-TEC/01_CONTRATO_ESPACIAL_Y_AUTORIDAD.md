# E19-TEC.01 — Contrato de sector espacial

## Autoridad
R0 (correcciones expresas del 14/11/2026) prevalece sobre las inferencias anteriores: oeste divisor de Valkram (oeste Darovan / este Edranor), este divisor de Azurios (oeste Edranor / este Galdren), sur administrativo Aethros salvo tramo del Lurien, **sin unión de líneas en el norte**. Las marcas rojas del boceto son aproximadas, **NO límites jurídicos digitalizables por sí solos**. Rodas: ALDEA regia de Corona Aethros; Hallheim exterior. Bosque Alto requiere permiso y Bosque Real es regio. Antela al sur no funda puerto urbano en Karsath; Caleran no pasa por Dorth acreditadamente.

## Representación
Entrada JSON de sector, NO inventario canónico global ni GeoJSON lon/lat. V1 admite solo **LOCAL_METRIC en metros**, con referencia a fuente y error documentado y transformación afín reversible obligatoria (escala positiva, rotación, origen de fuente y origen local). Una transformación declarada no demuestra por sí sola la exactitud: su correspondencia con la fuente debe auditarse externamente. Jamás hacer pasar píxeles por metros. Cada sector tiene identificador inmutable y uno o varios contextIds MF-01–MF-07 de procedencia; MF-08/U7 se rechaza mientras siga NO EVALUABLE. El alcance es finito de producción sin fingir un perímetro político del norte. Registro de autorización en cabecera (AUTHOR_APPROVED_SECTOR; aprobado por autor/editor; fuente y decisión trazables), transformaciones documentadas cuando procedan y características con ID estable.

Geometrías: Point = [x,y], LineString = [[x,y], ...], Polygon = anillo cerrado [[x,y], ...]. Uniones, cruces, colisiones y enclaves se justifican por fuentes; no se generarán aleatoriamente.

Tipos:
- boundary_divide: línea abierta con orientación, titularidad de cada ladera y ninguna clausura del norte.
- river: línea de red con receptor existente y trazabilidad hidrológica; una hipótesis R2 no basta.
- waterbody: receptor materializado, no se inventa emplazamiento.
- route_node / road: grafo físico Gp; los CT/Gq de R4 jamás son caminos.
- settlement: núcleo existente, jurisdicción y clase; estudios OS de R5 nunca se convierten solos en aldeas.
- forest: área y régimen; aprovechamiento Alto sólo con permiso, Bosque Real queda bajo Corona.
- parcel: tenencia y uso material acreditados; no significa edificio ni censo automático.

Todo elemento de producción requiere evidencia particular: sourceId, approvalId y status APPROVED_B3. Para caminos además extremos, inspección del terreno, transitabilidad, capacidad, conservación, permiso legal y registro de agua cruzada. El exportador falla de modo cerrado en caso de datos parciales, duplicados, topología inválida, fuentes genéricas o semántica prohibida.

Las únicas coordenadas ficticias se construyen **en memoria de los tests** con modo SYNTHETIC_TEST; nunca se guardan como Edranor ni se exportan. La salida JSON ordenada es determinista, contiene procedencia y geometría, pero **no** modifica CoreRPG/ContentPacks ni activa NPC, movimientos o pathfinding hasta integrarse y acreditarse el runtime.

## Responsabilidad compartida
Godot representa datos de sector autorizados; CoreRPG decide estado y simulación, incluida propiedad, licencias y transitabilidad actual. La IA sólo narra el resultado. El guard de geometría se ocupa de la forma, **no sustituye la autorización legal o editorial**.
