# DAROVAN D07 — Auditoría de entrega a revisión (21-10-2026)

**Estado:** BORRADOR DE CIERRE CON APROBACIONES AUTORALES ABIERTAS. No fusionar ni iniciar D08.
Repositorio: robdor80/Videojuego_Nimroel. Rama: feat/darovan-d07-ciudades-canonicas. Base de main previamente verificada: e2636f33791b11ec6ad2e478df95ab190de0f09e (merge D06 PR #31).

## Alcance entregado
- Auditoría original individual de Treihord, Veldora, Taramin y Syvaris, con contraste de Norgard y matrices D01–D06.
- Treihord CANON DISEÑO BASE CERRADO intacto; no se han renombrado barrios, cambiado 32.000 aproximados, palacio, Crisol, Vena o puerto del Belara.
- Veldora, Taramin y Syvaris: perfiles de identidad **referenciada** y capas funcionales PROPOSAL_PENDING_AUTHOR sin localización, barrio o edificio nuevo.
- Matriz de hechos con referencias y JSON operativo de planificación, junto con validación estática de campos, hechos y pruebas negativas.
- Registro de decisiones DAR-D07-01/02/03 expresamente pendientes del autor; UNKNOWN sin completar.

## Protección de fronteras
D02 cinco ríos/cuatro sistemas; D03 zonas contrastadas; D04 sin explotaciones/capacidades ficticias; D05 ningún camino derivado de suministro; D06 exclusión absoluta del generador; Norgard sin aduana interna ni armada privada Darovan. No hay cruces, puertos secundarios, poblaciones o puentes nuevos. CoreRPG conserva toda autoridad del estado; Godot solo visual.

## Validación y CI
**Primer run real de la PR Draft #32:** [GitHub Actions #39632063452](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39632063452), correspondiente al commit `701e24c167a1d60a2f9676d884aadef09f3e9c34`. Resultado comprobado en logs de ambos jobs:

| Runner | D01 | D02 | D03 | D04 | D05 | D06 | D07 | Job |
|---|---|---|---|---|---|---|---|---|
| ubuntu-24.04 | OK | OK | OK | OK | OK | OK | OK | SUCCESS |
| windows-2022 | OK | OK | OK | OK | OK | OK | OK | SUCCESS |

D07 ha validado **cuatro ciudades manuales, 40 hechos con referencia de fuente, 18 campos `UNKNOWN`, nueve capas conceptuales no canónicas y 43 mutaciones negativas rechazadas**, con comprobaciones cruzadas D01–D06. Todas las regresiones anteriores D01–D06 también finalizaron STATIC OK en los dos sistemas.

**Límite de esta evidencia:** pruebas documentales/JSON/Python en CI; no hay materialización urbana, cartografía métrica, simulación CoreRPG, escena Godot ni aprobación urbanística del autor. Este registro de auditoría genera un commit editorial posterior al primer run; **hay que comprobar además el Actions asociado al HEAD final de la PR #32 antes de proponer fusión**.

## Cierre editorial condicionado
Aprobación autoral pendiente de enfoques para Veldora, Taramin y Syvaris; solo entonces se podrá considerar cerrado el diseño urbano sustantivo, si así lo decide el autor. Ni CI verde ni JSON de propuesta promulgan identidad o localización. D08 no se ha desarrollado; traspaso preparado.
