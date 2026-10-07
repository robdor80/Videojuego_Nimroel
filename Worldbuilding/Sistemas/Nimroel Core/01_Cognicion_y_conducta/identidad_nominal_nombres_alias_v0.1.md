# Nimroel Core — identidad nominal, nombres y alias v0.1

## Autoridad

**CORE UNIVERSAL — namespace NAME**

Este sistema define cómo se registra y persiste el nombre de una persona.

No define:

- qué nombres usa cada cultura;
- cómo se transmiten apellidos;
- nombres de Grandes Casas;
- títulos;
- reglas dinásticas.

Esas materias pertenecen a la cultura o ley correspondiente.

---

## 1. Principio

El nombre visible no es la identidad técnica.

Una persona conserva el mismo `npc_id` aunque:

- cambie de nombre;
- cambie de apellido;
- adopte un alias;
- reciba un título;
- pierda un título;
- use un apodo;
- sea conocida con un nombre equivocado.

El World State referencia a la persona por ID estable.

---

## 2. Estados NAME

- NAME01 — registered_current;
- NAME02 — provisional_or_unregistered;
- NAME03 — former_legal_name;
- NAME04 — alias_or_byname;
- NAME05 — unknown_or_unresolved.

Estos estados describen registros nominales.

No sustituyen K, CRED, SELF, KIN ni títulos institucionales.

---

## 3. Registro nominal

Un registro puede contener:

- `name_record_id`;
- `npc_id`;
- `given_name`;
- `additional_given_names`;
- `family_name`;
- `display_name`;
- `NAME_state`;
- `culture_scope`;
- `source_event_ref`;
- `valid_from`;
- `valid_to_if_former`;
- `alias_type_if_any`;
- `legal_or_social`;
- `visibility`;
- `former_name_ref_if_any`;
- `notes`.

No toda cultura necesita todos los campos.

---

## 4. Nombre legal y nombre social

Debe distinguirse:

- nombre legal vigente;
- nombre anterior;
- apodo;
- sobrenombre;
- nombre profesional;
- alias deliberado;
- forma abreviada;
- título.

Un apodo no se convierte en apellido legal por repetición.

Un título no forma parte automáticamente del nombre civil.

---

## 5. Conocimiento

Que una persona posea un nombre legal no implica que todos lo conozcan.

K conserva autoridad sobre:

- quién conoce el nombre;
- qué alias conoce;
- si sabe que dos nombres corresponden a la misma persona.

CRED puede intervenir cuando una identidad es afirmada o discutida.

---

## 6. Cambio de nombre

Un cambio legal:

- crea un nuevo registro NAME01;
- convierte el nombre legal anterior en NAME03;
- conserva trazabilidad;
- no crea un nuevo NPC;
- no borra deudas, delitos, parentesco, propiedad, matrimonio, empleo ni obligaciones.

La cultura/ley define quién puede solicitarlo y qué autoridad lo registra.

---

## 7. Alias

Un alias puede existir por:

- apodo;
- oficio;
- reputación;
- ocultación;
- viaje;
- error;
- costumbre.

Puede ser persistente socialmente.

No cambia por sí solo:

- filiación;
- herencia;
- propiedad;
- ciudadanía;
- autoridad;
- identidad técnica.

---

## 8. Nacimiento

Un recién nacido puede existir temporalmente con NAME02 mientras el nombre no se haya registrado.

La ausencia temporal de nombre no impide:

- PREG;
- KIN;
- CARE;
- RES;
- HLTH;
- propiedad futura;
- filiación.

El nombre se añade sin recrear la entidad.

---

## 9. Generación procedural

Una cultura puede proporcionar:

- repertorio;
- fonotáctica;
- pesos regionales;
- apellidos;
- reglas de transmisión;
- nombres protegidos;
- nombres reservados.

La generación debe ser:

- determinista;
- compatible con parentesco;
- persistente;
- no rerolleable tras materialización.

La fórmula concreta pertenece al default cultural.

---

## 10. Familia antes que apellido aleatorio

Si un NPC se materializa dentro de una familia ya existente:

- el generador debe consultar la ley cultural de apellidos;
- no debe asignar un apellido independiente al azar;
- debe respetar filiación, adopción y registros existentes.

Hogar no equivale a apellido.

Dos convivientes pueden tener apellidos distintos.

---

## 11. Títulos

Rey, Reina, Lord, Lady, capitán, maestro u otros tratamientos pertenecen a sus sistemas institucionales.

Pueden modificar `display_name`.

No reemplazan NAME.

---

## 12. IA

La IA puede:

- utilizar una forma nominal conocida;
- emplear un apodo autorizado;
- omitir un apellido si el registro social lo hace natural.

No puede:

- inventar el nombre de un NPC persistente;
- cambiarlo;
- revelar un nombre que el interlocutor no conoce;
- convertir un apodo en apellido;
- adjudicar parentesco por compartir apellido;
- adjudicar título por apellido.

---

## 13. LOD

Cambiar de LOD no cambia:

- nombre;
- apellido;
- alias persistente;
- historial nominal.

Un NPC materializado no se renombra para evitar duplicados.

---

## Regla final

**El nombre es una capa persistente y conocida de una persona; nunca sustituye al ID técnico ni crea por sí mismo parentesco, autoridad o historia.**
