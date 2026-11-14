# EDRANOR E19 — Cartografía territorial de implementación
**Corte:** main `223f1e49adfbc73be6a80c6ce36e7aab506450c2`, 14/11/2026. **Resultado de este corte:** PREFLIGHT verificable, NO geometría métrica, NO runtime. **Estado general de E19: ABIERTA, bloqueada por fuente material.**

## Objeto y progreso real
La fase E19 debe entregar perímetro cerrado, escala, coordenadas Godot 2D, relieve/DEM, cuencas, hitos, capas y topología. Este corte **sí** entrega una fuente general binariamente verificada, inventario de fuentes y excepciones, protocolo de calibración/validación, modelo de capas, contrato JSON consumible, una lámina esquemática y pruebas adversariales en CI. **No** entrega mapa de propiedad, georreferencia, vías ni hidrografía local real.

1. [Fuentes reproducibles y discrepancia de mapas](01_FUENTES_PROCEDENCIA.md).
2. [Perímetro y jurisdicciones](02_PERIMETRO_Y_EXCEPCIONES.md).
3. [CRS interno y calibración](03_CRS_CALIBRACION_Y_GODOT.md).
4. [Relieve, cuencas y topología](04_RELIEVE_AGUA_Y_VIAS.md).
5. [Capas, contratos y exportación](05_CAPAS_Y_EXPORTACION.md).
6. [Pruebas, decisiones y puerta de salida](06_ACTA_Y_TRASPASO.md).
7. [Ratificación autoral de norte, vertientes, Hallheim y facultad berserker de Rodas](07_RATIFICACION_AUTORAL_LIMITES_RODAS.md).
7. [Atlas de relaciones, NO MÉTRICO](atlas_lectura_no_metrica.svg).

**Contrato:** `Datos operativos/edranor_e19_cartography_gate_v0.1.json`. **Validador:** `Tools/EdranorE19/validate.py`. **CI:** `.github/workflows/edranor-e19.yml`.

## Lectura jurídica vinculante
Dorth, Lumina y Karsath pertenecen a Casa Edranor; Rodas **ALDEA** dentro del contexto territorial pero regida directamente por la Corona Aethros; Hallheim fuera. U7 no evaluable, Bosque Alto sin tala libre, Azurios/Bosque Real no adjudicados por proximidad. Los ámbitos físicos no son dominios jurídicos. La barra «400 MILLAS» del mapa general no se traslada al recorte autoral sin calibración.

## Por qué E19 no puede certificarse aún
E00 cita un recorte `1000024893.jpg` con línea roja y X azul, cuyo **original íntegro no está disponible en las fuentes examinadas**, y además la línea queda cortada arriba. El autor ha ratificado el alcance territorial cualitativo (norte, vertientes y frontera sur aproximada), pero sigue faltando un perímetro digital cerrado trazable o un acta de vértices métricos (EDD-01), además de controles de calibración suficientes (EDD-02). Después se podrá validar drenaje/DEM (EDD-03) y trazas legales/reales (EDD-07). Sin estas pruebas: B2 documental, no B3/B4, ninguna importación a Godot 2D ni creación de edificios/parcelas o caminos.

**Política de fusión:** conservar PR Draft mientras las puertas materiales EDD-01/02 sigan abiertas para el objetivo íntegro E19. Las pruebas verdes **solo certifican el bloqueo seguro y la calidad del contrato**, no el mapa terminando.
## Material autoral y calco disponible (14/11/2026)
El autor ha aportado el mapa íntegro con contorno rojo `nimroel_Edranor.jpg`; el calco de la frontera oeste/sur/este se ha convertido a **21 coordenadas en imagen 2048×1024**, con cinco rayas interiores registradas separadamente. No se necesita una tercera imagen para definir esta lectura visual. Se publican [calco y método](08_CALCO_VECTORIAL_AUTOR.md), [SVG transparente](author_trace_overlay_2048.svg) y [coordenadas JSON](author_trace_raster_2048_v0.1.json).

El borde superior de la ilustración **no es el borde norte político** y no se rellena el mar. La relación de píxeles con `Worldbuilding/Nimroel.jpg` es reversible (`×2`) y válida para anclar la visualización 2D. Siguen **ABIERTAS las puertas de geometría territorial física, escala métrica, DEM y carreteras**: la PR no declara territorio jugable íntegro.
