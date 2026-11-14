# E19-R4.07 — Viaje, rumor, mensajería y continuidad del mundo
**Referencia funcional:** Valrik/Treskal, continuidad de viaje y aprendizaje de rutas. R4 describe el modelo, no mueve NPC ni instancia viajeros.

## 1. Conocimiento ≠ geografía ≠ estado
Conocimiento del camino: DESCONOCIDO → OIDO → RECORRIDO → FAMILIAR, con fuente, fecha y fiabilidad. Lo que sabe un mercader no transforma una pregunta CT en camino Gp. Conocer una ruta no informa de barro, corte, obras o vigilancia actual. La información de estado necesita observación reciente, mensajero acreditado o evidencia propia. El jugador puede creer erróneamente que un camino sigue abierto; el mundo no miente para ajustarse a su mapa.

## 2. Viaje con identidad
Un viajero real necesita: actorId, origen/destino válidos, motivo, ruta física legal certificada, modo permitido, inicio, carga o pertenencias, estado, efectos de tiempo/clima y posibilidad de retardo/descanso. No puede aparecer en el destino mientras está en tránsito; tampoco se calcula un encuentro por compartir una etiqueta CT. NPC y jugador solo coinciden cuando recorrido y tiempo lo permiten.

## 3. Orden de despacho de una mercancía
Pedido → reserva verificable → objeto/lote existente → remitente autorizado → tramos de Gp y permisos completos → transportista y medio reales → salida → hitos registrados → incidencia/espera/desvío comprobado → recepción → cambios de stock y custodia. Un encargo fallido no crea infraestructura. Dos pedidos pueden compartir tramo sin duplicar su entidad ni el stock reservado. Un servicio puede ofrecer entrega estimada solo si hay datos, no por promesa de un tendero.

## 4. Mensajería, patrulla y rumor
Un mensajero no transmite instantáneamente noticia de un puente dañado; viaja o usa un canal instalado verificado. Rumores tienen emisor, alcance, transmisión y margen de error. Una patrulla de Casa no adquiere autoridad en Rodas, aunque persiga a alguien hasta la frontera administrativa; deberá regirse por competencia. No hay estaciones, torres ni servicio postal operativo definidos en E05. La presencia de un castillo o la feria de Lumina no implica una estación de posta.

## 5. Viaje y respuesta narrativa
Posibles situaciones futuras: caravana retrasada por barro comprobado, petición de reparación, discusión por servidumbre, ruta indirecta para no dañar Bosque Alto, viñador que no consigue sacar barricas o rumor falso de cierre. El motor entrega a la IA entidades, prueba, estado y conocimiento por actor; **la IA narra, pero no crea camino, puente, mercancía, patrulla o derecho**.

## 6. Cambio de región o descarga de mapa
Una ruta con ID estable no desaparece al descargar celdas 2D. Debe conservar geometría inmutable/versionada, enlaces físicos, dueño/permiso, condición e historial de sucesos. Las estimaciones de un actor pueden caducar, pero no reinician la realidad. Nada de resembrar un puente en cada entrada a zona, ni de multiplicar un convoy al guardar.

## 7. Ejemplo trazable sin afirmar existencia
Si en una futura partida se acredita un camino desde una bodega real de Lumina y el jugador presencia lluvia prolongada, el terreno podría sufrir barro si tipo de suelo, compactación y drenaje lo justifican. Un carretero no sale hasta tener ruta válida y medio. Una noticia transmitida a Dorth llega cuando un portador real lo comunica. Si ese camino nunca fue certificado, **todo el caso sigue hipotético**, no un evento generado por R4.

## 8. Contrato de privacidad y procedencia narrativa
Un NPC conoce solo su observación, comunicaciones recibidas y permisos legítimos; no recibe telemetría omnisciente de todas las rutas. Los mensajes sobre Casa/Corona conservan destinatarios y autoridad. La persistencia técnica es futura E19-TEC/E28; R4 contiene 0 actores en viaje, 0 mercancías despachadas y 0 cambios de World State.