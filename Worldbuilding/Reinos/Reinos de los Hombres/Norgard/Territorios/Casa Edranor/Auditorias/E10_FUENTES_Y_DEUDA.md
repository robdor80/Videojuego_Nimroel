# E10 — Auditoría: fuentes, autorizaciones y pendientes

## CANON_REPO leído y protegido
- `Norgard/Grandes Casas/grandes_casas.md`: Edranor, Rodas, orgullo y vino; EDD-05 y EDD-08 antes pendientes; cinco Casas, bienes institucionales, apellidos protegidos.
- `Norgard/Gobierno y leyes/organizacion_del_reino.md`: unidad de Ley, sucesión hereditaria de Casa y confirmación regia, títulos Lord/Lady, sin autonomía militar.
- `Norgard/Gobierno y leyes/protocolo_regio.md`: asiento de Corona, anfitrión a su derecha y Aposentos Regios.
- `Norgard/Sociedad/calendario_fechas_estaciones_norgard_v0.1.md`: 15375 de referencia, 12 meses/365 días, sin festividades automáticas.
- `Norgard/Sociedad/nombres_apellidos_transmision_norgard_v0.1.md`: apellidos protegidos, NAME/KIN y matrimonio.
- `Norgard/Sociedad/costumbres_funerarias.md` y `luto_y_duelo.md`: cremación, retorno de cenizas y luto de tres jornadas.
- E00–E09: Rodas Corona Aethros, bosque bajo derechos, sin carreteras físicas confirmadas, sin edificios o cifras instanciados, cuatro núcleos protegidos.

## Fuente autoral
`AUTOR_2026_11_12` fija Rodas al norte del recorte y Hallheim fuera; confirma control de Corona. `VISUAL_APROBADO` fija la aldea de pizarra, Casa Druídica junto a plaza, Dorth tintos, Lumina blancos/plaza alargada/mercado anual, Karsath rareza lacustre. El permiso de E10 **autoriza redactar la propuesta**, no prueba que estos nombres ya existieran.

## Novedades PROPUESTA_E10
Lady Elira, Maelis, Caelen y Vesra Edranor; Orlan Vereth, Ysna Calven, Tovan Brask, Lira Venn, Heran Malk, Saer Celdan y Bren Tovar. Conexiones, motivaciones, casos C01–C08, escenas S01–S08 y cronología relativa H01–H05. Estos nombres no son `CANON_REPO` preexistente; están sujetos a ratificación como canon personal y a los contratos NAME/KIN/E09.

## Deuda
- EDD-01: cierre septentrional; EDD-02: georreferenciación; EDD-03: agua; EDD-04: censos; EDD-07: carreteras y tránsito.
- **EDD-05:** propuesta de señoría y familia redactada; faltan nacimiento, filiación probada, herencia jurídica y ratificación autoral de nombres.
- **EDD-08:** modelo diplomático y memoria relativa propuestos; falta fecha, instrumento real o cronología histórica acreditada; NO se inventan.
- E10-U01: soberano Aethros y interlocutores efectivos NO designados aquí.
- E10-U02: qué ciudad o finca alberga cada archivo, lugar de los eventuales testimonios y autoridad exacta de acceso por instanciar.
- E10-U03: fechas/cosechas/mercados, relaciones laborales, moneda y contratos físicos pendientes.
- E10-U04: ningún NPC, inventario, diálogo, privilegio, licencia o misión implementados.

## Auditoría de no-regresión
Ningún cambio en `Norgard Defaults`, `Grandes Casas`, `Game`, `CoreRPG`, mapas ni E00–E09. Se diferencian hechos, propuestas y UNKNOWN. JSON solo alimenta comprobación estática. La prueba negativa debe rechazar soberanía Edranor en Rodas, jueces nuevos, ejército propio soberano, confiscaciones, apelaciones hereditarias inventadas, fechas falsas, personajes de Casa procedurales y NPC instanciados.

## Preparación E11
Asegurar IDs estables y contratos de lectura con aprobación editorial previa. **E11 no está iniciada.** No convertir este material a Content Pack ejecutable sin tests de World State, Godot 4.7.2 2D y CoreRPG C++20.
