# EDRANOR — PORTRAIT VISUAL BIBLE v0.1

**Proyecto:** Nimroel RPG · **Fecha:** 2026-11-13  
**Documento:** Biblia territorial de retratos NPC — Casa Edranor, centros vinculados y Rodas regia.  
**Versión:** 0.1  
**Estado:** BASE PARA PRUEBAS Y REVISIÓN ARTÍSTICA. NO RATIFICA LOS ONCE NOMBRES E10 NI CREA NPC EN CORERPG.

## 1. Propósito y límites

Esta biblia construye **personas reconocibles, distintas y realistas** en el contexto de Dorth, Lumina, Karsath, sus entornos rurales y Rodas, sin atribuir una fisonomía común de linaje a quienes viven geográficamente en Edranor.

**Rodas es aldea de Corona Aethros**, no municipio, posesión, guarnición o familia Edranor. Sus retratos se gobiernan por cultura Norgard y la identidad local regia de Rodas, aunque la carpeta documental sea la del ámbito Edranor.

Edranor E10 documenta **once personajes propuestos** con historias/roles de diseño, pero EDD-05 **mantiene pendientes sus nombres como canon individual, genealogía, sucesión y promoción a WorldState**. No se aprobarán como retratos de NPC existentes a partir del texto por sí solo.

## 2. Orden de herencia

`NIMROEL_GLOBAL_VISUAL_BIBLE_v0.5.md` → `NPC_PORTRAIT_VISUAL_BIBLE_v0.3.md` → `NORGARD_VISUAL_PROFILE_v0.1.md` y `norgard_visual_profile_v0.5.json` → `EDRANOR_PORTRAIT_VISUAL_BIBLE_v0.1.md` → fuente de persona/localidad y estado real → ficha de diversidad → prompt → PNG.

Hereda obligatoriamente `Worldbuilding/Direccion artistica/Assets/PORTRAIT_WORKFLOW_RULES.md` (ACTIVE v1.2), `PORTRAIT_REGISTRY.json` y reglas de no clonación. **No copiar la biblia física de Treskal**, porque el contexto Edranor no tiene las mismas tendencias locales aprobadas.

Diferenciar `CANON_REPO`, `VISUAL_APROBADO`, `AUTOR_APROBADO`, `PROPUESTA_E10`, `UNKNOWN` y `TEST_ONLY`. Una propuesta de biografía es fuente artística **conceptual**, no una persona ratificada.

## 3. Principio de identidad humana

**DIVERSOS — SOBRIOS — TRABAJADORES CUANDO CORRESPONDE — NO UNIFORMES — CON EDAD REAL — CON HISTORIA INDIVIDUAL.**

Casa Edranor es región vinícola importante; no significa que cada habitante sea vinicultor, adinerado, bebedor de vino, leal al ciervo o políticamente ambicioso.

No imponer:

- una cara «Edranor» con ojos, nariz, mandíbula y tez uniformes;
- cabello rubio, oscuro, ojos azules o cualquier cuota racial inexistente;
- aristócratas siempre más bellos o «genéticamente» reconocibles;
- trabajadores siempre sucios, mujeres siempre jóvenes, hombres siempre fornidos/barbudos;
- una personalidad calculada por origen, profesión o pobreza;
- vestimenta púrpura para toda la población;
- casta de berserkers como apariencia física universal de Rodas.

La diversidad se construye deliberadamente **individuo a individuo**, evitando que el modelo regenere siempre el mismo rostro.

## 4. Encuadre de retrato NPC

Estándar de la Biblia NPC v0.3:

- **Vertical 4:5**, medio busto/busto amplio, cabeza completa, hombros y torso superior.
- Postura natural ligeramente frontal o en tres cuartos suave, sin teatralidad.
- Mirada a cámara o ligera desviación; expresión contenida, reutilizable en múltiples diálogos.
- Luz físicamente plausible que revele piel, ojos y material textil.
- Fondo contextual suave y **reconocible por actividad**: calle de Dorth, meseta/bodega de Lumina, espacio sobrio de Karsath, plaza o entorno rural de Rodas, cuando el lugar individual lo autorice.
- Sin foco de estudio, glamour, armadura fantástica, héroes genéricos, filtros HDR ni decorados de castillo por defecto.

