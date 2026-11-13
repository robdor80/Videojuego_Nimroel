# G01 — Fuentes y decisiones con incertidumbre preservada
**Baseline:** main 5b18e8f255a0ee90a0cb2c6ddf08f16760acc15f, resultado de fusión G00 PR #65. Las doce fuentes exactas de G01 constan en el JSON y deben existir como archivos versionados.

| Origen | Hecho conservado | Inferencia rechazada |
|---|---|---|
| Geografía general / regiones Norgard | Región oriental fértil; franja norte fría; separación física/política | Que una textura o valle sea propiedad de una Casa |
| Montañas y borrador Invernos | Azurios, Velaris, Vareth, Invernos compartidos y bandas altitudinales regionales | Cumbre o paso local exacto, glaciares o frontera sobre toda la cresta |
| Ríos y mares | Caleran y brazos, Vornarsk, Keldarsk, Bahía Zanthir y Suthiros | Nuevos afluentes, puertos, distancias o caudales |
| Bosques | Quebrado, Camino Real, Riberas y Gemelos de Treskal | Nuevos bosques o titularidad exclusiva |
| Grandes Casas / G00 | Arleon/Zanthir Galdren, Treskal Valrik, Hallheim Corona, Dorth Edranor; Forja bajo administración especial | Enclave independiente, propiedad real/institucional no probada |
| Convención toponímica | Nombres descriptivos y antiguos con su propia procedencia | Falsas etimologías enanas o ratificación automática |

## Cuestiones expresamente abiertas
- **G1-C01:** la fuente sitúa el **nacimiento del Caleran en vertiente occidental de Azurios** y el paso por la **llanura oriental**. G01 no inventa un paso hidrográfico ni corrige por su cuenta esta tensión del trazado; examinar en G02.
- **G1-C02:** Montes Invernos son O–E pero el límite Valrik–Galdren cruza N–S; no asignar la cumbre máxima, orillas de Gemelos ni toda la cordillera.
- **G1-C03:** Velaris y Paso de Vareth forman contexto regional canónico, pero la administración Galdren de ese corredor NO está acreditada.
- **G1-C04:** Zanthir asociado a Bahía no da propiedad de toda costa norte; Caleran desemboca en Suthiros sin adjudicar todas las bocas.
- **G1-C05:** Forja Estelar ubicación exacta, título jurídico y régimen patrimonial UNKNOWN; Metal Estelar solo Azurios.
- **G1-C06:** «Laderas Frías» y «Vegas de Arleon» son descriptores propuestos sin lugar independiente confirmado, PROPUESTA_NO_CANON.

## Estado de validación
La batería Python comprueba G00 y G01 con mutaciones adversariales sobre manifest, fuentes e IDs. Windows/Linux son plataformas de CI documental. Sin pruebas reales en Godot 4.7.2, CoreRPG, compilaciones nativas o juego 2D; **no inferir funcionalidad jugable**.

## Deudas transferibles
GDD-01/02 deslinde; GDD-03 Forja; GDD-07 accidentes y agua; frontera Invernos en detalle; origen/transición del Caleran; límites costeros. G02 investiga agua, G03 suelos/estaciones, G05 Forja/minería, G06 caminos, G08 Zanthir urbano, G10 jurisdicción/cultura.
