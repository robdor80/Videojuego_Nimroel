# Windows x64 — Pruebas

Base Nimroel `6c7ed6a8013b471be0e66dbc4d5bedaeb3541782`; CoreRPG
`4f282863737bcd8f5add401202a9e1064c133672`. Código verificado por CI:
`c071105fcb02e125641594cea4f859dbaad711a2`.
Godot 4.7.2 Standard; godot-cpp oficial `e83fd0904c13356ed1d4c3d09f8bb9132bdc6b77`
(API 4.5 compatible hacia versiones menores posteriores, comprobada con 4.7.2).
[Pins y hashes oficiales](evidence/dependencies.json).
Resultados nuevos y enlaces de CI: [evidencia compacta](evidence/ci-summary.json).
Las pruebas físicas no están realizadas.
CI final: [39430632471](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39430632471), success.
Checkout automático PR `8c990b3e1d3672b951f545e9028b6b6f7dc94259`,
árbol idéntico al HEAD de código (verificado por API). No se ha fusionado en main.

## Herramientas y procedimiento

Runner windows-2022; Visual Studio 2022, toolset v143 14.44.35207, x64,
Release con CRT /MT en Core, godot-cpp y adaptador. CMake 3.31.6 y Python 3.12.10.
La versión concreta de MSVC/SDK/imagen queda en el log y la evidencia compacta.
Se verifican las descargas oficiales antes de ejecutar Godot 4.7.2.

Comandos CI, desde raíz:

```
python Tools/NIM06/native_lab.py build --functional --target windows
python Tools/NIM06/native_lab.py smoke --functional
python Tools/NIM06/native_lab.py regressions --functional
python Tools/NIM06/native_lab.py export-windows --functional
```

## Comprobaciones independientes

1. C++20 compila CoreRPG, godot-cpp y puente; mapa de enlace requiere ActionEngine,
   Simulation, Persistence, Visibility y ContextBuilder reales.
2. DLL `nimroel_core.windows.x86_64.dll`: PE AMD64 0x8664, punto de entrada
   nimroel_core_init y dependencias inspeccionadas con dumpbin. Se rechazan runtimes
   C++ dinámicos incompatibles; hashes concretos en evidencia.
3. Importación y cierre del editor, salida 0 y NIM06_EDITOR_IMPORT_OK, sin ERROR.
4. Smoke desde Godot registra clases y ejecuta mundo, acciones, rechazos,
   proyecciones, población, guardado/restauración y continuación RNG.
5. Regresiones NIM-01, NIM-02, NIM-03, NIM-04 y teclado, sin modificar sus scripts.
   Suites offline de Tools/NIM03 y Tools/NIM04 ejecutadas también con extensión cargada.
6. Exportación debug EXE/PCK; DLL empaquetada idéntica a compilada. Se ejecuta
   realmente el `.console.exe --headless -- --nim06-self-test` exportado y se exige
   informe ok, salida 0 y ausencia de ERROR. Exportar por sí solo no basta.

Las pruebas incluyen schema/versiones/tipos/desbordamiento, ciclos/self-link,
no-op, revisión obsoleta, precondiciones, batch malformado, denegación de destino,
suplantación de actor, grants, sesiones NPC/AI de consulta, oculto frente a ausente,
truncamiento, contexto consumido, deduplicación, memoria recordada, corrupción y
truncado de save, aislamiento/destrucción/cierre e hilo incorrecto.

RNG independiente: seed 18446744073709551615, stream 7, rango [1,1000000],
primeros valores 714378, 888664, 173266, 20245. Calculados con el fixture Python
upstream tests/fixtures/actions_simulation_reference.py adaptando únicamente seed
al valor de la prueba; el fixture no importa ni ejecuta CoreRPG. Los valores
literales están en la prueba Godot, no en lógica de juego.

La capa Controller se prueba de extremo a extremo: crear, consultar, guardar,
actuar, consultar nuevo hecho, cargar, abrir sesión nueva y comprobar continuidad.
Las operaciones gráficas táctiles/ratón no se dan por probadas con headless.

## Evidencia y límites

Ver ci-summary.json para run/job, SHA compilado, número exacto de checks, hashes
DLL/EXE/PCK y versiones observadas. Los logs completos están en Actions y artefactos.
La primera implementación anterior obtuvo 108 checks, pero no se presenta como
validación de los controles añadidos después. El resultado aceptable es el run
final enlazado en la evidencia compacta.

MSI Raider Windows 11: pendiente de ejecución física. Se entregan los archivos
exportados juntos, con instrucciones en 09. No hay firma Authenticode de producción.
No se ejecutó una suite completa upstream CoreRPG ni un perfil ASan del adaptador;
no se declaran esas verificaciones como realizadas.

## Resultado final nuevo

- [Job Windows](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39430632471/job/118654458429): **success**.
- MSVC **MSVC 19.44.35229.0**, SDK **10.0.26100.0**, toolset fijado 14.44.35207.
- Core/godot-cpp/puente: compilación y enlace satisfactorios. DLL **472064 bytes**,
  PE x64 correcto; dependencia observada **KERNEL32.dll**.
- Editor: importación/cierre limpio y **124 checks aprobados**.
- EXE exportado: **124 checks aprobados**, salida 0, sin ERROR.
- Cinco suites Godot de regresión aprobadas; Python **8/8 y 29/29**.
- [Artefacto publicado](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39430632471/artifacts/12268685260), 30 días.

| Archivo | SHA-256 |
| --- | --- |
| nimroel_core.windows.x86_64.dll | `3f93adf7e03a4aedcb3d1f04b74c8d2b950908a686f2cbd7a9078a98bdfc734e` |
| Nimroel_NIM06_Functional.console.exe | `26da30e450d68668992cff319620e6d788fdcfa150534310cffa733a44b6f91c` |
| Nimroel_NIM06_Functional.exe | `9f44a61a9589e5dba56aa5001882d681f4ca6cca992ba3a3a24e23aafddf69af` |
| Nimroel_NIM06_Functional.pck | `947c1d5e1218ea0827a3af8c25ba3401f88b98a724411fe818247a1aba5804e7` |

[Extracto permanente del log](evidence/windows-excerpt.txt).
[Regresiones Linux independientes](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39430632469).
MSI físico continúa pendiente; no se sustituye por estos resultados.
