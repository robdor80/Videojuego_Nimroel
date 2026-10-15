# Darovan — metodología de asentamientos ordinarios v0.1
**Estado:** PRINCIPIOS DE IMPLEMENTACIÓN EN BORRADOR; no establece población ni asentamientos nuevos.

## Regla de clasificación
- **Ciudades canónicas** (Treihord, Veldora, Taramin y Syvaris): diseño manual; nodos de autoridad, producción y logística. Su existencia, nombres y función no son aleatorios.
- **Villas, pueblos, aldeas:** arquetipos de contenido procedural territorial; no crear de antemano ubicaciones/nameplate canónicos.
- **Otros nodos:** minas, bosques productivos, embarcaderos, campamentos, molinos, puestos y caminos. Una instalación no se eleva a villa/pueblo por generar población de trabajadores.
- **Isla de Arven:** arquetipos insulares solo como propuesta de estudio hasta definir jurisdicción.

## Proceso heredado (metodología de Treskal, no cifras)
1. **Mínimo obligatorio:** agua/abastecimiento, acceso, habitabilidad, función y red de servicios según ámbito; población por decidir. Definir límites e incompatibilidades.
2. **Posibilidades:** servicios, tipos de edificio, talleres, espacios comunes, oficios y variantes técnicas permitidas.
3. **Condiciones espaciales:** pendiente, drenaje, riesgo, costa, agua, bosque, vecindad, actividad productiva, conexión logística.
4. **Pesos y probabilidad:** parámetros explícitos versionados **solo** tras revisar datos locales. Ponderaciones no son hechos históricos.
5. **Modelos funcionales:** mixto rural, minero, metalúrgico de apoyo, puerto pesquero, forestal, ruta comercial, insular; son categorías candidatas, no asentamientos existentes.
6. **Instancias:** seed estable, origen, tipo, coordenadas solo si mapa real, persistencia y causalidad; registro de promociones de NPC/objetos.
7. **Validación:** mínimos, oferta/demanda, diversidad zonal, restricciones, sin duplicar edificios/instituciones de ciudades canónicas.

## Zonas que obligan a perfiles distintos
- **Valkram y soporte a Treihord:** minería oro/plata, combustible importado y custodia; no todos los pueblos deben ser mineros.
- **Veldora y su golfo:** comercio exterior y transporte, desembocaduras independientes.
- **Península Taramin:** clima semiárido de transición, pesca litoral y bosque longitudinal que cambia al sur.
- **Syvaris:** litoral abrigado, bahías y calas, interior más seco; sin atribuirle un desierto o bosque uniforme.
- **Norte frío:** densidad/ocupación dependiente de clima, sin presumir asentamientos extensos.
- **Arven (en verificación):** no activar perfil político Darovan.

## Contratos heredados que no se copiarán
- Core: `nimroel_physical_geography_drainage_contract_v0.1.json`, sistemas de propiedad, empleo, residencia, navegación, pesca, obligaciones y conocimiento de NPC.
- Norgard: moneda, justicia, fiscalidad, instituciones militares, toponimia, ley familiar, navegación civil y régimen de Armada.
- Casa Valrik: **solo proceso de esqueleto/posibilidades/probabilidades/instancias**; ninguna densidad, porcentaje, regla de herrería regional ni modelo de madera se convierte por defecto en Darovan.

## Pruebas propuestas (todas ficticias/no canónicas)
- Un pueblo minero sin acceso a transporte o agua debe fallar validación.
- Asentamiento con producción forestal que desborda sus límites de regeneración: prohibir el equilibrio ficticio.
- Puerto fluvial Treihord con gran nave marítima: rechazar.
- Población dispersa isleña sin puerto, agua o ruta: justificar o rechazar.
- Crear una segunda Treihord, Syvaris, Veldora o Taramin por generación: siempre rechazar.
- Aduana entre Casas de Norgard: rechazar por E8.
- Guardia Darovan presentada como armada soberana: rechazar por E5/E6.

## Pendientes antes de generar contenido real
Confirmar rangos demográficos **propios de Darovan**, necesidades por climatología y recursos, cartografía con escala, aprobación de modelos/zones, y contratos ejecutables del motor cuando proceda.
