# E13 — Hidrografía, cuencas, agua menor y pendientes causales

## Canon mayor que no se altera
El **Río Lurien** nace en la vertiente oriental de Valkram, recorre la región central, entra y sale de **Lago Antela** (al sur de Karsath), pasa por **Hallheim** y desemboca en Golfo de Norgard. La navegabilidad demostrada es **Hallheim → mar**, nunca Antela/Karsath. La intersección de Lurien o Antela con la jurisdicción de Edranor es UNKNOWN. El **Caleran** nace en vertiente occidental de Azurios pero su trayectoria oriental y Arleon no autorizan paso por Dorth. Belara/Lhera, Vornarsk/Keldarsk y demás ríos no son recursos intercambiables de Casa.

## Seis expedientes hidrogeomorfológicos, NO cuencas delimitadas
| Expediente | Unidad/área de estudio | Duda | Receptor autorizado |
|---|---|---|---|
| ED13-H01 | Valkram oriental en contacto eventual | Qué fracción aporta al sistema Lurien | UNKNOWN |
| ED13-H02 | Entorno Karsath | Qué interfluvios se vinculan a Antela, si alguno | UNKNOWN |
| ED13-H03 | Meseta Bosque Alto | Salidas de su drenaje por laderas | UNKNOWN |
| ED13-H04 | Viñedo central | Respuesta de vaguadas y suelo a lluvia | UNKNOWN |
| ED13-H05 | Piedemonte Dorth/Azurios | Divisorias y receptor final | UNKNOWN; no asignar Caleran |
| ED13-H06 | Transición fría norte | Drenaje estacional/deshielo si existe | UNKNOWN; no declarar salida marítima |

El extremo norte abierto no se representa como cuenca. Cada ficha guarda estado UNDELIMITED, ausencia de polígono y ubicación UNKNOWN, con pregunta y pruebas necesarias. No se crea un hidrónimo menor en E13.

## Red menor generable solo cuando existan condiciones físicas
1. Calcular macrorelieve compatible con cotas y bordes autorizados.
2. Resolver microrelieve (incluso depresiones plausibles) sin conectividad ilógica.
3. Extraer dirección de flujo, acumulación y divisorias; comprobar continuidad de cotas y no remontada espontánea.
4. Estimar recarga local con clima/suelo/cubierta; comprobar contacto de materiales para un manantial.
5. Proponer cursos efímeros, estacionales o permanentes según balances; jamás por un lanzamiento aleatorio aislado.
6. Asignar receptor aguas abajo conocido o condición endorreica **justificada**. No crear un río que termine abruptamente por falta de mapa.
7. Conservar derechos reales/privados, usos agrícolas y cruces como capas distintas de la hidrología.
8. Versionar geometría e identidad; estado de agua, hielo o turbidez cambia temporalmente en World State, no la posición persistente del cauce.

## Reglas de riesgo y actividad
- Ladera despejada + lluvia intensa + suelo erosionable: riesgo CONDICIONAL de erosión.
- Concavidad + aporte mayor que infiltración/salida: encharcamiento CONDICIONAL.
- Frío suficiente + acumulación previa + calentamiento: deshielo CONDICIONAL.
- Desbordamiento: exige cauce, sección, cota, extensión inundable y personas/bienes expuestos; no se declara inundación repetida por intuición.
- Viticultura: abastecimiento de agua requiere captación autorizada y viabilidad, no se crean canales o riegos por mencionar bodegas.
- Madera Bosque Alto: transporte y tratamiento de barricas exige rutas físicas antes de usar agua como atajo.

## Interfaces pendientes de las cuatro preguntas E05
Karsath–Lumina, Lumina–Dorth, Dorth–Rodas y posibles pasos Valkram siguen siendo CORRIDOR_STUDY_ONLY, con **0 aristas confirmadas, 0 puentes, 0 vados, 0 ferris y 0 aduanas**. E16 evalúa servicios; E19 y E28 solo podrán materializar rutas cuando exista topografía/hidrología. Rodas no cambia su mando por conectar un camino.

## Registro mínimo futuro por segmento
segmentId persistente, basinId válido, from/to topológicos, upstreamArea, centroid/trace, permanence, sourceAuthority, legalRights, terrainVersion, generatorVersion, downstreamReceiverId y WorldState estacional separado. Todo requisito sin evidencia real queda null/UNKNOWN, nunca un valor positivo por defecto.
