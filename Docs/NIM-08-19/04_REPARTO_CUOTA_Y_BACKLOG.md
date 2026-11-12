# Reparto operativo, reserva de Codex y backlog independiente

**Proyecto:** Nimroel RPG, vertical jugable V001. **Fecha:** 12/11/2026. **Estado:** propuesta de ejecución por autorización futura; nada iniciado por esta rama.

## Política de asignación

**ChatGPT es por defecto responsable del trabajo**. Codex solo se invoca por necesidad concreta: modificación C++/CoreRPG, ABI y GDExtension, algoritmos de mundo en producción, persistencia de dominio, integración compleja Godot y compilaciones/regresiones exigentes.

No etiquetar «Codex» una fase entera porque incluya programación. ChatGPT prepara los P01/P02, insumos de prueba, fixtures y documentación. **No consumir cuota Codex para reescribir lo que ChatGPT haya podido entregar y validar.**

| Fase | Trabajo completamente asignado a ChatGPT antes de llamar a Codex | Trabajo mínimo que se reservará a Codex | Puerta para liberar Codex |
| --- | --- | --- | --- |
| **08** | Auditoría CoreRPG/NIM07, arquitectura, tipos de datos, matriz, ADR e invariantes | **Ninguno** | Contratos cerrados, autor decide inicio |
| **09** | Inventario canon Valrik/Treskal, source locks, esquemas, parámetros, extractores y validators Python, pack de ejemplo | Solo enlace nativo al codec si falla la ruta existente | Dos reconstrucciones con hashes idénticos y pruebas negativas |
| **10** | Modelo V1, generador de datos de referencia, seeds de prueba, especificación de grafo, constraints y casos de conectividad | Generador ejecutable de mundo/layout, integración Core + pruebas multiplataforma | G01-G06 convertidos en test cases, datos/schemas congelados |
| **11** | Reglas de hogares, tamaños, profesiones, vínculos y población latente; escenarios de validez | Materialización de entidades, persistencia/relaciones, algoritmos eficientes | Fixtures demográficos y vínculos sin huecos canónicos |
| **12** | Contrato de posición/rutas, permisos, tiempo y visión; tablas de test positivos/negativos | Implementación autorizada de navegación/percepción y puente de sesión | Modelo espacial de NIM10 estable |
| **13** | Matriz de propiedad/posesión/custodia/daño, reglas y casos negativos, diseño de objeto | Motor de operaciones seguro, estado real de herramienta y persistencia | Contrato TOOL/COND/OWN validado y tests Q01/Q02 preparados |
| **14** | Reglas de cola, ocupación, disponibilidad, horario, calendario, insumos, pausas y autonomía | Scheduler/acciones/ticks deterministas y transacciones de dominio | NIM13 + modelo TIME/WAIT listos; escenarios de bloqueo definidos |
| **15** | Reglas de conocimiento, materiales de diálogo, voz/tono, filtros de NPC y tests sin IA | Integración diálogo/Knowledge/contexto/acciones | P02/Q08 con dos observadores y hechos ocultos definidos |
| **16** | Encargo completo A/B/C, máquina de estados, eventos/objetivos y test de indiferencia | Integrar orquestador/acciones de misión con mundo real | NIM10–15 pasan lógica sin Godot |
| **17** | UX limpia, textos, fondos 2D/retratos/prompt de arte, selección de escena y accesibilidad | Enlace GDExtension/UI, render y eventos; proveedor de IA solo con permiso | Endpoints de acciones/observaciones estables, UX aprobada |
| **18** | Auditoría de formatos, estrategia de compatibilidad, pruebas de referencia, índices SHA y casos adversariales | Persistencia plena transaccional y regresiones Windows/Android | Modelo completo fijado y salvaguarda I4 reconciliada |
| **19** | Auditoría independiente, matriz 28 IDs, pruebas multi-seed, informes, manual y réplica Darovan | **Solo defectos de código complejos si aparecen** | EXE/APK, guardado y A/B/C pasados; autor dispone de dispositivos |

## Orden temporal que economiza cuota

**Ola A — Cero Codex, comienzo inmediato tras autorización:**
- cerrar documentalmente NIM-08 y NIM-09;
- preparar contratos P01/P02 y fixtures de **NIM-10 a NIM-16** mientras Star Trek usa Codex;
- preparar UX y assets provisionales de NIM-17 y pruebas de NIM-18 sin implementar runtimes.

**Ola B — Primera asignación de Codex al quedar cuota:**
- ejecutar **NIM-10** generación V1/layout y luego **NIM-11** población/hogares; no empezar nueve ramas de código a la vez;
- solo después de pasar CI, derivar la siguiente pareja de contratos nativos (movimiento/percepción NIM-12 y objetos NIM-13);
- mantener auditorías entre lotes, no destruir trabajo validado.

