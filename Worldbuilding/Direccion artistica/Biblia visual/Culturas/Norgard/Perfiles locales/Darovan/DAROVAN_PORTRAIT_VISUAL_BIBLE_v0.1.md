# DAROVAN — PORTRAIT VISUAL BIBLE v0.1

**Proyecto:** Nimroel RPG  
**Documento:** Biblia territorial de retratos NPC — Casa Darovan  
**Versión:** 0.1 · 13/11/2026  
**Estado:** BASE PARA PRUEBAS Y REVISIÓN ARTÍSTICA; NO CREA RASGOS ÉTNICOS, FAMILIAS NI PERSONAJES  
**Ámbito:** Retratos de habitantes, profesionales, viajeros y personas de relevancia editorial del territorio de Casa Darovan (Norgard).

---

## 1. Propósito y alcance

Definir criterios de **identidad visual humana** para retratos ambientados en Darovan sin inventar un «rostro Darovan» único, una genética aristocrática, una uniformidad social ni parentescos.

Esta biblia afecta al territorio Darovan: Treihord, Veldora, Taramin, Syvaris, zonas rurales y localidades efectivamente autorizadas. **Arven está bajo administración Darovan pero su identidad cultural específica continúa UNKNOWN**: no transferir costumbres ni rasgos faciales de Syvaris a Arven.

Los retratos de una misma cultura pueden variar por lugar, oficio, edad, circunstancias, riqueza, trayectoria y experiencias reales. Las biografías de D.P20–D.P25 son **bases editoriales**; una ilustración no las transforma en personas existentes en CoreRPG ni puede completar sus atributos desconocidos como canon.

## 2. Herencia obligatoria y autoridad

`NIMROEL_GLOBAL_VISUAL_BIBLE_v0.5.md` → `NPC_PORTRAIT_VISUAL_BIBLE_v0.3.md` → `NORGARD_VISUAL_PROFILE_v0.1.md` + perfil operativo `norgard_visual_profile_v0.5.json` → esta `DAROVAN_PORTRAIT_VISUAL_BIBLE_v0.1.md` → fuente de localización y personaje (D10/D.P20–25) → ficha individual resuelta → prompt → PNG.

La Biblia de retratos NPC regula encuadre, mirada, luz, piel, edad, ropa y proporción; la presente regula **contexto Darovan, diferencias internas y límites de autoría**. Si no hay fuente biográfica específica, un rostro plausible es una **elección visual**, no una nueva norma genética o un linaje del territorio.

No aplicar `TRESKAL_PORTRAIT_VISUAL_BIBLE_v0.2.md` como si fuese patrón de Darovan: es perfil local de otro territorio.

## 3. ADN humano de Darovan

**DIVERSO — SOBRIO — INDIVIDUAL — DE OFICIO REAL — DE POSICIÓN SOCIAL NO AUTOMÁTICA — VIVIDO.**

Darovan es parte de Norgard, con una economía territorial rica en minerales, metalurgia, comercio, puertos, agricultura, ganadería, pesca, trabajo forestal y logística. **La riqueza de la Casa no se atribuye al ciudadano**, ni la ambición de una dinastía se convierte en personalidad por defecto.

No imponer:

- hombres siempre musculosos, barbudos y con trenzas «vikingas»;
- toda persona de Darovan con cabello negro, ojos claros o una forma facial estándar;
- aristócratas siempre hermosos o «racialmente distintos» del resto;
- mineros eternamente cubiertos de hollín, pescadores siempre desaliñados;
- mujeres de cierta profesión siempre jóvenes, bellas o con ropa de fantasía;
- isleños desconfiados, portuarios corruptos, pobres delincuentes o nobles crueles;
- símbolos heráldicos Darovan en cada prenda.

La individualidad procede del canon del personaje y de una variación física deliberada, **no** de una plantilla regional rígida.

## 4. Encuadre y calidad de retrato

Estándar heredado de NPC v0.3: **vertical 4:5**, **medio busto o busto amplio**, cabeza completa, cuello, hombros y torso superior; postura natural ligeramente frontal o tres cuartos suave. Mirada hacia cámara o poco desviada; expresión reutilizable y contenida.

Fondo ambiental **discreto y legible por contexto** (calle, interior, taller, campo, puerto o paisaje correcto) con profundidad de campo moderada. Evitar fondos de estudio contemporáneo, bokeh agresivo, poses teatrales, héroes genéricos, luces épicas, caricatura, glamour o «cosplay».

