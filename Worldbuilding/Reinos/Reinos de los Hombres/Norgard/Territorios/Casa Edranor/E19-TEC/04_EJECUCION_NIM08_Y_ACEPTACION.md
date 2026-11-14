# E19-TEC.04 — Ejecución técnica, NIM-08 y aceptación honesta

**14/11/2026.** Proyecto: Nimroel RPG, Godot 4.7.2 Standard, C++20 CoreRPG. Trabajo autónomo en PR Draft, sin Codex ni alteraciones de `main`.

## De qué se ha partido

- E19-R0 corrigió expresamente el antiguo error de exigir coordenadas o unir líneas rojas para construir geografía causal.
- E19-R1–R5 establecieron territorio, vertientes, cuencas, suelos, vegetación, rutas *preguntadas* y ocupación *estudiada*, bajo protección de canon.
- E19-R6 auditó paridad de **método B2** con Valrik/Treskal; no inventó geometría B3 ni juego B4.
- La fuente metodológica de Valrik, `Casa Valrik/Geografia_local/reglas_espaciales_generacion_motor_v0.1.md`, ordena: anclas → relieve → drenaje → cuencas → agua → microclima → suelo/cubierta → uso humano → World State.
- `Docs/NIM-01_GENERACION_ESPACIAL_PROCEDURAL.md` dispone que la topología puede ser lógica y no dibujada, la generación debe ser reproducible y el Host no inventa rutas.
- `Docs/NIM-08-19/NIM-08/01_CONTRATOS_Y_DISENO.md` (PR #50 aún Draft) fija **una sola autoridad CoreRPG**, prohíbe un World State duplicado y separa preparación determinista de simulación viva. NIM-10/12 tienen previstas la generación y navegación de producción; E19-TEC NO las duplica.

## Implementado en esta rama

| Archivo o módulo | Para qué sirve | Qué no hace |
| --- | --- | --- |
| `technical_manifest_v0.1.json` y `approval_registry_v0.1.json` | Inventario explícito de no materialización y autorización todavía vacía | No dice que haya sectores reales |
| `spatial.py` | Validación de geometría 2D LOCAL_METRIC, fuentes, transformaciones, continuidad de río/caminos, restricciones y exportación ordenada | No inventa coordenadas ni valida jurídicamente una fuente por el nombre de su campo |
| `causal_atlas.py` | Compila R1–R5 en los siete contextos evaluables con IDs y referencias de reglas, hipótesis y vetos | No convierte MF/HC/OS/CT en actores |
| `drainage_lab.py` | En malla de PRUEBA calcula gradientes D8, acumulación, salidas/sumideros declarados, balance y determinismo | No crea ríos reales ni mide precipitación |
| `route_query.py` | Prueba búsqueda en Gp validado, con sentido, modos, Corona, bosques y cierre dinámico de consulta | No despacha transporte, no concede derechos ni persiste cierre |
| `GodotLab/context_reader.gd` | Lector B2 real en Godot, en laboratorio aislado: siete contextos, sin mapa ni entidades ficticias | No está conectado a la sesión de jugador, no duplica Core |
| `test_spatial.py`, `test_causal_atlas.py`, `test_drainage_lab.py`, `test_route_query.py` | Rechazo adversarial y determinismo | Los tests sintéticos NO prueban canon cartográfico |
| `.github/workflows/edranor-e19-tec.yml` | Regresiones parentales R0–R6 en Windows/Linux y prueba headless Godot 4.7.2 | Ni APK físico ni partida Core en producción |

La condición `APPROVED_B3` del JSON es **declarativa y externa**: exige expediente, medición, revisión y autoridad contrastables fuera del comprobador. El código comprueba estructura y relaciones, no autentica la firma humana ni puede resolver la ausencia de una fuente física.

## Fases técnicas distintas: no trasladar exigencias erróneamente

**B2 causal** — No precisa coordenadas. E19-R0–R6 responde qué territorios, laderas, cuencas, clases y procesos son plausibles. El catálogo causal puede usarse para diseño/selección sin pretender que esas reglas sean un mundo materializado.

**Generación lógica de una campaña** — Puede utilizar grafos y localizaciones relativas, sin CRS global, cuando NIM-09/10/12 implementen su generador y autoridad CoreRPG según NIM-08. No exigir un levantamiento topográfico al autor para comenzar una aldea procedural; sí exigir que el modelo y el contexto no contradigan el canon. Los IDs lógicos y los grafos persistentes serán propiedad del Core al materializar.

**B3 cartografía métrica** — Solo cuando se solicite una capa visual/material que realmente necesite geometría, se exige fuente, escala, transformación reversible, pendientes y derecho. El exportador de E19-TEC sirve este caso; no condiciona toda la geografía B2.

**B4 juego vivo** — Requiere integración CoreRPG, NIM-10/12/17/18 y prueba real Godot/Windows/Android con rutas, NPC, permisos, acciones, guardado, restauración y no duplicación. Ejecutar un laboratorio Godot no demuestra B4.

## Pruebas innegociables

1. Retener R0–R6 y las correcciones autorales; no reintroducir la PR #84 descartada.
2. Dos compilaciones iguales del mismo catálogo producen idénticos bytes y SHA-256.
3. MF-08/U7 no tiene emplazamientos; ningún código cierra el norte político.
4. Cuencas y cauces potenciales solo nacen por pendiente, aportes y receptor, nunca por estética.
5. Un solapamiento o ciclo de agua, desagüe cuesta arriba, sumidero sin balance o carretera sin derecho debe bloquearse.
6. Gq/CT no es Gp; OS no es pueblo; la cobertura Sp vacía no crea servicios.
7. Rodas conserva tipo ALDEA y jurisdicción regia; Hallheim no aparece dentro de Edranor.
8. Bosque Alto exige autorización; Bosque Real sigue siendo de Corona; Dorth carece de Caleran probado y Karsath de puerto urbano probado.
9. Un paquete de TEST_ONLY nunca se exporta como canon de producción ni se registra como estado Core.
10. El resultado de toda CI sobre el HEAD final debe revisarse; no declarar integración de Godot sin cargarlo y no declarar CoreRPG sin ejecutar persistencia real.

## Criterios de promoción por componente

- **TEC-A documental y herramientas:** aceptar tras inspección de diff y CI del HEAD exacto en Windows y Linux; lectura en Godot para el subcomponente `GodotLab`.
- **Sector material B3:** solo con fuentes y geometría aprobadas, prueba de topología, terreno, agua/servidumbre y huellas reales; puede aprobarse UN sector sin elevar el conjunto de Edranor.
- **Juego B4:** solo bajo autoría y transacción Core, ruta física/legal, identidades, memoria y reanudación en Godot. No es misión del `GodotLab` simular Core o abrir una segunda partida.

## Límites y trabajo restante que NO debe ocultarse

Actualmente el inventario autorizado permanece vacío: no hay rutas Gp, parcelas, cauces menores, hogares, cobertura de servicios o población materializadas por esta fase. Los datos de R1–R5 siguen sin georreferenciación y no debemos inventarla. En consecuencia, TEC-B (primer sector material cartografiado) y TEC-C (runtime Godot + Core) no pueden declararse cerrados por estas herramientas. La integración futura se hará en las fases NIM previstas, reutilizando aquí contratos/validadores sin crear una segunda lógica de navegación ni nuevos tipos nativos por duplicado.

**La calidad de Valrik/Treskal es un umbral mínimo de método, no una licencia para rellenar lugares con datos imaginarios.**
