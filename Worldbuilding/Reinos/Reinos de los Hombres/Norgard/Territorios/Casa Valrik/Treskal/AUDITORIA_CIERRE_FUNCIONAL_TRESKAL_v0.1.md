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
- fiscalidad/aduanas;
- mayoría de edad, capacidad y reglas laborales.

Ya resuelto por Punto 8 de Norgard:

- herencia;
- alquiler;
- derecho de propiedad y régimen patrimonial.

Pueden quedar futuros detalles comerciales específicos que no reabren la arquitectura patrimonial.

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

- umbrales exactos de etapas CHD/ciclo vital más allá de las bandas jurídicas;
- longevidad;
- reproducción/concepción;
- fisiología específica de pueblos que todavía no se hayan desarrollado.

Las consecuencias sanitarias generales ya están resueltas por Core + Punto 9. La filiación legal está resuelta por Punto 6 y las bandas jurídicas de edad por Punto 7.

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

Punto 7 deja además cerrado: mayoría civil a los 18, aprendizaje formal desde 12, empleo juvenil desde 15 y capacidad laboral adulta desde 18.

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
- horarios exactos globales;
- fisiología y salud;
- progresión exacta de habilidades;
- nomenclatura naval;
- canon animal;
- vehículos exactos;
- gastronomía detallada;
- flora medicinal;
- frecuencias concretas de mercados especializados cuando se diseñen.

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

### Actualización posterior — Puntos 1–13 de Norgard

Varias dependencias que esta auditoría dejó correctamente fuera de Treskal ya han sido resueltas a nivel superior:

- sistema militar;
- Armada/Astilleros;
- sistema marítimo;
- fiscalidad/aduanas;
- sistema penal;
- moneda/balance base;
- matrimonio/filiación/tutela/adopción;
- mayoría de edad/capacidad/trabajo/aprendizaje;
- propiedad/herencia/alquiler;
- salud/curandería y fisiología sanitaria;
- gastronomía, alimentos, cocina y conservación;
- nombres personales, apellidos y transmisión nominal.

Esto confirma la decisión original de no crear una capa 100 local: Treskal hereda estos sistemas desde Core/Norgard.


---

### Actualización transversal — personalidad persistente

La capa psicológica de NPC humanos queda reforzada sin crear una nueva capa local:

- PERS ampliado en Core a 28 dimensiones;
- generación procedural activada en Norgard;
- población A/B/C de Treskal conectada a authored/procedural/latent;
- promoción C→B irreversible;
- persistencia a través de LOD;
- IA solo expresiva, no autoritativa.

Esto no altera el estado de cierre funcional de Treskal.


Punto 9 resuelve además las antiguas dependencias locales de:

- gravedad de accidentes;
- enfermedad/infección;
- recuperación y secuelas;
- efectos sanitarios de higiene/saneamiento;
- complicaciones de embarazo/parto;
- capacidad y espera de curanderas.

Permanece pendiente la flora medicinal concreta.


Punto 10 resuelve además las antiguas dependencias locales de:

- recetario canónico;
- grupos alimentarios concretos;
- conservación culinaria;
- oferta plausible de posadas/tabernas;
- comida preparada de mercado;
- comida de viaje;
- provisiones militares/navales;
- relación FOOD ↔ almacenamiento/combustible.

Siguen pendientes los nombres folclóricos locales y los menús ligados a festividades aún no definidas.


Punto 11 resuelve además las antiguas dependencias locales de:

- nombre procedural persistente;
- apellido de nacimiento;
- apellido matrimonial;
- apellido adoptivo;
- apodos/alias frente a nombre legal;
- apellidos protegidos de Grandes Casas;
- relación NAME ↔ KIN/PREG/filiación.

Treskal no necesita un sistema nominal local distinto.


Punto 12 resuelve además las antiguas dependencias locales de:

- fecha/hora global;
- calendario;
- estaciones;
- agenda exacta;
- cumpleaños y mayoría;
- tres jornadas de luto;
- vencimientos;
- mercados diarios;
- timestamps de World State.

Treskal no necesita calendario local diferente.


Punto 13 resuelve además las antiguas dependencias locales de:

- fibras textiles;
- materiales de lavado;
- herramientas/materiales comunes;
- cerraduras/herrajes;
- iluminación;
- mobiliario;
- escritura;
- vajilla;
- objetos sanitarios;
- cultura material temporal.

Treskal hereda esta base desde Norgard y no crea nivel tecnológico propio.

Regla autoral preservada: **relojes fuera**.
