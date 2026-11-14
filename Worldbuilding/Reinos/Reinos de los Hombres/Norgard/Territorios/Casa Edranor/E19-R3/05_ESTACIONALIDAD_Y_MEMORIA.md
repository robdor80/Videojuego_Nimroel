# E19-R3.05 — Tiempo, memoria ambiental y perturbaciones

## Modelo temporal — contrato, no simulador
Al igual que Valrik, cada emplazamiento debe conservar memoria. La meteorología reciente modifica el suelo; el suelo afecta al agua; la cubierta altera sombra e infiltración; el uso humano compacta o extrae biomasa; estos efectos pueden persistir más que una lluvia o una jornada. **No** se implementan todavía probabilidades, ticks, umbrales físicos ni guardados reales.

```text
clima regional y tiempo acreditado
    + topografía / orientación / exposición
    + suelo (textura, profundidad, drenaje, humedad previa)
    + hidrología R2 (receptor probado, aporte y balance)
    + dosel / uso humano / perturbaciones previas
    -> humedad, firmeza, sombra, nieve/helada si existen
    -> erosión, habitabilidad, fenología, transitabilidad, hábitat
    -> estado persistente y efectos sobre economía / autoridades
```

## Ocho ciclos trazables
| Ciclo | Desencadenante que exige prueba | Persistencia/consecuencia sin inventar evento |
|---|---|---|
| ES-01 — Lluvia tras periodo seco | Humedad infiltrada frente a escorrentía según sustrato | Secado retardado y barro solo si retención/compactación |
| ES-02 — Lluvia sobre suelo saturado | Saturación previa aumenta escorrentía | Daño de surcos y rutas solo con pendiente y tránsito |
| ES-03 — Helada radiativa en bajo | Enfriamiento e inversión solo con topografía y calma | Daño de brotes condicionado a fenología |
| ES-04 — Deshielo sobre ladera | Fusión y respuesta a infiltración/temperatura de suelo | Barro, desprendimiento o caudal solo si aporte verificado |
| ES-05 — Sequía acumulada en loma | Agua útil cae pese a lluvia antigua | Estrés hídrico en viña solo si parcela realmente plantada |
| ES-06 — Apertura de un claro real | Más sol/viento; cambia dosel y escorrentía | Regeneración sucesional; legalidad separada |
| ES-07 — Tránsito pesado por suelo blando | Compactación y roderas persistentes | Accesibilidad futura condicionada a camino real |
| ES-08 — Temporada de cosecha forestal | Extracción reduce stock y altera suelo | Cupo, titularidad, regeneración y trazabilidad obligatorios |

## Escenarios cruzados falsables
**Estiaje central:** una loma puede mostrar estrés en vid plantada después de déficit prolongado, mientras una vaguada conserva humedad; ninguna observación concluye riego activo. El rendimiento de la vendimia no se calcula sin variedad, trabajo y cosecha reales.

**Lluvia tras vendimia:** un camino de tierra existente puede embarrarse por tránsito y compactación; si no consta camino, solo existe el escenario ambiental, no la interrupción logística.

**Primavera fría de meseta:** helada de brote requiere brote activo y condición térmica probada; no destruir por defecto el blanco de Lumina ni la feria anual.

**Bosque Alto tras corta legal:** dosel reducido incrementa luz y viento local, puede modificar escorrentía y erosión y rebajar stock, con regeneración no inmediata. Sin licencia real, el escenario no autoriza la corta.

**Umbría de Azurios tras nevada:** nieve residual condicionada por temperatura, altitud y orientación; no crear curso permanente ni derrumbe sin agua y material.

**Nava de Rodas:** el topónimo es provisional; si no se acredita depresión, se retira. Rodas pertenece a Corona aunque la humedad sea relevante para un contexto vecino.

## Persistencia mínima para futura implementación
Identidad espacial estable; clase de procedencia `AUTHORED/DERIVED/GENERATED`; fuentes y confianza; humedad/compactación/cubierta antes y después; eventos con sello temporal; titularidad y permisos si hubo uso; existencias y ritmo de recuperación; dependencias con agua y vías; capacidad de corregir/restaurar sin duplicar objetos. No persistir la *plantilla* como si fuera una parcela, árbol o día lluvioso observado.
