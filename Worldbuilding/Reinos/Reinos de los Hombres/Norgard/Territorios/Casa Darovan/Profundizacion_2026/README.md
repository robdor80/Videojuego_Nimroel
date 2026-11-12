# Darovan — Profundización D.P14–D.P18

**Estado:** paquete de desarrollo documental condicional y auditoría, preparado en rama independiente. No hay integración física CoreRPG/Godot.

| Fase | Localización | Función |
|---|---|---|
| D.P14 | `D.P14/01_habitabilidad_y_diez_puertas.md` | 12 unidades y elegibilidad de asentamientos |
| D.P15 | `D.P15/01_coherencia_regional_servicios_y_asentamientos.md`; `02_cobertura_causal_y_limitaciones.md` | Nueve modelos, diez necesidades y servicios con capacidad real |
| D.P16 | `D.P16/01_auditoria_funcional_99_capas_treskal_y_cuatro_ciudades.md` + cuatro fichas `ciudad_*` | Comparación funcional con Treskal, sin inventar barrios |
| D.P17 | `D.P17/01_interfaces_causalidad_persistencia_y_24_escenarios.md` | Contrato de causalidad y pruebas hipotéticas |
| D.P18 | `D.P18/01_auditoria_comparada_y_deuda_real.md`; `02_precondiciones_cartograficas.md` | Dictamen, deuda y traspaso |

El material se acompaña de cinco JSON de contratos, validador estático y GitHub Actions. La finalización documental de este pack **no declara** a Veldora/Taramin/Syvaris urbanísticamente cerradas al nivel de Treskal ni nuevas entidades ejecutadas.

**Regla de autoridad:** Core → Norgard → Casa Darovan → localidad → WorldState. `AUTHORED` no se confunde con `DERIVED_CONDITIONAL` o `TEST_ONLY`.

**Fuente de comparación:** `../Casa Valrik/Treskal/AUDITORIA_CIERRE_FUNCIONAL_TRESKAL_v0.1.md`, `MAPA_EXTRACCION_CORE_NORGARD_TRESKAL_v0.1.md` y metodología de asentamientos de Valrik.

**Permisos:** revisión humana antes de fusión a `main`; el autor mantiene las decisiones de identidad canónica que faltan.

## Paquete editorial de rescate y lectura preferente — 11/11/2026

El índice inicial anterior refleja la PR #41 antes de profundizar el contenido. Para leer **la versión completa de diseño**, seguir este orden:

1. [D.P14/02 — Habitabilidad del territorio y doce contextos vividos](D.P14/02_territorio_vivido_habitabilidad_y_estaciones.md), además de la matriz D.P14/01.
2. [D.P15/03 — Economía regional vivida y ocho cadenas](D.P15/03_economia_vivida_red_regional_y_necesidades.md), además de D.P15/01–02.
3. Cuatro fichas de D.P16 **reescritas**: [Treihord](D.P16/ciudad_treihord_plan_funcional_condicionado.md), [Veldora](D.P16/ciudad_veldora_plan_funcional_condicionado.md), [Taramin](D.P16/ciudad_taramin_plan_funcional_condicionado.md), [Syvaris](D.P16/ciudad_syvaris_plan_funcional_condicionado.md) y [comparativa D.P16/03](D.P16/03_cuatro_ciudades_comparativa_editorial_y_criterios_de_lore.md).
4. [D.P17/02 — Cinco interacciones y memoria](D.P17/02_situaciones_jugables_autoridad_y_memoria.md), además del catálogo D.P17/01.
5. [D.P18/03 — Dictamen vigente y traspaso hacia D.P20](D.P18/03_cierre_editorial_real_y_traspaso_DP20.md), manteniendo las reservas de D.P18/01–02.

**Resultado:** D.P14–D.P18 se consideran **capas de planificación y diseño editorial sustantivas y diferenciadas**, aún bajo revisión de PR y sin canon nuevo por commit, mundo simulado ni aprobación automática de barrios/personajes. La siguiente fase de contenido es **D.P20 Veldora**; D.P19 auditó la insuficiencia anterior, no introduce una nueva espera ni otra vuelta de matrices.

## D.P23 — Treihord (12/11/2026)

[Monografía de Treihord](D.P23/README.md): mantiene su canon cerrado de ocho barrios y desarrolla doce establecimientos futuros, diez biografías base, cuatro memorias privadas, cuatro arcos condicionales y ocho escenas TEST_ONLY. Decisiones de autoría adoptadas por delegación; ninguna geometría ni NPC instanciados. PR Draft no fusionada mientras no haya orden expresa.
