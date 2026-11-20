# NIM-08 P04 — Traspaso controlado a NIM-09

**NIM-09 NO iniciada.** El presente traspaso fija precondiciones y trabajo permitido una vez el autor lo autorice. Repositorio y rama de NIM-08 permanecen aislados; no fusionar de oficio.

## Condiciones mínimas de entrada NIM-09 (sin decisiones fundamentales pendientes)

1. Partir de la versión aprobada de Docs/NIM-08-19/01_PLAN_MAESTRO_V001.md y del ADR NIM-08, usando la matriz original como referencia única de IDs.
2. Inventariar las 34 fuentes de ContentPacks/treskal-villages/authoring/source-lock.json, la selección por anchor y el modelo V1; no aplicar reglas de Pueblos como si fuesen Aldeas. Registrar los SHA de los textos vigentes y cualquier delta respecto a revisión 35c9d22; el autor decide canon.
3. Mantener el pack existente 0.1.0 y el Content Contract Core 0.1.0 intactos durante el diseño. Proyectar una **nueva edición** de datos si es imprescindible; nunca reescribir a mano los nueve archivos firmemente bloqueados de I4.
4. Fijar versión de cada esquema, etiquetas CANON/DATOS_OPERATIVOS/TUNING_EXPERIMENTAL, conversión por campo, source pointer, normalización, serialización SHA-256 y rechazo de referencias huérfanas.
5. Conservar el pin CoreRPG 4f2828 y el Godot 4.7.2 fijado. No introducir JSON Schema remoto, red, IA pagada o cambios de librería sin autorización.

## Orden NIM-09 P01–P04 recomendado

- **P01:** inventario de fuentes; matriz cada campo -> path/anchor/hash -> contrato; resolver posibles contradicciones con el autor, **no inventar parámetros canónicos**.
- **P02:** diseñar authoring declarativo, modelo de versiones/manifiestos, IDs semánticos y reglas de validación. Ajustar los tres esquemas NIM08 cuando se compruebe su viabilidad, bajo versión nueva si se rompe compatibilidad.
- **P03:** extractor + pack builder/checker deterministas (preferentemente Python sin Codex), tests positivos y negativos, dos ejecuciones independientes byte a byte; rechazar fuentes no autorizadas, alteraciones invisibles y edición del pack generado.
- **P04:** fixture de región explícita, selección V1, reglas de hogar/capacidad y oficios como datos, sin afirmar que ya existen edificios, personas ni órdenes en Core; entregar un pack de ejemplo **no mutador** y manifiesto de evidencias.

**Puerta NIM-09:** mismo input/versiones -> mismos bytes y SHA-256; 0 referencias huérfanas; comparación de canon aprobada; segunda reconstrucción limpia; esquema y Content Contract compatibles; matriz 28 IDs conservada. Todavía no exige un mundo Core ni gráficos.

## Bloqueos nativos posteriores: preparados, no autorizados

| Fase | Contrato que recibe | Trabajo nativo que no debe fingirse |
| --- | --- | --- |
| NIM-10 | generación/region, servicios, layouts, bindings | geometría/grafo, constraints 100 seeds, bootstrap Core |
| NIM-11 | hogar, residentes, identidad, oficios | materialización persistente y población sin duplicados |
| NIM-12 | localizaciones/edges/costes | navegación real, vista por observador y permisos |
| NIM-13 | objetos/condición/propiedad/custodia | operaciones atómicas sobre dominio material |
| NIM-14 | clock/work_orders/servicios | scheduler y taller con tiempo y materiales |
| NIM-15 | Knowledge/vista segura | transmisión por fuente, memoria y diálogo local |
| NIM-16 | encargo opcional A/B/C | orquestador derivado de mundo real, sin script universal |
| NIM-17 | proyección UI Godot | interfaz 2D offline/Android con flujo nativo |
| NIM-18 | formato de estado nuevo | guardado completo compatible, rollback, migraciones |
| NIM-19 | auditoría V001 | 28 evidencias, EXE/APK físicos y segundo contexto |

Para la programación compleja que efectivamente se delegue más adelante: **Modelo GPT-6, razonamiento Alto**; ticket preciso con versión/sha, paths permitidos, fallos negativos, tests/migración de dos consumidores y PR Draft. Ningún encargo se lanza en NIM-08.

## Criterios de coste/seguridad

ChatGPT realiza extracción documental, schema, manifest, Python, fixture, diseño UX, checkers, revisión y auditoría; Codex solo si la complejidad/seguridad de Core C++/GDExtension y persistencia lo justifican. Nunca sacrificar garantías de autorización, reproducibilidad ni save por ahorrar cuota.

La arquitectura de Core genérico puede interesar a Star Trek (tripulación, rutas de cubiertas, operaciones de mantenimiento, permisos de informe y PADD), pero **no introducir dependencia Nimroel ↔ Star Trek**. El cambio de Core se plantea como PR separada, con matriz de impacto y autorización del propietario.
