# E13 — Altimetría propuesta y reglas de microrelieve
**Decisión de diseño delegada, 13-11-2026.** Las bandas siguientes son **referencias conceptuales** elegidas por ChatGPT bajo delegación general del autor; NO son cotas medidas, topografía canónica, polígonos o altitud legal de localidades. El JSON E01 antiguo conserva UNKNOWN y no se modifica.

## Bandas de referencia para prototipado, en metros sobre nivel de mar ficticio
| Unidad E01 | Banda ilustrativa del paisaje de interés | Precisión / reserva |
|---|---:|---|
| Interfaz Valkram, piedemonte y flancos de estudio | 600–1600 | NO incluye las grandes cumbres del macizo, ni asigna vertientes al señorío |
| Lomas oeste interior Karsath | 300–650 | No es la cota municipal de Karsath |
| Meseta y borde forestal de Lumina/Bosque Alto | 650–1100 | No demuestra perímetro o altura del bosque completo |
| Centro vinícola de rellanos y lomas | 200–650 | Zona mixta, no plano horizontal ni viñedo continuo |
| Borde forestal Dorth/Azurios | 350–1500 | Piedemonte de estudio; NO incluye cotas de toda la cordillera |
| Transición fría norte | 350–1150 | Latitud y altitud no son equivalentes; no hay observación local |
| Extremo norte sin cierre | NO APLICABLE | No asignar cota a territorio cuya pertenencia se desconoce |

Las franjas pueden solaparse: describen **tipos de paisaje**, no alturas obligatorias ni niveles discretos. Cualquier forma generada habrá de conectar geométricamente con su vecino, sin acantilados artificiales ni cauces cuesta arriba.

## Bandas de emplazamiento recomendadas, estrictamente de diseño
- **Dorth:** 300–650 m, núcleo principal sobre un rellano de transición al piedemonte oriental. No se afirma que el dibujo actual tenga esta cota.
- **Lumina:** 650–900 m, asentamiento en relación con meseta y borde de Bosque Alto; se favorece un emplazamiento legible sin murallas.
- **Karsath:** 300–550 m, lomas interiores relacionadas visualmente con el contexto lacustre; jamás declarar la orilla propia de Antela.
- **Rodas:** 400–950 m como intervalo de investigación visual; el frío deriva prioritariamente del contexto septentrional y la exposición, NO de imponerle una cumbre. La Corona conserva todo mando.

Estas cuatro bandas NO crean puntos de elevación ni cambian el canon. Si E19 encuentra contradicción, se corrigen **estas referencias**, no el mapa canónico.

## Relación con decisiones anteriores en Valkram
La Viuda de ~4200 m al norte de Valkram, máximo de Norgard, y los neveros que persisten en verano constan como decisiones expresas de Darovan D.P13; las grandes cumbres Valkram tienen referencia 3600–4200 m y pasos principales 1400–2200 m. Las franjas E13 describen porciones inferiores y de contacto de Edranor **sin adscribir la Viuda, un paso concreto o un valle de Darovan a esta Casa**. Azurios mantiene predominio regional de altura y abruptidad, con la excepción máxima puntual previamente autorizada.

## Clasificador geomorfológico posterior, no instanciado
Para cada celda del futuro modelo se evaluarán: elevación relativa, pendiente local, curvatura, acumulación de flujo, relieve de vecindad, profundidad potencial del suelo y cobertura. Clases candidatas: cresta, ladera convexa, media ladera, concavidad, collado, terraza natural, fondo de valle, pie de monte y rellano. Las clases nacen de la topografía validada, no del azar aislado. Todo accidente materializado obtiene ID persistente y fuente.

## Puertas necesarias
- E19: mapa íntegro, cierres y puntos de control antes de situar elevaciones.
- E19: DEM/heightfield 2D coherente, cotas autorizadas como restricciones, ríos con declive aguas abajo.
- E19/E28: comprobar que centros urbanos y vías propuestos respetan pendiente, cuencas y transitabilidad.
- E29: compare con Darovan y Valrik, sin volver estas cifras «mediciones» retrospectivamente.

**Prohibiciones:** ninguna línea de nivel o valor en metros se extrae del grosor de la frontera roja o de la barra «400 millas» del mapa general; no se asignan porcentajes de superficie a una banda.
