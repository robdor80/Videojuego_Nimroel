# Nimroel RPG — Política de IA y distribución de funciones

**Origen de la política de modelos:** 17/10/2026. **Revisión funcional aprobada por el autor:** 20/10/2026. **Estado:** decisión arquitectónica aprobada, implementación narrativa en laboratorio; **NO es integración de gameplay ni CoreRPG**.

> Esta revisión prevalece sobre la **asignación de papeles narrativos** contenida en documentos antiguos. Las pruebas y decisiones históricas de NIM-03/04/05 se conservan como evidencia, sin reescribir hechos pasados. La PR #23 no debe activar proveedores pagables ni fusionarse sin aprobación humana.

## 1. Tres IA con responsabilidades diferentes

| Inteligencia | Entorno | Responsabilidad | Cuándo participa |
|---|---|---|---|
| **Luna** — `gpt-6-luna` | API OpenAI facturable, durante la partida | Diálogo de NPC **y consultas puntuales fuera de personaje al Máster** sobre una escena ya establecida; respuestas breves, naturales y económicas | Conversación, aclaración de observaciones, preguntas de detalle, sin recrear toda la escena |
| **Sol** — `gpt-6.1-sol` | API OpenAI facturable, durante la partida | **Máster narrativo principal**, presentación inicial rica y detallada de escenas nuevas, y narración de cambios o acontecimientos importantes autorizados | Al descubrir una escena o ante un cambio narrativo significativo; **no en cada pregunta ni movimiento menor** |
| **ChatGPT Plus** — conversación del autor | Suscripción ChatGPT, **fuera de la partida** | **Super IA de creación y preparación de contenido**: recibir ZIP con contexto relevante + encargo del autor; analizarlo, proponer y generar archivos estructurados para validación e importación | Operación manual, bajo solicitud del autor; no llamada embebida al juego |

**CoreRPG no es una cuarta IA.** Es la **única autoridad** del estado del mundo, acciones, consecuencias, visibilidad, conocimiento de NPC y persistencia. Ni Sol, ni Luna, ni ChatGPT pueden alterar directamente ese estado. Godot 4.7.2 es el Host 2D de Windows x64 y Android ARM64.

### Luna: dos voces, autoridad nula

- **En personaje (NPC):** encarna a un personaje concreto usando únicamente el conocimiento y datos autorizados de ese NPC. No conoce secretos del Máster ni respuestas no accesibles a ese personaje.
- **Fuera de personaje (consulta al Máster):** resuelve una pregunta breve del jugador basada en la ficha autorizada de la escena y su percepción, no en conocimiento oculto de NPC o del mundo.
- Estas rutas se distinguen por **intención y estado conversacional**, no porque el jugador deba usar comandos especiales; el enrutador no debe confundir una consulta al Máster con algo que el NPC oye o recuerda.
- Dato desconocido ≠ dato negado: si no consta el olor de una cocina, Luna no puede concluir que «no huele a comida».

### Sol: Máster de escenas, no árbitro del mundo

- Recibe de CoreRPG una ficha cerrada de hechos y percepciones **autorizados para el jugador**, junto con continuidad relevante. Narra con riqueza literaria **sin inventar hechos persistentes ni revelar datos fuera de visibilidad**.
- Controla presentación, estilo y ritmo: escenas iniciales pueden ser extensas; el lenguaje debe sonar a Máster de rol de mesa, no a inventario ni a prosa artificiosa.
- Una nueva escena relevante o evento **validado por CoreRPG** puede reclamar a Sol; preguntas de detalle posteriores normalmente corresponden a Luna.
- La narración de Sol es **una representación literaria, no el registro canónico**. Los hechos del mundo nunca se extraen de ella para escribir en CoreRPG sin validación.

## 2. ChatGPT Plus: creación externa mediante ZIP

El juego podrá preparar un **ZIP exportable** de información *necesaria y autorizada* para un encargo: lore, reglas y esquemas pertinentes, objetivos, estado autorizado de la partida si procede, contexto útil y especificación de versión del contenido. **No exportar claves API, tokens, datos privados innecesarios o secretos no autorizados.** No presuponer que es seguro incluir «todo» sin filtrar.

1. El **autor** exporta el ZIP y lo envía manualmente a una conversación de ChatGPT Plus, junto con su requerimiento.
2. ChatGPT analiza el contenido recibido y genera una propuesta **revisable**: archivos JSON/documentación/recursos admitidos por un contrato de importación, con manifiesto, referencias, esquema y trazabilidad.
3. El autor descarga el paquete y ordena **una importación explícita**. El juego comprueba formato, versión, nombres y rutas permitidas, hashes, referencias, dependencias, canon, duplicados y conflictos; primero realiza una simulación/preview y pide aprobación.
4. **Solo el mecanismo validado del juego/CoreRPG** incorpora lo autorizado. Fallo de validación = rechazo sin efectos parciales; no ejecución de código arbitrario del ZIP ni acceso libre al disco.

**Límite comercial/técnico:** ChatGPT Plus **no es una API** y no permite realizar llamadas programáticas gratis desde Godot. Este circuito requiere intercambio manual y está sujeto a los límites de la suscripción; las operaciones en esta conversación **no consumen el saldo de la API del videojuego**. El exportador, validador e importador automáticos **son diseño futuro, no funciones implementadas en la PR #23**.

## 3. Proveedores técnicos de NIM-04 frente a roles narrativos

