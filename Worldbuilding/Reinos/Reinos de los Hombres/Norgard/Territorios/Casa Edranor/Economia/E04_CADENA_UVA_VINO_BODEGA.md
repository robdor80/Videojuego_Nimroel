# E04 — Cadena del vino: del campo a la venta

## Tres niveles de evidencia
- **CANON_REPO**: Edranor es principal región vinícola y comerciante de vino de Norgard; el vino viaja por el reino. La gastronomía admite vino común, de calidad, joven, añejado y cocinado/especiado como posibilidades, no como cinco marcas existentes.
- **PROPUESTA**: pasos productivos y puntos de trabajo siguientes; permiten diseñar casos para E11, no fijan edificios, máquinas, rendimientos ni productos en stock.
- **UNKNOWN**: localización, variedades, parcelas, equipo, agentes, agua, combustible, tiempos, mermas, inversión y propiedad.

## Circuito operativo propuesto (no producción certificada)
`verificación de suelo / título / permisos → cultivo → vendimia y selección → estrujado/prensado según técnica → mosto → fermentación → trasiegos, cuidado y eventual crianza → recipientes y conservación → venta mayorista/minorista → consumo`.

1. **Habilitación de parcela.** Inspección de suelo E03, clima y riesgos, agua E02, derechos de tenencia, cubierta forestal y límites E01; sin estos requisitos no asignar un viñedo a World State.
2. **Cultivo.** Necesita cepas reales, labores, herramientas, mano de obra y un ciclo meteorológico resuelto. Ni cosecha anual fija ni rendimiento constante.
3. **Vendimia.** Evento de trabajo cuando la fenología y madurez verificadas lo permitan; registro de procedencia y lote. No se fija mes, tradición ni fiesta de vendimia en E04.
4. **Transformación.** La elección de prensado, maceración, fermentación y ensamblaje es tecnología por definir. No todos los vinos tienen por qué seguir la misma ruta.
5. **Bodega.** Capacidad, condiciones de conservación, material del recipiente, edad, origen, custodio y riesgo de deterioro reales. La madera del Bosque Alto alimenta parte de esta cadena según canon, sin monopolio absoluto.
6. **Expedición.** Un lote solo circula si existe, tiene titular legitimado, embalaje y transporte físico; pedidos, fletes, pérdidas y recibos no aparecen por escribir un grafo.
7. **Distribución/venta.** Mayorista, tratante, mercado o taberna son roles posibles, no negocios fundados por este documento.

## Familias de producto
- **Uva:** fresca, seca o de transformación son usos coherentes con la cocina general de Norgard; no se asigna a ninguna variedad concreta.
- **Mosto y vino:** etapas de proceso como diseño; categorías de vino canónicamente posibles, pero no se certifican inventarios o recetas de Edranor.
- **Vinagre:** derivación posible, documentada en la gastronomía de Norgard. No se presupone fábrica de vinagre.
- **Residuos y retornos:** hollejos, lías y recipientes reparables se registrarán como materias reales solo cuando la tecnología y el balance se concreten; no son recursos infinitos.

## Balance material mínimo para E11
Cada transición futura debe conservar `lote_origen`, `owner_ref`, `cantidad real`, `unidad`, `ubicación`, `responsable`, `fecha/ventana`, `transformación autorizada`, `lotes_resultado`, `pérdidas`, `capacidad`, `evidencia`. Nunca convertir una factura o registro en inventario de vino, ni generar uva por cambio de estación.

## Riesgos condicionales
Heladas, sequía, suelo encharcado, erosión, contaminación, fermentación fallida, pérdida de almacenamiento, incendios o interrupción de transporte se investigarán vinculando E02/E03; aquí no se asigna su frecuencia ni se da un suceso por ocurrido.