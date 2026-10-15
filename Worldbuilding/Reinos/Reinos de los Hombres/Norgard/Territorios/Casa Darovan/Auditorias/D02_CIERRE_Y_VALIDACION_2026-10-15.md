# DAROVAN D02 — Acta de cierre documental y validación (15-10-2026)

**Estado:** D02 CERRADA DOCUMENTALMENTE, propuesta de PR a revisión, SIN FUSIONAR. **No** canon nuevo, mapa georreferenciado, runtime ni hidrología simulada. Rama `feat/darovan-d02-hidrografia-cuencas`.

## Inicio verificado
Se comprobó en GitHub la PR #15 de D01: `merged=true`, merge SHA `9f3f723b0e7b2b78567c6397bba7099bfe658b0a`. Esta es la base de la rama D02. Se consultaron directamente los originales de ríos, montañas, bosques, mares, geografía, Treihord y Core, además del traspaso D02, decisiones, control y perfiles de D01.

## Entregables
1. `Hidrografia/01_red_hidrografica_y_grafo_v0.1.md`: grafo conceptual Mermaid; hechos, relaciones y límites de lectura.
2. `Hidrografia/02_cuencas_divisorias_y_reglas_v0.1.md`: cuencas cualitativas, drenaje, escorrentía, manantiales candidatos, inundabilidad y permanencia (sin ubicar instancias ficticias).
3. `Hidrografia/03_interacciones_territoriales_y_traspaso_v0.1.md`: efectos sobre ciudades, bosques, economía, rutas y fases futuras.
4. `Datos operativos/darovan_d02_hydro_network_v0.1.json`: planificación **NO RUNTIME**; cuatro ríos canónicos, tres sistemas hidrográficos, 13 nodos conceptuales y 10 aristas dirigidas. Dos salidas del sistema Belara/Lhera; río Veldora aparte; Thalen con dos brazos propios.
5. `Validacion/D02_MATRIZ_INVARIANTES_Y_PRUEBAS_v0.1.md`: 25 controles; `Validacion/validate_d02.py`: verificador Python reproducible con 8 fixtures negativos.
6. Índices, registro de fases, bloqueos y `00_Control_del_proyecto/TRASPASO_D03.md`.

## Canon protegido
Belara: origen occidental septentrional Valkram, junto a Treihord y **no dentro**, desemboca en Golfo Norgard, barcazas industriales de poco calado. Lhera: bifurcación del Belara, curso propio junto al Bosque de las Agujas y Golfo Veldora. Veldora: independiente de ambos y Golfo Veldora. Thalen: único río, bifurcación terminal con Taramin entre los dos brazos y desembocadura Golfo Norgard.

Arven sigue sin propietario territorial acreditado (DAR-P01); pendientes frontera/escala/cotas (DAR-P04) e identificación del río visual tras Veldora (DAR-P07). Nuevo DAR-P08 cataloga orden desconocido bifurcación/Tr​eihord, cabeceras Veldora/Thalen y cuantificación hidrográfica. Syvaris Darovan, Karsath excluida y Bosque de Agujas sin poblados permanentes interiores. No se modifica ningún original de Norgard, Core, Valrik o Treihord.

## Verificación REALIZADA, con alcance exacto
- Consultas GitHub: PR #15 fusionada, HEAD de base, originales, árbol de fuentes y comparación de rama contra base.
- **16 verificaciones positivas remotas realizadas y superadas** sobre JSON recuperado de GitHub: parseo, jerarquía idéntica a D01, anclas D01, unicidad de IDs, conectividad, separación de sistemas, dos brazos Thalen, Treihord, protección territorial, `sourcePaths` existentes y ausencia de geometría/cifras no autorizadas; diff restringido a Casa Darovan.
- **8 mutaciones negativas remotas realizadas y rechazadas** en JavaScript sobre copias del JSON: boca falsa Belara, Lhera desconectado, Veldora conectada, un solo brazo Thalen, Belara cruzando ciudad, Arven adjudicada, afluente ficticio y arista entre sistemas.
- **Script Python incorporado pero NO ejecutado en un checkout completo** durante esta sesión. El resultado de las comprobaciones JavaScript no demuestra que haya corrido el script Python ni que exista CI asociada.
- **Runtime, Godot/CoreRPG, GIS y simulación hidráulica NO ejecutados.** Sin pruebas de juego, generación, guardar/cargar, caudales, erosión real, barcazas navegando o crecidas.

## Incertidumbres que se mantienen
No existen aquí coordenadas, polígonos de cuenca, altitudes, pendientes, afluentes nombrados, manantiales concretos, aforos, cuantificación de deshielo, frecuencia de inundación, puentes ni nuevos asentamientos. Los tipos regionales de barrancos estacionales en Taramin no se materializan como cauces individuales. El grafo D02 expresa conectividad **lógica**, no cartografía aprobada.

## Salida
Documentación propuesta lista para revisión. El **autor decide el merge** y cualquier ampliación del canon. D03 NO INICIADA y se abrirá solo tras verificar que la PR D02 quedó fusionada en main. Leer TRASPASO_D03.md.
