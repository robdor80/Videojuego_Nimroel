# Treskal — ciclo de residuos, recogida y destino v0.1

> **MIGRADO A NIMROEL CORE — documentación derivada con override local explícito.** La autoridad normativa de WASTE / WST reside en `Worldbuilding/Sistemas/Nimroel Core/04_Material_y_riesgo/residuos_saneamiento_ciclo_v0.1.md`. Treskal conserva únicamente su infraestructura y organización sanitaria preindustrial; ante conflicto prevalece el Core.

## Estado

**DISEÑO DE WORLD STATE APROBADO**

## Objetivo

Cerrar el ciclo:

**generación → almacenamiento temporal → recogida → transporte → reutilización/eliminación**

---

# 1. Estados

## WST01 — generated

Residuo recién producido.

## WST02 — contained

Recogido en punto o recipiente temporal.

## WST03 — awaiting_collection

Pendiente de retirada.

## WST04 — in_transport

En movimiento.

## WST05 — recovered_or_reused

Aprovechado.

## WST06 — disposed

Retirado a destino final.

## WST07 — problematic_accumulation

La carga supera capacidad o tiempo aceptable.

---

# 2. Campos mínimos

Una carga relevante puede registrar:

- waste_id_or_batch;
- waste_type;
- source_ref;
- location_ref;
- quantity_class;
- state;
- container_ref_if_any;
- collection_need;
- destination_ref_if_known;
- hazard_flags;
- created_time;
- last_update_time.

---

# 3. Cantidad agregada

La mayoría de residuos pueden tratarse por lote.

No se individualiza cada espina de pescado o trozo de basura.

---

# 4. Capacidad

Un punto o contenedor tiene capacidad finita.

Si se supera:

- WST07;
- desbordamiento;
- necesidad urgente de retirada.

---

# 5. Retirada programada

Puede existir rutina habitual.

No se fija:

- frecuencia exacta;
- calendario;
- cuerpo profesional.

La demanda y el lugar determinan prioridad.

---

# 6. Trabajo

La retirada puede generar empleo o tareas dentro de:

- hogares;
- negocios;
- mercado;
- transporte;
- mantenimiento urbano.

No se presupone servicio municipal moderno.

---

# 7. Transporte

Una carga de residuos usa:

- persona;
- recipiente;
- TR03/TR04 u otro medio compatible;
- ruta.

Compite por espacio con otros movimientos urbanos.

---

# 8. Reutilización

Solo ocurre si existe:

- uso válido;
- receptor;
- ruta;
- capacidad.

No porque el sistema prefiera “reciclar”.

---

# 9. Incendio y residuos

Algunos residuos de madera o combustible pueden elevar FIRE risk.

Otros residuos húmedos u orgánicos no se tratan igual.

El riesgo depende del tipo.

---

# 10. Persistencia

WST07 no desaparece al descargar zona.

La limpieza real debe reducir la carga.

---

# 11. LOD

En bajo detalle puede guardarse:

- waste_pressure_by_area;
- critical_batches;
- collection_capacity.

En alto detalle se materializan residuos coherentes con esa presión.

---

## Regla final

**La limpieza visible de Treskal debe ser el resultado de una cadena logística de retirada, no de borrar objetos al cambiar de escena.**