La PR #23 contiene cambios reales de compatibilidad y tests en `Tools/NIM04/provider_proxy.py` y Godot. Ese broker es **solo un clasificador diagnóstico** (`observar`, `desplazarse`, `dialogar`, `otro`); **NO es el enrutador narrativo Sol/Luna**, ni voz NPC, ni consultor de escena, ni pasarela de ChatGPT Plus.

| Perfil histórico del laboratorio NIM-04 | Principal configurado | Alternativa solo con consentimiento |
|---|---|---|
| `simple` | `gemini-3.5-flash-lite` | `gpt-6-luna` |
| `complex` | `gemini-3.8-flash` | `gpt-6.1-sol` |

- Se **conserva** esta tabla de diagnóstico y sus pruebas offline. No cambiar silenciosamente `ROUTES` ni activar gasto al aprobar los **roles narrativos**; Gemini **no está designado** por esta revisión para sustituir a Luna o Sol en la narración.
- La posibilidad histórica de Gemini gratuito y fallback por clase se mantiene **en estudio / issue #29**, **no implantada como ruta narrativa de producción**. Cualquier decisión posterior sobre integrar Gemini en gameplay requerirá aprobación expresa y pruebas específicas de calidad, latencia y coste.
- El acceso OpenAI exige autorización explícita; `NIMROEL_ENABLE_FALLBACK=0` y `NIMROEL_OPENAI_CONSENT=0` por defecto. Cupos por proceso **no son** límites monetarios de facturación. No hay autorización para gasto automático de producción.
- **Mistral está excluido** de rutas activas; pruebas pasadas solo son historia.
- Los identificadores son fijos y revisados; no utilizar alias flotantes ni reemplazar Luna por un ID no publicado.

## 4. Qué se ha comprobado realmente

- **20/10/2026:** ensayos API de laboratorio `gpt-6-luna` como Taren (NPC) y `gpt-6.1-sol` como Máster, en escenario **ficticio** «Linde del Vado», con mundo mock no canónico. En V2, **10/10 llamadas**: cinco Luna y cinco Sol; en el ensayo posterior A/B de Sol, **6/6 llamadas**. Ambas pruebas muestran funcionamiento de API/roles experimentales, **no fiabilidad en producción ni compatibilidad CoreRPG/GDExtension**. Evidencia detallada en issue #29.
- **20/10/2026:** diagnóstico real del broker de `gpt-6-luna` y `gpt-6.1-sol` desde MSI también registrado en #29. Una prueba de clasificación no acredita narrativa.
- El perfil «Máster» del A/B **no queda declarado definitivo**: la mejora fue irregular, por lo que ritmo e instrucciones narrativas requieren iteraciones controladas.
- **No** se han probado: importación ZIP al juego, acceso automático a ChatGPT Plus desde el juego, persistencia de conversaciones en CoreRPG, generación contextual plena ni límites monetarios robustos de pagos.

## 5. Condiciones para integración posterior

1. **Autoridad:** CoreRPG decide estado, reglas y observaciones; Context Builder (sistema 62) genera vistas player-safe y vistas NPC separadas. La validación (65) protege las salidas y la capa de acciones. Jamás confiar en el texto de un LLM para decidir cambios del mundo.
2. **Enrutado:** sistema 63 decide entre `npc_dialogue` (Luna), `master_query` (Luna), `scene_introduction` (Sol) y `significant_event` (Sol), sin invocar IA para UI, consultas puramente locales o movimientos triviales. Son **contratos previstos, no endpoints implementados**.
3. **Gasto y secretos:** sistema 64 deberá aplicar consentimiento, presupuesto en moneda por periodo, corte real, telemetría sin datos privados e idempotencia. No guardar credenciales en EXE/PCK/APK/repositorios. Requiere gateway seguro antes de llamadas desde Android.
4. **Conversaciones:** NPC no debe aprender automáticamente lo que se preguntó *off the record*; la escena narrada por Sol no se convierte en fuente canónica. Contexto acotado y protección de inyección en ZIP y prompts.
5. **ChatGPT Plus:** generación externa nunca ejecutable automáticamente ni vinculada a cargos de API; todo paquete debe pasar por contrato versionado, validación y aprobación del autor.

## 6. Trazabilidad histórica y sistemas relacionados

- **Sistema 44:** diálogo NPC — Luna. **58:** voz local sherpa-onnx (separada de los LLM). **62:** contexto/visibilidad. **63:** selección de la función narrativa. **64:** presupuesto. **65:** validación. **66:** objetivos. **67:** Máster y coordinación narrativa. **68:** propuesta de cambios y validación. **69:** director de partida. Ninguno sustituye a CoreRPG.
- **NIM-05:** PR #22 fusionada; TTS Godot MSI y teclado Android comprobados. Las mejoras de pronunciación (issue #28) y voz de NPC quedan para otra fase.
- **NIM-06:** integración CoreRPG/GDExtension independiente de esta PR; mantener sin efectos sobre ramas existentes.
- Referencias: [catálogo JSON versionado](catalogo_modelos_nimroel_2026-10-17.json); [registro de NIM-04](../NIM-04_PROVEEDORES_Y_PRUEBAS_17-10.md); issues [#28](https://github.com/robdor80/Videojuego_Nimroel/issues/28) y [#29](https://github.com/robdor80/Videojuego_Nimroel/issues/29).

**Cierre de esta actualización:** la política de las tres IA queda **documentada**, pero **ninguna ruta narrativa, importación ZIP ni gasto automático se activa por fusionar esta documentación**.
