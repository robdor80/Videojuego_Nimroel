# DAROVAN D06 — Auditoría estática y entrega a revisión (21-10-2026)

## Base, alcance y autoridad
- Repositorio: `robdor80/Videojuego_Nimroel`; rama: `feat/darovan-d06-asentamientos-ordinarios`.
- Base verificada de `main`: merge PR #30 / D05, commit `0818886f8cc9f91c21b5db00f91feb1b942d230d`. No se ha modificado directamente `main`.
- Entrega: nueve modelos de asentamiento, doce regiones de estudio D01, reglas de esqueleto/posibilidades/condiciones/pesos, ejemplos `TEST_ONLY` y generador determinista **solo de laboratorio**.
- CoreRPG sigue siendo único propietario de población, residencia, empleo, propiedad, inventario y persistencia. Godot continúa como interfaz, sin ejecutar materialización D06.

## Resultados reproducibles

**Primera ejecución verificada en GitHub Actions:** [run #39627654566](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39627654566), disparada por PR Draft D06 #31, `head_sha=72c81554da146813287611248ac04313888f087b`:

| Runner | D01 | D02 | D03 | D04 | D05 | D06 | Resultado de job |
|---|---|---|---|---|---|---|---|
| `ubuntu-24.04` | OK | OK | OK | OK | OK | OK | **SUCCESS** |
| `windows-2022` | OK | OK | OK | OK | OK | OK | **SUCCESS** |

D06: **6 fixtures positivos**, pruebas de ID y pesos deterministas, **20 mutaciones negativas de reglas y 22 negativas de sitio**, todas rechazadas. El validador lee archivos D01–D05 reales del checkout y confirma referencias Core/Default Norgard. Resultado `STATIC OK` sin construcción jugable. Los 22 negativos incluyen denegación expresa de la promoción de un enclave de trabajo sin comunidad residente.

El cierre editorial de este acta puede crear un commit posterior al SHA de la primera ejecución: **para aprobar la PR se requiere inspeccionar también la CI del HEAD final**. Esa evidencia se dejará en la conversación de PR, sin afirmar aquí que un commit aún no ejecutado superó CI.

## Regla de no invención y compatibilidad

- Ciudades Treihord, Veldora, Taramin y Syvaris quedan fuera del generador. Karsath excluida.
- Arven Darovan reconocida; aldeas existentes citadas cualitativamente por Norgard, ninguna localidad nueva ni nombre oficial.
- D02: Belara/Lhera, Veldora, Fhalion y Thalen, cinco ríos/cuatro redes; Treihord junto a Belara, sin cruzarla; navegación Fhalion/Thalen desconocida.
- Bosque de las Agujas sin asentamiento permanente interior. Pilares y Taramin bosques únicos; Taramin sin tala industrial; Syvaris bosque disperso; Arven sin tala industrial.
- D05: tres conexiones modales cualitativas; cuatro relaciones de suministro NO son rutas. Sin nuevos caminos, puentes, puertos, mapas métricos o ferris.
- Las seis instancias son propuestas sintéticas, sin población, coordenadas, nombre, estado guardado ni activos instanciados. No se inventaron hechos históricos.

## Bloqueos conservados

**DAR-P04**, parte pendiente de **DAR-P08**, **DAR-P09**, **DAR-P10** y **DAR-P11**. P01 y P07 fueron resueltas por el autor. Continúan sin definirse emplazamientos y derechos específicos, propiedades/contratos locales, agua potable real, modelos demográficos D08, grafos de accesibilidad D11 y mapa métrico.

## Entregables y siguientes fases

- `Asentamientos/01_ESQUELETO_Y_MODELOS_D06_v0.1.md`.
- `Asentamientos/02_PESOS_Y_GENERACION_D06_v0.1.md`.
- `Asentamientos/03_INSTANCIAS_SEMILLAS_D06_v0.1.md`.
- `Datos operativos/darovan_d06_settlement_rules_v0.1.json`.
- `Datos operativos/darovan_d06_test_fixtures_v0.1.json`.
- `Validacion/d06_generator.py`, `Validacion/validate_d06.py` y matriz.
- Workflow `Darovan static regression D01-D06` Windows/Linux; registro de fase/decisiones/plan.
- `00_Control_del_proyecto/TRASPASO_D07.md` preparado; **D07 NO INICIADA**.
- **D07:** auditoría y diseño manual de cuatro ciudades; **D08:** población, servicios, hogares y profesiones; **D11:** integración CoreRPG/Godot, grafo de rutas real, GIS, persistencia/versiones y pruebas Windows/Android.

**Estado de esta entrega:** documentos y primera regresión completa superados. La PR **permanece Draft, sin fusionar, pendiente de revisión del autor y verificación CI de su HEAD final**.
