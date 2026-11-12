# D.P21 — Taramin: seis escenas para probar que la ciudad es jugable

**Estado editorial: todas las escenas TAR-E01–E06 siguen TEST_ONLY.** TAR-DP21-06 A aprueba cuatro diseños de arcos condicionales en capítulo 05, pero **no** activa estas seis escenas, personajes, misiones ni sucesos. La implementación es **PENDIENTE**.

**Todas las escenas TAR-E01–E06 son TEST_ONLY**, no misiones activas, ni eventos del mundo. Cada una exige que CoreRPG sostenga hechos, recursos, conocimiento, autoridad y persistencia antes de utilizarse.

## E01 · «No puedes vender lo que no has visto» (N01, N05)
**Entrada hipotética:** alguien pide avalar una entrega cuya calidad es incierta. **Como comprador:** pedir inspección o declinar. **Como ayudante:** confesar el límite de lo conocido sin revelar datos privados. **Como autoridad:** no se inventa infracción por desconfiar. **Resultado válido:** prueba que cambia una oferta o negociación; **inválido:** inventario materializado por frase de IA. **Persistencia:** credibilidad de declaraciones cuando la mecánica exista.

## E02 · «El remiendo y la salida» (N02, N07)
Una pieza reparada podría no estar lista. **Como cliente:** decidir si espera o busca alternativa efectivamente existente. **Como trabajador:** explicar riesgo y negarse a garantizar lo inseguro. **Como tercero:** comprobar que el bien y el oficio existen. **Finales:** entrega apta, retraso aceptado o encargo rechazado; nunca un naufragio automático.

## E03 · «Para beber o para limpiar» (N03, N04, N09)
Se simula una limitación de agua **solo si** el sistema tiene una fuente, reserva y derecho de acceso. **Como familiar:** defender cuidados. **Como operario:** explicar necesidad de higiene. **Como intermediario:** negociar uso proporcional sin legislar. **Finales:** pacto, espera, consulta competente, no magia. **No se declara que Taramin esté bajo sequía permanente.**

## E04 · «La dirección que no existe aún» (N08, N10)
Un viajero describe un cruce entre brazos del Thalen. **Como explorador:** registrar la afirmación como hipótesis. **Como testigo:** decir «no lo sé» si no conoce el trayecto. **Como agente civil:** impedir que un rumor se convierta en orden oficial. **Final:** falta de ruta conocida o evidencia validada en un futuro mapa; **no se construye un puente**.

## E05 · «Una deuda escrita, una deuda recordada» (N06, N05)
Un recado y un acuerdo discrepan. **Como acreedor:** aportar pruebas; **como aprendiz de escribanía:** leer literalmente sin suplantar a una autoridad; **como deudor:** discutir términos. La escena no sentencia ni altera cuentas reales sin ledger validado. Puede acabar con rectificación voluntaria, negociación o remisión.

## E06 · «No quiero seguir el oficio» (N05, N01, N03)
Una persona próxima al mundo pesquero solicita aprender otra función. **Como solicitante:** explicar capacidades y tiempo; **como posible mentor:** decidir con recursos reales; **como cuidadora:** examinar necesidades del hogar. Ninguna rama asigna automáticamente mentor, salario, escuela obligatoria ni obligación familiar. La historia sigue viva aunque se rechace el aprendizaje.

## Prueba transversal

Un mismo hecho ha de narrarse de modo distinto según la información y responsabilidad del personaje: escuchar una discusión, poseer el bien, revisar su estado o intervenir por competencia no son equivalentes. La IA nunca crea por sí sola productos, salarios, sanciones, rutas, puentes, sucesos o recuerdos. Las escenas solo son semillas para D.P25 y posteriores integraciones.
