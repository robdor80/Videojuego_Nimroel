# E10 — Matriz de conflictos: las consecuencias no se escriben antes de jugar
**Estado:** semillas propuestas, NO guerras, delitos, resoluciones ni eventos del año 15375 ya consumados.

| ID | Eje y actores | Prueba/decisión del jugador | Autoridad que NO se suplanta |
|---|---|---|---|
| EDR-C01 | Rodas: Elira, Heran, Vesra | Distinguir petición Edranor de orden real; revisar original y vigencia | Corona Aethros |
| EDR-C02 | Sucesión: Elira, Maelis, Caelen | Separar reputación, preferencias y documentos de filiación/derecho | Ley sucesoria y confirmación regia |
| EDR-C03 | Lumina: Ysna, Tovan | Acreditar madera y calidad del tonel antes de resolver responsabilidad | Propietario del bosque y licencia competente |
| EDR-C04 | Karsath: Lira, Orlan | Rastrear origen del vino escaso y evaluar etiquetado | Justicia del Rey / derechos privados |
| EDR-C05 | Dorth: Orlan, Maelis | Cotejar un lote incompleto con registros sin señalar culpable prematuro | Justicia y autoridad comercial existente |
| EDR-C06 | Mercado anual de Lumina: Ysna, comerciantes | Decidir distribución espacial conforme a autorización existente | E09 mercados, sin tributo nuevo |
| EDR-C07 | Tradición de Rodas: Saer, Bren, Heran | Elegir qué información divulgar de manera legítima | Corona; custodia no religión |
| EDR-C08 | Crisis de suministro: Caelen, Tovan, Orlan | Priorizar reparaciones y cargas cuando las rutas estén validadas | Inventarios, derechos, autoridad de transporte |

## Escalada responsable
Cada conflicto sigue una progresión **opcional**: indicio → fuente o testimonio → contraste → propuesta de solución → respuesta de autoridad competente → persistencia solo tras transacción válida. No se marca «culpable», «guerra», «rey cedió Rodas» ni «el heredero subió al poder» sin hechos verificables y World State.

## Criterios narrativos de arbitraje
- **Evidencia antes de reputación:** las acusaciones requieren fuente, contradicción y derecho de réplica.
- **Ganador no equivale a cambio jurisdiccional:** apoyar a Edranor en Rodas puede mejorar la relación o el conocimiento, no cambiar propiedad/competencia de la Corona.
- **Lo moral no habilita lo jurídico:** el jugador no dicta sentencias, impuestos ni talas por buena intención.
- **Coste y beneficio ubicados:** reparar toneles consume madera, tiempo y mano de obra solo si existen en mundo; no crear recursos invisibles.
- **Personajes falibles:** los intereses propios no son prueba de dolo; la Corona tampoco es antagonista por definición.
- **Reversibilidad y memoria:** un testimonio falso descubierto posteriormente abre corrección/reparación, nunca reescribe retrospectivamente todos los diálogos.

## Requisitos E11
`authority_ref`, `evidence_refs`, `actor_knowledge`, `world_state_version`, `jurisdiction`, `consent_ref` y `effects_requested`. Si falta una fuente materializada, la misión permanece **BLOQUEADA POR DATOS**, no se simula un permiso.
