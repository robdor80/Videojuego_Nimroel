# E14 — Matriz de decisiones de uso de suelo
## Seis clases, no seis tipos de propiedad
| Clase | Sentido | Condiciones orientativas; la lista formal está en JSON |
|---|---|---|
| PERMANENT_RESIDENCE | residencia habitual | agua potable perenne, saneamiento, vía anual real, vivienda, sustento, clima y suelo estable |
| SEASONAL_WORKSTATION | estación de trabajo temporal | agua y saneamiento estacionales, refugio, acceso, riesgo laboral y permisos |
| AGRICULTURAL_USE | uso agrícola | parcela legal, suelo productivo verificado, agua disponible para uso, ventana climática, derecho de cultivo y riesgo |
| FOREST_USE | gestión forestal | titularidad, permiso forestal expreso, compatibilidad con protección, regeneración y acceso |
| TEMPORARY_PASSAGE | paso temporal | derechos de paso, estabilidad, acceso real probado, riesgos y topología levantada |
| EXCLUDED | ocupación excluida | pertenencia no probada, protección incompatible, prohibición de uso o amenaza insalvable |

## Algoritmo de clasificación propuesto
1. **Bloqueo espacial/legal**: norte sin cierre o Hallheim → NON_EVALUABLE / OUTSIDE_SCOPE. Rodas solo admite autoridad Aethros; no se proponen exacciones ni guarniciones de Edranor. Núcleo protegido → no generar aldeas procedurales.
2. **Exclusión**: `CROWN_LAND` fuera de competencia, `PROTECTED_HABITAT` incompatible, `SLOPE_UNSTABLE` o `ACTIVE_UNMITIGATED_HAZARD` → INELIGIBLE; sin pretender que estos hechos estén comprobados localmente hoy.
3. **Faltan verificaciones**: basta un campo obligatorio UNKNOWN para `PENDING_EVIDENCE`; jamás se da por positivo por defecto.
4. **Denegación real**: título o permiso denegado → `INELIGIBLE`.
5. **Prueba completa**: solo un expediente con cada requisito verificado y sin exclusiones puede resultar `ELIGIBLE_IF_VERIFIED`; hoy esto existe **únicamente en fixture sintético**, no en parcela de Edranor.
6. **Revalidación**: estado del mundo, estación, amenazas, tenencia, cubierta y capacidad obligan a reevaluar; la selección no equivale a spawn.

La **viabilidad** no es aditiva: ningún promedio de pendiente, suelo y proximidad sustituye al agua potable, derechos o acceso. Los riesgos deben combinar desencadenante, susceptibilidad, exposición y vulnerabilidad; `riesgo condicional` no es desastre materializado. En la meseta forestal, un buen claro no autoriza tala por deducción; en la transición norte, la proximidad a los vinos regionales no permite viticultura boreal.
## Invariantes de integración
El motor CoreRPG sigue siendo dueño de economía, hogar, trabajo, permisos, justicia, memoria y riesgos. E14 solo define un **contrato documental no-runtime** y una función pura sintética de decisión. E15–E17 consumen necesidades, no instancias; E19 aporta geometría; E26 aporta censo verificable; E28 podrá conectar los contratos tras pruebas reales.
