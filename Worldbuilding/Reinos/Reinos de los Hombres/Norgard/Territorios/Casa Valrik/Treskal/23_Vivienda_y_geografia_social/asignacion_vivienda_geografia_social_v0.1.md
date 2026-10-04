# Treskal — asignación de vivienda y geografía social v0.1

## Estado

**DISEÑO DE SIMULACIÓN APROBADO — SIN CLASES URBANAS RÍGIDAS**

## Objetivo

Asignar hogares a edificios y subzonas de forma coherente sin convertir Treskal en barrios de riqueza perfectamente segregados.

---

# 1. Principio

La vivienda de un hogar debe depender de una combinación de:

- tamaño del hogar;
- oficio;
- lugar de trabajo;
- capacidad económica;
- disponibilidad;
- necesidad de espacio;
- vínculos familiares;
- actividad doméstica;
- World State.

No se decide únicamente por “clase social”.

---

# 2. Mezcla urbana

Treskal debe mantener mezcla social.

En una misma calle pueden coexistir:

- taller próspero;
- vivienda modesta;
- comercio;
- posada;
- casa subdividida;
- artesano reconocido.

La diferencia se expresa mediante:

- tamaño;
- estado;
- materiales;
- parcela;
- mobiliario;
- herramientas;
- empleados;
- almacenamiento.

No mediante muros invisibles de clase.

---

# 3. Proximidad al trabajo

Es deseable, no obligatoria.

Favorecer:

- artesanos cerca de T04;
- portuarios cerca de T07;
- trabajadores de T08 en zonas con buen acceso a C07;
- comerciantes cerca de T03/T07;
- personal administrativo cerca de T05/T06.

Pero puede existir desplazamiento diario.

---

# 4. Coste de desplazamiento

La asignación puede considerar:

- distancia;
- puente;
- pendiente;
- tráfico;
- hora;
- clima.

Un hogar puede aceptar mayor distancia si obtiene:

- más espacio;
- mejor vivienda;
- vínculo familiar;
- acceso a patio/taller.

---

# 5. Necesidad de espacio

## Hogar ordinario

Prioriza:

- capacidad residencial;
- cocina;
- descanso;
- almacenamiento doméstico.

## Hogar artesanal

Puede necesitar:

- U02;
- patio;
- taller;
- almacén.

## Hogar de transportista

Puede valorar:

- establo;
- acceso de carro;
- borde urbano.

## Hogar vinculado a posada

Puede integrarse en U05.

---

# 6. Capacidad económica

No se fija moneda ni renta.

El motor puede utilizar una variable de recursos o solvencia.

Más capacidad económica puede permitir:

- más espacio;
- mejor mantenimiento;
- ubicación deseada;
- mejores acabados;
- dependencias adicionales.

No garantiza una posición institucional.

---

# 7. Prestigio

Riqueza y prestigio no son idénticos.

Un maestro ebanista puede tener:

- gran reputación;
- buen taller;
- vivienda sólida

sin pertenecer a nobleza.

Un funcionario puede poseer prestigio institucional sin gran patrimonio.

---

# 8. Nobleza

La Casa Valrik y visitantes nobles tienen necesidades propias.

No se crea un “barrio noble” obligatorio.

La sede Valrik está en Z07, pero otros hogares acomodados pueden existir en distintas partes de la ciudad.

---

# 9. Vivienda modesta

Puede situarse en:

- Z13;
- calles secundarias;
- partes de Z05;
- periferias;
- edificios subdivididos.

No debe equipararse automáticamente a:

- suciedad;
- delincuencia;
- abandono.

---

# 10. Vivienda portuaria

Z10 puede contener:

- marineros;
- familias vinculadas al puerto;
- posadas;
- comerciantes.

No toda la población portuaria es transitoria.

---

# 11. Vivienda de trabajadores de Astilleros Reales

Los trabajadores ordinarios no viven dentro de T08 por defecto.

Deben poder residir en:

- Z13;
- Z05;
- Z10;
- periferias conectadas.

El acceso a C07 influye en el recorrido laboral.

---

# 12. Hogares multigeneracionales

Pueden necesitar:

- más espacio;
- anexos;
- división interna;
- varias unidades dentro del mismo edificio.

La vivienda puede crecer o subdividirse con el tiempo.

---

# 13. Cambio de vivienda

Un hogar puede mudarse por:

- matrimonio;
- crecimiento;
- muerte;
- empleo;
- incendio;
- prosperidad;
- pérdida económica;
- conflicto;
- cambio de negocio.

La mudanza altera World State.

---

# 14. Edificio y hogar

Un edificio puede contener:

- un hogar;
- varios hogares;
- negocio + hogar;
- taller + hogar;
- habitaciones alquiladas o cedidas si el futuro sistema jurídico/económico lo define.

El contrato legal exacto de ocupación queda pendiente.

---

# 15. Propiedad

World State puede registrar:

- owner_ref;
- occupant_refs.

Pero no se define todavía:

- herencia;
- alquiler;
- arrendamiento;
- desahucio;
- compraventa legal.

Esos mecanismos pertenecen a la futura Ley/economía institucional de Norgard.

---

# 16. Daño y desplazamiento

Incendio o inundación pueden dejar temporalmente un hogar sin vivienda.

El sistema debe poder representar:

- alojamiento familiar;
- posada;
- traslado provisional;
- reconstrucción.

No se resuelve instantáneamente.

---

# 17. Generación inicial

Orden recomendado:

1. materializar edificios residenciales;
2. determinar unidades residenciales;
3. generar hogares;
4. asignar necesidades;
5. asignar ubicación compatible;
6. crear personas.

No crear primero 15.000 NPC y después “meterlos” en casas.

---

## Regla final

**La geografía social de Treskal surge de hogares, oficios, espacio y recursos; no de pintar un barrio rico y otro pobre.**
