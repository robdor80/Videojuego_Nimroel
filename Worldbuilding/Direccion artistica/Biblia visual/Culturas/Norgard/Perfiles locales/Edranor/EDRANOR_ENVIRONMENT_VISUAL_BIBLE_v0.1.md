# EDRANOR — ENVIRONMENT VISUAL BIBLE v0.1

**Proyecto:** Nimroel RPG · **Fecha:** 2026-11-13  
**Ámbito:** paisajes, bosques, viñedos, suelos, clima, rutas, naturaleza e interiores ambientales del territorio Edranor.  
**Estado:** BASE PARA PRUEBAS Y REVISIÓN ARTÍSTICA. NO CREA CANON, CARTOGRAFÍA NI INSTANCIAS JUGABLES.

## 1. Alcance y jerarquía

Esta biblia especializa la ambientación de Casa Edranor, **sin convertirla en una estética de viñedos omnipresentes**. Para edificios, aldeas, pueblos, villas y los núcleos manuales usar también `EDRANOR_LOCATIONS_VISUAL_BIBLE_v0.1.md`; para personas, `EDRANOR_PORTRAIT_VISUAL_BIBLE_v0.1.md`.

Jerarquía: `NIMROEL_GLOBAL_VISUAL_BIBLE_v0.5` → `SCENE_ENVIRONMENT_VISUAL_BIBLE_v0.1` (incluida prevención de animales fusionados §9.1) → `SETTLEMENT_VISUAL_BIBLE_v0.1` si aplica → `NORGARD_VISUAL_PROFILE_v0.1` + operativo `norgard_visual_profile_v0.5.json` → Edranor E00–E12 → localización, autoridad y estado → prompt/asset.

Etiquetas obligatorias: `CANON_REPO`, `VISUAL_APROBADO`, `AUTOR_APROBADO`, `OBSERVACION_MAPA`, `DERIVED_CONDITIONAL`, `PROPUESTA`, `UNKNOWN`, `TEST_ONLY`. Ninguna fuente de menor autoridad rellena automáticamente otra de mayor.

El cierre E12 de la PR #64 es **documental/contractual**, no el mundo materializado en CoreRPG o Godot. Continúan pendientes EDD-01/02/03/04/05/07/08. EDD-06 resolvió Rodas como **aldea bajo autoridad real Aethros**, no ciudad Edranor.

## 2. ADN visual

**CENTRO-OCCIDENTE DE NORGARD — SOBRIO — PRODUCTIVO — VITIVINÍCOLA SIN MONOCULTIVO — BOSQUES DIFERENCIADOS — ARTESANAL — FÍSICO — HABITADO.**

Realismo cinematográfico naturalista: piedra, madera, teja y pizarra según localidad; luz motivada; colores de suelo, vegetación, metal y vino según materia, no filtros; desgaste localizado por uso. La riqueza de la Casa no equivale a riqueza individual. La heráldica tampoco define la paleta cromática de cada casa o viñedo.

No llenar automáticamente panorámicas de hileras de viñas, barricas, ciervos, púrpura, castillos, jinetes nobiliarios o mercados del vino. Su presencia requiere sitio, función y estado.

## 3. Siete unidades físicas cualitativas E01

Los siete identificadores son **unidades de estudio, no polígonos ni límites políticos**:

| Unidad E01 | Referencia utilizable | No afirmar |
| --- | --- | --- |
| `west_valkram_interface` | Transición próxima a Valkram | Paso, mina, carretera, ladera o dominio parcelario específico |
| `karsath_central_west` | Contexto central-occidental más abierto de Karsath | Ribera, muelle o viñedo cultivado concreto |
| `lumina_bosque_alto` | Meseta y Bosque Alto próximo a Lumina | Tala, parcelas, sendero o propietarios determinados |
| `central_wine_context` | Gran territorio vitícola de Norgard | Que todo suelo esté plantado de vid |
| `dorth_azurios_west` | Transición de Dorth a Bosque de los Azurios | Que todo el bosque y su sector real sean de la Casa |
| `north_cold_transition` | Gradiente frío central–boreal de Norgard | Frontera climática local exacta |
| `far_north_unclosed` | Norte polar solo como contexto regional | Pertenencia efectiva a Edranor, asentamientos o viñas polares |

Ninguna unidad E01 crea una localización NAP ni un sitio presente en WorldState.

## 4. Bosque Alto y Azurios

**Bosque Alto, Lumina:** masa templada mixta de meseta, robles y hayas donde corresponde; coníferas en sectores más fríos/expuestos. La madera abastece artesanía de barricas, toneles y bodegas con aprovechamiento **importante pero controlado**. No inventar talas sin derechos, concesiones, especies nuevas, inventarios o carreteras de saca.

**Bosque de los Azurios, Dorth:** mosaico continental/montano con frondosas en cotas bajas y mezcla de coníferas en otros pisos. **Su sector meridional próximo a Hallheim es Bosque Real de Aethros**. No atribuirlo ni adjudicar su aprovechamiento a Edranor. Bosques de Norgard no son fondos intercambiables.

