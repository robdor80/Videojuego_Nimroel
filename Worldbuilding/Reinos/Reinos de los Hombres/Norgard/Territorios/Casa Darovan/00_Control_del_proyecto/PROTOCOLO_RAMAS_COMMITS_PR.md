# Protocolo aprobado — una conversación y una rama por fase
**Directriz del autor (Darovan 1, 15-10-2026):** cerrar D00 aquí, abrir D01 y siguientes en conversaciones nuevas.

1. Leer el control de fases, el traspaso, el canon original completo y la matriz de fuentes; consultar estado real de GitHub antes de actuar.
2. **Iniciar la fase siguiente desde `main` únicamente cuando la anterior esté fusionada.** Si aún hay PR pendiente, esperar o solicitar autorización de rama encadenada con dependencia explícita; jamás fingir que `main` contiene trabajo no fusionado.
3. Abrir rama `feat/darovan-dXX-descripcion` y trabajar con commits verificables `docs(darovan-dXX): …`, `data(darovan-dXX): …`, `test(darovan-dXX): …`.
4. En cada documento: identificar hecho canónico y ruta, inferencia geográfica, propuesta y decisión pendiente. No duplicar sistemas universales ni alterar una ciudad aprobada.
5. Ejecutar verificaciones: JSON parseable; IDs únicos; rutas de fuentes; herencia de autoridad; coherencia geográfica; diff limitado; pruebas runtime solo cuando se ejecute el motor.
6. Emitir acta de cierre con limitaciones y pruebas. PR en Draft durante implementación; marcar lista para revisión cuando el paquete documental esté listo.
7. **Nunca fusionar a `main` sin autorización expresa.** Cierre documental, PR lista, merge y validación runtime son estados **diferentes**.
8. Cada nueva conversación revisa el HEAD, la base de su PR y las dependencias; no se continúa otra fase en la conversación actual.

Requieren al autor: alterar topónimos o ciudades canónicas, mapas de frontera definitivos, identidad histórica, personajes significativos o hechos políticos trascendentes. Las decisiones técnicas menores pueden prepararse sin consultarle.
