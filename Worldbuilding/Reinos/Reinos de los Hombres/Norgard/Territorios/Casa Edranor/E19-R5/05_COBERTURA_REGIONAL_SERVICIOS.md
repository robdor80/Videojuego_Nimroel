# E19-R5.05 — Red de aldeas, centralidades y cobertura de servicios
## Paridad funcional con Valrik
El método regional de Valrik detecta huecos en molino, curandería, intercambio, herrería y posada mediante red, población servida, capacidad y tiempos reales. Edranor necesita la **misma pregunta**, no la misma lista universal de edificios. E06 y E16 describen capacidades y necesidades; E08 distingue trabajo, servicio y hogar. Ningún servicio nace por corregir una tabla sin un lugar y trabajadores.

## Tres capas separadas
- **Sd (demanda):** un hogar necesita agua, alimentos, herramientas, salud, abrigo, reparación, información o venta de cosecha. Puede expresarse sin identificar proveedor.
- **Sq (cobertura hipotética):** un pueblo podría servir a varias aldeas si existe competencia, derechos, capacidad y conexión. Es una pregunta, no asignación.
- **Sp (cobertura verificada):** proveedor real con `ProviderId`, `BusinessId`, recursos, horario/turnos, accesibilidad Gp, derecho y capacidad. **Actualmente Sp está vacío**.
Un `CT-01` entre Dorth y Lumina NO es servicio ni trayecto. No se asignan tiempos/distancias, ni nodos conectados de ficción.

## Catálogo de necesidades que se cruzará con E15–E17
Agua potable y saneamiento; abrigo/calor; comida y reserva; reparación/herramientas; carpintería/tonelería solo cuando exista; cuidado de enfermos/partos; comercio local y periódico; alojamiento viajeros; administración/justicia competente; mensajería; evacuación; acceso autorizado al bosque; recepción de uva y almacén. No todos requieren un edificio separado; vivienda-taller/taberna-hogar son posibles, pero jamás cuentan dos veces una cama o un trabajador.

## Secuencia de futura coordinación
1. Cerrar parcela y acceso; identificar hogares/actividades que realmente existen.
2. Calcular necesidades por estado/estación; inventariar proveedores certificados.
3. Comprobar competencia, capacidad restante, horarios, acceso legal y distancia **medida** en red Gp.
4. Detectar huecos reales, permitir proveedores nuevos **solo con** recursos, permiso, personal y emplazamiento.
5. Revalidar el equilibrio; persistir vínculos por IDs estables y el cambio de inventarios/turnos.
6. Si un servicio deja de estar accesible, registrar falta o retraso y consecuencias, no teletransportarlo.
La ubicación más bonita no derrota la geografía; la cobertura es causal y puede ser imperfecta.

## Tensiones propias de Edranor
La vendimia concentra mano de obra y depósitos, el mercado anual de Lumina presiona camas/servicios, los tintos de Dorth requieren custodia, la exclusividad de Karsath evita macroindustria, Bosque Alto introduce cupos y derechos, el invierno norte condiciona calor y movilidad. Rodas exige acuerdo de Corona para intercambios y **nunca** se toma como cobertura tributaria de Edranor.

## Pendiente
No se calcula radio de servicio, densidad, multiplicador, probabilidad ni centralidad real sin población, emplazamientos, Gp, inventarios y calendario. En B2 se entrega contrato de restricciones y catálogo de preguntas, no una falsa solución óptima.
