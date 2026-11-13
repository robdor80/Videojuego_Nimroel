# E13 — Autoridad, fuentes y auditoría de partida
**Fecha:** 13-11-2026. **Base Git:** main 660fcf13b45916cb5df062303f40ef5168558af0. **Naturaleza:** diseño delegado, no canon superior ni runtime.

## Principio editorial
Se aplica la cadena Nimroel Core → Norgard Defaults → Casa Edranor → localidad → World State. El sistema compartido gobierna la causalidad; la Casa aporta datos locales; una propuesta de diseño no constituye dato de juego instanciado. No se altera ninguno de los once archivos JSON E00–E10 que E11 protege mediante SHA.

## Inventario comprobado
1. Casa Edranor: E00–E12, 159 entradas del árbol territorial de main, siete unidades físicas E01, cuatro núcleos E07, ocho modelos sintéticos E06, once personajes y ocho conflictos/escenas propuestos E10, Content Pack E11 y auditoría E12.
2. Casa Darovan: D00–D12 y D.P13–D.P26, con atlas físico, 12 unidades de estudio, referencias de altimetría expresamente aprobadas, desarrollo de Treihord, Taramin, Syvaris, Veldora, campo, personajes y cierres editoriales. No se trasladan sus magnitudes, hidrología ni población a Edranor.
3. Casa Valrik / Treskal: sistema de 99 capas funcionales, microrelieve, cuencas, red menor, climatología local, cartografía técnica y reglas espaciales deterministas. Se reutiliza el método y la jerarquía de reglas, nunca sus atributos locales.
4. Nimroel Core: contratos compartidos y physicalGeographyDrainage; Norgard Defaults: reino, calendario, justicia, fiscalidad, límites de autoridad y toponimia.
5. Cartografía: E00 registra un recorte autoral rojo y una X azul para Rodas (archivo de origen 1000024893.jpg), con el norte cortado. El mapa general ilustrado del proyecto lleva una barra gráfica «400 millas», que NO ha sido calibrada como escala local de este recorte. Sin esa imagen de perímetro íntegro no existe geometría métrica autorizada.

## Fuentes primarias del repositorio
- Norgard/Geografía/montanas.md: Valkram, Azurios, Vareth e Invernos.
- Norgard/Geografía/rios_y_lagos.md: Lurien, Antela, Caleran y demás sistemas.
- Norgard/Geografía/bosques.md, regiones_naturales.md y Norgard/Clima.
- Norgard/Grandes Casas/grandes_casas.md y Norgard/NORGARD.md.
- Casa Edranor/Cartografia/E00_MAPA_Y_LIMITES.md, E01_ATLAS_RELIEVE.md, E01_LIMITES_Y_VERTIENTES.md, E02_ATLAS_HIDROGRAFICO.md y E02_CUENCAS_DIVISORIAS.md.
- Casa Edranor/Clima/E03_FRANJAS_Y_MICROCLIMAS.md; Suelos/E03_EDAFOLOGIA_Y_VITICULTURA.md; Ecosistemas/E03_ATLAS_ECOLOGICO.md; Riesgos/E03_ESTACIONALIDAD_Y_RIESGOS.md.
- Casa Edranor/Auditorias/E12_REGISTRO_INCIDENCIAS.md y E12_MATRIZ_TRANSVERSAL.md; datos E01–E03, E07 y E10.
- Casa Darovan/D.P13/00_comparacion_fuentes_y_metodo.md, 01–11 y 12–22; D.P14–D.P26.
- Casa Valrik/Geografia_local/reglas_espaciales_generacion_motor_v0.1.md y Treskal/99 capas.

## Autoridad por clase
| Clase | Qué permite | Qué no permite |
|---|---|---|
| CANON_REPO | Identidad, posición relativa y grandes procesos ya escritos | Precisión geográfica no sustentada |
| AUTOR_EXPRESO | Decisión propia del autor documentada en su fecha y ámbito | Extenderla a otra Casa |
| ASISTENTE_DELEGADO_DISENO | Elegir propuestas de altimetría, repertorios, método, nombres candidatos y orden de trabajo | Afirmar que el autor ratificó cada opción; modificar el canon superior |
| OBSERVACION_MAPA | Relaciones cualitativas entre lugares visibles | Pasar de píxeles a millas, cotas o jurisdicciones |
| DERIVACION_CONDICIONAL | Reglas causales universales y plausibilidad | Declarar un río, camino, riesgo o parcela existente |
| UNKNOWN | Reserva explícita vinculada a fase y puerta de cierre | Considerarla corregida por mera redacción |

**Protecciones:** Dorth, Lumina, Karsath son Edranor; Rodas es aldea de Corona Aethros, con justicia, impuestos, seguridad y mando berserker regios; Hallheim está fuera de Edranor. No aduanas interiores, no templos en Casa Druídica, no ejército soberano, no acuñación propia. Lurien–Antela son regionales sin adscripción local verificada.

## Matriz de incidencias E12 y destino
EDD-01 cierre norte: E19 con mapa autoral íntegro; EDD-02 escala/CRS: E19; EDD-03 drenaje local: E19/E28; EDD-04 población: E26; EDD-05 sucesión/NPC: E25; EDD-07 caminos: E16/E19/E28; EDD-08 historia Rodas: E27. EDD-06 ya RESUELTA como ALDEA real. Cada deuda tiene propuesta, evidencia requerida y prueba de cierre en 10_GOBIERNO_DEUDA.md.

## Regla de lectura de esta fase
Las bandas métricas de 02_ALTIMETRIA son **hipótesis de dirección artística y diseño territorial delegadas**, no medición física ni corrección de archivos E01 que mantienen UNKNOWN. Se podrán comparar y ajustar en E19. El mapa esquemático SVG de esta carpeta es una representación de relaciones, jamás un mapa de límites.
