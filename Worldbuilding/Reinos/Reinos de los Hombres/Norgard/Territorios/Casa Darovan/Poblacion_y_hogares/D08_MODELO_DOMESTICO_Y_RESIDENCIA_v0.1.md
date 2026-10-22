# D08 — Hogares, residencia, población y vínculos v0.1
**Estado:** diseño operativo documental `DERIVED/PROPOSAL_PENDING_AUTHOR`, SIN nuevos habitantes o categorías sociales canonizadas.

## Individuos y grupos
El concepto de hogar modela una unidad de convivencia y cooperación doméstica; no es sinónimo de familia, matrimonio, propiedad ni empresa. Puede existir una persona viviendo sola, familiares residentes juntos, residentes sin parentesco y familiares que viven separados. Son **patrones técnicos posibles**, no porcentajes ni clases sociales autorizadas. No imponer familia nuclear como plantilla universal ni una figura de autoridad doméstica por defecto.

Una persona puede mantener identidad, vínculos y oficio tras mudanza o disolución doméstica. El `RES` canónico exige cambio válido del World State; visitante prolongado no adquiere automáticamente residencia y viaje temporal no la extingue. `MOVE` exige origen/destino, causa, tiempo, medios y estado; el taller no se muda automáticamente con el titular.

`KIN` diferencia hechos, filiación jurídica, conocimiento y disputas. Un hogar compartido no crea relación biológica o filiación; el matrimonio solo nace de acto válido, nunca por convivencia. `CARE/DEP` requiere necesidad y cuidador real con tiempo; nadie es cuidador automático por vecindad, parentesco o edad. `CHORE/DOM` consume tiempo, agua, combustible, materiales y capacidad real. Distribución de tareas por disponibilidad/competencia, nunca asignación rígida por sexo.

## Edad y capacidad de Norgard
- 0–7: cuidados, sin empleo ni aprendizaje formal.
- 8–11: ayuda ligera guiada, sin contrato laboral ni sustitución de trabajador.
- 12–14: aprendizaje formal con tutor/mentor, consentimiento/asentimiento y supervisión; no equivale a plaza plena de empleo.
- 15–17: empleo juvenil limitado, con consentimiento, protección frente al riesgo y autorizaciones cuando proceda.
- 18+: capacidad civil general, sin que la edad por sí sola acredite competencia o salud.

Toda norma específica remite a las fuentes superiores de Norgard; D08 no redefine edades, matrimonio, tutela, herencia, ocupación o pagos.

## Distribución
Treihord mantiene su cifra aproximada canónica de **32.000**. Por resolución autoral **DAR-D08-01 (22/10/2026)**, Veldora cuenta con **intervalo aprobado de 29.000–35.000 habitantes (opción B)**, pero el número exacto continúa **UNKNOWN**. Número de hogares, edades, densidades, relaciones urbano-rural, cifras de Taramin/Syvaris y población del territorio completo: **UNKNOWN**. El intervalo no determina automáticamente profesiones ni infraestructura. Se puede mantener una reserva de población abstracta a nivel de diseño, pero `CoreRPG PopulationRecord` precisa un grupo real en WorldState y una cifra concreta; no se invoca con población supuesta. La población latente no son NPC personalizados. Ningún número de fixtures es canon ni un límite demográfico de D06.

## Dependencias causales del mundo persistente
`Necesidad → recursos/tiempo/acceso disponibles → proveedor real → capacidad y espera → transacción/autorización → mutación por CoreRPG`. Si falta un elemento, el resultado puede ser necesidad insatisfecha, espera o incapacidad. Prohibida creación espontánea de stocks, viajes, personas, permisos o viviendas. La simulación fuera de pantalla deberá aplicar las mismas restricciones cuando exista motor implementado.

## Interfaces diferidas
D11 decidirá IDs estables, relaciones numéricas `RelationKind`, adaptadores de políticas `RES/KIN/EMP/CARE`, orden de mutación, guardado y tests runtime. El JSON D08 es exclusivamente un índice operativo de requisitos con vacíos declarados, no un pack ejecutable.
