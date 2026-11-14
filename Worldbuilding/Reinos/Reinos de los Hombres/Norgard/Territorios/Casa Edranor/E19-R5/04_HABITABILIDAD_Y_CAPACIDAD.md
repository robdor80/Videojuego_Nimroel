# E19-R5.04 — Capacidad habitable, agua, saneamiento y decisiones
## Un lugar no es habitable por sumar puntos
La aptitud es **conjuntiva**: jurisdicción + parcela + estabilidad + riesgo tolerable + agua potable suficiente + saneamiento + alimento/sustento + título de ocupación + acceso físico legítimo + vivienda/camas y servicios + compatibilidad de conservación. Un suelo magnífico con agua UNKNOWN no permite vivienda; una ruta Gq no sustituye Gp; una licencia forestal no autoriza casa.

## Seis clases E14 reutilizadas
- `PERMANENT_RESIDENCE`: residencia habitual; exige en B3 agua potable **perenne**, saneamiento, evacuación/abasto, acceso certificado en estación crítica, vivienda, derechos y balance de población.
- `SEASONAL_WORKSTATION`: estación temporal; además refugio/camas, accesos estacionales, agua/residuos/calentamiento, retirada segura y permiso laboral.
- `AGRICULTURAL_USE`: parcela apta, disponibilidad de agua del uso concreto, licencia/título, ventana térmica, gestión de erosión y acceso para trabajos necesarios; no implica residentes.
- `FOREST_USE`: propiedad, régimen protector, permiso de aprovechamiento, cupos, regeneración, estación, seguridad y salida legítima; no implica domicilio ni propiedad de Casa.
- `TEMPORARY_PASSAGE`: servidumbre, firme/paso realmente reconocidos, permiso y exposición; no deriva de un programa CT.
- `EXCLUDED`: fuera de competencia, prohibición, protección incompatible o riesgo insalvable. MF-08 sigue `NON_EVALUABLE`, categoría distinta de `EXCLUDED`.

## Modelo mínimo de capacidad
Con datos reales: `residentesEnCorte = |PersonId con ResidenceId habitual vigente|`. Visitantes presentes aportan consumo, pero no población censada. `capacidadEfectiva = min(capacidadAguaSegura, camasHabitables, saneamiento, alimentoAbasto, servicioTiempo, evacuacionAccesible, derechos)` **solo si** todas las magnitudes comparten unidad y están medidas. Los cuellos de botella no se compensan sumando otros recursos. Los hogares, animales y actividades productivas tienen demandas distintas; no reducir un lagar a una cama ni equiparar un visitante a residente.

## Cadena de captación y contaminación
La cercanía de un lago, vaguada, fuente o río NO garantiza potabilidad, permanencia ni derechos de extracción. Separar captación, distribución, consumo, aguas grises/residuos y efectos aguas abajo. Una curtiduría, bodega, establo o letrina requiere solución segura. Cualquier déficit detectado debe bloquear el uso o generar **necesidad futura**, no crear automáticamente un pozo.

## Decisión sin ambigüedad
1. `OUTSIDE_SCOPE` si Hallheim; `NON_EVALUABLE` si MF-08 o pertenencia septentrional indecidible.
2. `INELIGIBLE` para prohibición legal o riesgo incompatibles **acreditados**.
3. `PENDING_EVIDENCE` con cualquier prueba obligatoria `UNKNOWN` o sin Gp cuando es necesaria.
4. `ELIGIBLE_IF_VERIFIED` únicamente cuando cada evidencia vale positiva, no hay veto y la autoridad competente lo confirma; en R5 esto **solo** puede ensayarse con fixtures sintéticos.
5. `MATERIALIZED` se reserva a decisión B3+B4 independiente, no es salida del validador.
