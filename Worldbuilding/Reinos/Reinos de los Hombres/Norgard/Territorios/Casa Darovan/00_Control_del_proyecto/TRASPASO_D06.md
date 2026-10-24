# DAROVAN 7 — Traspaso preparado a D06 (asentamientos ordinarios)
**D06 NO INICIADA.** Este documento es traspaso, no implementación ni permiso de crear rama D06 antes del merge expresamente autorizado de D05.

## Puerta de entrada obligatoria
1. Verificar estado `merged=true` de PR D05 en GitHub, y que `main` contiene el commit correspondiente.
2. Revisar `00_Control_del_proyecto/REGISTRO_FASES.md`, `DECISIONES_Y_BLOQUEOS.md`, acta de auditoría y evidencias CI; si hay prueba pendiente, no atribuirla como superada.
3. Leer plan de D06 y todos los perfiles D01–D05 desde `main`, no ramas viejas.
4. Crear **nueva conversación y rama exclusivas de D06**, sin fusionar por automatismo.

## Herencia territorial obligatoria
- 12 unidades D01 cualitativas, no polígonos ni administración determinada; terrenos seguros y límites reales aún no definidos.
- Red D02 Belara/Lhera/Veldora/Thalen; cuatro ciudades **Treihord, Veldora, Taramin, Syvaris** protegidas como diseño manual, nunca generador.
- Clima D03 y riesgos candidatos no son hechos vividos ni parámetros medidos.
- D04 tiene ocho cadenas económicas, no ocho rutas comprobadas; no convertir cada mina, almacén, parcela, astillero, caladero o carreta conceptual en asentamiento.
- D05 tiene exactamente **tres** conexiones modales físicas confirmadas cualitativamente (camino Veldora–Treihord; barcazas Belara desde funciones de carga indeterminadas; galería privada Vena) y **cuatro** relaciones de suministro que NO son rutas. No asumir una malla de caminos, estaciones postales o ferris.
- Arven propiedad UNKNOWN (DAR-P01), no generar una aldea Darovan allí por proximidad. No crear población permanente en el interior del Bosque de las Agujas. Bosques Pilares y Taramin únicos; Syvaris forestación discontinua. Karsath excluida.

## D06 tiene reservado
Metodología `esqueleto → posibilidades → condiciones → pesos regionales → modelos → instancias/seed`; aldeas, pueblos, villas y enclaves laborales **sujetos** a recursos/agua/accesos verdaderos; IDs y persistencia solo como diseño si CoreRPG/Godot no están integrados. No usar D05 como generador de trayectos ni fuente de distancias, destinos o horas.

## Obligaciones de autor y fases posteriores
Pendientes DAR-P01/P04/P07/P08/P09/P10/P11; nuevos topónimos, límites políticos y asentamientos importantes no se promulgan sin decisión del autor. D07 ciudades/puertos; D08 hogares/servicios/mensajería; D11 rutas reales, embarcaciones, mensajes, stocks, navegación y persistencia. Cualquier mapa métrico, servicio de correos o ruta Azurios se tratará aparte.

**No comenzar D06 en esta conversación.**

## Evidencia de D05 a heredar (21-10-2026)
PR [#30](https://github.com/robdor80/Videojuego_Nimroel/pull/30) debe estar **fusionada** antes de D06. La CI [#39587112092](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39587112092) ejecutó D01–D05 en Windows/Linux y rechazó **30 mutaciones negativas D05**. Consultar [acta D05](../Auditorias/D05_CIERRE_Y_VALIDACION_2026-10-21.md), y comprobar nuevamente el resultado asociado al último commit y a la fusión; no dar por realizadas pruebas CoreRPG/Godot ni GIS.


### Anexo canónico aprobado por el autor — 21/10/2026

Las referencias de esta fase que afirmaban **Arven UNKNOWN**, **cuatro ríos** o **río Veldora no identificado** son históricas y se sustituyen por esta decisión expresa del autor:

- **DAR-P01 RESUELTA:** Arven pertenece formalmente a Casa Darovan. No se autoriza por ello puerto, travesía o ruta comercial nueva.
- **DAR-P07 RESUELTA:** el cauce verde junto al sur de Veldora es el **río Veldora**, independiente del sistema Belara/Lhera.
- **DAR-P08 PARCIALMENTE RESUELTA:** cinco ríos nombrados según flechas del mapa confirmado: **Belara** (azul, río principal desde el norte y junto a Treihord), **Lhera** (rojo, rama del Belara hasta el litoral al norte de Veldora), **Veldora** (verde), **Fhalion** (amarillo, nuevo río menor al sur del Veldora), **Thalen** (violeta, al otro lado de las montañas con dos brazos finales alrededor de Taramin). **Cuatro sistemas hidrográficos:** Belara/Lhera, Veldora, Fhalion, Thalen.
- **DAR-P04 aún abierta:** la escala gráfica de **400 millas** aportada por el autor no constituye levantamiento topográfico verificado. Nacimientos exactos, caudales, cotas, recorridos métricos, bifurcación Belara/Lhera, desembocadura precisa del Fhalion, puentes, vados, navegación y accesos siguen pendientes. No deducir rutas a Arven o por Fhalion.

**Corrección retroactiva de las referencias documentales D01–D05, no una reapertura de sus implementaciones ni runtime.** El grafo D02 pasa a 5 ríos / 4 redes / 15 nodos / 11 enlaces topológicos simbólicos, manteniendo D05 sus 17 nodos logísticos y 3 conexiones modales acreditadas. Los hitos documentados anteriormente permanecen como actas de lo que se sabía en aquella fecha.
