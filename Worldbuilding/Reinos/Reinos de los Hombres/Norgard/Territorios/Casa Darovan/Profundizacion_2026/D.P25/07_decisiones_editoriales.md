# D.P25/07 — Ocho elecciones aprobadas por delegación

**12/11/2026.** El autor ha concedido autonomía para completar D.P25 y adoptar las recomendaciones creativas como decisiones propias. Esta autorización comprende las siguientes **elecciones editoriales**. La materialización jugable, la creación de hechos públicos, la aprobación de genealogías concretas y el merge a `main` no se infieren de esa instrucción.

| ID | Elección editorial adoptada | Alcance |
|---|---|---|
| DP25-D01 | **A** — preservar las 52 bases personales existentes/propuestas y seleccionar 27 hilos conductores | Relevancia de diseño, no 27 NPC generados |
| DP25-D02 | **A** — usar IDs del material fuente en lugar de renombrar biografías | Referencias trazables a D.P20–24; sin retcon |
| DP25-D03 | **A** — diseñar 30 relaciones posibles, bidireccionalidad no supuesta | Estado inicial desconocido y `actualRelationshipId: null` |
| DP25-D04 | **A** — cuatro modelos de hogar/cuidado sin genealogía nueva | Cero parentescos, matrimonios o herencias creados |
| DP25-D05 | **A** — diez conflictos causales territoriales con salidas plurales | Ninguna misión, sanción, viaje o evento activado |
| DP25-D06 | **A** — diez escenas multirrol y conocimiento no omnisciente | `TEST_ONLY`, ninguna consecuencia persistente |
| DP25-D07 | **A** — autoridad de Norgard y CoreRPG, cartografía y recursos reales como puertas de entrada | No aduanas internas, autoridad naval impropia ni nuevas rutas |
| DP25-D08 | **A** — publicar rama y PR Draft para auditoría D.P26; cierre por CI real y revisión de dependencias | **No** fusión a `main` sin autorización separada |

**Decisiones expresamente NO tomadas:** quién ocupa actualmente la jefatura de Casa Darovan; herederos, alianzas matrimoniales, rivalidades familiares ejecutadas; rangos de Orel; jueces identificados; fundación de nuevos grupos; fechas históricas; paso a pie entre islas; ubicación de las nueve comunidades; inventarios, tarifas, censos, contratos reales o resultado forzoso de ninguna historia.

## Gobernanza de las dependencias
D.P23 (#46) y D.P24 (#47) estaban Draft al abrir D.P25. Aunque la dirección editorial esté aprobada, el **orden de fusión** exige resolver esas dos PR, comparar sus HEAD fusionados y ejecutar regresiones sobre la rama actualizada de D.P25. Ninguna CI sobre una rama que carece de las fuentes de D.P23/24 demuestra coherencia definitiva del conjunto. D.P26 debe registrar explícitamente su estado.

## Distinción de autorizaciones
- Selección creativa: **sí**, por la petición del 12/11/2026.
- Publicar documentación y preparar PR Draft: **sí**, dentro de la fase.
- Crear NPC, familias, misiones y actividades ejecutables: **no**; requeriría proyecto de materialización con fuentes y contratos.
- Fusionar `main`: **no implícito**; el cierre queda preparado para revisión.

Una futura decisión autoral concreta de materializar personajes y otorgar hogares sustituirá los `null` pertinentes mediante una operación revisada, nunca por reinterpretación retrospectiva de este documento.
