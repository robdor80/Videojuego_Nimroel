# Nimroel Core — salud, lesiones, enfermedad y recuperación v0.1

## Autoridad

**CORE UNIVERSAL — namespaces HLTH / HCOND / HTRT / OUTB**

Este sistema define la fisiología jugable genérica.

No define:

- tradición cultural de curación;
- nombres de enfermedades propias de una cultura;
- flora medicinal concreta;
- instituciones médicas;
- medicina sobrenatural;
- diferencias fisiológicas específicas de pueblos no humanos.

Esas capas pertenecen a defaults culturales o sistemas posteriores.

---

## 1. Principio

La salud no es una barra de puntos de vida.

Una persona puede acumular varias condiciones simultáneas:

- heridas;
- dolor;
- sangrado;
- infección;
- enfermedad;
- agotamiento;
- deshidratación;
- secuelas.

Cada condición persiste hasta que:

- mejora;
- se resuelve;
- se vuelve crónica;
- produce otra consecuencia;
- contribuye a una muerte válida.

---

## 2. Estado general

### HLTH01 — well
Sin limitación sanitaria relevante.

### HLTH02 — limited
Existe una condición que limita parte de la actividad.

### HLTH03 — serious
La salud exige atención, reposo o adaptación importante.

### HLTH04 — critical
Existe riesgo inmediato o alto de muerte o deterioro grave.

### HLTH05 — recovering
La amenaza aguda ha pasado, pero la recuperación sigue activa.

### HLTH06 — chronic_impairment
Persiste una secuela o condición duradera.

HLTH es resumen funcional.

No sustituye los registros HCOND concretos.

---

## 3. Tipos genéricos de condición

### Lesiones

- HCOND01 — superficial_wound;
- HCOND02 — deep_or_penetrating_wound;
- HCOND03 — blunt_trauma;
- HCOND04 — fracture_or_dislocation;
- HCOND05 — burn_or_scald;
- HCOND06 — crush_injury;
- HCOND07 — sprain_strain_soft_tissue;
- HCOND08 — head_injury;
- HCOND09 — cold_or_heat_exposure.

### Enfermedad y deterioro

- HCOND10 — respiratory_illness_syndrome;
- HCOND11 — gastrointestinal_illness_syndrome;
- HCOND12 — febrile_systemic_illness;
- HCOND13 — local_or_wound_infection;
- HCOND14 — severe_systemic_infection;
- HCOND15 — poisoning_or_toxic_exposure;
- HCOND16 — dehydration_health_consequence;
- HCOND17 — undernutrition_health_consequence;
- HCOND18 — pregnancy_or_birth_complication;
- HCOND19 — other_supported_condition.

Un HCOND no es necesariamente el diagnóstico que conoce el NPC.

El motor puede conocer más que el personaje.

---

## 4. Severidad

Cada condición puede tener:

- minor;
- moderate;
- serious;
- critical.

La severidad no se deriva solo del tipo.

Una quemadura pequeña y una quemadura extensa siguen siendo HCOND05, pero no tienen el mismo riesgo.

---

## 5. Campos fisiológicos posibles

Una condición puede registrar cuando proceda:

- body_region;
- onset_time;
- cause_refs;
- severity;
- trajectory;
- bleeding_state;
- pain_state;
- consciousness_effect;
- mobility_effect;
- hand_or_limb_function_effect;
- breathing_effect;
- contamination_or_infection_risk;
- fever_or_temperature_effect;
- hydration_effect;
- nutrition_effect;
- sleep_rest_effect;
- contagious_or_exposure_model;
- treatment_refs;
- complication_refs;
- recovery_requirements;
- permanent_sequela_refs;
- death_event_ref_if_any.

No todos los campos son necesarios en todas las condiciones.

---

## 6. Sangrado

Puede ser:

- none;
- minor;
- controlled;
- ongoing;
- severe;
- life_threatening.

El control del sangrado necesita:

- presión;
- vendaje;
- procedimiento;
- o causa material equivalente.

No se detiene automáticamente porque una escena termine.

---

## 7. Dolor

Puede ser:

- none;
- mild;
- moderate;
- severe;
- overwhelming.

El dolor puede afectar:

- atención;
- descanso;
- movilidad;
- trabajo;
- diálogo;
- decisión.

