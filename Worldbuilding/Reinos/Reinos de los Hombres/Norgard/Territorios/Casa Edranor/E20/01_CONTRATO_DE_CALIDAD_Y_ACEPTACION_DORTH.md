# E20-P00 — Contrato de calidad de Dorth y equivalencia territorial

**Estado:** criterio de admisión, no certificación ni autorización para inventar canon. **Patrón:** Valrik/Treskal v1.0. **Objetivo:** Dorth será una ciudad distinta de Treskal, pero igual de fundada, comprensible, espacialmente consistente, socialmente viva y técnicamente aprovechable.

## 1. Regla de oro

**No se aceptará E20 como COMPLETADA** por acumular 99 capas, dibujar un SVG bonito o aprobar pruebas sobre objetos sintéticos. Debe haber suficiente evidencia para que un desarrollador pueda reconstruir Dorth en 2D, que los sistemas de Nimroel puedan consultar sus objetos y que un jugador encuentre una comunidad coherente. **No afirmaremos B4 hasta la integración real.** Cada requisito tiene un responsable, una prueba y un estado honesto.

## 2. Especificación exigible por dominio

### A. Identidad y autoridad — MUST
- Dorth es la sede **administrativa** de Casa Edranor, bajo la única Ley del Rey de Norgard.
- Deberá distinguir de forma legible administración señorial, recepción regia, justicia, custodia y espacio público.
- Ni independencia legislativa, ni castillo desmesurado, ni fiscalidad o mando sobre Rodas.
- El ciervo de plata envejecida sobre púrpura se usará solo en soportes heráldicos funcionales, nunca banderas ambientales masivas.
- Pruebas: contratos de jurisdicción y casos adversariales reales del mapa, sedes y órdenes.

### B. Situación y relieve — MUST para B3
- Límite territorial, huella urbana, norte, sistema de coordenadas, unidad y relación con el terreno verificables y procedentes de fuente admisible.
- Ubicación local de Azurios como vecindad real o visual según soporte; **sin apropiación del Bosque Real**.
- No adjudicar río, puerto, canal o puente a Dorth si no existe fuente.
- Pruebas: geometría cerrada, nodos, cruces, error de calibración, controles y validación inversa de coordenadas.

### C. Organización funcional y grafo de ciudad — MUST para B3
- Sectores identificables y funciones distintas: casa/administración, vida cívica, talleres, recepción de vendimia, elaboración, guarda, expedición, viviendas y borde forestal.
- IDs propios de Dorth, no T01–T12 ni S01–S13 de Treskal. Las relaciones de carga y accesibilidad deben estar motivadas.
- Edificios singulares con huella y puerta; tránsito público, carro pesado, custodia y accesos reservados diferenciados.
- Pruebas: grafo conectable, conectividad y acceso, no solape incompatible, carga pesada sin cuello residencial absurdo, retorno a mapa tras guardar/cargar.

### D. Materialidad edificada e interiores — MUST para B3 funcional
- Tipología de casa, taller, bodega, archivo, almacén, posada y patio con escala y función.
- Recepción de uva, prensado, trasiego, guarda y despacho tendrán necesidades espaciales coherentes (circulación, higiene, almacenamiento, madera, incendios).
- Interiores jugables donde la misión lo exija y puntos de actividad estables, sin prometer cada habitación modelada.
- Pruebas: capacidad física, puertas, distancias, rutas de suministro y salidas.

### E. Economía vinícola vivida — MUST
- Cadena concreta uva → recepción → registro → prensa/elaboración → barrica → crianza/guarda → venta/expedición.
- Introducir productores, derechos, lotes y stock **solo** cuando tengan autoridad, procedencia y persistencia.
- Vino tinto, no denominaciones, precios o variedades inventadas. Distinguir factura real de muestra y escenario.
- Se deberá modelar reacción a malas cosechas, pérdida de barricas, daños o interrupciones de abastecimiento sin conjurar mercancía.
- Pruebas: conservación de entradas y salidas, idempotencia, titularidad, inventario y costo de viaje con vías realmente existentes.

