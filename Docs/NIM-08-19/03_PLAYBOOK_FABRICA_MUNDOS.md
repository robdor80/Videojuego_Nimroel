# Playbook — fábrica reproducible de mundos y aventuras de Nimroel

**Fecha:** 12/11/2026. **Versión:** 1.0 de diseño. **Estado:** protocolo propuesto; no implementación.
**Propósito:** no perder el conocimiento técnico acumulado al construir V001 y poder repetir el proceso en toda Casa Valrik, Casa Darovan y el resto de territorios, sin duplicar reglas ni motor.

## 1. Qué debe repetirse y qué no

**Se reutiliza sin editar por territorio:** el parser/validador de contratos, esquema de fuentes, sistema de IDs, generador paramétrico, grafo espacial, materialización de hogares, gestión de NPC, navegación, propiedad, tiempo, órdenes de trabajo, conocimiento, actions, guardado, GDExtension y presentación Godot.

**Cambia como datos versionados:** territorio, contexto físico y regional, modelos de asentamiento disponibles, estadísticas/constraints autorizadas, oficios y variantes, personajes canónicos cuando correspondan, culturas, recursos/estacionalidad, nombres y estilos artísticos, argumentos de sucesos, pesos de tuning debidamente etiquetados.

**Nunca se copia la lógica de «La herramienta rota» a otra misión para fabricar la siguiente:** el flujo es resultado de operaciones sobre sistemas generales. Un nuevo encargo aporta condiciones/objetivos/diálogo y referencias, no un nuevo motor de propiedad, reparación ni tiempo.

## 2. Contrato de autoridades

| Capa | Qué posee | Qué NO puede hacer |
| --- | --- | --- |
| Worldbuilding | Canon y rangos/relaciones autorizados; procedencia histórica | Simular mutaciones de una partida |
| Selección/authoring | Elección autoral versionada y mapa canon -> datos operativos | Convertir una laguna de canon en hecho definitivo |
| Content Pack Nimroel | Definiciones, reglas y parámetros declarativos validados; dependencias/hashes | Ejecutar código arbitrario o alterar estado saltando Core |
| Generación Nimroel | Propuestas deterministas de una instancia inicial y trazas de decisiones | Mantener un WorldState alternativo persistente |
| CoreRPG | Identidades, estado real, acciones validadas, conocimiento, tiempo cuando se implemente, RNG y persistencia autoritativa | Contener canon de Norgard o lógica específica del encargo |
| Adaptador nativo/GDExtension | Traducir peticiones y devolver resultados filtrados, control de sesiones | Crear reglas «alternativas» o pasar snapshots privilegiados al jugador/LLM |
| Godot 2D | Mostrar, recoger texto/voz y representar acciones resultantes | Declarar que un objeto está reparado por un bocadillo o sprite |
| IA Sol/Luna opcional | Interpretación de intención y narración con contextos autorizados | Mutar directamente la realidad, adquirir secretos o gastar API sin consentimiento |

**Criterio de revisión:** ante una discrepancia, prevalecen CoreRPG para estado de partida y canon autorizado para parámetros de contenido. La UI y las respuestas IA nunca corrigen una contradicción inventando un hecho.

## 3. Flujo de producción por etapas

### Paso A — Alta de fuente canónica
1. Identificar territorio, tipo de asentamiento, versión de fuente y autoridad de la decisión.
2. Conservar path de la fuente, commit SHA exacto, anclaje/clave original y SHA-256 del contenido autorizado. No aplicar silenciosamente un borrador sin validar.
3. Clasificar cada dato: CANON_APROBADO, CONTRATO_OPERATIVO_APROBADO, TUNING_TECNICO_REVISABLE, REFERENCIA_NO_NORMATIVA o BLOQUEADO.
4. Identificar conflictos entre documentos (p.ej., modelos IA históricos) y documentar precedencia. No «corregir» Lore desde un script.

