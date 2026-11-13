# E15 — Alcance, autoridad y cadena de evidencia
**Fecha:** 13/11/2026 · **Estado:** diseño delegado, documental y NO RUNTIME.

## Por qué existe E15
E04 estableció la identidad del vino y de la madera; E07 dibujó las personalidades funcionales de Dorth, Lumina y Karsath; E08 vinculó hogares y oficios; E09 fijó competencias; E13 describió el medio y E14 prohibió convertir un terreno plausible en explotación autorizada. E15 conecta estas piezas en **procesos que tienen entradas, trabajo, tiempo, capacidad, pérdidas, destinatario y derechos**. No certifica ninguna cosecha, taller, ruta, negocio, almacén, persona ni suceso.

## Jerarquía y lenguaje editorial
1. **CANON_REPO:** Edranor es el principal territorio vinícola y distribuye vinos por Norgard; Dorth se asocia al tinto, Lumina a blancos artesanos, Karsath a pequeñas partidas selectas; Bosque Alto suministra madera controladamente a tonelería/bodegas de Lumina. Mercado del vino **anual** de Lumina; Rodas **aldea de la Corona**.
2. **DELEGATED_DESIGN:** circuitos causales, roles, balances, escenarios e interfaces de E15 aprobados como criterios de diseño por autorización general del autor. No equivalen a historia ocurrida ni a instalaciones existentes.
3. **UNKNOWN:** viñas concretas, título de propiedad, variedades, volúmenes, tasas, tiempos de crianza, rutas, capacidad de agua, inventarios, precio, número de hogares/profesionales, existencia física de almacenes y talleres.
4. **SYNTHETIC_TEST:** ejemplos con datos ficticios para ejercitar restricciones; absolutamente ajenos al World State y al canon.

**Regla de herencia:** CoreRPG → Defaults Norgard → jurisdicción de Edranor o Corona → lugar/hogar/actor autorizado → World State. Un documento de E15 no crea recursos ni reemplaza los contratos E04/E11.

## Fuentes directas
- `Economia/E04_CADENA_UVA_VINO_BODEGA.md`, `E04_OFICIOS_Y_RED_PRODUCTIVA.md`, `E04_COMERCIO_FISCALIDAD.md` y `E04_MATRIZ_LOCALIDADES_Y_FLUJOS.md`.
- `Viticultura/E04_VITICULTURA_Y_VENDIMIA.md`, `Toneleria/E04_BOSQUE_ALTO_Y_TONELERIA.md`.
- `Ciudades/{Dorth,Lumina,Karsath,Rodas}/E07_*.md`; `Poblacion_y_hogares/E08_OFICIOS_Y_EMPLEO.md`, `Servicios/E08_RED_SERVICIOS_Y_ABASTECIMIENTO.md`, `Autorizaciones/E09_MERCADOS_BODEGAS_BOSQUE_SERVICIOS.md`.
- `E13/06_SUELOS_ECOSISTEMAS_Y_APROVECHAMIENTO.md`, `E14/02_MODELO_CAUSAL_Y_USOS.md`, `E14/05_CAPACIDAD_DEUDA_Y_TRASPASOS.md`, `E14/07_TRASPASO_E15.md`.

## Restricciones y ausencia de materialización
- Cinco anclas: Dorth/Lumina/Karsath bajo Casa Edranor; Rodas bajo Corona Aethros; Hallheim fuera. **Rodas no paga impuestos a Edranor** ni obedece sus órdenes; sin aduanas interiores.
- Las siete unidades E01/E13 siguen siendo expedientes, **U7 no evaluable** mientras la frontera septentrional esté abierta. No inferir viñas boreales ni derecho de tala por ver un bosque.
- E14 conserva **cero parcelas NUEVAS certificadas por esa fase**. No significa que el canon carezca de actividades y habitantes; tampoco permite asignarlos cuantitativamente.
- Ninguna superficie, cosecha, moneda local, coeficiente de conversión, salario, tasa, permiso emitido, camino o muelle se fija en E15. El Bosque Real meridional no se incorpora a la madera de Edranor.
- No se modifica Core, Defaults, Godot, ContentPacks ni contratos históricos bloqueados.

## Criterio de validación
La documentación describe quién necesita qué y qué sucede **si** falta. El JSON es catálogo de diseño; el laboratorio Python se limita a escenarios sintéticos y rechaza cambios de jurisdicción, cifras falsas, obtención gratuita de stock o promoción a runtime. La ausencia de prueba es un estado PENDING_EVIDENCE, no una denegación penal ni un permiso implícito.
