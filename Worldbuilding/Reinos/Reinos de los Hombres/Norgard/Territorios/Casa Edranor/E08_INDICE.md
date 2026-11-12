# EDRANOR E08 — Hogares, población, servicios y profesiones
**13/11/2026 · Diseño social, económico y contractual · NO RUNTIME**

E07 (PR #59) está fusionada en `main`. E08 **no crea ciudadanos**, censos reales, viviendas, instituciones, comercios ni partidas guardadas. Avanza la arquitectura documental y una batería sintética reproducible.

## Entregables
- [Hogar, vivienda y residencia](Poblacion_y_hogares/E08_MODELO_HOGAR_RESIDENCIA.md): convivencia, tenencia, cuidados, transición de residencia e identidad.
- [Censo pendiente y carga estacional](Poblacion_y_hogares/E08_CENSO_CARGA_ESTACIONAL.md): cierres de capacidad y contabilidad de personas.
- [Profesiones y contratación](Poblacion_y_hogares/E08_OFICIOS_Y_EMPLEO.md): roles y protección laboral de Norgard.
- [Red de servicios](Servicios/E08_RED_SERVICIOS_Y_ABASTECIMIENTO.md): agua, saneamiento, alimentación, salud, alojamiento y mantenimiento.
- [Matriz por localidad](Servicios/E08_MATRIZ_LOCALIDADES_Y_PUERTAS.md): Dorth, Lumina, Karsath y Rodas, sin servicios instalados automáticamente.
- [Manifiesto JSON](Datos%20operativos/edranor_e08_population_services_v0.1.json) y [fixtures sintéticos](Datos%20operativos/edranor_e08_synthetic_fixtures_v0.1.json).
- [Auditoría de fuentes y deuda](Auditorias/E08_FUENTES_Y_DEUDA.md), [acta](Auditorias/E08_ACTA.md), [traspaso E09](00_Control_del_proyecto/TRASPASO_E09.md).
- `Tools/EdranorE08/validate.py`, workflow multiplataforma E00–E08.

## Preservación del canon
Dorth: ciudad sede y tintos. Lumina: núcleo compacto, blancos, plaza alargada, mercado **anual**, posada como **tipo visual** y explotación **controlada** del Bosque Alto. Karsath: núcleo pequeño de vino escaso/exclusivo, contexto lacustre sin orilla urbana confirmada. Rodas: **aldea Aethros** con herrerías, plaza abierta y Casa Druídica de dos plantas custodiada, **NO templo**; ningún impuesto, mando, efectivos o monopolio de Edranor. Hallheim fuera. Sin aduanas interiores.

**Censo EDD-04 pendiente:** población, hogares, composición etaria, capacidad de agua, camas, empleo, servicio, horarios y ratio de ocupación en cada localidad `UNKNOWN`/`null`. No importar cifras, proporciones, profesiones individualizadas ni taxonomías jurisdiccionales de Darovan o Valrik.

## Criterio de cierre
Se cierra la **entrega documental E08** con pruebas estructurales y de casos sintéticos; la entrada a E09 se realiza en conversación separada. No hay prueba Godot/CoreRPG ni Content Pack ejecutable.
