# NIMROEL — PORTRAIT WORKFLOW RULES

**Estado:** ACTIVE / OBLIGATORIO  
**Versión:** 1.0  
**Fecha:** 2026-09-25  
**Ámbito:** generación, aprobación y almacenamiento de retratos visuales de Nimroel.

---

## 1. Regla maestra

**No se debe generar ningún retrato nuevo sin consultar antes las biblias visuales aplicables y el registro de diversidad de retratos.**

La consulta del registro no sustituye al canon. El registro sirve para decidir la **variación individual** dentro de las posibilidades permitidas por las biblias.

---

## 2. Fuentes obligatorias antes de generar

Como mínimo deben revisarse, según proceda:

1. Biblia Visual General vigente.
2. Biblia Visual de Retratos NPC vigente.
3. Perfil cultural vigente.
4. Perfil regional / local vigente cuando exista.
5. Perfil de raza, profesión, clase o facción cuando exista y sea relevante.
6. Datos operativos asociados vigentes.
7. `PORTRAIT_REGISTRY.json`.

Para Norgard, a fecha de creación de este workflow, las referencias vigentes consultadas son:

- `Worldbuilding/Direccion artistica/Biblia visual/General/NIMROEL_GLOBAL_VISUAL_BIBLE_v0.5.md`
- `Worldbuilding/Direccion artistica/Biblia visual/Categorias/NPC/NPC_PORTRAIT_VISUAL_BIBLE_v0.3.md`
- `Worldbuilding/Direccion artistica/Biblia visual/Culturas/Norgard/NORGARD_VISUAL_PROFILE_v0.1.md`
- `Worldbuilding/Direccion artistica/Biblia visual/Culturas/Norgard/Datos operativos/norgard_visual_profile_v0.4.json`

Para cualquier retrato de un habitante de la **zona de Treskal** es además obligatoria la consulta de:

- `Worldbuilding/Direccion artistica/Biblia visual/Culturas/Norgard/Perfiles locales/Treskal/TRESKAL_PORTRAIT_VISUAL_BIBLE_v0.1.md`

Esta Biblia local tiene prioridad para resolver la identidad visual específica de la zona de Treskal dentro del marco superior de la Biblia Global, la Biblia NPC y el perfil cultural de Norgard.

Si existen versiones posteriores aprobadas, deben prevalecer las vigentes más recientes.

---

## 3. Construcción del pool comparable

Antes de resolver la apariencia se debe consultar el registro y formar un pool comparable.

Prioridad de comparación:

1. misma localización + misma profesión + mismo sexo;
2. si el pool es pequeño, misma localización + grupo profesional + mismo sexo;
3. si sigue siendo insuficiente, misma cultura / región + profesión + mismo sexo;
4. como control general adicional, población completa de la localización.

El propósito no es obtener una cuota matemática rígida, sino detectar repeticiones y huecos evidentes.

---

## 4. Ejes mínimos de diversidad

Antes del prompt final se deben resolver deliberadamente, cuando sean aplicables:

- rango de edad;
- edad aparente;
- complexión;
- forma general del rostro;
- anchura facial;
- mandíbula;
- pómulos;
- nariz;
- ojos;
- cejas;
- labios;
- frente;
- asimetrías naturales;
- color de cabello;
- textura del cabello;
- longitud;
- grado de pérdida de cabello / entradas / calvicie;
- presencia y tipo de canas;
- vello facial;
- estado de piel;
- exposición al clima / trabajo;
- rasgos distintivos moderados;
- expresión base;
- presentación contextual;
- pátina de la indumentaria.

No todos los campos necesitan ser extraordinarios. La diversidad debe sentirse humana y natural.

---

## 5. Regla de cobertura antes de repetición

Las características pueden repetirse.

Sin embargo, si un pool ya contiene varias personas con una combinación muy similar, se debe preferir una variante menos representada siempre que:

- sea compatible con el canon;
- sea compatible con la profesión;
- sea compatible con la edad;
- no contradiga cultura, región, clase o contexto.

Ejemplo de repetición a evitar por inercia:

`male + adult 30–40 + robust + dark_brown_hair + full_short_beard + broad_face`

Si esa combinación ya domina el pool, el siguiente asset debería explorar otra combinación plausible: joven, maduro mayor, anciano, delgado, heavy, afeitado, bigote, calvicie parcial, canas, rostro estrecho, etc.

---

## 6. Regla anti-clonación

Debe rechazarse un retrato candidato si parece:

- la misma persona con distinta ropa;
- la misma cara con distinto cabello;
- un duplicado facial;
- una variante casi idéntica de un retrato ya aprobado.

La comprobación se realiza contra el pool comparable y, si es necesario, contra retratos próximos de la misma localización.

