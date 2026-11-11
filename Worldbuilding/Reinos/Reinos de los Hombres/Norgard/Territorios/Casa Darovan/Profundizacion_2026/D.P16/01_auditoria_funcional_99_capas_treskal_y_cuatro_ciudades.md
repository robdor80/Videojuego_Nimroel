# D.P16 — Cuatro ciudades manuales frente al modelo funcional de Treskal

**Estado:** matriz de funciones y requisitos de autor, NO cierre de planos urbanos individuales ni geometría de producción.

## Evidencia de referencia: Casa Valrik

La ciudad de Treskal mantiene un inventario de **99 números funcionales 01–99**; la carpeta del repositorio presenta **100 subcarpetas numeradas del 01 al 99** porque el número 34 se usa en dos ámbitos distintos (fiscalidad/aduanas y salud/cuidados). La auditoría de Valrik declara su base funcional completa y su extracción de sistemas generales a Core/Norgard, **no** que las calles, residentes y servicios de Treskal puedan clonarse en Darovan.

Esta fase registra los nombres de las carpetas de Treskal como **índice de revisión** en JSON, sin copiarlos como módulos localmente implementados.

## Principio: capas globales frente a diferencias locales

- **No duplicar:** memoria, personalidad, relaciones, salud, casa, trabajo, cuidado, propiedad, mensajería, reputación y reglas legales si ya tienen autoridad Core/Norgard.
- **Diseñar en la ciudad propia:** relación con río/puerto/industria, tejido urbano acreditado, rutas internas, localización exacta de servicios/instalaciones, clases de acceso, capacidad real e historia local.
- **Solo autor:** nombres y número de nuevos barrios, hitos históricos, personalidades singulares, edificios excepcionales, edificios militares nuevos y cruces de río.
- **Solo cartografía:** coordenadas, superficie de distrito, trazado vial, escaleras, puentes, aforos exactos, inundabilidad o accesibilidad de cada parcela.

## Ciudades y autoridades

| Ciudad | Estado fuente D07 | Población D08 | Concepto aprobado |
|---|---|---|---|
| **Treihord** | `CANON_DISENO_BASE_CERRADO` | ~32000 (aprox.) | capital de Casa Darovan |
| **Veldora** | `VISUAL_APROBADO_TRAZADO_URBANO_PENDIENTE` | 29000–35000 (banda) | principal puerto mercante y comercio exterior con aduanas reales |
| **Taramin** | `VISUAL_APROBADO_TRAZADO_URBANO_PENDIENTE` | 14000–20000 (banda) | una zona principal de actividad pesquera (DAR-D07-02 opción A) |
| **Syvaris** | `VISUAL_APROBADO_TRAZADO_URBANO_PENDIENTE` | 7000–10000 (banda) | bahía principal concentradora de actividad (DAR-D07-03 opción A) |

## Doce puertas de madurez funcional

1. **topology:** Huella, costa y ríos concretos solo cuando existan geometrías verificadas.
2. **housing:** Residencia y hogares sujetos a derechos, ocupación y capacidad; población urbana no es número de viviendas.
3. **goods:** Entradas de mercancías sustentadas por cadena, permiso, stock y acceso; sin cargas conjuradas.
4. **services:** Proveedor real, localización, turno y aforo; necesidad no obliga a instalar institución.
5. **employment:** Oficios y contratos condicionados a empleador, vacante, aptitud, edad y normas de Norgard.
6. **law:** Justicia del Rey, jurisdicción Casa-Corona y custodia diferenciadas; sin ley local propia.
7. **fiscal:** No aduanas entre Grandes Casas; control exterior solo donde está respaldado.
8. **security:** Autoridad de Guardia urbana, Casa y Armada Real separada; no nuevo cuerpo militar.
9. **care:** Salud, cuidados y dependencia sin hospital o cuidador universal por plantilla.
10. **relationships:** Core hereda parentesco, reputación, conocimiento, memoria, diálogo y consentimientos.
11. **maintenance:** Agua, saneamiento, incendios, desgaste y combustible solo con infraestructura específica o estado UNKNOWN.
12. **worldstate:** Entidades, ubicaciones, accesos, actividades y cambios persisten solamente cuando CoreRPG los ejecuta.

Los sectores funcionales son funciones de estudio, **no** barrios, solares, edificios ya existentes ni nuevos servicios.

## Puntos de comparación

Treskal posee planificación sectorial T/S aprobada y plano métrico en progreso. Darovan todavía no tiene para Veldora, Taramin o Syvaris un plano urbano métrico, un inventario de barrios aprobados o localización exacta de instalaciones. **Este déficit es real y no se marca como completado por un JSON**.

El trabajo **intelectual de contratos, principios y compatibilidades urbanas queda preparado**; la materialización y aprobación de detalles únicos permanecen abiertas y necesitan autor/cartografía cuando corresponda.
