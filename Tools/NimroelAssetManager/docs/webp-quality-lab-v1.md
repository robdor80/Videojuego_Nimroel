# WebP Quality Lab v1

## Objetivo y límite

WebP Quality Lab v1 compara conversiones reales de un `staged source` privado después de `ready_to_commit`. Sirve para tomar más adelante una decisión humana sobre **Canonical Image Profile v1**.

**LAB RESULT != CANONICAL ASSET.** Los candidatos no son Assets, `LocalRepresentation`, binarios canonical ni documentos persistentes. El laboratorio no modifica `Asset.Content`, no calcula un SHA canónico, no llama a `commitIngestedAsset`, no usa ImageKit y no escribe en Room.

La “imagen canónica” de la guía artística es una referencia visual del mundo. Un “canonical binary” sería el archivo técnico definitivo de un Asset. Este hito sólo produce candidatos temporales y mantiene separados ambos conceptos.

## Pipeline y orden de orientación

1. Resuelve exclusivamente `filesDir/nimroel-assets/staging/<workId>/source` dentro de la raíz privada.
2. Rechaza fuentes que no sean JPEG, PNG o WebP estático; un WebP con flag de animación se rechaza.
3. Lee bounds reales y comprueba que coincidan con el `Content` verificado.
4. Lee EXIF mediante `androidx.exifinterface.media.ExifInterface`.
5. Determina las dimensiones visuales: transpose, 90°, transverse y 270° intercambian los ejes.
6. Calcula `inSampleSize`, decodifica un bitmap ARGB_8888 muestreado y aplica físicamente la orientación EXIF.
7. Escala a las dimensiones finales sin upscale y comprime un único candidato.
8. Escribe un temporal UUID exclusivo de la ejecución, hace `flush` + `fsync` y lo cierra.
9. Valida el temporal: existencia, bytes positivos, MIME WebP, dimensiones esperadas y transparencia cuando fue observada.
10. Comprueba cancelación y sólo entonces promueve el temporal al target final.
11. Actualiza la referencia opaca y devuelve el resultado después de completar la promoción.

El staged source nunca se abre mediante el `content://` original, nunca se sobrescribe y nunca se elimina por el laboratorio.

## Sustitución, temporales y cancelación

Cada ejecución usa un nombre como `.long1536-q85.webp.<uuid>.part`. Los bloques `catch/finally` sólo eliminan ese temporal; nunca eliminan el target final.

Si ya existe un candidato para el perfil, permanece intacto durante decode, orientación, resize, compresión y verificación. Una cancelación, OOM, error de codec o fallo de verificación anterior a la promoción conserva el candidato y su referencia previa.

La promoción intenta `ATOMIC_MOVE + REPLACE_EXISTING`. Si el filesystem no ofrece sustitución atómica, el fallback conserva una copia rollback del target anterior y la restaura si falla el reemplazo. Tras una promoción correcta no se introduce otro punto suspendible antes de publicar la nueva referencia.

## Concurrencia y lifecycle

`generate(workId)` y `clear(workId)` comparten un `Mutex` por `workId`. Una limpieza espera a que el procesador abandone la sección crítica y no puede borrar archivos mientras una generación del mismo trabajo los manipula. Trabajos distintos usan mutex distintos.

El `ViewModel` mantiene además un contador de generación y el `workId` actual. Un resultado tardío de A no puede aparecer en B y una operación limpiada no puede volver a publicar su resultado. El doble toque durante `Processing` se ignora.

El trabajo pesado se ejecuta en `Dispatchers.IO`. La sesión y sus metadatos sólo viven en memoria y no se restauran desde Room.

## Presets, WebP y compatibilidad

- Lado largo: 2048, 1536, 1280 y 1024 px.
- Calidad: 90, 85 y 80; nunca 100.
- API 30 o superior: `Bitmap.CompressFormat.WEBP_LOSSY`.
- API 26–29: `Bitmap.CompressFormat.WEBP` con las calidades lossy indicadas.

Se añadió únicamente `androidx.exifinterface:exifinterface:1.4.2`. Esta versión estable de AndroidX es compatible con `minSdk 26` y permite leer/escribir EXIF en JPEG, PNG y WebP sin depender de las diferencias históricas del `android.media.ExifInterface` de cada API.

El encoder sigue siendo el codec WebP de la plataforma. Las pruebas host no demuestran equivalencia con el encoder de Samsung y no se promete identidad byte-for-byte entre APIs, fabricantes o revisiones del codec.

## EXIF

Se contemplan las ocho orientaciones:

1. normal;
2. flip horizontal;
3. rotate 180;
4. flip vertical;
5. transpose;
6. rotate 90;
7. transverse;
8. rotate 270.

La transformación se aplica al raster antes del escalado. El candidato WebP no copia ni necesita la orientación EXIF original.

- Metadata ausente o `ORIENTATION_UNDEFINED`: orientación normal, estado `ABSENT`.
- Orientación 1 válida: orientación normal, estado `NORMAL`.
- Orientaciones 2–8: transformación física, estado `TRANSFORMED`.
- Metadata presente inválida o ilegible: orientación normal controlada, estado `UNREADABLE` visible en UI.
- Un raster corrupto se rechaza al validar bounds; no se disfraza como una imagen normal sin EXIF.

## Resize y redondeo

Se conserva el aspect ratio y nunca se amplía una imagen. Si el lado largo visual ya es menor o igual que el target, se conservan ambas dimensiones.

`scale = targetLongEdge / max(visualWidth, visualHeight)`

Cada eje se redondea al entero más cercano; `.5` positivo sube mediante `roundToInt`. Ninguna dimensión puede quedar en cero. Por ejemplo, 3456 × 4608 a 1536 produce 1152 × 1536. Una fuente 3000 × 4000 con EXIF 6 se trata visualmente como 4000 × 3000 antes de calcular el resize.

