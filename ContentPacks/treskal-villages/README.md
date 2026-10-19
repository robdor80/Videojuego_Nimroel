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

## Artefactos y extracción

- `authoring/source-lock.json`: revisión aprobada y hashes de 34 fuentes.
- `authoring/selection.json`: correspondencia definición → fuente/anchor/pointer.
- `fixtures/v001.json`: receta técnica explícita, sin autoridad sobre el canon.
- `pack/`: nueve archivos reproducibles, incluidos manifiesto, cuatro recursos,
  perfil específico, procedencia, fixture e identidad de publicación.
- `schemas/`: cuatro schemas específicos Draft 2020-12. No son Content Contract
  0.2.0; el sobre Core permanece exactamente en 0.1.0.
- `Tools/CoreRPG413/`: extracción, validación offline y pruebas negativas.

Desde la raíz de Nimroel, con un checkout local CoreRPG fijado (schemas 0.1.0):

```sh
python -m pip install -r Tools/CoreRPG413/requirements.txt
python Tools/CoreRPG413/pack.py --check
python Tools/CoreRPG413/validate.py --core-root ../CoreRPG
python -m unittest discover -s Tools/CoreRPG413 -p test_pack.py -v
python Tools/CoreRPG413/pack.py --output ../scratch/pack-rebuilt
```

El destino de extracción debe ser nuevo. `--check` compara inventario y bytes,
incluido orden canónico/UTF-8/LF; no modifica archivos. No se actualiza el lock de
fuentes automáticamente. Cambiar canon exige revisión explícita, nueva versión de
pack y regeneración, conservando identidades lógicas. El autor sigue editando
Worldbuilding; no debe editar manualmente `pack/` como segunda autoridad.

La validación de instalación sin consultar Worldbuilding:

```sh
python Tools/CoreRPG413/validate.py --core-root ../CoreRPG --installed-only
```

Usa únicamente schemas locales; no descarga URIs de `$schema`. Esta herramienta de
autoría usa Python/jsonschema; el videojuego no necesita Python ni red para consumir
el JSON ya instalado. El futuro adaptador Godot debe implementar/usar la validación
específica equivalente antes de ejecutar reglas Nimroel.

## Fixture estructural y responsabilidades

Semilla explícita `413001`, fuente `explicit_technical_fixture`; generador
`structural-fixture-1`, reglas `v001-handoff-0.1`, instancia
`region-fixture-1/node-0001`. El fixture regional `interior-timber-route-fixture`
versión 1 contiene dos nodos y una salida rural funcional apta para carros.
La frontera exterior es abstracta, no un Pueblo canónico inventado. Costes de
viaje, cruces de agua, estaciones y cobertura regional quedan sin resolver.
No se acredita generación regional completa.

La integración C++ crea aldea, dos **nodos de servicio**, frontera exterior y una
herramienta de categoría ordinaria; declara 50 unidades y materializa dos
identidades anónimas como observadores. Las 48 restantes son latentes, sin EntityId.
Los servicios no obligan a edificios independientes ni a profesionales exclusivos.
No se generan viviendas/hogares: su suficiencia permanece como requisito declarado,
no una prueba de que ya existan. No hay mapa ni NPC individualizados por lore.

Etiquetas estructurales de fixture: 1 (aldea → nodo de servicio), 2 (aldea →
frontera externa), 3 (individuo → agregado poblacional). Son números estables
asignados por este adaptador de prueba, no un registro universal del Core.
La contención de la herramienta en el nodo de servicio no expresa propiedad,
custodia, reparación, empleo ni agenda. El Core sólo valida extremos/forma.
El stream 413 se usa para comprobar continuidad RNG con una tirada explícita,
no para sortear población, profesiones o servicios. No se implementa aún la
fórmula regional de derivación de semillas.

## Compatibilidad externa y guardado

`content-lock.json` fija pack/version, conjunto de pares ID/kind y huella de todos
los documentos distribuidos. Cada archivo usa SHA-256 de sus bytes; el conjunto
y mapa de hashes se codifican como JSON UTF-8, claves ordenadas, indentación 2,
LF y LF final antes de calcular SHA-256. No usar `std::hash` ni orden de filesystem.
El fixture también está incluido; una nueva receta cambia la huella.

El Host debe conservar junto a CRPGSAVE la identidad **original** verificada de
publicación y la huella del contexto inicial (fixture/seed/región/generador/reglas).
Primero valida la publicación instalada y compara contra esos metadatos; después
invoca Persistence::load con catálogo explícito. Cualquier diferencia se rechaza
si no existe una migración explícita. Conservar la publicación antigua permite
continuar la partida sin regenerar nada. La coincidencia de DefinitionId por sí
sola no garantiza compatibilidad de canon. Los hashes detectan cambios, no firman
al publicador; la selección de una publicación de confianza pertenece al Host.

CoreRPG incorpora el ejemplo neutral `examples/external_content_restore.hpp`
para esa comparación previa. No cambia v1/v2/v3 ni guarda catálogo/payloads en el
Core. La prueba conecta el preflight Python real con ese ejemplo y Persistence
real. No existe todavía el almacenamiento físico transaccional de Godot ni una
migración automática entre versiones de canon.

## Android, motores y siguiente fase

Los JSON/localizadores usan `/`, sin rutas de plataforma. Godot podrá distribuir
los archivos dentro de la aplicación y entregar bytes desde FileAccess a
`read_json_document` y los decoders de CoreRPGContentJson. El loader filesystem es
una alternativa desktop; no debe recibir `res://` como una ruta nativa.
CoreRPG sin ContentJson permanece independiente de JSON/filesystem/motor.
No se crea GDExtension ni se acredita NDK, ABI ARM64, excepciones Android,
persistencia entre arquitecturas o ejecución en Galaxy Tab S9+.

4.15/Host deberá resolver TOOL/COND/OWN/WAIT, capacidad/materiales, calendario y
progreso, hogares/layout, descubrimiento/diálogos y consecuencias del encargo.
La IA sólo recibe contexto autorizado y propone solicitudes estructuradas. No
hay rumores, percepción auditiva, secretos completos o personalidad ejecutable
por haber heredado sus documentos. La v0.0.1 jugable sigue pendiente.
