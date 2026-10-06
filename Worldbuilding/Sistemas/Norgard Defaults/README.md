# Norgard Defaults

## Estado

**CAPA DE DEFAULTS DEL REINO — E1–E4 ACTIVOS**

## Objetivo

Esta capa contiene únicamente reglas, costumbres, instituciones y valores por defecto que el canon establece como compartidos por **todo Norgard**.

Jerarquía:

**Nimroel Core → Norgard Defaults → Casa/Territorio → Localidad → World State**

## Regla de autoridad

Un default de Norgard sólo puede crearse cuando exista fuente canónica suficiente a nivel Reino.

No se promueve a Norgard por analogía:

- una costumbre de Treskal;
- una costumbre de Casa Valrik;
- una dirección de diseño aún pendiente;
- una solución rural con scope mixto;
- un detalle tecnológico local.

Cuando un documento de Norgard esté marcado como pendiente, revisión o dirección no canonizada, se registra como dependencia y no como default activo.

## Estado inicial de auditoría

Listos para extracción inmediata:

- tradición funeraria común: cremación en pira y retorno de restos al territorio;
- luto formal de tres jornadas, separado del duelo personal;
- monopolio de la Corona sobre la acuñación oficial;
- convención toponímica general de Norgard.

No listos todavía:

- sistema militar final;
- derecho familiar, matrimonio, tutela y adopción;
- mayoría de edad y derecho laboral;
- propiedad, herencia y alquiler;
- sistema monetario completo, precios y fiscalidad;
- marco naval y terminología naval;
- tradición sanitaria de reino;
- gastronomía general del reino;
- nombres personales y apellidos;
- calendario oficial detallado;
- cultura material común suficientemente cerrada.

Casa Valrik, no Norgard:

- peso cultural especial de la palabra dada/honor cuando la fuente sólo lo fija para Valrik.

## Principio final

**Norgard Defaults no rellena huecos: hereda canon demostrado y deja lo demás pendiente.**


## Defaults activos

### E1 — funeral y luto

Activo a nivel Reino:

- cremación en pira;
- retorno territorial de los restos;
- luto formal de tres jornadas;
- duelo personal sin duración fija;
- ausencia de color, vestimenta o rito religioso universal.

Contrato operativo:

`Datos operativos/norgard_funeral_mourning_default_v0.1.json`

### E2 — autoridad monetaria

Activo parcialmente a nivel Reino:

- monopolio exclusivo de la Corona sobre la acuñación oficial;
- metal precioso no implica derecho de acuñar;
- falsificación y acuñación ilícita son delitos graves;
- sistema monetario completo permanece pendiente.

Contrato operativo:

`Datos operativos/norgard_crown_minting_authority_default_v0.1.json`

### E3 — convención toponímica

Activo a nivel Reino:

- sistema mixto de nombres propios, históricos, descriptivos y populares;
- nombres antiguos solo con base real;
- prohibición de pseudo-nórdico decorativo;
- separación nombre visible / ID técnico.

Contrato operativo:

`Datos operativos/norgard_toponymic_convention_default_v0.1.json`

### E4 — protocolo regio en residencias de Grandes Casas no reinantes

Activo a nivel Reino para Darovan, Edranor, Galdren y Valrik:

- asiento regio de recepción reservado al monarca;
- posición de máximo prestigio durante visita oficial;
- Aposentos Regios permanentes, preparados y bajo custodia;
- uso exclusivo del monarca durante visitas oficiales;
- la solución arquitectónica concreta pertenece a cada Casa.

Contrato operativo:

`Datos operativos/norgard_royal_reception_residence_default_v0.1.json`

**Todos los candidatos de Norgard actualmente respaldados por canon suficiente están extraídos.**

Pendiente siguiente capa:

- Casa Valrik — peso especial de la palabra dada/honor.

El resto continúa bloqueado hasta que exista canon suficiente.


## Validación de cierre

E1, E2, E3 y E4 han superado la regresión estática de contratos del cierre Treskal/Core.

Estado:

**NORGARD_DEFAULTS_STATICALLY_VALIDATED**

Los elementos de `blockedPendingCanon` permanecen deliberadamente sin definir hasta que exista canon suficiente.