## Alpha

- `sourceHasAlphaCapability`: capacidad alpha del bitmap muestreado.
- `transparentPixelsObserved`: se encontró al menos un píxel con alpha menor que 255 en ese raster.

Las matrices y el escalado no añaden fondo opaco. Si se observa transparencia, el WebP temporal se decodifica y se descarta si no conserva ningún píxel transparente.

El muestreo puede omitir transparencia extremadamente localizada. Esta comprobación es una salvaguarda experimental, no una política canonical.

## Preview interna y memoria

No existe `FileProvider`, `ContentProvider`, URI de preview ni exposición de `cacheDir`, `filesDir` o staging. La UI conserva un `ImageLabArtifactRef` opaco y llama a una frontera Android interna `ImageLabPreviewLoader`; Compose no conoce `File` ni paths.

La preview tiene estados explícitos `Idle`, `Loading`, `Ready`, `Unavailable` y `Error`:

- archivo disponible y decodificable → `Ready`;
- archivo eliminado por Android → `Unavailable`;
- I/O, seguridad, formato inválido, decode nulo u OOM → `Error` estable.

La decodificación aplica `inSampleSize` y después un downscale exacto si todavía supera `maxLongEdge`. Nunca hace upscale. Los bitmaps intermedios se reciclan y ningún bitmap se guarda en `ImageLabResult` ni en el `ViewModel`.

El pico real de memoria depende del decoder, codec y dispositivo. Sigue pendiente medir heap Java, memoria nativa, latencia y comportamiento OOM en la Galaxy Tab S9+.

## Almacenamiento y cleanup

Los candidatos viven únicamente en:

`cacheDir/nimroel-image-lab/<workId>/long<target>-q<quality>.webp`

`clear(workId)` elimina el directorio experimental de ese trabajo y sus referencias opacas. No elimina staging, la raíz `filesDir`, la raíz `cacheDir`, otros trabajos, Assets ni representaciones. Un trabajo ya desaparecido se considera limpiado sin error.

## Descartar una ingestión preparada

Mientras un work está en `ready_to_commit`, la UI ofrece **Descartar ingestión** con confirmación. Al confirmarlo se invalida cualquier generación del Lab, se serializa `clear(workId)`, se elimina la fila operacional `ingest_work_items` únicamente si sigue en `ready_to_commit` y se borra sólo `filesDir/nimroel-assets/staging/<workId>/...`. La ausencia previa de un temporal no es un error y se rechazan workId que no sean seguros.

El `AssetId` reservado se abandona: la siguiente preparación genera un identificador nuevo. No se crea Asset, documento canónico, representación ni se llama a `commitIngestedAsset`. La imagen seleccionada, `PreparedImage`, provenance y la sesión del Lab se limpian; el `ProductionDraft` editorial se conserva.

## Métricas y unidades

Los bytes salen del fichero verificado. La UI presenta una variación neutral respecto al original:

- resultado menor: `Variación -XXX KiB` y `-YY.Y %`;
- resultado mayor: `Variación +XXX KiB` y `+YY.Y %`;
- sin cambio: cero sin signo.

`KiB` usa 1024 bytes y `MiB` usa 1024² bytes. Internamente `sourceBytes - resultBytes` permanece como reducción firmada; la presentación invierte el signo para expresar `resultado - original`.

## Evidencia automatizada

### VALIDADO POR TEST JVM

- presets permitidos;
- métricas con reducción y aumento;
- resize landscape, portrait, square, 1×1, igualdad con target, no upscale, dimensiones extremas, mínimo de un píxel y redondeo;
- 3456 × 4608 → 1152 × 1536.

### VALIDADO POR ROBOLECTRIC

- escritura WebP real del entorno host y staging inmutable;
- selección `WEBP` en API 26 y `WEBP_LOSSY` en API 30;
- lectura AndroidX EXIF de JPEG y, en el entorno probado, PNG/WebP;
- las ocho transformaciones mediante patrón asimétrico y píxeles esperados;
- EXIF ausente, inválido y raster corrupto;
- transparencia observada y comprobada;
- temporal exclusivo, regeneración fallida/OOM/cancelada preservando el target anterior;
- reemplazo exitoso sólo después de verificación;
- cleanup real, aislamiento entre works, rechazo de traversal y serialización generate/clear;
- preview con límite real y fichero desaparecido;
- protección del `ViewModel` ante resultados tardíos.

Robolectric y sus gráficos nativos siguen siendo pruebas host: no validan el codec, EXIF, filesystem, memoria ni rendimiento reales de Samsung.

### PENDIENTE DE DISPOSITIVO FÍSICO

- codec WebP y tamaños producidos por la Galaxy Tab S9+;
- lectura EXIF de ficheros reales de cámara en JPEG/PNG/WebP;
- las ocho orientaciones con fixtures visuales;
- alpha, halos y bordes sobre pantalla real;
- presión de memoria, latencia, caché eliminada por Android y cancelación/cleanup interactivos;
- inspección humana de retrato, paisaje, ciudad, texturas, texto y degradados.

## Límites de v1

- No hay comparación A/B directa, zoom sofisticado ni editor.
- No hay benchmark integrado ni métrica perceptual automática.
- WebP animado no está soportado.
- No existe elección automática de ganador.
- No existe política final para alpha o reproducibilidad canonical.
- No se crea `canonical.webp`, Asset, SHA canonical ni `LocalRepresentation`.

## Próximo hito

Realizar sesiones físicas y decidir humanamente **Canonical Image Profile v1**. Sólo después corresponde diseñar **Canonical Image Processing v1**.
