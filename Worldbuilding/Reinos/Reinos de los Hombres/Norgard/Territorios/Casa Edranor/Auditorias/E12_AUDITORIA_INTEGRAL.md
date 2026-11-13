# E12 — Auditoría integral de Casa Edranor (E00–E11)
**Inicio:** 13/11/2026 · **Base real comprobada:** `main` `680b757ff4593a825dcd40ee827a479eb0a8ce21`.
**Alcance:** canon documental, contratos JSON, integridad Git, laboratorio CoreRPG y matriz de regresión. **NO** auditoría de juego completo.

## 1. Estado comprobado en GitHub
Las PR territoriales Edranor están fusionadas:
`E00 #51`, `E01 #52`, `E02 #53`, `E03 #54`, `E04 #55`, `E05 #56`, `E06 #58`, `E07 #59`, `E08 #60`, `E09 #61`, `E10 #62`, `E11 #63`. No existe PR Edranor #57; no inferir fases omitidas.
E11 se fusionó el 13/11/2026 (UTC) en el SHA base indicado. Última ejecución E11 publicada en acta: [Actions #43335463248](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/43335463248), HEAD `52891d2b0b6eb74789f3c8659ad5ab7fbe208d10`, Ubuntu 24.04 y Windows 2022 SUCCESS. Esa ejecución acredita el HEAD E11 probado, **no la futura PR E12**.

## 2. Inventario inicial
En el árbol territorial de `main` anterior a E12 había **121 archivos**: 106 Markdown, 15 JSON. El nuevo índice E12, matrices, acta y estado son adiciones; los once archivos `Datos operativos/edranor_e00...e10` se dejan intactos para preservar hashes. El Content Pack E11 añade cinco recursos, manifest, sidecar con once sourceLocks, contrato y doce casos de laboratorio.

## 3. Contraste superior y entre territorios
Se han leído `Norgard/NORGARD.md`, `Grandes Casas/grandes_casas.md`, `Norgard Defaults/README.md`, `Casa Valrik/territorio_valrik.md` y la auditoría D12 de Darovan. La autoridad de Corona es única; las Casas administran, no son soberanas. Los datos Valrik/Treskal y Darovan/Treihord **no son valores por defecto**: no importar barcos, minas, rangos demográficos, rutas ni sistemas hidrográficos. La matriz y el inventario enumeran las afirmaciones Edranor verificables.

## 4. Anclas y excepciones
Dorth (capital y tintos), Lumina (blancos, mercado anual, plaza alargada), Karsath (vino escaso, contexto lacustre sin ribera adjudicada) y Rodas (aldea Corona Aethros, Casa Druídica custodiada no religiosa) son cuatro lugares protegidos. La Corona conserva jurisdicción, justicia, seguridad, impuestos y mando berserker de Rodas. Hallheim es capital real ajena al territorio Edranor y no aparece como DefinitionId de lugar en E11. Heráldica y viticultura proceden de fuentes superiores.

## 5. Verificación transversal, limitaciones y semántica
- E01–E06 reutilizan siete unidades cualitativas, sin mapa métrico; E02 conserva Lurien/Antela como regionales `UNKNOWN` respecto al perímetro.
- E03–E04 no extienden viñedos al norte polar; Bosque Alto aporta madera para barricas, no propiedad o tala sin derechos.
- E05 contiene cuatro cuestiones de ruta, **cero enlaces físicos confirmados**. Ni E07 ni E08 crean población o caminos.
- E06 ofrece ocho modelos con prohibición de generar los cinco anclajes. Los ejemplos sintéticos no son settlements del World State.
- E08 ofrece quince servicios y dieciséis familias de oficios; E09 diez roles y once clases de permiso; todos sin personas, tarifas, edificios ni expedientes reales.
- E10 propone once identidades, ocho conflictos, ocho escenas y una familia sin filiación legal ratificada. Su aprobación como texto de trabajo NO activa NPC, NAME/KIN, guerras o diplomacia ejecutable.
- E11 usa contrato JSON CoreRPG 0.1.0 con cinco DefinitionIds, once locks SHA y doce TEST_ONLY. No contiene lógica regional ejecutable; fuente de datos y validación no equivalen a instancia real.

## 6. Niveles de evidencia
| Nivel | Evidencia y límite |
|---|---|
| I — Fuentes | Canon Norgard y decisiones autorales, no verdades producidas por validadores |
| II — Estático | Documentación, 11 blobs, punteros, 5 definiciones, contratos y mutaciones |
| III — C++ nativo | E11 carga catálogo, binding sintético de Dorth/Rodas, save/load, determinismo, CTest en CI |
| IV — Juego Godot | **NO VERIFICADO** para Edranor: no GDExtension/escena 2D, caminos, economía, hogares, NPC, guardias, impuestos ni misiones |

## 7. Procedimiento final
El workflow E12 deberá ejecutar validador transversal propio, E00–E10, E11 con esquemas oficiales fijados y C++ CTest en Windows/Linux, todos contra el **HEAD exacto de E12**. Comprobar ausencia de cambios fuera de E12, sin regresiones del proyecto, aprobación del autor y no deriva de `main` antes de fusionar. El reporte de GitHub Actions/PR, y no una frase escrita de antemano, será la prueba final. Si fallara alguna puerta crítica, no fusionar.

## 8. Dictamen de auditoría
**Cierre documental/contractual potencialmente favorable, condicionado a las puertas anteriores y al registro de incidencias.** No se elimina deuda por silencio ni se asegura jugabilidad. EDD-06 se resuelve como aldea; EDD-01/02/03/04/05/07/08 continúan abiertos. Ninguna rama posterior debe tratar `PROPUESTA_E10` como `CANON_REPO` sin decisión expresa adicional.