La iluminación debe tener fuente plausible; piel real con poros, arrugas y marcas pertinentes, sin suavizado cosmético universal. Herramientas o joyas solo si tienen sentido para ese individuo; no anular la lectura facial con accesorios.

## 5. Diversidad física sin inventar etnias

No existe en las fuentes revisadas una **distribución Darovan aprobada** de color de ojos, cabello, pigmentación, estatura o morfologías faciales que justifique cuotas poblacionales territoriales fijas. No trasladar automáticamente las tendencias específicas de Treskal a Darovan.

Resolver cada candidato conforme a canon individual y diversidad plausible en Norgard:

- edad y apariencia realmente visibles;
- perfil de rostro, frente, mandíbula, pómulos, nariz, ojos, cejas, labios y asimetrías;
- cabello: color, longitud, textura, entradas, calvicie, canas;
- vello facial solo si corresponde: afeitado, bigote, barba diversa;
- complexión, postura, manos, piel y marcas de trabajo;
- expresión neutral suficientemente versátil.

Evitar clones de «varón fuerte de 35 años con barba oscura», rostros idénticos con distintos sombreros y rostros demasiado perfeccionados. Las diferencias deben ser naturales, no generadas mediante deformaciones exageradas.

**No inferir parentesco por parecido ni fabricar parecido de familia entre personajes con apellido compartido** sin genealogía autorizada.

## 6. Edad y etapa vital

Reutilizar los cinco grupos técnicos definidos por `PORTRAIT_WORKFLOW_RULES.md`: `child` 0–15, `young_adult` 16–25, `adult` 26–54, `older_adult` 55–69, `elderly` 70+. Son **grupos visuales**, no edades legales.

El envejecimiento debe afectar piel, volumen, cabello, musculatura y postura de manera realista. No hacer de todo anciano un anciano solemne ni de todo menor un trabajador adulto.

La edad exacta de una persona D.P20–D.P25 **no se inventa** cuando está pendiente. Si se requiere un retrato exploratorio, indicar `approximate_visual_age = PROVISIONAL` y solicitar validación antes de convertirlo en identidad persistente.

## 7. Ropa, materiales, pátina y presentación

Mantener las dos capas obligatorias de la Biblia General y el workflow de retratos:

- **Pátina de ropa A–D**: A excepcional/casi nueva; B cuidada; C uso cotidiano; D muy trabajada.
- **Presentación contextual 1–5**: 1 exposición intensa, 2 trabajo/viaje, 3 cuidado cotidiano, 4 muy cuidado, 5 ceremonial.

La profesión orienta y la situación decide. Un minero retratado fuera de su turno puede estar limpio; un funcionario de viaje puede llevar ropa desgastada; un portuario acomodado no necesita terciopelo ni insignias; una persona de La Costra puede estar aseada.

Usar tejidos, costuras, prendas de abrigo, cuero, delantales, herramientas, cierres y calzado plausibles para la región, estación y función. **No fijar una paleta de vestimenta Darovan obligatoria** ni uniforme heráldico civil.

La ropa clara sin uso visible en trabajadores de actividad intensa requiere justificación. No asignar pátina D o nivel 1 de suciedad a todas las personas humildes.

## 8. Contextos específicos: Treihord

Capital minera/mercantil de unos **32.000 habitantes**, con contrastes socioeconómicos entre sus **ocho barrios canónicos**:

- El Recinto: contexto documental e institucional cuando el rol lo requiera.
- Los Altos: mayor cuidado material posible, no nobleza automática.
- El Peso: orfebrería, metales, valoración, cuentas.
- Las Lonjas: comercio, carga, entrega, trato.
- Los Oficios: artesanía y aprendizaje real.
- La Calzada: viajeros, carreteros, mensajeros.
- La Ribera: trabajo de transporte fluvial somero, no marinería oceánica.
- La Costra: diversidad humana, viviendas modestas y trabajo/cuidado; **pobreza no equivale a criminalidad**.

Una persona no adquiere acceso a La Vena o La Bóveda por llevar ropa noble. El Crisol ensaya/refina, **no acuña**; un trabajador de este entorno no es empleado de una ceca Darovan.

D.P23 aprobó **diez biografías TRH-N01–N10 como bases editoriales**, no personajes instanciados. Evitar inventar sus edades, hogares y biografías familiares. Las denominaciones funcionales provisionales no deben convertirse en insignias oficiales.

## 9. Contextos específicos: Veldora

Mayor puerto comercial de Norgard y ciudad de personalidad **predominantemente tradicional y gremial** según D.P20; red de talleres familiares, confianza y oficios que conviven con intercambio exterior.