Dolor no equivale automáticamente a daño estructural grave y daño grave puede existir con dolor limitado.

---

## 8. Conciencia

Una lesión o enfermedad puede producir:

- alert;
- confused;
- reduced;
- unconscious.

La pérdida de conciencia requiere una causa física válida.

La IA no puede desmayar a un NPC solo por dramatismo.

---

## 9. Infección

Una herida puede infectarse.

El riesgo depende de:

- tipo de herida;
- contaminación;
- profundidad;
- tiempo;
- limpieza;
- materiales;
- tratamiento;
- estado previo;
- entorno.

No toda herida se infecta.

La infección puede:

- permanecer local;
- extenderse;
- deteriorar el estado general;
- matar.

---

## 10. Enfermedad

El motor puede representar enfermedad aunque los personajes no conozcan su causa científica.

Una enfermedad puede tener:

- periodo de inicio;
- síntomas;
- gravedad;
- contagiosidad;
- vías de exposición;
- recuperación;
- complicaciones.

La percepción de los NPC se basa en:

- signos;
- experiencia;
- historial;
- contacto conocido;
- conocimiento cultural.

No se concede diagnóstico moderno omnisciente.

---

## 11. Vías de exposición

Cuando una condición es transmisible o ambiental puede usar:

- respiratory_proximity;
- direct_contact;
- contaminated_food_or_water;
- contaminated_wound_or_material;
- animal_or_vector_exposure;
- toxic_material;
- unknown_or_not_yet_resolved.

La existencia de una vía de exposición no garantiza contagio.

---

## 12. Brotes

OUTB modela agrupación sanitaria persistente.

- OUTB01 — isolated_case;
- OUTB02 — suspected_cluster;
- OUTB03 — local_outbreak;
- OUTB04 — spreading_outbreak;
- OUTB05 — contained;
- OUTB06 — declining;
- OUTB07 — resolved.

Un brote necesita casos y vías plausibles.

No aparece porque el guion quiera una epidemia.

---

## 13. Tratamiento

HTRT describe episodios de atención.

- HTRT01 — requested;
- HTRT02 — waiting;
- HTRT03 — assessment;
- HTRT04 — active_care;
- HTRT05 — monitoring;
- HTRT06 — completed;
- HTRT07 — interrupted;
- HTRT08 — unavailable_or_failed_to_start.

Un tratamiento puede:

- estabilizar;
- reducir riesgo;
- aliviar síntomas;
- favorecer recuperación;
- evitar complicaciones;
- fracasar.

No garantiza curación.

---

## 14. Acciones genéricas de cuidado

Cuando son adecuadas y existe capacidad, pueden incluir:

- controlar sangrado;
- limpiar una herida;
- retirar suciedad superficial;
- cubrir o vendar;
- inmovilizar;
- colocar férula;
- reducir movimiento;
- proporcionar reposo;
- dar agua o alimento cuando sea seguro;
- proporcionar calor o enfriamiento;
- vigilar signos de empeoramiento;
- ayudar en respiración o postura;
- aislar una posible exposición;
- aplicar un material medicinal canónico;
- transportar a un lugar más seguro;
- asistencia de parto;
- procedimiento invasivo limitado si existe competencia.

---

## 15. Procedimientos de alto riesgo

Algunas situaciones pueden requerir, si la cultura y capacidad lo permiten:

- cierre de heridas;
- extracción de cuerpo extraño accesible;
- recolocación de articulación;
- reducción e inmovilización de fractura;
- drenaje u otra intervención limitada;
- amputación de último recurso.

Estos actos:

- consumen tiempo;
- materiales;
- competencia;
- pueden causar dolor;
- pueden fallar;
- pueden empeorar el cuadro;
- no usan anestesia moderna por defecto.

La existencia mecánica de una posibilidad no significa que todas las culturas la practiquen.

---

## 16. Recuperación

Una condición puede estar:

- worsening;
- stable;
- improving;
- recovering;
- resolved;
- chronic.

La recuperación puede depender de:

- gravedad;
- tiempo;
- descanso;
- hidratación;
- alimentación;
- calor/entorno;
- higiene;
- tratamiento;
- competencia de quien atiende;
- edad/desarrollo;
- condiciones previas;
- complicaciones.

