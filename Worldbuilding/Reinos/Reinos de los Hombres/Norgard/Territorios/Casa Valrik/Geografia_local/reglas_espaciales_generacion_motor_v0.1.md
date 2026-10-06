# Territorio de Treskal — reglas espaciales de generación para motor v0.1

## Estado

**PUENTE DE WORLDBUILDING A MOTOR — APROBADO**

No prescribe todavía implementación, resolución de malla ni fórmulas numéricas. Sí prescribe el orden causal.

## Pipeline territorial

```text
CANON MAYOR
Sareno + Theleno + costa + Montes Invernos
↓
MACRORELIEVE
alturas y grandes pendientes
↓
MICRORRELIEVE
lomas + vaguadas + terrazas + barrancos + depresiones
↓
DRENAJE
dirección + acumulación + divisorias
↓
CUENCAS
Sareno / Theleno / costa / norte-oriente
↓
HIDROGRAFÍA MENOR
manantiales + arroyos + cauces efímeros
↓
MICROCLIMA LOCAL
humedad + niebla + nieve residual + exposición
↓
SUELO / VEGETACIÓN
infiltración + barro + estabilidad + cobertura
↓
USO HUMANO
caminos + puentes + campos + asentamientos
↓
WORLDSTATE
estado actual y persistente
```

## Reglas de generación

1. Las anclas canónicas se bloquean antes de generar detalle.
2. El generador puede añadir detalle, nunca contradecir las anclas.
3. El microrelieve debe conectar de forma continua con el macrorelieve.
4. Se conservan depresiones plausibles; no se “rellenan” todas automáticamente.
5. Las cuencas se calculan antes de sembrar cauces.
6. La red de cauces se construye desde cabeceras hacia receptores.
7. Un arroyo no se crea por probabilidad aislada; necesita aptitud hidrológica.
8. La probabilidad solo puede elegir entre alternativas físicamente válidas.
9. Los manantiales pueden iniciar un cauce con cuenca superficial pequeña si existe recarga plausible.
10. Los cauces de deshielo pueden ser estacionales aun con fuertes caudales temporales.
11. Los elementos menores sin nombre no dejan de ser persistentes una vez materializados.
12. El plano urbano debe leer esta geografía, no sobrescribirla silenciosamente.

## Determinismo

La generación debe ser reproducible mediante semilla/identidad territorial.

Mismo:
- Content Pack;
- semilla;
- anclas authored;

debe producir la misma estructura base salvo migración explícita de versión.

## Materialización

Antes de materializar:
- un detalle puede permanecer potencial.

Después de materializar:
- recibe identidad estable;
- se guarda su conectividad;
- el WorldState conserva su estado;
- no cambia de sitio al alejarse el jugador.

## Separación geometría / estado

Ejemplo:

```text
StreamSegment #TRES-HYD-184
geometry: persistent
basin: Theleno tributary
permanence: seasonal

WorldState today:
active
flow: high
cause: spring rain + snowmelt
```

El motor no necesita recalcular la existencia del arroyo cada día. Recalcula su estado.

## Regla para la IA

La IA narrativa no decide si existe un arroyo.

Recibe:
- existencia;
- tipo;
- estado;
- causa relevante;
- contexto perceptible;

y lo narra.
