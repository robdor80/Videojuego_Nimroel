# Treskal — relaciones laborales, vacantes y continuidad del trabajo v0.1

> **MIGRADO A NIMROEL CORE — documentación derivada.** La autoridad normativa de EMP reside en `Worldbuilding/Sistemas/Nimroel Core/03_Actividad_y_tiempo/empleo_puestos_vacantes_v0.1.md`. Este archivo conserva explicación y ejemplos de Treskal; ante conflicto prevalece el Core.

## Estado

**DISEÑO ECONÓMICO/SOCIAL APROBADO — RELACIÓN LABORAL PERSISTENTE**

## Objetivo

Definir la relación entre:

- persona;
- oficio;
- puesto;
- negocio/institución;
- disponibilidad;
- ausencia;
- vacante.

Este documento aplica localmente los sistemas EMP y hereda del Reino:

- escala salarial del Punto 5;
- capacidad, contratos laborales básicos y edades del Punto 7.

No fija una duración universal de jornada en horas.

---

# 1. Profesión ≠ puesto actual

Un NPC puede tener:

- profesión u oficio aprendido;
- empleo actual;
- empleo anterior;
- periodo sin puesto;
- actividad por cuenta propia;
- aprendizaje.

No toda persona con profesión está siempre ocupando un puesto.

---

# 2. Estados técnicos de relación laboral

## EMP01 — available_or_seeking

Persona disponible o buscando trabajo.

## EMP02 — active

Relación laboral activa.

## EMP03 — temporarily_absent

Mantiene el puesto, pero no trabaja actualmente.

Causas:

- enfermedad;
- visita;
- viaje;
- cuidado familiar;
- evento;
- permiso futuro si existe.

## EMP04 — reduced_capacity

Trabaja con capacidad reducida.

## EMP05 — suspended_or_waiting

La relación existe, pero no hay trabajo efectivo por:

- falta de material;
- cierre temporal;
- obra;
- bloqueo;
- evento.

## EMP06 — ending

Transición hacia salida.

## EMP07 — ended

La relación terminó.

## EMP08 — temporary_assignment

Trabajo temporal ligado a:

- entrega;
- temporada;
- evento;
- visita;
- necesidad concreta.

---

# 3. Puesto de trabajo

Un puesto puede registrar:

- job_id;
- occupation_family;
- workplace_ref;
- employer_or_responsible_ref;
- worker_ref;
- required_capability;
- state;
- schedule_or_daypart_pattern;
- start_time;
- end_time_if_known;
- reason_if_inactive.

---

# 4. Vacante

Un puesto puede quedar vacante por:

- muerte;
- salida;
- mudanza;
- cambio de oficio;
- despido futuro;
- crecimiento del negocio;
- nueva necesidad.

La vacante no crea automáticamente un trabajador.

---

# 5. Cobertura

Un negocio/institución puede intentar cubrir una vacante mediante:

- familiar;
- aprendiz preparado;
- trabajador conocido;
- persona disponible;
- visitante temporal;
- recomendación.

No se fija todavía un mercado laboral formal.

---

# 6. Sustitución

Una persona sustituta puede realizar solo tareas compatibles con su capacidad.

Ejemplo:

un ayudante puede mantener ventas ordinarias.

No puede asumir automáticamente:

- trabajo maestro;
- autoridad institucional;
- oficio especializado.

---

# 7. Ausencia

La ausencia afecta:

- capacidad;
- horario;
- producción;
- atención;
- encargos.

El trabajador no se teletransporta al lugar de trabajo porque el jugador haya llegado.

---

# 8. Enfermedad

Puede producir:

- EMP03;
- EMP04;
- cierre parcial;
- sustitución.

La curación no se resuelve por el contrato laboral.

---

# 9. Aprendiz

Un aprendiz puede tener simultáneamente:

- relación de aprendizaje;
- actividad laboral real.

Pero su capacidad sigue limitada por progreso.

No se cuenta automáticamente como maestro completo.

---

# 10. Trabajo familiar

Un miembro de hogar puede colaborar en negocio familiar sin que toda colaboración necesite contrato formal.

Aun así, el motor puede registrar:

- workplace_ref;
- role;
- activity;

si es relevante.

---

# 11. Autónomo/artesano propietario

Un artesano puede ser:

- propietario;
- trabajador principal;
- maestro;
- vendedor.

Son roles distintos aunque los cumpla la misma persona.

---

# 12. Visitante temporal

V07 puede asumir EMP08 cuando:

- existe necesidad real;
- tiene capacidad;
- hay alojamiento/estancia.

No se convierte en residente automáticamente.

---

# 13. Muerte

La muerte de un trabajador:

- termina su relación;
- crea posible vacante;
- afecta hogar;
- puede afectar negocio.

No genera reemplazo instantáneo.

---

# 14. Cambio de empleo

Una persona puede:

- cambiar de negocio;
- abandonar oficio;
- especializarse;
- mudarse.

La profesión aprendida no desaparece porque cambie workplace_ref.

---

# 15. Recomendación y reputación

La reputación profesional puede afectar:

- oportunidad;
- recomendación;
- confianza inicial.

No garantiza contratación.

---

# 16. Palabra dada

Un compromiso de trabajo puede enlazarse a PLEDGE.

Ejemplo:

- acudir;
- terminar encargo;
- permanecer hasta fecha.

La relación social de honor es distinta del vínculo económico.

---

# 17. Horario

Este documento usa patrones de:

- daypart;
- actividad;
- necesidad.

No fija horas exactas universales.

El futuro sistema temporal podrá concretarlas.

---

# 18. Pago

El Punto 5 monetario resuelve la dependencia económica general.

Treskal hereda como anclas de Reino:

- jornalero/no especializado: 8–12 Clavos por jornada equivalente, ancla 10;
- trabajador formado/estable: 12–18 Clavos, ancla 15;
- oficial cualificado: 16–24 Clavos, ancla 20;
- maestro/especialista: 24–48 Clavos, ancla 36;
- trabajo raro, extraordinario o peligroso: por contrato.

Esto **no crea una jornada legal ni una frecuencia salarial universal**.

El pago puede producirse por jornada, periodo, obra, viaje, temporada u otro acuerdo y puede incluir:

- moneda;
- comida;
- alojamiento;
- participación;
- especie;
- combinación pactada.

El precio concreto del trabajo sigue dependiendo de oficio, escasez, riesgo, reputación, disponibilidad y World State.

---

# 19. Derecho laboral

Treskal hereda el Punto 7 de Norgard:

- aprendizaje formal desde 12 años;
- empleo juvenil ordinario desde 15;
- mayoría/capacidad civil general a los 18;
- contratos orales o escritos según contexto;
- compensación ganada obligatoria;
- inexistencia de indemnización universal automática por despido;
- inexistencia de jornada universal fija en horas;
- prohibición de trabajo forzoso por deuda, contrato o parentesco;
- límites de trabajo peligroso para menores.

La propiedad, herencia y alquiler permanecen para el Punto 8.

---

# 20. LOD

En LOD-L:

puede conservarse:

- puestos cubiertos;
- vacantes;
- ausencias;
- capacidad agregada.

En LOD-H:

se materializa quién trabaja realmente.

Los hechos no cambian por LOD.

---

## Regla final

**Treskal funciona porque personas concretas ocupan puestos concretos; una vacante es un problema real, no una llamada automática al generador de NPC.**