No existe restauración instantánea por dormir unas horas.

---

## 17. Secuelas

Una lesión o enfermedad importante puede dejar:

- cicatriz;
- dolor persistente;
- limitación de movilidad;
- pérdida de función;
- debilidad;
- sensibilidad;
- necesidad de cuidado;
- cambio de capacidad laboral.

Una secuela no desaparece por bajar LOD.

---

## 18. Necesidades físicas

NEED puede producir HCOND cuando una necesidad permanece gravemente desatendida.

Ejemplos:

- hidratación insuficiente → HCOND16;
- alimentación insuficiente prolongada → HCOND17;
- frío/calor extremo → HCOND09.

NEED sigue registrando la necesidad.

HLTH registra la consecuencia sanitaria.

---

## 19. Descanso

REST influye en recuperación.

Dormir no cura automáticamente:

- fracturas;
- infección;
- heridas críticas;
- enfermedad grave.

La recuperación puede exigir reposo continuado.

---

## 20. Higiene y saneamiento

WASTE e higiene pueden modificar presión de riesgo.

La acumulación:

- no crea enfermedad automáticamente;
- puede aumentar exposición plausible.

Agua contaminada puede participar en enfermedad si existe:

- causa;
- ruta;
- consumo/exposición;
- resolución del motor.

---

## 21. Accidentes

ACC puede crear uno o más HCOND.

El estado ACC03/04/05 no sustituye la lesión.

Ejemplo:

una caída puede producir simultáneamente:

- HCOND03;
- HCOND04;
- HCOND08.

---

## 22. Embarazo y parto

PREG04 puede generar HCOND18 si existe complicación.

PREG05 o PREG06 pueden coexistir con:

- recuperación;
- sangrado;
- infección;
- debilidad;
- otras condiciones.

No toda gestación o parto produce complicación.

---

## 23. Recién nacidos

Un recién nacido puede:

- estar sano;
- necesitar cuidado;
- enfermar;
- sufrir una complicación;
- morir.

No se fijan aquí probabilidades por población.

---

## 24. Capacidad funcional

HLTH y HCOND pueden alterar:

- EMP;
- APR;
- CHORE;
- CARE;
- MOVE;
- RES;
- AGEN;
- REST;
- ATTN;
- DEC.

La consecuencia concreta depende del tipo y gravedad.

No toda enfermedad produce incapacidad total.

---

## 25. Muerte

Una condición puede contribuir a una muerte válida.

La muerte no se produce por una barra genérica llegando a cero.

Puede derivar de:

- sangrado fatal;
- lesión incompatible con la vida;
- daño crítico;
- infección sistémica grave;
- exposición extrema;
- intoxicación;
- complicación de parto;
- enfermedad severa;
- combinación de factores.

La muerte se registra en el sistema propietario de mortalidad/restos.

La IA no decide por sí sola que una persona muere.

---

## 26. Off-screen

El LOD puede abstraer:

- revisiones;
- cuidados;
- evolución;
- exposición;
- recuperación.

Pero utiliza las mismas causas y probabilidades.

No existe “curación fuera de cámara” automática.

---

## 27. Conocimiento

Debe distinguirse:

- condición real;
- síntomas visibles;
- diagnóstico o creencia;
- conocimiento del paciente;
- conocimiento del cuidador;
- información pública.

Un diagnóstico equivocado no cambia la condición real.

---

## 28. IA

La IA puede:

- describir síntomas autorizados;
- proponer una respuesta coherente con conocimiento y oficio;
- expresar dolor, malestar o limitación.

No puede:

- crear una enfermedad;
- resolver una lesión;
- declarar una infección;
- inventar un remedio;
- curar;
- matar;
- crear una secuela;
- alterar HLTH/HCOND/HTRT/OUTB.

---

## 29. Sistemas sobrenaturales

Core no presupone curación sobrenatural.

Si existe en algún canon:

- necesita sistema propio;
- debe declarar efectos;
- debe modificar World State mediante contrato válido.

No existe “magia curativa genérica” por defecto.

---

## Regla final

**La salud de Nimroel es causal y persistente: el cuerpo puede empeorar, estabilizarse, recuperarse o quedar marcado, y ninguna escena narrativa sustituye ese proceso.**
