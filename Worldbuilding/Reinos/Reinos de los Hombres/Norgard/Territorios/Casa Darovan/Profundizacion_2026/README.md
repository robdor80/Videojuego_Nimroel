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
