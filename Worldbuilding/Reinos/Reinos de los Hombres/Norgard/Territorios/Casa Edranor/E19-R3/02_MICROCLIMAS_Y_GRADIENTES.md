# E19-R3.02 — Microclimas derivados, sin meteorología inventada

## Diferencia clima / tiempo / microclima
Norgard posee transiciones climáticas regionales; E03 no tiene series de Edranor. La regla de Valrik es superponer **clima regional + situación topográfica + dosel y suelo + meteorología reciente**, conservando memoria. Un bosque **no fabrica lluvia**; una ribera no crea por sí sola un río. Radiación, exposición, ventilación, frío nocturno y agua almacenada actúan en escalas distintas. No se asignan deltas térmicas ni probabilidades de niebla.

## Once reglas de inferencia (nunca localizaciones nuevas)
| ID | Modificador | Evidencia positiva imprescindible | Posible respuesta | Denegación |
|---|---|---|---|---|
| MU-01 | Solana de ladera | ORIENTACION INSOLACION PROBADAS | Mayor secado posible | No equivale a ausencia de helada |
| MU-02 | Umbría de ladera | ORIENTACION SOMBRA PROBADAS | Humedad o nieve retenida posibles | No produce lluvia propia |
| MU-03 | Bolsa de aire frío en fondo | DEPRESION Y NOCHE ESTABLE PROBADAS | Helada local potencial | Sin valle acreditado no hay inversión |
| MU-04 | Interior de dosel forestal | DOSel DENSO VERIFICADO | Menos viento/sol y humedad persistente posibles | No niebla perpetua |
| MU-05 | Borde o claro forestal | CLARO REAL Y ESTADO DE CUBIERTA | Mayor amplitud y viento potenciales | No imputar tala ilegal |
| MU-06 | Cercanía a cauce o humedad | CURSO O SATURACION Y RECEPTOR VERIFICADOS | Rocío/bruma local condicional | No crear regato ni ribera |
| MU-07 | Cresta expuesta | CRESTA Y VIENTO VERIFICADOS | Mayor exposición, posible desecación | No huracanes por etiqueta |
| MU-08 | Nieve y deshielo de umbría | NIEVE REAL Y BALANCE TERMICO | Persistencia de nieve y barro condicional | No calendario terrestre fijo |
| MU-09 | Suelo compactado húmedo | TRANSITO REAL Y LLUVIA ANTERIOR | Barro persistente posible | No todo suelo mojado es barro |
| MU-10 | Borde de meseta de Lumina | BORDE MESa REAL Y SERIE METEO | Contrastes de viento, sol y nube | Sin elevación numérica inventada |
| MU-11 | Transición boreal gradual | CONTINUIDAD REGIONAL Y LATITUD | Pueden cambiar helada y cubierta | No fijar límite polar dentro de Edranor |

## Transectos de estudio
**Valkram oriental → piedemonte:** puede descender la exposición y la frecuencia de nieve, pero una vaguada protegida podría ser más fría de noche que su ladera. No trasladar Belara desde la vertiente Darovan. Sin mediciones no es lícito dibujar cotas de helada.

**Karsath → campiña:** los rellanos ventilados, bajíos y solanas constituyen situaciones ecológicas diferenciables si existen. Un bajo puede concentrar humedad y aire frío, mientras una media ladera drena mejor; no deducir Antela urbano ni vendimia temprana.

**Meseta de Lumina → Bosque Alto:** bosque cerrado, borde y claro cambian radiación y viento. Una umbría podría retener nieve más tiempo; una tala real altera respuesta durante estaciones posteriores. Bosque Alto tiene aprovechamiento de madera regulado: la relación microclimática **no autoriza** abrir un claro.

**Resaltes de Dorth → Azurios occidental:** pisos forestales y exposición forman transición, no una franja donde todo el viento, niebla o nieve sea igual. No llevar Caleran a Dorth ni extender derechos de Edranor al Bosque Real.

**Transición fría y Rodas:** los efectos boreales son regionales y graduales; Rodas sigue aldea de Corona Aethros. MF-08 no participa mientras el norte no esté resuelto; no tundra, permafrost permanente ni viña septentrional por defecto.

## Estacionalidad responsable
La helada exige temperatura local, exposición y duración; el daño exige además cultivo real y fenología. La niebla exige humedad, enfriamiento y condiciones de aire; no nace por el simple dosel. La nieve exige precipitación y temperatura compatibles; el deshielo tiene inercia en umbrías. Todos los procesos permanecen `UNKNOWN` para fechas y magnitudes.

## Escenarios de contraste obligatorios
- Bosque Alto seco tras semanas sin lluvia: el dosel no obliga a barro o niebla.
- Claro húmedo tras lluvia frente a umbría drenante: el claro puede encharcarse más por compactación.
- Fondo de valle más frío de madrugada que una solana cercana, **solo si** existe valle y noche estable.
- Ribera verde en seca estacional, **solo si** hay cauce acreditado y agua disponible.
- Ladera septentrional con nieve residual y vecino soleado sin nieve, solo con evento real.

El futuro generador debe publicar **por qué** asignó cada modificador y qué datos faltan. Si el requisito falla, conserva estado desconocido: no sortear una niebla o una helada para decorar.
