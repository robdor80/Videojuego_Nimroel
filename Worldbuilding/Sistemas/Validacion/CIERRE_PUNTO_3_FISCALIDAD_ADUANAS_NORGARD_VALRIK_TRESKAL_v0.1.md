# CIERRE PUNTO 3 — Fiscalidad y Aduanas de Norgard / Valrik / Treskal v0.1

## Estado

**CERRADO Y VALIDADO ESTÁTICAMENTE**

Marcador global:

`FISCAL_CUSTOMS_POINT_3_CLOSED_NORGARD_VALRIK_TRESKAL`

## Arquitectura

**Nimroel Core → Norgard E8 → Casa Valrik V3 → Treskal → World State**

## Core

- TXN — transacción real;
- OBL — obligación formal;
- LED — entrada de registro.

El registro no crea recursos y puede contener error o fraude.

## Norgard

- Corona = autoridad fiscal superior;
- Grandes Casas administran y recaudan;
- parte estipulada → Corona;
- parte autorizada → administración territorial;
- no hay aduanas entre las cinco Grandes Casas;
- contribución territorial;
- tasas de mercado/servicio;
- tasas portuarias;
- aduana exterior;
- leva extraordinaria solo por orden real;
- fraude fiscal no se detecta de forma omnisciente.

## Valrik

- no crea ley fiscal propia;
- S02 centraliza las cuentas territoriales;
- Casas menores solo recaudan por delegación;
- pago en especie posible si la obligación lo autoriza;
- T08 queda fuera de potestad tributaria Valrik.

## Treskal

- S02 = administración fiscal territorial;
- T07 = control portuario/aduanero integrado;
- no se añade Casa de Aduanas singular;
- no se añade Tesoro singular;
- pesca local no es importación;
- mercante de otra Gran Casa no paga aduana interior;
- mercante exterior puede generar caso CUS;
- servicios portuarios siguen siendo transacciones reales;
- contrabando, manifiesto falso y corrupción tienen hooks causales;
- 14 escenarios de integración.

## Cifras

Importes, porcentajes y tablas monetarias no se inventan todavía.

Quedan vinculados al futuro cierre de moneda/balance económico. Esto no reabre Punto 3 porque ya están cerrados:

- autoridad;
- bases fiscales;
- sujetos;
- exenciones;
- flujos;
- registros;
- control;
- inspección;
- remesa;
- fraude;
- integración física.

## Próximo punto

**Punto 4 — prisión / sistema penal.**
