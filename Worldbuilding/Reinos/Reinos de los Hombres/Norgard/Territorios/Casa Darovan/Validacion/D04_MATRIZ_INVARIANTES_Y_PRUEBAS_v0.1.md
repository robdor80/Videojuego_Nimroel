# D04 — Matriz de invariantes y pruebas (v0.1)
**NO CANON NUEVO, NO RUNTIME.** 36 controles de diseño agrupados a continuación; 22 comprobaciones JS remotas ejecutadas; Python D04 PENDIENTE MSI.

| Controles | Regla |
|---|---|
| 01–04 | Schema, D04, status no-runtime, banderas de contenido nuevo falsas |
| 05–08 | Autoridad Core→Defaults→Casa→localidad→World State, evidencia, 19 fuentes reales, referencias D01/D02/D03/Core/Default |
| 09–12 | 12 IDs D01=D03 únicos, sin polígonos de producción, suelo/agua no medidos, producción/parcelas/cantidades nulas |
| 13–16 | 8 cadenas con fuentes, sin productor nuevo ni producción/capacidad/ruta nueva, incertidumbres explícitas |
| 17–20 | Oro/plata Valkram y Elyra a escala regional; Treihord explota Valkram; carbón Azurios no Valkram; Crisol no ceca |
| 21–24 | Pilares único y madera minero, Agujas sin poblados interiores, Taramin bosque único tradicional, Syvaris discontinuo |
| 25–28 | Belara adyacente sin atravesar Treihord; Lhera desde Belara; Veldora independiente; Thalen doble terminal con Taramin entre brazos |
| 29–32 | Solo ciudades manuales; Karsath excluida/Arven UNKNOWN; Taramin pesca y aceite de ballena sin asumir caladeros/navegabilidad; Syvaris sin acuíferos inventados |
| 33–36 | Aduana interior prohibida, Ceca Hallheim/Clavo 24/480, libro Core no produce pagos, no fingir runtime |

## Negativos definidos en `validate_d04.py` (16)
`arven_owned`, `unknown_mine`, `production_yield`, `coal_from_valkram`, `belara_through_city`, `lhera_wrong_source`, `veldora_join`, `thalen_one_arm`, `pilares_two_forests`, `industrial_taramin_logging`, `inside_agujas`, `crisol_mints`, `interhouse_customs`, `species_invent`, `route_geometry`, `runtime_claim`.

## CMD en raíz del repositorio (MSI)
```cmd
python "Worldbuilding\Reinos\Reinos de los Hombres\Norgard\Territorios\Casa Darovan\Validacion\validate_d01.py" && python "Worldbuilding\Reinos\Reinos de los Hombres\Norgard\Territorios\Casa Darovan\Validacion\validate_d02.py" && python "Worldbuilding\Reinos\Reinos de los Hombres\Norgard\Territorios\Casa Darovan\Validacion\validate_d03.py" && python "Worldbuilding\Reinos\Reinos de los Hombres\Norgard\Territorios\Casa Darovan\Validacion\validate_d04.py"
```
**Salida esperada solo si realmente se ejecuta:** `D04 STATIC OK: 12 zones, 8 chains, 19 sources, 16 negative tests; NOT RUNTIME`. No declarar que Python o Godot corrieron basándose en JS.
