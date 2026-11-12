# E07 — Matriz urbana comparativa y contrato visual para Godot 2D
**Estado:** dirección de arte y arquitectura lógica conceptual; ninguna escena Godot implementada.

| Rasgo | Dorth | Lumina | Karsath | Rodas |
|---|---|---|---|---|
| Autoridad | Edranor | Edranor | Edranor | **Corona Aethros** |
| Paisaje | bosque Azurios próximo, viñedos | meseta, Bosque Alto, viñedo en altura | llanura y lago visual; ribera UNKNOWN | frío, bosques, campos y nieve lejana |
| Bebida | tintos y distribución regional | blancos, producción familiar | partidas de vino pequeñas y exclusivas | sin especialidad vinícola inferida |
| Forma | ciudad logística y administrativa | compacta, acogedora y plaza alargada | pequeña, abierta y de producción restringida | aldea dispersa, plaza abierta |
| Materia | piedra, madera, teja | piedra clara, madera, teja roja | piedra, madera, teja | piedra oscura, madera y pizarra |
| Silueta | baja relativa | baja, no monumental | baja, sin monumentalidad inventada | una planta habitual, Casa Druídica dos |
| Defensa | forma local UNKNOWN | **sin murallas** | forma local UNKNOWN | **sin muro, valla o empalizada** |
| Agua | sin curso local probado | **sin río grande, canal, lago ni puerto** | lago paisaje, **sin costa urbana verificada** | fuente de agua local UNKNOWN |
| Diferencial | flujo de cargas y Casa | plaza, posada y tonelería | rareza, claridad y poco volumen | custodio druídico y berserkers no transformados |

## Guía de composición
Dorth se reconoce por patio de recepción, almacenaje, edificios señoriales y tráfico de mercancías; Lumina, por empedrado cuidado, blancos, pequeñas bodegas y **plaza longitudinal**; Karsath, por paisaje abierto lacustre y bodegas de poca capacidad; Rodas, por su tejido rural discontinuo y el edificio druídico custodiado junto a la plaza. Ningún rasgo permite generar un mapa geográfico automático.

**Gramática 2D sugerida para E11**: LocalityRoot → mapa de suelo autorizado → calles y accesos reales → huellas de edificios → portales de interiores → props decorativos → población/World State → estados de eventos. Son responsabilidades, no nombres de nodos implementados ni APIs aceptadas. Reutilizar módulos gráficos de casa-taller, posada, bodega y plaza, con materiales de cada lugar y sin duplicar la identidad de edificio.

## Reglas de estado e inventario
- Barril visible = recurso de ambientación; NO crea mercancía.
- Ventana iluminada = ambientación; NO demuestra hogar ocupado.
- Banco de plaza = mobiliario; NO crea automáticamente mercado permanente.
- Casa de Druidas de Rodas es hito visual real, pero el control de acceso aún exige E09/E11.
- Plaza de Lumina y mercado anual son referentes visuales aprobados, pero calendario y participantes concretos exigen E08/E11.
- Un camino lógico entre dos áreas nunca sustituye el grafo físico E05: todas sus aristas están aún QUESTION_ONLY.

## Auditoría de encuadre
Una captura sin rótulo debe permitir distinguir las cuatro localidades. Comprobar que Lumina no tiene grandes ríos ni murallas; Karsath no recibe puerto artificial; Rodas no tiene palisada, culto religioso, berserkers transformados paseando ni símbolos Edranor de gobierno. En Dorth, no exagerar verticalidad o decorar la calle de estandartes. Los usos heráldicos deben ser funcionales y nunca inventados.

## Bloqueos de integración
EDD-01/02/03/07; validación de suelos/agua/rutas; E08 censo y propietarios; E09 seguridad y fiscalidad; E10 personas, cronologías y conflictos; E11 portales, colisiones, persistencia y escenarios de pruebas reales.