### F. Bosque, madera y tonelería — MUST
- Edranor produce toneles y barricas con requisitos de madera, secado, calidad, oficio y cuidado del bosque.
- El Bosque Alto y Azurios no son licencia de explotación ilimitada. Los propietarios, permisos, aprovechamientos y traslados deben poder verificarse.
- No habrá acceso ficticio Lumina–Dorth si no existe camino real certificado.
- Pruebas: cupos/permisos, origen de tablas, lotes de madera y rechazo de tala sin derecho.

### G. Población, hogares y empleo — MUST para ciudad habitada
- Censo o población propuesta correctamente etiquetada; hogares individuales y colectivos con residencia identificable; edades, ocupaciones y dependientes.
- Necesidades de trabajo y plazas en talleres, bodegas, venta, transporte y servicios coherentes con las personas disponibles.
- Un edificio no se puebla por existir en el plano; un NPC no se produce por figurar su nombre en un contrato.
- Pruebas: sumas hogar/población, ocupación laboral compatible, capacidad de vivienda, ausencia de doble residencia y continuidad de IDs.

### H. Servicios y vida cotidiana — MUST
- Agua, distribución, saneamiento, residuos, combustibles, curación, abastos, mercados, alojamiento, cuidado, descanso, formación, carga y mantenimiento.
- No duplicar reglas globales de Nimroel, heredar Norgard Defaults y parametrizar accesibilidad/capacidad local.
- Las actividades deben reaccionar a horarios y estaciones del canon general, no a calendarios inventados.
- Pruebas: caso de una jornada ordinaria, caso de estación adversa y caso de servicio fuera de capacidad.

### I. Personajes, vínculos y memoria — MUST
- Biografías con nombre/filiación y legitimidad documentada según E25; relaciones territoriales, conocimiento parcial, reputación, secretos y competencias.
- NPC persistentes con vivienda, empleo, actividad, hábitos, confianza y alcance de conocimiento.
- No mezclar el relato hipotético de E17 con un hecho histórico ocurrido. Aceptar versiones divergentes solo con fuente/narrador.
- Pruebas: se identifica a la misma persona tras recargar, no duplica hogar, conoce solo lo permitido, conserva memorias y relaciones coherentes.

### J. Conflictos y juego emergente — MUST
- Encargos locales construidos desde entidades reales: barricas defectuosas, lotes, permisos, rumores, negocios, convivencia, registros y reclamaciones.
- Ningún encargo puede alterar jurisdicción regia, atribuir delitos consumados o transformar una propuesta en canon sin decisión.
- Pruebas: estados inicial/intermedio/final, causas, tiempo, testigos, consecuencias, recuperación, fallo y persistencia.

### K. Seguridad, riesgos y reparación — MUST
- Protección de mercado, incendio de bodega, extravío de mercancía, accidente de trabajo, tránsito de carros, daños y restauración.
- Competencias reales de instituciones y vecinos; nunca delegar la sentencia en un NPC sin base jurídica.
- Pruebas: respuesta ante emergencia, trabajo interrumpido, recuperación y efectos sobre stock, hogares, servicios y reputación.

### L. Materialización 2D / estabilidad — MUST para B3/B4
- Geometrías 2D autoritativas y exportables (preferencia GeoJSON con CRS local válido; SVG técnico, operativo y lore derivados coherentes).
- IDs permanentes para objetos, hogares, rutas y parcelas; nombre visible desacoplado del identificador técnico.
- Regiones materializadas fuera del runtime y persistidas; no reroll al volver a entrar ni al actualizar reglas sin migración.
- Pruebas: importación, lookup espacial, colisiones/pasos, reversibilidad, hash/IDs, regeneración determinista y migración.