### Paso B — Selección, perfil y validación
1. Seleccionar modelo V1 y contexto del territorio; heredar rangos y restricciones; distinguir obligatorios de opcionales.
2. Mantener un manifiesto «source-lock» y un «selection» por definición, imitando el pack 4.13 ya existente.
3. Transformar únicamente los datos seleccionados a un contrato/schema versionado de Nimroel; validar cardinalidades, vínculos, vocabulario y límites.
4. Emitir un registro de cambios cuando un valor de tuning cambia, sin introducirlo en la Biblia de Lore.
5. Ejecutar pruebas negativas: falta un recurso, hash inválido, definición duplicada, dependencia circular, carácter ilegítimo, rango imposible, referencia rota, versión incompatible.

### Paso C — Publicación del Content Pack
1. Generar manifest y definiciones de manera determinista (UTF-8, LF, orden de serialización e IDs estables).
2. Construir SHA-256 de cada documento, lock de publicación y digest del conjunto.
3. Ejecutar validación Nimroel y la validación ContentJson/Core; el Host nunca acepta un pack por su nombre únicamente.
4. Versionar schema y contenido separadamente; si cambia una receta semántica, cambiar versión/huella y definir compatibilidad antes de abrir un save antiguo.
5. Publicar el pack únicamente tras revisión, no editar su carpeta generada a mano.

### Paso D — Generar una instancia
1. Recibir world_seed, stable_settlement_id, territory_context_id, region_graph_or_fixture, pack_release_id, generator_versions.
2. Derivar streams por clave (world_seed + settlement_id + subsystem_key + rules_version), evitando que añadir un servicio renumere todas las familias.
3. Generar región/entrada y luego modelo y capacidades; hogares, parcelas, edificios, conexiones; pobladores, trabajos, recursos, ubicaciones, memoria inicial. Corregir conectividad con mínima modificación trazada.
4. Asegurar dependencias reales: la herrería no equivale automáticamente a edificio independiente, ni un habitante agregado equivale a NPC materializado. Emitir identidades persistentes solo donde lo justifique el modelo.
5. Comprobar invariantes **antes de publicar la instancia autoritativa**. Registro de reglas aplicadas y parámetros experimentales; el nombre visible no puede alterar ID.
6. No volver a generar una instancia guardada; restaurar el snapshot exacto.

### Paso E — Ejecutar la partida
1. La petición del jugador se interpreta como consulta/intención, no como mutación.
2. El Host resuelve identidad del actor, alcance, autorización, precondiciones, targets, revisión y plazo.
3. Core valida y ejecuta o rechaza; el resultado se registra y se proyecta según observador. «Desconocido» no equivale a «ausente».
4. Si interviene otro NPC, tiene su propia memoria, disponibilidad, ubicación y derechos; no conoce automáticamente el resultado.
5. La narración y fondos/retratos son posteriores a la decisión Core. Una escena fuera de pantalla sigue teniendo estado lógico.
6. Los relojes/colas avanzan por eventos autorizados del mundo, no por FPS ni por completar un texto narrativo.

### Paso F — Guardar y recuperar
1. Incluir una identidad de publicación verificada, huella de generación/contexto, schemas, snapshot Core y extensión de dominio autoritativa **en un protocolo transaccional coherente**.
2. Comparar primero pack/version/hash; restaurar con ContentCatalog autenticado; rechazar o migrar explícitamente, nunca reconstruir default.
3. Abrir capacidades nuevas después de restore, caducar las anteriores; no entregar bytes privilegiados a la sesión de jugador.
4. Guardar casos de interrupción: .tmp, .bak, fallo de escritura, archivo corrupto, versión futura, guardado durante orden activa y vuelta a escena.
5. Validar igualdad de snapshot/estado/stream RNG tras ejecutar el EXE en **dos procesos independientes**. La compilación APK no sustituye ejecución Android.

