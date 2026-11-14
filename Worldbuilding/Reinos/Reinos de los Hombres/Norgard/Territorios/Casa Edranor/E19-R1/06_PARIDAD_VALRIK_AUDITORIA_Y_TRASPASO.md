# E19-R1.06 — Auditoría de suficiencia, paridad con Valrik y entrega a R2
**Fecha:** 14/11/2026. **Corte de fuente:** main `223f1e49adfbc73be6a80c6ce36e7aab506450c2`; base E19-R0 `addd767de9bf27ef35e8aef6d68cde00dea79c10`.

## 1. Alcance auditado
Se han leído explícitamente en Valrik/Treskal: `Geografia_local/montes_invernos_cotas_y_altitudes.md`, `microrelieve_y_unidades_de_drenaje_v0.1.md`, `cuencas_manantiales_red_hidrografica_menor_v0.1.md`, `reglas_espaciales_generacion_motor_v0.1.md` y su README. **El método homologado** es ancla mayor → macrorelieve → microrelieve → drenaje → cuencas → red menor → microclima → suelo/cubierta → uso humano → World State. Edranor no hereda nombres, cuencas ni contratos métricos de Valrik.

## 2. Matriz de cobertura
| Dimensión de Valrik | Estado Edranor al entrar R1 | Entrega R1 | Lo que falta |
|---|---|---|---|
| grandes sistemas montanos | Valkram/Azurios existentes, vertientes confirmadas en R0 | morfología propia, divisorias y contactos | perfiles de relieve reales |
| unidades naturales | E01 siete unidades; R0 seis nombres de diseño | ocho contextos morfológicos ligados a E01; no nuevas provincias | límites físicos situados |
| microrelieve | E13 vocabulario y bandas hipotéticas | 5 valles, lomas, mesetas, piedemonte, depresiones, 4 perfiles causales | cuencas y arroyos instanciados |
| hidrología principal | Lurien/Antela regional | coherencia por receptores y vetos de trasplante | R2 detalle de cuencas, manantiales, permanencia |
| toponimia menor | ocho propuestas E13 | 6 seleccionadas de diseño + 12 candidatos + 2 reservados; 8 grandes referentes de autoridad | ratificación local y su correspondencia con terreno |
| clima y cubierta | E03 y bosques canónicos | vínculos exposición/agua/vegetación sin falsa cifra | R3 suelo, balance, calendario y riesgo |
| red natural y viajes | E05/Gp 0 aristas | 3 clases de collado, condiciones de acceso, no caminos | R4 corredores/caminos con derecho y seguridad |
| asentamientos y economía | anclas y sectores E07, E15/E16 | compatibilidad de relieve con vino, madera, logística y Rodas | R5 sitios, tenencia, aforos y censos |
| fabricación de mundo | contrato conceptual E13 | reglas de continuidad, procedencia e ID | E19-TEC/E28 y pruebas de runtime |

**Juicio:** **paridad metodológica específica de relieve/toponimia de R1** con Valrik, no paridad integral del territorio ni cartografía implementable. El modelo Valrik de red hidrográfica menor pertenece a R2: **no declarar completado R2 aquí**.

## 3. Pruebas de prohibición
1. Valkram oeste Darovan / este Edranor; Azurios oeste Edranor / este Galdren. No invertir laderas.
2. Lurien nace en Valkram oriental; atraviesa Antela; sigue Hallheim-Golfo. Antela al sur de Karsath; no puerto asumido.
3. Sur de Aethros solo sigue **parte** del Lurien, no todo el río; el resto administrativo.
4. Norte no se cierra artificialmente; U7 no evaluable.
5. Rodas aldea de Corona Aethros; Hallheim exterior.
6. Bosque Alto no tala libre; Bosque Real no es recurso Edranor.
7. Dorth = tinto/sede; Lumina = blancos, núcleo pequeño, feria anual; Karsath = vino selecto pequeño.
8. Sin Caleran en Dorth, Vareth en Edranor, Viuda apropiada o ríos Belara/Lhera trasladados.
9. Los nombres de propuesta jamás devienen accidentes materiales, históricos o autorizaciones.
10. 0 coordenadas, polígonos, caminos, cruces, afluentes locales, habitantes, parcelas o World State creados.
11. No se usa la PR descartada #84.
12. R1 no se declara B3/B4 ni validación CI si el HEAD exacto no ha superado los comprobantes.

