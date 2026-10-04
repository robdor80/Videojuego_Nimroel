# Treskal — cuidado de niños, ancianos y dependientes v0.1

## Estado

**DISEÑO SOCIAL/JUGABLE APROBADO — CUIDADO COMO PARTE DE LA VIDA DOMÉSTICA**

## Objetivo

Definir cómo los hogares atienden a personas que necesitan ayuda cotidiana por:

- edad;
- enfermedad;
- lesión;
- limitación temporal;
- otra situación real.

Sin crear por defecto:

- guarderías modernas;
- residencias institucionales modernas;
- sistema público profesionalizado de cuidados.

---

# 1. Principio

El cuidado consume:

- tiempo;
- presencia;
- espacio;
- alimentos;
- descanso;
- organización doméstica.

No es una animación sin coste.

---

# 2. Categorías funcionales de necesidad

## DEP01 — child_care

Necesidad de supervisión/cuidado por edad.

## DEP02 — temporary_recovery_care

Persona temporalmente limitada por:

- lesión;
- enfermedad;
- convalecencia.

## DEP03 — long_term_daily_assistance

Necesita ayuda frecuente durante un periodo prolongado.

## DEP04 — elderly_assistance

Persona mayor que necesita apoyo en algunas tareas.

## DEP05 — high_dependency

Necesita presencia o asistencia intensa.

Estas categorías son funcionales.

No definen derechos legales ni diagnósticos.

---

# 3. Estados de cobertura

## CARE01 — covered

Las necesidades están cubiertas de forma suficiente.

## CARE02 — shared

El cuidado se reparte entre varias personas.

## CARE03 — strained

El hogar cubre necesidades con dificultad.

## CARE04 — gap

Existe un periodo sin cobertura suficiente.

## CARE05 — emergency_support

Se ha activado ayuda extraordinaria.

## CARE06 — external_help

Existe apoyo de persona externa al hogar.

## CARE07 — relocated_for_care

La persona se aloja temporal o establemente en otro lugar para recibir cuidado.

---

# 4. Quién puede cuidar

Puede participar:

- pareja;
- padres;
- hijos adultos;
- hermanos;
- otros familiares;
- miembros del hogar;
- vecinos;
- amistades;
- persona contratada futura;
- curandera cuando la necesidad sea sanitaria.

No toda ayuda implica convivencia.

---

# 5. Cuidado infantil

Un niño pequeño no debe tratarse como NPC autónomo con rutina adulta.

La supervisión puede afectar:

- disponibilidad laboral;
- desplazamientos;
- visitas;
- descanso;
- compras;
- vida social.

La autonomía aumenta según desarrollo futuro.

Este documento no fija edades exactas.

---

# 6. Niños mayores

Pueden tener más capacidad para:

- desplazarse;
- ayudar;
- jugar;
- realizar tareas apropiadas.

No se les asigna automáticamente trabajo adulto.

---

# 7. Ancianos

Ser anciano no implica dependencia.

Una persona mayor puede ser:

- plenamente autónoma;
- parcialmente asistida;
- altamente dependiente.

DEP04 solo se aplica cuando existe necesidad real.

---

# 8. Enfermedad o lesión

DEP02 puede aparecer por:

- accidente;
- enfermedad;
- recuperación;
- parto futuro si el sistema lo define.

Puede afectar simultáneamente:

- REST;
- EMP;
- household;
- salud.

---

# 9. Red familiar

Un hogar puede recibir ayuda de otro hogar.

Ejemplos:

- abuelo que supervisa a niños;
- hermana que lleva comida;
- vecino que acompaña;
- familiar que duerme temporalmente allí.

La ayuda requiere:

- relación;
- disponibilidad;
- conocimiento de la necesidad.

---

# 10. Vecindad

La proximidad puede facilitar apoyo.

No convierte a todos los vecinos en cuidadores automáticos.

La relación social sigue importando.

---

# 11. Trabajo y cuidado

Un cuidador puede:

- reducir jornada real;
- ausentarse;
- cambiar franja;
- rechazar trabajo temporal;
- compartir cuidado.

EMP debe reflejar la consecuencia cuando sea relevante.

No se crea “permiso laboral” legal universal.

---

# 12. Negocio familiar

En una casa-taller:

el cuidado puede convivir con actividad económica.

Pero:

- cliente;
- fuego;
- herramienta;
- ruido;
- riesgo

pueden limitar dónde permanece una persona dependiente.

---

# 13. Posada o alojamiento temporal

Una familia desplazada puede necesitar cuidar a dependientes en:

- posada;
- casa de pariente;
- otro alojamiento.

La capacidad del lugar importa.

---

# 14. Curandera

Una curandera puede tratar salud.

No sustituye automáticamente:

- alimentación;
- compañía;
- ayuda doméstica;
- supervisión continua.

El cuidado médico y el cuidado cotidiano son sistemas relacionados pero distintos.

---

# 15. Agotamiento del cuidador

CARE03 puede aparecer si:

- falta apoyo;
- el cuidado es intenso;
- el cuidador trabaja;
- existen otros dependientes;
- hay emergencia.

No se fija mecánica psicológica numérica.

Sí puede afectar:

- REST;
- disponibilidad;
- rutina.

---

# 16. Brecha de cuidado

CARE04 no significa automáticamente daño.

Sí significa que existe un problema real de cobertura.

El futuro sistema de necesidades/salud decide consecuencias.

---

# 17. Emergencia

CARE05 puede movilizar:

- familiares;
- vecinos;
- curandera;
- transporte;
- alojamiento.

No despierta a toda la ciudad.

---

# 18. Ayuda pagada

Puede existir de forma local si:

- alguien tiene capacidad;
- existe demanda;
- se acuerda compensación.

No se define un oficio institucional universal de cuidador.

---

# 19. Muerte del cuidador

Puede producir:

- CARE03/04/05;
- cambio de hogar;
- mudanza;
- necesidad de nueva red.

La tutela legal futura resolverá responsabilidades formales.

---

# 20. Muerte del dependiente

Termina la necesidad de cuidado, pero puede iniciar:

- MORT;
- luto;
- duelo;
- cambios de hogar y rutina.

---

# 21. LOD

En bajo detalle puede mantenerse:

- dependents_by_household;
- care_capacity;
- care_pressure;
- critical_gaps.

En alto detalle se materializa quién cuida a quién.

---

# 22. IA

Un NPC no debe abandonar a una persona altamente dependiente sin que exista:

- relevo;
- emergencia;
- decisión coherente;
- fallo real del sistema.

La IA no ignora CARE para facilitar una misión.

---

## Regla final

**En Treskal cuidar a alguien ocupa tiempo y organiza la vida de un hogar; la dependencia no desaparece cuando el jugador deja de mirar.**
