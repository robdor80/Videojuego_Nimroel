# E09 — Auditoría de precedencia, fuentes y deuda de decisiones

## Fuentes de autoridad
- **CANON_REPO**: `Norgard/Gobierno y leyes/organizacion_del_reino.md` (Corona/Casa, unidad legal, sucesión); `sistema_fiscal_y_aduanero_v0.1.md` (contribuciones, servicios y aduana exterior); `moneda_y_acunacion.md` (Clavo, moneda y ceca); `sistema_militar_norgard_v0.1.md` (cuatro capas, movilización); `protocolo_regio.md` (asiento y aposentos); `Norgard Defaults/08_Sistema_penal/SISTEMA_PENAL_Y_JUSTICIA_DEL_REY_NORGARD_v0.1.md` (ley común y procedimiento).
- **CANON_REPO heredado E00–E08**: E00 identidad/aspiración a Rodas; E04 comercio, fiscalidad y madera; E05 sin carreteras físicas; E06 sin núcleos generados; E07 monografías y cuatro anclas; E08 roles, hogares y servicios NO instanciados.
- **AUTOR_2026_11_12**: Rodas incluida en recorte Edranor pero bajo soberanía y fiscalidad **Corona Aethros**; Hallheim fuera. **VISUAL_APROBADO**: tipos de edificios, plaza anual y Casa Druídica no religiosa; no confundir visual con operación.

## Campos clasificados PROPUESTA
Nombres de campos del contrato, tipos de acto, circuito administrativo, controles cruzados, evento idempotente, simulación de disputas, órganos como **roles funcionales sin plazas creadas** y las pruebas sintéticas. La clasificación PROPUESTA no habilita una licencia ni un cuerpo.

## UNKNOWN abiertos y bloqueos
`EDD-01` cierre norte de perímetro; `EDD-02` escala/parcelario; `EDD-03` agua; `EDD-04` población, funcionarios, guardias, reservas, capacidad de servicio; `EDD-05` Lord/Lady, herederos y administración personal; `EDD-07` rutas; `EDD-08` cronología y pretensiones históricas sobre Rodas. `EDD-06` resuelto solo para nomenclatura editorial de Rodas como ALDEA. Además `E09-U01` autoridad capital territorial titular no individualizada; `E09-U02` cuotas/remesas, tarifas, periodicidades desconocidas; `E09-U03` licencias forestales, límites de corte y titularidad concreta no materializados; `E09-U04` plantilla, sedes, jurisdicción microscópica y horarios aún sin crear.

## Prohibiciones verificables
Sin tributos o guardia Edranor en Rodas; sin mando berserker ni institución religiosa; sin aduanas entre Casas, moneda/ceca propia, guerra soberana, fiscal inventada, tribunales o penas locales, personal inventado, menor armado, carreteras y agua ficticias ni escenas de gameplay declaradas. No modificar capas superiores ni manifiestos E00–E08.

## Alcance técnico y deuda E11
El JSON no es Content Pack en funcionamiento. `validate.py` únicamente prueba estructura, coherencia E08/E07, casos de laboratorio y mutaciones adversariales en Python. No hay compilación de Godot/CoreRPG, economía persistida, lectura de inventarios, combate o guardado/carga. La integración real exige soporte transaccional, autorización de World State, validación de que las instituciones existen, contexto temporal del juego y pruebas de runtime en E11.
