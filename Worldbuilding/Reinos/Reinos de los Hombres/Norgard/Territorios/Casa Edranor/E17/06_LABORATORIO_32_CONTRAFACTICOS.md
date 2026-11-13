# E17 — Laboratorio de 32 escenarios conceptuales

**Clase de autoridad:** diseño delegado, no hecho canónico, historia consumada ni runtime. Fuente de trabajo: `main` tras E16 (`93499f466cbfb5b920b513b817c6185e727db274`). E18 no se ejecuta en esta fase.

Cada fila representa un **si ocurriera** y no un suceso. `PENDING_EVIDENCE` equivale a dato faltante; `BLOCKED` a prueba explícitamente negativa. Aunque todo estuviera sintéticamente en verde, el resultado máximo es `ELIGIBLE_SYNTHETIC_ONLY`, sin escritura en World State.

| ID | Ancla | Supuesto comprobado | Prueba crítica | Resultado | Reparación lógica |
|---|---|---|---|---|---|
| ED17-H01 | dorth | Grano reclamado pero no inventariado | `stock` | PENDING_EVIDENCE | Mantener necesidad insatisfecha; reintentar solo ante alta de lote legítima |
| ED17-H02 | lumina | Cuidados y jornada incompatibles | `labor` | BLOCKED | Reprogramar según disponibilidad real; no duplicar trabajador ni ignorar menores |
| ED17-H03 | karsath | Agua apta todavía desconocida | `potableWater` | PENDING_EVIDENCE | Solicitar verificación de captación, potabilidad y derechos antes de consumir |
| ED17-H04 | dorth | Leña de procedencia impedida | `forestPermit` | BLOCKED | Registrar demanda no atendida y buscar origen lícito probado |
| ED17-V01 | dorth | Vendimia sin madurez acreditada | `maturity` | PENDING_EVIDENCE | No cosechar por demanda; comprobar parcela, estación y madurez |
| ED17-V02 | lumina | La misma reserva prometida dos veces | `reservationUnique` | BLOCKED | Rechazar segunda reserva o conciliar disponibilidad sin inventar vino |
| ED17-V03 | karsath | Vino selecto sin recipiente apto | `containerSafety` | PENDING_EVIDENCE | Retener lote hasta inspección de capacidad e identidad de recipiente |
| ED17-V04 | lumina | Feria anual convertida en mercado permanente | `marketWindow` | BLOCKED | Respetar el carácter anual y comprobar fecha/permiso reales |
| ED17-B01 | lumina | Bosque Alto sin permiso de aprovechamiento | `forestPermit` | PENDING_EVIDENCE | No extraer; requerir título, zona, permiso y cuota real |
| ED17-B02 | lumina | Duelas sin herrajes acreditados | `parts` | PENDING_EVIDENCE | Mantener piezas intermedias diferenciadas; no completar barrica ficticia |
| ED17-B03 | dorth | Fuga de tonel sin identidad comprobada | `assetEvidence` | PENDING_EVIDENCE | Identificar el contenedor y su custodio antes de deducir o reparar |
| ED17-B04 | karsath | Contenedor reparado sin verificación | `inspection` | BLOCKED | Restringir uso hasta inspección efectiva conservando containerId |
| ED17-T01 | dorth | Corredor Dorth–Lumina confundido con carretera | `routeSurvey` | PENDING_EVIDENCE | Conservar encargo; no despachar ni calcular kilómetros |
| ED17-T02 | lumina | Mercancía en ruta sin acuse | `receiverAck` | PENDING_EVIDENCE | No reconocer consumo, titularidad nueva ni recepción sin acuse real |
| ED17-T03 | karsath | Embarque en muelle urbano no verificado | `portVerified` | BLOCKED | Rechazar itinerario acuático asumido; E19/EDD-07 deberán verificarlo |
| ED17-T04 | rodas | Tránsito a Rodas sin interfaz regia | `crownAuthority` | BLOCKED | Solicitar autorización a Corona; no crear aduana ni derecho fiscal de Casa |
| ED17-S01 | dorth | Fuente de agua sin análisis | `potableWater` | PENDING_EVIDENCE | No prestar abastecimiento hasta probar agua, titular y distribución |
| ED17-S02 | lumina | Molino presumido por demanda de harina | `provider` | BLOCKED | Mantener grano como grano; prestador e infraestructura requieren evidencia |
| ED17-S03 | rodas | Cuidados en aldea regia bajo mando ajeno | `crownAuthority` | BLOCKED | Escalar a competencia de Corona, sin cambiar la titularidad de la aldea |
| ED17-S04 | karsath | Hospedaje sin camas verificadas | `beds` | PENDING_EVIDENCE | No alojar ni crear negocio sin capacidad, agua y responsables |
| ED17-A01 | rodas | Rodas reasignada a la Casa | `owner` | BLOCKED | Denegar operación por jurisdicción y mantener soberanía regia |
| ED17-A02 | rodas | Impuesto doméstico sobre Rodas | `crownFiscal` | BLOCKED | Anular el apunte de Casa; los tributos regios exigen órgano competente |
| ED17-A03 | hallheim | Hallheim anexionada por enlace económico | `territoryMembership` | BLOCKED | Mantener interfaz exterior, no censar ni fiscalizar como Casa |
| ED17-A04 | lumina | Servidumbre deducida por topónimo forestal | `title` | PENDING_EVIDENCE | Requerir título y servidumbre probados sin activar caminos |
| ED17-I01 | dorth | Mensajero nombrado por necesidad | `agent` | PENDING_EVIDENCE | Permanece no entregada; no informar automáticamente al destinatario |
| ED17-I02 | lumina | Rumor recibido como decreto | `receiverAck` | BLOCKED | No difundir; recepción individual y competencia lectora obligatorias |
| ED17-I03 | rodas | Alarma regia sin incidente observado | `eventEvidence` | PENDING_EVIDENCE | No activar emergencias; canal a Corona solo con hecho y receptor real |
| ED17-I04 | dorth | Narración ficticia promovida a historia | `sourceVerified` | BLOCKED | Mantener etiqueta contrafáctica sin pasado consumado |
| ED17-R01 | dorth | Reparar puente que no existe en el registro | `assetEvidence` | BLOCKED | No crear puente ni obra; verificar existencia y titularidad en E19 |
| ED17-R02 | lumina | Reapertura de servicio sin inspección | `inspection` | PENDING_EVIDENCE | Mantener restricción hasta inspección y acuse de reapertura |
| ED17-R03 | karsath | Pérdida contabilizada y recuperada dos veces | `ledgerUnique` | BLOCKED | Asentar pérdida una vez; recuperación exige devolución verificada con nuevo evento |
| ED17-R04 | rodas | Bucle de necesidad sin final ni autoridad | `boundedIteration` | BLOCKED | Cerrar la evaluación en pendiente con identidad de petición y revisión; sin efectos |

## Seis controles cruzados del laboratorio
1. La prueba `false` prevalece sobre cualquier `UNKNOWN`; ausencia de prueba no significa evento rechazado ni aprobado.
2. El escenario con todos los requisitos sintéticos `true` sigue sin actor/activo real ni ejecución autorizada.
3. Inventarios, contenedores, identidad y revisión son idempotentes; no se duplican reservas, pérdidas, devoluciones ni entregas.
4. Rodas, Hallheim, Bosque Alto, el norte U7 y la feria anual no se transforman por inferencia editorial.
5. Una flecha conceptual no genera camino, nodo, puente ni recorrido usable en el motor.
6. Una narración hipotética no crea memoria, suceso, cronología, NPC ni consecuencia fiscal.
