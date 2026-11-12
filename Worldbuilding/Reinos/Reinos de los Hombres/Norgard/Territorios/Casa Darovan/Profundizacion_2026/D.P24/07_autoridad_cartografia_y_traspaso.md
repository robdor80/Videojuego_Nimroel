# D.P24/07 — Autoridad, cartografía y contrato de implantación rural

## Jerarquía de fuentes, sin redefinir Nimroel
`Nimroel Core → Norgard Defaults → Casa Darovan → sitio autorizado → WorldState`. D01/D.P13 aportan relieve; D02 ríos; D03 clima; D04 economía; D05 los vínculos de transporte limitados; D06 nueve modelos y puertas; D08 hogares y necesidades; D09 autoridades y justicia; D10 cultura; D.P14–D.P18 método; D.P20–22 contenido urbano editorial. D.P23 existe solo como trabajo de PR Draft #46 al crear esta rama.

Las nueve etiquetas S01–S09, sus nombres y personajes **no superan por sí mismos ninguna puerta D06**; en JSON todos tienen `siteId: null`, `geometry: null`, `actualResidentCount: null`, `instantiated: false`. Los nombres no son ubicaciones verificadas del mapa del proyecto.

## Evidencia requerida antes de cada promoción
1. Identificar polígono o sitio real en mapa autorizado, georreferenciación compatible y derecho de uso.
2. Verificar terreno seguro, drenaje y riesgo D03; no usar solo color de mapa.
3. Identificar agua potable con calidad/acceso; no equiparar mar, curso industrial, deshielo o cauce estacional con fuente doméstica.
4. Comprobar acceso físico modal concreto; `d05_road_veldora_treihord` no prueba que pase por S07; `d05_belara_shallow_haul` es transporte industrial de poco calado; `d05_vena_restricted` NO es vía civil.
5. Acreditar sustento viable, recursos finitos, derecho y comunidad residente para elegir clase aldea/pueblo/villa. Un enclave sin residentes sigue siendo instalación.
6. Verificar capacidades y proveedores reales para cada necesidad D08. Un edificio opcional no aparece automáticamente.
7. Definir los NPC y hogares seleccionados con identidad estable y conocimientos propios, sin crear parentesco por coincidencia de nombres.
8. Registrar una decisión explícita de materialización física y someter el paquete a pruebas de mapas, identidad, legalidad y persistencia.

**No se autoriza:** crear puentes, vados, ríos, pozos, carreteras, barcas, muelles, minas, nuevos bosques, aldeas dentro de las Agujas, superávit hídrico en Syvaris, tala intensiva en Arven/Taramin, ceca fuera de Hallheim, armada propia Darovan, aduanas internas, impuestos no acreditados, escuelas/hospitales universales ni eventos históricos de la fase.

## Contrato de la escena rural
Entrada propuesta (NO API en producción):
`{siteId, actorId, action, observedAt, evidenceRefs, knowledgeMask, rightsRefs, stockRefs, capacityRefs, timeBudget, expectedRevision, idempotencyKey}`.
Salidas posibles: `allowed`, `blocked_missing_evidence`, `blocked_rights`, `blocked_resource`, `blocked_access`, `blocked_time`, `offered_alternative`. Solo CoreRPG ejecutará transacciones atómicas; decisiones literarias pueden informar al Máster IA sin efectuar mutaciones.

**Criterios negativos innegociables:** no decidir `true` cuando evidencia sea `null`; no producir recursos de `UNKNOWN`; no mutar por diálogo; no repetir una transacción bajo mismo idempotencyKey; no entregar información que el NPC no conozca; no promover la propuesta a localidad por pasar tests de sintaxis.

## Diferencias respecto a D.P15
D.P15 definía nueve modelos y dependencias genéricas. **D.P24 añade autoría específica**: nueve nombres y dilemas, doce individuos diferenciados, diez cadenas dramatizadas, cuatro recuerdos, cinco arcos y ocho escenas; no reemplaza tablas de cobertura ni multiplica generadores. D.P25 coordinará personajes y conflictos entre localidades sin convertir este paquete en una simulación.

## Bloqueos y seguimiento
- **Canon base protegido:** las cuatro ciudades; geografía e hidrología D01/D.P13; Arven Darovan y Manto Verde; bosque Agujas sin residencia interior; ley real.
- **DEPENDENCY:** PR #46 D.P23 debe resolverse antes de declarar cerrado el conjunto D.P20–D.P24; esta rama parte de main para evitar incorporar trabajo no fusionado.
- **UNKNOWN:** coordenadas de S01–S09; cantidades de aldeas; números de hogares; caminos, puertos, aguas/pozos, producción e instalaciones; estado de cada persona; precios, salarios, fechas y trayectos.
- **VALIDACIÓN:** script independiente comprueba forma, referencias, IDs y límites; CI en Windows y Ubuntu si se incorpora workflow. Pruebas del motor y cartografía quedan para una implementación futura.

## Dictamen
**Completo como creación editorial**, **pendiente de CI y revisión Git**, **no instanciado en videojuego**. Ni el texto ni la validación son una prueba de que el jugador pueda visitar un núcleo todavía sin mapa.