Un estibador, contable, marinero, aprendiz, comerciante o persona de servicios **no tienen una cara prototípica** ni pertenecen automáticamente a gremio. La ropa puede reflejar el trabajo, no un «uniforme marinero» no autorizado.

El carácter tradicional y gremial define un **ambiente cultural**, no una genética ni personalidad común; Veldora puede tener residentes y visitantes de procedencias diferentes si su presencia individual está respaldada.

La aduana exterior corresponde a la **Corona**. Un funcionario de inspección no debe llevar insignia de una supuesta aduana entre Grandes Casas. Los seis ámbitos populares no son distritos oficiales.

D.P20: **VEL-N01–N10** son nombres, roles y biografías base editorialmente autorizados, pero **sin EntityId, domicilio, profesión ejecutada o edad física fijada** por esa ratificación.

## 10. Contextos específicos: Taramin

Ciudad de **14.000–20.000 habitantes**, pesquera, marítimo-fluvial, **pragmática, marinera y plural**, entre brazos terminales del mismo Thalen.

Los habitantes pueden dedicarse a pesca, conservación, comercio, reparaciones, cuidado y oficios de tierra según fuentes de individuo, no a una profesión universal. La exposición al viento, agua, sol y trabajo puede marcar ropa y piel **según la biografía real**, no por norma étnica.

No inferir dialectos, enfermedades, uniformes, tatuajes rituales, símbolos o estilos de pelo exclusivos sin canon. Los apodos de ámbitos TAR-U son **topónimos populares**, no castas ni asociaciones profesionales.

D.P21: **TAR-N01–N10** tienen aprobación de biografía base, sin personas materiales, familias, domicilios o edades numéricas instanciadas.

## 11. Contextos específicos: Syvaris y Arven

**Syvaris:** ciudad insular de **7.000–10.000 habitantes** junto a bahía resguardada, con clima relativamente cálido, centro/norte más seco, sur más verde. Carácter editorial de **convivencia de abrigo, prudencia práctica y orgullo del oficio**, no desconfianza automática.

Trabajos marítimos y domésticos pueden afectar ropa, exposición solar y materiales, pero la isla no crea un «tipo racial». La presencia naval es de la **Armada de Norgard**; jamás inventar una Armada Darovan ni conceder rango naval a alguien sin autoridad.

D.P22: **SYV-N01–N10** son biografías editoriales aprobadas, no identidades residentes ya insertadas en el juego.

**Arven:** pertenece a Darovan, con el Bosque del Manto Verde de coníferas continuo (~90 % de la isla), pero el perfil cultural específico permanece **UNKNOWN**. No presentar a sus habitantes como copia de Syvaris ni inventar vestuario insular, apellidos, lengua, costumbres, fisonomía o relatos de clan.

## 12. Mundo rural y profesiones

Las fuentes D06 y D.P24 contemplan agricultura, ganadería, servicios de camino, minería/metalurgia auxiliar, bosque y actividad insular **solo bajo condiciones de sitio**.

Las nueve comunidades **RUR-S01–S09 son candidatas editoriales, no aldeas ya materializadas**. Sus doce biografías rurales **RUR-N01–N12** (D.P24) son bases narrativas que requieren lugar, edad, hogar, oficio y contexto verificables antes de asignar un retrato final de NPC existente.

No dar por supuesto que toda aldea Darovan dispone de herrero, taberna, molino, comerciante, sanador o guarnición. Los oficios son compatibles con entornos reales y sujetos a disponibilidad de personas y servicios; una herramienta en el retrato no acredita empleo o titularidad.

## 13. Personajes de relevancia territorial D.P25

D.P25 preserva **52 perfiles base** (diez por cada una de las cuatro ciudades y doce rurales) y selecciona **27 hilos conductores** para desarrollo narrativo. Los 27 no constituyen otros 27 NPC diferentes ni un censo ejecutado.

- Conservar **ID de fuente** (p. ej., `TRH-N01`, `VEL-N01`, `TAR-N01`, `SYV-N01`, `RUR-N01`) al vincular retratos con biografías.
- Verificar cada nombre, oficio, conocimientos, vínculos y límites específicos de su expediente.
- No transformar 30 relaciones potenciales, cuatro modelos de hogar, diez conflictos o memorias privadas en hechos públicos.
- No fijar el nombre/aspecto del titular actual de Casa Darovan, herederos, jueces o comandantes sin autorización; esas identidades constan como pendientes.
- Evitar insignias, grados, claves o emblemas militares si la autoridad y la adscripción personal no están acreditadas.
- Un retrato editorial puede etiquetarse **REVIEW / CONCEPT**, pero **no APPROVED como retrato de entidad existente** hasta que se resuelvan apariencia y correspondencia individual.