La diversidad facial es un requisito de calidad.

---

## 7. Edad

Rangos base heredados de la Biblia NPC:

- `child`
- `young`
- `adult`
- `elderly`

Además del rango se registrará una **edad aparente aproximada** para poder detectar concentración excesiva en una franja.

La profesión debe ser compatible con la edad. Un aprendiz adolescente puede existir donde sea plausible; un niño no debe recibir una profesión adulta incompatible.

El envejecimiento debe afectar realmente a proporciones, piel, volumen facial, cabello, postura y textura. Un anciano no es un adulto joven con pelo gris.

---

## 8. Cabello y vello facial

No usar barba como marcador automático de ambiente medieval.

El registro debe distinguir al menos:

- color;
- longitud;
- textura;
- pérdida de cabello;
- canas;
- tipo de vello facial.

Estados posibles de pérdida de cabello, cuando sean útiles:

- `none`
- `receding`
- `thinning`
- `tonsure_like_crown_loss`
- `advanced_balding`
- `bald`

No son cuotas ni una lista cerrada.

---

## 9. Complexión

Etiquetas recomendadas heredadas de la Biblia NPC:

- `very_thin`
- `thin`
- `average`
- `robust`
- `heavy`
- `muscular`
- `frail`

No asociar automáticamente profesión con una sola complexión.

---

## 10. Ficha de variación resuelta

Antes de redactar el prompt final debe existir internamente una ficha de variación resuelta con, como mínimo:

- localización;
- profesión;
- sexo;
- rango de edad;
- edad aparente;
- complexión;
- morfología facial principal;
- cabello;
- pérdida de cabello / canas;
- vello facial;
- rasgos distintivos;
- presentación contextual;
- pátina;
- diferencias buscadas respecto al pool existente.

La apariencia individual se decide **antes** del prompt, no se deja completamente a la solución por defecto del generador.

---

## 11. Presentación y pátina

Se mantienen las dos capas obligatorias definidas por las biblias:

### Presentación contextual 1–5

- 1 — exposición intensa / trabajo especialmente sucio / campaña;
- 2 — jornada de trabajo o viaje;
- 3 — uso cotidiano aseado;
- 4 — muy cuidado / alto nivel de presentación;
- 5 — presentación ceremonial / excepcionalmente cuidada.

### Pátina de ropa A–D

- A — excepcional / casi nueva;
- B — bien mantenida;
- C — uso cotidiano normal;
- D — muy trabajada.

Ambas capas son independientes.

---

## 12. Convención de nombre

La convención oficial y prevalente de nombres y empaquetado está definida en `nimroel_asset_naming_convention.md`.

Cada asset tendrá un `asset_id` único que será también su nombre base.

Ejemplo:

`portrait_treskal_farmer_male_001`

El ZIP de transferencia y los archivos internos deben compartir exactamente el mismo nombre base.

En GitHub, el asset se almacena descomprimido en una carpeta con ese mismo nombre base:

```text
portrait_treskal_farmer_male_001/
├── portrait_treskal_farmer_male_001.png
├── portrait_treskal_farmer_male_001_prompt.md
└── portrait_treskal_farmer_male_001_info.md
```

El ZIP es un contenedor de entrega local y no forma parte del almacenamiento definitivo del repositorio.

---

## 13. Momento de registro

Un retrato solo entra en `PORTRAIT_REGISTRY.json` y `PORTRAIT_REGISTRY.md` cuando haya sido aprobado.

Los borradores o imágenes descartadas no cuentan para el equilibrio poblacional permanente.

Al aprobar:

1. asignar nombre final;
2. guardar PNG;
3. crear ZIP;
4. registrar características físicas reales del resultado aprobado;
5. registrar presentación y pátina;
6. actualizar la vista MD;
7. actualizar `VISUAL_ASSET_REGISTRY.md`.

No registrar únicamente lo solicitado en el prompt: registrar lo que realmente aparece en el asset final aprobado.

---

## 14. Regla de fidelidad del registro

El registro debe describir el asset final, no inventar características que no sean visibles o razonablemente inferibles.

Si un atributo no puede determinarse con suficiente seguridad se usará `unknown`, `not_visible` o `not_applicable` según corresponda.

---

## 15. Resultado buscado

Una campaña correcta debe producir:

**personas distintas, del mismo mundo, de la misma cultura y bajo una dirección artística coherente.**

Debe fallar la aprobación colectiva si los retratos:

- parecen clones;
- repiten continuamente la misma franja de edad;
- repiten sistemáticamente barba, peinado o complexión;
- parecen personajes de universos distintos;
- pierden la identidad cultural para ganar variedad.


---

