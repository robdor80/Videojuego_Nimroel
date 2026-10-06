# Treskal — cobertura de puestos y disponibilidad de trabajadores v0.1

> **MIGRADO A NIMROEL CORE — documentación derivada.** La autoridad normativa de EMP reside en `Worldbuilding/Sistemas/Nimroel Core/03_Actividad_y_tiempo/empleo_puestos_vacantes_v0.1.md`. Este archivo conserva explicación y ejemplos de Treskal; ante conflicto prevalece el Core.

## Estado

**DISEÑO DE SIMULACIÓN APROBADO**

## Objetivo

Cerrar el ciclo:

**necesidad → puesto → búsqueda → candidato → incorporación → actividad → salida/vacante**

sin inventar un sistema burocrático moderno.

---

# 1. Creación de puesto

Un job_id nuevo necesita causa:

- nueva capacidad;
- negocio que crece;
- sustitución;
- evento;
- institución;
- temporada/flujo temporal.

No se crean puestos para emplear población sobrante.

---

# 2. Candidatos

Un candidato puede surgir de:

- EMP01;
- aprendiz próximo a competencia;
- recomendación;
- familia;
- visitante V07;
- trabajador que quiere cambiar.

---

# 3. Compatibilidad

Se evalúa:

- capacidad;
- profesión;
- experiencia;
- disponibilidad;
- ubicación;
- relación;
- reputación;
- horario;
- necesidad.

No se elige exclusivamente por “nivel”.

---

# 4. Incorporación

Al cubrir:

- job.worker_ref se asigna;
- relación pasa a EMP02/EMP08;
- rutina se actualiza;
- hogar/traslado puede verse afectado.

---

# 5. Periodo sin empleo

No borra:

- profesión;
- experiencia;
- relaciones;
- reputación.

Puede afectar:

- economía del hogar;
- rutina;
- búsqueda.

El impacto monetario se expresa ya mediante Clavo/Luna/Corona y las anclas salariales del Punto 5; la cuantía concreta depende del puesto, duración, acuerdo y World State.

---

# 6. Puestos críticos

Algunos roles pueden tener mayor prioridad de cobertura:

- producción esencial;
- puerto;
- cuidado;
- mantenimiento;
- institución.

No se fija una lista legal rígida.

---

# 7. Saturación laboral

Una ciudad no debe crear más trabajadores persistentes que:

- hogares;
- población;
- capacidad económica

puedan sostener.

---

# 8. Cambio fuera de escena

Una vacante puede cubrirse offscreen si:

- existen candidatos plausibles;
- pasa tiempo;
- la relación puede formarse.

No debe aparecer un maestro excepcional de la nada.

---

## Regla final

**El mercado laboral de Treskal emerge de personas, familias y necesidades reales; no de rellenar automáticamente una plantilla.**