Un retrato **no es una escena de misión**: no mostrar una batalla, un secreto revelado, una ceremonia inventada o una acción ya ocurrida.

## 5. Variación física: dimensiones a resolver

Antes del prompt individual elegir, conforme a fuente:

- edad real cuando existe / **edad aparente provisional** cuando no;
- etapa `child` 0–15, `young_adult` 16–25, `adult` 26–54, `older_adult` 55–69, `elderly` 70+; son **etapas visuales, no la mayoría legal**;
- talla aparente y complexión: delgada, media, robusta, corpulenta, frágil, etc., sin causalidad automática por oficio;
- forma de cara, pómulos, frente, mandíbula, nariz, cejas, ojos, labios, orejas y asimetrías plausibles;
- cabello por color, textura, longitud, entradas/calvicie/canas y cuidado;
- barba/bigote/afeitado cuando corresponda, sin «barba medieval obligatoria»;
- postura, manos, marcas de uso/exposición al clima y señales de envejecimiento;
- expresión base y diferencias frente a personajes registrados.

La Biblia de Edranor **no asigna porcentajes de cabello/ojos/piel** porque las fuentes revisadas no establecen distribución específica. No trasladar una genética «medieval europea» por costumbre visual.

## 6. Edad, ropa, pátina y aseo

No representar ancianos como adultos jóvenes con canas superficiales: piel, volumen facial, musculatura, postura y cabello deben transmitir edad coherente. Menores con apariencia y actividades compatibles con su vida y la legislación Norgard; la mayoría civil/militar general es a los **18 años**, no la taxonomía visual.

Capas obligatorias heredadas:

- **Pátina de ropa A–D:** de nueva/poco gastada a ropa muy trabajada.
- **Presentación contextual 1–5:** desde trabajo/exposición intensa hasta ceremonia.

No confundir **ropa envejecida** con suciedad de un día. Trabajador de bodega puede tener prendas limpias fuera de turno; persona noble puede llegar cansada de viaje. El vino no tiñe automáticamente la ropa. La piel puede mostrar sol, viento o trabajo cuando la biografía lo soporte.

Tejidos, delantales, botas, cierres, herramientas y joyería acorde con medios y oficio. Sin vestuario elegante para todas las personas porque la Casa es próspera.

## 7. Dorth: sede, tintos y diferencia social

Dorth es ciudad de trabajo productivo y administración señorial. Contextos plausibles para retratos **con oficio autorizado**:

- recepción de uva, registro y medición de lotes;
- prensado, elaboración, guarda y expedición de vino tinto;
- tonelero, aprendiz, comerciante, carretero y trabajo de almacén;
- personas en administración, registro, recepción y oficios civiles;
- hogares y servicios con realidades materiales distintas.

Una figura con libro no es automáticamente funcionario de Justicia; un comerciate no posee todas las bodegas. No colocar insignias de Corona/Casa sin acreditación del cargo. El entorno boscoso de Azurios no autoriza mostrarse como propietario de su sector regio.

**Protocolo Edranor:** la Casa actúa como administradora subordinada; ni la vestimenta ni un retrato convierten al titular propuesto en monarca soberano.

## 8. Lumina: blancos, vida artesanal y Bosque Alto

Lumina es pequeña y compacta; **vinos blancos**, plaza alargada y mercado anual, entorno de meseta/Bosque Alto. Retratos posibles de vinicultores, artesanos, tonelero, comerciantes, vecinos, hogares y visitantes **si la identidad y actividad están autorizadas**.

El fondo debe diferenciar un taller/bodega modesto de un comercio urbano gigante. Piedra clara/teja roja y madera trabajada cuando esas superficies resultan visibles, sin imponerlas a la ropa.

