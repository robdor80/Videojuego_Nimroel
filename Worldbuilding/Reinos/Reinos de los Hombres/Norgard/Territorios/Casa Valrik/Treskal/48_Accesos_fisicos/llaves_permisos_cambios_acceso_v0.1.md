# Treskal — llaves, permisos y cambios de acceso v0.1

## Estado

**DISEÑO DE WORLD STATE APROBADO**

## Objetivo

Gestionar llaves y autorizaciones sin convertirlas en “tokens universales de acceso”.

---

# 1. Permiso y llave

Deben registrarse por separado.

## permiso

Derecho social/institucional.

## llave

Capacidad física para operar un cierre compatible.

Puede existir:

- permiso sin llave;
- llave sin permiso;
- ambos;
- ninguno.

---

# 2. Entrega de llave

Una entrega válida requiere:

- llave existente;
- poseedor con capacidad de transferirla;
- destinatario;
- World State actualizado.

La IA no crea una llave al decir “toma”.

---

# 3. Préstamo de llave

Puede registrar:

- lender_ref;
- borrower_ref;
- key_ref;
- valid_until_if_any;
- expected_return;
- access_scope.

El owner_ref puede seguir siendo otra persona/institución.

---

# 4. Llave perdida

Puede producir:

- búsqueda;
- cambio de cerradura futuro;
- retirada de permiso;
- riesgo de acceso no autorizado.

No revela automáticamente quién la encontró.

---

# 5. Cambio de cerradura

Si el cierre cambia:

las llaves antiguas pueden dejar de funcionar.

El access_ref permanece, pero cambia su mecanismo/compatibilidad.

No se fija frecuencia ni coste.

---

# 6. Permiso revocado

Una persona puede conservar físicamente una llave pero perder autorización.

Esto importa para:

- robo;
- empleado despedido;
- huésped que terminó estancia;
- proveedor cuyo acceso expiró.

---

# 7. Rol

En P4/P5, el acceso puede depender de rol además de llave.

Ejemplo:

tener una llave encontrada de T08 no convierte al jugador en trabajador autorizado.

---

# 8. Guardado

Para llaves relevantes debe persistir:

- identidad;
- propietario;
- poseedor;
- compatibilidad;
- estado.

Las llaves ordinarias de fondo pueden abstraerse mientras no sean jugables.

---

## Regla final

**La llave abre el mecanismo; el permiso abre la relación social. Nimroel debe recordar ambas cosas.**
