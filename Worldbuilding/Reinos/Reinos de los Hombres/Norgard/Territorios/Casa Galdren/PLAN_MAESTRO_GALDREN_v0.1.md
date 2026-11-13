# GALDREN — Plan maestro territorial G00–G12 v0.1
**Política:** una fase = una conversación + una rama + una PR. G00 autorizada por el autor a fusionarse si no hay conflicto canónico y pasa CI. Fases G01–G12 necesitan inicio separado. No usar Codex para G00.

| Fase | Objetivo | Salida auditable y puerta |
|---|---|---|
| **G00** | Fundación, inventario canónico, perímetro rojo, identidad, plan y contrato no-runtime | Fuentes identificadas, incertidumbres, manifest, negativas, CI, acta |
| **G01** | Geografía, relieve, límites, accidentes y **toponimia** | Atlas cualitativo, inventario de nombres existentes, ficha de accidentes sin nombre, propuestas con estado `NO_CANON`, colisiones y barreras; ratificación humana de nombres importantes |
| **G02** | Hidrología y cuencas | Caleran/brazos, Vornarsk, Keldarsk, divisorias y régimen nival; cuencas coherentes con G01; **cero ríos inventados por el dibujo** |
| **G03** | Clima, suelos y ecosistemas | Gradientes interior/costa/norte, bosques canónicos, suelos fértiles, pastos, hielo y riesgos estacionales sin uniformizar Zanthir |
| **G04** | Agricultura, ganadería y economía alimentaria | Ciclos de cultivo y cría, caballos del Bosque Quebrado, oficios, almacenamiento, abastos y dependencia de agua/suelos; sin cifras ficticias |
| **G05** | Minería, industria, Zanthir y **Forja Estelar** | Recursos Azurios, prohibición de otro yacimiento de Metal Estelar, metalurgia, herramientas/armas, permisos y mando regio permanente de la Forja (ratificación G05 13/11/2026), sin recetas mágicas no ratificadas |
| **G06** | Comunicaciones y redes económicas | Candidatos de corredores Arleon–Zanthir–capital/vecinos, fluvial/costa y restricciones por relieve/hielo; sin convertir candidatos en carreteras cartografiadas |
| **G07** | Asentamientos ordinarios y generación procedural | Arquetipos agrarios/mineros/boscosos y reglas deterministas; excluir Arleon, Zanthir, Forja, Treskal, Hallheim, Dorth; herencia Norgard |
| **G08** | Ciudades y enclaves canónicos | Arleon y Zanthir diseñados manualmente; Forja como instalación; interfaces vecinas excluidas; clasificación urbana justificada |
| **G09** | Hogares, población, servicios y oficios | Familias, viviendas, servicios y estructuras profesionales con interdependencias de G04/G05/G08, sin censos inferidos |
| **G10** | Gobierno, historia, cultura, personajes y conflictos | **G10-P01** jurisdicción, fiscalidad, justicia, seguridad, defensa; **G10-P02** historia y cultura; **G10-P03** genealogías/NPC, rivalidad Darovan y relaciones Aethros; todos con canon/propuesta separados |
| **G11** | Contratos, Content Pack y ensayos CoreRPG | IDs, manifiestos y schemas oficiales, escenarios sintéticos, regresión, C++/CTest cuando exista prueba real; Godot/Windows/Android solo si ejecutados |
| **G12** | Auditoría integral, conciliación y cierre | Matriz G00–G11, trazabilidad SHA/PR, registro de deuda canónica, verificación Windows/Linux y dictamen **documental vs jugable** |

## Dependencias
G01 → G02 → G03; G04 requiere suelos/agua; G05 requiere relieve y canon minero; G06 depende de G01/G02/G04/G05; G07 requiere reglas G03–G06; G08 precede G09; G10 cruza G04–G09; G11 reúne contratos verificables; G12 audita todo.

## Política reforzada de topónimos
1. Heredar primero la convención `Toponimia/convencion_toponimica_norgard_v0.1.md`.
2. Separar **nombres canónicos, nombres descriptivos previos, lugares sin nombre y nombres propuestos** con ficha: accidente, fuente, evidencia geográfica, idioma/origen, conflicto potencial, estado y responsable de ratificar.
3. Registrar entidades naturales aunque crucen Casas; **etiqueta geográfica ≠ potestad política**.
4. No inventar etimologías de lenguas antiguas ni personajes históricos de conveniencia; no bautizar cada tramo de cauce o colina.
5. El río Caleran conserva identidad aun cuando se ramifica; un drenaje nuevo solo puede proponerse después de justificar pendientes y cuenca.
6. Los nombres nuevos no entran al manifiesto `CANON_REPO` antes de ratificación; se mantendrán `PROPUESTA_NO_CANON`.

## Invariantes generales
**Corona única y Ley del Rey.** Sin moneda Galdren, sin aduanas interiores, sin ejército soberano; la Forja Estelar está bajo dominio, administración y mando permanente de la Corona / Casa Aethros, igual que Rodas, aun estando geográficamente en Zanthir (ratificación autoral G05, 13/11/2026). El Metal Estelar solo aparece en los **Montes Azurios**. **Treskal es de Valrik**, no Galdren. La estética Galdren no sustituye heráldica ya aprobada. No existen coordenadas, tamaño de tropas, volúmenes de cosechas, rutas ni poblaciones fijadas en G00.

## Portabilidad y niveles de prueba
Diseño para Godot 4.7.2 **2D** y CoreRPG C++20, Windows x64 y Android ARM64. JSON/Markdown y pruebas negativas = validación **documental**; no equivalen a compilación nativa, GDExtension, carga del mapa ni RPG jugable. Cualquier prueba futura deberá aportar logs y HEAD.
