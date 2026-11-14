# E19-R3.07 — Contrato causal para una futura fábrica Godot 2D

## Capas e interpretación
```text
Fuentes canon + E19-R1 macro/microrelieve (MF, nombres)
        ↓ evidencia local y pertenencia administrativa
E19-R2 red y balance hídrico (HC/HS/SP/WH; hoy desconocidos)
        ↓ drenaje, saturación, recarga, receptor comprobados
E19-R3 suelo SO + microclima MU + cubierta CV (solo reglas B2)
        ↓ validación local + derechos
E19-R3 recursos RN + escenarios estacionales ES
        ↓ R4 continuidad de corredores / R5 suelo habitable y uso
E19-R6 auditoría → E19-TEC geometría 2D y World State
```

## Orden de inferencia futuro (no implementado)
1. Cargar topología espacial **autorizada** y comprobar que posición y laderas corresponden a la Casa, no a Darovan/Galdren/Corona.
2. Adscribir punto a MF si hay geometría y el contexto es evaluable; `MF-08` produce `DENIED_UNASSESSED`.
3. Resolver cuenca y receptor material **solo** cuando R2 disponga de datos locales verificables; si no, conservar `UNKNOWN`.
4. Evaluar suelo de forma explicable con muestras y posición de relieve; no elegir aleatoriamente profundidad o pH.
5. Calcular reglas MU que realmente tengan detonante, evidencia meteorológica y memoria suficiente.
6. Ubicar CV por transición ecológica y límites de protección, no por densidad decorativa deseada.
7. Separar recurso RN visible, material, propiedad, acceso, permiso y cuota; denegar extracción si falta uno.
8. Registrar resultados con procedencia, versión de fuente, razón causal y estado persistente idempotente.
9. Propagar consecuencias a tránsito, viñedo o habitabilidad **solo si existen** camino, cultivo o núcleo.

## Contrato de autoridad y tipos
`CANON/REPO` fija los bosques y la identidad del vino; `AUTHOR` fija fronteras por accidentes y jurisdicciones; `ASSISTANT_DELEGATED_DESIGN` solo define mecanismos condicionales. `UNKNOWN` nunca se convierte silenciosamente en `false` o en un valor generado. Las familias `SO/MU/CV/RN/ES` no son objetos de mundo ni tienen coordenadas. Los futuros objetos requieren ID estable diferente de los IDs de *plantilla*.

**Predicados de aprobación futuro:** `soilAssigned` requiere muestra/sustrato+drenaje+posición; `microApplied` requiere morfología+tiempo+estación+memoria; `coverPlaced` requiere hábitat/transición+legalidad; `harvestAllowed` requiere stock+dueño+licencia+cuota+regeneración; `landUseApproved` requiere también agua/acceso/empleo y revisión competente.

## Seguridad de fronteras y continuidad
- Oeste: vertiente occidental de Valkram = Darovan; oriental = Edranor.
- Este: occidental de Azurios = Edranor; oriental = Galdren.
- Sur: Aethros administrativo salvo tramo del Lurien sin localizar.
- Norte: sin unir líneas rojas ni fijar costa o tundra propia.
- Rodas = aldea de Corona; Hallheim fuera; Bosque Real = Corona.
- La secuencia Valkram oriental → Lurien → Antela → Lurien → Hallheim → Golfo no se modifica.
- Dorth no adquiere gran río ni Caleran; Karsath no adquiere puerto o ribera urbana por Antela.
- Bosque Alto no adquiere permiso ilimitado de tala.
- No usar la PR #84 descartada, no inventar cotas/CRS/parcelas y no subir artificialmente a B3/B4.

## Pruebas adversariales a heredar
El validador comprueba progenitor R2, equivalencia MF↔HC, plantillas no materializadas, derechos, recursos, ausencia de métricas, 7 contextos válidos y MF-08 vedado. Casos sintéticos exploran suelo sin muestras, microclima sin evento, caza sin permiso, agua sin concesión y punto en jurisdicción regia. El contrato no es un componente runtime; modificarlo no modifica Godot ni CoreRPG.
