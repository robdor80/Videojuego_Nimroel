# Treskal — Regresión Armada Real / T08 v0.1

## Estado

**VALIDACIÓN ESTÁTICA SUPERADA**

Marcador: `NORGARD_TRESKAL_ROYAL_NAVY_STATIC_REGRESSION_VALIDATED`

Marcador de cierre: `NAVAL_POINT_2_CLOSED_FOR_NORGARD_AND_TRESKAL`

## Contratos comprobados

- `Worldbuilding/Sistemas/Norgard Defaults/Datos operativos/norgard_royal_navy_default_v0.1.json`
- `Datos operativos/treskal_royal_naval_complex_contract_v0.1.json`
- `Datos operativos/treskal_city_structure_v0.1.json`
- `Datos operativos/treskal_preplan_external_canon_constraints_v0.1.json`

## Resultado estructural

- 8 clases navales.
- 25 grandes navíos nominales únicos.
- Clase Norgard: 12.
- Clase Treihord: 8.
- Clase Aethros: 4.
- Clase Corona: 1.
- Nave Real: **Lobo de Plata**.
- pólvora: false.
- T08: `royal_naval_complex`.
- T08 contiene S08 + S13.
- S13 es Base Naval Principal, no necesariamente única.
- autoridad T08: Corona de Norgard / Casa Aethros.
- mando interno Casa Valrik: false.
- antiguo pendiente `royalNavalFramework`: eliminado.
- antigua prohibición de base naval separada: eliminada y sustituida por el canon S13 dentro de T08.

## Compatibilidad

- T07 continúa siendo puerto civil.
- T12 continúa siendo recinto militar Valrik.
- S08 conserva su ID estable como Astilleros Reales.
- S13 se añade sin renumerar S01–S12.
- No se requiere migración de saves: no existía estado persistente previo de S13 y los IDs existentes no cambian.
- La geometría métrica interna de T08 sigue siendo trabajo cartográfico futuro, no deuda de canon naval.

## Resultado

**POINT_2_ARMADA_ASTILLEROS_CLOSED**
