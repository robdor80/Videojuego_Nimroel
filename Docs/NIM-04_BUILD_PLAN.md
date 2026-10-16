# NIM-04 BUILD — Plan autorizado y puertas de aceptación

> **ACTUALIZACIÓN DEL 17/10/2026 — política posterior (prioritaria).**
> El autor define **Free: Gemini 3.5 Flash-Lite / Gemini 3.8 Flash** y **Pago: OpenAI Luna 6.1 / OpenAI Sol 6.1**; **Mistral fuera**. `gpt-6.1-sol` está verificado en el catálogo y es la ruta `complex` propuesta en la rama de actualización; no se ha revalidado en API real. **`gpt-6.1-luna` no figura en el catálogo oficial**: `gpt-6-luna` se conserva únicamente en el laboratorio anterior hasta decisión del autor. Las pruebas previas de `gpt-6-luna`/`gpt-6-sol` siguen siendo históricas; los párrafos originales no deben leerse como la configuración definitiva.
>
> Contrato normativo: [Política de modelos](IA/POLITICA_MODELOS_NIMROEL_2026-10-17.md) · [Catálogo JSON](IA/catalogo_modelos_nimroel_2026-10-17.json).


Fecha de inicio: 2026-10-16. Base verificada: `main` @ `8d27751809f11c1dae1cdeb881a5cf41f11c012d` (NIM-03 PR #19 fusionada). Rama: `feat/nim-04-build`. Estado: **en desarrollo; no autoriza fusión automática**.

## Decisión arquitectónica de proveedores — 17/10/2026

**Decisión definitiva del propietario tras las pruebas reales:** Mistral **descartado y retirado del código operativo**, sin rutas, credenciales o fallback activos. Solo se admiten los siguientes modelos:

| Nivel | Primario gratuito | Respaldo de pago |
|---|---|---|
| `simple` | Gemini `gemini-3.5-flash-lite` | OpenAI `gpt-6-luna` |
| `complex` | Gemini `gemini-3.8-flash` | OpenAI `gpt-6-sol` |

El fallback es **opt-in**, requiere `NIMROEL_ENABLE_FALLBACK=1` y además `NIMROEL_OPENAI_CONSENT=1` para permitir llamadas facturables; tope local de 4 solicitudes OpenAI por proceso de laboratorio. Se preserva la opción de selección directa de OpenAI para pruebas autorizadas, pero no Mistral. El broker no es un motor narrativo; CoreRPG no está conectado ni admite mutación desde proveedores. Los ensayos históricos de Mistral (HTTP 429 en Small y Medium) permanecen documentados en el registro de pruebas como hechos pasados, **no como opciones de uso**. Calidad narrativa real y conmutación real Gemini→OpenAI todavía pendientes de prueba. No autoriza merge de PR #21.

**Nota de trazabilidad:** el alcance y la tabla de «Estado inicial por evidencia» siguientes reflejan el *plan original* aprobado al arrancar la fase, cuando Mistral aún era candidato. Esta decisión posterior lo sustituye; no deben interpretarse esas entradas históricas como arquitectura vigente.

## Procedencia del alcance
No existía un `NIM-04_BUILD_PLAN.md` previo en `Docs/`. Este alcance se concreta a partir de `NIM-03_CIERRE_Y_TRASPASO.md`, `NIM-03_BUILD_PLAN.md` y la autorización expresa de inicio del propietario. No se presenta como un plan anterior encontrado en GitHub.

## Prioridades NIM-04
- **P01 Auditoría**: base/main, continuidad NIM-01/02/03, fronteras CoreRPG y voz, CI y riesgos del teclado Samsung.
- **P02 Proveedores aislados**: adaptador Python de diagnóstico Gemini/OpenAI para Windows, sin secretos en Godot, sin NPC ni acción de mundo, con credenciales por variables de entorno y modelos fijados; llamadas reales solo tras decisión del usuario.
- **P03 Respaldo fail-closed**: configuración explícita, cadena de proveedores por nivel (sencillo/complejo), validación estricta del JSON, controles de tiempos, fallos 429/503/timeout, sin suponer equivalencia de calidad ni ejecutar acciones. Pruebas negativas offline.
- **P04 Host/CI**: ensayo diagnóstico opt-in solo en Windows, conservar modo demo e integración bloqueada por Core; extender smoke/CI/exportaciones Windows x64 + Android ARM64. CI de simulaciones **no es** validación de proveedor real.
- **P05 Preparación del 17/10**: protocolo corto Gemini 3.8 (1 intento mínimo y reintento acotado si procede); el ensayo histórico de Mistral Small/Medium quedó registrado como HTTP 429. Decisión posterior: continuar solo con Gemini gratis y OpenAI de pago, con ambos OpenAI comprobados en Godot. No enviar claves al repositorio ni guardar textos del canon en logs.
- **P06 Regresión pendiente**: descargar APK actualizada, Tab S9+ teclado Samsung virtual y Bluetooth, historial, enviar, ocultar IME y recuperación de layout. **Pendiente de prueba humana**, no bloquea trabajo independiente.

## Definición de terminado y pendientes NO incluidos
- El adaptador `Tools/NIM04/` puede probarse offline y compilarse sin cuentas; no es gameplay.
- Las pruebas reales de Gemini y OpenAI requieren credenciales locales y consentimiento para el envío de texto. La habilitación de fallback y costes debe ser explícita, controlada; no se activa producción ni Android.
- CoreRPG continúa como única autoridad. `interaction_pipeline.gd` mantiene `CORE_NOT_CONNECTED`; no WorldState en Godot/Python, ni narración canónica.
- sherpa-onnx TTS Godot Windows/Android, STT/ASR, puente GDExtension, snapshots cross-arch y narrativa NPC permanecen como trabajos futuros dependientes de contrato nativo, ensayos en dispositivos y otra fase si hace falta.
- No alterar `Worldbuilding/`, otros repositorios ni el canon.

## Puertas de prueba
1. Código versionado en rama exclusiva + revisiones de contratos y seguridad.
2. Unit tests offline positivos/negativos: formato, falta de credenciales, 401/403, 429, 503, timeouts, fallback, circuit breaker, límites y ausencia de mutación.
3. CI del **HEAD final**: Godot headless, pruebas previas, export exe+pck Windows y APK únicamente ARM64. Confirmar artefactos; compilación y exportación no equivalen a arranque físico.
4. Pruebas físicas MSI y Tab S9+ separadas; proveedor real separado de mocks y de la disponibilidad de la clave.
5. PR en borrador **sin merge**, auditoría final y autorización explícita del propietario.

## Estado inicial por evidencia
| Elemento | Código | Servicio real | Dispositivo |
| --- | --- | --- | --- |
| Gemini 3.5 Flash-Lite, NIM-03 | Sí, diagnóstico | Verificado | MSI, intentos dialogar/desplazarse |
| Gemini 3.8 Flash | Petición técnica NIM-03 | HTTP 503 repetido; no verificado | Reprueba 17/10 |
| Mistral Small 4 / Medium 3.5 | Preparar en NIM-04 | No probado | Requiere clave MSI 17/10 |
| sherpa TTS WAV externo | Banco CI Windows | Sí, WAV escuchado | Fuera de Godot |
| Samsung virtual/Bluetooth, ajuste | Sí, test geométrico | No aplica | Nueva APK aún sin prueba física |
| CoreRPG GDExtension / WorldState | No conectado | No | Dependiente de CoreRPG |

Fuentes técnicas externas sujetas a verificación: https://docs.mistral.ai/models/mistral-small-4-0-26-03 ; https://docs.mistral.ai/models/mistral-medium-3-5-26-04 ; https://docs.mistral.ai/inference/model-lifecycle ; https://docs.mistral.ai/admin/billing-usage/usage-limits ; https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training .
