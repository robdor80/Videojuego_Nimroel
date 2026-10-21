# D06 — Pesos regionales y reglas de elegibilidad v0.1

**PROPUESTA TÉCNICA NO CANÓNICA.** Los pesos relativos 0–4 son *prioridades de ensayo*, no porcentajes, densidades, probabilidades históricas ni estimaciones de número de localidades. **0** significa que D06 no propone ese modelo en la unidad de estudio; un valor positivo es una **posibilidad sujeta a todas las pruebas locales**. No activa geografía ni población.

## 1. Procedimiento — exactamente seis puertas

1. **Esqueleto obligatorio:** suelo, agua, acceso, sustento, competencia local; toda prueba local exigible.
2. **Posibilidades:** edificio/oficio/servicio potencial, sin materialización automática.
3. **Condiciones:** restricciones de costa, montaña, bosque, clima, transporte, suministro, derechos y compatibilidad con Core/Norgard.
4. **Pesos regionales:** se consultan solo **tras** filtrar la elegibilidad. Ponderaciones de diseño, nunca mapa real.
5. **Modelos:** seleccionar entre opciones admisibles con desempate determinista. Los servicios se estudiarían por demanda y cobertura, no por trocear tiradas aleatorias globales.
6. **Instancias y semillas:** laboratorio exclusivamente `TEST_ONLY`; identidad estable y campos nulos de posición/población. Integración persistente pendiente D11.

Orden contrario, por ejemplo `peso alto ⇒ aldea`, es inválido.

## 2. Prioridades por las 12 unidades cualitativas

El catálogo JSON es la fuente de verdad para las nueve columnas `agricola, ganadera, pesquera, minera_auxiliar, metalurgica_auxiliar, forestal_sostenible, servicio_camino, insular_mixta, enclave_especializado`.

| Unidad D01 | Mayor énfasis de diseño | Precaución primaria |
|---|---|---|
| Valkram oeste | minería auxiliar condicionada | mina real **concreta**, acceso, titularidad; no colocar bocaminas |
| Elyra | ganadería/enclaves hipotéticos | titularidad territorial y minería Darovan sin demostrar; minero desactivado |
| norte frío | ganadería y posible agricultura restringida | no fijar cosechas, permanencia ni estaciones |
| Agujas litoral | ninguno en D06 | bloqueo conservador sin mapa para separar bosque interior de costa |
| Belara/Treihord | cultivo de abastecimiento y posibles apoyos | no recrear el Crisol ni la ciudad; navegación somera |
| Veldora litoral | pesca y agricultura local condicionadas | ciudad comercial manual; no crear muelles ni caladeros |
| Linde/camino | servicios de camino | solo corredor general acreditado, sitio de parada UNKNOWN |
| Pilares sur | actividad forestal compatible, cultivos condicionados | un único bosque y explotación regenerativa demostrada |
| Taramin norte/centro | pesca litoral posible, ganadería | semiárido ≠ desierto ni agua utilizable |
| Taramin bosque sur | litoral pesquero y uso forestal tradicional | un solo bosque, sin explotación industrial |
| Syvaris | pesca, insularidad, diversificación menor | isla parcialmente seca, bosquetes dispersos |
| Arven | comunidad insular y pesca costera condicional | Manto Verde continuo, madera no intensiva, sin rutas nuevas |

Un peso local mayor no afirma que el asentamiento esté presente: solo expresa cuál **se ensayaría primero** si existieran pruebas verificadas de su emplazamiento. No hay densidad o número de tiradas autorizado, porque no disponemos de superficie georreferenciada, capacidad de carga ni conectividad puntual.

## 3. Separación entre región, emplazamiento y red

`d01_*` = área de estudio **no** cartografía; `slotId` = identificador sintético en pruebas, nunca coordenadas o nueva aldea. Para ejecución real futura: un servicio de cartografía aporta celdas geográficas válidas, derechos y fuentes; un servicio de accesibilidad acredita accesos locales comprobados; CoreRPG decide bienes, residentes, trabajo y cambios dinámicos. Si un dato es UNKNOWN, el generador no sustituye esa ausencia con azar.

Las cuatro localidades canónicas son anclas externas manuales. Un puerto canónico es instalación dentro de ciudad; D06 no puede clonar la instalación para generar un pueblo. Una relación de abastecimiento D04/D05 no se convierte en carretera transitable o itinerario de barcazas. **D05 cuenta 17 nodos, tres enlaces modales acreditados y cuatro relaciones de suministro no ejecutables.**

## 4. Restricciones por clase

Aldea, pueblo y villa son escalas funcionales, todavía sin mínimos de habitantes ni edificios. Enclaves pueden ser instalaciones sin población permanente; ese caso **no entra** en la lista de asentamientos. La futura promoción exige evidencia de **comunidad residente** y validación D08. No se generan niños, NPC, contratos laborales, propiedad o inventario en D06.

**Sin hipótesis numérica de densidad** no se efectúa muestreo de cantidad ni colocación espacial. Los pesos 0–4 solo intervienen en selección *entre modelos viables de un único escenario sintético*.

## 5. Condiciones para publicar reglas futuras

Una iteración posterior con geografía, derechos, población aprobada y contratos runtime deberá definir: celdas reales, cobertura de agua, red de accesos verificada, límites de explotación, jerarquía funcional, oferta/demanda, competencia de autoridades, cuota de generación territorial, migración de versión y pruebas de persistencia cross-arch. Ninguno queda resuelto por este documento.
