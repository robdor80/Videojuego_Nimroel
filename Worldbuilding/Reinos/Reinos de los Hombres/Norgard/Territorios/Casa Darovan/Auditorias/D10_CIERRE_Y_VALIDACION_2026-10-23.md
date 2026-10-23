# D10 — Acta de cierre documental y validación

**Fecha:** 23/10/2026. **Proyecto:** Nimroel RPG / Casa Darovan. **Estado:** DOCUMENTACIÓN PREPARADA Y VALIDADA EN PR DRAFT; **NO FUSIONADA** y **NO RUNTIME**.

## Fusión previa verificada
D09 PR #35 fusionada en `main` `26a2ed5d43b6bd794bad8954b28994742d52ac97`, Actions #39775254865 SUCCESS Windows/Linux. Rama D10 iniciada expresamente desde ese commit, `feat/darovan-d10-cultura-sociedad`.

## Autoría respetada
Respuesta expresa del autor «Apruebo todas tus recomendaciones» del 23/10/2026. Diecisiete decisiones: 01–08 B, 09 C (Arven UNKNOWN), 10–17 B. No se inventan castas, privilegios jurídicos, personalidad automática, fiestas nuevas, religiones, monumentos, rutas, topónimos, habitantes o actos del World State.

## Entregables
1. Cinco documentos culturales (identidad, perfiles locales, vida cotidiana, relaciones, matriz).
2. Acta de autoría y esta acta de cierre, registro de fases y decisiones.
3. Índice JSON con 17 decisiones, seis perfiles (cuatro ciudades, Arven desconocida y rural condicionado), **34 rutas de fuentes presentes** verificadas contra árbol GitHub.
4. JSON Schema Draft 2020-12 y **16** escenarios ficticios TEST_ONLY.
5. Validador Python `validate_d10.py` con **98 mutaciones negativas rechazadas**, comprobaciones de D07–D09 y fuentes canónicas.
6. Workflow GitHub Actions D01–D10 en Windows 2022 y Ubuntu 24.04.
7. `TRASPASO_D11.md` meramente preparatorio, D11 no iniciada.

## Validación real
Primera ejecución de la PR #36 #39951068905: **FAILED**, por un control del nuevo validador D10 que exigía que el objeto `populationRange` de D08 solo tuviera dos campos cuando su JSON real incluye metadatos canónicos. No era una contradicción D08. Reparación limitada a comparar `minInclusive`, `maxInclusive` y `status` manteniendo exactamente los valores aprobados.

Segunda ejecución [#39951196364](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39951196364), commit `878a1a932e56b2815478d0151233d2793156cea0`: **SUCCESS**, tanto Windows Server 2022 como Ubuntu 24.04. Se ejecutaron D01–D10 completos; D10 mostró «17 author decisions | 6 locality profiles | 16 TEST_ONLY cases | 98 negative mutations rejected». La presente acta constituye un commit administrativo posterior, por lo que es obligatoria la comprobación de CI de su HEAD final antes de cualquier recomendación de fusión.

## Verificación de ámbito
GitHub compare contra el SHA base constató que no se editaron documentos/códigos de fases D00–D09. Únicamente nuevos entregables D10, registro administrativo, README de sección/validación y workflow. No se modifican CoreRPG, Godot, GDExtension ni se declara API runtime.

## Reservas intactas
Origen preciso de rivalidad Galdren, nombre/fecha de feria metálica, identidad y costumbres Arven, cargos y personajes históricos, información métrica y rutas, nuevos ritos, ubicaciones y World State siguen sin definirse.

**Prohibiciones de cierre:** NO FUSIONAR automáticamente PR #36. No iniciar D11 ni D12. La autorización de fusionar corresponde al autor.
