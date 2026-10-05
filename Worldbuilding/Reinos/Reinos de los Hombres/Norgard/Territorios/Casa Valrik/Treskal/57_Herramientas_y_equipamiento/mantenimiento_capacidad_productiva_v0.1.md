# Treskal — mantenimiento de herramientas y capacidad productiva v0.1

> **MIGRADO A NIMROEL CORE — documentación derivada.** La autoridad normativa de TOOL / WS reside en `Worldbuilding/Sistemas/Nimroel Core/04_Material_y_riesgo/herramientas_estaciones_capacidad_v0.1.md`. Este archivo conserva explicación y ejemplos de Treskal; ante conflicto prevalece el Core.

## Estado

**DISEÑO DE SIMULACIÓN APROBADO**

## Objetivo

Conectar el estado del equipo con:

- BIZ;
- EMP;
- COM;
- calidad;
- reparaciones.

---

# 1. Capacidad efectiva

Puede derivarse de:

- trabajadores capaces;
- herramientas funcionales;
- estaciones disponibles;
- materiales;
- tiempo;
- estado del negocio.

La capacidad es el mínimo práctico entre cuellos de botella relevantes.

---

# 2. Mantenimiento preventivo

Un negocio competente puede dedicar tiempo a:

- revisar;
- limpiar;
- afilar;
- ajustar.

Ese tiempo reduce producción inmediata pero evita fallos.

No se fija fórmula económica.

---

# 3. Deuda de mantenimiento

Si se pospone demasiado:

puede aumentar:

- TOOL02/03;
- riesgo de TOOL04/06;
- lentitud;
- errores.

No se genera avería aleatoria sin relación con uso/estado.

---

# 4. Herramienta crítica

Una herramienta puede marcarse como critical_for_task.

Si falta:

la tarea asociada no progresa aunque existan otras herramientas.

---

# 5. Herramienta sustituible

Otra herramienta compatible puede permitir:

- continuar más lento;
- calidad distinta;
- tarea parcial.

La compatibilidad la define el oficio.

---

# 6. Reparación

Puede usar:

- repair job;
- COM;
- proveedor especializado;
- trabajador interno capaz.

Al terminar:

el estado mejora al nivel justificable.

No siempre vuelve a TOOL01.

---

# 7. Stock de repuestos

Piezas y consumibles pueden formar parte de stock real.

No se inventan componentes cuando se rompe algo.

---

# 8. Efecto en encargos

Un COM puede:

- pausarse;
- retrasarse;
- cambiar método;
- necesitar renegociación

si falla equipo crítico.

La causa queda registrada.

---

# 9. Offscreen

El mantenimiento puede resolverse agregadamente si:

- equipo;
- trabajador;
- tiempo;
- material

existen.

---

## Regla final

**El estado del taller debe poder explicar por qué hoy produce, por qué mañana se retrasa y qué necesita para volver a funcionar.**
