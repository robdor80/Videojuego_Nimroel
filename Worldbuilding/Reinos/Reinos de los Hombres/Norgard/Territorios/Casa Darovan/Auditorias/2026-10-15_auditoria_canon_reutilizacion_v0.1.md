# Auditoría de arranque — Darovan 1 (15-10-2026)
**Estado:** AUDITORÍA INICIAL VERIFICADA CONTRA `main`, no cierre definitivo de todo el canon. **No es documento canónico nuevo.**

## Hallazgos del repositorio
- En `main` hay una única ficha urbana directa bajo `Norgard/Ciudades/Casa Darovan/Treihord.md` (diseño base cerrado), y activos/prompts heráldicos Darovan.
- Antes de este incremento no existía carpeta `Norgard/Territorios/Casa Darovan`.
- `Casa Valrik` dispone de `Aldeas`, `Pueblos`, `Villas`, `Clima_local`, `Geografia_local`, `Seguridad_y_defensa`, `Treskal` y documentación raíz. Su árbol territorial en la auditoría de `main` contenía **437 archivos** (recuento de ese momento; no es contrato).
- `Nimroel Core` registra extracción genérica validada estáticamente y extensiones para geografía física/drenaje, simulación de embarcaciones, pesca, transacciones y causas legales.
- `Norgard Defaults`: E1–E17 activos y validados **estáticamente**; no equivale a prueba runtime de un videojuego.

## Canon confirmado, con autoridad original
| Materia | Hecho confirmado | Fuente |
|---|---|---|
| Administración | Darovan gobierna el occidente; capital Treihord; Veldora puerto comercial; Taramin puerto pesquero; isla de Syvaris bajo Darovan | `Norgard/Grandes Casas/grandes_casas.md` |
| Política | Casa rica en oro, plata y comercio; rivalidad económica con Galdren; influencia política, no se establece rebelión | `Grandes Casas/grandes_casas.md` |
| Treihord | ~32.000 habitantes; diseño urbano base cerrado; ocho barrios, cuatro grandes plazas | `Ciudades/Casa Darovan/Treihord.md` |
| Industria Treihord | Montes Valkram, río Belara, barcazas de poco calado, puerto industrial; carbón importado de Azurios; El Crisol no acuña moneda | `Ciudades/Casa Darovan/Treihord.md`; `Geografía/rios_y_lagos.md` |
| Poder Casa | La Bóveda del Grifo y la conexión de custodia «La Vena» | `Ciudades/Casa Darovan/Treihord.md` |
| Ríos occidentales | Belara desemboca en Golfo de Norgard; Lhera se separa del Belara y desemboca en Golfo de Veldora; Veldora es un río independiente; Thalen se bifurca en torno a Taramin | `Geografía/rios_y_lagos.md` |
| Relieve | Montes Valkram, oro y plata; Montañas Elyra prolongadas por península | `Geografía/montanas.md` |
| Forestal | Agujas, Linde (ruta Veldora–Treihord), Pilares (madera de mina), Taramin, bosques dispersos de Syvaris; isla de Arven con Bosque del Manto Verde | `Geografía/bosques.md` |
| Mar e islas | Golfos de Veldora y Norgard; Arven frente a Veldora; Syvaris con bahía principal y calas | `Geografía/mares_y_costas.md` |
| Clima | Península Taramin semiárida de transición; Syvaris cálida de rasgos semitropicales y zonas secas sin ser desierto; norte frío | `Geografía/regiones_naturales.md`; `Clima/clima_general.md` |
| Ámbito ajeno | Karsath figura en **región central** en `norgard_regions_v0.1.json`, no incorporarla a Darovan por aparecer en la imagen | `Direccion artistica/Biblia visual/Culturas/Norgard/Datos operativos/norgard_regions_v0.1.json` |

## Comparación estructural y decisión de reutilización
| Bloque de Valrik/Treskal | Darovan | Tratamiento |
|---|---|---|
| Procedimiento esqueleto → posibilidades → probabilidades → instancias | Sí | Reutilizar metodología, sin copiar números ni particularidades Valrik |
| Núcleo Core de memoria/NPC, familias, empleo, inventario, transacciones, accidentes | Sí | Referenciar Core por IDs y contratos; no clonar documentos |
| Norgard Defaults E1–E17: ley, fiscalidad, nombres, milicia, armada, moneda y mar | Sí | Heredar sin reimplementar ni excepciones inventadas |
| Microcuencas/drenaje, medio físico y estado temporal | Sí | Reutilizar contrato Core, cambiar **fuentes geográficas locales** |
| Generación de aldeas/pueblos/villas | Sí, con rediseño | Ajustar solo tras estudiar zonas mineras, puertos, península, isla, frío y abastecimiento |
| Seguridad territorial Valrik | Parcial | Marco común Norgard; guardia Darovan y ubicaciones requieren perfil propio |
| Plano/identidad de ciudad única Treskal | Metodología solamente | Treihord, Veldora, Taramin y Syvaris son lugares deliberados, no instancias aleatorias |
| Madera/artesanía/astilleros propios de Treskal | No | No trasladar especialización local a Darovan |
| Rangos de población de asentamientos Valrik | No | Sus archivos prohíben explícitamente extrapolarlos a Norgard |

## Contradicciones / incertidumbres (no resolver sin autor)
1. **Topónimo fluvial manuscrito vs canon:** el PDF de trabajo `TODO NIMROEL 10.09.26.pdf` (pasaje del capítulo 27, página impresa 1059) dice «Treihord ... sobre el Eshneva». El canon geográfico y urbano de GitHub sitúa junto a Treihord al **Belara** (que no atraviesa el casco urbano). **No cambiar ningún documento**: aclarar si la versión narrativa es histórica, provisional o requiere corrección editorial. No se incorpora «Eshneva» a contratos.
2. **Arven:** ubicación en ámbito occidental de Norgard confirmada; falta documento explícito hallado que la asigne administrativamente a Darovan. Se analiza por proximidad, con adscripción `pendiente_verificacion`.
3. **Fronteras y geometría:** la línea roja es una marca de recorte/área de estudio proporcionada por el autor; no se georreferencia como frontera política.
4. **Treihord, militar:** el documento urbano aún conserva lenguaje histórico de «revisión militar»; Norgard E5 ya aparece activo. Requiere una futura auditoría de compatibilidad, **sin reabrir** el canon base.
5. **Faltan cierres de autor:** señor actual de Casa, herederos, origen histórico, casas menores, origen de rivalidad y organización particular guardia; `grandes_casas.md` marca varios explícitamente pendientes.
6. **Escalas:** no existen aquí medidas cartográficas suficientes para fijar kilómetros, cotas, tiempos de viaje o caudales. Ninguno se inventa.
7. **Ciudades Veldora/Taramin/Syvaris:** constan perfiles visuales regionales en JSON, pero no equivalen a biblia urbana detallada ni a trazado de calles.

## Revisión de compatibilidad por hacer antes de declararlo «auditado completamente»
- Inventario cruzado de TODAS las referencias a Darovan/Treihord en canon urbano, gobierno, economía, heráldica, barcos y archivos operativos.
- Matriz de contratos Core/Defaults: versión, campo, autoridad, override y prueba estática por subsistema.
- Comparación de la ficha completa de Treihord con el canon narrativo y referencias visuales, especialmente textos históricos/cronológicos.
- Auditoría de los perfiles regionales con sus manifiestos visuales vigentes para no confundir v0.1 con revisión más reciente.

**Regla:** lo no contradicho por esta auditoría no se convierte automáticamente en canon. No crear nuevas ciudades importantes ni resolver las dudas señaladas.
