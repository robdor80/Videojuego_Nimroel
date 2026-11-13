# E19 — Fuentes, procedencia e integridad

## Fuente primaria comprobada
- `Worldbuilding/Nimroel.jpg`: mapa GENERAL del mundo, 4096 × 2048 px, 4 752 802 bytes.
- SHA-1 del **blob Git**: `c46e017a5c9a0ab66f8f072dd37d7236e05b5e2d`.
- SHA-256 de los bytes: `582405ee3e38a6606a89342f4b28262d3bf88c087b05c23655a886130ffab91b`.
- La subida autoral «Mapa de Nimroel (1).jpg» aportada en el proyecto es **idéntica bit a bit** a ese archivo del repositorio: tamaño y blob Git comprobados, no solo semejanza visual.
- Contiene toponimia ilustrada (Karsath, Lumina, Dorth, Hallheim) y leyenda de «400 MILLAS» para el mapa **general**. No presenta allí un perímetro administrativo Edranor ratificado. Sus píxeles no implican metros ni coordenadas de Godot.

## Referencia secundaria: recorte territorial E00
`Cartografia/E00_MAPA_Y_LIMITES.md` documenta un recorte autoral `1000024893.jpg`, con línea roja delimitadora y X azul de Rodas. La línea superior se corta en la imagen; no es evidencia de costa o frontera cerrada. No hemos obtenido **bytes verificables de ese recorte** ni el mapa íntegro de sus líneas. La existencia de una referencia escrita no equivale a tener la imagen reproducible. Debe archivarse original, licencia/autor, hashes y revisión antes de vectorizar.

## Fuentes semánticas cruzadas
- `E00_MAPA_Y_LIMITES.md`: interpretación autoral y lectura del recorte.
- `E01_ATLAS_RELIEVE.md`, `E02_ATLAS_HIDROGRAFICO.md`: unidades y agua regional, no geometría local.
- `E13/07_CARTOGRAFIA_2D_Y_FABRICA_DE_MUNDO.md`: capas y restricciones.
- `E18/04_DICTAMEN_Y_TRASPASO_E19.md`: puertas materiales auditadas.
- `Norgard/Geografía/rios_y_lagos.md`: Lurien y Antela con **situación regional**, sin asignación parcelaria Edranor.

## Protocolo de captura de original
Guardar los bytes sin editar en carpeta de fuentes de autor con identificador y sha256; extraer tamaño, orientación, recorte, transformaciones conocidas, metadatos de generación si existen; registrar visualmente los dos extremos del perímetro septentrional y todas las excepciones. Cualquier versión ampliada debe vincularse mediante hash al archivo base. Nunca confundir píxel de la ilustración con vértice administrativo.

## Dictamen de adquisición
`world_image_verified=true`; `author_crop_bytes_verified=false`; `boundary_closed=false`; `metric_calibration_accepted=false`. EDD-01/02 abiertas.