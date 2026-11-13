# E12 — Matriz de coherencia transversal E00–E11

| ID | Fases y dependencia | Invariante auditable | Dato no demostrado |
|---|---|---|---|
| C01 | E00/E01/E02/E03/E04/E05/E06/E07/E08/E09/E10/E11 | Dorth, Lumina, Karsath, Rodas protegidos; Hallheim excluida; propiedad de Rodas siempre Corona | Polígono de jurisdicción |
| C02 | E00/E01/E02/E03 | Cierre norte, escala y datum no validados | Línea roja georreferenciada |
| C03 | E01/E02/E03/E04/E06 | Siete IDs de unidades físicas idénticos al referenciar drenaje, clima, viñedo y zonas de generación | Parcela real o biome |
| C04 | E02/E03/E04/E05 | Río Lurien y Lago Antela son fuentes regionales; su intersección Edranor es UNKNOWN | Lago/puerto/cauce local |
| C05 | E03/E04/E06 | Franja norte no se convierte automáticamente en viñedo; bosque y derechos separados | Hectáreas, riego, cupos |
| C06 | E04/E05/E07/E08 | Comercio y cadena vino/tonelería NO demuestran cuatro carreteras estudiadas; E05 0 aristas físicas | Viajes, precios, stocks |
| C07 | E06/E07/E11 | 8 modelos de asentamiento de laboratorio; 4 localidades fijas manuales; 5 IDs estables pack | Spawn real, ciudad extra |
| C08 | E07/E08/E09/E10/E11 | Rodas es aldea regia con mando berserker real, no jurisdicción de Casa | Fiscalidad/tribunales Edranor en Rodas |
| C09 | E07/E08 | Dorth tintos y sede; Lumina blancos/plaza alargada/mercado; Karsath producción escasa | Censos heredados de Darovan |
| C10 | E08/E09 | 15 servicios/16 oficios y 10 roles/11 permisos, todos sin instanciar | Edificios/funcionarios/capacidad |
| C11 | E09/Norgard Defaults | Ley única, acuñación real en Hallheim, sin aduanas interiores ni ejército soberano | Tributo/tarifa/ley de Casa inventados |
| C12 | E10/E11 | 11 personas propuestas / 8 conflictos / 8 escenas; cero NPC, NAME/KIN, quest y eventos | Ratificación editorial EDD-05/08 |
| C13 | E00–E10/E11 | 11 locks Git SHA de documentos fuente, con rutas y punteros; cinco recursos tipados del contrato 0.1.0 | Lógica territorial de CoreRPG |
| C14 | E11 y NIM-06 | C++/CTest laboratorio CoreRPG y posible puente genérico son niveles diferentes a Godot jugable | GDExtension, escena 2D, persistencia real |
| C15 | E00–E12/Valrik/Darovan | Datos locales de otras Casas NO son canon transferible | Rangos de población, caminos, barcos o minas Edranor |

## Método de validación
`Tools/EdranorE12/validate.py` lee los JSON E00–E10, la proyección/recursos/fixtures E11, inventaría archivos MD/JSON territoriales, comprueba referencias internas y ejecuta mutaciones negativas `in-memory`. La CI E12 repite **todos** los validadores E00–E11 y el C++/CTest E11 tanto en Ubuntu 24.04 como en Windows 2022. Ninguna prueba ejecuta Godot ni valida automáticamente la verdad editorial de cada frase. Las conclusiones de las matrices no deberán presentarse como runtime.