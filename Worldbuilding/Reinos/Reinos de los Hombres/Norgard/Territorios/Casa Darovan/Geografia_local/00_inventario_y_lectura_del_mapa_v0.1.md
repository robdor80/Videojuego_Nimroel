# Darovan — lectura cartográfica e inventario de relieve
**Estado:** inventario de trabajo; hechos comprobados separados de observación y propuestas.

## Fuente gráfica
Recorte del mapa oficial de Nimroel facilitado por el autor en «Darovan 1». La línea roja es una delimitación visual de estudio, no una frontera georreferenciada aprobada. En esta fase no se incorporan coordenadas ni topónimos nuevos.

## Lugares canónicos administrados por Darovan
1. **Treihord:** capital; interior occidental, sector de Valkram/Belara. Canon urbano independiente (diseño base cerrado).
2. **Veldora:** gran puerto comercial en el Golfo de Veldora.
3. **Taramin:** ciudad pesquera de la península homónima, junto a los dos brazos finales del Thalen.
4. **Syvaris:** ciudad insular situada junto a una bahía principal. **Isla de Syvaris administrada por Casa Darovan**.

**No adjudicar Karsath a Darovan:** registro de regiones visuales de Norgard la sitúa en región central. **Isla de Arven:** occidental, frente a Veldora, con aldeas; adscripción político-administrativa pendiente de comprobación/autor.

## Accidentes geográficos existentes, sin reinterpretaciones
- **Montes Valkram:** eje montañoso norte-sur, oro/plata; Belara nace en vertiente occidental y Lurien en vertiente oriental.
- **Montañas Elyra:** más meridionales, prolongación en la península; también minerales preciosos.
- **Río Belara:** nace en sector septentrional de vertiente occidental de Valkram, pasa junto a Treihord, desemboca en Golfo de Norgard. Su puerto urbano es industrial, de barcazas pequeñas.
- **Río Lhera:** se separa del Belara; desemboca en Golfo de Veldora; discurre junto al Bosque de las Agujas.
- **Río Veldora:** cauce independiente del Belara/Lhera; desemboca en Golfo de Veldora y da nombre a ciudad.
- **Río Thalen:** península meridional; tramo final en dos brazos rodea a Taramin; desemboca en Golfo de Norgard.
- **Golfo de Veldora**, **Golfo de Norgard**, fachada del **Mar del Crepúsculo / Ishalien**.
- Bosques: **Agujas**, **Linde** (camino Veldora–Treihord), **Pilares** (apuntalamiento minero), **Taramin** (gradiente norte-sur), **Syvaris** (dispersos), **Manto Verde de Arven**.
- **Isla de Syvaris:** calas y bahía principal, sectores secos y luminosos, algunos más verdes; no desierto.
- **Isla de Arven:** isla media con bosque continuo de coníferas aprox. 90 %, aldeas costeras; su administración exacta requiere confirmación.

## Observaciones del recorte, sin carácter de canon adicional
- La sección continental occidental muestra un mosaico de cordillera, masas forestales y ramales de agua.
- Una península meridional larga y una isla separada a sureste generan barreras de movilidad y rutas marítimas potenciales.
- Al norte de las cordilleras hay regiones de tonos fríos/nieve; la representatividad estacional de los colores no está fijada.
- La imagen no basta para inferir si cada trazo azul es un río permanente, brazo fluvial, arroyo estacional o simple decoración.

## Capas técnicas propuestas, aún no parametrizadas
`administrative_owner` (solo explícitos), `canonical_places`, `watercourse_graph`, `basin_ids`, `relief_regions`, `coastal_segments`, `biome_transition`, `resources`, `routes`, `navigation_constraints`, `settlement_suitability`.

### Invariantes para el futuro motor
- No invertir drenaje contra el relieve; ningún afluente nuevo crea conexiones canónicas prohibidas.
- Conservar identidad separada del Veldora y la bifurcación Belara/Lhera.
- No extender navegación profunda a Treihord: solo barcazas de poco calado en su tramo de Belara.
- No convertir toda Syvaris en selva ni toda Taramin en desierto; respetar gradientes.
- No importar a Darovan topónimos, porcentajes ni rasgos exclusivos de Valrik/Treskal.
- Zonas naturales no coinciden necesariamente con fronteras administrativas.

### Fuentes
`Norgard/Grandes Casas/grandes_casas.md`, `Norgard/Geografía/{montanas,rios_y_lagos,mares_y_costas,bosques,regiones_naturales,geografia_general}.md`, `Norgard/Clima/clima_general.md`; `Direccion artistica/Biblia visual/Culturas/Norgard/Datos operativos/norgard_regions_v0.1.json`.
