# Treskal — espera, colas y capacidad de atención v0.1

## Estado

**DISEÑO DE GAMEPLAY APROBADO — SERVICIOS FINITOS SIN SISTEMA MODERNO DE TURNOS**

## Objetivo

Definir qué ocurre cuando varias personas necesitan al mismo tiempo:

- curandera;
- artesano;
- comerciante;
- posada;
- administración;
- transporte;
- otro servicio.

Sin introducir:

- máquinas de tickets;
- cola universal FIFO;
- citas digitales;
- atención instantánea al jugador.

---

# 1. Principio

Un servicio requiere:

- persona capaz;
- lugar;
- tiempo;
- recursos;
- disponibilidad.

Si alguno falta, aparece espera.

---

# 2. Estados de solicitud

## WAIT01 — intent

La persona quiere ser atendida pero todavía no inició la espera formal/social.

## WAIT02 — waiting

Está esperando.

## WAIT03 — acknowledged

El proveedor sabe que espera y prevé atenderla.

## WAIT04 — being_served

Atención en curso.

## WAIT05 — deferred

Se pospone por una causa.

## WAIT06 — abandoned

La persona deja de esperar.

## WAIT07 — completed

La atención terminó.

## WAIT08 — refused

El proveedor rechaza atender.

---

# 3. No existe orden universal

El orden puede depender de:

- llegada;
- urgencia;
- compromiso previo;
- relación;
- naturaleza del servicio;
- autoridad;
- capacidad;
- contexto.

No se define una cola matemática idéntica para todo Treskal.

---

# 4. Orden de llegada

Puede ser la regla social más sencilla en:

- vendedor;
- artesano;
- taberna;
- espera ordinaria.

Pero puede romperse por:

- emergencia;
- cliente ya comprometido;
- tarea en curso;
- autoridad institucional legítima.

---

# 5. Curandería

La urgencia puede tener prioridad sobre orden de llegada.

Una persona con problema menor puede esperar si aparece:

- herido grave;
- parto urgente;
- accidente.

No se fija un triage médico moderno.

---

# 6. Artesano

Un artesano puede distinguir entre:

- consulta rápida;
- encargo COM;
- reparación;
- entrega ya terminada.

La existencia de cola no altera plazos prometidos sin causa.

---

# 7. Comercio

Una tienda con mucha afluencia puede:

- hacer esperar;
- atender por orden práctico;
- repartir tareas entre trabajadores.

El jugador no detiene a todos los demás clientes al iniciar diálogo.

---

# 8. Posada

Puede haber espera para:

- habitación;
- comida;
- establo;
- atención del propietario.

Si no hay capacidad:

no existe obligación de atender más rápido.

---

# 9. Administración

Una dependencia puede necesitar:

- recepción;
- funcionario;
- documento;
- acceso.

Puede haber espera aunque el edificio esté abierto.

No se inventa un sistema burocrático de cita previa universal.

---

# 10. Transporte

Un carretero ocupado no se vuelve disponible por abrir interfaz.

La solicitud puede quedar:

- esperando;
- diferida;
- rechazada.

---

# 11. Espacio físico

La espera ocurre en un lugar.

Puede ser:

- sala;
- exterior;
- patio;
- mesa;
- zona de mercado.

Una acumulación grande puede afectar:

- tránsito;
- ruido;
- privacidad;
- comodidad.

---

# 12. Abandono

Una persona puede dejar de esperar por:

- tiempo;
- urgencia propia;
- cambio de plan;
- cierre;
- conflicto.

No desaparece del World State; cambia de actividad.

---

# 13. Rechazo

Puede deberse a:

- falta de capacidad;
- servicio incompatible;
- relación;
- acceso;
- comportamiento;
- cierre;
- falta de recursos.

No toda negativa es hostilidad.

---

# 14. Compromiso

WAIT03 puede crear una expectativa social:

“te atenderé después de este cliente.”

Puede enlazarse con PLEDGE si el lenguaje alcanza ese nivel.

No toda promesa informal de espera se convierte automáticamente en pledge.

---

# 15. Prioridad institucional

Un funcionario o guardia puede tener prioridad cuando:

- cumple función legítima;
- existe emergencia;
- el servicio lo requiere.

No es privilegio universal de cualquier persona con rango.

---

# 16. LOD

En LOD bajo puede agregarse:

- demand_count;
- service_capacity;
- average_wait_pressure;
- urgent_cases;
- persistent_requests.

En alto detalle se materializan personas concretas relevantes.

---

# 17. IA

La IA puede decir:

- “tendrá que esperar”;
- “estoy con otro cliente”;
- “vuelva más tarde”

solo si World State lo justifica.

No inventa una cola para bloquear al jugador ni elimina la existente para favorecerlo.

---

## Regla final

**En Treskal ser atendido significa encontrar tiempo dentro de la vida real de otra persona; el jugador no tiene prioridad metafísica.**