Un retrato situado en el mercado del vino presupone **el día del evento**, no un mercado cotidiano. La madera de Bosque Alto está sometida a aprovechamiento controlado: un tonelero no recibe automáticamente una licencia de extracción.

## 9. Karsath: pequeña escala, paisaje abierto y vino escaso

Karsath tiene carácter lacustre y especialización en vino **muy limitado/exclusivo**. Los retratos deben comunicar **el trabajo del individuo**, no un aristócrata con copa de oro por defecto. Producción escasa no determina riqueza, belleza, moralidad o dieta.

Fondos contextuales: espacio abierto, piedra/teja, conservación de lotes pequeños o entornos domésticos si autorizados. El lago puede ser referencia remota, **nunca muelle, orilla urbana o navegación** sin fuente E02.

No inventar denominaciones, rituales de catar, variedades, barricas especiales o marcas oficiales por la escasez del producto.

## 10. Rodas: personas de una aldea regia

Rodas es **aldea Aethros**, de entorno septentrional, arquitectura de piedra oscura, madera y tejados muy inclinados de pizarra. Su vida incluye campesinos, familias, artesanos y herrerías pequeñas; no es una comunidad de combatientes en estado permanente.

En un retrato civil de Rodas:

- ropa práctica y protección climática **según la escena real**, no uniforme militar general;
- fondo de aldea, plaza abierta, casas bajas o campo, evitando templo y fortaleza;
- la **Casa Druídica custodiada** puede contextualizar un personaje autorizado, pero no convierte a cualquiera en sacerdote ni hechicero;
- un berserker tiene identidad y competencia individuales, no transformación permanente ni «ojos mágicos»;
- la poción druídica, su elaboración y los rituales excepcionales no se dibujan como poderes cotidianos;
- **toda insignia de autoridad responde a la Corona Aethros**, no al ciervo Edranor.

La Casa Druídica tiene tradición y custodia, **NO culto religioso**. Las figuras regias necesitan permiso de acceso y competencia, no se deducen por el paisaje.

## 11. Once nombres de E10: PROPUESTA, nunca canon automáticamente

`Personajes/E10_PERSONAJES_Y_RELACIONES.md` propone:

| Contexto | Personajes de diseño | Estado |
| --- | --- | --- |
| Dorth / familia Edranor | Lady Elira Edranor, Maelis Edranor, Caelen Edranor, Vesra Edranor | `PROPUESTA_E10`; genealogía, nombramiento y sucesión pendientes EDD-05 |
| Dorth | Orlan Vereth | Comerciante propuesto, no NPC activo |
| Lumina | Ysna Calven, Tovan Brask | Bodega y tonelería propuestas, sin propiedad ni contrato real |
| Karsath | Lira Venn | Productora propuesta, sin viñedo o inventario materializado |
| Rodas | Heran Malk, Saer Celdan, Bren Tovar | Interlocución, custodia y fragua propuestas bajo régimen regio, sin cargos ratificados |

Los once nombres están **escritos como candidatos de composición narrativa**, **NO RATIFICADOS** por el autor como personas canónicas existentes. En particular:

- Lady Elira **no** se reconoce como titular actual real por una imagen.
- Maelis **no** es heredera jurídica efectiva por su retrato; Caelen y Vesra tampoco reciben derechos automáticos.
- Heran no es delegado regio nombrado; Saer no es sacerdotisa ni autoridad militar; Bren no es berserker por su profesión.
- Edad, rostro, estatura, sexo visual cuando no esté definido, cabello, parentesco legal, prendas heráldicas, oficio vigente, horarios, relaciones y domicilios **no se inventan como canon**.
- Si se hace un **concept art** de estos nombres, etiquetarlo `PROPOSAL_PENDING_AUTHOR`, con identidad facial provisional y sin registrar al personaje como NPC existente.

Los conflictos, ocho escenas y relaciones E10 son **diseños**, no eventos o memorias activadas.

## 12. Nombre, linaje, símbolos y derechos

