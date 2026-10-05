# Treskal — aprendizaje de oficio y relación maestro-aprendiz v0.1

> **MIGRADO A NIMROEL CORE — documentación derivada.** La autoridad normativa de APR reside en `Worldbuilding/Sistemas/Nimroel Core/03_Actividad_y_tiempo/aprendizaje_oficio_transmision_habilidad_v0.1.md`. Este archivo conserva explicación y ejemplos de Treskal; ante conflicto prevalece el Core.

## Estado

**DISEÑO SOCIAL/ECONÓMICO APROBADO — TRANSMISIÓN PRÁCTICA DE OFICIO**

## Objetivo

Definir cómo una persona aprende un oficio mediante:

- observación;
- práctica;
- supervisión;
- tareas reales;
- corrección;
- experiencia acumulada.

Sin presuponer:

- gremios universales;
- escuelas profesionales modernas;
- certificados estandarizados;
- progreso automático por tiempo.

---

# 1. Principio

Aprender un oficio requiere:

- alguien o algo de lo que aprender;
- acceso a tareas;
- herramientas;
- tiempo;
- práctica;
- dificultad creciente.

El paso del tiempo por sí solo no convierte a un aprendiz en maestro.

---

# 2. Estados de aprendizaje

## APR01 — observing

Observa, ayuda y aprende rutinas básicas.

## APR02 — assisted_practice

Realiza tareas sencillas con supervisión directa.

## APR03 — supervised_work

Ejecuta trabajo real limitado con revisión frecuente.

## APR04 — competent_routine_work

Puede completar tareas ordinarias del oficio sin supervisión constante.

## APR05 — advanced_practice

Puede afrontar trabajos complejos dentro de su experiencia.

## APR06 — independent_practitioner

Puede ejercer de forma autónoma dentro de su especialidad real.

APR06 no equivale automáticamente a maestro excepcional.

---

# 3. Maestro

Un maestro o trabajador experimentado puede transmitir:

- técnica;
- secuencia;
- juicio práctico;
- estándares;
- seguridad;
- conocimiento local;
- uso de herramientas.

Ser excelente artesano no garantiza ser excelente enseñando.

---

# 4. Relación formativa

Una relación puede registrar:

- apprenticeship_id;
- learner_ref;
- mentor_refs;
- occupation_family;
- workplace_ref;
- learning_state;
- allowed_task_classes;
- supervised_task_refs;
- progress_evidence;
- start_time;
- end_time_if_any;
- interruption_reason_if_any.

---

# 5. Progreso

Puede depender de:

- variedad de tareas;
- repetición útil;
- calidad de supervisión;
- resultados;
- errores corregidos;
- herramientas disponibles;
- materiales;
- tiempo efectivo;
- capacidad individual.

No se calcula solo con “horas acumuladas”.

---

# 6. Tareas permitidas

Cada estado APR limita tareas.

Ejemplo conceptual:

APR01:
- observar;
- transportar;
- preparar;
- limpiar;
- asistir.

APR02:
- tareas simples y reversibles.

APR03:
- producción real limitada.

APR04:
- trabajo ordinario completo.

APR05:
- trabajos complejos con menor supervisión.

APR06:
- trabajo autónomo.

La clasificación exacta depende del oficio.

---

# 7. Producción

Un aprendiz puede contribuir a producción real.

Pero:

- su velocidad;
- calidad;
- autonomía;
- riesgo

dependen de estado y tarea.

No cuenta automáticamente como trabajador plenamente competente.

---

# 8. Error

El error puede:

- desperdiciar material;
- retrasar encargo;
- dañar pieza;
- requerir corrección;
- convertirse en aprendizaje.

No todo error produce accidente.

---

# 9. Seguridad

Tareas peligrosas deben respetar:

- HAZ;
- TOOL;
- supervisión;
- capacidad.

No se entrega trabajo crítico a APR01 para acelerar progreso.

---

# 10. Herramientas

El acceso a herramientas puede ser:

- prestado;
- compartido;
- restringido;
- progresivo.

Poseer herramienta no demuestra competencia.

---

# 11. Familia

Un oficio puede transmitirse dentro del hogar.

Eso no significa que:

- todo hijo siga el oficio familiar;
- la capacidad se herede automáticamente;
- exista obligación universal.

---

# 12. Taller ajeno

Un aprendiz puede formarse con:

- artesano;
- negocio;
- institución;
- familiar;
- especialista.

No se exige parentesco.

---

# 13. Aprendiz visitante

Una persona puede viajar o permanecer temporalmente para aprender.

Puede combinar:

- V07;
- EMP08;
- HOSP/posada;
- APR.

No se vuelve residente automáticamente.

---

# 14. Cambio de mentor

Puede ocurrir por:

- muerte;
- mudanza;
- conflicto;
- especialización;
- cierre;
- oportunidad.

El aprendiz conserva aprendizaje previo.

---

# 15. Interrupción

La relación puede pausarse por:

- enfermedad;
- cierre;
- falta de material;
- evento;
- cuidado doméstico;
- viaje.

El progreso no se borra.

---

# 16. Finalización

APR06 puede alcanzarse cuando existe evidencia suficiente de autonomía real.

No requiere examen universal.

Puede existir reconocimiento social por:

- mentor;
- clientes;
- compañeros;
- resultados.

---

# 17. Maestro excepcional

La excelencia superior depende de:

- práctica;
- talento;
- especialización;
- experiencia;
- calidad de trabajo;
- reputación.

No forma parte de la progresión básica APR.

---

# 18. Conocimiento tácito

Parte del oficio puede ser difícil de convertir en instrucciones explícitas.

El sistema puede representar esto mediante necesidad de:

- observación;
- práctica;
- mentoría.

La IA no debe regalar conocimiento técnico completo en una sola conversación.

---

# 19. NPC generado

Un NPC persistente con profesión debe recibir:

- historial plausible de aprendizaje;
- nivel de capacidad coherente;
- relación pasada si es relevante.

No necesita biografía detallada completa.

---

# 20. LOD

En bajo detalle puede persistir:

- learning_state;
- mentor;
- occupation;
- recent_training_opportunity;
- evidence.

En alto detalle se materializan tareas concretas.

---

## Regla final

**En Treskal un oficio se aprende haciendo trabajo real bajo ojos más expertos; el tiempo ayuda, pero no sustituye a la práctica ni al juicio.**
