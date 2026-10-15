# Acta de cierre — DAROVAN D00 (15-10-2026)
**Resultado:** CERRADA A NIVEL DOCUMENTAL Y DE ESTRUCTURA. **PR #14 pendiente de revisión/fusión**. **D01 no iniciada.**
Este acta pertenece a la rama `feat/darovan-01-auditoria-base-20261015`; no se atribuye el contenido a `main` mientras siga sin fusionar.

## Entregables cerrados
1. Inventario de canon de Casa Darovan, Norgard, recursos, geografía y Treihord; matriz de **13 fuentes** con SHA de blob en `MATRIZ_FUENTES_Y_AUTORIDAD_v0.1.md`.
2. Estructura territorial con índices README, separando áreas temáticas, asentamientos ordinarios, **cuatro ciudades manuales** y contratos no-runtime.
3. Anclas de Treihord extraídas del documento completo original (2.374 líneas) sin moverlo ni copiarlo.
4. Hoja de ruta D00–D12, criterios generales y metodología de asentamientos sin extrapolar reglas Valrik.
5. Registro de fases, decisiones del autor y protocolo GitHub, continuidad `Darovan 2 — D01`.
6. Manifiestos JSON de arranque y anclas con herencia, ciudades protegidas y pendientes explícitos.

## Auditoría de coherencia
- Canon de Treihord: **Belara** adyacente, no río interior; puerto industrial de barcazas de poco calado; barrios/plazas/puertas preservados; El Crisol no es ceca, La Vena es custodia, carbón de Azurios. Se mantiene referencia a su archivo canónico.
- Casa Darovan: Treihord, Veldora, Taramin, Syvaris; Karsath excluida por decisión expresa del autor.
- Arven: isla occidental forestal; **adscripción administrativa no verificada** y expresamente no inventada.
- Bosque de las Agujas: **ninguna aldea ni población permanente en su interior**, regla vigente para fases posteriores.
- Clima: Taramin semiárida de transición (no desierto uniforme), Syvaris insular cálida con gradientes internos.
- Contratos: Core y Norgard se referencian, no clonan; Valrik/Treskal aporta arquitectura metodológica, no rangos demográficos ni su identidad productiva.

## Verificaciones GitHub ejecutadas para la publicación
- Comparación contra `main` antes del acta: **39 ficheros añadidos**, **ningún fichero modificado del canon preexistente** y **ningún cambio fuera de la carpeta territorial Darovan**.
- `README`, registro de fases, anclas JSON y referencias principales descargados de la rama para inspección; parseo JSON de anclas realizado.
- **13 rutas de fuentes canónicas verificadas** contra el árbol de `main` al preparar estructura.
- Comprobado: D00 marcado como cerrada documentalmente, D01 no iniciada, cuatro ciudades en anclas, Karsath excluida, Belara presente, Arven sin dueño declarado, runtime marcado `false`.
- Tras incorporar esta acta se espera **40 archivos nuevos** en la rama con cambios limitados a Darovan; el recuento definitivo se verifica al publicar el cierre.

## No afirmamos haber hecho
- No se ha ejecutado simulación procedimental, CI de motor, compilación Godot/ARM64, prueba CoreRPG ni test de partida.
- No se han definido nuevas ciudades, fronteras exactas, NPCs canónicos, poblaciones nuevas, cronologías o nombres nuevos.
- No se modifica Treihord original, Norgard Defaults, Nimroel Core ni Valrik.
- No se ha fusionado `main`.

## Deuda aceptada para fases posteriores
- D01 límites/relieve/mapa métrico; D02 drenaje; D03 clima; D04+ economía y población.
- DAR-P01 administración de Arven; DAR-P02 casa dirigente/herederos; DAR-P03 historia; DAR-P04 límites y magnitudes; DAR-P05 compatibilidad militar; DAR-P06 errata narrativa Eshneva (no afecta al canon Belara).
La deuda pertenece a fases posteriores, **no bloquea el cierre de D00**.

## Puerta de salida
1. Publicar el acta y el índice final en PR #14.
2. Verificar diff, número de archivos, JSON y apertura de enlaces principales.
3. Marcar PR lista para revisión; el autor decide el merge.
4. Abrir conversación Darovan 2 para D01 después de confirmar que D00 quedó integrada en `main`, o con dependencia encadenada autorizada.