## 4. Decisiones delegadas
| Decisión | Se elige | Se descarta | Justificación |
|---|---|---|---|
| ED19R1-01 | Atlas morfoestructural como primer producto | calcar el rotulador rojo | instrucción autoral R0 y método Valrik |
| ED19R1-02 | Ocho contextos MF sin nuevas provincias | sustituir los siete IDs E01 | compatibilidad documental |
| ED19R1-03 | Dos piedemontes diferenciados | relieve uniforme entre montañas | identidad natural Edranor |
| ED19R1-04 | Seis nombres E13/R0 como diseño condicionado | promocionarlos a canon de World State | preservar trazabilidad |
| ED19R1-05 | Doce nombres C como propuestas, dos reservas D | inventario forzado de lugares existentes | topónimos deben proceder de formas |
| ED19R1-06 | Perfil R1 sin coordenadas ni metros | exigir m/píxel para lore | paridad real de Valrik |
| ED19R1-07 | R2 se encargará del receptor y permanencia | inventar hidrónimos y arroyos en R1 | continuidad hidrográfica |
| ED19R1-08 | Separar bosque y propiedad | ceder Bosque Real o explotación libre | canon de Norgard y Corona |
| ED19R1-09 | Validez narrativa B2 independiente de mapa técnico | presentar Godot como ya materializado | honestidad de madurez |
| ED19R1-10 | E19-R1 como PR apilada sobre R0 | modificar main/PR descartada | una fase, una conversación, dependencia explícita |

**Autoridad de estas decisiones:** `ASSISTANT_DELEGATED_DESIGN`. No constituyen acto histórico, jurisdiccional, genealogía, permiso de aprovechamiento ni fuente para redibujar la frontera del autor.

## 5. Estado de deudas
| Código | Estado al salir de R1 | Puerta de aceptación futura |
|---|---|---|
| EDD-01 | reglas de frontera natural autoral resueltas; **geometría de diseño material pendiente** | representaciones posteriores coherentes con divisorias y sin cierre norte inventado |
| EDD-02 | pospuesta a fase técnica Godot | medidas solo cuando sean necesarias para runtime |
| EDD-03 | **abierta: R2** | receptores, cuencas, permanencia y topología plausibles |
| EDD-04 | abierta: E26 | hogares, capacidad y censo |
| EDD-05 | abierta: E25 | personas y legitimidad |
| EDD-06 | resuelta **solo para diseño** | Rodas aldea Corona; no transferencia |
| EDD-07 | abierta: R4/E28 | vías físicas y permisos probados |
| EDD-08 | abierta: E27 | hechos históricos y relaciones ratificados |

## 6. Traspaso estricto a E19-R2
**R2** deberá: (a) definir familias de cuenca por relieve válido y receptor explícito; (b) diferenciar oeste/este de divisorias sin hacer que los cursos «atraviesen montañas» arbitrariamente; (c) evaluar surgencias, ríos menores y cauces efímeros por causa, no por distribución aleatoria; (d) estudiar relación real de drenajes con Lurien/Antela cuando proceda, sin dar por hecho todas las conexiones; (e) preservar ausencia de puerto urbano Karsath y de un gran río Dorth; (f) registrar casos negativos, versionado y persistencia; (g) no materializar aún Godot ni alterar bosque, Corona o historia.

R2 no está iniciado ni entregado en esta PR; R3–R6 y el trabajo técnico siguen pendientes. Los topónimos C pueden revisarse y descartarse; si «La Nava de Rodas» no corresponde al suelo, se retirará.

## 7. Condiciones de aceptación documental
1. Control cruzado de `natural_features_v0.2.json` con R0 `natural_regions_v0.1.json`.
2. ID y nombre no duplicados; clases y autoridad de todos los candidatos.
3. Prueba negativa de al menos un intento de transformar un nombre C en CANON; un paso en carretera, un río inventado, Bosque Real apropiado, Rodas transferida o norte cerrado.
4. Conservar R0 intacta y documentar dependencia de rama.
5. Workflow Ubuntu/Windows en HEAD exacto, sin afirmar ejecución si falta evidencia.
6. Auditabilidad de cada documento contra el método de Valrik.

**Resultado editorial R1:** corpus profundo de morfología y toponimia **propuesto para integración tras auditoría**, no certificación de geografía material.
