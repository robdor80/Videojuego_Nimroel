# D08 — Matriz de invariantes y pruebas v0.1

| Grupo | Condición estática y negativa |
|---|---|
| Integridad de fuente | Todos los `sourceRefs` existen; los índices D04/D06/D07 siguen siendo autoridad |
| Jerarquía | Nimroel Core → Norgard Defaults → Darovan → Localidad → World State |
| Canon urbano | Solo cuatro ciudades manuales, fuera Karsath; Treihord aproximadamente 32.000 |
| D07 conceptos | Veldora B, Taramin A, Syvaris A solo concepto, sin nuevo plano/edificio |
| Demografía | Poblaciones restantes, población territorial y número de hogares `null/UNKNOWN` |
| Población CoreRPG | Nada de simulación runtime por JSON, sin registro numérico `RelationKind` aprobado |
| Edad y convivencia | 18+ civil, aprendiz desde 12 y empleo limitado desde 15; no co-residencia matrimonial automática |
| Recursos e inventarios | Sin stock ex nihilo, ni proveedor gratuito, ni demanda que cree edificio |
| Trabajo | Profesión ≠ empleo; ausencia/vacante ≠ sustituto instantáneo |
| D05/D06 | Referencias existentes válidas; no se generan ciudades ni caminos a partir de suministros |
| Servicios | Diez necesidades, no diez edificios; capacidades y proveedores cuantificados UNKNOWN |
| TEST_ONLY | Casos de laboratorio aislados, IDs prefijados y sin NPC persistentes creados |

Ejecutar `python "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan/Validacion/validate_d08.py"` sobre checkout íntegro. CI GitHub Actions en Ubuntu y Windows ejecutará D01–D08 sin necesidad de MSI. Estas pruebas **son estáticas**, no certifican integración CoreRPG/Godot, ni desplazamientos, guardados o economía simulada.