La información biográfica privada no tiene por qué aparecer en `_info.md` público ni inferirse a partir de la expresión del personaje.

## 14. Nombres, familia y leyes de Norgard

El sistema de Norgard usa normalmente **nombre propio y un apellido**, con posible segundo nombre; no requiere doble apellido ni cambio automático por matrimonio.

**Aethros, Darovan, Edranor, Galdren y Valrik son apellidos protegidos**, no se asignan aleatoriamente. Darovan es una Gran Casa y un ámbito administrativo, **no el apellido de todos sus habitantes**. Compartir apellido, ciudad u oficio no acredita parentesco, matrimonio, confianza, amistad, criminalidad, propiedad ni rango.

No crear dialecto «darovano», insultos de grupo, etnias nuevas, marcas de nacimiento dinásticas, genealogías ni tatuajes colectivos sin texto de autoridad.

## 15. Integridad anatómica del individuo

El retrato debe superar un control de **anatomía humana individual**: rostro con ojos, orejas y dentadura plausibles, cuello y mandíbula coherentes, manos no duplicadas, dedos y objetos sin fusiones, hombros y brazos correctamente conectados, cabello sin fundirse en sombreros o prendas, accesorios que no atraviesan piel.

Si aparece un animal secundario, aplicar también la regla de la Biblia de Escenas Ambientales §9.1: no cabezas/cuello duplicados ni cuerpos compartidos.

Examinar la imagen ampliada y **rechazar el candidato defectuoso**; no normalizar errores de generación como rasgos peculiares del mundo.

## 16. Diversidad y registro antes de producir

El protocolo `Worldbuilding/Direccion artistica/Assets/PORTRAIT_WORKFLOW_RULES.md` es **ACTIVE/OBLIGATORIO**. Antes de cada retrato consultar biblias y `PORTRAIT_REGISTRY.json`, y formar un **pool comparable**:

1. misma localidad + mismo oficio + mismo sexo;
2. misma localidad + grupo de oficios + mismo sexo;
3. misma cultura/región + oficio + mismo sexo;
4. diversidad total del entorno.

Resolver edad, edad aparente, cuerpo, cara, cabello, pérdida de pelo, canas, vello facial, expresión, pátina, presentación y diferencias frente al pool **antes** de redactar el prompt. Si parece la misma persona con otra ropa o peinado, **rechazar**.

Los 39 retratos históricos aprobados de Treskal **no son retratos Darovan**; sirven a lo sumo como control general de estilo, nunca como población transplantada.

Registrar solo después de aprobación artística, sin declarar sincronizado un asset que NAP todavía no ha procesado.

## 17. Ficha visual individual requerida

Para cada retrato:

- `asset_id` técnico y `character_source_id` si corresponde a biografía editorial.
- Reino/cultura, territorio y **localidad autorizada**.
- Tipo de sujeto: `generic_procedural`, `editorial_named_concept` o `instantiated_character` según la realidad.
- Sexo, etapa de edad, edad aparente, complexión y rasgos físicos **resueltos sin convertirse automáticamente en canon**.
- Oficio, nivel de presentación 1–5, pátina A–D, vestimenta, postura, fondo y fuentes de iluminación.
- Elementos distintivos permitidos; insignias y autoridad verificadas.
- Comparación anti-clonación con el pool.
- Referencias documentales/versión; qué es `AUTHORED`, `PROVISIONAL` y `UNKNOWN`.
- Resultado de auditoría de manos, cuello, ojos, orejas, prendas y accesorios.
- Identidad de asset, aprobación artística, estado NAP y ruta de catálogo **por separado**.

`_visual_identity.json` describe rasgos **visibles en el PNG**, no atributos ocultos, nombres aleatorios o intenciones incumplidas del prompt.

## 18. Compatibilidad con NAP 2.0

Esta biblia no altera contratos técnicos. NAP vigente para Nimroel:

| Campo | Contrato |
| --- | --- |
| `asset_type` | `portrait` |
| `production_profile` | `portrait_npc` |
| Maestro | PNG estático vertical **4:5 exacto** |
| Derivado NAP | WebP **768×960**, calidad **90** |
| Clasificación requerida | `culture`, `location`, `role`, `sex` |
| Otras dimensiones admitidas | `realm`, `region` |
| ZIP de entrada | Cinco archivos planos con mismo asset_id |

Archivos: `<id>.png`, `<id>_manifest.json` (v2), `<id>_prompt.md`, `<id>_info.md` y `<id>_visual_identity.json`. Sin WebP dentro del ZIP ni recorte/padding silencioso.

