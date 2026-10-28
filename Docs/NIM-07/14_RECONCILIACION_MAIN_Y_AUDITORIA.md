# NIM-07 — Reconciliación controlada con main y auditoría de integración

**Fecha:** 28 de octubre de 2026. **Estado:** reconciliación preparada; pendientes las regresiones y la prueba Android física.

## Autoridad y procedencia

- Rama original NIM-07 I1–I4, auditada: `feat/nim-07-first-rpg-experience` en `333f7d124d22a4f6b5e23d92cab3df1e39b456d3`. **Intacta.**
- `main` en `c12dc6b8162f1f20eb92adb5724714da5d63a7e9`, después de Darovan D12 y D.P13. **Intacta.**
- Base común: `1865fb7fedb616ef7abdffbb195d3698825d4c8a`.
- Divergencia antes de reconciliar: NIM-07 **23** commits exclusivos y `main` **36** exclusivos.
- Rama independiente de integración: `chatgpt/nim07-reconciliacion-main-20261028`.
- Merge commit genuino de dos padres: `a62cf1f663e166710c597f243199089097583424` con padres ordenados `333f7d...` (NIM07) y `c12dc6b...` (`main`).

## Método y verificación estructural

Se compararon las rutas cambiadas de ambas ramas desde la base común: **50 rutas** en NIM-07 y **55 rutas** en `main`, sin ningún solapamiento. Se construyó un árbol de Git desde el árbol exacto de NIM-07, añadiendo únicamente las **55 entradas blob** del árbol de `main`, conservando rutas, modos (100644) y SHAs. Se creó un commit Git real con **dos padres** y se publicó solamente en la rama temporal, sin rebase ni force push.

Verificación exhaustiva del árbol combinado:

- Árbol fusionado: `e6b4c1fd62d3ac28d64141721b7ea49885f9d0cb`.
- Entradas blob esperadas y observadas: **1419**.
- Árboles recursivos completos, ninguno truncado.
- Se comparó la **totalidad** de rutas y valores SHA/modo con el resultado esperado: tomar de `main` todas sus rutas exclusivas modificadas y de NIM-07 todo lo demás.
- **Desviaciones: 0.** La rama fusionada incorpora los datos, validadores, workflows y documentos de Darovan D12/D.P13 tal como están en `main`, sin convertirlos en el fixture estructural de Treskal ni modificar el pack original.
- Este control acredita **integridad de Git**, pero **no sustituye** los tests funcionales cruzados.

## Plan de pruebas cruzadas

Se añadió el workflow `.github/workflows/nim07-integration-audit.yml` para ejecutar **D01–D12, D11 ContentCatalog C++ y D.P13** en Windows 2022 y Ubuntu 24.04 sobre el árbol reconciliado. Reutiliza scripts exactos, acciones fijadas y versión CoreRPG fijada en la infraestructura de Darovan; el workflow original D01–D12 y el D.P13 de `main` se mantienen idénticos.

En paralelo debe ejecutarse el workflow NIM-06 native, Windows x64 + Android ARM64/control Linux, con las regresiones I1 **48**, I2 **37**, I3 **51**, I4 **113** y NIM-06 **129**, Host NIM01–05 y exportaciones EXE/APK. El nuevo workflow de integración no reemplaza el de NIM-06.

**Resultados de CI:** pendientes de registrar tras abrir PR Draft. No interpretar un workflow iniciado como prueba satisfactoria hasta comprobar ambos jobs y los logs.

## Pruebas de dispositivos y presentación

- MSI Raider GE78 HX, Windows 11: el autor verificó manualmente I4 (guardado, cierre de proceso, reanudación directa y consultas) en siete pasos satisfactorios el 28/10/2026. Se hizo **sobre la compilación I4 anterior a esta reconciliación**, no sobre un export nuevo de la rama reconciliada.
- Samsung Galaxy Tab S9+, Android ARM64: **pendiente de prueba física**; el APK original I4 había sido compilado y verificado pero no ejecutado en tablet.
- Una PR Draft a `main` puede prepararse para revisión, **sin fusionarla ni activar auto-merge**. La decisión de pasar a Ready/Merge y el cierre completo de NIM-07 corresponden al propietario.

## Restricciones preservadas

No cambiar canon, CoreRPG, versiones fijadas, política IA, el contenido V001, las ramas originales ni `main`. No iniciar NIM-08. El único archivo nuevo específicamente de reconciliación a incorporar como CI es el workflow de regresión integral y esta evidencia documental.

**No es un informe de aprobación final hasta comprobar las CI y las pruebas de dispositivos pendientes.**
