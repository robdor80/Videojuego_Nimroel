# D07 — Matriz de aceptación estática de ciudades canónicas

**Contrato:** darovan_d07_canonical_cities_v0.1.json y validate_d07.py. Las referencias y etiquetas son índices técnicos de hechos preexistentes, no fuente alternativa del canon.

| Grupo | Invariante | Modo de comprobación |
|---|---|---|
| Autoridad | Core → Norgard Defaults → Darovan → Localidad → World State | igualdad de jerarquía y no-runtime |
| Inventario | Treihord, Veldora, Taramin, Syvaris únicos y manuales; Karsath excluida; Arven sin rango de ciudad canónica | ids y flags |
| Fuente Treihord | Treihord.md conserva CANON BASE CERRADO, ~32.000, 8 barrios, 4 plazas, 4 puertas | cotejo literal/estructural |
| Hidrografía | 5 ríos / 4 sistemas; Belara junto sin cruzar Treihord; Veldora independiente; Thalen dos brazos; Fhalion sin navegación probada | datos D02 y campos D07 |
| Fiscalidad | Aduana exterior Veldora, sin arancel interior entre Casas | Norgard Defaults |
| Economía/ecología | Carbón Azurios; Taramin no tala industrial; Syvaris bosques discontinuos/no tala intensiva; Agujas sin residencias permanentes | datos D03/D04 |
| Movilidad | Solo 3 conexiones confirmadas D05, 4 suministros no rutas, sin materializar trayectorias | cotejo D05 |
| D06 | Las cuatro ciudades fuera del generador | manualCityIds y cityGenerationAllowed |
| Urbanismo | Hechos de ciudades con fuentes y propuestas no aprobadas/no localizadas | matriz de facts/layers |
| Datos | UNKNOWN nulos, sin población D08 nueva, coordenadas, distancias, capacidad, cruces, barrios nuevos ni tramos marítimos | controles de campos |
| Motor | Ninguna instancia CoreRPG o Godot por documento | flags de integración falsos |

**Pruebas negativas:** el validador muta el inventario, régimen hídrico, fiscalidad, normativa forestal, geometría, rutas, perfiles y estados de autoría. Debe rechazar cualquier falsa aprobación, hecho sin fuente, población inventada, nuevo barrio Treihord, Puerto/Vena alterados, isla desértica o estado runtime ficticio. Son pruebas de laboratorio contra datos inmutables, sin modificar archivos canónicos.

**Criterio de CI:** Windows 2022 y Ubuntu 24.04 ejecutarán secuencialmente D01, D02, D03, D04, D05, D06 y D07. Informar número real de negativas en salida, y diferenciar primer run y HEAD final si hay commits posteriores. Éxito estático NO acredita juego ejecutado ni canon promulgado.
