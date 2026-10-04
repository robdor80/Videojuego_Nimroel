# Treskal — construcción, ampliación y cambio de uso v0.1

## Estado

**DISEÑO URBANO/JUGABLE APROBADO — CRECIMIENTO PERSISTENTE**

## Objetivo

Definir cómo un edificio de Treskal puede:

- construirse;
- ampliarse;
- subdividirse;
- cambiar de uso;
- quedar vacío;
- demolerse;
- reconstruirse.

Sin convertir el crecimiento urbano en aparición instantánea de edificios.

---

# 1. Principio

Un edificio nuevo necesita:

- parcela/espacio compatible;
- materiales;
- trabajo;
- tiempo;
- acceso;
- causa funcional.

No se construye porque el sistema “necesita más casas” sin proceso físico.

---

# 2. Estados de proyecto

## BUILD01 — proposed

Existe intención o necesidad.

## BUILD02 — preparing_site

Se prepara espacio, materiales o acceso.

## BUILD03 — foundations_or_initial_structure

Comienza la obra física.

## BUILD04 — structural_work

La estructura principal está en construcción.

## BUILD05 — enclosure_and_services

Se completan cerramientos e instalaciones preindustriales compatibles.

## BUILD06 — fit_out

Se acondiciona para su uso.

## BUILD07 — usable

Puede cumplir función.

## BUILD08 — paused

La obra está detenida.

## BUILD09 — cancelled

No continuará.

## BUILD10 — demolition_or_clearance

Se desmonta/retira estructura existente.

---

# 3. Proyecto de obra

Una obra relevante puede registrar:

- project_id;
- site_ref;
- target_building_id_if_existing;
- target_type_U;
- purpose;
- state;
- material_requirements;
- reserved_materials;
- worker_refs;
- transport_requirements;
- access_effects;
- progress;
- start_time;
- completion_time_if_known.

---

# 4. Edificio nuevo

Al completarse:

- recibe building_id persistente;
- se vincula a parcela/localización;
- entra en World State.

La seed puede ayudar a materializar detalles compatibles.

Después manda el building_id, no la seed.

---

# 5. Ampliación

Un edificio existente puede incorporar:

- estancia;
- planta adicional cuando tipología y estructura lo permitan;
- patio cubierto;
- taller;
- almacén;
- anexo.

No todas las ampliaciones son posibles.

Dependen de:

- espacio;
- estructura;
- materiales;
- uso;
- entorno.

---

# 6. Subdivisión

Un U01/U03/U04 u otro edificio compatible puede dividirse en:

- varias unidades domésticas;
- vivienda + negocio;
- dependencias separadas.

La subdivisión modifica:

- accesos;
- ocupantes;
- capacidad;
- privacidad.

No crea edificio nuevo si la identidad estructural sigue siendo una sola.

---

# 7. Cambio de uso

Un building_id puede conservarse y cambiar de:

- vivienda;
- comercio;
- taller;
- almacén;
- alojamiento;
- otro uso compatible.

Puede requerir obra previa.

Ejemplo:

una vivienda no se convierte en gran herrería sin adaptar espacio, ventilación y riesgo.

---

# 8. Vacío

Un edificio puede quedar:

- desocupado;
- sin negocio;
- en espera de nuevo uso.

Vacío no significa:

- abandonado;
- libre para cualquiera;
- sin propietario.

---

# 9. Demolición

Puede ocurrir por:

- daño;
- decisión;
- seguridad;
- reconstrucción;
- cambio urbano.

Los materiales recuperables pueden:

- reutilizarse;
- venderse;
- almacenarse;
- desecharse.

No desaparecen necesariamente.

---

# 10. Reconstrucción

Tras incendio o destrucción:

puede:

- reconstruirse igual;
- modificarse;
- cambiar de uso;
- permanecer vacío.

La decisión no es automática.

---

# 11. Materiales

Una obra puede necesitar:

- piedra;
- madera;
- metal;
- pizarra;
- cuerda;
- otros materiales compatibles.

La disponibilidad depende de stock y logística.

---

# 12. Mano de obra

Puede requerir:

- O13 construcción/mantenimiento;
- O01 madera;
- O11 metal;
- transporte;
- especialistas.

La falta de una especialidad puede detener fase concreta.

---

# 13. Tráfico y espacio

Una obra puede ocupar:

- calle;
- patio;
- carros;
- materiales;
- andamios/estructuras auxiliares compatibles.

Esto puede alterar:

- navegación;
- ruido;
- actividad vecinal.

---

# 14. Presión residencial

ResidentialPressure = high puede aumentar probabilidad de:

- subdivisión;
- ocupación de espacio existente;
- ampliación;
- nuevas construcciones.

No crea automáticamente densidad infinita.

La tipología y el espacio siguen imponiendo límites.

---

# 15. Crecimiento orgánico

El crecimiento de Treskal debe respetar:

- T;
- Z;
- C;
- densidades;
- usos;
- riesgos;
- topología.

No se crean barrios nuevos completos sin decisión de diseño/canon.

---

# 16. Edificios singulares

No se generan proceduralmente:

- La Casa;
- Justicia;
- Astilleros Reales;
- grandes landmarks.

Cualquier alteración estructural importante requiere decisión autoral.

---

# 17. Propiedad

Quién puede encargar o autorizar una obra depende del futuro sistema de:

- propiedad;
- administración;
- ley.

Este contrato solo modela el proceso físico.

---

# 18. Offscreen

Una obra puede avanzar fuera de escena si siguen disponibles:

- trabajadores;
- materiales;
- acceso;
- tiempo.

No avanza si:

- está pausada;
- faltan recursos;
- evento lo impide.

---

# 19. Visual

El estado BUILD debe reflejarse en:

- materiales visibles;
- estructura;
- ruido;
- trabajadores;
- accesos;
- polvo/suciedad contextual.

No debe parecer terminada antes de estar usable.

---

# 20. Guardado

El progreso de una obra relevante persiste.

Recargar no:

- completa;
- borra;
- reinicia

la construcción.

---

## Regla final

**Treskal crece construyendo de verdad: espacio, materiales, trabajadores y tiempo convierten una necesidad en un edificio.**
