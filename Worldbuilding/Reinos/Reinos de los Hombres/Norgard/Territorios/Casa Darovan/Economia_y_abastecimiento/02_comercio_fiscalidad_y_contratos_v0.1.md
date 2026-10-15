# D04 — Economía formal, fiscalidad y contratos v0.1
**Estado:** compatibilidad documental, NO implementación fiscal nueva. Autoridad: Nimroel Core/08_Economia_formal; Norgard Defaults/02_Gobierno_y_economia E2 y fiscalidad; navegación E7.

## Jerarquía obligatoria
`Core (transacción/obligación/libro real) → Norgard Defaults (moneda, impuestos, aduana, autoridad) → Darovan (instalaciones y actividad autorizada) → localidad → World State`.
Darovan no define un motor comercial alternativo. `TXN` mueve recursos; `OBL` registra obligación con deudor/acreedor/base; `LED` puede diferir de la verdad física. Una anotación no inventa moneda, carbón, metal ni peces. El cumplimiento es persistente y auditable.

## Sistema fiscal único
- La Corona tiene supremacía fiscal y monopolio de acuñación; las Casas administran y recaudan dentro de sus competencias, rinden cuentas y entregan una parte estipulada. **No** porcentaje universal.
- **No hay aduanas internas entre Grandes Casas** por cruzar frontera de Casa; sí puede haber precio, tasa portuaria/mercado/almacenaje o servicio realmente prestado, con fundamento.
- Aduana **exterior** solo cuando mercancía sujeta cruza frontera fiscal externa de Norgard; no asumir régimen aduanero de Elandor (jurisdicción externa de política aún por precisar).
- Captura local descargada en el puerto local no es importación exterior, aunque puede haber tarifa por lonja, desembarco u otros servicios efectivamente utilizados.
- El movimiento oficial de Corona/Armada no se somete a impuestos de Casa; una compra comercial por la Corona conserva transacción y pago legal salvo otra autoridad válida.
- No inventar impuestos por venta cotidiana, peajes universales, tasas a discreción, confiscaciones automáticas ni detección omnisciente del fraude.

## Moneda y lingotes
Moneda común: Clavo (cobre); Luna = **24 Clavos**; Corona = **480 Clavos**. Ceca Real permanente en **Hallheim**, exclusivamente. El Crisol **no** acuña ni posee monopolio monetario. El lingote es activo físico rastreable sin valor facial, con valoración oficial en Clavos si corresponde; ensaye de Crisol no excluye reensaye por Ceca. La tasa de acuñación privada ordinaria del default monetario es **2,5 %**, no impuesto territorial general ni tarifa aplicable indiscriminadamente a los lingotes.
**Propuesta técnica:** en una futura transacción con mineral, lingote o mercancía, separar propietario, origen físico, ubicación, peso/ley comprobados solo si existen, valoración documental, pago real y recibo. No preasignar precios ni salarios locales.

## Responsabilidad documental
- La Casa gestiona minas, fundiciones, Crisol, transporte y registros propios según Treihord canónico.
- La representación permanente de la Corona en Treihord fiscaliza producción y cumplimiento sin asumir administración.
- Los movimientos de alto valor a través de `La Vena` mantienen custodia y discreción; no exponerse como almacén de libre acceso.
- No inventar gremios exclusivos, bancos, contratos individuales, fiscalidad portuaria concreta o competencia militar a partir de este estudio.

## Reglas de validación para D11
Comprobar en transacciones reales, no en perfiles descriptivos: conservación de activos, deudas y pagos parciales, origen/destino, no doble gasto, discrepancia libro/realidad, stock de carbono/madera/metal, remesa, exención, aduana exterior frente a límite entre Casas, continuidad fuera de pantalla; navegación de barcazas y barcos condicionada por calado, tripulación y carga.
**La presente fase no acredita ninguna de estas pruebas runtime.**
