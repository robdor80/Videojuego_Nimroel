# E19-R4.06 — Firmes, fenómenos estacionales, averías y conservación
**Diez mecanismos HZ; ninguno es un corte ocurrido ni prueba la existencia de un camino.** Se derivan de E19-R2 (balance y crecidas), R3 (suelos/microclima/ES) y E05 (viabilidad), no de probabilidades decorativas.

## Cadena causal obligatoria
Entidad vial real → localización y suelo → exposición y memoria previa → fenómeno observado → efecto físico → inspección/aviso → restricción por modo → reparación y reapertura autorizada. Un mapa de tipos HZ no permite cerrar rutas inexistentes. Las consecuencias del tránsito sobreviven a la lluvia.

## Diez escenarios con prueba y memoria
| ID | Disparador comprobable | Efecto posible (no garantizado) | Prueba exigible |
|---|---|---|---|
| HZ-01 | lluvia + suelo saturado + rodadas | barro y atasco localizado | suelo, historial de humedad, tráfico y segmento real |
| HZ-02 | deshielo sobre pendiente inestable | erosión, piedras o pérdida de borde | material, orientación, nieve observada, daño inspeccionado |
| HZ-03 | helada posterior a agua presente | hielo en paso sombreado | temperatura/agua, tramo real, inspección, no etiqueta «norte» |
| HZ-04 | avenida sobre cruce existente | vado o puente temporalmente inseguro | cauce y receptor reales, nivel observado, capacidad de obra |
| HZ-05 | sequedad + tráfico sobre fino | polvo y pérdida de firme | tipo de suelo, paso real, desgaste medido |
| HZ-06 | tránsito forestal pesado autorizado | compactación/roderas progresivas | licencia, viaje y masa de carga, firme y recuperación |
| HZ-07 | caída de árbol o rama comprobada | obstáculo y posible desvío | individuo/ubicación/evento/limpieza, no bosque genérico |
| HZ-08 | desprendimiento en corte de ladera | cierre parcial por detritos | localización, estratos, acción y autoridad de retirada |
| HZ-09 | sobrecarga en evento real de feria/vendimia | cola, retraso, deterioro | calendario, viajeros, capacidad, ruta validada |
| HZ-10 | falta de mantenimiento comprobada | degradación acumulada y mayor coste | responsable, inspecciones, historial de obras y material |

## Territorios y diferencias
**Valkram:** exposición y estabilidad, con nieve solo donde conste. **Piedemonte:** avenidas laterales y suelo heterogéneo; ni todo barranco es paso ni toda estación es inaccesible. **Karsath:** suelos de rellanos, problemas de fondo y helada condicionales; no inventar crecidas del Antela en calles. **Lumina/Bosque Alto:** dosel, umbrías y compactación tras actividad autorizada; no heladas perpetuas. **Dorth/Azurios:** paso de bosque a ladera, nunca río mayor inventado. **Rodas:** transición fría y autoridad regia, sin calendario boreal automático.

## Estados futuros distintos
- **Físico permanente:** eje y firme certificados, obras e identidad estable.
- **Condición cambiante:** SECO, HUMEDO, EMBARRADO, HELADO, OBSTRUIDO, DANADO, INSPECCION_PENDIENTE; usar solo si existe segmento y prueba.
- **Acceso legal:** PERMITIDO, RESTRINGIDO, DENEGADO, UNKNOWN; independiente del estado físico.
- **Conocimiento del viajero:** lo que sabe, cuándo lo supo y por qué; puede estar desfasado.

## Reparación
Un aviso no arregla la vía. Orden de obra → propietario/autoridad → disponibilidad de cuadrilla/herramientas/materiales → acceso a la avería → ejecución → inspección → actualización persistente. La reapertura no resulta del paso de un número fijo de días. Si la reparación consume piedra, madera o trabajo, proceden de stocks reales. Si un puente no existe, tampoco puede repararse.

## Falsadores
No cerrar todos los caminos de Lumina al llegar el invierno; no abrir al salir el sol si persisten roderas; no asignar horas de viaje a CT; no computar tráfico en un grafo vacío; no marcar inundación de Dorth por Caleran; no eliminar el rastro de un derrumbe tras cambiar de escena; no inventar una ruta alternativa al aparecer un bloqueo.