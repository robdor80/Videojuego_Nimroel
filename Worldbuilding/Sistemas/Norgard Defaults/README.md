# Norgard Defaults

## Estado

**CAPA DE DEFAULTS DEL REINO — E1–E10 ACTIVOS**

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

### E2 — sistema monetario y acuñación

Activo a nivel Reino — **Punto 5 cerrado**:

- monopolio exclusivo de la Corona sobre la acuñación oficial;
- **Clavo, Luna y Corona** como únicas denominaciones oficiales;
- 1 Luna = 24 Clavos;
- 1 Corona = 20 Lunas = 480 Clavos;
- pesos y ley monetaria cerrados;
- Ceca Real única y permanente en Hallheim;
- dependencia administrativa del Tesoro de la Corona;
- El Crisol como Casa de Ensaye Darovan, nunca como ceca;
- lingotes, metal privado y tasa de acuñación del 2,5 %;
- moneda extranjera sin curso legal obligatorio;
- multas F1–F5 monetizadas;
- balance base de precios y salarios.

Contratos operativos:

`Datos operativos/norgard_crown_minting_authority_default_v0.1.json`

`Datos operativos/norgard_currency_economic_balance_default_v0.1.json`

Balance humano:

`02_Gobierno_y_economia/balance_monetario_precios_salarios_v0.1.md`

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

E1, E2, E3, E4, E5, E6, E7, E8 y E9 han superado la regresión estática de contratos del cierre Treskal/Core.

Estado:

**NORGARD_DEFAULTS_STATICALLY_VALIDATED**

Los elementos de `blockedPendingCanon` permanecen deliberadamente sin definir hasta que exista canon suficiente.


### E5 — sistema militar de Norgard

Activo a nivel Reino:

- autoridad militar suprema de la Corona;
- fuerzas directas de la Corona;
- Guardia de Casa, seguridad territorial, fuerza profesional y reserva para las Grandes Casas;
- capacidad defensiva territorial sin soberanía militar;
- convocatoria real obligatoria;
- Casas menores con fuerzas limitadas subordinadas;
- Armada Real exclusiva de la Corona;
- separación entre Guardia urbana y ejército territorial.

Contrato operativo:

`Datos operativos/norgard_military_authority_house_forces_default_v0.1.json`

El antiguo bloqueo `military_and_guard_final_framework` queda resuelto.


### E6 — Armada Real de Norgard

Activo a nivel Reino:

- la Armada Real pertenece exclusivamente a la Corona de Norgard / Casa Regente Aethros;
- navegación militar a vela, sin pólvora, cañones, bombardas ni armas de fuego;
- combate mediante arquería, ballestas, escorpiones, balistas, maniobra, daño a aparejo/timón y abordaje;
- doctrina centrada en transporte de tropas, escolta, protección de convoyes, logística e intercepción;
- clasificación técnica en Categorías I–V y ocho clases;
- Categorías I–III sin nombre propio individual obligatorio; identificación por clase y numeral/registro;
- Categorías IV–V con nombre propio;
- 25 grandes navíos nominales cerrados entre Categorías IV y V;
- Clase Corona compuesta por la Nave Real **Lobo de Plata**;
- Astilleros Reales y Base Naval Principal materializados en T08 de Treskal bajo autoridad directa de la Corona.

Contrato operativo:

`Datos operativos/norgard_royal_navy_default_v0.1.json`

Desarrollo canónico:

`06_Armada_real/armada_real_norgard_v0.1.md`

El antiguo bloqueo `royal_naval_framework` queda resuelto. La terminología marítima general no necesaria para este marco puede seguir ampliándose sin reabrir E6.


### E7 — navegación civil, pesca y operación marítima

Activo a nivel Reino:

- arquetipos funcionales civiles/fluviales/pesqueros/mercantes;
- generación finita y persistente de flotillas civiles;
- caladeros persistentes, presión de pesca y recuperación;
- viajes pesqueros y comerciales;
- integración con puertos, clima, empleo, carga y mantenimiento;
- registro finito de Armada I–III al inicializar mundo;
- operaciones de patrulla, convoy, escolta, transporte, intercepción, bloqueo, desembarco y rescate;
- resolución off-screen con las mismas consecuencias persistentes.

Contratos:

`Datos operativos/norgard_civil_maritime_fishing_default_v0.1.json`

`Datos operativos/norgard_royal_navy_operations_default_v0.1.json`

El sistema fiscal/aduanero se conecta en Punto 3 y no bloquea el cierre marítimo.


### E8 — sistema fiscal y aduanero

Activo a nivel Reino:

- autoridad fiscal superior de la Corona;
- administración y recaudación territorial por Grandes Casas;
- remesa de la parte estipulada a la Corona;
- ausencia de aduanas internas entre las cinco Grandes Casas;
- contribución territorial;
- tasas de mercado/servicio;
- tasas portuarias;
- aduana sobre frontera fiscal exterior;
- leva extraordinaria solo por orden real;
- registros, recibos, deuda, auditoría y fraude causal.

Contrato:

`Datos operativos/norgard_fiscal_customs_default_v0.1.json`

Canon:

`Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Gobierno y leyes/sistema_fiscal_y_aduanero_v0.1.md`

El Punto 5 ya aporta unidad monetaria, equivalencias y procedimiento de valoración. Los porcentajes o tarifas fiscales concretos siguen perteneciendo al calendario fiscal autorizado y no se inventan desde la capa monetaria.


### E9 — Justicia del Rey y sistema penal

Activo a nivel Reino: Ley penal única; Justicia del Rey administrada por Grandes Casas; procedimiento medieval directo sin abogados, fiscales profesionales ni jurado moderno; 120 tipificaciones en 22 grupos; ausencia de prisión de larga duración como condena ordinaria; destierro perpetuo con marca frontal; excepción corporal específica para delitos sexuales penetrativos consumados; responsabilidad juvenil/capacidad y resolución determinista.

Contratos: `Datos operativos/norgard_penal_code_v0.1.json` y `Datos operativos/norgard_kings_justice_procedure_v0.1.json`.

Canon: `08_Sistema_penal/SISTEMA_PENAL_Y_JUSTICIA_DEL_REY_NORGARD_v0.1.md`


### E10 — familia, matrimonio, filiación, tutela y adopción

Activo a nivel Reino — **Punto 6 cerrado**:

- mayoría matrimonial a los 18 años;
- matrimonio civil, monógamo y por consentimiento libre;
- validez independiente del sexo de los contrayentes;
- autoridad reconocida y dos testigos adultos;
- separación de hecho distinta de disolución;
- disolución y nulidad bajo Justicia del Rey;
- filiación jurídica separada del hecho biológico;
- segundo progenitor no inferido por pareja/matrimonio;
- responsabilidad parental;
- tutela;
- adopción;
- protección civil ordinaria de descendencia nacida fuera de matrimonio;
- preservación de las reglas especiales de sucesión Aethros;
- integración con AFF, KIN, CARE, RES y PREG.

Contrato operativo:

`Datos operativos/norgard_family_marriage_guardianship_default_v0.1.json`

Canon:

`Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Gobierno y leyes/familia_matrimonio_filiacion_tutela_adopcion_v0.1.md`

Regresión:

`Validacion/regresion_e10_familia_matrimonio_tutela_adopcion_v0.1.md`