### Paso G — Replicar el territorio
1. Cambiar **solo** el contexto de entrada autorizado (p.ej. otro stable_settlement_id + otra semilla; después Casa Darovan con documentación aprobada).
2. Ejecutar el mismo pipeline con igual versión de reglas y validador, sin código de misión duplicado.
3. Certificar diferencias legítimas de servicios, distribución y población sin romper obligaciones de modelo.
4. Detectar extensiones del contrato imprescindibles para un nuevo modelo; diseñar migración general, nunca condicional hardcodeado «if Darovan».
5. Producir un nuevo expediente de evidencias por pack/territorio, no reutilizar resultados de V001 como si fuesen de la nueva instancia.

## 4. Registro mínimo de fabricación y ejecución

Ejemplo **conceptual** de campos que habrá que convertir en schema real al implementar NIM-08/09:

    {
      "build_schema": "nimroel-world-factory/1",
      "status": "proposed",
      "source_lock_sha256": "<sha256 autorizado>",
      "pack_id": "nimroel.treskal.villages",
      "pack_version": "0.1.0",
      "pack_release_sha256": "<sha256 publicado>",
      "region_context_id": "region-fixture-1",
      "region_fixture_version": "1",
      "stable_settlement_id": "region-fixture-1/node-0001",
      "world_seed": "413001",
      "generator_versions": {
        "region": "<versión>",
        "settlement_v1": "<versión>",
        "layout": "<versión>",
        "households": "<versión>",
        "npc": "<versión>",
        "time_and_services": "<versión>"
      },
      "core_commit": "<sha>",
      "nimroel_commit": "<sha>",
      "snapshot_sha256": "<sha de bytes validados>",
      "test_evidence_index": "<referencia versionada>"
    }

**El ejemplo no es un formato de guardado implementado.** El contrato final deberá distinguir entre campos de identidad inicial y estado mutable, y ser compatible con el envelope I4.

## 5. Regla específica para la situación «La herramienta rota»

No se codifican directamente nombres ni diálogos de misión en CoreRPG.

- El agrícola y el herrero son **roles de una instancia generada**, no NPC universales.
- La herramienta es una **instancia con ID** y capacidades/condición, no un texto del catálogo.
- Separar, siempre, **propiedad, poseedor, ubicación, custodia/autorización, condición, solicitud, orden de taller, progreso, hora, conocimiento individual y seguimiento narrativo**.
- Crear una orden solo por una solicitud validada; aceptar ayuda no crea un juramento ni obliga a terminar.
- Mantener cola y materiales del herrero aunque el jugador visite otra escena.
- Reparada no significa devuelta, devuelta no implica que todos los aldeanos sepan lo ocurrido.
- El itinerario de abandono no destruye la necesidad ni cancela automáticamente el trabajo de los demás.
- Un segundo tipo de herramienta normal reparable deberá usar **las mismas reglas**, cambiando parámetros, no añadiendo otra clase de misión artificial.

## 6. Paquetes de documentación permanentes por fase

Cada NIM-XX contiene, como mínimo:

| Archivo propuesto | Responsable | Función |
| --- | --- | --- |
| 00_ESTADO_Y_FUENTES.md | ChatGPT | HEAD actual, fuentes/canon, dependencias, riesgos y límites |
| 01_CONTRATOS_Y_DISENO.md | ChatGPT | ADR, datos/algoritmos, autoridad, APIs autorizadas y exclusiones |
| 02_FIXTURES_Y_ACEPTACION.md | ChatGPT | Entradas doradas, positivos/negativos, IDs V001 y determinismo |
| 03_ENCARGO_CODEX.md | ChatGPT | Solo si hay implementación compleja: modelo, razonamiento, límites y pruebas |
| 04_RESULTADO.md | Codex o ChatGPT ejecutor | Código/commits, CI, hashes, test results y limitaciones |
| 05_AUDITORIA_INDEPENDIENTE.md | ChatGPT | Verificación externa y dictamen |
| 06_TRASPASO.md | ChatGPT | Estado cerrado, dependencias y siguiente puerta |

La estructura no impide incorporar documentos más finos. El README de cada fase debe apuntar al contrato vigente y no a un reporte histórico supersedido. **Ningún Codex inicia un incremento sin un encargo versionado.**

## 7. Gestión compartida con Star Trek/CoreRPG

