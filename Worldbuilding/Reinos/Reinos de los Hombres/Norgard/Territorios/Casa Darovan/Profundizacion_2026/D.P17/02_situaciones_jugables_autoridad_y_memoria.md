# D.P17 — Interacciones jugables, causalidad, autoridad y memoria del mundo

**Rescate editorial y arquitectónico 11/11/2026. Estado: ESPECIFICACIÓN CONCEPTUAL, NO C++ EJECUTADO NI ACTUALIZACIÓN DE API.**

D.P17/01 inventaría 57 namespaces de referencia y 24 situaciones TEST_ONLY. Aquí se explica **cómo se convertirían en una experiencia de rol reconocible**, sin fingir que CoreRPG dispone ya de todos esos servicios. La fuente técnica D11 sólo empaqueta identidades y referencias del territorio, no mecanismos de ciudad, propiedad, rutas y relaciones.

## 1. La regla esencial: la IA no rellena el mundo cuando no sabe

El jugador puede decir «Quiero ir desde Veldora a Taramin», «¿quién me vende sal?», «quiero entrar en La Vena» o «¿qué hay detrás de aquella puerta?». Ninguna frase añade por sí sola una carretera, tienda, sal, acceso autorizado o habitación.

El sistema debe distinguir cuatro resultados:
- **HECHO:** hay evidencia canónica o WorldState de lugar, persona u objeto.
- **HIPÓTESIS:** alguien cree o afirma algo que puede ser falso; se conserva su fuente.
- **POSIBILIDAD DE JUEGO:** una acción puede intentarse bajo precondiciones, con capacidad y consecuencias.
- **DESCONOCIDO:** falta dato suficiente; el narrador puede orientar una investigación o describir percepción sin convertir el silencio en realidad.

El canon authored establece definiciones; el WorldState ejecutado establece qué existe y ha sucedido. Una propuesta o fixture TEST_ONLY no entra en ninguno de esos campos por estar en Git.

## 2. Información mínima de una operación futura

**Modelo conceptual; NO nombres de métodos ni API publicada.**

| Dato | Propósito | Límite |
| --- | --- | --- |
| Identidad del intento | Evitar aplicar una compra, traslado o daño dos veces | Un ID estable permite reconocer reintentos |
| Actor, rol, posición | Saber quién hace qué y dónde | El narrador no teletransporta al avatar |
| Referencias de objetivo | Bien, lugar o persona existentes | ID persistente; nombre mostrado no es EntityId |
| Estado previo | Stock, dinero, propiedad, salud, disponibilidad | UNKNOWN no se reemplaza por una cifra razonable |
| Evidencia y permisos | Fuentes, conocimientos, normas y acreditaciones | Rango no confiere omnisciencia |
| Conectividad | Medio, accesos y restricciones físicas | Relación comercial no significa carretera |
| Resultado | Rechazo, espera o mutación legitimada | Sólo el motor autorizado aplica cambios |
| Historia posterior | Evento, consecuencias y visibilidad | Guardar y reanudar no duplican efectos |
| Relato filtrado | Lo que puede contar la IA | No revelar información privada del mundo |

## 3. Cinco casos jugables desarrollados

### C-01 — Comprar metal en Treihord

**Escenario sintético:** el jugador pregunta por una pieza de plata ofrecida en El Peso. El relato puede describir la Plaza de las Balanzas; no inventa al vendedor ni la pieza.

**Preparación:** persona/tienda perceptible, bien con estado/origen/propiedad/posición, precio efectivamente ofrecido, fondos válidos, permiso para examinar y habilidad si se precisa.

**Secuencia:** preguntar → recibir sólo información conocida por interlocutor → examen autorizado → contraste de peso o certificación con recursos reales → negociación → validación legal y de fondos → intercambio atómico de bien y pago → persistencia de inventarios y memoria.

**Ramas:** si vendedor y bien existen, se permite compra válida. Si el propietario no autoriza, puede haber diálogo pero no transferencia. Si no existe el bien, debe informarse de la incertidumbre, sin compra ficticia.

**Conocimiento:** un testigo presente puede recordar lo observado; nadie conoce la transacción por contagio automático.

### C-02 — Paquete retenido en Veldora

**Escenario:** un comerciante dice que su lote exterior no ha llegado al almacén. Hay que distinguir llegada, papeles, inspección y traslado.

**Preparación:** embarcación/carga, custodio, procedencia, autoridad de aduana **de Corona**, instalación acreditada, ocupación y posible compromiso contractual.

**Resolución:** si una inspección exterior legítima está pendiente, el traslado espera o se rechaza. Concluida, todavía necesita capacidad y trayecto real. No se inventa tasa ni se crea aduana entre Grandes Casas.

**Investigación:** diferentes testigos conocen diferentes tramos del proceso; ni la IA ni el jugador leen contabilidad reservada por preguntar. El lote retiene identidad a través de cambios de custodia.

**Guardado:** si el usuario sale durante la espera, al reanudar no se liberan ni descuentan los bienes dos veces.

### C-03 — Pesca y conservación en Taramin

**Escenario:** una captura existente llega a la zona de actividad pesquera principal, cuando su posición real esté definida. No se elige arbitrariamente uno de los brazos del Thalen como navegable.

**Preparación:** persona, herramienta y embarcación cuando proceda, capacidad de faena, captura realmente obtenida, estado de conservación, punto de descarga reconocido, propiedad, comprador existente.

**Resultado:** demora y conservación afectan utilidad o valor sólo según reglas reales; ninguna venta es automática. Un producto que no se vende no desaparece sin causa, y una cura inventada no salva el lote.

