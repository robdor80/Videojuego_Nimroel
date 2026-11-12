# E09 — Hacienda de Casa, Tesoro Real y unidad fiscal

**CANON_REPO:** `sistema_fiscal_y_aduanero_v0.1.md` + `moneda_y_acunacion.md` + E04. Corona autoridad superior; Casas recaudan obligaciones **autorizadas** y remiten parte estipulada. Rodas = hacienda **Corona Aethros**. Hallheim no es dependencia Edranor.

## Catálogo de ingresos — sin generar obligaciones
1. **Contribución territorial** periódica: necesita título, base aplicable, sujeto, periodo, regla autorizada, deuda no satisfecha. No se cobra por cada compra de vino.
2. **Servicios públicos prestados:** puesto de mercado, pesaje, depósito y administración efectiva, solo cuando haya autorización, prestación y tarifa vigente demostrables. Un edificio visual no equivale a servicio.
3. **Aduana exterior:** únicamente ante la **frontera fiscal exterior de Norgard**, bajo autoridad aplicable; el paso Dorth–Lumina, Dorth–Rodas o entre Grandes Casas **no devenga aduana**.
4. **Exacción extraordinaria:** solo orden temporal y causal de Corona, documentada, no recurrente por defecto.
5. **Remesa Edranor→Corona:** obligación con proporción/fecha establecida documentalmente; el porcentaje Edranor y fecha concreta siguen `UNKNOWN`.
6. **Multa judicial:** consecuencia de delito tipificado y sentencia competente, no tarifa creada por Hacienda local.

## Unidad de cuenta
**1 Clavo** base entera; **1 Luna = 24 Clavos**; **1 Corona = 480 Clavos**. Valoración oficial en Clavos para recursos o moneda extranjera, conservando movimiento físico de la especie. Redondeo al entero más próximo, exactamente medio hacia arriba, **solo si existe fórmula legal previa**. Ni Edranor ni Lumina poseen ceca propia; Ceca Real en Hallheim. Precios específicos de tintos/blancos/Karsath, tipo tributario del vino, porcentajes y fechas `UNKNOWN`.

## Libro y evento — contrato PROPUESTA
`obligationId`, `legalAuthorityId`, `competenceLocalityId`, `taxpayerId`, `sourceEventId`, `basis`, `taxRateOrFeeRef`, `grossAmountClavos`, `resourceKind`, `resourceQuantity`, `paymentEventIds`, `receiptId`, `remittanceRef`, `auditTrail`, `status`. Requiere idempotencia por obligación y prueba del pago en World State; recibo sin entrega no supone cobro. Auditar posible doble devengo y refundir correcciones como asientos trazables, sin borrado histórico.

**Rodas:** el mercado o la forja de Rodas pueden vender a un comerciante Edranor sin transferir su potestad fiscal. Ni un arriendo mercantil, ni un carro que cruce el linde autorizan aduana interior. La Corona puede inspeccionar en su competencia con prueba de habilitación. Las operaciones oficiales de Corona/Armada no están gravadas por la Casa; compras privadas siguen pagándose.

## Seguridad del cobro
No embolsar tributos sin identidad, título y derecho; no inferir obligación de una bodega por tener barricas visuales; no ejecutar embargo, decomiso o pena sin base en código y procedimiento. E09 propone registros, no liquida impuestos ni fija tarifas.
