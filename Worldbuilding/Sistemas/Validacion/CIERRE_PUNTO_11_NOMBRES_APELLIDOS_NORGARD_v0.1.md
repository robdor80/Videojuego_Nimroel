# Cierre Punto 11 — Nombres personales / apellidos / transmisión nominal de Norgard v0.1

## Estado

**PUNTO 11 CERRADO — NOMBRES / APELLIDOS**

Marcador:

`NAMING_POINT_11_CLOSED_NORGARD_PERSONAL_NAMES_SURNAMES`

## Cerrado en Nimroel Core

- NAME como capa nominal persistente;
- nombre legal vigente;
- nombre provisional;
- nombre legal anterior;
- alias/sobrenombre;
- identidad nominal desconocida;
- separación entre nombre visible y npc_id;
- historial de cambios;
- conocimiento de nombres;
- integración con K/CRED/KIN/SELF;
- persistencia a través de LOD;
- autoridad de IA.

## Cerrado en Norgard

- estructura ordinaria nombre + un apellido;
- segundo nombre opcional;
- sin doble apellido obligatorio;
- sin patronímico obligatorio;
- sin apellido distinto por sexo;
- sin apellido de bastardo;
- transmisión con un progenitor;
- elección con dos progenitores;
- fallback registral al apellido de quien dio a luz si no existe acuerdo;
- reconocimiento posterior sin cambio automático;
- menores sin filiación conocida;
- matrimonio sin cambio automático;
- disolución/viudedad sin reversión automática;
- cambio legal de nombre;
- nombre de menores;
- adopción;
- hijastros;
- hermanos con apellidos diferentes;
- apodos y sobrenombres;
- homónimos;
- variación documental;
- apellidos protegidos de Grandes Casas;
- preservación completa de la excepción Aethros;
- generador procedural humano de Norgard.

## Generador

Biblioteca inicial:

- 48 nombres de sesgo masculino;
- 48 nombres de sesgo femenino;
- 24 nombres unisex;
- 72 apellidos ordinarios;
- expansión fonotáctica;
- sesgos regionales suaves;
- ninguna exclusividad por Gran Casa;
- nombres autorales reservables;
- apellidos Aethros/Darovan/Edranor/Galdren/Valrik bloqueados para random.

## Integración con población

- A → nombre autoral;
- B → nombre completo persistente;
- C → seed nominal latente;
- C→B resuelve una sola vez;
- el apellido se decide después de consultar KIN/filiación;
- un nombre ya observado se conserva.

## No reabre Punto 6

Punto 6 sigue siendo autoridad sobre:

- matrimonio;
- filiación;
- tutela;
- adopción.

Punto 11 únicamente determina consecuencias nominales.

## No reabre Punto 8

Herencia no se decide por apellido.

El cambio de apellido no crea ni elimina derechos hereditarios.

## No reabre sucesión Aethros

NAME no crea sangre Aethros.

El apellido Aethros continúa sujeto a su canon dinástico específico.

## No definido deliberadamente

- nombres élficos;
- nombres de otros pueblos;
- santoral;
- onomástica religiosa;
- festividades nominales;
- Casas menores todavía no canonizadas.

## Validación

- regresión E15 de 100 invariantes;
- pack estático de 63 casos;
- contrato Core NAME;
- default de Reino;
- generador procedural.

## Regla final

**Punto 11 cierra cómo se llama una persona y cómo puede cambiar ese nombre sin confundir jamás nombre, familia, sangre, título e identidad técnica.**

`NAMING_POINT_11_CLOSED_NORGARD_PERSONAL_NAMES_SURNAMES`
