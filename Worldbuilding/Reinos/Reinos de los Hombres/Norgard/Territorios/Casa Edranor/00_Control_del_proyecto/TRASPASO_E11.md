# Traspaso E10 → E11 — Integración contractual y pruebas reales

E10 aporta **material narrativo de diseño**. E11 es otra fase, otra rama y otra PR desde `main` posterior a E10, sujeta a nueva autorización.

## Entradas
1. `Datos operativos/edranor_e10_lore_v0.1.json` para IDs semánticos **no NPC** y estados de canon.
2. E07 cuatro anclas/representación 2D, E08 personas y hogares NO instanciados, E09 competencias y procedimiento legal.
3. Norgard Defaults y sistemas NAME/KIN, propiedad/herencia, KNOW, autoridad, PREG/AGE, inventarios, AGEN y World State.
4. Historia H01–H05 relativa, matriz C01–C08 y semillas S01–S08, sin desenlaces fijos.

## Puertas obligatorias
- Revisión y ratificación **explícita** de nombres/propuesta EDD-05 antes de crear miembros protegidos de Casa, documentos de filiación y NPC con ID.
- EDD-08 solo puede adquirir fechas y actos si una fuente superior/autoral lo respalda; Rodas no cambia competencia por diálogo ni por ganar una misión.
- Un mapa final, rutas físicas, aguas y parcelas necesarios para escenas deben provenir de EDD-01/02/03/07 resueltos, nunca del contrato E10.
- Materializar instituciones solo tras autoridad E09 efectiva; ningún civil se convierte por dibujo en funcionario.
- Escenas 2D y misiones deben proteger `jurisdiction`, `source_refs`, `actor_knowledge`, `consent`, `version`, `consequence` e idempotencia.
- Pruebas de lectura, validación negativa, persistencia y recuperación; reportar por separado compilación Godot GDExtension/CoreRPG cuando realmente se ejecute.

## Canon innegociable
Dorth/Lumina/Karsath Edranor; Rodas Corona; Hallheim fuera. Una Ley, misma moneda, sin aduanas entre Casas; sin orden Edranor sobre berserkers, sin culto ni magia ambiental en Rodas. Familias y oficios no equivalen a tasas o tropas. Ninguna salida de E10 **ejecuta** un evento.

## Estado
E10 entrega diseño. **E11 no iniciado.**
