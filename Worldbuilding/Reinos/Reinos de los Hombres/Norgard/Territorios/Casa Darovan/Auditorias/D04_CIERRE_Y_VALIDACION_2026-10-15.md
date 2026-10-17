# DAROVAN D04 — Acta de cierre documental (15-10-2026)
**Estado:** preparado para revisión PR #20, sin fusionar; NO CANON NUEVO, NO RUNTIME.

## Base y fuentes
GitHub PR #17 D03 merged=true, squash `191bcd5ea11308952f567f9e7e15f4f6ed2cf54a`; HEAD main para rama D04 `df43be5b2a62b137b8ed77f7900818e39646c272` (contiene NIM-02 PR #18). Consultados control Darovan, originales de geografía, montañas, bosques, ríos, mares, clima, Treihord, Grandes Casas, visual de puertos, D01–D03, Core navegación/transacciones y Norgard Defaults moneda/fiscal/pesca. D01/D02/D03 Python MSI SUPERADOS 15-10-2026, según acta específica; esta evidencia no se reetiqueta como pendiente.

## Entrega
Cuatro documentos: inventario y cadenas; matriz territorial D01–D03; flujos y almacenes; fiscalidad y contratos. Perfil JSON D04 (12 zonas, 8 cadenas, 19 referencias, 7 instalaciones/funciones ya documentadas, 3 puertos y 5 escenarios hipotéticos). Registro de fuentes, matriz 36 invariantes, validador Python 16 negativos, actualización de plan/registro/deuda, TRASPASO_D05 sin iniciarla.

## Pruebas efectivamente ejecutadas
- **Remoto JavaScript sobre D04 JSON publicado en GitHub, commit `ddb8ca4`: 22/22 OK.** Positivos: parseo JSON, 19/19 archivos de fuentes existentes, igualdad 12 IDs con D01/D03, topología de D02, fiscalidad Norgard y Core ledger, invariantes D04; 16 negativos rechazados (Arven, mina, rendimiento, carbón, Belara, Lhera, Veldora, Thalen, Pilares, Taramin industrial, Agujas, Crisol, aduana entre Casas, especies, ruta, falso runtime).
- **Python `validate_d04.py`: NO EJECUTADO sobre checkout real** en esta fase remota; ejecutar en MSI y aportar resultado. Su código incluye pruebas, pero no equivale a su ejecución.
- **GIS, Godot/CoreRPG conectado, saldo económico, inventarios, persistencia, embarcaciones y CI: NO EJECUTADOS/acreditados.**
- Verificación final de alcance y comparación rama-main se documenta en comentario/PR una vez publicada esta acta.

## Canon y decisiones
Créditos originales intactos; oro/plata Valkram/Elyra sin explotar Elyra automáticamente, carbón Azurios, Pilares único y uso minero, Agujas sin asentamientos, Taramin único forestal, Syvaris disperso, cuatro ciudades manuales, Karsath fuera, Arven UNKNOWN, Belara junto a Treihord, Lhera bifurcación, Veldora independiente, Thalen dos brazos. El Crisol no ceca, no aduanas entre Grandes Casas. No autorizadas cifras, cultivos, rutas, propietarios, minas concretas, acuíferos ni cuotas. DAR-P01/P04/P07/P08/P09/P10/P11 abiertos.

## Puerta de salida
El autor revisa y decide el merge de PR #20. **D05 NO iniciada.** La evidencia JS prueba únicamente consistencia estática de datos, no funcionamiento en juego.
