# Treskal — tareas domésticas y carga del hogar v0.1

## Estado

**DISEÑO DE VIDA COTIDIANA APROBADO — TRABAJO DOMÉSTICO REAL**

## Objetivo

Unificar en un mismo sistema las tareas que mantienen un hogar funcional:

- traer agua;
- conseguir combustible;
- cocinar;
- limpiar;
- lavar;
- retirar residuos;
- cuidar dependientes;
- comprar;
- mantener objetos y ropa.

Sin convertirlas en animaciones gratuitas ni asignarlas automáticamente por sexo.

---

# 1. Principio

El hogar consume tiempo además de recursos.

Una vivienda con:

- agua;
- comida;
- ropa limpia;
- combustible;
- espacio habitable

solo puede mantenerse porque alguien realiza trabajo doméstico o existe ayuda real.

---

# 2. Familias de tarea

## CHORE01 — water_supply

- recoger;
- transportar;
- almacenar agua.

## CHORE02 — fuel_supply

- traer;
- cortar/preparar cuando proceda;
- almacenar combustible.

## CHORE03 — food_preparation

- preparar;
- cocinar;
- conservar;
- servir.

## CHORE04 — cleaning

- barrer;
- limpiar superficies;
- retirar suciedad;
- mantener espacio usable.

## CHORE05 — laundry

- lavar;
- secar;
- recoger;
- reparar de forma simple.

## CHORE06 — waste_removal

- contener;
- transportar;
- llevar residuos al punto compatible.

## CHORE07 — dependent_care

- supervisar;
- acompañar;
- alimentar;
- ayudar.

## CHORE08 — shopping_and_errands

- comprar;
- recoger encargos;
- llevar recados domésticos.

## CHORE09 — household_maintenance

- pequeñas reparaciones;
- revisar mobiliario;
- ordenar almacenamiento;
- resolver desgaste menor.

---

# 3. Estados

## DOM01 — covered

La carga doméstica está razonablemente cubierta.

## DOM02 — shared

Las tareas se reparten entre varios miembros o ayudas externas.

## DOM03 — delayed

Algunas tareas se han retrasado sin causar todavía un problema serio.

## DOM04 — strained

El hogar tiene dificultades para mantener el ritmo.

## DOM05 — backlog

Se acumulan tareas pendientes.

## DOM06 — external_support

Existe ayuda regular o puntual desde fuera del hogar.

## DOM07 — disrupted

Evento, enfermedad, muerte, mudanza u otra causa ha alterado seriamente la organización doméstica.

---

# 4. Reparto de tareas

Puede depender de:

- edad;
- capacidad;
- disponibilidad;
- trabajo;
- relación;
- preferencia;
- costumbre familiar;
- habilidad;
- salud.

No se asignan tareas por sexo de forma automática.

Si una cultura futura fija tendencias, deberán documentarse expresamente.

---

# 5. Niños

Pueden colaborar en tareas apropiadas a su desarrollo.

No se les trata como trabajadores domésticos adultos completos.

---

# 6. Ancianos

Pueden:

- participar plenamente;
- realizar tareas ligeras;
- necesitar ayuda.

La edad sola no decide capacidad.

---

# 7. Trabajo remunerado y hogar

EMP puede competir con CHORE por tiempo.

Un hogar con varios adultos trabajando fuera puede necesitar:

- reparto distinto;
- tareas nocturnas;
- ayuda familiar;
- ayuda pagada;
- simplificación de actividad.

No aparece un sirviente automático.

---

# 8. Agua

CHORE01 depende de:

- punto real de agua;
- distancia;
- recipientes;
- capacidad de transporte.

No se genera por rutina abstracta.

---

# 9. Combustible

CHORE02 depende de:

- stock;
- proveedor;
- transporte;
- clima;
- almacenamiento.

Una pila llena reduce necesidad inmediata.

---

# 10. Cocina

CHORE03 requiere:

- alimento;
- combustible cuando haga falta;
- utensilios;
- tiempo.

No se cocina durante horas en las que nadie disponible pueda hacerlo salvo preparación previa o ayuda real.

---

# 11. Limpieza

CHORE04 puede responder a:

- ocupación;
- barro;
- humo;
- actividad;
- huéspedes;
- animales;
- accidente.

No existe suciedad lineal universal por paso del tiempo.

---

# 12. Colada

CHORE05 conecta con:

- agua;
- clima;
- ropa;
- secado.

Puede posponerse por lluvia o falta de agua.

---

# 13. Residuos

CHORE06 conecta con WASTE/WST.

El hogar no se considera limpio si la basura simplemente se oculta de render.

---

# 14. Cuidado

CHORE07 enlaza con CARE.

Una persona puede estar físicamente en casa y no disponible porque cuida a alguien.

---

# 15. Compras y recados

CHORE08 puede implicar:

- mercado;
- comercio;
- espera;
- mensajería;
- desplazamiento.

El hogar necesita salir al mundo.

---

# 16. Mantenimiento menor

CHORE09 puede resolver:

- ajuste simple;
- limpieza de herramienta doméstica;
- remiendo básico;
- organización.

Reparaciones complejas pasan a:

- O;
- COM;
- repair job.

---

# 17. Acumulación

DOM03/04/05 puede producir señales como:

- falta de ropa seca;
- menos comida preparada;
- agua baja;
- leña baja;
- suciedad localizada;
- residuos pendientes.

No genera todos los problemas a la vez.

---

# 18. Huéspedes

HOSP puede aumentar:

- agua;
- comida;
- limpieza;
- ropa de cama;
- combustible;
- residuos.

La hospitalidad tiene coste doméstico real.

---

# 19. Luto

Durante luto formal:

la carga puede redistribuirse mediante:

- familiares;
- vecinos;
- amigos;
- ayudas externas.

Esto permite que el hogar reduzca actividad ordinaria sin dejar de funcionar.

---

# 20. Enfermedad o muerte

Si una persona que realizaba muchas tareas queda ausente:

puede aparecer:

- DOM04;
- DOM05;
- DOM07.

No se redistribuye todo automáticamente.

---

# 21. Capacidad económica

Un hogar con recursos puede:

- comprar más servicios;
- encargar tareas;
- disponer de más herramientas;
- almacenar más.

No elimina por completo la logística doméstica.

---

# 22. LOD

En bajo detalle pueden mantenerse:

- domestic_load;
- chore_coverage;
- backlog;
- critical_shortages;
- external_support.

En alto detalle se materializan tareas concretas cuando son relevantes.

---

## Regla final

**Una casa funciona porque alguien hace el trabajo que no se ve; Nimroel debe recordarlo aunque no obligue al jugador a contemplar cada cubo de agua.**
