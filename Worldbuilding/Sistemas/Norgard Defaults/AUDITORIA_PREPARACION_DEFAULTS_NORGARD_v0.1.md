# Auditoría de preparación — Norgard Defaults v0.1

## Estado

**AUDITORÍA EJECUTADA — EXTRAER SÓLO CANON REALMENTE NORGARDIANO**

## Objetivo

Revisar los candidatos surgidos del prototipo de Treskal y decidir cuáles pueden convertirse en defaults de todo Norgard sin borrar diferencias entre Grandes Casas, territorios o localidades.

---

## 1. READY — canon suficiente a nivel Reino

### Funeral, cremación y retorno de cenizas

Fuentes:

- `Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Sociedad/costumbres_funerarias.md`
- `Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Sociedad/luto_y_duelo.md`

Canon confirmado:

- la cremación en pira es tradición común en todo Norgard;
- no es un rito religioso;
- el principio general es devolver los restos al territorio;
- nobleza y Corona comparten el mismo principio corporal;
- la forma concreta del retorno puede variar localmente.

Clasificación:

**READY_FOR_NORGARD_DEFAULT_EXTRACTION**

### Luto formal de tres jornadas

Las mismas fuentes establecen:

- luto formal = tres jornadas;
- duelo personal = duración no fijada;
- el luto comienza cuando la muerte es conocida, cierta y asumida por el círculo responsable;
- un retraso material de la cremación no prolonga automáticamente el luto formal;
- no existe color, vestimenta o rito religioso universal de luto.

Clasificación:

**READY_FOR_NORGARD_DEFAULT_EXTRACTION**

### Monopolio de acuñación

Fuente:

- `Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Gobierno y leyes/moneda_y_acunacion.md`

Canon confirmado:

- la acuñación de moneda oficial es monopolio exclusivo de la Corona;
- poseer oro o plata no concede derecho de acuñar;
- falsificación y acuñación ilícita son delitos graves;
- ubicación y organización de la ceca siguen sin definirse.

Clasificación:

**READY_AS_PARTIAL_ECONOMIC_DEFAULT**

No autoriza todavía a definir moneda completa, denominaciones, precios, salarios o fiscalidad.

### Convención toponímica

Fuente:

- `Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Toponimia/convencion_toponimica_norgard_v0.1.md`

Canon confirmado:

- sistema mixto de nombres propios, históricos, descriptivos y populares;
- nombres antiguos sólo con fundamento cultural/histórico real;
- no se inventa pseudo-nórdico por defecto;
- nombre visible e ID técnico son capas distintas.

Clasificación:

**READY_FOR_NORGARD_DEFAULT_EXTRACTION**

---

## 2. HOUSE/TERRITORY — no promover a todo Norgard

### Peso especial de la palabra dada

La evidencia operativa actual lo fija específicamente para **Valrik**.

Debe situarse en:

**Casa Valrik Defaults**, no en Norgard Defaults, salvo que un futuro documento de reino lo extienda expresamente.

Clasificación:

**VALRIK_DEFAULT_CANDIDATE**

---

## 3. PENDING — canon insuficiente o no final

### Sistema militar y guardia

`revision_militar_y_casas_menores.md` declara explícitamente:

**DIRECCIÓN APROBADA — PENDIENTE DE DESARROLLO Y CANONIZACIÓN FORMAL**

No puede convertirse todavía en default normativo.

### Familia, matrimonio, tutela y adopción

No existe en la auditoría una especificación final suficiente de reino.

### Mayoría de edad y reglas laborales

Pendiente de canon legal/familiar.

### Propiedad, herencia y alquiler

Los sistemas Core ya modelan propiedad material, pero las consecuencias jurídicas siguen pendientes del derecho de Norgard.

### Economía completa

El monopolio de acuñación está definido, pero no el sistema económico completo.

### Curandería de Norgard

Treskal tiene una red sanitaria concreta, pero no se ha encontrado una autoridad de reino suficiente para universalizarla.

### Marco naval, terminología marítima, gastronomía, nombres personales/apellidos, calendario oficial y cultura material común

No existe todavía base suficiente para promoverlos como defaults generales sin añadir canon nuevo.

---

## 4. Fuente mixta que requiere cautela

`Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Sociedad/aldeas_servicios_y_economia_local.md` contiene material valioso, pero varios bloques usan scope mixto del tipo:

`Norgard/Treskal/village`

No debe copiarse entero a Norgard Defaults.

Cada futura extracción necesita separar:

- principio realmente norgardiano;
- aplicación territorial de Treskal;
- instancia local.

---

## 5. Orden de ejecución aprobado por esta auditoría

1. E1 — funeral / luto / cenizas;
2. E2 — acuñación y autoridad monetaria, sólo lo ya canonizado;
3. E3 — convención toponímica;
4. crear capa Casa Valrik cuando se aborde palabra dada/honor;
5. mantener bloqueados los demás candidatos hasta que exista canon suficiente.

---

## Regla final

**Una regla entra en Norgard Defaults porque el canon dice que pertenece a Norgard, no porque Treskal la utilice.**