La «caza abundante» de fuentes generales no permite representar especies, densidades, cotos o botín sin comprobación.

## 5. Vid, uva y vino: ambiente, no inventario

La identidad principal de Edranor es el vino, pero `E04_VITICULTURA_Y_VENDIMIA` exige para **cada viñedo real** suelo, pendiente, climatología, agua, variedad, acceso, titularidad y derecho de uso comprobados. La viticultura puede ser de secano; **no instalar riego ni canales por defecto**.

Podrán representarse labores de poda, vendimia, transporte, prensado, elaboración, almacenamiento y crianza **cuando la escena esté autorizada y situada**. No decidir estaciones o fecha de vendimia, tipo de uva, marca, cosecha, volumen de barriles, precio, bodega propietaria, contratos o abundancia sin datos.

Lumina se asocia a **blancos**, Dorth a **tintos**, Karsath a vinos **muy escasos y exclusivos**, y Rodas **no se transforma en localidad vinícola Edranor** por su cercanía geográfica. La tonelería necesita madera legal, herramientas, secado y trabajo: no materializar toneles infinitos.

## 6. Aguas y relieve sin fingir geografía

El **Lurien** y **Lago Antela** son referencias de escala Norgard; E02 y E12 no certificaron ribera, lago, afluente o navegabilidad **en un emplazamiento local Edranor concreto**. Karsath cuenta con un contexto **visual lacustre**, con Antela situado al sur en canon, pero no tiene puerto, embarcadero, paseo de orilla ni agua potable demostrados por ese hecho.

E05 formuló cuatro interrogantes de conectividad y **cero aristas físicas certificadas**. No trazar carretera Dorth–Lumina–Karsath–Rodas, puente, vado, ferry, calzada o servicio de posta por necesidad narrativa. La cámara y el fondo no sustituyen a un mapa autorizado.

## 7. Clima, luz, astronomía y estaciones

Norgard tiene gradientes continentales y septentrionales; E03 no determina datos locales de lluvia, viento, isoyetas, fechas de helada, duración de nieve ni calendario de vendimia.

- Lumina: meseta elevada y bosque mixto, sin precipitación o temperaturas exactas.
- Dorth: contexto sobrio junto a Azurios; no humo, tormenta, río o niebla obligatorios.
- Karsath: paisaje abierto de referencia seco/semiárido; no desierto permanente.
- Rodas: entorno septentrional frío y austero con nieve en **montañas lejanas** según su perfil, sin nieve permanente en cada vivienda ni climas trasladados al resto.
- Norte no delimitado: no atribuir a Edranor tundra ni polaridad propias antes de EDD-01/02.

Para noche, heredar la astronomía de las **tres lunas de Nimroel**. No colocar lunas decorativas ni luces modernas. Hora, estación, nubes, fuego y barro derivan de datos de escena o se señalan como hipótesis visuales.

## 8. Interiores y materia de trabajo

Los espacios de bodega, almacén, tonelería, vivienda, comercio, trabajo agrícola y recepción señorial deben ser físicamente construibles: acceso practicable, iluminación, ventilación, personas y mercancía proporcionados. No crear una fábrica de producción industrial moderna, barricas de escala imposible, toneles mágicos o salas palaciegas por prestigio.

La Casa Druídica de Rodas está **custodiada y no es templo**, y no tiene culto, espectáculo mágico, ritual público ni arquitectura religiosa inventada. El protocolo de alojamiento regio en Dorth no autoriza dibujar un palacio nuevo con plano definitivo.

La presencia de objeto no confiere su posesión, consentimiento o inventario en CoreRPG.

## 9. Actividad humana y anatomía animal

Los animales y personas son individuos físicos, no relleno de composición. La sección 9.1 de la Biblia de Escenas Ambientales es **obligatoria**: sin gallinas bicéfalas, ovejas fusionadas, cuerpos compartidos, patas adicionales, brazos y cabezas unidos indebidamente.

Antes de aprobar, **ampliar cada zona con animales** (corrales, huertos, caminos) y personas en grupos; comprobar cabeza, cuello, tronco y articulaciones por individuo. Si hay duplicación, fusión o ambigüedad anatómica relevante: **REJECTED, corregir/regenerar y revisar el PNG final**. No disimular errores en el prompt o en la identidad visual JSON.

No introducir fauna extraordinaria o animales de caza sin apoyo de lugar/estación.

## 10. Heráldica y administración

Casa Edranor: **ciervo heráldico de plata envejecida con gran cornamenta sobre púrpura vino oscuro**, según emblema maestro aprobado. No añadir uvas, corona o nuevos símbolos. Solo mostrar heráldica donde la Casa tenga un uso autorizado.

Corona Aethros: **lobo azul y plata**. **Rodas pertenece a la Corona**, con sus berserkers, jurisdicción, justicia, impuestos y mando; no colocar ciervos Edranor como marcas de autoridad allí. Tampoco transferir el Bosque Real de Azurios a la Casa. Sin aduanas interiores, ceca o ejército soberano.