La regla general de Norgard es nombre y un apellido, con eventual segundo nombre. **Aethros, Edranor, Darovan, Galdren y Valrik son apellidos protegidos**; no se asignan a extras ni se usan para afirmar herencia.

El emblema **Edranor** es ciervo de plata envejecida y gran cornamenta sobre púrpura vino oscuro. Debe usarse **únicamente** con cargo, documento o representación autorizados. La Corona Aethros usa el lobo azul/plata; en Rodas no se reemplaza por el ciervo.

No inventar dialecto Edranor, tatuajes de vendimia, marcas familiares «de sangre», ritos de vino, ornamentos religiosos, uniformes específicos de oficios o nobleza de todas las personas ricas.

## 13. Relaciones y privacidad

Un retrato **no establece** amistad, parentesco, residencia, deuda, rango, propiedad, confianza, acusación ni memoria privada. E10 distingue expresamente deseos y conflictos narrativos de hechos jurídicos. Ningún personaje conoce todo el canon ni tiene acceso a archivos por su aspecto.

La rivalidad política sobre Rodas no convierte a sus vecinos en rebeldes ni a la Casa Edranor en villanos inevitables. No usar expresión «sospechosa» para representar culpa futura. La IA narrativa no crea testimonios ni acciones desde una imagen.

## 14. Revisión anatómica: rostros, manos y objetos

Examinar el PNG final ampliado:

- dos ojos coherentes, párpados, orejas, nariz, boca y dentadura plausibles;
- cuello correctamente conectado a cabeza y hombros, sin extremidades o torsos duplicados;
- dedos y manos completos sin deformación, herramienta fusionada o mangas que atraviesen piel;
- accesorios, cabello, sombreros y prendas sin mezclas antinaturales;
- animales incidentales conforme a §9.1 de `SCENE_ENVIRONMENT_VISUAL_BIBLE_v0.1`.

No justificar defectos generativos como rasgos de un personaje fantástico salvo canon explícito. Ante error evidente, **REJECTED; corregir/regenerar y verificar**.

## 15. Diversidad y registro antes del prompt

`PORTRAIT_WORKFLOW_RULES.md` exige consultar `PORTRAIT_REGISTRY.json` **antes de cualquier nueva generación**. Formar pool comparable:

1. misma localización, oficio y sexo;
2. localización/grupo profesional/sexo;
3. cultura o región/oficio/sexo;
4. conjunto visual próximo para control de identidad.

Resolver una **ficha individual** (edad, complexión, cara, mandíbula, nariz, ojos, cabello, entradas/canas, vello facial, piel, asimetrías, ropa, contexto, pátina/presentación) **antes** de redactar el prompt. No hacer la misma cara con otra vestimenta.

Los retratos de Treskal registrados sirven como referente estilístico general Norgard, **no como familia física que deba copiarse** en Edranor. No registrar en el catálogo retratos no aprobados ni declarar sincronizado un PNG sin NAP.

## 16. Metadatos de la ficha individual

Por cada retrato se deben conservar:

- `asset_id`, `character_source_id` si procede y `subject_status` (genérico, concepto E10, personaje instanciado).
- `culture`, `realm`, `region`, `location`, `role`, `sex` según NAP y evidencia.
- Fuentes y versiones; autoridad del lugar (Edranor o **Corona/Rodas**).
- Edad aparente/etapa, complexión, morfología facial, cabello y vello; señalar lo `PROVISIONAL`.
- Ropa, herramientas y accesorios permitidos; pátina A–D y presentación 1–5.
- Fondo contextual aprobado, cámara y luz.
- Pool revisado y diferencias anticlonación.
- Resultado de control anatómico, discrepancias entre prompt e imagen, estado de revisión visual y procesamiento técnico NAP.
- `_visual_identity.json`: **describir exactamente lo visible en la imagen**, no inventar atributos invisibles de personalidad o genealogía.

## 17. NAP 2.0: perfil de retratos

En NAP actual, Nimroel admite `asset_type=portrait`, `production_profile=portrait_npc`, PNG maestro estático **4:5 exacto** y WebP derivado **768×960 Q90**, sin recorte ni relleno silencioso.

