# Treskal — puertas, llaves, cerraduras y acceso físico v0.1

> **MIGRADO A NIMROEL CORE — documentación derivada con override local explícito.** La autoridad normativa de DOOR reside en `Worldbuilding/Sistemas/Nimroel Core/04_Material_y_riesgo/puertas_llaves_acceso_fisico_v0.1.md`. Treskal conserva como particularidad su sistema de clases de acceso P; ante conflicto prevalece el Core.

## Estado

**DISEÑO DE GAMEPLAY APROBADO — ACCESO SOCIAL ≠ ACCESO FÍSICO**

## Objetivo

Separar tres preguntas distintas:

1. ¿Está físicamente abierto?
2. ¿Puede este actor abrirlo?
3. ¿Tiene permiso para entrar?

Estas respuestas no son equivalentes.

---

# 1. Capas de acceso

## Capa social

Clase P0–P5 y permisos.

## Capa física

Puerta, portón, ventana u otro acceso.

## Capa de cierre

Abierto, cerrado, bloqueado o asegurado.

## Capa de conocimiento

El actor sabe o no:

- dónde está el acceso;
- si existe;
- cómo abrirlo;
- quién puede autorizarlo.

---

# 2. Estados físicos de acceso

## DOOR01 — open

Paso físicamente abierto.

## DOOR02 — closed_unsecured

Cerrado, pero no asegurado.

## DOOR03 — secured

Asegurado mediante cierre compatible.

## DOOR04 — barred_or_blocked

Bloqueado físicamente.

## DOOR05 — damaged

El acceso existe pero está dañado.

## DOOR06 — destroyed

Ya no cumple función normal de cierre.

## DOOR07 — sealed_or_unavailable

No puede usarse temporalmente por:

- obra;
- evento;
- daño;
- decisión institucional.

---

# 3. Cerradura no equivale a permiso

Una puerta puede estar:

- abierta pero ser P3 privada;
- cerrada sin llave pero ser P0/P1;
- asegurada y ser P5;
- abierta por emergencia aunque normalmente sea P4.

El motor debe evaluar:

**estado físico + clase P + permiso + contexto**.

---

# 4. Llave

Una llave persistente puede registrar:

- key_id;
- owner_ref;
- possessor_ref;
- access_refs;
- state.

Poseer una llave no implica:

- ser propietario del lugar;
- tener permiso;
- autoridad permanente.

---

# 5. Copias

Puede existir más de una llave compatible con un mismo acceso cuando el contexto lo justifique.

No se presupone una única llave mágica por puerta.

El número exacto de copias no necesita materializarse hasta ser relevante.

---

# 6. Autoridad

Una persona puede abrir un acceso por:

- propiedad;
- residencia;
- trabajo;
- rol;
- invitación;
- autorización temporal;
- emergencia.

La relación debe existir en World State.

---

# 7. Acceso temporal

Ejemplos:

- huésped de posada;
- proveedor;
- aprendiz;
- visitante invitado;
- trabajador temporal.

El permiso puede caducar sin que cambie la cerradura.

---

# 8. Puertas de negocio

Durante horario/estado abierto:

la entrada pública puede funcionar como P0/P1.

Las áreas traseras pueden seguir siendo:

- P2;
- P3;
- P4.

Abrir la tienda no abre todo el edificio.

---

# 9. Viviendas

La vivienda ordinaria es P3.

Puede existir acceso legítimo para:

- residentes;
- invitados;
- familiares autorizados;
- trabajadores concretos.

No todo familiar tiene permiso automático.

---

# 10. Instituciones

P4/P5 pueden añadir:

- guardia;
- controles;
- identificación;
- acceso por rol.

Una llave por sí sola no debe anular esos controles.

Especialmente en Astilleros Reales.

---

# 11. Cerradura y World State

Un acceso materializado debe poder persistir:

- open_state;
- lock_state;
- damage_state;
- access_class;
- authorized_refs_or_rules;
- key_refs si son relevantes.

No se resetea al cargar escena.

---

# 12. Abrir y cerrar

La IA puede decir:

“abre la puerta”.

El motor debe validar:

- puerta existe;
- actor puede alcanzarla;
- estado;
- llave o mecanismo;
- permiso si afecta a la acción.

Solo entonces cambia World State.

---

# 13. Forzado

Una puerta puede sufrir:

- intento de forzado;
- daño;
- rotura.

El sistema de habilidades futuro determina posibilidad y resultado.

Este documento no define técnicas concretas.

---

# 14. Evidencia

Un acceso manipulado puede dejar:

- daño;
- marcas;
- estado alterado.

La Percepción puede revelar únicamente lo autorizado.

No se infiere culpable sin evidencia.

---

# 15. Cierre interior

Un acceso puede quedar bloqueado desde dentro mediante sistema físico compatible.

Esto puede impedir que una llave externa baste.

La arquitectura exacta define cada caso.

---

# 16. Ventanas y accesos secundarios

También pueden tener:

- clase P;
- estado físico;
- cierre;
- daño.

No se consideran “entrada libre” solo porque el motor permita alcanzar el punto.

---

# 17. Horarios

Un acceso puede cambiar por rutina:

- negocio abre/cierra;
- institución limita entrada;
- hogar se asegura por la noche.

No se usa horario universal.

---

# 18. Emergencia

Un incendio o peligro puede alterar temporalmente:

- permisos;
- puertas;
- rutas.

La emergencia puede justificar entrada excepcional.

No convierte el acceso en público para siempre.

---

# 19. NPC

Un NPC puede saber:

- qué puerta usar;
- dónde guarda una llave;
- quién autoriza.

Otro NPC puede ignorarlo.

El conocimiento de acceso no se comparte globalmente.

---

## Regla final

**En Treskal poder abrir una puerta no significa tener derecho a cruzarla, y tener permiso no significa que la puerta esté físicamente abierta.**
