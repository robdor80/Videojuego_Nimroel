# E19 — Ratificación autoral del marco territorial y reserva de Rodas
**Fecha:** 14/11/2026. **Fuente:** manifestación expresa del autor en conversación E19 y captura de pantalla del mapa «Nimroel (2).jpg» con trazos rojos (aportada en la conversación, no incorporada como raster fuente al repositorio). **Autoridad semántica:** AUTOR_2026_11_14. **Naturaleza:** aclaración geopolítica y orográfica; no es levantamiento métrico.

## Ratificaciones expresas
1. **Norte.** «Por el norte no hay límite, más que el propio norte». No existe frontera política intermedia que interrumpa Edranor hacia el norte. Se interpreta como alcance septentrional del territorio del Reino de Norgard; **no significa extensión ilimitada ni define por sí sola píxeles, vértices o costa**.
2. **Oeste.** La barrera compartida con Darovan es el macizo occidental (Valkram en el corpus). **Su vertiente oriental corresponde a Edranor**; la delimitación puntual por divisoria topográfica queda pendiente de DEM.
3. **Este.** Los montes Azurios son el límite del este; **su vertiente occidental corresponde a Edranor**. No atribuir por proximidad toda la cordillera o Bosque Real.
4. **Sur.** La separación con Aethros sigue **aproximadamente** el corredor fluvial que señala el trazo rojo. La precisión es visual; **no se identifica el curso concreto como Lurien** ni se vectoriza una polilínea sin calibración.
5. **Hallheim.** Fuera de Edranor, **capital de Norgard y sede de la Casa Aethros**.
6. **Rodas.** Aldea **dentro del territorio geográfico Edranor**. La **Casa Regente Aethros** conserva la prerrogativa militar de **convocar a los berserkers de Rodas**; Edranor no puede hacerlo por sí misma. La localización geográfica NO transfiere esa facultad.

## Desambiguación del control de Rodas
El autor precisa expresamente que, al decir «control», **se refiere a convocar a los berserkers**. Es una aclaración de la prerrogativa militar, **no una nueva ratificación específica de tasas, funcionarios, mando civil, propiedad parcelaria ni revisión del régimen fiscal**. E07/E09 ya documentaban administración/hacienda regia y otras competencias; se conservan como fuentes históricas **sin reescribirlas por deducción**. Si se decidiese revisar ese alcance civil o fiscal, requeriría un acto separado, con cotejo de canon. En los contratos E19, `owner=crown_aethros` de Rodas denota **autoridad administrativa heredada**, no la ubicación de su suelo.

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
