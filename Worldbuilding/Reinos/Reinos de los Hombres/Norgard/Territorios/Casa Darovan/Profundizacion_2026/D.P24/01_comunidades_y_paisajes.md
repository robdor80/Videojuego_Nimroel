# D.P24/01 — Nueve comunidades objetivo y la geografía que permite vivir

## Regla de implantación
La fase da **identidad editorial** a nueve comunidades **candidatas**, no crea nueve aldeas canónicas. Su nombre es útil para escribir ficción y distinguir acentos locales, pero no identifica parcela, desembarcadero, pueblo existente ni una población contada. Las doce unidades `d01_*` son contextos cualitativos, no polígonos ni fronteras. Antes de incorporar un núcleo a un mapa deben acreditarse, para un sitio singular, terreno, agua potable, acceso, sustento, jurisdicción, comunidad residente y compatibilidad ambiental. Si cualquiera falla, podrá cambiarse el emplazamiento, transformarse la idea en presencia temporal o descartarse sin retcon.

| Clave | Nombre editorial seleccionado | Contexto de referencia | Modelo D06 dominante *condicional* | Pregunta que la hace singular |
|---|---|---|---|---|
| RUR-S01 | **Los Hojales** | `d01_belara_treihord` | `agricola` | ¿Se vende el alimento disponible o se guarda para la familia? |
| RUR-S02 | **Casas del Resguardo** | `d01_norte_transicion` | `ganadera` | ¿De quién es el forraje cuando el frío se adelanta? |
| RUR-S03 | **Piedra de Sal** | `d01_taramin_norte_centro` | `pesquera` como actividad sólo si se acredita acceso pesquero; si no, núcleo de sustento mixto a reconsiderar | ¿Por qué se abandona una promesa de provisiones? |
| RUR-S04 | **La Cuesta de la Pesa** | `d01_valkram_oeste` | `minera_auxiliar` | ¿Quién paga una jornada suspendida por un acceso inseguro? |
| RUR-S05 | **Patio de las Tenazas** | `d01_belara_treihord` | `metalurgica_auxiliar` | ¿Cómo se repara una herramienta si faltan combustible y piezas? |
| RUR-S06 | **El Claro Guardado** | `d01_pilares_sur` | `forestal_sostenible` | ¿Talar hoy o permitir que el lugar se recupere? |
| RUR-S07 | **La Última Sombra** | `d01_linde_caminos` | `servicio_camino` | ¿Se atiende a quien llega sin recursos ni aval? |
| RUR-S08 | **Orilla del Manto** | `d01_arven_contexto` | `insular_mixta` | ¿Cuánto puede extraerse de un bosque que se quiere conservar? |
| RUR-S09 | **Las Piedras Quietas** | `d01_elyra_paso_peninsular` | `enclave_especializado` | ¿Es lugar habitado o apenas un servicio de temporada? |

**RUR-S03 no constituye una nueva aldea pesquera en colinas secas**: el modelo de pesca se suspende hasta verificar acceso real y se puede reubicar a un lugar habilitado de la península de Taramin. Tampoco S09 declara paso, ruta, albergue o población permanente. El inventario JSON expone estas condiciones de manera explícita.

## Paisajes que no se domestican

**Belara / Treihord (S01, S05).** Hay huertas perimetrales y dependencia alimentaria, pero ninguna parcela, molino ni fuente rural concreta se añade ahora. S01 contrasta reserva y venta; S05, la dependencia del artesanado auxiliar respecto a los metales y carburantes realmente disponibles. El Crisol sigue siendo único: S05 no ensaya metales preciosos ni acuña.

**Frío del norte (S02).** El ganado solo existirá con cabezas reales, pastos, tenencia y abrigo; la dificultad puede ser obtener comida antes que encontrar un comprador. Se evita convertir la transición climática en invierno permanente.

**Taramin (S03).** La piedra, el suelo difícil y la variabilidad del agua son el conflicto rector. Ni el Thalen ni la costa autorizan por sí solos acequias, puertos, puentes o barcos. El Bosque de Taramin meridional continúa intacto y sin tala industrial; sus formas de vida se representan en escenas, sin necesitar una décima aldea ficticia.

**Valkram (S04).** Solo se vincula a una explotación identificada cuando se demuestre titularidad y acceso; la riqueza de la cordillera no permite abrir otra mina ni crear carbón local: el carbón procede de Azurios.

**Pilares (S06).** El Bosque de los Pilares es uno solo. La madera destinada a minería no elimina condiciones de extracción sostenible, cuotas, custodia, útiles ni renovación. «Claro» es aquí **nombre editorial**, no apertura geográfica confirmada.

**Linde (S07).** Se conoce un enlace viario cualitativo Veldora–Treihord; no su trazado ni el punto de parada. S07 nunca es una posada ya existente ni presume tránsito a pie o carro desde cualquier lugar.

**Arven (S08).** La isla sí pertenece a Darovan y existen aldeas sin nombre establecido, sobre todo en su litoral interior frente al Golfo de Veldora. El Manto Verde conserva aproximadamente un 90 % de cobertura continua y aprovechamiento limitado. No se supone un ferry, puerto, caza libre o ruta a Syvaris.

**Elyra (S09).** Un servicio de paso estacional no acredita población, un paso operativo ni extracción de minerales. Su identidad literaria gira en torno a qué se puede prometer cuando nadie puede garantizar el trayecto.

## Tres niveles de pertenencia
- **Residente**: duerme habitualmente allí, participa del sustento común y tiene relación comprobada con el sitio.
- **Temporero**: trabaja o pernocta durante un periodo, sin sumar automáticamente a hogares residentes ni al censo.
- **Visitante**: pasa si hay acceso acreditado; ni su llegada ni su conversación crean camino.

Un núcleo nunca adquiere el rótulo de «pueblo» por mera abundancia comercial, y un campamento sin hogares no se convierte en aldea. La escala de cada nombre es `UNKNOWN` hasta sus pruebas de sitio.
