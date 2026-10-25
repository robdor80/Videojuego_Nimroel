# D12 — Matriz de preparación técnica, CoreRPG y Host Nimroel
**Fecha:** 25/10/2026. No modifica CoreRPG, Godot, NIM-06 ni GDExtension.

## Evidencia de capacidad (tres columnas NO equivalentes)
| Área | Canon/dato estructurado disponible | Código realmente probado | Falta para jugar en Darovan |
|---|---|---|---|
| Identidad territorial | D00/D07: 4 ciudades canónicas + Casa; Arven y Karsath | D11: 5 ResourceDefinitions, referencias y catálogo C++ CoreRPG | Instancias WorldState, escenas/ubicaciones, reglas/Host |
| Geografía/hidrografía | D01–D03: 12 zonas, 5 ríos, 4 sistemas, topología cualitativa | Validadores estáticos Python; no GIS | Terreno 2D, coordenadas, costes, clima/agua simulados |
| Recursos y producción | D04: 8 cadenas, estructuras existentes y prohibiciones | Ningún ciclo productivo territorial probado | CORE-REQ-D11-01: inventario, propiedad, stocks, transformación, save/load y doble gasto |
| Rutas/comunicaciones | D05: 3 conexiones modales y 4 suministros sin ruta | Validadores estáticos; NO pathfinding/coste | CORE-REQ-D11-03: disponibilidad, movimiento, riesgos, enlaces accesibles, tiempos y persistencia |
| Asentamientos | D06: 9 modelos, pesos cualitativos, semillas, TEST_ONLY | Generador y checks deterministas de diseño, sin spawn en juego | Selección de sitio acreditado, instancia estable, guardado, representación |
| Ciudades | D07: perfiles y tres orientaciones aprobadas, Treihord base cerrada | Índices y JSON validados, sin escena jugable | Diseño espacial autoral + Host 2D y personajes |
| Población/hogares/profesiones | D08: intervalos y reglas orientativas, sin censos/personas | Contratos semánticos y tests estáticos; CoreRPG generic population/relations preexistentes NO son hogar Darovan | CORE-REQ-D11-02: residencia, parentesco, empleo, propiedad, turnos, traslado con conservación de identidad |
| Gobierno/fiscalidad/seguridad | D09: límites competenciales, autoridades, categorías fiscales | Tests estáticos, NO motor fiscal/judicial | CORE-REQ-D11-04: autoridad, permisos, libro mayor, jurisdicción y recursos |
| Cultura/NPC/vida social | D10: 17 elecciones, límites de atribución, Arven UNKNOWN | Tests estáticos, NO personalidad social de Darovan | CORE-REQ-D11-06: personalidad individual no esencialista, conocimiento, hechos, relaciones y consecuencias |
| Acontecimientos | D11 T01–T08: especificaciones de situaciones futuras | NO ejecutadas: \`SPECIFICATION_NOT_EXECUTED\` | CORE-REQ-D11-05: reloj, eventos, determinismo, continuidad, snapshots |
| Catálogo/persistencia | D11: manifest+5 defs+11 locks+8 fixtures | C++ real de catálogo con binding/save-load sintético y esquemas Core 0.1.0; CI D11 verde en ambos SO | Adaptador semántico del sidecar; secuencia de migración/persistencia de contenido |
| Host 2D | NIM-06 merge PR #27 en main 24/10 | Bridge genérico GDExtension; CI y comprobaciones propias NIM-06, NO prueba de Darovan | NIM-HOST-D11-01: integración del pack, preflight de versión/locks, escenarios en MSI y Tab S9+ |

## Qué puede consumirse ya SIN atribuir simulación
1. \`ContentPacks/darovan-territory/pack\`: identificadores estables y enlaces tipados (contrato Core 0.1.0).
2. \`authoring/projection-v0.1.json\`: sidecar Nimroel para preflight, reglas/guardrails y trazabilidad. CoreRPG no acepta directamente ese objeto como ResourceDefinition.
3. Índices D00–D10 como fuentes de diseño y validación, manteniendo UNKNOWN y PROPOSAL.
4. \`fixtures/d11-scenarios-v0.1.json\` SOLO como especificación futura, nunca evidencia de juego.

## Dependencias y estrategia futura (no autorizadas para ejecutar ahora)
- **P1 — CORE-REQ-D11-01/02/03**: recursos, hogares, movimiento; definir APIs genéricas reutilizables, pruebas temporales y de persistencia, sin codificar Darovan dentro de CoreRPG.
- **P2 — CORE-REQ-D11-04/05/06**: competencias/fiscalidad, eventos/reloj y personalidad/autonomía NPC; coherencia causal y visibilidad.
- **P1 — NIM-HOST-D11-01**: loader de packs, preflight SHA/contratos/migraciones, visualización 2D y pruebas físicas Windows x64 / Android ARM64.
- **Autor:** ubicación y características de emplazamientos, rutas adicionales, cifras concretas y cultura de Arven solo si una implementación concreta las requiere. Pueden continuar UNKNOWN para cierre territorial documental.

## Compatibilidad y migración
El pack declara Content Contract 0.1.0, cinco DefinitionIds propios e inmutables; no son EntityIds. No se forzarán payloads suplementarios en los esquemas oficiales, ni dependencias físicas sobre Content Packs no publicados. Modificaciones posteriores a fuentes protegidas deben provocar revalidación de los once SHA y un proceso de preflight/migración; no se recalculan silenciosamente. Mantener siempre test negativo frente a catalogación de caminos inexistentes, populación inventada y ejecución ficticia.

**Dictamen B:** preparada la base de identidad/contratos/validaciones; pendiente implementación de semántica y simulación real. La CI que compila C++ NO constituye prueba de gameplay.