## 16. Registro inmediato y binario diferido

Durante una sesión de creación de assets puede utilizarse el siguiente flujo operativo:

1. generar el retrato;
2. aprobarlo;
3. asignar el nombre base canónico;
4. crear el PNG y el ZIP local con su documentación;
5. entregar el ZIP al usuario;
6. **actualizar inmediatamente** `PORTRAIT_REGISTRY.json`, `PORTRAIT_REGISTRY.md` y `VISUAL_ASSET_REGISTRY.md`;
7. marcar el asset como `local_pending_gitsync`;
8. continuar generando nuevos assets consultando ya esa entrada;
9. el usuario descomprime el ZIP en local, conserva la carpeta del asset, elimina el ZIP y sincroniza la carpeta mediante GitSync;
10. cuando se confirme en GitHub la carpeta con PNG + `_prompt.md` + `_info.md`, el estado pasa a `synced`.

La memoria de diversidad **no debe esperar al GitSync final**. Un retrato aprobado cuenta para la diversidad desde el momento en que su ZIP local ha sido creado y entregado.


---

## 17. Fondo contextual por oficio y localización

Por defecto, todo retrato NPC asociado a un oficio debe utilizar un fondo discreto y desenfocado que refuerce ese oficio sin convertir el retrato en una escena narrativa.

Ejemplos:

- campesino / campesina → campo, cultivos, viñedos, cercados, útiles agrícolas o paisaje rural;
- carpintero / carpintera → taller de carpintería, madera, banco o herramientas;
- herrero / herrera → herrería, fragua, yunque, metal y entorno de taller;
- panadero / panadera → horno, mesa de amasado, harina, pan o interior de panadería.

Cuando exista una localización concreta, el fondo debe resolver **oficio + localización** simultáneamente. Por ejemplo, una campesina de Treskal debe mostrar un entorno agrícola compatible con Treskal.

Para la zona de Treskal, el fondo deberá respetar específicamente `TRESKAL_PORTRAIT_VISUAL_BIBLE_v0.1.md`: fondo contextual suave y secundario, adecuado al oficio y al entorno concreto (campo, bosque, taller, cocina, mercado, muelle, calle, establo, vivienda u otro entorno productivo cuando corresponda). No se deben introducir automáticamente elementos regionales no establecidos por la Biblia local.

El fondo debe permanecer secundario y normalmente desenfocado. Un fondo neutro o de estudio solo se utilizará como excepción justificada, no como valor por defecto.


---

## 18. Reconciliación del estado de sincronización

El estado de un asset en el registro debe reflejar la realidad actual del repositorio.

Cuando se vaya a actualizar cualquiera de los registros de assets o diversidad durante una sesión posterior, se debe comprobar si las carpetas de los assets marcados como `local_pending_gitsync` ya existen realmente en su ruta prevista dentro de `Assets/`.

Si la carpeta ya está presente en el repositorio:

1. verificar que el nombre y la ruta coinciden con el asset registrado;
2. verificar que contiene el PNG, `_prompt.md` y `_info.md` correctos;
3. cambiar `binary_sync_status` de `local_pending_gitsync` a `synced`;
4. actualizar las vistas Markdown relacionadas para eliminar cualquier texto que siga diciendo que el ZIP está pendiente;
5. mantener coherentes todos los registros entre sí.

No se debe dejar un asset marcado como pendiente si su carpeta definitiva ya está presente y validada en el repositorio.

---

## 19. Revisión obligatoria del ZIP antes de entrega

Antes de entregar al usuario cualquier ZIP de asset visual aprobado, se debe realizar una revisión final obligatoria del paquete.

La revisión debe comprobar, como mínimo:

1. que el nombre base corresponde exactamente al asset actual;
2. que el PNG incluido es la imagen aprobada correcta;
3. que el `_prompt.md` corresponde a esa imagen y no a otro asset;
4. que el `_info.md` corresponde a esa imagen y no contiene datos heredados por error de otro retrato;
5. que sexo, profesión, localización, edad aparente, rango de edad y rasgos físicos coinciden con la imagen aprobada;
6. que presentación, pátina, ropa, fondo y contexto profesional coinciden con lo realmente visible;
7. que no hay referencias cruzadas incorrectas a otro asset;
8. que PNG, ZIP, `_prompt.md` y `_info.md` comparten exactamente el mismo nombre base según la convención vigente;
9. que la numeración de variante es correcta;
10. que el contenido interno del ZIP está completo y sin archivos sobrantes.

Esta revisión es especialmente obligatoria en sesiones largas con múltiples assets consecutivos, donde aumenta el riesgo de arrastrar datos de una imagen anterior.

El ZIP solo debe entregarse después de superar esta comprobación.
