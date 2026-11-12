# E06 — Prioridades por las siete unidades E01
Los pesos son enteros **0–4**, solo preferencias de selección entre modelos *elegibles*. No son probabilidades poblacionales, frecuencia real de aldeas, número de tiradas, hectáreas, cosechas ni densidades.

| Unidad E01 | Prioridad de estudio | Restricción |
|---|---|---|
| Interfaz oeste Valkram | sin pesos activos | laderas, límites y accesos sin verificar |
| Karsath centro-oeste | viticultura/agricultura, usos secundarios | parcelas, agua y derechos pendientes |
| Lumina/Bosque Alto | tonelería y uso forestal gestionado | propiedad y protección forestal sin detallar |
| Centro vinícola | viticultura, agricultura, bodega auxiliar | no viña continua ni bodegas automáticas |
| Dorth/Azurios oeste | artesanía; bosque de producción desactivado | protección del Bosque Real e interfaz forestal |
| Transición norte fría | sin pesos activos | EDD-01, microclima y accesos |
| Norte lejano sin cierre | sin pesos activos | no afirmar que pertenece a Edranor |

La matriz completa, por ID técnico y ocho columnas, está en `Datos operativos/edranor_e06_settlement_rules_v0.1.json`. Las áreas E01 son sectores cualitativos, **no** polígonos de reclutamiento. Un cero significa «no elegible para este ensayo», no «la región carece de personas».

Orden: resolver anclas/exclusiones → confirmar ocho pruebas locales → verificar requisitos de clase/modelo → aplicar peso y semilla → devolver **candidato de laboratorio sin representación real**. No hay cupo total ni algoritmo de dispersión espacial porque faltan superficie, capacidad de carga y geometría medible.
