# Cierre de refactorización — Treskal / Nimroel Core / Norgard / Casa Valrik v0.1

## Estado

**TRESKAL_REFACTOR_COMPLETE_AND_STATICALLY_VALIDATED**

Validado contra el HEAD previo al cierre:

`68eccc98d72c1e787fc1c95a4a7a49f7f8086f8e`

## Alcance

Esta validación certifica la arquitectura de contratos y worldbuilding:

**Nimroel Core → Norgard Defaults → Casa/Territorio → Treskal Overrides → World State**

No pretende certificar todavía ejecución runtime de un motor que aún no consume todos estos contratos.

## Resultado cuantitativo

- 48 contratos operativos de Nimroel Core revisados: **48 activos como `active_core_contract`**.
- 57 namespaces Core revisados.
- Conjunto de namespaces del Core = conjunto del mapa de extracción = conjunto migrado por Treskal: **coincidencia exacta**.
- 48 sistemas migrados de Treskal revisados.
- Bridges locales ordinarios: `migrated_to_core_override`.
- Excepción deliberada K/reputación: `split_migration_bridge`, con K en Core y reputación todavía local.
- 19 especificaciones de regresión revisadas: 15 Core + 3 Norgard + 1 Casa Valrik.
- 119 referencias internas de contratos/manifests/regresiones comprobadas.
- Referencias rotas: **0**.
- Autoridad Core duplicada detectada: **0**.
- Descriptores de namespace antiguos corregidos en el manifest de Treskal: **11**.
- IDs de namespace modificados: **0**.

## Overrides locales confirmados

La auditoría confirma que los overrides se conservan solo cuando existe una particularidad real de Treskal, entre ellas:

- embarazo/entorno de asistencia;
- dependencia y modelo local de cuidados;
- construcción y acceso físico local;
- saneamiento/residuos;
- riesgos e incendios;
- mensajería y educación con supuestos institucionales locales;
- canales locales de conocimiento;
- práctica funeraria urbana;
- máquina PLEDGE de Treskal bajo el default cultural Valrik.

Los sistemas sin excepción local mantienen `localOverrides = {}`.

## Norgard Defaults

Validados:

- E1 — cremación, retorno territorial y luto de tres jornadas;
- E2 — monopolio real de acuñación, con alcance deliberadamente parcial;
- E3 — convención toponímica.

Los elementos sin canon suficiente permanecen en `blockedPendingCanon`. No son errores ni tareas de migración pendientes.

## Casa Valrik Defaults

Validado:

- V1 — peso cultural especial de la palabra dada/honor.

No se promueve esta regla a todo Norgard.

## Compatibilidad

El cierre no cambia IDs estables ni introduce una migración de save.

Las correcciones realizadas son de autoridad, herencia y metadata descriptiva.

## Límite de esta validación

Modo de validación:

`static_contract_regression`

Las regresiones gameplay/runtime deberán ejecutarse cuando exista una implementación de motor que materialice estos contratos. Ese trabajo pertenece a implementación técnica futura, no a la extracción/refactorización de Treskal.

## Decisión de cierre

No crear nuevas capas de Treskal por inercia.

A partir de este punto:

- nuevas reglas universales → Nimroel Core;
- canon común de Norgard → Norgard Defaults;
- canon de Casa → capa de Casa;
- particularidad urbana → Treskal u otra localidad;
- huecos de canon → permanecen explícitamente pendientes.

**Treskal deja de ser la autoridad accidental del mundo y queda consolidada como instancia local sobre una arquitectura reutilizable.**
