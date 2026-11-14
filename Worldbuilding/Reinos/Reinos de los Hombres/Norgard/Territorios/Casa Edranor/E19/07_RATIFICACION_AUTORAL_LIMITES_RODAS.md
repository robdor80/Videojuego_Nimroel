# E19 — Ratificación autoral del marco territorial y reserva de Rodas
**Fecha:** 14/11/2026. **Fuente:** manifestación expresa del autor en conversación E19 y captura de pantalla del mapa «Nimroel (2).jpg» con trazos rojos (aportada en la conversación, no incorporada como raster fuente al repositorio). **Autoridad semántica:** AUTOR_2026_11_14. **Naturaleza:** aclaración geopolítica y orográfica; no es levantamiento métrico.

## Ratificaciones expresas
1. **Norte.** «Por el norte no hay límite, más que el propio norte». No existe frontera política intermedia que interrumpa Edranor hacia el norte. Se interpreta como alcance septentrional del territorio del Reino de Norgard; **no significa extensión ilimitada ni define por sí sola píxeles, vértices o costa**.
2. **Oeste.** La barrera compartida con Darovan es el macizo occidental (Valkram en el corpus). **Su vertiente oriental corresponde a Edranor**; la delimitación puntual por divisoria topográfica queda pendiente de DEM.
3. **Este.** Los montes Azurios son el límite del este; **su vertiente occidental corresponde a Edranor**. No atribuir por proximidad toda la cordillera o Bosque Real.
4. **Sur.** La separación con Aethros sigue **aproximadamente** el corredor fluvial que señala el trazo rojo. La precisión es visual; **no se identifica el curso concreto como Lurien** ni se vectoriza una polilínea sin calibración.
5. **Hallheim.** Fuera de Edranor, **capital de Norgard y sede de la Casa Aethros**.
6. **Rodas.** Aldea **dentro del territorio geográfico Edranor** y **bajo control íntegro de la Corona**, ejercido por Casa Regente Aethros: administración, justicia, fiscalidad, seguridad y mando militar. En especial, **solo Aethros puede convocar a los berserkers de Rodas**. La localización geográfica NO transfiere competencias a Edranor.

## Ratificación adicional: control íntegro de Rodas
El autor aclara de forma **expresa y definitiva** que «TODO está bajo el control de la Corona» en Rodas. Se mantienen sin cambios las competencias regias de E07/E09: **administración civil, justicia, fiscalidad, seguridad, gobierno y mando militar**, junto con la prerrogativa singular de **convocar a los berserkers**, reservada a la Casa Regente Aethros. La Casa Edranor no recauda impuestos ni administra Rodas y no puede convocar a los berserkers, aunque la aldea se encuentre dentro del ámbito geográfico de Edranor.

El autor describe Rodas como **aldea pequeña, de escasa relevancia fiscal**, cuya importancia es distinta: estratégica y vinculada a los berserkers. Esto no aporta cifras de habitantes, riqueza, ingresos o tributos: todos ellos siguen UNKNOWN.

**No existe contradicción entre localización territorial y gobierno:** `insideEdranor=true` es geografía; `owner=crown_aethros` representa competencia administrativa y política, no propiedad parcelaria inventada. No dibujar un agujero administrativo ni una frontera específica para Rodas sin material cartográfico, aunque las competencias regias estén ratificadas.

## Deuda geométrica y EDD
- **EDD-01:** aclarado el **criterio semántico** de norte y las dos vertientes. **No está cerrada la línea administrativa vectorial**: faltan posición de divisoria norte y contorno de frontera meridional exactos, así como fuente raster autoral reproducible. El norte no debe cerrarse arbitrariamente en el borde de una captura.
- **EDD-02:** sin escala o puntos de control metricamente ratificados. La imagen general tiene barra de 400 millas, pero no se prueba una transformación para la captura marcada.
- **EDD-03:** la alusión al río del sur NO autoriza hidrología local; falta DEM y validación fluvial.
- **EDD-07:** siguen sin existir trazas de vías, puentes, pendientes, derechos de paso validados.
- **U7:** el extremo septentrional ya tiene alcance **conceptual autoral**, pero **sigue NON_EVALUABLE para ocupación o capas métricas**.

## Consecuencia para fases posteriores
La dirección territorial y competencias pueden emplearse como **canon semántico ratificado** en monografías. El mapa utilizable por Godot 2D, tiles, polígonos jurisdiccionales y caminos no se publicará sin superar EDD-01/02/03/07. Esta acta evita declarar «E19 terminada» por el mero acuerdo verbal sobre el norte.

## Identificadores de decisión
- `ED19-AUT-01`: norte sin frontera interna arbitraria; límite norte geográfico del Reino, contorno exacto pendiente.
- `ED19-AUT-02`: vertiente oriental occidental/Valkram y vertiente occidental oriental/Azurios de Edranor.
- `ED19-AUT-03`: frontera Aethros al sur próxima a corredor fluvial dibujado, geometría pendiente.
- `ED19-AUT-04`: Hallheim capital real, sede Aethros, fuera.
- `ED19-AUT-05`: Rodas en Edranor territorialmente, convocatorias berserkers reservadas a Casa Regente Aethros.
- `ED19-AUT-06`: Rodas bajo control **íntegro** de la Corona (administración civil, justicia, fiscalidad, seguridad y mando militar); sin competencias Edranor; relevancia fiscal baja únicamente cualitativa, sin cifras.