**Conocimiento:** quien examinó el pescado puede saber su estado; quien lo vio pasar no necesariamente conoce peso u origen.

### C-04 — Refugio ante mal tiempo en Syvaris

**Escenario:** una embarcación solicita abrigo en la bahía principal ante episodio de mal tiempo **instanciado**, no creado para justificar el relato.

**Preparación:** ubicación, clima, estado de nave, riesgo, instalaciones/capacidades existentes, roles civiles y órdenes de Armada Real.

**Competencia:** un oficial de Norgard manda su personal naval, no todo hogar o comercio; la guardia Darovan atiende seguridad civil. Toda requisa o detención necesita autoridad conforme a la ley común.

**Resultado:** se concede refugio si hay condiciones, espera cuando no hay capacidad o rechazo motivado. No hay «puerto infinito».

**Información:** desde la costa se puede ver una vela sin conocer misión, tripulación o carga privada.

### C-05 — Intento de acceso a La Vena, Treihord

**Escenario:** el jugador intenta entrar en la galería fortificada Crisol–Bóveda, cuya existencia es canónica y su acceso restringido.

**Preparación:** puerta y localización real, credencial efectiva, finalidad y autorización de responsable competente, vigilancia y estado de cierre.

**Resultado:** una conversación informal no abre el acceso. Una acreditación válida permite sólo tránsito dentro de su alcance; el intento ilegal no equivale a éxito. El guardia no revela secretos que no conoce.

**Persistencia:** permisos, uso y consecuencias sobreviven al guardado cuando exista el sistema real.

## 4. Vida social que permanece entre sesiones

**Residencia y familia:** una persona se traslada. Parentesco, convivencia, titularidad, obligación de cuidados y amistad son relaciones distintas. El cambio de habitación no transporta propiedad ajena ni cambia apellido; requiere derecho de ocupación y movimiento real.

**Aprendizaje y empleo:** una artesana de Veldora abandona un puesto para aprender otra actividad. Conserva experiencia, memoria y carácter. Cambiar oficio no genera vacante, mentor o empleo por sí solo.

**Rumor y reputación:** una barquera de La Ribera oye acusación sobre alguien de La Costra. Puede transmitirla sólo con contacto y atención, señalando a quién se la oyó. Un rumor no modifica culpabilidad jurídica ni obliga a un individuo a actuar conforme a prejuicios.

## 5. Estados mínimos y seguridad del guardado

**INTENCIÓN → EVALUACIÓN DE PRECONDICIONES → RECHAZADA / PENDIENTE / RESUELTA → DELTA AUTORIZADO → REGISTRO → VISIBILIDAD → NARRACIÓN.**

- Rechazo: razón identificable y **cero cambios materiales**.
- Pendiente: conservar petición sin inventar proveedor o reserva.
- Resuelta: transferencia/daño/traslado se realiza en conjunto, exactamente una vez, con eventos registrados.
- Reanudación: no repetir un efecto ya comprometido ni perder un intento pendiente.
- Rectificación de un hecho: requiere nueva acción autorizada; que la IA cambie de opinión no borra gastos, daños ni memoria.

Este procedimiento **es una exigencia de diseño**, no prueba de que CoreRPG actual publique esas capacidades.

## 6. ¿Qué sabe cada personaje?

| Observador | Puede conocer | No recibe automáticamente |
| --- | --- | --- |
| Jugador en plaza | Lo que percibe, le dicen o lee con acceso | Contabilidad secreta o causa real de un rumor |
| Guardia de acceso | Órdenes y permisos de su servicio | Toda la seguridad interior de La Bóveda |
| Fiscalizador de aduanas | Expedientes bajo competencia y cargas inspeccionadas | Pensamientos ajenos o cualquier asunto civil |
| Navegante en Syvaris | Mar aparente, instrumentos y órdenes propias | Misión secreta de otro buque |
| Persona del hogar | Recuerdos, acuerdos y observaciones individuales | Bienes, secretos y lealtad automática de parientes |
| IA narradora | Contexto filtrado por Core y Context Builder | Poder para alterar WorldState o ver información omnisciente |

La diferencia entre realidad y creencia es una mecánica importante: alguien puede equivocarse **sin cambiar la verdad del mundo**.

## 7. Pruebas futuras y relación con D11

D11 ya dispone del paquete de identidad 0.1.0 de Darovan con cinco ResourceDefinitions, sidecar de procedencia y un smoke C++ de catálogo/binding/save/load **sintético**. Eso **no demuestra** transporte, trabajo, fiscalidad o comercio simulado.

Cuando se implemente de verdad, las pruebas deberán demostrar:
1. Rechazo sin mutación de compra de bien inexistente, cruce no acreditado o La Vena sin permiso.
2. Atomicidad de stock, propiedad y pago; protección contra recepción duplicada.
3. Guardar/cerrar/reanudar conservando lotes, pendientes y relaciones sin regenerar actores.
4. Aduana exterior en Veldora, nunca entre Casas; Armada de Norgard, nunca Darovan.
5. Los NPC no revelan lo que no saben y la IA no crea hechos ni sentencias.
6. Determinismo por estado/semilla/versión con migración segura.
7. Pruebas de integración reales por separado en Windows MSI y Galaxy Tab S9+; APK compilada no significa prueba física Android.

## 8. Cierre de alcance

D.P17/01 conserva la cobertura conceptual y los escenarios adversariales; este segundo documento define secuencias jugables y resultados observables. **Se completa D.P17 como especificación de diseño**, no como implementación. La integración futura pertenece a una fase técnica diferente y **no es requisito para empezar el trabajo creativo D.P20**.