### M. Integración real — MUST para B4, NO exigible para declarar B3
- CoreRPG debe ser autoridad para hechos, identidades y consecuencias; Godot 4.7.2 Standard 2D representa el estado. Windows x64 y Android ARM64 son plataformas de destino.
- Una prueba nativa aislada en C++ no sustituye a una escena real del juego.
- Pruebas: cargar la escena en Godot, mover un personaje por rutas admisibles, interacción con entidad del pack, modificar World State, guardar/cerrar/reabrir y recuperar mismo estado.

## 3. Protocolo del plano: aprender del método de Treskal

No se trasplanta el plano: se trasplanta el rigor de los **10 puntos**.

| Punto de referencia | Adaptación obligatoria Dorth | Salida |
|---|---|---|
| 1 Auditoría de canon | Autoridades y reservas de suelo | Documento de no contradicción |
| 2 Escala y huella | Límites y escala de Dorth | Envolvente certificada |
| 3 Geografía métrica | Relieve y agua local si respaldados | Terreno y drenajes |
| 4 Sectores | Zonas funcionales de la ciudad vinícola | IDs y polígonos |
| 5 Instalaciones | Sede, bodegas, talleres, mercados, servicios | Huellas y accesos |
| 6 Red viaria | Carros de vendimia, servicio y peatones | Grafo transitable |
| 7 Especialización | No puerto: recepción, elaboración, guarda, transporte, Azurios | Logística local |
| 8 Parcelas y tejido | Viviendas, patios, viñas solo donde legal y físico | Parcelario reproducible |
| 9 Validación integral | Cruce de autoridad, riesgos, servicios y economía | Batería adversarial |
| 10 Mapa canónico | Export técnico/operativo/lore e IDs concordantes | Fuente espacial maestra |

**Nota esencial:** los puntos 2/3 requieren resolver E19-R para el marco territorial. El punto 7 se adapta a la especificidad vinícola y **no copia** las infraestructuras navales de Treskal.

## 4. Test de aceptación global

La puerta de **E20-Dorth B3** solo puede pasar con: A–L documentados e instanciados a escala de ciudad en la medida aplicable; planos con geometría comprobable; al menos un flujo económico completo materializable; población/servicios con identidad; un grafo transitable; casos de fallo; y una matriz de evidencia por requisito. No fija una cifra arbitraria de calles, habitantes ni parcelas. Se justifica la suficiencia por funciones, capacidades y dimensión urbana.

La puerta **B4** exige M demostrado en juego. Aunque B3 pase, B4 puede quedar cerrado por falta de integración, y así se informará.

No se cerrará Edranor global por haber cerrado Dorth: Lumina, Karsath, Rodas y campo requieren evidencias locales equivalentes y sus propias puertas.

## 5. Casos adversariales obligatorios

1. Una orden señorial de cobrar impuestos en Rodas debe rechazarse.
2. Una feria mensual en Lumina no podrá promoverse sobre su feria anual.
3. Karsath no obtendrá muelle ni carretera ribereña por su perfil visual lacustre.
4. Dorth no obtendrá puerto, río mayor o puente de un atlas incompleto.
5. El Bosque Alto no entregará madera sin titularidad/licencia.
6. El mapa E19 #84 no podrá aparecer como fuente autorizada.
7. Una viña en U7 no evaluable no podrá convertirse en campo productivo.
8. Un escenario E17 no podrá mutar historia ni generar NPC reales.
9. Un cambio de seed no podrá duplicar parcelas/negocios persistidos.
10. Un artefacto JSON sin escena integrada no bastará para declarar B4.

## 6. Registro de evidencia

Cada unidad implementada debe poder citar un expediente: ID, jurisdicción, fuente/categoría de autoridad, geometría, función, ocupantes, capacidad, permisos, interacciones, dependencias, contrato, tests, importador, versión y estado. Los campos UNKNOWN permanecerán explícitos. Cada test debe distinguir **diseño contractual**, **instancia material** y **ejecución runtime**. La revisión final de E20 tendrá un dictamen: CONFORME, CONDICIONADA o RECHAZADA; no hay cierre tácito por número de PR o fecha.
