# D.P19 — Auditoría editorial y plan de rescate de Darovan

**Fecha:** 11/11/2026  
**Naturaleza:** auditoría de calidad creativa y planificación; **no genera canon nuevo ni runtime**.  
**Estado de partida:** D00–D12 y D.P13 ya en `main`; D.P14–D.P18 desarrolladas en la **PR Draft #41**, abierta y **sin fusionar** al revisar.  
**PR de referencia:** https://github.com/robdor80/Videojuego_Nimroel/pull/41  
**Decisión de dirección:** regresar a una metodología **fase por fase, conversación por conversación, evaluación cualitativa antes de cerrar**, empezando por la identidad y la vida del mundo, no por aumentar validadores.

## 1. Dictamen ejecutivo

**No se recomienda fusionar aún la PR #41 en bloque.** Es un paquete técnicamente ordenado, pero el grado de profundidad creativa que aporta es insuficiente para cerrar la evolución territorial de Darovan.

La distinción esencial es:

- **Qué conserva valor:** restricciones canónicas; criterios físicos y legales de habitabilidad; razonamiento de abastecimiento y servicios; índice de responsabilidades compartidas con Core/Norgard; inventario de lagunas reales; precauciones cartográficas; pruebas estáticas contra contradicciones.
- **Qué no alcanza la calidad exigida:** cuatro «planes funcionales de ciudad» que reproducen casi literalmente la misma matriz de doce apartados sin desarrollar barrios, lugares, personajes, conflictos, historia, cultura material, usos cotidianos ni recorridos narrativos concretos.
- **Qué era una mala medida de éxito:** inferir madurez creativa de 26 archivos, 70 mutaciones negativas, 99 capítulos indexados o 24 escenarios `TEST_ONLY`. Esas cantidades miden cobertura documental o técnica, **no contenido construido**.

**No se ha detectado aquí una licencia para invalidar el canon existente**: los errores principales son de **suficiencia, enfoque y presentación de cierre**, no una afirmación verificada de que todos los datos nuevos contradigan D00–D13.

## 2. Referencias efectivamente contrastadas

En la rama D.P14–D.P18/PR #41:

- `D.P14/01_habitabilidad_y_diez_puertas.md`.
- `D.P15/01_coherencia_regional_servicios_y_asentamientos.md` y `02_cobertura_causal_y_limitaciones.md`.
- `D.P16/01_auditoria_funcional_99_capas_treskal_y_cuatro_ciudades.md`.
- `D.P16/02_99_capas_triado_y_13_cadenas_darovan.md`.
- Cuatro fichas `D.P16/ciudad_*_plan_funcional_condicionado.md`.
- `D.P17/01_interfaces_causalidad_persistencia_y_24_escenarios.md`.
- `D.P18/01_auditoria_comparada_y_deuda_real.md` y `02_precondiciones_cartograficas.md`.

En `main`:

- `Ciudades/Treihord/ANCLAS_CANONICAS_TREIHORD_v0.1.md`.
- `Ciudades/Veldora/D07_PERFIL_URBANO_OPERATIVO_v0.1.md`.
- `Ciudades/Taramin/D07_PERFIL_URBANO_OPERATIVO_v0.1.md`.
- `Ciudades/Syvaris/D07_PERFIL_URBANO_OPERATIVO_v0.1.md`.
- `Cultura_y_sociedad/D10_PERFILES_LOCALES_v0.1.md`.
- Histórico de decisiones autorales en `00_Control_del_proyecto/REGISTRO_FASES.md`.

Esta auditoría **no pretende certificar una lectura línea a línea de los 190 archivos markdown/JSON de Darovan**, ni inspección íntegra de los 99 capítulos de Treskal, ni pruebas de runtime. Se limita al material identificado y contrastado.

## 3. Clasificación de recuperación

