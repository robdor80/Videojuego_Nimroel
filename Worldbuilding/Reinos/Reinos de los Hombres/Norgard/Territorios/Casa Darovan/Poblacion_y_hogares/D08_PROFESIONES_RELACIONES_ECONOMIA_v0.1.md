# D08 — Ocupaciones, trabajo, economía doméstica y recursos v0.1
**Estado:** perfil funcional basado en D04/D05/D06/D07 y contratos Nimroel Core/Norgard. No crea puestos, gremios, NPC, salarios, tasas, oficios exclusivos o edificios.

## Separaciones obligatorias
`Profesión` = capacidades aprendidas y trayectoria, `empleo` = vínculo actual `EMP`, `puesto` = función/plaza real y dotada, `aprendizaje` = proceso `APR`, `tarea doméstica` = `CHORE`. Propietario, responsable, trabajador, maestro y vendedor son roles que pueden coexistir sin confundirse. Un desempleado conserva competencias. Vacante no crea candidato; muerte o ausencia no teletransporta sustituto.

## Contextos profesionales de Darovan
| Actividad funcional | Apoyo territorial autorizado | Límite |
|---|---|---|
| Minería y traslado de mineral | Valkram–Treihord, D04 | No se fijan nuevas minas, cuadrillas ni aforos |
| Fundición, ensayo y artesanía metalúrgica | Treihord, El Crisol | No acuña moneda; no duplicar ceca Hallheim |
| Agricultura, ganadería y abasto | Cadena de alimentos D04; modelos D06 condicionados | Parcelas, rendimientos y ganado no acreditados por unidad |
| Comercio exterior, talleres y almacenes | Veldora, D04/D07 | Aduana exterior, no entre Grandes Casas |
| Pesca y transformación básica de productos marinos | Taramin, Syvaris, D04/D07 | Sin caladeros, flotillas, capacidad o navegación Thalen inventados |
| Transporte y logística | D05 | Oferta de carbón Azurios no acredita itinerario terrestre; barcazas Belara solo someras |
| Oficios domésticos, reparación, cuidado y curandería | Norgard rural y Punto 9 | Profesionales concretos, talleres y curanderas deben verificarse |

Las familias profesionales del JSON son **etiquetas técnicas** de demanda/capacidad, no nuevos estamentos, gremios u obligaciones exclusivas. Una localidad puede importar servicios; no todos los asentamientos tienen profesionales distintos.

## Condiciones laborales
`EMP` consume disponibilidad, salud, turnos, habilidades, lugar y recursos. `APR` exige mentor, práctica supervisada y evidencias; tiempo transcurrido ≠ maestría. En trabajos mineros, industriales, pesqueros o de navegación, aplicar capacidad, riesgo y normas existentes. El trabajo familiar respeta edades y esfuerzo real. No fijar jornadas universales, número de trabajadores o equivalencias automáticas por vivienda.

## Presupuesto lógico e inventarios
Cada hogar puede necesitar alimento, agua, abrigo, cuidados, alojamiento, herramientas y tiempo. Las entradas posibles (no cuantificadas) proceden de trabajo, venta, transferencias, producción autorizada, ayuda o recursos propios; salidas de consumo, compra, alquiler, reparación, transporte y obligaciones legales. `TXN/OBL/LED` prohíbe doble gasto, pago sin recursos y registro que cree saldo; `OWN` separa propietario, poseedor, custodio y emplazamiento; `FOOD` exige lote, estado, titular, conservación y stock real. Un hogar no posee automáticamente todo el inventario de sus miembros. La moneda es la de Norgard Defaults; D08 no añade precios ni salarios.

## Cobertura dinámica
`Demanda → ¿persona disponible y competente? → ¿herramientas/espacio/materia prima? → ¿régimen de propiedad y pago válido? → ¿acceso físico probado? → ¿capacidad efectiva y espera? → atender o registrar déficit`.
El resultado puede ser `UNKNOWN`, `sin servicio local`, `pendiente` o `insatisfecho`; ninguno habilita al generador para fabricar un establecimiento.

## Vínculos y fronteras
Treihord/Veldora/Taramin/Syvaris conservan sus énfasis, sin inferir profesiones únicas ni cuotas demográficas; D06 solo perfiles candidatos de aldea/pueblo/villa/enclave. Todo puesto individual, salario concreto, propiedad, saldo, stock o contrato persistente necesita datos del World State y API efectiva en etapa de implementación, no basta validar JSON.
