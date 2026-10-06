# Treskal — auditoría de cierre funcional v0.1

## Estado

**BASE FUNCIONAL CERRADA HASTA LA CAPA 99 — PENDIENTE DE DEPENDENCIAS CANÓNICAS Y DETALLE DE IMPLEMENTACIÓN**

## Objetivo

Determinar si Treskal necesita nuevas capas funcionales locales o si el trabajo restante pertenece a:

- canon superior de Norgard/Nimroel;
- cartografía y geometría detallada;
- sistemas globales todavía no definidos;
- implementación técnica;
- extracción de reglas reutilizables.

---

# 1. Resultado

La auditoría de las capas 01–99 no identifica un hueco funcional local suficientemente independiente como para justificar una capa 100.

Esto no significa que Treskal esté terminada en todos sus detalles.

Significa que su **modelo funcional base** cubre ya:

- ciudad y topología;
- infraestructura;
- economía y materiales;
- población persistente;
- trabajo y negocios;
- hogares y vivienda;
- percepción e información;
- relaciones;
- ciclo vital;
- necesidades;
- memoria;
- personalidad;
- valores;
- decisiones;
- diálogo;
- tiempo;
- emergencias;
- parentesco;
- IA y World State.

---

# 2. Criterio para no crear la capa 100

No se añade una capa por numeración.

Una nueva capa solo deberá aparecer si:

1. existe una autoridad funcional que ninguna capa actual posee;
2. no puede resolverse mediante composición de sistemas existentes;
3. no pertenece claramente a un canon superior pendiente;
4. necesita persistencia o reglas propias.

La auditoría actual no encuentra otro caso que cumpla esos cuatro puntos.

---

# 3. Estado por dominios

## Ciudad y espacio

**Cubierto a nivel funcional.**

Pendiente:

- plano métrico;
- geometría exacta del río;
- geometría exacta del puente principal;
- posibles cruces menores;
- geometría de calle;
- planos detallados de edificios singulares.

Eso es cartografía/detalle, no una nueva capa de simulación.

## Economía y propiedad

**Cubierto a nivel causal y operativo.**

Ya resuelto por canon superior:

- moneda y balance base;
- fiscalidad/aduanas.

Pendiente de canon superior:

- herencia;
- alquiler;
- derecho económico/patrimonial;
- reglas laborales.

## Vida material

**Cubierta.**

Incluye:

- objetos;
- propiedad;
- desgaste;
- reparación;
- herramientas;
- mobiliario;
- ropa;
- combustible;
- agua;
- residuos;
- stock;
- mercados.

## NPC y ciclo vital

**Cubierto como base funcional.**

Incluye:

- infancia;
- aprendizaje;
- trabajo;
- pareja;
- embarazo;
- nacimiento;
- envejecimiento;
- dependencia;
- muerte;
- parentesco.

Pendiente:

- edades exactas;
- longevidad;
- reproducción;
- fisiología;
- consecuencias médicas;
- filiación legal.

## Relaciones y sociedad

**Cubierto como base funcional.**

Incluye:

- amistad;
- pareja;
- confianza;
- conflicto;
- favores;
- regalos;
- peticiones;
- límites;
- confidencias;
- opiniones;
- familia.

Ya resuelto por Punto 6 de Norgard:

- matrimonio formal;
- filiación jurídica;
- tutela;
- adopción;
- afinidad;
- responsabilidad parental.

La mayoría de edad general está fijada en 18 años; las reglas laborales detalladas permanecen para el Punto 7.

## Cognición y conducta

**Cubierto como base funcional.**

Incluye:

- conocimiento;
- credibilidad;
- verdad y falsedad;
- memoria;
- personalidad;
- valores;
- identidad;
- emociones;
- ánimo;
- presión;
- objetivos;
- decisiones;
- expectativas;
- atención;
- opinión;
- agenda.

## Conversación e IA

**Cubierto como contrato funcional.**

Incluye:

- contexto limitado;
- percepción;
- privacidad;
- audición;
- divulgación;
- mentira;
- memoria;
- autonomía;
- cierre de conversación;
- acciones validadas por motor.

La IA interpreta.

El motor conserva autoridad.

## Riesgo y emergencia

**Cubierto a nivel funcional.**

Incluye:

- riesgos laborales;
- accidentes;
- incendios;
- respuesta personal;
- evacuación;
- atención;
- cuidados.

Pendiente:

- salud exacta;
- lesión exacta;
- protocolos institucionales futuros.

---

# 4. Dependencias que NO deben resolverse dentro de Treskal

No deben inventarse localmente:

- rangos de guardia;
- derecho de propiedad/herencia;
- reglas laborales y capacidad laboral;
- horarios exactos globales;
- fisiología y salud;
- progresión exacta de habilidades;
- nomenclatura naval;
- canon animal;
- vehículos exactos;
- gastronomía detallada;
- flora medicinal;
- calendario fino de mercados.

Resolverlas en Treskal crearía contradicciones cuando el resto de Norgard las herede.

---

# 5. Validación

Estado actual de packs:

- pruebas comparativas IA: **27**;
- pruebas de integración urbana: **22**.

Los packs ya cubren tanto sistemas fundacionales como capas sociales/cognitivas recientes.

La ejecución real contra modelos o motor sigue siendo una fase posterior.

---

# 6. Reutilización

Una parte importante de Treskal ya no debe considerarse “lore exclusivo de Treskal”.

La siguiente gran fase correcta es extraer tres niveles:

**Nimroel Core → defaults culturales de Norgard → override local de Treskal**

Treskal debe conservar únicamente aquello que sea realmente local.

---

# 7. Estado de cierre

Clasificación:

**FUNCTIONAL_BASE_COMPLETE_PENDING_EXTERNAL_CANON**

No significa:

- contenido final;
- geometría final;
- balance final;
- implementación final.

Sí significa:

**no seguir añadiendo sistemas locales por inercia.**

---

## Regla final

**Treskal ya tiene suficiente estructura para vivir; el siguiente salto de calidad no consiste en añadir una capa 100, sino en separar qué pertenece a todo Nimroel, qué pertenece a Norgard y qué pertenece únicamente a Treskal.**


---

### Actualización posterior — Puntos 1–6 de Norgard

Varias dependencias que esta auditoría dejó correctamente fuera de Treskal ya han sido resueltas a nivel superior:

- sistema militar;
- Armada/Astilleros;
- sistema marítimo;
- fiscalidad/aduanas;
- sistema penal;
- moneda/balance base;
- matrimonio/filiación/tutela/adopción.

Esto confirma la decisión original de no crear una capa 100 local: Treskal hereda estos sistemas desde Norgard.