| Área de la PR #41 | Dictamen | Acción |
| --- | --- | --- |
| D.P14 — diez filtros de habitabilidad y 12 ámbitos | **CONSERVAR COMO REFERENCIA** | Mantener como reglas condicionantes; no equivale a emplazamientos materializados. Evitar que diez puertas binarias sustituyan la descripción rica de cada comarca. |
| D.P15 — nueve modelos D06 y red de necesidades | **CONSERVAR COMO REFERENCIA** | Útil para que asentamientos y servicios tengan causas; no volver a reescribir un generador D06 ni suponer infraestructuras inexistentes. |
| D.P16 — índice de capítulos de Treskal y separación local/Core | **CONSERVAR COMO HERRAMIENTA** | Sirve de lista de comprobación; no demuestra igual nivel urbano ni autoriza a copiar la personalidad de Treskal. |
| D.P16 — las cuatro fichas `ciudad_*` | **REHACER EN FASES CREATIVAS** | Sustituir las matrices repetidas por estudios urbanos distintos, propuestas concretas, historia, sociedad, lugares y habitantes; confrontar D07/D08/D09/D10. |
| D.P17 — 24 escenarios e interfaz CoreRPG | **APARCAR COMO CONTRATO TÉCNICO** | Conservar ideas de autoridad, visibilidad y persistencia, pero no dedicar más tiempo creativo a multiplicar escenarios de laboratorio. Sin implementación runtime. |
| D.P18 — doce lagunas G01–G12 | **CONSERVAR Y REORDENAR** | Convertirlas en pendientes accionables por ciudad y por fuente de decisión. Retirar cualquier sugerencia de «cierre territorial completo». |
| D.P18 — precondiciones cartográficas | **CONSERVAR COMO PRECAUCIÓN** | No deducir coordenadas, cauces, rutas ni precisión métrica del mapa ilustrado o de rangos altitudinales. |
| JSON, validador y workflow de la PR #41 | **PRESERVAR COMO EVIDENCIA, NO COMO APROBACIÓN EDITORIAL** | Mantener la PR Draft intacta durante la recuperación; futuras pruebas deberán seguir al contenido aprobado, no dirigirlo. |

**No se propone borrar material sin copia o trazabilidad.** La PR #41 conserva el paquete experimental íntegro. Las futuras fases escribirán propuestas y canon aprobado en nuevas ramas; la decisión de cerrar, dividir o archivar #41 se reservará a una revisión posterior.

## 4. Evidencia concreta de insuficiencia

Las cuatro fichas D.P16 presentan prácticamente la **misma matriz de doce campos**: topología, hogares, mercancías, servicios, empleo, ley, fiscalidad, seguridad, cuidados, relaciones, mantenimiento y WorldState. Son preocupaciones legítimas, pero su repetición produce cuatro documentos que hablan sobre **qué faltaría estudiar**, y casi ninguno que permita imaginar de verdad estar en esas ciudades.

Ejemplos del vacío editorial:

- **Veldora**: sabemos que es puerto principal del reino, con gremios, aduana exterior y actividad comercial orgánica. Todavía falta un diseño urbano significativo, circulación cotidiana, lugares emblemáticos, personajes, identidad mercantil específica y conflictos propios.
- **Taramin**: sabemos que está entre los dos brazos terminales del Thalen y que concentra su actividad pesquera en una zona principal. Faltan la organización del trabajo, ambientes propios, barrios/sectores propuestos, relaciones familiares y sociales y vida reconocible.
- **Syvaris**: sabemos que la bahía protegida concentra actividad urbana y presencia de la Armada **real de Norgard**. Falta la ciudad vivida: barrios/sectores, arquitectura adaptada al clima, población local, vínculos civiles/navales, personajes e historia.
- **Treihord**: tiene una base canónica sólida (ocho barrios, cuatro plazas y cuatro puertas, Crisol, Bóveda del Grifo, La Vena, Belara) que no debe ser reemplazada. Faltan escenas, habitantes y densidad social particularizados sin alterar ese trazado ni adjudicarle nuevas instituciones a la ligera.

**Conclusión:** D.P14/D.P15 son principalmente marcos reutilizables; D.P16 no representa la profundización creativa comprometida; D.P17 pertenece a integración futura; D.P18 contiene un diagnóstico valioso pero no resuelve por sí mismo las lagunas.

## 5. Método de producción desde D.P20

Una fase/conversación/rama, con **un objetivo creativo delimitado**. El orden de trabajo para una ciudad será:

