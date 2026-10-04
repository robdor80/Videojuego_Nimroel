# Treskal — desgaste, mantenimiento y reparación v0.1

## Estado

**DISEÑO DE WORLD STATE APROBADO — CIUDAD MANTENIDA, NO ESTÁTICA**

## Objetivo

Representar deterioro y reparación de:

- edificios;
- calles;
- talleres;
- muelles;
- carros;
- instalaciones;
- infraestructura.

Sin convertir Treskal en una ciudad permanentemente arruinada ni mágicamente autorreparable.

---

# 1. Principio

Treskal está:

- trabajada;
- usada;
- razonablemente mantenida.

Por tanto debe mostrar:

- desgaste;
- reparaciones;
- mantenimiento;
- daños contextuales.

No:

- abandono general;
- perfección permanente.

---

# 2. Estados técnicos de condición

## COND01 — maintained

Funcionamiento normal con desgaste compatible.

## COND02 — worn

Desgaste visible, aún funcional.

## COND03 — damaged

Daño que afecta aspecto o función.

## COND04 — impaired

Funciona parcialmente o con restricciones.

## COND05 — unsafe

Uso normal no recomendable o bloqueado.

## COND06 — under_repair

Intervención activa.

## COND07 — destroyed_or_unusable

No puede cumplir su función principal.

No todo elemento necesita recorrer todos los estados.

---

# 3. Causas de desgaste

Puede proceder de:

- uso;
- tráfico;
- lluvia;
- humedad;
- sal marina;
- viento;
- fuego;
- agua;
- accidente;
- negligencia;
- tiempo.

No existe deterioro arbitrario por “tick” sin contexto.

---

# 4. Calles

El estado puede depender de:

- firme;
- tráfico;
- carros pesados;
- ganado;
- lluvia;
- drenaje;
- mantenimiento.

Consecuencias:

- barro;
- baches;
- menor velocidad;
- desvíos;
- reparación.

---

# 5. Edificios

Pueden requerir:

- cubierta;
- carpintería;
- piedra;
- revocos/acabados compatibles;
- drenaje;
- puertas;
- ventanas.

Un edificio en buen estado puede mostrar uso sin parecer nuevo.

---

# 6. Talleres

El mantenimiento incluye:

- herramientas;
- bancos;
- ventilación;
- superficies;
- almacenaje;
- seguridad frente a fuego.

Una herramienta rota afecta trabajo real.

---

# 7. Puerto y muelles

El entorno marítimo/fluvial exige mantenimiento por:

- humedad;
- uso;
- golpes;
- carga;
- agua;
- viento.

Puede afectar:

- plataformas;
- amarres;
- almacenes;
- accesos.

No se fija ingeniería exacta hasta cartografía/arquitectura detallada.

---

# 8. Puente

El Puente de los Gemelos es infraestructura crítica.

Puede requerir:

- inspección;
- reparación;
- control de carga;
- cierre parcial.

La geometría exacta sigue pendiente.

---

# 9. Materiales

Una reparación necesita materiales plausibles.

Ejemplos:

- madera;
- piedra;
- metal;
- cuerda;
- piezas;
- otros materiales canónicos.

No aparecen automáticamente.

---

# 10. Mano de obra

Puede requerir:

- O01 madera;
- O11 metal;
- O13 construcción/mantenimiento;
- transporte;
- especialistas.

La disponibilidad laboral afecta duración.

---

# 11. Repair job

Una reparación relevante puede registrar:

- repair_id;
- target_ref;
- damage_ref;
- requested_time;
- state;
- required_materials;
- reserved_materials;
- worker_refs;
- access_effects;
- progress;
- completion_time.

---

# 12. Estados de reparación

## requested

Se reconoce la necesidad.

## waiting_resources

Faltan materiales/trabajadores.

## scheduled

Puede comenzar.

## active

Trabajo en curso.

## paused

Interrumpido.

## completed

Función restaurada hasta el grado definido.

## abandoned

No se continúa.

---

# 13. Reparación no equivale a restauración total

Un elemento reparado puede conservar:

- cicatriz;
- material distinto;
- parche;
- desgaste previo.

La reparación funcional no obliga a “volver a asset nuevo”.

---

# 14. Prioridad

Puede aumentar por:

- peligro;
- bloqueo;
- infraestructura crítica;
- actividad económica;
- institución.

Un agujero menor no recibe la misma urgencia que un puente afectado.

---

# 15. Propiedad y responsabilidad

El World State puede registrar quién:

- posee;
- usa;
- mantiene;
- encarga reparación.

Quién está legalmente obligado a pagar queda sujeto al futuro sistema jurídico/económico.

---

# 16. Obras y circulación

Una reparación puede:

- cerrar paso;
- reducir anchura;
- generar ruido;
- mover materiales;
- ocupar trabajadores.

Debe modificar navegación.

---

# 17. Visual

El renderizado debe derivar de condición real:

- tablón nuevo;
- zona chamuscada;
- andamio compatible;
- parche;
- carga de materiales;
- barro.

No se aplican decals aleatorios contradictorios con estado.

---

# 18. Sonido

Una obra activa puede generar:

- golpes;
- sierras manuales;
- carros;
- voces.

Solo si el trabajo está ocurriendo.

---

# 19. Offscreen

La reparación puede progresar fuera de escena si:

- trabajadores;
- materiales;
- acceso;
- tiempo

siguen disponibles.

No progresa durante un bloqueo incompatible.

---

# 20. Ruina

COND07 no implica abandono permanente.

Puede conducir a:

- reconstrucción;
- cambio de uso;
- retirada.

La decisión depende de importancia y World State.

---

## Regla final

**Treskal se conserva porque la gente la repara; cada parche visible debe tener una causa y cada reparación un coste real de tiempo, material y trabajo.**
