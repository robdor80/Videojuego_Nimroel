# G02 — Caleran: topología sin geometría inventada

## Secuencia lógica autorizada por la fuente canónica
```text
Montes Azurios, vertiente OCCIDENTAL [ORIGEN CANON]
    ↓ conexión topográfica occidental→llanuras orientales = UNKNOWN
Grandes llanuras fértiles del ESTE [CANON]
    ↓
Arleon [CANON, orden relativo del río]
    ↓
Río Caleran, bifurcación principal [CANON]
    ├─ Brazo occidental del Caleran [NO es un río independiente]
    │     └─ Posterior bifurcación [CANON, canales sin nombre]
    └─ Brazo oriental del Caleran [NO es un río independiente]
          └─ Posterior bifurcación [CANON, canales sin nombre]
    ↓ conjunto del sistema, dibujo terminal UNKNOWN
Mar de Suthiros [CANON]
```

Este esquema expresa **orden y pertenencia**, no dirección de cada giro del cauce ni coordenadas. No añade túnel, cañón, collado, transvase, río de paso ni atravesamiento de la dorsal Azurios. La aparente tensión **nacimiento occidental → llanuras orientales** se mantiene abierta (`G02-I01`), sin corregir una frase canónica a conveniencia.

## Invariantes de identidad
- `rio_caleran` es el **único** río de este sistema; los dos brazos conservan la misma raíz. Las ramificaciones secundarias no adquieren ni nombre ni ID de río: el modelo JSON codifica **dos marcas de bifurcación**, no cauces autónomos.
- La fuente indica dos bifurcaciones ulteriores, pero **no** especifica si los cuatro cursos finales permanecen diferenciados hasta el mar, vuelven a unirse, forman islas o poseen un número concreto de desembocaduras. `confirmedOutletCount=null`.
- La proximidad del Bosque del Camino Real y del Bosque de las Riberas a sus brazos es cualitativa y **no** crea lagos, afluentes o canales de riego.
- La navegabilidad, las crecidas, los caudales y la propiedad de márgenes son preguntas abiertas; la importancia agrícola del Caleran **sí** está confirmada.

## Validación exigible para pasar de topología a cartografía
1. Resolver con el autor y el mapa completo el tránsito Azurios occidental→oriente, sin sustituir unilateralmente la fuente.
2. Dibujar después un perfil de cotas y pendientes que no permita flujos cuesta arriba.
3. Trazar bifurcaciones sin introducir brazos con nombre ni conexiones obligatorias no citadas.
4. Registrar límites de casas como **capa independiente**; la línea roja G00 no sirve de cuenca hidrológica.
5. Obtener revisión de desembocaduras y zonas inundables antes de ubicar un puente, un pueblo o un puerto en Godot.
