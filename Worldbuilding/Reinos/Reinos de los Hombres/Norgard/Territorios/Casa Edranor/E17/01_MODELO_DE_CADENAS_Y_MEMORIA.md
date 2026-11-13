# E17 — Modelo causal: necesidad, economía, administración y memoria

**Clase de autoridad:** diseño delegado, no hecho canónico, historia consumada ni runtime. Fuente de trabajo: `main` tras E16 (`93499f466cbfb5b920b513b817c6185e727db274`). E18 no se ejecuta en esta fase.

## Cadena condicional general
**Necesidad del hogar → solicitud con identidad → autorización de titular/autoridad → stock real y trabajo disponible → reserva única → vía y agente verificados → entrega con acuse → consumo o servicio → posible mantenimiento → conciliación → memoria con fuente.** El contrato contiene etapas de diseño, no despachos ejecutados. No se presume que todo encargo termine con éxito.

## Capas y agentes de decisión
1. Hogar: necesidad y recursos, pero no genera productores ni censos E26.
2. Negocio: recibe pedido, verifica capacidad, lote, oficio y seguridad; precio/contrato no crea mercancía.
3. Mercado y economía regional: necesidades entre Dorth/Lumina/Karsath/Rodas son hipótesis de interacción, no comercio celebrado ni vías E19.
4. Administración: resuelve competencia, derechos, protección y solicitudes; para Rodas, Corona Aethros.
5. Comunicación: los mensajes no actualizan destinatarios hasta recepción y permiso de lectura.
6. Memoria: distingue solicitud, rumor, prueba, resultado, hecho realmente observado y crónica autorizada; no canoniza pruebas.

## Contrato futuro de evento (solo interfaz)
Identificadores `eventId`, `worldRevision`, `causalParentId` y `sourceRef`; fecha observada relativa al calendario oficial, actor real, rol, autoridad, sujeto/activo georreferenciado, antes/después, lotes afectados, receptor y prueba de acuse. Ausencias: NO mutar. Correlación e idempotencia impiden dos asientos por un mismo evento. El motor concreto, serialización y sincronización se decidirán en E28; E17 no añade formatos persistentes ni tablas.

## Retroalimentación y límites
Una escasez puede solicitar ayuda, pero **no** autocrea proveedor; una avería puede requerir materiales, pero **no** autocrea repuestos; un rumor puede motivar pregunta, pero **no** se transforma en noticia oficial. Si no hay evidencia nueva, el proceso queda `PENDING_EVIDENCE`, preserva su ID y no vuelve a emitir acciones. Cada reintento necesita revision/evento verificable distinto. Horizon sintético de auditoría: 16 pasos como límite del verificador, **no** tiempo diegético.
