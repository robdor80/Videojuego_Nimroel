# Primer pack de aldeas de Treskal — 4.13

En desarrollo para auditoría humana. Fuente aprobada fijada:
`35c9d22ca3f688c62c709320b20cba565518669d`.

Reutiliza **La primera aldea**, V1 mixta maderera y agrícola; no Treskal ciudad.
El canon existente conserva su autoridad. Los artefactos se derivan de fuentes
integradas, con trazabilidad por SHA y SHA-256; no se incorporan PR #20/#22/#23.

Pack: `nimroel.treskal.villages` versión `0.1.0`, Content Contract `0.1.0`.
Modelo: `nimroel.treskal.villages:models/v1` (`settlement_model`). Aquí v1
identifica la familia del modelo, no una versión de publicación. Capacidades:
`capabilities/basic-blacksmithing` y `capabilities/local-tavern`
(`service_capability`). Categoría `objects/ordinary-agricultural-tool`
(`object_category`). Cuatro definiciones bastan para identificar el modelo y el
puente estructural del encargo; no se crean NPC, casas ni profesiones fijas.

CoreRPG conserva IDs/estado/relaciones/reserva/Knowledge/persistencia. Nimroel
conserva modelo, reglas y procedencia; el Host conservará metadatos de publicación,
contexto de generación y archivos. No se implementan nuevos sistemas RPG ni un
segundo WorldState. Las relaciones numéricas del fixture no otorgan propiedades,
permisos, capacidad profesional o significado automático en Core.

Fuentes: Aldeas/00_Base, modelo V1, los cinco documentos de 03_Prueba_v0.0.1,
metodología, coordinación regional y contratos vigentes de Sistemas. Inventario
exacto en authoring/source-lock.json. Los contratos de Pueblos se consultan para
fronteras y región: su población, probabilidades y hogares no se aplican a Aldeas.
Nimroel Core/Norgard/Valrik son herencia documental, no dependencias físicas de
packs cargables. TOOL/COND/OWN/WAIT/TIME/MEM requieren implementación posterior.

El modelo general permite 35–100 habitantes. V001 ensaya 40–60; el fixture técnico
usará 50 para repetir pruebas sin convertirlo en canon. Pesos, layout, hogares,
nombres y composición profesional siguen pendientes. 4.13 demuestra integración
reproducible; la experiencia jugable y reparación completa pertenecen a 4.15/Host.
