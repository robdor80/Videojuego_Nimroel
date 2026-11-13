# E17 — Auditoría, decisiones delegadas y traspaso a E18

**Clase de autoridad:** diseño delegado, no hecho canónico, historia consumada ni runtime. Fuente de trabajo: `main` tras E16 (`93499f466cbfb5b920b513b817c6185e727db274`). E18 no se ejecuta en esta fase.

## Registro de decisiones
| Código | Elección de diseño delegada | Alternativa rechazada |
|---|---|---|
| ED17-DEC-01 | Identificador causal y evidencia previa a todo efecto | disparar efectos en cuanto aparece la demanda |
| ED17-DEC-02 | Invariantes de lotes, reservas y conciliación transaccional | producir recursos o gastarlos dos veces |
| ED17-DEC-03 | Eventos de comunicación y conocimiento solo con recepción | omnisciencia entre asentamientos |
| ED17-DEC-04 | Jurisdicción de Rodas y exclusión de Hallheim | absorber enclaves y gravarlos |
| ED17-DEC-05 | No degradar UNKNOWN a True por presión narrativa | atribuir carretera, agente, agua o proveedor inventado |
| ED17-DEC-06 | Proveniencia de memoria con distinción entre hipótesis y hechos | grabar escenarios de diseño como historia |
| ED17-DEC-07 | Recuperación condicionada a activo, piezas, trabajo e inspección | reparación instantánea o reinicio gratuito |
| ED17-DEC-08 | Cierre de bucles por evento único, revisión y causalidad finita | torbellinos de reintentos y ecos |
| ED17-DEC-09 | Escenario conceptual no equivale a mundo jugable | activar CoreRPG o Godot por ejecutar Python |
| ED17-DEC-10 | E18 audita madurez; E19/E26/E28 resuelven evidencia material | dar por terminada la geografía, censo o gameplay en E17 |

## Suficiencia documental y límites
- **Entregado:** 32 escenarios conceptuales en ocho familias, trazabilidad de anclas, grafo causal solo de plantillas, prohibiciones normativas, modelo de recuperación e interfaz para eventos futuros.
- **No entregado ni reclamado:** NPC o hogares reales, rutas, cartografía E19, censo E26, fechas E27, historias consumadas, misiones y gameplay E28. Sin modificación CoreRPG/Godot/Content Packs, sin promoción del atlas a canon superior.
- **Deuda sin clausura:** EDD-01/02/03/04/05/07/08 abiertas; EDD-06 resuelta para diseño. La mención de un mecanismo no aporta evidencia de su existencia.

## Traspaso: E18 — auditoría de madurez intermedia (no iniciada)
Evaluar E13–E17 en las 10 dimensiones de Nimroel (geografía, clima, recursos, asentamientos, población, instituciones, cultura, personajes, conflictos y contratos de implementación); identificar coherencia, contradicciones y vacíos antes de E19. Comprobar métricas UNKNOWN, U7, Rodas Corona, excepciones forestales, Gp vacío, acuses de comunicación, balances y 32 escenarios contrafácticos.

## Dependencias posteriores
E19: geometría y derechos EDD-01/02/03/07. E20–E24: prestadores, contextos por localidad y hogares reales si procede. E25: linajes. E26: censo y capacidad. E27: ratificación cronológica. E28: contratos persistentes y pruebas reales en CoreRPG/Godot 2D. **Ningún éxito de Python demuestra ejecución del videojuego.**

## Puertas de fusión
SHA exacto, regresiones E00–E16, schema locks E11 y consumidor Core C++20/CTest con pin fijo Ubuntu/Windows; validador E17 positivo y mutaciones adversariales; diff sin modificar canon ni siguiente fase. Si falla, PR Draft sin fusionar.
