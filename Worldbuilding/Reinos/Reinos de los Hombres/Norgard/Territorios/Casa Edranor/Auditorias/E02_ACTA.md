# E02 — Acta de entrega y control de cierre
**Fecha:** 12/11/2026 · **Fase:** E02 hidrología y drenaje · **Naturaleza:** documentación y contratos de planificación.

## Entregables / criterios de aceptación
1. Recuperados **Lurien y Antela** de documento canónico y localización relativa; preservado su curso regional y límite de navegabilidad.
2. Cero hidrónimos inventados; cero cuencas delimitadas o cursos locales declarados sin soporte.
3. Siete unidades E01 reciben fichas de incertidumbre, sin pendiente, dirección de flujo, manantial ni cauce inventados.
4. Cuatro expedientes de cuenca/divisoria son **preguntas** y nunca mapas validados.
5. Cuatro escenarios de riesgo son **condicionales**, no alarmas ni mapas de inundación declarados.
6. Cuatro necesidades de agua conservan procedencia, derechos e infraestructura \`UNKNOWN\`.
7. Los cuatro corredores E01 no incorporan pasos, puentes, rutas ni vados inventados.
8. Rodas conserva fiscalidad y mando Aethros; Hallheim sigue fuera de Edranor; sin aduanas interiores; norte sin cierre.
9. Manifiesto JSON con IDs, herencia, evidencia y \`runtimeEnabled=false\`, validador negativo y CI para Linux/Windows, con regresión E00/E01.
10. Trazabilidad de fuentes, registro de deuda y traspaso E03 presentes.

## Límites de las pruebas
Tests estáticos detectan *deriva documental*; no prueban hidrodinámica, inundabilidad real, simulador de clima, terreno transitable ni CoreRPG/Godot/Android. **No existe polígono/DEM ni caudal local certificado**.

## Cierre administrativo
La fase se considera **técnicamente validada** solo tras ejecución verde en Windows y Linux sobre HEAD exacto de la PR, con regresiones E00/E01. La publicación no equivale a fusión; la autorización general de esta conversación permite fusionar cuando se cumplan las puertas y GitHub lo admita. Mantener E03 independiente.
