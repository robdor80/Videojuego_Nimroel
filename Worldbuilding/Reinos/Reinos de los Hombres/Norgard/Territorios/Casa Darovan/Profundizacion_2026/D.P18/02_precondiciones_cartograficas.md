# D.P18 — Inventario de precondiciones para futura cartografía y mapas urbanos

**No existe una escala/DEM georreferenciada derivada de este documento.** Tampoco se generan mallas, parcelas, puentes o accesos transitables.

## Anclas que deben verse antes de construir terreno

- Valkram: grandes cumbres ~3.600–4.200 m, la Viuda ~4.200 m, pasos naturales principales 1.400–2.200 m, piedemonte occidental 400–900 m, valles interiores 700–1.300 m.
- Elyra: cumbres hasta ~2.600 m; pasos principales 900–1.500 m y valles interiores 400–900 m.
- Treihord: núcleo principal 150–350 m; ocho barrios canónicos, Belara junto a la ciudad, industrial barcazas someras.
- Veldora: núcleo principal 0–60 m; litoral del Golfo, Lhera y Veldora independientes, aduana exterior real.
- Taramin: núcleo principal 0–40 m, Thalen un río de dos brazos terminales; colinas norte/centro 300–600 m, lomas boscosas meridionales 150–500 m fuera de Elyra.
- Syvaris: ciudad 0–40 m, máximo insular 200–400 m, bahía protegida, ecosistemas dispersos.
- Arven: máximo insular 250–500 m, bosque Manto Verde ~90 %, aldeas sobre todo costa interior, ninguna ubicación nueva.

**No interpretar** rangos como cotas de cada celda, cada casa o cada barranco.

## Dependencias secuenciales reales

1. Plano ilustrativo y límites de administración: confirmar escala y sistema de coordenadas antes de digitalizar.
2. Altimetría: superficies continuas y transiciones topológicas entre cordilleras, colinas, ciudades, costas e islas.
3. Hidrografía: divisorias y pendientes; respetar Belara/Lhera/Veldora/Fhalion/Thalen. **Fhalion boca exacta UNKNOWN**.
4. Asentamientos: georreferenciar solo las cuatro ciudades autorizadas y los sitios de asentamientos que se documenten/autorice.
5. Accesos: rutas y puentes deben seguir evidencia, no vínculos comerciales abstractos D05.
6. Infraestructura: validar cupos, accesibilidad, riesgos y derechos antes de dibujar instalaciones.
7. Mundo: identidad estable del contenido y migraciones para toda instancia persistente; WorldState actual solo cuando exista motor ejecutable.

## Puerta de no invención

Para cada geometría futura se exige: `canonicalAnchor`, `sourcePath`, `coordinateSystem`, `geometryEvidence`, `rights`, `validatedAgainstHydrology`, `authoredOrGeneratedProvenance`. Sin ellos no se promueve ninguna celda a canon físico de juego.

Los mapas urbanos detallados de Veldora/Taramin/Syvaris continúan pendientes de decisión autoral y cartografía; los de Treihord han de respetar el diseño base canónico, no sustituirlo.
