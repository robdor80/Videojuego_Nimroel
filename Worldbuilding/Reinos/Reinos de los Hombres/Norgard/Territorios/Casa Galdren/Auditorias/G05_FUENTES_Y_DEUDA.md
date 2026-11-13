# G05 — Auditoría de fuentes, decisiones, contradicciones y deuda

**Fecha:** 13/11/2026. **Base auditada:** main b003eaf5a9a4eaeaf5d952b4929db5b439ff99ac, G04 PR #69 fusionada. Salida de G05 en rama separada, sin tocar CoreRPG ni Godot.

## Matriz de procedencia
| Fuente | Aporta | Restricción |
|---|---|---|
| Autor, inicio G05, 13/11/2026 | Forja bajo dominio de Corona/Casa Aethros como Rodas | **DECISIÓN AUTORAL CANÓNICA; prevalece ante texto G00–G04** |
| Norgard/Grandes Casas/grandes_casas.md | Zanthir Galdren, recursos industriales, Rodas y excepción Forja | Rectificada en G05 para dominio regio permanente |
| Norgard/NORGARD.md | Corona única, Casas, Metal Estelar y enclave | Rectificada coherentemente en G05 |
| Norgard/Gobierno y leyes/sistema_militar_norgard_v0.1.md | Mando estratégico bajo Rey | Rectificada excepción de control permanente |
| Norgard/Geografía/montanas.md | Pizarra, hierro, carbón, cobre, Metal Estelar solo Azurios | **No se infieren minas Galdren ni en Zanthir** |
| Norgard/Geografía/rios_y_lagos.md y mares_y_costas.md | Vornarsk, Keldarsk y hielo de Bahía Zanthir | Solo condición regional |
| Norgard/Gobierno y leyes/sistema_fiscal_y_aduanero_v0.1.md | Fisco común, remesas y sin aduanas internas | Sin tarifas, licencias nuevas ni peajes |
| Galdren G00–G04 contratos y traspaso G05 | Zanthir, geografía, clima, alimentación y deuda | Lectura histórica de Forja **SUPERSEDED_BY_G05** |
| Cuaderno de Lore Preguntas 001–104 (aportado al proyecto) | Relato autoral de origen enano, descubrimiento y tres guerras | **PENDIENTE_CONCILIACION**; no cronología ni automatismos nuevos |
| TODO NIMROEL 10.09.26 (aportado al proyecto) | Escena narrativa de Dorvan y Forja apagada | **BORRADOR_NARRATIVO**, no estado actual verificado |

## Cambio explícito G05-D01
ANTES (histórico G00–G04): «forjaOwner UNKNOWN / forjaPeacetimeAdmin casa_galdren / forjaWartimeCommand crown_aethros_hallheim». AHORA (ratificación autoral): «forjaJurisdictionOwner crown_aethros / forjaDirectAdministrationPeace crown_aethros / forjaDirectAdministrationWar crown_aethros / forjaDirectCommandPeace crown_aethros / forjaDirectCommandWar crown_aethros». No se ha reescrito ni manipulado ninguno de los JSON históricos: G05 define un override por fecha/autoridad; los validadores anteriores deben seguir pudiendo comprobar el estado documental de su época.

## Decisiones de diseño G05 (sin nueva historia ratificada)
- G05-D02: cinco minerales Azurios; exclusivamente Azurios para Metal Estelar.
- G05-D03: las siete cadenas de estudio no generan producción ni autorizaciones.
- G05-D04: Zanthir industrial = ámbito territorial; Forja = instalación real, régimen jurídico especial.
- G05-D05: seis relaciones económicas son consultas, no rutas o remesas activas.
- G05-D06: hechos de hielo regional vs daños, delitos y contaminación hipotéticos.
- G05-D07: artesanía enana, tres guerras y Forja apagada se documentan con su nivel de evidencia, sin conciliación inventada.

## Deuda que se traspasa
Minas y canteras identificadas, concesiones, jurisdicción exacta Azurios, trazado de transporte, localización de la instalación, propiedad catastral y su adquisición histórica, personal/custodia/registros, capacidad industrial, procesos reales, energía y carbón, riesgos medidos, suministros, precios, aranceles exteriores aplicables, cronología enana, tecnología y estado operativo de la Forja. Resolver explícitamente en G06/G08/G10/G11 o por ratificación del autor.

## Puertas de cierre
Documentos + contrato JSON no-runtime + validación positiva y ataques negativos + G00–G04 intactos en sus contratos históricos + CI Windows 2022 / Ubuntu 24.04 sobre HEAD exacto. Si falla algún paso, PR Draft sin fusión. Ninguna prueba documental equivale a compilación o juego.
