# Treskal — herramientas, equipo y estaciones de trabajo v0.1

## Estado

**DISEÑO ECONÓMICO/JUGABLE APROBADO — PRODUCCIÓN CON EQUIPO REAL**

## Objetivo

Definir cómo herramientas y equipo participan en:

- oficio;
- calidad;
- capacidad;
- mantenimiento;
- propiedad;
- préstamo;
- avería.

Sin introducir mecanización industrial.

---

# 1. Principio

Un trabajador capaz puede no poder ejecutar una tarea si carece de:

- herramienta;
- equipo;
- espacio;
- material.

La habilidad no sustituye al equipo físico.

---

# 2. Herramientas manuales

El canon de madera ya permite herramientas coherentes como:

- hachas;
- azuelas;
- sierras;
- formones;
- gubias;
- cepillos;
- barrenas;
- mazos;
- herramientas de medición y marcado.

Otros oficios usan herramientas compatibles con su tecnología.

La presencia de herramienta manual no implica mecanización industrial.

---

# 3. Función técnica

Una herramienta puede registrar:

- tool_id;
- function;
- owner_ref;
- possessor_ref;
- workplace_ref;
- condition;
- maintenance_state;
- specialization_if_any.

No toda herramienta ordinaria necesita ID individual hasta ser relevante.

---

# 4. Estados de condición

## TOOL01 — functional

Uso normal.

## TOOL02 — worn

Funciona, pero con desgaste.

## TOOL03 — degraded

Función reducida o peor precisión.

## TOOL04 — damaged

Necesita reparación para uso fiable.

## TOOL05 — under_repair

No disponible durante mantenimiento.

## TOOL06 — unusable

No puede cumplir su función.

## TOOL07 — retired_or_repurposed

Sale de uso ordinario.

---

# 5. Desgaste

Puede depender de:

- frecuencia;
- material trabajado;
- fuerza;
- humedad;
- corrosión;
- mal uso;
- mantenimiento.

No se degrada cada herramienta con el mismo ritmo.

---

# 6. Mantenimiento

Puede incluir:

- limpieza;
- secado;
- afilado;
- ajuste;
- sustitución de pieza;
- reparación.

El tipo exacto depende de herramienta y canon material.

---

# 7. Herramienta desafilada o degradada

Puede producir:

- trabajo más lento;
- peor acabado;
- mayor esfuerzo;
- más errores;
- imposibilidad de tarea fina.

No reduce automáticamente toda producción a cero.

---

# 8. Avería

Una herramienta rota puede:

- detener una fase;
- obligar a usar otra;
- generar COM de reparación;
- requerir O11/O01 según el caso.

No aparece un reemplazo automático.

---

# 9. Propiedad

Puede pertenecer a:

- trabajador;
- maestro;
- negocio;
- hogar;
- institución.

Quien la usa no se convierte en propietario.

---

# 10. Herramienta de taller

Algunas herramientas pueden estar asociadas al workplace_ref.

Un trabajador autorizado puede usarlas por rol.

Si cambia de empleo:

no se las lleva salvo transferencia válida.

---

# 11. Préstamo

Una herramienta puede prestarse.

Debe poder enlazarse con:

- OWN02;
- PLEDGE;
- expected_return;
- condition_before;
- condition_after.

El prestatario puede devolverla desgastada o dañada.

---

# 12. Estación de trabajo

Una tarea puede requerir además:

- banco;
- fragua/instalación futura;
- superficie;
- sujeción;
- horno;
- área de secado;
- espacio de montaje.

No todo equipo es portátil.

---

# 13. Estado de estación

## WS01 — available

Lista para uso.

## WS02 — occupied

En uso por otra tarea.

## WS03 — maintenance

Mantenimiento.

## WS04 — damaged

Capacidad reducida.

## WS05 — unavailable

No puede usarse.

---

# 14. Capacidad

La existencia de diez trabajadores no implica diez puestos simultáneos.

La producción puede limitarse por:

- número de estaciones;
- herramientas compartidas;
- espacio;
- material.

---

# 15. Calidad

Las herramientas influyen en calidad junto con:

- material;
- trabajador;
- especialidad;
- tiempo;
- dificultad;
- errores;
- acabado.

No existe “herramienta +10” abstracta.

---

# 16. Herramienta excepcional

Puede existir una pieza especialmente buena.

Su valor puede venir de:

- manufactura;
- material;
- ajuste;
- mantenimiento;
- historia.

No convierte automáticamente a su usuario en maestro.

---

# 17. Pérdida o robo

Una herramienta perdida/robada puede afectar:

- producción;
- encargo;
- relación;
- propiedad;
- investigación.

El negocio debe reaccionar al hecho real.

---

# 18. Inventario agregado

En LOD bajo:

las herramientas comunes pueden representarse como capacidad agregada:

- functional_tool_capacity;
- missing_critical_tools;
- maintenance_pressure.

Las piezas relevantes mantienen ID.

---

# 19. Astilleros Reales

T08 puede tener equipamiento especializado y controlado.

Este documento no define:

- herramientas navales exclusivas;
- inventario militar;
- cadena de custodia interna.

Eso depende del sistema naval/tecnológico futuro.

---

## Regla final

**En Treskal saber hacer algo no basta: hay que disponer de la herramienta correcta, en condiciones de trabajar y en un lugar donde usarla.**
