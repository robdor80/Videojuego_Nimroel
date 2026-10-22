# D09 — Auditoría de fuentes, decisiones y admisibilidad

**Fecha:** 22/10/2026. **Punto de partida:** main `1b64b3894d12c5b95c1894f1a6564c064e5efddb` (D08 PR #34 fusionada, D01–D08 Windows/Linux verde). **Estado:** aprobación sustantiva del autor; NO ejecución.
**Autorización textual:** «Apruebo todas tus recomendaciones...tienes luz verde para implementarlas».

## Lote autoral único (17 decisiones)
| Área | ID / opción | Alcance aprobado |
|---|---|---|
| Gobierno | G01B | dirección Treihord, delegaciones funcionales |
| Gobierno | G02B | administradores consultan actores existentes; sin órgano nuevo |
| Gobierno | G03B | gestión rural/isleña local subordinada, divisiones UNKNOWN |
| Justicia | G04B | funciones judiciales en cuatro ciudades y atención itinerante rural; sin edificios/personas nuevas |
| Justicia | G05C | confirmante concreto de pena capital UNKNOWN, ley de Norgard intacta |
| Gobierno | G06A | existencia y listado de Casas menores Darovan UNKNOWN |
| Fiscalidad | F01B | libros locales, conciliación territorial y rendición a Corona |
| Aduanas | F02C | control aduanero real Veldora + colaboración Darovan |
| Ensaye | F03B | documentos Darovan de producción/ensaye contrastados con supervisión Corona |
| Fiscalidad | F04C | periodicidad/parte exacta remesa UNKNOWN |
| Fuerzas | D01A | Guardia Casa protege Bóveda, Crisol, Vena y escoltas |
| Fuerzas | D02C | guardias locales coordinadas territorialmente |
| Ejército | D03C | fuerza territorial flexible para defensa real |
| Syvaris | D04A | seguridad civil Darovan, Armada de Corona |
| Seguridad | S01B | patrullas adaptadas a hechos, riesgo y recursos |
| Seguridad | S02C | escoltas mixtas según titularidad/amenaza |
| Seguridad | S03B | autorización y custodia coordinadas Crisol–Bóveda |

**G05C/G06A/F04C** son decisiones aprobadas **de mantener UNKNOWN**, no autorizaciones implícitas para completar nombres/cuotas.

## Fuentes y precedencia
1. `Worldbuilding/Sistemas/Nimroel Core/Datos operativos/`: `nimroel_legal_case_sentence_contract_v0.1.json`, `nimroel_transaction_obligation_ledger_contract_v0.1.json`, `nimroel_property_possession_object_contract_v0.1.json`, `nimroel_emergency_personal_response_contract_v0.1.json`, `nimroel_messaging_letters_delivery_contract_v0.1.json` (**contratos de diseño**, no API CoreRPG ejecutada).
2. `Worldbuilding/Sistemas/Norgard Defaults/` E4 protocolo, E5 fuerza, E6 Armada, E8 fiscalidad y E9 penal, además E2 moneda, E11 capacidad y E12 propiedad. Código penal y procedimiento reales no se copian como leyes nuevas.
3. `Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Gobierno y leyes/` organización, sistema fiscal y monetario, sistema militar, propiedad; `Ciudades/Casa Darovan/Treihord.md` para Bóveda, Crisol, Vena y enviado permanente.
4. `.../Casa Darovan/Datos operativos/darovan_d0X_...json` D04–D08; planes, matrices de ciudad, actas autorales y `TRASPASO_D09.md`.

## Controles de alcance
- D08 canónico: Treihord ~32.000; Veldora 29–35 mil; Taramin 14–20 mil; Syvaris ciudad 7–10 mil; Darovan 300–450 mil; urbano 35–45 % y rural 55–65 %, hogares urbanos media 3–5, rurales 4–6, edades globales 30/60/10. No se deduce plantilla funcionarial o militar.
- Arven es Darovan; Karsath no. Cinco ríos / cuatro sistemas; nada autoriza puentes nuevos, itinerarios a islas, nuevos puertos o rutas a minas.
- E5 vigente prevalece sobre menciones históricas de Treihord a revisión militar pendiente; Treihord no se rediseña.
- El enviado real inspecciona, no gestiona las instalaciones; Lord Caedren Darovan (Tesorero de Corona en 15.374) no recibe aquí señorío actual.
- Se preserva la distinción **AUTHORED** (lote y reino), **DERIVED** (compatibilidad), **TEST_ONLY** (casos), **UNKNOWN** (hechos no aprobados). Ni JSON, schema, test o CI crea un habitante, edificio, cuerpo especial o World State real.

## Bloqueos vivos
Lord/Lady actual y herederos; Casas menores concretas; confirmar pena capital; plazo de remesa y porcentajes; oficinas, dotación y ubicaciones precisas; mapa, itinerarios, cronología y capacidades; cargos singulares. Ninguno es precondición para validar D09 estáticamente.
