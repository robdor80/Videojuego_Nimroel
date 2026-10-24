# D09 — Matriz de invariantes y regresión estática

**Alcance:** diseño y JSON de planificación (NO RUNTIME). El validador `validate_d09.py` tiene dependencias solo stdlib y se ejecuta en Windows y Linux junto a D01–D08.

| Categoría | Invariante / caso adversarial | Fuente |
|---|---|---|
| Gobierno | Corona suprema, Casa no legisla ni es soberana, Arven Darovan, Karsath excluida | organización Reino / D00–D07 |
| Administración | centro Treihord, funciones delegadas; consulta no crea órgano ni cargo singular | lote G01–G03 |
| Justicia | misma ley; cuatro ciudades; itinerancia rural sin itinerario inventado | E9 / G04B |
| Pena capital | confirmación obligatoria; identidad confirmante Darovan UNKNOWN, sin ejecutar por defecto | E9 / G05C |
| Casas menores | identidad/existencia específicas UNKNOWN; no autogeneración | E5 / G06A |
| Fiscalidad | seis categorías EXISTENTES, sin gravámenes territoriales nuevos o aduanas entre Casas | E8 / F01B |
| Veldora | aduana exterior bajo autoridad fiscal real; Darovan coopera sin apropiarse de autoridad | E8 / F02C |
| Crisol | ensaye, lingote y fiscalización no equivalen a moneda o control operativo real | E2/E8 / F03B |
| Remesa | período, porcentaje, tarifas UNKNOWN | E8 / F04C |
| Guardia | Guardia de Casa, urbana, profesional, reserva, fuerza no fungible; edades 18+ | E5 / D01–D03 |
| Syvaris | Darovan seguridad civil terrestre; Armada solo Corona | E6 / D04A |
| Patrol/Escorts | hechos/recurso/custodia, sin ruta, plantilla o escolta gratuita | D05 / S01B S02C |
| Vena | cerrada; autorización Crisol+Bóveda registrada | canon Treihord / S03B |
| Geografía | D05: solo tres conexiones acreditadas, 4 suministros no equivalen a ruta | D05 |
| Demografía | rangos D08 no generan dotación ni nuevas villas | D08 |
| Persistencia | fixtures no crean World State, NPC, inventarios ni titulares | NIM Core/ D11 |
| Referencias | rutas fuente en repo y 17 decisiones autorales exactas, IDs únicos | GitHub main D08 + lote D09 |

## Casos sintéticos
14 ejemplos `TEST_ONLY`: robo almacén, conflicto comercial, aduana exterior, amenaza minera sin emplazamiento real, ataque a caravana en camino acreditado, conflicto jerárquico, incendio, coordinación naval Syvaris, acceso Vena, tasa interior ilícita, menor reclutado, pena capital sin confirmante, pesca local y falsa acuñación. Ninguno es un evento histórico ni una implementación que ya funcione.

## Mutaciones
La prueba negativa cambia cada una de las **17 decisiones** y agrega alteraciones hostiles de competencia, moneda, fiscalidad, rutas, Armada, fuerza, censos, Justicia, fuentes y fixtures. Cada perturbación debe ser rechazada por `validate_d09.py`. Ejecutar 1 vez el paquete final D01–D09 en `darovan-static-regression.yml` y observar dos jobs `ubuntu-24.04`/`windows-2022`. Una CI estática **no** valida IA, patrullas reales, detenciones, CoreRPG, Godot ni GDExtension.
