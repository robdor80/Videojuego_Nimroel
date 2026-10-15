# DAROVAN D01 — Acta de cierre documental y validación (15-10-2026)

**Fase:** D01 — Geografía y orografía. **Estado:** CERRADA DOCUMENTALMENTE; **PR #15 abierta y pendiente de merge**. No se proclama canon adicional, cartografía métrica ni validación de motor. **Origen:** main con PR #14 ya integrada (merge 73aa5c4691a3dc07ca588c07a7ce267a69fdd085). **Rama:** feat/darovan-d01-geografia-orografia.

## Inventario de la entrega
- Marco físico de Norgard occidental: Valkram/Elyra, norte frío, península Taramin, Syvaris/Arven, costa, golfos.
- 12 subzonas/códigos operativos cualitativos: ninguna frontera, altitud ni topónimo nuevos.
- Corredores/barreras físicas documentados, con fase futura responsable (D02–D07).
- Perfil JSON de planificación, con jerarquía, fuentes reales, cuatro ciudades protegidas, anclas de drenaje canónico y zonas con administración UNKNOWN.
- Dependencias para cartografía futura, separando relieve físico, hidrografía, cobertura vegetal y jurisdicción.
- Matriz D01 de 18 invariantes y script de prueba estática reproducible.
- Registro/README/plan actualizados para reflejar la integración real de D00 y el carácter documental de D01.
- Documento de transferencia a D02, sin iniciar la fase.

## Verificaciones ejecutadas y ámbito
- **PR D00:** #14 consultada en GitHub; merged=true; main de base en commit 73aa5c4691a3dc07ca588c07a7ce267a69fdd085.
- **Estructura JSON:** parseo real contra contenido descargado de la rama; se verificaron 15 grupos lógicos, incluidos 12 IDs únicos, cuatro ciudades manuales, administración y anclas fluviales.
- **Referencias:** 12 sourcePaths diferentes comprobadas contra el árbol GitHub main; sin rutas huérfanas.
- **Semántica:** lectura de originales de geografía, ríos, montañas, bosques, mares, clima, Grandes Casas, Treihord y Core; contrastadas invariantes con índices D00.
- **Alcance de Git:** primer diff contra main mostró exclusivamente seis archivos añadidos bajo Casa Darovan, dos commits, ninguna modificación original. El diff final debe reevaluarse al publicar esta acta y actualizaciones de gobierno.
- **Runtime:** NO ejecutado. Ninguna simulación CoreRPG, Godot, compilación ARM64, generación territorial ni gameplay certificado. La validación corresponde a documentación/JSON.

## Regresiones y decisiones preservadas
Belara junto a Treihord, no dentro; barcazas pequeñas, carbón Azurios; Lhera nace de bifurcación Belara y acaba en Golfo Veldora; río Veldora es independiente; Thalen bifurcado al final en Taramin; cuatro ciudades Darovan y Karsath excluida; Arven sin jurisdicción atribuida; Agujas sin poblados interiores; Syvaris insular cálida seca/verde variable, Taramin peninsular no desierto uniforme; Valkram montaña compartible y nunca polígono automático.

## Límites y pendientes
No se ha aprobado escala de mapa ni fronteras; no hay densidad, coordenadas, altitudes, pendientes métricas, trazado costero georreferenciado, rutas, puentes, afluentes nuevos ni cuencas menores. Arven permanece DAR-P01; cotas y límites DAR-P04; identificación del río visual tras Veldora DAR-P07; drenaje D02; clima D03; transporte D05; ciudades D07.

## Puerta de salida y autorización
La PR #15 puede revisarse como documentación completa, con pruebas estáticas repetibles. Revisión humana y decisión de fusionar corresponden exclusivamente al autor. **No abrir D02 desde main sin confirmar la integración de PR #15.** Ningún resultado documental implica aprobación automática de canon.
