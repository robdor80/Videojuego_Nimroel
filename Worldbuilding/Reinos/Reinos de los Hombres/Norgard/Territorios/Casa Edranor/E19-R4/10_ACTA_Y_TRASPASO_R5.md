# E19-R4.10 — Acta de alcance y traspaso a ocupación del territorio
**14 de noviembre de 2026.** Se documenta un atlas funcional B2 de movilidad y pasos con autoridad explícita y evidencias todavía no disponibles. Este acta no declara PASS hasta inspeccionar diff, pruebas y CI del HEAD.

## Entregado en R4
- Separación rigurosa Gd/Gq/Gp (Gp vacío), ocho clases TC y doce expedientes CT (11 estudios + veto MF-08).
- Cruces de agua y collados condicionados a continuidad, hidrología y jurisdicción; cero infraestructuras creadas.
- Siete cadenas FS de actividad compatible con E04, E15, E16 y E17; sin mercancías, personas ni servicios en tránsito.
- Diez riesgos HZ de suelo, agua, clima y mantenimiento que no instancian accidentes.
- Viaje, información, rumores, retrasos, derechos y memoria con contratos de identidad y observación.
- Contrato JSON versionado, validador y workflow Windows/Linux; pruebas documentales, no escenas 2D.

## Pendientes de fuente y autoridad
1. EDD-01/02: extremo norte, límites y posicionamiento/topografía local para B3; nunca cerrar por dibujo rojo.
2. EDD-03: cauces específicos, caudales estacionales, vados y receptores: R2 solo tipologías.
3. EDD-07: derecho, servidumbres, propiedad y trazado físico de caminos.
4. Reconocimiento de collados, pendientes, firmes y capacidad de modos.
5. Datos climatológicos y calendario: nieve, hielo, barro, heladas, crecidas y memoria.
6. Mantenimiento, presupuesto, autoridad, presencia de cuadrillas, carreteros y mensajeros.
7. Permisos forestales y acuerdo regio para Rodas; prohibición de tala libre y aduana interior.
8. E19-TEC y E28: persistencia y navegación Godot/CoreRPG con pruebas físicas; no habilitados en esta fase.

## Traspaso obligatorio a E19-R5 — habitabilidad, asentamientos y ocupación
R5 puede usar **la demanda funcional** de CT/FS para preguntar dónde haría falta acceso. No puede usar CT como carretera. Para cada parcela, hogar o núcleo deberá acreditar: suelo y agua aptos R1–R3; capacidad legal de ocupación; saneamiento; conexión **Gp certificada** cuando el uso dependa del transporte; límites de bosque; mercancías/profesiones reales; riesgo estacional y autoridad. Si no hay camino validado, la accesibilidad queda UNKNOWN o INSUFFICIENT_PROOF; no se arregla moviendo el poblado sobre un camino inventado.

## A R6 y E19-TEC
R6 contrastará el estándar de Valrik en geografía, vías, agua, ocupación y persistencia, y resolverá contradicciones con E05/E16/E17. La fase E19-TEC podrá parametrizar tramos **únicamente** cuando se cumplan las puertas B3; IDs de segmento diferentes de CT. No duplicar rutas para cada misión, actor o entrega.

## Integración y versión
Branch R4 separada sobre HEAD R3 **8887445eec5996d18f4c63b849f568ea39c8b0ef**. Integrar ordenadamente R0 #87 → R1 #89 → R2 #90 → R3 #91 → R4, con auditoría y CI antes de fusionar. No tocar main, E00–E19-R3, otras Casas, CoreRPG, ContentPacks o Game. La PR #84 descartada permanece excluida.

**Dictamen documental provisional:** nivel B2 completo para el diseño de movilidad si todas las pruebas pasan; nivel B3 y B4 **NO ACREDITADOS**. Ninguna futura IA, mapa ni test de esquema tendrá autoridad para declarar un camino real sin evidencia.