1. **Recuperar fuentes y límites.** Qué está aprobado, qué es referencia visual, qué es desconocido y qué sería contradicción.
2. **Proponer identidad concreta.** Trazado conceptual y sectores posibles, materiales, sonoridad, olores, espacios, usos, ritmos, tensiones y particularidades. **Propuesta no es canon**.
3. **Construir contenido.** Lugares relevantes, tejido residencial y comercial, vida pública, instituciones realmente aprobadas, abastecimiento, celebraciones si se aprueban, personajes nominados con relaciones y motivaciones, escenas y oportunidades narrativas.
4. **Debatir decisiones autorales en lotes pequeños.** Presentar alternativas que puedan compararse; registrar aprobación, rechazo o reserva. No introducir automáticamente nombres, barrios, puentes, puertos o episodios históricos como hechos.
5. **Auditar cruces.** D07/D08/D09/D10, geografía/hidrología, legislación real, contexto de Casa Darovan y sistemas Core/Norgard compartidos.
6. **Guardar únicamente el resultado clasificado.** `CANON_APROBADO`, `PROPUESTA_PENDIENTE` o `UNKNOWN`; ninguna de las tres categorías se disfraza de otra. Pruebas cuando aporten fiabilidad, no como producto principal.

Una ficha de ciudad debe permitir contestar, con contenido específico y no plantillas: «¿qué veo y oigo al entrar?», «¿por dónde vive y trabaja la gente?», «¿a quién conozco y qué quiere?», «¿qué me ocurriría en una semana de juego?», «¿qué hace esta ciudad diferente de las otras tres?».

**El autor aprueba el nuevo canon.** El asistente puede y debe proponer con imaginación; la ausencia de aprobación **no debe paralizar la propuesta** ni convertirse en cincuenta líneas de `UNKNOWN`.

## 6. Secuencia de fases propuesta

| Fase | Producto editorial principal |
| --- | --- |
| **D.P19 (esta fase)** | Auditoría, conservación selectiva y plan de reconstrucción de lo insuficiente. |
| **D.P20** | Veldora: desarrollo profundo de ciudad mercante, sus espacios, residentes, cultura y tramas. |
| **D.P21** | Taramin: desarrollo profundo de ciudad pesquera e interfluvio. |
| **D.P22** | Syvaris: desarrollo profundo de ciudad insular y bahía. |
| **D.P23** | Treihord: enriquecimiento sobre ocho barrios y demás canon existente, sin rediseñarla. |
| **D.P24** | Asentamientos rurales y red de vida territorial, dentro de D06 y límites físicos. |
| **D.P25** | Personajes y relaciones relevantes a escala de Casa, tramas cruzadas y continuidad. |
| **D.P26** | Auditoría integral de contenido territorial y preparación de integración técnica posterior. |

La numeración representa **orden editorial**, no un plazo ni obligación de clausurar un ámbito en una sola fase. Si una ciudad exige ampliaciones, crear subfases explícitas (por ejemplo D.P20.1/D.P20.2) antes de declararla terminada.

## 7. Anclas especialmente protegidas

- **Cuatro ciudades canónicas manuales:** Treihord, Veldora, Taramin, Syvaris. No reemplazo procedural ni quinta ciudad.
- **Treihord:** ~32.000 habitantes, ocho barrios, cuatro plazas y cuatro puertas; Belara **junto** a la ciudad, no cruzándola; barcazas industriales de poco calado; El Crisol **no acuña**; La Vena restringida.
- **Veldora:** 29.000–35.000 habitantes; puerto comercial principal; aduana exterior de la Corona; sectores comerciales distribuidos orgánicamente; río Veldora y Lhera independientes.
- **Taramin:** 14.000–20.000 habitantes; los dos brazos terminales corresponden al **mismo río Thalen**; una zona pesquera principal aprobada **solo como concepto**.
- **Syvaris:** 7.000–10.000 habitantes en la ciudad; bahía principal resguardada; Armada **real de Norgard**, no una fuerza naval Darovan; entorno con gradientes secos/verdes.
- **Arven:** pertenece a Casa Darovan; Bosque del Manto Verde ~90%; no crear puertos/rutas o aldeas por defecto.
- **Normativa y estado:** no aduanas entre Grandes Casas; no duplicar mecanismos globales Core/Norgard; IA narrativa sin autoridad para inventar mutaciones de WorldState.
- **Geometría:** no presentar mapa ilustrado o propuestas conceptuales como cartografía métrica.

## 8. Condición de cierre D.P19

D.P19 se considera **auditoría editorial iniciada y documentada**, **no cierre de D.P14–D.P18 ni aprobación de sus contenidos**. Falta la decisión del autor sobre la estrategia final de la PR #41 (mantenerla experimental, dividirla o cerrarla sin fusionar) y el comienzo de D.P20 con propuestas de contenido originales.

**No fusionar D.P19 ni #41 de forma automática. No modificar `main`.**