Manifest JSON v2, `classification` **culture, location, role, sex** obligatorias; realm y region admitidas. ZIP **plano de cinco archivos**:

`<id>.png`, `<id>_manifest.json`, `<id>_prompt.md`, `<id>_info.md`, `<id>_visual_identity.json`.

El perfil debe verificarse en `robdor80/NAP/config/universes/nimroel/profile.json` antes de cada producción. El valor técnico `location` **no prueba existencia de una persona o asentamiento**.

**Validación NAP ≠ aprobación facial ≠ ratificación de E10 ≠ NPC activo en WorldState.**

## 18. Checklist de aceptación

- [ ] Se ha consultado la Biblia NPC v0.3, Norgard y el registro de retratos.
- [ ] La persona es genérica autorizada, concepto rotulado o NPC realmente ratificado.
- [ ] No se promociona ninguno de los once E10 a canon por su aspecto.
- [ ] Rodas se mantiene bajo autoridad regia, con oficio/sexo/edad reales según fuente.
- [ ] No se inventan linajes, títulos, parentescos, residencias o rango.
- [ ] Rasgos faciales y cuerpo individualizados; el pool no contiene un clon.
- [ ] Piel y edad realistas, sin embellecimiento de toda la población.
- [ ] Ropa y herramientas corresponden a oficio/vida, no a estereotipo vinícola.
- [ ] Pátina A–D y presentación 1–5 están diferenciadas.
- [ ] Fondo no inventa puerto, templo, bodega operativa o ruta de viaje.
- [ ] Heráldica correcta, sin ciervo en autoridad Aethros de Rodas.
- [ ] Anatomía humana/animal ampliada y aprobada.
- [ ] PNG/JSON/ZIP cumplen NAP y describen fielmente al sujeto.
- [ ] Se separan aprobación autoral, técnica y materialización.

## 19. Fuentes y reservas

**Biblias:** `Worldbuilding/Direccion artistica/Biblia visual/General/NIMROEL_GLOBAL_VISUAL_BIBLE_v0.5.md`; `Categorias/NPC/NPC_PORTRAIT_VISUAL_BIBLE_v0.3.md`; `Categorias/Escenas/SCENE_ENVIRONMENT_VISUAL_BIBLE_v0.1.md`; `Culturas/Norgard/NORGARD_VISUAL_PROFILE_v0.1.md` y datos operativos v0.5.

**Workflow:** `Worldbuilding/Direccion artistica/Assets/PORTRAIT_WORKFLOW_RULES.md`; `PORTRAIT_REGISTRY.json`.

**Edranor** (bajo `Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor/`): `Auditorias/E12_INVENTARIO_CANON_Y_AUTORIDAD.md`; `Auditorias/E12_REGISTRO_INCIDENCIAS.md`; `Personajes/E10_PERSONAJES_Y_RELACIONES.md`; `Personajes/E10_CASA_FAMILIA_Y_SUCESION.md`; `Cultura/E10_COSTUMBRES_CIVILES_Y_OFICIOS.md`; `Cultura/E10_RODAS_IDENTIDAD_Y_CUSTODIA.md`; fichas E07 Dorth/Lumina/Karsath/Rodas; `Poblacion_y_hogares/E08_OFICIOS_Y_EMPLEO.md`.

**Heráldica:** `Worldbuilding/Direccion artistica/Biblia visual/Culturas/Norgard/Heráldica/Casa Edranor/EDRANOR_HERALDIC_EMBLEM_v0.1_PROMPT.md`. **NAP:** `robdor80/NAP/config/universes/nimroel/profile.json`.

**Reserva clave:** EDD-05 requiere ratificación del autor antes de declarar personajes E10 como personas existentes, familias legales o cargos reales.

---

**Regla final:** un retrato Edranor muestra **una persona irrepetible con contexto territorial correcto**, no «un noble del vino» genérico ni una identidad propuesta convertida por error en canon.
