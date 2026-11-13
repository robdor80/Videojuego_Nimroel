# G00 — Acta de fundación y condiciones de cierre
**Autoriza:** usuario en conversación de 13/11/2026 para trabajar, publicar y **fusionar G00 si pasa puertas**.
**Alcance:** documentos, tabla de topónimos existentes, mapa cualitativo y JSON no-runtime. No se modifica canon superior ni otras Casas.

## Puertas verificables
1. Existencia de 18 fuentes versionadas, manifest parseable y sin IDs duplicados.
2. Rechazo por mutaciones: soberanía, moneda/aduanas, guerra autónoma, anexión Treskal, reclasificación Forja, usurpación de mando en guerra, Metal Estelar fuera de Azurios, mapas metricados, propuesta promovida a canon o runtime activado.
3. `Tools/GaldrenG00/validate.py` ejecutado en Windows y Ubuntu, en **HEAD exacto**, con negativas.
4. Diff **solo** Casa Galdren G00, `Tools/GaldrenG00` y workflow G00; comprobar que `main` no derivó antes de fusionar.
5. Ninguna deuda de canon de G01 bloquea G00 siempre que se preserve `UNKNOWN`.
6. Documentación no igual a validación del motor ni a juego funcional.

## Dictamen del documento
La estructura es **apta para CI**. El resultado y los números de ejecución se reflejarán en PR/registro final **solo después** de comprobar Github Actions, nunca antes. G01 queda expresamente sin iniciar.