**Ola C — Simulación de misión:**
- NIM-14 reloj/colas y NIM-15 diálogo/Knowledge;
- NIM-16 usa APIs ya existentes; no introducir servicios hechos a medida para un único encargo.

**Ola D — Host y certificación:**
- NIM-17 Godot integra; NIM-18 conserva todo; NIM-19 valida y replica.

Estos son **paquetes de planificación**, no una promesa de consumo ni de fecha. Si una pieza nativa la puede implementar ChatGPT con riesgo bajo, se revisa antes de asignarla a Codex; el ahorro nunca justifica romper la frontera del Core.

## Reglas de ejecución de Codex (para cada encargo)

1. En el prompt indicar **modelo GPT-6, razonamiento Alto**, repositorio, rama, base SHA, archivos/contratos obligatorios, código permitido, exclusiones y pruebas.
2. No modificar main, canon, otros territorios, pins de CoreRPG, API de pago, Android signing ni ramas Star Trek sin autorización específica.
3. Cuando afecte CoreRPG común, crear **propuesta separada de API genérica**, con impacto en Star Trek y validación cruzada, no introducir lógica de aldeas en CoreRPG.
4. Codex desarrolla, prueba, documenta y publica **PR Draft no fusionada**, con commits, CI, hashes, factores de riesgo, compatibilidad y ejemplo de uso.
5. ChatGPT realiza auditoría ajena al implementador; ni CI en verde ni el reporte de Codex equivalen a aceptación humana.
6. El propietario autoriza la fusión. Cada fase desbloquea la siguiente únicamente tras puerta de aceptación.

## Lista de prerrequisitos que puede preparar ChatGPT sin bloquear a Star Trek

- Catálogo de datos fuente, trazabilidad de Casa Valrik/Treskal y tabla de campos que necesitará Darovan.
- Corpus canónico de profesiones/recursos/herramientas/propiedad/memoria/espera, sin suposiciones silenciosas.
- 100 semillas y regiones fixture con resultados esperados a nivel de invariantes (no mundos completamente inventados a mano).
- Fixtures de un herrero ocupado/libre, recurso faltante, herramienta en manos ajenas, distinto observador, retrasos y reparaciones parciales.
- Diagramas de estados, contratos de objetivos, respuestas a comandos, prueba de narración alucinada y política de IA offline.
- Listado de ilustraciones reutilizables por categoría + retratos por ID, sin necesidad de NPC canónicos nuevos.
- Protocolo de snapshots y manifiestos del nuevo dominio; fixtures de versión compatible/incompatible.
- Plan de pruebas físicas MSI/Tab S9+, protocolo de evidencias y tabla PASS/FAIL de los 28 criterios.
- Borrador de adaptación territorial: nuevo pack y contexto, **cero cambios en las reglas universales**, antes de intentar la segunda aldea.

## Condiciones para decidir «lo hago yo» o «lo hace Codex»

**ChatGPT puede asumir directamente**: diseño, transformación de datos, scripts Python acotados, pruebas deterministas estáticas, JSON, documentación, GitHub gestión, prompts, imágenes o UI no crítica. Puede también reparar código limitado y bien cubierto si el riesgo técnico es bajo, pero **sin fingir pruebas nativas que no se hayan ejecutado**.

**Codex es preferible**: cambios de C++ con estado/persistencia, serialización y migraciones, ABI GDExtension, seguridad en autorización, algoritmos de generación/movimiento con muchos invariantes, scheduler, Android NDK/CI, integración con partes de Core compartidas con Star Trek.

**Criterio de riesgo:** si un error puede corromper una partida, filtrar información oculta, alterar el canon o romper ambos videojuegos, se incrementan revisión/aislamiento y pruebas en lugar de optimizar cuota a cualquier precio.

## Detenciones obligatorias

No proseguir automáticamente cuando:
- falta un contrato canónico o hay contradicción normativa;
- una API de CoreRPG compartida necesita alteración no prevista;
- sería necesario crear un segundo WorldState o perder datos al guardar;
- la prueba depende de IA pagada sin consentimiento;
- una fase quiere declarar PASS sin ejecución real en la plataforma requerida;
- es necesaria una modificación de esquema que haga incompatibles partidas anteriores sin migración.

**Meta del reparto:** máxima producción de conocimiento y preparación con ChatGPT; mínimo empleo de Codex, reservado a las decisiones y operaciones donde su entorno de desarrollo/testing aporta seguridad real.