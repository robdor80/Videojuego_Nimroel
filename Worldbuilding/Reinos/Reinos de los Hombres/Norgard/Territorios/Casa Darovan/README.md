# Territorio de Casa Darovan — índice de desarrollo
**Estado:** **D00 CERRADA DOCUMENTALMENTE** (PR #14 pendiente de aprobación/fusión). D01 no iniciada. La documentación de trabajo **NO eleva a canon**.
**Sede administrativa:** Treihord. **Ámbito:** occidente de Norgard, incluida la isla de Syvaris.

## Fuentes de autoridad (no duplicarlas)
- [Treihord canónica](../../Ciudades/Casa%20Darovan/Treihord.md): **CANON — DISEÑO BASE CERRADO**. El diseño urbano permanece en su fichero original.
- [Grandes Casas](../../Grandes%20Casas/grandes_casas.md): pertenencia de Treihord, Veldora, Taramin y Syvaris a Darovan.
- [Geografía general de Norgard](../../Geografía/geografia_general.md), [ríos](../../Geografía/rios_y_lagos.md), [mares e islas](../../Geografía/mares_y_costas.md), [montañas](../../Geografía/montanas.md), [bosques](../../Geografía/bosques.md), [regiones naturales](../../Geografía/regiones_naturales.md) y [clima](../../Clima/clima_general.md).
- [Nimroel Core](../../../../../Sistemas/Nimroel%20Core/README.md) y [Norgard Defaults](../../../../../Sistemas/Norgard%20Defaults/README.md).
- [Referencia metodológica Valrik](../Casa%20Valrik/): reutilizar procedimiento, no trasladar parámetros locales.

## Jerarquía obligatoria
`Nimroel Core → Norgard Defaults → Casa Darovan → Localidad → World State`.
La Casa **no sustituye** contratos activos de rango superior. Un override requiere ámbito, justificación y compatibilidad comprobada.

## Archivos de Darovan 1
1. [Auditoría de canon y reutilización](Auditorias/2026-10-15_auditoria_canon_reutilizacion_v0.1.md).
2. [Inventario geográfico y cartográfico](Geografia_local/00_inventario_y_lectura_del_mapa_v0.1.md).
3. [Hoja de ruta](PLAN_DESARROLLO_DAROVAN_v0.1.md).
4. [Metodología de asentamientos](Asentamientos/METODOLOGIA_ASENTAMIENTOS_DAROVAN_v0.1.md).
5. [Manifiesto de referencias — NO runtime](Datos%20operativos/darovan_bootstrap_manifest_v0.1.json).

## Separación de contenidos
- **Ciudades canónicas:** Treihord, Veldora, Taramin y Syvaris: diseño deliberado/manual. La fuente aprobada de Treihord **no se mueve ni modifica**.
- **Asentamientos ordinarios:** aldeas, pueblos, villas, puestos e instalaciones: arquetipos/instancias con restricciones y semillas, sujeto a compatibilidad regional.
- **Subámbitos de diseño, sin atribuir nuevos límites administrativos:** litoral Veldora/Arven, cuenca Belara, Valkram/Elyra, península Taramin, isla Syvaris, norte frío.
- **Registro de incertidumbres:** toda interpretación cartográfica o pendiente de autor se marca. Ningún documento de esta etapa crea topónimos, NPC importantes, cifras de población o fronteras nuevos.

## Reanudación en Darovan 2+
Leer por orden este README, la auditoría, la hoja de ruta y el manifiesto; verificar el HEAD de la rama/PR contra `main`. Continuar tareas por fases, sin fusionar sin autorización.

## Organización establecida en D00 (15-10-2026)
- [`00_Control_del_proyecto/`](00_Control_del_proyecto/README.md): registro de fases, protocolo PR/commits, decisiones y traspaso D01.
- [`Auditorias/`](Auditorias/D00_CIERRE_Y_VALIDACION_2026-10-15.md): cierre D00, matriz de fuentes y auditoría original.
- [`Geografia_local/`](Geografia_local/README.md), [`Hidrografia/`](Hidrografia/README.md), [`Clima_local/`](Clima_local/README.md), [`Cartografia/`](Cartografia/README.md): medio físico y documentación del mapa.
- [`Recursos_y_produccion/`](Recursos_y_produccion/README.md), [`Rutas_y_comunicaciones/`](Rutas_y_comunicaciones/README.md), [`Economia_y_abastecimiento/`](Economia_y_abastecimiento/README.md): producción, transporte y economía.
- [`Asentamientos/`](Asentamientos/README.md): aldeas, pueblos, villas e instancias, no ciudades canónicas.
- [`Ciudades/`](Ciudades/README.md): Treihord, Veldora, Taramin y Syvaris, todas de diseño manual.
- [`Poblacion_y_hogares/`](Poblacion_y_hogares/README.md), [`Servicios_e_infraestructuras/`](Servicios_e_infraestructuras/README.md), [`Administracion_y_fiscalidad/`](Administracion_y_fiscalidad/README.md), [`Seguridad_y_defensa/`](Seguridad_y_defensa/README.md), [`Cultura_y_sociedad/`](Cultura_y_sociedad/README.md): capas sociales e institucionales.
- [`Contratos_y_runtime/`](Contratos_y_runtime/README.md), [`Datos operativos/`](Datos%20operativos/README.md), [`Validacion/`](Validacion/README.md): integración futura y verificación.

La presencia de una carpeta **no** significa que su fase haya empezado o finalizado. Ningún dato de D01–D12 se declara implementado con esta estructura.
