# Nimroel RPG — Política de proveedores y modelos de IA

**Decisión inicial del autor:** 17 de octubre de 2026. **Aclaración sobre Luna:** 20 de octubre de 2026. **Estado:** normativa de proyecto aprobada; implementación y validaciones por modelo, en curso.

## Tabla de intención del autor

| Modo | Clase lógica | Proveedor permitido | Nombre elegido por el autor | ID de API confirmado | Situación |
|---|---|---|---|---|---|
| Free | `simple` | Google Gemini | Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | Confirmado en catálogo oficial; pruebas NIM-03 previas |
| Free | `complex` | Google Gemini | Gemini 3.8 Flash | `gemini-3.8-flash` | Confirmado en catálogo oficial; pruebas NIM-04 previas |
| Pago | `simple` | OpenAI | **La versión Luna más avanzada oficialmente disponible** (actualmente GPT-6 Luna) | `gpt-6-luna` | ID oficial verificado; E2E de diagnóstico NIM-04 previo (17/10) |
| Pago | `complex` | OpenAI | Sol 6.1 | `gpt-6.1-sol` | ID oficial verificado; NO validado aún en el broker NIM-04 |

**Mistral queda excluido completamente de la arquitectura activa:** no crear nuevas integraciones, rutas, credenciales, fallback, interfaz de selección o pruebas positivas de Mistral. Los ensayos anteriores pueden permanecer como **historial archivado** claramente marcado y no deben confundirse con la configuración operativa.

### Decisión definitiva del autor — 20/10/2026: última versión oficial de Luna

El autor aclara que **no exige Luna 6.1**: quiere siempre la versión Luna más avanzada **que esté publicada oficialmente y comprobada para la API**. La designación «Luna 6.1» del 17/10 fue una referencia imprecisa, no un bloqueo de lanzamiento.

- **Selección actual (20/10/2026): GPT-6 Luna, ID fijo `gpt-6-luna`.** Es la versión más avanzada de Luna que muestra el catálogo oficial consultado. No consta un ID público `gpt-6.1-luna`; no inventarlo.
- **Criterio futuro:** cuando aparezca una nueva versión oficial de Luna, revisar catálogo, compatibilidad, precio, permisos y pruebas automatizadas/físicas; actualizar el ID versionado mediante cambio revisado. **No usar aliases flotantes ni cambiar silenciosamente de modelo**, para preservar reproducibilidad.
- **Antecedente comprobado:** NIM-04 validó un diagnóstico real desde Godot Windows con `gpt-6-luna` el 17/10/2026; esa prueba no valida narrativa de NPC, ni uso de CoreRPG, ni futuras versiones.
- El acceso OpenAI sigue siendo **de pago, deshabilitado sin consentimiento expreso**, con fallback desactivado por defecto. Esta aclaración no autoriza ni dispara llamadas remotas pagables.

Fuente de selección actual: https://developers.openai.com/api/docs/models (consulta 20/10/2026).

## Enrutado y responsabilidad

- El objetivo gratuito usa Gemini 3.5 Flash-Lite para tareas ordinarias y Gemini 3.8 Flash para tareas exigentes. El servicio gratuito tiene cuotas/rate limits, **no implica acceso ilimitado**; verificar disponibilidad y términos por cuenta.
- La ruta de pago debe requerir **consentimiento explícito** y controles de coste; nunca es una conversión automática al agotar el tier gratuito sin opt-in.
- El sistema 63 elige capacidades y proveedor; 62 forma contexto acotado/player-safe; 64 vigila cuotas y coste; 65 valida estructuras; 44/66/67/68/69 son consumidores, no autoridades sobre el World State.
- **CoreRPG conserva en exclusiva la autoridad lógica.** La IA interpreta, organiza y redacta propuestas validadas, jamás confirma hechos por sí sola ni altera directamente estado persistente.
- Godot 4.7.2 Standard 2D es el Host de Nimroel (Windows x64 / Android ARM64); el broker actual NIM-04 es un laboratorio Windows, no backend de producción.
- El reconocimiento y síntesis locales aprobados con sherpa-onnx son una capa de voz separada, sin dependencia de los cuatro LLM.
- No incluir claves de API en repositorios, binarios, APK, partidas, telemetría o capturas; si en el futuro se presta el servicio en Android, diseñar gateway y protección adecuados.
- Fallback entre proveedores por clase solo tras autorización y validación; conmutación fail-closed, sin reintentos infinitos y sin facturación silenciosa.
- Mantener IDs en configuración versionada y alias estables internos. Nada de hardcodear modelos como requisitos de las partidas guardadas.

## Alineación con los 69 sistemas históricos

Documento de partida: `Videojuego de Nimroel_CORREGIDO(2).docx` (69 sistemas, ~1431 páginas). Sistemas prioritarios afectados:

| Sistema | Efecto de esta decisión |
|---|---|
| 44 Diálogo y conversación | Consumidor de IA, salida textual opcional y fallback |
| 58 Audio, música, ambientación sonora y voz | sherpa-onnx local; proveedor LLM no sustituye STT/TTS |
| 62 Context Builder | Construye contexto y evita filtraciones; independiente de proveedor |
| 63 Enrutado de IA | Tabla free/pago y resolución real de modelo; Mistral excluido |
| 64 Presupuesto | Free con cuotas, pago con consentimiento y tope monetario futuro |
| 65 Validación de IA | Respuestas estructuradas player-safe y sin mutación autoritativa |
| 66 Objetivo personal | Elegir clase de capacidad; nunca fijar SDK directamente |
| 67 Partida Maestra / Magíster | Estrategia narrativa sobre propuestas y datos validados |
| 68 Master Patch | Replanificación propuesta/validada; nunca escribir hechos sin CoreRPG |
| 69 Director de Partida | Observa/prioriza eventos, no controla persistencia |

El resto de los sistemas conserva los contratos de IA abstractos ya existentes. Este documento prevalece sobre selecciones de proveedor en material anterior **solo respecto a política futura**, no borra evidencia real de pruebas anteriores.

## Evidencia histórica y estado de despliegue

- NIM-04 probó `gpt-6-luna` y `gpt-6-sol` reales desde Godot Windows, ambos como clasificadores diagnósticos; la prueba de Luna corresponde al modelo ahora seleccionado, **pero NO valida** Sol 6.1, posibles Luna futuras ni un máster narrativo real.
- Nueva integración de `gpt-6.1-sol` requerirá regresiones unitarias, CI, prueba autorizada contra API y aceptación humana. La generación/diálogo CoreRPG permanece sin conectar.
- Mistral Small/Medium fueron ensayos históricos; el código actual ya los retiró antes de esta política.

## Fuentes oficiales (verificadas 17/10/2026)

- Catálogo Gemini: https://ai.google.dev/gemini-api/docs/models
- Precios/tiers Gemini: https://ai.google.dev/gemini-api/docs/pricing
- Catálogo OpenAI: https://developers.openai.com/api/docs/models

## Pendientes para cierre definitivo

1. **Decisión Luna resuelta el 20/10/2026:** mantener la última Luna oficial verificada (`gpt-6-luna`), y revisar si aparece una versión más reciente antes de futuras actualizaciones.
2. Comprobar acceso API real a `gpt-6.1-sol` con credenciales privadas y consentimiento del propietario.
3. Completar control de coste robusto y diseño de servicio seguro antes de producción y Android.
4. Revisar la documentación de NIM-04 y los 69/70 sistemas con esta política sin reescribir registros históricos.
