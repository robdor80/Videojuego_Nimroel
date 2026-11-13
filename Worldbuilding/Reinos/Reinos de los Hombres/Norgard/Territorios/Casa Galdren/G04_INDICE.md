# GALDREN G04 — Agricultura, ganadería y economía alimentaria

**13/11/2026 — v0.1 — DOCUMENTARY_PLANNING_ONLY.** Base: G03 fusionada mediante PR #68; main SHA 0cec00d7b05a28972a9e6969279446aa0a6d119a.

## Propósito
Diseñar la capa productiva y alimentaria de la Casa Galdren sin inventar superficies, producción, rutas, talleres, explotaciones, razas, calendarios de cosecha ni precios. La fase es **documental**, nunca un sistema activado.

## Expedientes
1. [Atlas productivo](Economia/G04_ATLAS_PRODUCTIVO.md): 12 unidades G01 enlazadas a G03, anclas de Arleon, Zanthir, Caleran y Bosque Quebrado, tres grados de evidencia.
2. [Cultivos, suelos y ciclos](Agricultura/G04_CULTIVOS_Y_CICLOS.md): catálogo canónico **de Norgard**, aptitud de parcela UNASSESSED y cuatro estaciones civiles ya canónicas.
3. [Ganadería y caballos](Ganaderia/G04_GANADERIA_Y_CABALLOS.md): animales y productos autorizados a escala de reino; referencia regional caballar confirmada sin reproducir el override Treskal.
4. [Cadenas alimentarias](Economia/G04_CADENAS_Y_CONSERVACION.md): seis propuestas de transformación y conservación, con stocks reales aún no demostrados.
5. [Servicios y flujos](Economia/G04_ABASTECIMIENTO_COMERCIO_FISCALIDAD.md): dependencias rurales, almacenes, molinos, mercados, Corona e inexistencia de aduana interior.
6. [Estacionalidad, riesgos](Riesgos/G04_ESTACIONALIDAD_Y_RIESGOS.md): calendario civil contrastado y diez riesgos/condicionantes con evidencia separada.
7. [Contrato G04](Datos%20operativos/galdren_g04_agriculture_livestock_food_v0.1.json), [fuentes y deuda](Auditorias/G04_FUENTES_Y_DEUDA.md), [acta](Auditorias/G04_ACTA.md) y [traspaso G05](00_Control_del_proyecto/TRASPASO_G05.md).
8. Tools/GaldrenG04/validate.py + .github/workflows/galdren-g04.yml: regresión G00–G04 en Ubuntu 24.04 y Windows 2022, integridad y mutaciones negativas.

## Jerarquía de autoridad
Nimroel Core → Norgard Defaults → Casa Galdren → Localidad → World State. Dentro de fuentes Norgard: calendario/FOOD/RURAL/Gobierno prevalecen frente a anotaciones pendientes de G03. **Calendario civil fijado:** 12 meses, 365 días, primavera marzo–mayo, verano junio–agosto, otoño septiembre–noviembre e invierno diciembre–febrero. **No equivale a cosecha local fijada**. G03 dejó sin fechar fenología y actividades rurales locales, no el calendario civil vigente.

## Salvaguardas
- El **granero de Norgard** es Galdren; Arleon sobre Caleran; Bosque Quebrado principal región caballar; Zanthir centro minero/metalúrgico.
- Trigo, cebada, avena y centeno son **cultivos y alimentos canónicos del reino**, no plantaciones atribuidas por defecto a cada unidad Galdren.
- Los ejemplos de explotación familiar, ganado y fases de trabajo con scope **Norgard/Treskal/village** no pasan a Galdren como regla obligatoria.
- Sin cereal o animal exótico inventado, patata canónica, agricultor concreto, hectáreas, rendimiento, receta exclusiva Galdren, rutas, barcos, puertos o derechos de agua.
- Treskal es Valrik; Dorth Edranor; Hallheim Corona; Forja Estelar mantiene jurisdicción/titularidad pendientes y mando bélico regio. Metal Estelar solo Azurios.
- G04 no desarrolla G05 (minería, metalurgia, Forja Estelar), G07 (generadores), G08 (ciudades), G11 (runtime).
