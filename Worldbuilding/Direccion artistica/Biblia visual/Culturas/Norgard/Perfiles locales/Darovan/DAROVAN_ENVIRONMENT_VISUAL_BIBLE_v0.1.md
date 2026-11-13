# DAROVAN — ENVIRONMENT VISUAL BIBLE v0.1

**Proyecto:** Nimroel RPG  
**Documento:** Biblia territorial de escenas ambientales — Casa Darovan  
**Versión:** 0.1 · 13/11/2026  
**Estado:** BASE PARA PRUEBAS Y REVISIÓN ARTÍSTICA; NO CREA GEOGRAFÍA NI CANON NUEVO  
**Ámbito:** Paisajes, naturaleza, rutas, costas, bosques, montañas, atmósfera, exteriores e interiores ambientales del territorio de Casa Darovan, Norgard.

---

## 1. Propósito

Concretar cómo se representan **escenas ambientales de Darovan** sin reducir un territorio diverso a una estética única. Esta biblia regula el **entorno y su percepción**. Las vistas urbanas y las escalas de aldeas, pueblos, villas y cuatro ciudades manuales se completan con `DAROVAN_LOCATIONS_VISUAL_BIBLE_v0.1.md`; los rostros y NPC con `DAROVAN_PORTRAIT_VISUAL_BIBLE_v0.1.md`.

Esta biblia **no crea** minas, caminos, puentes, muelles, aldeas, calas, edificios, propietarios, climas observados ni seres vivos que no estén acreditados. Las doce unidades `d01_*` son **zonas cualitativas de estudio**, no polígonos ni fronteras.

## 2. Autoridad documental y orden de herencia

**NIMROEL_GLOBAL_VISUAL_BIBLE_v0.5 → SCENE_ENVIRONMENT_VISUAL_BIBLE_v0.1 → SETTLEMENT_VISUAL_BIBLE_v0.1 (si hay poblado o edificio) → NORGARD_VISUAL_PROFILE_v0.1 y norgard_visual_profile_v0.5.json → fuentes Darovan D00–D10 y D.P13–D.P26 → geografía/estación/estado de instancia → prompt resuelto → asset.**

No asumir que toda fase editorial construye físicamente el lugar: D.P26 es cierre de diseño, no mundo 2D materializado. D01–D03 contienen anclas y derivaciones cualitativas, no un modelo digital de terreno. Para discrepancias prevalecen las fuentes autorizadas y decisiones de autor, no una visualización anterior.

Etiquetar los hechos utilizados:

- `AUTHORED/CANON`: respaldado por fuentes de Norgard/Darovan o decisión autoral.
- `DERIVED_CONDITIONAL`: inferencia física plausible, dependiente de datos locales.
- `PROPOSAL/UNKNOWN`: sin autorización suficiente para representarlo como hecho.
- `TEST_ONLY`: fixture o simulacro, **jamás** ubicación o evento real del mundo.
- `SCENE_CHOICE`: elección artística de encuadre/luz sin alterar geografía o historia.

## 3. ADN visual específico

**OCCIDENTE DIVERSO — GEOLOGÍA REAL — TRABAJO Y MATERIA — COSTA HABITADA — BOSQUES DIFERENCIADOS — FANTASÍA CONTENIDA.**

La identidad de Darovan no equivale a rojo y oro omnipresentes, minas en cada colina, castillos por todas partes, puerto en cada cala o nieve en todo el paisaje. La riqueza minera y comercial de la Casa convive con medios rurales, actividad artesanal, vida portuaria y desigualdades reales.

Materialidad naturalista, luz físicamente motivada, color sin saturación artificial, escala humana, mantenimiento contextual y señales de actividad proporcionadas. El paisaje es bello **por su funcionamiento y localización**, no por una cascada o pico espectacular inventados.

## 4. Matriz de paisajes y anclas permitidas