La localización `location` y el rol `role` serán identificadores normalizados, no sustitutos de pruebas de persona y emplazamiento real. Verificar siempre `robdor80/NAP/config/universes/nimroel/profile.json` y nombres del catálogo actual antes de reservar un `asset_id`.

**Validación técnica NAP ≠ aprobación visual ≠ NPC instanciado en CoreRPG.**

## 19. Plantilla operativa de prompt

1. Identidad/documento de sujeto (fuente, autoridad, estado editorial o de instancia).
2. Contexto Darovan correcto: Treihord/Veldora/Taramin/Syvaris/rural/Arven UNKNOWN.
3. Descripción individual distinta del pool; edad, complexión, rasgos y cabello.
4. Ropa, materiales, pátina y presentación coherentes con situación, estación y ocupación real.
5. Encuadre 4:5 busto, mirada y expresión natural, luz físicamente justificada.
6. Fondo contextual tenue, sin arquitectura, símbolos, relatos ni lugares inventados.
7. Negativos: sin glamour, clonación, poses heroicas, insignias no acreditadas, deformaciones anatómicas.
8. Notas `PROVISIONAL` de apariencia y fuente, separadas del prompt y del canon.

## 20. Checklist de aceptación

- [ ] Biblias generales NPC/Norgard y expediente Darovan consultados.
- [ ] Localidad e identidad correctamente clasificadas sin NPC inventados.
- [ ] Para nombres de D.P20–25, biografía y límites resueltos; no se inventan edades, genealogías ni cargos.
- [ ] Persona no recibe personalidad, moralidad, clase, riqueza o genética por su territorio.
- [ ] Diversidad comprobada contra `PORTRAIT_REGISTRY.json`; sin clones.
- [ ] Anatomía facial y manos/ropa sin duplicaciones ni fusiones.
- [ ] Contexto profesional/material/temporal coherente con la persona.
- [ ] Pátina A–D y presentación 1–5 distintas y justificadas.
- [ ] Sin símbolos o títulos no autorizados, apellidos protegidos aleatorios ni estereotipos.
- [ ] Fondo no convierte localidad futura en realidad cartografiada ni revela información privada.
- [ ] PNG 4:5, metadata fiel y ZIP/manifest NAP vigentes.
- [ ] Revisión humana separada de validación NAP antes de APPROVED.

## 21. Fuentes y reservas

**Biblias y workflow**:

- `Worldbuilding/Direccion artistica/Biblia visual/General/NIMROEL_GLOBAL_VISUAL_BIBLE_v0.5.md`.
- `Worldbuilding/Direccion artistica/Biblia visual/Categorias/NPC/NPC_PORTRAIT_VISUAL_BIBLE_v0.3.md`.
- `Worldbuilding/Direccion artistica/Biblia visual/Culturas/Norgard/NORGARD_VISUAL_PROFILE_v0.1.md` y `Datos operativos/norgard_visual_profile_v0.5.json`.
- `Worldbuilding/Direccion artistica/Assets/PORTRAIT_WORKFLOW_RULES.md`.
- `Worldbuilding/Direccion artistica/Assets/PORTRAIT_REGISTRY.json`.

**Darovan** (relativo a `Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan/`):

- `Cultura_y_sociedad/D10_IDENTIDAD_SOCIAL_v0.1.md`, `D10_PERFILES_LOCALES_v0.1.md`, `D10_RELACIONES_Y_NPC_v0.1.md`.
- `Profundizacion_2026/D.P20/08_decisiones_autorales.md`; `D.P21/08_decisiones_autorales.md`; `D.P22/08_syvaris_decisiones_editoriales.md`; `D.P23/08_resoluciones_editoriales.md`.
- `Profundizacion_2026/D.P24/08_decisiones_editoriales_delegadas.md`.
- `Profundizacion_2026/D.P25/01_reparto_y_relevancia_territorial.md`; `D.P25/07_decisiones_editoriales.md`.
- `Profundizacion_2026/D.P26/03_deuda_real_y_traspaso.md`.

Las bases biográficas aprobadas de D.P20–D.P25 **no fijan automáticamente físico, edad, sexo, vivienda, familiares, rango ni existencia en WorldState**; todos esos extremos requieren comprobación individual. La identidad cultural de **Arven** permanece sin definición local propia.

---

**Regla final:** el retrato Darovan debe hacer visible **a una persona única en un contexto auténtico**, no convertir una procedencia territorial en una cara, destino, virtud o delito.
