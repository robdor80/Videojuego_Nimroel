# Nimroel Core — geografía física, drenaje y red hidrográfica menor v0.1

## Estado

**SISTEMA UNIVERSAL ACTIVO — REGLAS FÍSICAS DE ALTA CONFIANZA**

## Objetivo

Definir las restricciones universales que permiten explicar **por qué** un arroyo, manantial, vaguada, humedal o pequeña cuenca puede existir en un punto del mundo.

Este sistema no decide la geografía concreta de cada reino. Cada territorio aporta su relieve, clima, suelos, vegetación y grandes elementos canónicos.

## Principio rector

La hidrografía menor no se coloca al azar.

```text
macrorelieve
+ microrelieve
+ pendiente
+ divisorias
+ acumulación de drenaje
+ infiltración / manantiales
+ clima
+ nieve / deshielo
+ suelo
+ vegetación
= red hidrográfica plausible
```

## Reglas universales

1. El agua superficial sigue gradientes descendentes. Un cauce no asciende una ladera sin una causa física explícita.
2. Las crestas y divisorias separan cuencas. Un curso no cruza una divisoria para reaparecer al otro lado sin una conexión geográfica real.
3. Un cauce necesita una fuente: área de captación, manantial, deshielo, lago/humedal con salida o aporte aguas arriba.
4. La acumulación de caudal tiende a aumentar aguas abajo cuando confluyen tributarios.
5. Los tributarios convergen en redes. Cruces naturales de cauces sin interacción requieren una explicación excepcional.
6. Las depresiones pueden almacenar agua, pero deben tener salida, infiltración, evaporación o una condición de cuenca cerrada.
7. Un manantial necesita una causa plausible: contacto de materiales, nivel freático, fractura, acuífero colgado, pie de ladera o alimentación de nieve/lluvia.
8. La permanencia de un curso depende de su captación y alimentación base, no solo de la lluvia del día.
9. La vegetación y el suelo modifican infiltración y respuesta de escorrentía, pero no anulan el relieve.
10. La geometría de un cauce materializado persiste. Su estado —seco, bajo, normal, crecido— puede cambiar con el WorldState.
11. Cambios geomorfológicos grandes son eventos persistentes, no regeneraciones arbitrarias al cargar una partida.
12. Si faltan datos suficientes, `UNKNOWN` es preferible a inventar precisión.

## Unidades de microrelieve reutilizables

- **divisoria / cresta**: origen de separación de flujos;
- **loma convexa**: evacua agua, menor acumulación;
- **ladera**: transmite escorrentía;
- **vaguada / concavidad**: concentra agua y sedimentos;
- **fondo de valle**: concentra drenaje y humedad;
- **terraza fluvial**: superficie elevada respecto al cauce, menor inundabilidad que la vega;
- **llanura aluvial**: baja pendiente, alta conectividad con el río;
- **depresión**: posible encharcamiento o humedal si el drenaje es pobre;
- **abanico de piedemonte**: dispersa y redistribuye escorrentía al perder pendiente;
- **barranco / garganta**: concentración rápida de flujo;
- **paso / collado**: punto bajo de una divisoria, útil para rutas pero no convierte automáticamente dos cuencas en una;
- **llanura costera**: drenaje lento o directo al mar según pendiente y sustrato.

## Orden de inferencia espacial

El futuro generador debe respetar esta dependencia:

```text
1. elementos AUTHORED de gran escala
2. campo de elevación / macrorelieve
3. microrelieve coherente
4. pendiente y dirección de drenaje
5. divisorias y microcuencas
6. acumulación de flujo
7. candidatos a manantial
8. inicio de cauces
9. conexión de tributarios
10. humedales / zonas inundables
11. clasificación permanente / estacional / efímero
12. carreteras, campos y asentamientos
13. materialización y persistencia
```

Los asentamientos pueden modificar el drenaje después mediante zanjas, puentes, molinos u obras, pero no deben preceder conceptualmente a la geografía que los condiciona.

## Procedencia

Toda propiedad importante debe poder distinguir:

- `AUTHORED`: fijada por canon;
- `DERIVED`: deducida de reglas;
- `GENERATED`: concretada proceduralmente dentro de límites;
- `DYNAMIC`: estado temporal de WorldState;
- `UNKNOWN`: información insuficiente.

## Relación con clima

El clima y el microclima **no crean por sí solos la posición de un arroyo**.

Determinan principalmente:

- disponibilidad de agua;
- estacionalidad;
- alimentación nival;
- evaporación;
- saturación;
- probabilidad de manantiales y humedales.

La posición espacial nace de la combinación entre disponibilidad de agua y estructura del relieve/drenaje.

## Regla de persistencia

Una vez materializado un elemento menor con ID estable:

- conserva posición y conectividad;
- puede cambiar de estado;
- puede erosionarse o desviarse solo por un evento del mundo;
- no se recalcula aleatoriamente en cada visita.
