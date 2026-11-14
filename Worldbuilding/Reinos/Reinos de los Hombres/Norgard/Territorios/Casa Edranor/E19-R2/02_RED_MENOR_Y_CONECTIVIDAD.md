# E19-R2.02 — Red menor: del terreno al cauce, sin ríos ficticios

## Distinciones
**Vaguada**: forma del terreno; puede estar seca. **Cauce efímero**: flujo tras episodio de lluvia o fusión. **Cauce estacional**: flujo previsible en parte del ciclo hídrico local. **Cauce permanente**: aporte sostenido incluso en el periodo de estiaje bajo condiciones normales. **Manantial**: surgencia localizada solo si hay acuífero/recarga. **Río nombrado canónico**: Lurien, no un sinónimo de regato futuro. La densidad potencial no concede categoría de permanencia.

## Catorce escenarios de MICROCUENCA, no catorce arroyos existentes
Cada escenario está inscrito en hydrology_v0.3.json con ID HS-01..HS-14, exactamente dos por familia HC, y estado **SCENARIO_UNLOCATED**. Todos tienen receiver=UNKNOWN, sourceEvidence=NOT_VERIFIED y materialized=false. La denominación describe una **función geomorfológica**, no un hidrónimo registrado.

| Familia | Escenarios de generación | Causa de activación | Prueba de rechazo |
|---|---|---|---|
| HC-01 | HS-01 barranco de cabecera; HS-02 vaguada nival | convergencia sobre ladera y precipitación/deshielo | subida contra pendiente o cruce a Belara |
| HC-02 | HS-03 colector de piedemonte; HS-04 tramo perdedor | unión de escorrentías, depósito permeable | «termina» sin infiltración contabilizada |
| HC-03 | HS-05 regato entre rellanos; HS-06 bajo saturable | lluvia/recarga y concavidad | unión automática con Antela |
| HC-04 | HS-07 vaguada de interfluvio; HS-08 cauce de tormenta | escorrentía desde parcelas y laderas naturales | crear acequia o bodega para justificarlo |
| HC-05 | HS-09 cabecera de meseta; HS-10 rezume de umbría | lluvia infiltrada, nivel freático y contacto de material | manantial de caudal fijo sin acuífero |
| HC-06 | HS-11 quebrada forestal; HS-12 colector bajo resalte | ladera Azurios occidental, convergencia | gran río por Dorth o Caleran adjudicado |
| HC-07 | HS-13 drenaje de fondo frío; HS-14 cauce de deshielo | agua líquida y balance local compatible | río helado perpetuo o «deshielo» sin nieve |

## Topología exigida al materializar
Cada segmento tendrá ID estable, parentBasin, posición/cota relativa validada, causa, aportes aguas arriba, receptor aguas abajo, régimen, nivel de evidencia y procedencia. La unión de segmentos construye un **grafo acíclico dirigido** hacia un receptor final definido; no se permite ciclo de retorno. Un lago puede ser un nodo de regulación con entrada y salida diferenciadas, no una excepción para crear bucles. El desbordamiento de una depresión es un nuevo enlace *condicional y trazable*, no agua que teletransporta entre cuencas. Si hay pérdida a subsuelo, se anota descarga, recarga y salida incierta sin inventar una surgencia aguas abajo.

## Orden de nacimiento futuro
(1) terreno con divisoria y pendiente coherentes; (2) área aportante; (3) precipitación y nieve con balance; (4) infiltración/retención; (5) punto de concentración; (6) destino o receptor; (7) régimen en escenario estacional; (8) nombre local acreditado o propuesto expresamente. El número de quebradas lo fija la geomorfología, no una lista decorativa. Cuando la topología carezca de salida o viole jurisdicción se devuelve NO_MATERIALIZE y se conserva la causa de error.

## Caso Antela y frontera sur
La confluencia de un tributario en Antela no es automática por proximidad de Karsath. Debe verificarse si el agua alcanza físicamente la cubeta, si no se infiltra antes y cuál es la continuidad tras el lago. El tramo fronterizo del Lurien, sin localizar, no extiende soberanía o derechos de pesca a todo el río. Ningún puente, presa, canal de navegación, embarcadero, molino ni azud nace de un nodo de confluencia por defecto.
