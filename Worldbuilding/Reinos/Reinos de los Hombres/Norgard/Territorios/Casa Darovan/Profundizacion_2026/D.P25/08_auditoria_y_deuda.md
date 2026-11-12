# D.P25/08 — Auditoría de fuentes, bloqueos y traspaso a D.P26

## Inventario de autoridad
- **Primaria:** `Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Ciudades/Casa Darovan/Treihord.md`; las ciudades reales y el reino prevalecen sobre cualquier escena hipotética.
- **Territorial D00–D12/D.P13:** D01 relieve; D02 red hidrográfica; D03 ecosistemas; D04 economía; D05 transporte; D06 reglas de asentamiento; D07 cuatro ciudades; D08 hogares/servicios; D09 gobierno, justicia y seguridad; D10 cultura; D11 y D12 contratos y auditoría; D.P13 relieve físico.
- **Editorial fundido en main:** D.P20 Veldora, D.P21 Taramin, D.P22 Syvaris, cada uno con diez biografías base.
- **Editorial aún no fusionado al inicio:** D.P23/PR #46 Treihord (diez biografías); D.P24/PR #47 campo y Arven (doce biografías). Los 22 perfiles de esas PR son dependencias explícitas, con SHA de inicio fijados en JSON.
- **Proyecto Maestro Nimroel:** individuos importantes no procedurales; relaciones persistentes asimétricas; verdad del mundo distinta del conocimiento y percepción; CoreRPG decide estado.

## Inventario de salida
- 27 selecciones de protagonista editorial, todas referenciadas por biografía original.
- 30 relaciones condicionales; ninguna deuda, parentesco, amistad o enemistad real.
- Cuatro modelos de hogar/cuidado; cero familias jurídicas.
- Diez conflictos futuros y diez escenas TEST_ONLY; cero misiones.
- Ocho decisiones creativas documentadas.
- Inventario JSON con incógnitas nulas, validador adversarial y workflow; no CoreRPG, Godot, mapas, contratos de comercio ni WorldState modificados.

## Preguntas **que todavía no están resueltas**
1. ¿Están finalmente fusionadas PR #46 y #47 sobre el mismo canon? **No al inicio**; exigir nueva verificación antes de integrar D.P25.
2. ¿Qué biografías se convertirán en NPC únicos? Selección editorial **no responde** a presencia física, edad, atributos, hogar o itinerario.
3. ¿Qué relaciones efectivamente nacen? No existe testigo o evento instanciado que lo justifique.
4. ¿Qué casa/hogar jurídicamente existe? Ninguna genealogía ni capacidad real asignada.
5. ¿Qué permisos y rutas autorizan encuentro interregional? D05 cualitativo no crea geometría ni puerto.
6. ¿Cuáles son los bienes, precios, stocks, trabajos o deudas? UNKNOWN.
7. ¿Quién es el titular actual de Casa Darovan o los actuales mandos? No definido aquí; no inventarlos.
8. ¿Cómo integraremos agendas, revelación parcial y persistencia? Contrato conceptual D.P25/06; implementación separada.
9. ¿Qué geometría D06/D08 tendrá cada comunidad RUR-S01–S09? Pendiente de sitio real, derecho, acceso, agua y sustento.
10. ¿Qué hechos históricos sobre el reino/casas han sucedido? No se añade ninguno en D.P25.

## Revisión adversarial
El validador debe rechazar: ID repetido; biografía fuente inexistente; relación con actor no seleccionado; activación real de conflicto; contacto o encuentro fingido; ruta añadida; parentesco afirmado; permiso/fiscalidad no reconocido; `UNKNOWN` rellenado; escenas con `worldStateChanged`; títulos de mando inventados; merge autorizado por delegación; pérdida de dependencia #46/#47. Además comprobará que los 27 IDs aparecen en el capítulo 01, R01–R30 en capítulo 02, C01–C10 en capítulo 03, E01–E10 en capítulo 05 y D01–D08 en capítulo 07.

## Cierre editorial y límites de CI
D.P25 podrá declararse **APTO editorialmente** cuando corran validador propio y regresiones existentes en Windows 2022 y Ubuntu 24.04 sobre el HEAD final, y se audite su diff. La prueba no convierte documentos en habitantes, ni simula relaciones reales, ni valida caminos/puertos/rutas o el funcionamiento de Godot/Android. Un fallo de dependencias debe dejar la PR bloqueada. **La PR permanecerá Draft y no se fusionará hasta nueva autorización.**

## Traspaso obligatorio a D.P26
1. Resolver y auditar orden de PR #46 → #47 → #D.P25; si cambia el canon, reconciliar referencias sin cambiar IDs aprobados a escondidas.
2. Auditar 52 biografías, 30 relaciones hipotéticas y diez conflictos contra autoridades, mapas y D.P14–18.
3. Separar **cierre editorial** de **materialización física**: NPC y hogares solo después de sitio/contrato autorizado; integración CoreRPG/Godot en fase de desarrollo distinta.
4. Verificar que las escenas se puedan contar desde perspectivas incompatibles sin transmitir secretos indebidamente.
5. Mantener registro de incógnitas y decisión expresa cuando haya que aprobar la entidad real.

**Dictamen estructural:** D.P25 es una capa narrativa territorial completa, con integración física pendiente de forma declarada y auditable.
