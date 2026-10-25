# D12 — Auditoría integral de Casa Darovan (D00–D11)
**Fecha:** 25/10/2026. **Alcance:** territorio documental, JSON, dependencias de CoreRPG y ejecución CI.
**Clase:** auditoría técnica; NO decisión de canon ni prueba jugable. **Estado del dictamen:** ver acta de cierre D12 y resultados CI de la PR Draft.

## 1. Evidencia real de GitHub y línea base
- Repositorio: robdor80/Videojuego_Nimroel. Base comprobada al iniciar: `main` = `1865fb7fedb616ef7abdffbb195d3698825d4c8a` (merge PR #27 NIM-06, 24/10/2026), sucesor de D11.
- D11 PR #37 fusionada 23/10/2026: `028ea86ec69cf2223d0e47b006cbb84554068b91`.
- GitHub Actions posterior al merge D11: run #40031213970 SUCCESS, Ubuntu 24.04 y Windows 2022. CI posterior a NIM-06 en `main`: runs #40099719022 y #40099719008 SUCCESS.
- Comprobadas como fusionadas las PR D00–D11: #14, #15, #16, #17, #20, #30, #31, #32, #34, #35, #36 y #37. Los textos antiguos «no iniciada», «sin fusionar» y «PR Draft» conservan valor histórico, no estado presente.
- D11 fija CoreRPG en `4f282863737bcd8f5add401202a9e1064c133672` (versión 4.13 de referencia); `main` de CoreRPG se comprobó en ese SHA al comienzo de esta auditoría.

## 2. Autoridad y fuentes
Orden: fuentes superiores Nimroel/Norgard → decisiones expresas del autor → fichas de ciudad/territorio → datos operativos derivados → hipótesis/propuestas/sintéticos. Nunca al revés.

Fuentes superiores efectivamente cotejadas: `Norgard/NORGARD.md`, `Norgard/Grandes Casas/grandes_casas.md`, `Norgard/Geografía/{rios_y_lagos,bosques,montanas}.md`, `Norgard/Ciudades/Casa Darovan/Treihord.md`; actas, índices y registro autoral D00–D11. Complementan, no sustituyen, `00_Control_del_proyecto/DECISIONES_Y_BLOQUEOS.md` y sus anexos.
D00 es fotografía histórica: su `arvenAdministrativeOwner: null` precede a la resolución autoral del 21/10. El dato VIGENTE Arven Darovan consta en D01 actualizado, D02, D06, D09, D10 y proyección D11. Cambiar D00 sin actualizar su fuente lock de D11 sería improcedente.

## 3. Revisión transversal
| Frontera | Hecho y límite comprobable | Riesgo rechazado |
|---|---|---|
| D00→D01→D07 | Cuatro ciudades manuales: Treihord, Veldora, Taramin, Syvaris; Karsath excluida | Generar/añadir ciudad principal |
| D01→D02→D03 | 12 unidades cualitativas; 5 ríos/4 sistemas; grafo simbólico 15 nodos/11 aristas | Convertir categorías en polígonos/medidas |
| D02→D04→D05 | Belara junto a Treihord, poca profundidad; transporte mineral por barcaza documentado | Asumir navegación universal |
| D03→D04→D06 | Clima/recursos condicionan viabilidad de modelos, sin localizaciones ni aforos | Inferir mina, explotación o aldea |
| D04→D05→D08 | Cadenas de suministro diferenciadas de conexiones físicas | Hacer carretera Azurios o Pilares |
| D05→D07→D09 | 3 enlaces modales admitidos y 4 relaciones logísticas sin ruta acreditada | Añadir cruces, puentes o escoltas automáticas |
| D06→D07→D08 | Generador de 9 modelos, 12 áreas cualitativas y ejemplos sin instanciar | Recontar escenarios como población real |
| D07→D08→D10 | Conceptos urbanos aprobados no implican diseño de barrios, hogares o temperamentos | Convertir preferencias en NPC |
| D08→D09 | Rangos poblacionales aprobados; fiscalidad y seguridad no inventan censos ni recursos | Crear contribuyentes o guardias concretos |
| D09→D10 | Corona suprema; Syvaris con Armada REAL de Norgard; diversidad personal | Armada Darovan o conducta obligatoria |
| D00–D10→D11 | 11 hashes de fuentes, 5 definiciones tipadas, 8 TEST_ONLY | Equiparar catálogo con simulación |

## 4. Integridad del Content Pack
`ContentPacks/darovan-territory/pack/manifest.json`: pack `nimroel.darovan.territory`, contrato 0.1.0, cinco definiciones: territorio y cuatro ciudades. `authoring/projection-v0.1.json`: once locks por SHA Git, procedencia, políticas de movilidad e indicadores de capacidades NO implementadas. `fixtures/d11-scenarios-v0.1.json`: ocho especificaciones `TEST_ONLY`, expresamente `SPECIFICATION_NOT_EXECUTED`. No se promocionan a canon, partida, física, camino o ejecución temporal.

`Tools/DarovanD11/validate.py` ya prueba hashes, esquemas originales CoreRPG, referencias y negativas; `Tools/DarovanD11/cpp_smoke.cpp` ejercita carga de catálogo y persistencia sintética, NO reglas del territorio. D12 añade `Tools/DarovanD12/validate.py` con comprobaciones ENTRE archivos, lectura censal de archivos Markdown/JSON del territorio, referencias de fuentes y mutaciones adversariales. El workflow conserva regresiones D01–D11 y C++ en ambos SO.

## 5. Distinción de niveles de prueba
**Canon:** identidad/fuentes/decisiones autorales. **Datos:** JSON, validaciones, pack catálogo y contratos de planificación. **Ejecutable comprobado:** compilación/carga/persistencia estructural D11 y, en repositorio Host, integración genérica NIM-06 verificada de forma independiente. **NO demostrado:** economía temporal, transacciones, rutas causales, desplazamientos, materialización de hogares/NPC, gobierno, fiscalidad, clima, cultura social dinámica ni generación jugable de Darovan.

La existencia de NIM-06 NO corrige esta ausencia. No se han alterado CoreRPG, Godot, GDExtension ni fuentes D00–D11.

## 6. Incidencias y decisiones no fabricadas
Registro de clasificación y estados: `D12_REGISTRO_INCIDENCIAS.md`. Matrices: `D12_MATRIZ_COHERENCIA_TRANSVERSAL.md`, `D12_INVENTARIO_CANON_Y_AUTORIDAD.md` y `Contratos_y_runtime/D12_PREPARACION_CORERPG_Y_HOST.md`.
No se valida cartografía métrica, censos exactos, puentes, clima medido, emplazamientos, nuevas rutas, especies, individuos o impuestos.
El cierre documental/técnico no implica plena jugabilidad. Para dictamen A/B/C, consultar `D12_CIERRE_TERRITORIAL.md` después de la última CI.

## 7. Primera CI integral realmente ejecutada
[Actions #40178146688](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40178146688), commit `71fdb5b44bb5c83056cf21dd3a7d841e148b6df6`: SUCCESS en Windows 2022 y Ubuntu 24.04. Log D12: `D12 STATIC PASS: 162 archivos Darovan; 131 Markdown, 19 JSON; 282 referencias a fuentes existentes; 11 fases + pack D11; 17 negativas rechazadas.` D11: 11 locks, 5 definiciones, 8 TEST_ONLY y 23 negativas rechazadas. Compilación nativa y CTest catálogo/persistencia sintética superados. El cierre en el HEAD final requiere nuevo CI (véase PR #38).
