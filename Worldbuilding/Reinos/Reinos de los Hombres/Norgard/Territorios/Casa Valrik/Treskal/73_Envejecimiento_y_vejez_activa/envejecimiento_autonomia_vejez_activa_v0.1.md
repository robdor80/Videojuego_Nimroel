# Treskal — envejecimiento, autonomía y vejez activa v0.1

## Estado

**DISEÑO SOCIAL/JUGABLE APROBADO — SER MAYOR NO EQUIVALE A SER DEPENDIENTE**

## Objetivo

Definir cómo envejece un NPC de Treskal sin convertir la edad en un interruptor que pasa de adulto plenamente funcional a persona dependiente.

Este documento no fija:

- edades numéricas exactas;
- esperanza de vida;
- probabilidades de deterioro;
- edad legal de retiro;
- pensiones;
- herencia.

---

# 1. Identidad continua

Envejecer conserva:

- npc_id;
- personalidad;
- memoria;
- relaciones;
- reputación;
- profesión;
- bienes;
- historia.

La edad cambia capacidades y circunstancias, no crea una persona nueva.

---

# 2. Estados operativos

## AGE01 — mature_active

Adulto maduro con actividad ordinaria compatible con salud y profesión.

## AGE02 — later_life_active

Edad avanzada sin necesidad de reducción relevante de actividad.

Puede continuar trabajando, viajando, cuidando, comerciando y socializando.

## AGE03 — adapted_workload

Existe adaptación real de carga o tareas.

Puede afectar:

- esfuerzo;
- duración;
- desplazamientos;
- horarios;
- tipo de trabajo.

## AGE04 — selective_work_and_mentoring

La producción directa puede reducirse mientras aumenta el peso de:

- supervisión;
- enseñanza;
- consejo;
- control de calidad;
- transmisión de experiencia.

## AGE05 — withdrawn_from_regular_work

La persona ya no mantiene trabajo regular.

Eso no implica dependencia ni aislamiento.

## AGE06 — care_dependent_late_life

Existe necesidad real de ayuda cotidiana.

DEP04 y CARE pasan a ser relevantes.

---

# 3. No es una progresión obligatoria

AGE no es una escalera universal.

Una persona puede permanecer mucho tiempo activa.

Otra puede reducir actividad antes por:

- lesión;
- enfermedad;
- oficio físicamente exigente;
- circunstancias personales.

La edad cronológica por sí sola no decide el estado funcional.

---

# 4. Capacidad física y conocimiento

El envejecimiento puede reducir algunas capacidades físicas sin reducir automáticamente:

- experiencia;
- criterio;
- conocimiento;
- precisión;
- reputación;
- capacidad de enseñar.

Un artesano mayor puede producir menos volumen y, aun así, seguir siendo una referencia profesional.

---

# 5. Movilidad

La movilidad puede adaptarse según:

- salud;
- distancia;
- terreno;
- clima;
- carga;
- descanso.

No se presupone inmovilidad.

Una persona mayor puede recorrer Treskal con normalidad si su estado lo permite.

---

# 6. Hogar

El hogar puede absorber cambios mediante:

- redistribución de tareas;
- ayuda puntual;
- reducción de cargas pesadas;
- proximidad de objetos o actividades;
- apoyo de familia o convivientes.

No se crea dependencia completa por tener edad avanzada.

---

# 7. Cuidados

DEP04 solo se activa cuando existe una necesidad concreta de asistencia.

Una persona mayor también puede:

- cuidar nietos;
- ayudar a enfermos;
- cocinar;
- enseñar;
- gestionar hogar;
- apoyar un negocio.

Ser potencial receptor de ayuda no elimina la capacidad de ayudar a otros.

---

# 8. Ocio y vida social

La vejez no implica aislamiento.

Puede participar en:

- hogar;
- taberna;
- plaza;
- visitas;
- relatos;
- juegos;
- paseos;
- música;
- reuniones.

LEIS se mantiene sujeto a salud y disponibilidad real.

---

# 9. IA y diálogo

La IA no debe convertir automáticamente a un personaje mayor en:

- frágil;
- olvidadizo;
- lento mentalmente;
- enfermo;
- dependiente;
- sabio universal.

La personalidad y experiencia real siguen mandando.

---

# 10. Apariencia

El envejecimiento visual debe conservar continuidad reconocible.

Puede reflejar:

- cambios de cabello;
- piel;
- postura;
- constitución;
- desgaste corporal compatible.

No se rerrollea una cara distinta.

---

# 11. Enfermedad y deterioro

La edad puede ser un factor del futuro sistema de salud, pero este contrato no inventa diagnósticos ni probabilidades.

Un deterioro concreto debe provenir de un estado de salud real.

---

# 12. Muerte

AGE06 no significa muerte inminente.

La muerte se resuelve mediante salud/ciclo vital y luego MORT.

El juego no mata automáticamente a una persona por alcanzar una etiqueta de vejez.

---

# 13. LOD

El envejecimiento continúa fuera de cámara cuando avanza el tiempo válido.

Al regresar el jugador, el NPC mantiene continuidad de:

- hogar;
- relaciones;
- oficio;
- reputación;
- salud;
- actividad.

---

## Regla final

**En Treskal una persona envejece sin dejar de ser quien era: puede cambiar lo que hace y cuánto hace, pero su experiencia, relaciones y lugar en la comunidad continúan mientras su estado real lo permita.**
