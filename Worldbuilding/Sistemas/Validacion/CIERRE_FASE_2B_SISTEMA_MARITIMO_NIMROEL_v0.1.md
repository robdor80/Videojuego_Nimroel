# CIERRE FASE 2B — Sistema marítimo procedural de Nimroel v0.1

## Estado

**CERRADO Y VALIDADO ESTÁTICAMENTE**

Marcador global:

`MARITIME_POINT_2B_CLOSED_CORE_NORGARD_TRESKAL`

## 1. Arquitectura

**Nimroel Core → Norgard Defaults → perfiles institucionales/civiles → Treskal → World State**

No existe autoridad duplicada.

## 2. Core

Contratos activos:

- embarcaciones, navegación, tripulación, carga, puertos y LOD;
- encuentros, persecución, combate, abordaje, captura y rescate;
- caladeros, recursos acuáticos, captura, presión y recuperación.

Namespaces añadidos:

`VSL VOY CREW BERTH WENC WCOM BOARD RESC AQR FGR HARV`

## 3. Norgard civil

- 7 arquetipos funcionales civiles;
- flotillas generadas por necesidad/capacidad, no por cifra decorativa;
- materialización persistente;
- pesca fluvial, estuarina, costera y de altura soportada;
- comercio marítimo y fluvial soportado;
- especies concretas no se inventan sin ecología.

## 4. Armada

Se conserva el canon E6:

- 8 clases;
- 25 grandes navíos nominales únicos;
- Lobo de Plata único.

E7 añade:

- registro finito I–III al inicializar mundo;
- prohibición de spawn ilimitado;
- misiones y selección de fuerza;
- convoy, escolta, transporte, patrulla, intercepción, bloqueo, desembarco y rescate;
- combate y consecuencias off-screen;
- pérdida, captura, daño y reparación persistentes;
- prohibición de inventar nuevas clases.

## 5. Treskal

- T07 = puerto civil/pesquero;
- S07 = desembarco prioritario de pescado;
- T08 = Complejo Naval Real, separado;
- flotilla pesquera procedural-persistente;
- 4 ámbitos funcionales de caladero;
- cadena caladero → captura → barco → S07 → mercado/conservación;
- clima, tripulación, mantenimiento y presión del recurso afectan actividad;
- 12 escenarios de integración definidos.

## 6. Validación automática/estática realizada

Resultado comprobado:

- Core manifest v0.3;
- Norgard manifest v0.9;
- Treskal manifest v0.8;
- 3 contratos Core marítimos presentes;
- 11 namespaces Core marítimos presentes;
- 7 arquetipos civiles;
- 8 clases militares;
- 25 nombres militares / 25 únicos;
- Lobo de Plata único;
- spawn militar desde la nada prohibido;
- pesos iniciales de flotilla Treskal = 1.00;
- 4 caladeros funcionales;
- número fijo de pesqueros = false;
- especies inventadas = false;
- T07 civil;
- T08 Corona;
- 12 escenarios de integración;
- 8 archivos operativos principales comprobados: 0 ausentes.

## 7. Pendientes legítimos que no reabren 2B

- implementación runtime en el futuro motor;
- especies cuando se desarrolle ecología;
- clima numérico final;
- geometría métrica de rutas/muelles;
- títulos navales especializados;
- cifras canónicas I–III si se desean fijar manualmente.

El siguiente sistema, Aduanas/Fiscalidad, dispone ya de hooks en llegada, manifiesto, carga, almacenamiento y salida.

## Resultado final

**La capa marítima ya no es sólo worldbuilding descriptivo: queda especificada como sistema procedural persistente listo para implementación futura.**

**PUNTO 2A — ARMADA / ASTILLEROS: CERRADO.**

**PUNTO 2B — NAVEGACIÓN / PESCA / SIMULACIÓN MARÍTIMA: CERRADO.**

**SIGUIENTE: PUNTO 3 — ADUANAS / FISCALIDAD.**
