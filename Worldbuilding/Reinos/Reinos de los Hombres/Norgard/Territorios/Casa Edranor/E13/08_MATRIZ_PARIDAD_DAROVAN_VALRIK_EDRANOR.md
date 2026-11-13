# E13 — Matriz de equivalencia territorial y diagnóstico verificable
**Corte comparado:** main 660fcf13 (13-11-2026). La paridad significa **densidad de resolución adecuada a la identidad de cada territorio**, no copiar entidades.

| Capacidad | Darovan D.P13–D.P26 | Valrik/Treskal | Edranor E00–E12 antes de E13 | Aportación real E13 | Siguiente cierre |
|---|---|---|---|---|---|
| Marco físico | 12 unidades y atlas causal D.P13 | clima/relieve local y 8 contextos | 7 unidades E01 cualitativas | 7 perfiles ampliados + 6 interfaces + 6 expedientes hidro | E19 |
| Altimetría | bandas de Valkram, Elyra, ciudades, islas autorizadas | Montes Invernos con borradores propios | cero bandas locales | referencias de diseño **no canónicas** por unidad y núcleo | E19 y autorización si cambia canon |
| Agua | cuatro redes principales, microcuencas condicionales | redes Sareno/Theleno y diseño menor | Lurien/Antela solo regionales, cero cauces locales | topología/protocolos de receptor, ninguna cuenca inventada | E19/E28 |
| Clima | gradientes y causalidad por unidad D.P13 | diez capítulos de clima local | E03 siete perfiles sin cuantificar | microclimas, estaciones y escenarios físicos detallados | E14/E19 |
| Suelo/ecosistemas | matrices integradas y vegetación protegida | microrelieve, drenaje, suelos | siete UNASSESSED, 3 grandes referencias forestales | fichas por unidad, reglas de aptitud/uso | E14/E15/E19 |
| Producción material | cadenas específicas y vida económica D.P15 | pesca, madera, oficios y mercados | vino y tonelería E04 abstractos | dependencia suelo→agua→vid/madera; sin inventar stocks | E15 |
| Red de transportes | D.P15 y corredores de estudio | sistemas de acceso y viaje | 4 preguntas E05, cero carreteras | puertas hidrológicas y jurídico-físicas | E16/E19 |
| Población y hogares | planes de residencia y monografías personales D.P20–26 | modelos persistentes, niveles de población | E08 15 servicios/16 oficios sin instanciar, censo desconocido | auditoría y fase obligatoria, no cifras ficticias | E26 |
| Ciudades y campo | Treihord + Veldora/Taramin/Syvaris, aldeas D.P24 | Treskal densa y rural | Dorth/Lumina/Karsath/Rodas E07 con esbozos | programa físico urbano y atlas de entorno, no monografías | E20–E24 |
| Personas e historia | biografías, vínculos y conflicto D.P25 | red social de las 99 capas | 11 nombres propuestos, 8 escenas no ejecutadas | matriz de autoridad y puerta de promoción | E25/E27 |
| Contratos y tests | perfiles D.P13, 14–26 y validadores | contratos Core/Treskal y pruebas | E00–E12 + E11 C++ sintético | contrato E13, validador negativo, CI y traspaso | E28/E29 |
| Cartografía jugable | diseños/estudios, algunas sedes sin todo el mapa materializado | plano métrico canónico de Treskal | sin coordenadas ni cierre norte | esquema SVG cautelar y protocolo de capas | E19 / E28 |

## Escala cualitativa de madurez
**B0** vacío; **B1** referencia canónica; **B2** diseño físico/causal auditado; **B3** datos concretos y georreferencia validados; **B4** runtime integrado probado. Edranor antes de E13 tiene B1–B2 repartido y sin B3/B4. E13 amplía B2, pero **no salta a B3 por añadir cifras orientativas**. Algunas piezas de Treskal sí tienen geometría de mapa canónico; no se la puede atribuir a Edranor.

## Diferencias que deben conservarse
Darovan concentra metales, puertos, Treihord y paisajes costeros/insulares; Valrik tiene Treskal, navegación/forestal y su propia hidrografía; Edranor debe expresarse mediante viticultura, Bosque Alto, Dorth, Lumina, Karsath, mesetas, interfaces montanas y tensión de Rodas bajo Corona. Los sistemas universales se heredan; sus implementaciones no se clonan.

## Dictamen
E13 resuelve la falta de **atlas conceptual profundo** y **gobierno explícito de la paridad**. Siguen siendo deudas verdaderas: cerrar norte/escala, definir agua de detalle, ubicar rutas, obtener censos reales, desarrollar barrios/lugares, ratificar protagonistas y materializar geometría 2D. Ninguna fila B2 se presentará como trabajo jugable.