CoreRPG es una biblioteca compartida: cambios genéricos se preparan en rama específica de CoreRPG y requieren una revisión de compatibilidad para Nimroel y Star Trek. Se fija SHA/ABI por consumidor, no se cambia silenciosamente el pin. El C++ propio de ambientación Nimroel se queda fuera de CoreRPG. El adaptador Godot 2D no introduce dependencias UE5, ni UE5 introduce su simulación en Nimroel.

En cada contrato nativo registrar:
- problema que **no** puede cubrir la API actual;
- si es una operación genérica o de dominio;
- contrato de entrada/salida, errores, rollback, coste/limites;
- pruebas Core independientes del Host, GDExtension y de escenarios;
- compatibilidad de snapshot y ABI/pins de los dos videojuegos;
- autorización antes de modificar CoreRPG o cambiar pins.

## 8. Reglas de ahorro de cuota y control de coste

- **ChatGPT primero**: extraer Lore, preparar documentación, construir tablas de conversión, fixtures de prueba, validadores pequeños, scripts de trazabilidad, propuestas de escenas/UX, manuales y auditorías GitHub.
- **Codex después**: solo cambios de C++/GDExtension, algorítmica procedural de producción, interfaces nativas de acciones, scheduler, serialización de dominio y builds multiarquitectura con alto riesgo.
- Prompt de Codex **indica explícitamente modelo GPT-6 y razonamiento Alto** para esos trabajos. No entregar «haz una aldea»; entregar contratos, carpeta y diff permitido, pruebas y puerta de cierre.
- Separar un cambio de datos/arte de una compilación de Core; reutilizar CI y no gastar cuota en reformular decisiones ya documentadas.
- La IA integrada de pago (Sol/Luna) requiere autorización de consumo y medidas de seguridad; demostrar primero toda la partida A/B/C con interpretación y narrativa locales limitadas.

## 9. Evidencias obligatorias y criterio de repetición

Repetir éxito significa:
1. Un pack íntegro surge de fuentes y versiones identificadas.
2. Una semilla produce la misma instancia en dos ejecuciones con hashes idénticos.
3. Diferentes semillas producen variación dentro de límites de canon, sin introducir invariantes falsos.
4. A/B/C pasan con actores/objetos generados, **sin IDs/diálogos especiales hardcodeados**.
5. La partida se recupera intacta durante reparación parcial.
6. El grafo, los NPC, el reloj y objetos continúan fuera de pantalla y sin renders.
7. Godot 2D presenta hechos autorizados, sin inventar rutas, personas ni progreso.
8. Funciona en Windows x64 y Android ARM64 reales con trazas versionadas.
9. Una segunda aldea usa idéntica maquinaria. Casa Darovan y otros territorios se incorporan cuando su contenido operativo esté listo, con una **nueva versión de pack**, no copiando la escena V001.

La misión es la **certificación del método**, no el destino final del motor.

## 10. Fuentes prioritarias de consulta

- NIMROEL RPG — PROYECTO MAESTRO.pdf, documento del proyecto: principios, plataformas y autoridad.
- Docs/NIM-01_EXPERIENCIA_CONVERSACIONAL.md y Docs/NIM-01_GENERACION_ESPACIAL_PROCEDURAL.md.
- Docs/NIM-07/13_AUDITORIA_ACEPTACION_I4.md y Docs/NIM-07/12_RESULTADO_I4.md.
- ContentPacks/treskal-villages/README.md y Docs/CORERPG_4_13_CONTENT_PACK.md.
- Los cuatro documentos Worldbuilding de Aldeas/03_Prueba_v0.0.1 (especialmente matriz y encargo).
- Docs/IA/POLITICA_MODELOS_NIMROEL_2026-10-17.md, revisión aprobada 20/10.
- CoreRPG: README.md, include/corerpg/action.hpp, docs/phases/4.10-actions-simulation.md, docs/phases/4.12-context-builder-ai.md, docs/roadmap.md.

**Estado normativo:** este playbook es planificación técnica, no modifica ni sustituye las fuentes de canon.