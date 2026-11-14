# E19-R0 — Reconstrucción con puertas de prueba, no por dibujo
El procedimiento toma de Treskal la secuencia de autoridad → huella → geografía → funciones → rutas → parcelario → consistencia → export, pero no transplanta coordenadas.

## R1 Perímetro
**CORRECCIÓN AUTORAL PREVALENTE:** las líneas rojas son orientativas; NO se digitalizan como fronteras. Oeste contra Darovan: Montes Valkram. Este contra Galdren: Montes Azurios. Sur contra Aethros: demarcación administrativa salvo un tramo del gran río Lurien que desemboca en el Golfo. El norte NO se une. El trazado material deberá apoyarse en divisorias, valles, curso fluvial y demarcación cuando corresponda. Ver 06_CANON_FRONTERAS_NATURALES.md.

## R2 Escala
Crear CRS local con origen/orientación/unidades; obtener **tres o más puntos no colineales** y referencias de distancia compatibles, transformación reversible y residuo/error publicado. La barra «400 millas» del mapa global no calibra por sí sola el recorte. NO cerrar EDD-02 antes.

## R3 Relieve e hidrología
Probar unidades, cotas, divisorias, flujo y receptor; comprobar Lurien/Antela solo donde esté autorizado. Sin asignar ríos a Dorth, agua de riego a Karsath ni propiedad forestal por polígono coloreado. EDD-03 sigue abierta.

## R4 Caminos físicos
Separar Gp (traza y nodos medidos), Gd (demanda) y Gq (preguntas). Cada arista Gp necesita origen, destino, geometría, pendiente/obstáculos, paso/puente, derechos y fuente. Las cuatro preguntas de E01/E05 NO son cuatro carreteras. EDD-07 sigue abierta.

## R5 Datos espaciales
Un solo conjunto autoritativo de objetos con IDs permanentes, CRS explícito, GeoJSON y SVG técnico/operativo/lore concordantes, control de integridad, pruebas de reimportación y separación World State/arte/colisión/navegación.

## R6 Auditoría
Pruebas de validez/no autocruce de dos líneas abiertas sin unión norte, separación de recorte técnico y frontera legal, consistencia jurídica donde haya datos, calibración/error, cuencas, rutas, propiedades, IDs y rechazo de fuentes descartadas. Evidencia de geometría B3 y runtime B4 se auditan aparte.

### Decisión actual
R1–R6 no superadas: recorte íntegro/definición norte, calibración, altimetría, drenaje, vías y planos siguen pendientes. Solo R0 (inventario y clasificación de evidencia) se ha trabajado. Las fuentes descartadas en PR #84 se excluyen en cualquier circunstancia.


**Precedencia:** ver 05_CORRECCION_AUTORAL_NO_UNION_NORTE.md. Cualquier referencia histórica a «cerrar el norte» queda sustituida por la instrucción expresa «NO se unen».


**Regla de prevalencia:** cualquier referencia previa a calcar trazos rojos es errónea. La precisión deriva de la geografía del territorio, no del color. Ver 06_CANON_FRONTERAS_NATURALES.md.