| Ámbito | Identidad visual respaldada | Riesgo de invención prohibida |
| --- | --- | --- |
| Montes Valkram | Gran cadena occidental N–S, metal precioso oro/plata, laderas y transiciones reales aún por cartografiar | No abrir nuevas minas, bocaminas, pasos, fronteras coincidentes con toda cresta o nieve permanente |
| Montañas Elyra | Cadena meridional vinculada a transición hacia península | No enlazar con pasos concretos, puentes ni explotaciones no acreditadas |
| Franja norte y Agujas | Gradiente frío; Bosque de las Agujas de coníferas antiguas y caza mayor, **sin población permanente interior** | No inventar aldeas en el bosque ni invierno/ventiscas perpetuas |
| Belara / Treihord | Río Belara junto a Treihord, actividad fluvial industrial de bajo calado en su tramo, entorno de abastecimiento | No hacer que el río atraviese la ciudad ni introducir buques oceánicos |
| Veldora y litoral occidental | Golfo, puerto marítimo principal, mar y contacto humano; ríos Lhera y Veldora independientes | No fusionar las dos desembocaduras, inventar bocas métricas, islas o rutas |
| Bosque de La Linde | Bosque pequeño junto a corredor existente, explotación maderera limitada y caza escasa | No transformarlo en enorme bosque de recursos infinitos |
| Bosque de los Pilares | **Una** masa forestal con claros y aprovechamiento ligado a minería | No duplicarlo como varios bosques ni inventar concesiones o talas ilimitadas |
| Taramin norte/centro | Península de colinas ocres, piedra, matorral, breñas, pastos duros y variabilidad de agua | No desierto de arena uniforme, oasis y cauces permanentes inventados |
| Bosque de Taramin hacia el sur | **Un solo bosque longitudinal**: transición de coníferas a mixto y subtropical húmedo hacia el sur | No tres bosques independientes, tala industrial supuesta o selva idéntica en toda la península |
| Isla de Syvaris | Isla cálida parcialmente seca; lomas, roca, calas y sectores resguardados más verdes; bosquetes discontinuos | No selva continua, desierto total ni montañas alpinas |
| Isla de Arven | Administración Darovan; Bosque del Manto Verde continuo, coníferas ~90 %, aprovechamiento maderero limitado | No copiar la vegetación de Syvaris, ni abrir carreteras y ferris nuevos |

Esta tabla es **un filtro de elegibilidad** para el prompt: no garantiza que desde cualquier ubicación se vea cada elemento.

## 5. Agua y litoral: precisión narrativa

- Mantener separados el **Belara** y la red central del **Lurien**. El Lurien nace en la vertiente oriental de Valkram; no se inventa confluencia local.
- En Veldora, **Lhera** y **río Veldora** son cursos distintos, con desembocaduras propias hacia el golfo; no fijar su distancia, navegabilidad ni plano urbano al dibujarlos.
- En Taramin, **Thalen** es un río con **dos brazos terminales**: no representarlo como dos grandes ríos independientes ni decidir en qué brazo navegan embarcaciones.
- Syvaris posee **bahía principal resguardada**; sus calas menores no implican muelles ni rutas de comercio.
- La costa de Arven se distingue de Syvaris; su litoral interior frente al Golfo de Veldora alberga referencias a aldeas, pero sin emplazamiento nuevo.
- La existencia de mar, desembocadura o escorrentía **no acredita agua potable**, puentes, vados, fondeaderos, barcos ni explotación pesquera en un punto preciso.

La meteorología condiciona oleaje, suelo húmedo y visibilidad; no se decide mareas o corrientes marítimas sin fuente.

## 6. Bosques, biomas y estacionalidad

No usar el mismo conjunto de árboles en todos los territorios. Las coníferas antiguas de Agujas, la limitada Linde, los claros de Pilares, la secuencia norte-sur de Taramin, los bosquetes discontinuos de Syvaris y la cobertura continua de Arven tienen **identidades diferentes**.

Una lluvia puntual no vuelve tropical un bosque, ni una mañana soleada convierte un entorno seco en pradera de regadío. La escena hereda clima, estación, disponibilidad hídrica y suelo de su fuente. No asignar especies nuevas, floraciones, fauna abundante o cortes de madera sin autorización.

En Arven, la cifra de cubierta forestal aproximada **90 %** se refiere a la isla, no a cada encuadre y no convierte todas sus playas/calas en bosque cerrado.

## 7. Trabajo visible, materiales y desgaste

Los indicios de trabajo deben tener procedencia:

- **Minería y metalurgia:** mineral, acarreo, herramientas y carbón solo donde haya explotación/acceso reales; el combustible industrial de Treihord procede de **Azurios**, no de Valkram.
- **Bosque y madera:** troncos, pilas, carros y cobertizos cuando correspondan a un aprovechamiento acreditado; sin aserradero industrial automático.
- **Costa y pesca:** útiles, almacenamiento y faena cuando función e infraestructura sean reales; no crear grandes flotas para ambientar.
- **Rutas:** firme, huellas y desgaste proporcionales a importancia y tránsito, sin carretera recta ficticia entre ciudades.
- **Interiores:** mesas, útiles, capacidad, ventilación y fuentes de luz según economía y oficio; sin talleres heroicos sobredimensionados.

La riqueza de la Casa no vuelve ricos a todos sus habitantes. La suciedad, el hollín, la humedad y las reparaciones son **situaciones**, no filtros territoriales constantes.

## 8. Exteriores e interiores ambientales

En exteriores usar geometría legible, planos de profundidad y un punto de interés funcional. La topografía y la arquitectura específicas vienen de la biblia de localizaciones y de la ubicación autorizada.

En interiores observar estructura, escala y conexiones; no crear una sala del tesoro Darovan, taller de acuñación, cámara secreta, capilla, almacén militar o laboratorio de mina porque suene plausible. **El Crisol refina/ensaya; no acuña**. La galería **La Vena** es custodiada, no recorrido turístico.

Las imágenes son fondos ilustrativos: no crean inventario, caminos, NPC ni resultados de una misión.

## 9. Personas y fauna ambiental

Respetar ocupaciones y número de figuras según localidad, con diversidad realista. La procedencia territorial no determina moralidad, riqueza, idioma, personalidad o rango. Los NPC identificables se rigen por la Biblia Darovan de retratos y por fuentes de personas autorizadas.

**Control anatómico obligatorio** heredado de `SCENE_ENVIRONMENT_VISUAL_BIBLE_v0.1` §9.1: ampliar todos los grupos de animales y comprobar individuos completos, una cabeza/cuello perteneciente a cada cuerpo, extremidades físicamente coherentes, sin gallinas de doble cuello, ovejas fusionadas, patas compartidas ni humanos amalgamados. Rechazar el candidato defectuoso, aunque la deformación parezca secundaria; regenerar o editar y volver a revisar el PNG final.

No introducir criaturas o especies extraordinarias por ambientación gratuita.

## 10. Heráldica y símbolos

Casa Darovan posee una referencia heráldica de **grifo dorado envejecido sobre carmesí oscuro**. Solo mostrarla cuando exista presencia concreta y autorizada de la Casa y se reutilice su **emblema aprobado**, sin reinterpretar su silueta.

El lobo azul/plata corresponde a la Casa Aethros / Corona en el régimen documentado y no sustituye al grifo Darovan. Un guardia de la Corona no viste automáticamente estandarte Darovan; la **Armada de Norgard** no es una flota privada de Darovan.

No añadir carteles pseudoescritos, gremios imaginarios, religiones, templos, banderas o marcas de propiedad sin fuente y contexto.

## 11. Luz y astronomía

La luz debe proceder de sol, cielo, fuego, lámparas, ventanas y fuentes autorizadas. Escenas nocturnas cumplen las **tres lunas** de la Biblia General, con presencia y fase adecuadas; jamás lunas arbitrarias por adorno. No fijar amanecer, tormenta, niebla o nieve en un lugar solo porque mejoran la composición.

## 12. Continuidad y familias de variantes

Para un lugar concreto aprobado, conservar imagen madre **DAY_BASE**. Las variantes con lluvia, estación, noche o actividad cambian **lo que de verdad puede cambiar**, no relieve, edificios, silueta de costa, caminos, disposición de muelles ni arboledas por capricho.

No generar DAY_BASE de una comunidad rural meramente candidata `RUR-S01…S09` como si el emplazamiento hubiera sido cartografiado. Etiquetar `generic_reference`, `candidate_concept` o `instance_bound` y anclar su procedencia.

## 13. Uso técnico con NAP

Esta biblia es artística, **no configura NAP**. En la configuración consultada:

- `asset_type: scene`, `production_profile: scene_environment`.
- Maestro PNG 16:9 exacto; derivado WebP **1920×1080**, calidad 90, sin crop/pad silenciosos.
- ZIP plano: `<id>.png`, `<id>_manifest.json`, `<id>_prompt.md`, `<id>_info.md`, `<id>_visual_identity.json`.
- Manifest v2; clasificación obligatoria `culture` y `location`, opcional `realm`/`region` según perfil activo.
- Verificar el `profile.json` vigente en `robdor80/NAP` antes de producir. El paso de NAP no equivale a aprobación artística ni a canon territorial.

El campo `location` debe identificar una localización/instancia válida, no un nombre genérico fingido. NAP permite IDs técnicos, **no certifica que un sitio exista en lore**.

## 14. Plantilla de prompt resuelto

1. Fuentes, revisión, región, localidad e identificador de instancia.
2. Propósito de escena y grado de autoridad geográfica.
3. Relieve, agua, vegetación y bioma **permitidos**.
4. Elementos funcionales y actividad respaldados.
5. Cámara, profundidad, área libre para UI y escala.
6. Hora, estación y clima **conocidos** o hipótesis de prueba rotulada.
7. Materiales, desgaste y paleta naturalista.
8. Personas/animales con anatomía y distancias verificables.
9. Restricciones por zona (sin minas inventadas, estandartes, ríos, muelles, etc.).
10. Referencia de DAY_BASE si hay variantes; decisiones provisionales a declarar.

Conservar el prompt realmente empleado y describir **la imagen que salió**, no solo la que se quiso generar.

## 15. Checklist de revisión

- [ ] Unidad cualitativa y localización identificadas sin atribuir geometría ficticia.
- [ ] Relieve y cursos de agua compatibles con las fuentes.
- [ ] Bioma, estación y clima justificados, con diversidad regional Darovan.
- [ ] Oficios, recursos, minería, puertos y vehículos no multiplicados por decoración.
- [ ] No se confunden río Belara / Treihord, brazos del Thalen, Lhera / Veldora, Arven / Syvaris.
- [ ] No se confunden grifo Darovan y lobo de Corona.
- [ ] Animales/personas individualizados, sin partes fusionadas.
- [ ] Interiores, luces y materiales físicamente realizables.
- [ ] Imagen y metadatos separan CANON de PROPOSAL/UNKNOWN/TEST_ONLY.
- [ ] Misma ubicación conserva identidad entre variantes.
- [ ] La revisión artística es independiente de la técnica de NAP.

## 16. Fuentes y límites de vigencia

**Fuentes directas (rutas bajo `Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan/`):**

- `Geografia_local/01_marco_fisico_y_orografia_v0.1.md`.
- `D.P13/01_regiones_y_subzonas.md`; `D.P13/08_bosques_vegetacion_ecosistemas.md` y resoluciones topográficas D.P13.
- `Hidrografia/01_red_hidrografica_y_grafo_v0.1.md`.
- `Clima_local/01_gradientes_climaticos_regionales_v0.1.md`; `Clima_local/02_ecosistemas_suelos_y_microclimas_v0.1.md`.
- `Ciudades/Treihord/ANCLAS_CANONICAS_TREIHORD_v0.1.md`.
- `Cultura_y_sociedad/D10_IDENTIDAD_SOCIAL_v0.1.md`; `Cultura_y_sociedad/D10_PERFILES_LOCALES_v0.1.md`.
- `Profundizacion_2026/D.P24/01_comunidades_y_paisajes.md`.
- `Profundizacion_2026/D.P26/03_deuda_real_y_traspaso.md`.

**Fuentes visuales de categoría:** Biblia General v0.5; Escenas Ambientales v0.1 (incluido control anatómico §9.1); Asentamientos v0.1; Norgard Visual Profile v0.1 y perfil operativo Norgard v0.5. Heráldica: `.../Heráldica/Casa Darovan/DAROVAN_HERALDIC_EMBLEM_v0.1_PROMPT.md`.

**Limitaciones explícitas:** falta geografía métrica, localización precisa de asentamientos, caminos, puentes, puertos, recursos materiales y estado de partida. Esta biblia **no subsana** esas ausencias ni convierte hipótesis en canon.

---

**Regla final:** Darovan es una suma de paisajes relacionados por geografía, economía y vida; **nunca una plantilla única con montañas, grifos y riqueza añadidos a todas las escenas**.
