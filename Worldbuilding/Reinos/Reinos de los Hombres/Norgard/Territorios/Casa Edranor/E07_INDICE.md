# EDRANOR E07 — Dorth, Lumina, Karsath y Rodas
**12/11/2026 · Diseño manual canónico de localidades · NO RUNTIME**

Fase construida sobre E06, PR #58 fusionada en main el 12/11/2026. Cuatro lugares protegidos; Hallheim queda expresamente fuera y sigue siendo capital de Aethros.

| Núcleo | Identidad | Autoridad | Situación editorial |
|---|---|---|---|
| **Dorth** | Ciudad sede, vino tinto, logística y gobierno de Casa | Edranor subordinada a Corona | Ciudad, censo UNKNOWN |
| **Lumina** | Pequeña, plaza alargada, blancos, bodegas familiares, Bosque Alto | Edranor | Núcleo urbano pequeño; clase jurídica UNKNOWN |
| **Karsath** | Núcleo pequeño lacustre, vino muy escaso/exclusivo, paisaje abierto | Edranor | Escala pequeña; ribera y clase jurídica UNKNOWN |
| **Rodas** | Aldea rural fría, herrerías, Casa Druídica y tradición berserker | **Corona Aethros directa** | **ALDEA**; EDD-06 resuelto para diseño |
| **Hallheim** | Capital real fuera del perímetro | Corona | NO se diseña como Edranor |

## Entregables de fase
- Cuatro monografías de diseño manual: [Dorth](Ciudades/Dorth/E07_DORTH.md), [Lumina](Ciudades/Lumina/E07_LUMINA.md), [Karsath](Ciudades/Karsath/E07_KARSATH.md) y [Rodas](Ciudades/Rodas/E07_RODAS.md).
- [Matriz comparativa, reglas de composición y capas 2D](Ciudades/E07_MATRIZ_2D.md).
- [Edificios, servicios y puertas de materialización](Ciudades/E07_EDIFICIOS_Y_SERVICIOS.md).
- [Doce ideas de actividades jugables condicionadas](Ciudades/E07_GANCHOS_JUGABLES.md).
- [Fuentes, precedencias y resolución de EDD-06](Auditorias/E07_FUENTES_Y_DECISIONES.md).
- [Acta de fase](Auditorias/E07_ACTA.md) y [traspaso a E08](00_Control_del_proyecto/TRASPASO_E08.md).
- Contrato JSON NO-RUNTIME en Datos operativos/edranor_e07_canonical_nuclei_v0.1.json, validador Tools/EdranorE07/validate.py, CI multiplataforma.

## Gobernanza y limitaciones
Jerarquía: Nimroel Core → Norgard Defaults → Casa Edranor / Corona Aethros (según localidad) → Localidad → World State. Las zonas diseñadas en E07 no son calles verificadas, celdas Godot, edificios instanciados, permisos, habitantes, economía activa, rutas E05 o historia ya acontecida.

Toda hipótesis se identifica como **PROPUESTA**. CANON_REPO y VISUAL_APROBADO autorizan rasgos existentes; AUTOR_2026_11_12 sitúa X azul de Rodas; UNKNOWN permanece sin resolver. No heredamos censos de Darovan. No aduanas entre Grandes Casas, no fuerzas Edranor ni impuestos señoriales en Rodas, no magia vistosa casual, no bosques explotados sin derecho.

La implementación en Godot 4.7.2 2D y CoreRPG C++20 corresponde a E11/NIM-08 cuando se ejecute de verdad. La presencia de JSON, Python y CI estática **no acredita gameplay**.