No inventar capillas, símbolos religiosos, textos falsos, gremios, festividades ni magia de ambiente.

## 11. Cámara y continuidad

Priorizar propósito: llegada, fondo de actividad, bosque, viñedo condicional, exterior, interior y ambiente temporal. Profundidad natural primer plano–medio–fondo; cámara a altura humana cuando se presenta exploración, sin panorámicas imposibles de «todas las viñas».

Para una ubicación **realmente fijada** y vinculada a instancia/fixture válido, una imagen madre `DAY_BASE` permite lluvia, noche y estación conservando terreno, edificaciones, rutas, árboles principales y cámara. No imponer una única DAY_BASE canónica a todos los ensayos E06.

El fondo Godot 2D no materializa navegación, NPC, puestos de mercado o actividad comercial.

## 12. Requisitos NAP consultados

Contrato externo vigente: `asset_type=scene`, `production_profile=scene_environment`, PNG estático **16:9 exacto**; conversión WebP **1920×1080 Q90**, sin crop/pad silenciosos. Clasificación `culture` y `location` obligatoria; `realm`/`region` permitidas.

Paquete ZIP plano de cinco archivos: `<id>.png`, `<id>_manifest.json` v2, `<id>_prompt.md`, `<id>_info.md`, `<id>_visual_identity.json`. Sin WebP de entrada. Comprobar siempre el `robdor80/NAP/config/universes/nimroel/profile.json` actual antes de producir; el contrato técnico no es un decreto artístico.

## 13. Ficha de generación y comprobación

Registrar **fuente y versión**, localización real/instancia, autoridad (Casa o Corona), finalidad, E01 cualitativa, relieve/cubierta/agua, actividad y derechos, hora/clima, cámara, elementos visibles, prohibiciones, incertidumbres, serie `DAY_BASE` y perfil NAP.

Lista de aceptación:

- [ ] No hay viñedos, parcelas, caminos, ríos, riberas o minas creados sin autoridad.
- [ ] Bosque Alto y Azurios no se confunden; Bosque Real no se adjudica a Edranor.
- [ ] Dorth/Lumina/Karsath/Rodas presentan entornos y escalas diferentes.
- [ ] Rodas permanece en ámbito jurídico y militar Aethros, no en Casa Edranor.
- [ ] No hay fechas de vendimia, cifras de cosecha o cultivos polares inventados.
- [ ] Herramientas, animales y personas son físicamente posibles.
- [ ] Se han ampliado y examinado grupos de fauna: **no animales fusionados**.
- [ ] Meteorología y luz dependen de estado real o hipótesis rotulada.
- [ ] Variantes mantienen la identidad espacial, y sus metadatos describen lo visible.
- [ ] NAP valida el paquete por separado de la **aprobación humana de canon visual**.

## 14. Fuentes consultadas y reservas

**Biblias superiores:** `Worldbuilding/Direccion artistica/Biblia visual/General/NIMROEL_GLOBAL_VISUAL_BIBLE_v0.5.md`; `Categorias/Escenas/SCENE_ENVIRONMENT_VISUAL_BIBLE_v0.1.md`; `Categorias/Asentamientos/SETTLEMENT_VISUAL_BIBLE_v0.1.md`; `Culturas/Norgard/NORGARD_VISUAL_PROFILE_v0.1.md` + `Datos operativos/norgard_visual_profile_v0.5.json`.

**Edranor** (bajo `Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor/`): `Auditorias/E12_INVENTARIO_CANON_Y_AUTORIDAD.md`; `Auditorias/E12_ACTA_CIERRE.md`; `Ecosistemas/E03_ATLAS_ECOLOGICO.md`; `Clima/E03_FRANJAS_Y_MICROCLIMAS.md`; `Suelos/E03_EDAFOLOGIA_Y_VITICULTURA.md`; `Viticultura/E04_VITICULTURA_Y_VENDIMIA.md`; `Toneleria/E04_BOSQUE_ALTO_Y_TONELERIA.md`; `Asentamientos/E06_ESQUELETO_ELEGIBILIDAD.md`; `Ciudades/Dorth/E07_DORTH.md`; `Ciudades/Lumina/E07_LUMINA.md`; `Ciudades/Karsath/E07_KARSATH.md`; `Ciudades/Rodas/E07_RODAS.md`.

Heráldica: `Culturas/Norgard/Heráldica/Casa Edranor/EDRANOR_HERALDIC_EMBLEM_v0.1_PROMPT.md`. Contrato NAP: `config/universes/nimroel/profile.json`. Suelos, cursos de agua locales, caminos, censo, genealogía y persistencia siguen pendientes como los define E12.

---

**Regla final:** el paisaje Edranor se construye desde la **geografía y los usos autorizados**, nunca colocando viñas, ciervos y barricas en cualquier lugar.
