# E19 — Sistema 2D, calibración y contratos Godot

## Diseño elegido (no coordenadas efectivas)
Definir en la **futura instancia autorizada** un CRS interno `EDRANOR_LOCAL_2D`, plano cartesiano local, con X positivo hacia el este del plano y Y positivo hacia abajo para alinearse con Godot 2D; origen convencional, documentado **solo una vez** tras decidir el recorte y los controles. Esta convención no corresponde a latitud/longitud WGS84, no afirma orientación real del arte original y **no activa una escala hoy**. En el contrato E19 `crs=null`, `transform=null`, `metersPerPixel=null`, `imageControlPoints=[]`, `worldAnchorCoordinates=null`.

## Aceptación de calibración
Capturar al menos tres controles no colineales identificables tanto en raster como en espacio de mundo con distancias de referencia autorizadas. Elegir transformación afín
`X = a0 + a1 * px + a2 * py; Y = b0 + b1 * px + b2 * py`.
Comprobar determinante de la submatriz 2×2 distinto de cero para invertir y reconstruir; comprobar RMS residual en controles y, preferiblemente, punto(s) de verificación independientes. Documentar tolerancia según resolución material esperada, incertidumbre de digitalización, precisión por escala y error máximo. **Tres puntos exactos permiten ajustar pero no ofrecen control independiente**, por lo que para validar error externo se recomienda un cuarto o más.

No deducir metros/píxel a partir del rótulo «400 MILLAS» sin demostrar que la barra y el recorte comparten proyección, escala, rotación, distorsión y transformaciones. En caso contrario: `CALIBRATION_REJECTED`.

## Cuando se supere EDD-02
- Versionar `sourceImageId`, `crsId`, `transformForward`, `transformInverse`, puntos de control con autoridad, residual RMS, tolerancias y fecha de aceptación.
- Representar entidades con `world_x/world_y` en unidades documentadas, no derivar estados de la textura ilustrada. Separar malla decorativa, colisiones/navegación, agua, jurisdicción y lógica Core.
- Usar tile coords `(tile_x,tile_y)` y offset local; guardar IDs estables, semillas y revisiones de algoritmos; no alterar geometría permanente por estación ni render LOD.
- El export GeoJSON requiere CRS confirmado y polígonos revisados. Si se usa CRS local, describirlo en metadatos **no** etiquetarlo EPSG:4326 por conveniencia.

## Tests de E19/E28
Tres controles no colineales; determinante; ida/vuelta; residuos y holdouts; coordenadas exactas en bordes de tiles; reproyección reversible; actualización idempotente; ausencia de efectos sobre `World State` al importar capas preliminares.