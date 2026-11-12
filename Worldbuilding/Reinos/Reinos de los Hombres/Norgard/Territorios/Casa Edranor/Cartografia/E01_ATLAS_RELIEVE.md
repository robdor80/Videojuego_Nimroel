# E01 — Atlas cualitativo del relieve Edranor

## Método y escala de confianza
Este atlas estudia el marco físico **de oeste a este y del centro hacia el norte**, no una cuadrícula. Un «sector» no es una provincia nueva, una delimitación definitiva, una parcela ni un bioma exclusivo. Los IDs del JSON son técnicos y no crean topónimos narrativos. El recorte aprobado en E00 solo da una línea roja y una X azul; no proporciona escala, coordenadas, elevaciones ni cierre septentrional.

| Unidad de planificación | Observación / canon disponible | Lectura permitida | Lo no establecido |
|---|---|---|---|
| `edr_e01_west_valkram_interface` | Montes Valkram delimitan oeste y centro de Norgard (CANON_REPO) | Interfaz orográfica occidental **a estudiar** | Qué laderas, picos, pasos o minas administra Edranor |
| `edr_e01_karsath_central_west` | Karsath figura más al oeste que Lumina y Dorth (OBSERVACION_MAPA) | Posible alternancia de planicies, lomas y mesetas en el oeste interior (PROPUESTA) | Cotas, pendientes y geología local |
| `edr_e01_lumina_bosque_alto` | Bosque Alto está en meseta elevada en torno a Lumina (CANON_REPO) | Altiplano forestal con variación de exposición, claros y laderas | Perímetro, propiedad de cada ladera y desniveles |
| `edr_e01_central_wine_context` | Edranor es principal región vinícola; el centro de Norgard presenta llanuras y mesetas (CANON_REPO) | Zona de evaluación agraria, **no** viñedo continuo (PROPUESTA) | Suelo apto, extensión, rendimiento o orientación de parcelas |
| `edr_e01_dorth_azurios_west` | Dorth linda con Bosque de los Azurios, en vertiente occidental de su cordillera (CANON_REPO) | Borde de bosque mixto y piedemonte, donde la cubierta cambia con la altura | Si Edranor posee cumbres o vertientes completas |
| `edr_e01_north_cold_transition` | Centro norte frío; bosques boreales; gradiente latitudinal (CANON_REPO del Reino) | Hipótesis de estudio de continuidad hacia el norte (PROPUESTA) | Ubicación local del límite entre formaciones |
| `edr_e01_far_north_unclosed` | En el recorte no se ve el cierre rojo superior (AUTOR/OBSERVACION_MAPA) | Condición abierta: alcance subpolar/polar **no demostrado** | Costa, tundra en propiedad Edranor, final territorial |

## Geometría y escala
No se asignan latitud, longitud, longitud de caminos, porcentajes de pendiente, metros, celdas Godot, áreas ni distancias entre localidades. El orden relativo del mapa no equivale a camino conectado. Las diferencias de altura aludidas por «meseta», «piedemonte» o «montaña» son **cualitativas**.

## Paisaje y relación con otras fases
- **Bosque Alto:** mosaico de frondosas (robles/hayas) y coníferas por altura/exposición; madera aprovechada para tonelería y bodegas de Lumina. La organización productiva concreta corresponde a E04.
- **Bosque de los Azurios:** bosque escalonado con claros y lomas abiertas, junto a Dorth; su sector meridional próximo a Hallheim se usa como Bosque Real de Aethros. No adscribirlo globalmente a Edranor.
- **Norte:** bosque boreal discontinuo, después vegetación más baja y tundra a escala de Norgard; no se infiere que todos los estados estén presentes dentro del perímetro Edranor.
- **Rodas:** enclave institucional en el contexto físico; no es accidente geológico ni autorización para desplazar la línea roja.
- **Vino:** la actividad confirmada no asegura suelos fértiles homogéneos en las siete unidades.

## Contactos de estudio (no aristas transitables)
Las cinco relaciones del JSON se marcan `HYPOTHESIS` y `physicalContactValidated=false`. Expresan preguntas para E02/E05; no equivalen a continuidad de valle, sendero, calzada, puente o paso de montaña.

## Restricción importante
El **Paso de Vareth** existe canónicamente entre Azurios y Velaris como conexión centro-oriente del Reino; ninguna fuente revisada lo coloca en Edranor. No crear un «Paso de Valkram» con nombre propio ni asignar Vareth a esta Casa.
