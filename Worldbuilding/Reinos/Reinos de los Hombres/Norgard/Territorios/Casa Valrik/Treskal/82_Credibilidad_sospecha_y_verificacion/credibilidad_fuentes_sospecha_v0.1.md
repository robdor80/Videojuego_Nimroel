# Treskal — credibilidad, fuentes y sospecha v0.1

## Estado

**DISEÑO SOCIAL/JUGABLE APROBADO — CREER NO ES SABER**

## Objetivo

Definir cómo un NPC valora una afirmación sin consultar la verdad oculta del motor.

## Estados operativos

### CRED01 — unassessed_claim
Ha recibido la afirmación, pero todavía no la ha valorado de forma relevante.

### CRED02 — provisionally_credible
Le parece plausible de forma provisional.

### CRED03 — trusted_but_unverified
Confía bastante en la fuente, aunque no dispone de comprobación independiente.

### CRED04 — uncertain_or_unverified
No tiene base suficiente para decidir.

### CRED05 — doubted_or_suspicious
Existen razones para dudar.

### CRED06 — corroborated
Ha encontrado apoyo adicional independiente o suficientemente distinto.

### CRED07 — contradicted_by_evidence
Existe evidencia que entra en conflicto con la afirmación.

### CRED08 — resolved_by_direct_confirmation
Dispone de una vía de confirmación directa o equivalente suficientemente fuerte.

## Credibilidad no es verdad

Una afirmación puede ser verdadera y poco creíble o falsa y muy creíble.

CRED describe la evaluación del observador.

STAT y World State conservan la realidad de la declaración.

## Fuente

La credibilidad de una persona depende del contexto.

Un maestro ebanista puede ser excelente fuente sobre madera y mediocre sobre política naval.

No existe una fiabilidad universal para todos los temas.

## Relación

Amistad, familia o pareja pueden aumentar confianza.

No convierten automáticamente cada afirmación en verdad.

Desconfiar de alguien tampoco vuelve falsa una información cierta.

## Historial

Un NPC puede recordar que una persona suele acertar, exagera, repite rumores o ha dado información falsa antes.

Solo si conoce realmente ese historial.

## Apariencia y conducta

Nerviosismo, evasión, calma o seguridad pueden influir en sospecha.

No prueban por sí solos verdad, falsedad ni intención.

No hay detector de mentiras sobrenatural.

## Rumor repetido

Escuchar la misma historia de cinco personas no equivale necesariamente a cinco fuentes.

Si todas la recibieron del mismo origen, la independencia es baja.

La procedencia importa.

## Jugador

Las afirmaciones del jugador se valoran con las mismas reglas.

La reputación puede influir en disposición a creer, no en la verdad objetiva.

## IA

La IA puede expresar confianza, duda o necesidad de comprobación.

No puede conocer directamente el estado interno STAT de otro hablante.

## Regla final

**En Treskal una persona cree a otra por razones humanas; nunca porque el motor le susurre quién dice la verdad.**
