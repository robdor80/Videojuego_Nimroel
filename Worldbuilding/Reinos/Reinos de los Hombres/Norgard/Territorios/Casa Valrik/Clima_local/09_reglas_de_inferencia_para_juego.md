# Territorio de Treskal — reglas ambientales de inferencia para el videojuego

## Estado

**BORRADOR DE DISEÑO — PENDIENTE DE ESTRUCTURACIÓN TÉCNICA**

Este documento no contendrá todavía fórmulas definitivas.

Recogerá relaciones causales validadas durante el desarrollo del lore para que, posteriormente, puedan traducirse a datos, categorías, rangos, probabilidades y reglas del motor.

Modelo conceptual:

```
localización
+ subzona
+ latitud
+ altitud
+ relieve
+ estación
+ clima
+ tiempo reciente
+ nieve/deshielo
+ suelo/drenaje
+ vegetación
+ red hidrográfica
= estado ambiental plausible y persistente
```

Ejemplos futuros:

- caudal de un arroyo no diseñado;
- barro de un camino;
- presencia de nieve residual;
- niebla en un valle;
- humedad de un bosque;
- riesgo de crecida;
- estado de pastos o cultivos;
- dificultad de viaje.


---

## Estado persistente del mismo lugar

### Estado

**BORRADOR DE DISEÑO — APROBADO COMO PRINCIPIO**

Un mismo elemento persistente del mundo —por ejemplo, un camino— puede presentar estados muy diferentes en momentos distintos sin dejar de ser el mismo elemento.

Ejemplo:

```
mismo camino
+ varios días secos
= firme, polvoriento, rápido de recorrer
```

```
mismo camino
+ lluvia prolongada
+ suelo de drenaje mediocre
+ tránsito de carros
= blando, con rodadas profundas y barro
```

```
mismo camino
+ deshielo reciente
+ heladas nocturnas
= barro, charcos, hielo residual y firme inestable
```

La IA narrativa podrá consultar ese estado ambiental persistente para describir la escena de forma coherente sin que cada variante tenga que escribirse manualmente.

### Principio narrativo

La descripción no debe inventar un estado ambiental desconectado del mundo.

Debe derivarse, cuando sea posible, de:

- identidad del lugar;
- suelo y drenaje;
- estación;
- meteorología reciente;
- humedad acumulada;
- nieve/deshielo;
- tránsito;
- hora del día.

Por tanto:

> **el lugar permanece; su estado cambia.**

Esta regla puede aplicarse también a:

- ríos;
- arroyos;
- vados;
- campos;
- bosques;
- laderas;
- puentes;
- plazas y calles sin pavimentar;
- zonas costeras.

La narración generada por IA debe reflejar el estado actual del mundo y conservar coherencia con visitas anteriores y con la evolución ambiental reciente.
