# E09 — Administración civil, competencias y registros

## Base normativa CANON_REPO
En Norgard existe un solo Rey y una sola Ley. La Casa Edranor puede administrar su dominio, impartir la Justicia del Rey y gestionar rentas legalmente autorizadas; la Corona conserva soberanía, fiscalidad superior, revisión judicial excepcional y autoridad militar suprema. El señorío es hereditario y la Corona confirma formalmente sucesiones ordinarias. **No se conoce todavía el nombre del Lord/Lady Edranor, sus herederos ni la composición de su consejo (EDD-05; E10)**. No inventar un gobernador de Edranor: ese título general corresponde a territorios humanos externos a Norgard.

## Separación de sujetos — PROPUESTA de contrato
- **Corona:** ley, supremacía, órdenes reales, moneda, movilización del Reino, rendición de cuentas y Rodas.
- **Casa Edranor:** administración subordinada en Dorth, Lumina y Karsath, hacienda delegada, custodia del protocolo regio, defensa propia y Justicia del Rey dentro de competencia.
- **Órgano judicial competente:** examina un caso y sentencia bajo ley común. El magistrado no es idéntico al tesorero, al dueño de una bodega ni al comandante.
- **Hacienda o responsable fiscal habilitado:** registra obligación, recibo, compensación, cobro, remesa y auditoría; no inventa base ni tarifa.
- **Autoridad local habilitada:** administra usos públicos, orden y licencias conforme a delegación documentada, sin crear legislación penal ni tributaria.
- **Propietario, poseedor, arrendatario, comerciante y proveedor:** cada cual conserva derechos y obligaciones propios. El ciervo de Edranor pintado en una fachada no demuestra propiedad de la Casa.
- **Cuerpo de seguridad y fuerza militar:** ejecutan órdenes legales dentro de competencia; la mera existencia conceptual de un cuerpo no equivale a una patrulla activa.

Estos nombres describen **roles**, no oficinas construidas, funcionarios nombrados, NPC, escalafones nuevos ni plazas presupuestadas.

## Registro mínimo propuesto para futura implementación
Cada acto necesitará `actId`, `worldStateEventId`, `localityId`, `jurisdictionOwner`, `issuerActorId`, `issuerAuthorityProof`, `competenceKind`, `legalBasisId`, `subjectIds`, fecha de mundo, evidencia, versión, estado, resolución, notificación y trazabilidad de revisión. La existencia del acta administrativa **no modifica por sí misma** propiedad, inventario, pago, permisos, arrestos o unidades: hace falta transacción validada del World State. Evitar doble cobro o doble sanción por reintentos; `worldStateEventId` es clave de idempotencia.

**Separación obligatoria:** identidad civil ≠ hogar ≠ residencia ≠ inmueble ≠ tenencia ≠ puesto ≠ empleador ≠ propietario. Respetar mayoría de edad 18 y documentación de tutelas, adopciones, contratos y bienes de menores en Norgard. Las inspecciones de servicios de E08 no pueden asumir que existe un proveedor; primero verificar instancia y habilitación.

## Protocolo regio E4
La residencia principal Edranor debe reservar **asiento regio** y **Aposentos Regios**, preparados y custodiados, para el monarca. Durante audiencia oficial el asiento real predomina y el anfitrión se sitúa normalmente a la derecha. No fijar planta, nombre de palacio, dotación de escoltas ni fecha de visita. Un incumplimiento deliberado puede crear tensión narrativa en E10, no es automáticamente delito penal.

## Control de calidad
Jurisdicción independiente de ubicación visual; firma y cadena de competencias; fuente legal y procedencia de evidencia; auditoría y reversibilidad por resolución; consentimiento y debido proceso. Si no existe soporte legal, `NO_AUTHORITY`; si falta acto, `NOT_MATERIALIZED`. Ninguno autoriza fabricar sustitutos.
