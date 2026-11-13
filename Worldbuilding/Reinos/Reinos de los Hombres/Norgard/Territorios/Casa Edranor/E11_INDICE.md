# EDRANOR E11 — Integración contractual, Content Pack y pruebas técnicas
**13/11/2026 · Contrato estructural 0.1.0 · Integración de laboratorio, NO gameplay**

## Resultado diseñado
Se publica `ContentPacks/edranor-territory` conforme al precedente D11 Darovan y al contrato oficial de CoreRPG. Cinco DefinitionId estables: `nimroel.edranor.territory:territory/edranor` y `nimroel.edranor.territory:places/{dorth,lumina,karsath,rodas}` (cada nombre literal tiene su propio recurso). **Los cuatro son anclas protegidas, nunca spawns procedurales**.

La proyección autoral del paquete preserva las once fuentes E00–E10 mediante SHA de blob, autoridad por localidad y datos UNKNOWN. El manifiesto solo tiene referencias técnicas; no concede a Edranor la administración de Rodas. Ninguna herencia, nombre dinástico ni conflicto E10 se transforma en NPC, ley, tratado, guerra o quest.

## Documentos de entrega
- [Pack](https://github.com/robdor80/Videojuego_Nimroel/tree/feat/edranor-e11-contentpack-contratos-20261113/ContentPacks/edranor-territory) (documento de la rama E11).
- [Auditoría y deuda](Auditorias/E11_FUENTES_Y_DEUDA.md).
- [Acta y pruebas](Auditorias/E11_ACTA.md).
- [Traspaso E12](00_Control_del_proyecto/TRASPASO_E12.md).
- `Tools/EdranorE11/validate.py`, `Tools/EdranorE11/cpp_smoke.cpp`, `Tools/EdranorE11/CMakeLists.txt`, `.github/workflows/edranor-e11.yml`.

## Semántica de la integración
CoreRPG carga únicamente **identidades y enlaces**. No se ha creado binding funcional Edranor↔Godot 4.7.2 ni ejecución de motor sobre mundo poblado. Las pruebas C++ usan estado sintético aislado y no acreditan simulación territorial.
