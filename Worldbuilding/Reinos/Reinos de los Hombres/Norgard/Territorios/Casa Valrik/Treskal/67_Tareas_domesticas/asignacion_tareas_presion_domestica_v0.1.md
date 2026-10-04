# Treskal — asignación de tareas y presión doméstica v0.1

## Estado

**DISEÑO DE WORLD STATE APROBADO**

## Objetivo

Resolver trabajo doméstico de forma eficiente sin simular manualmente cada tarea ordinaria.

---

# 1. Registro agregado del hogar

Puede mantener:

- household_ref;
- domestic_state;
- water_need;
- fuel_need;
- food_prep_need;
- cleaning_need;
- laundry_need;
- waste_need;
- care_need;
- errand_need;
- maintenance_need;
- available_domestic_time;
- external_support_refs;
- backlog_flags.

---

# 2. Capacidad doméstica

Se deriva de:

- miembros presentes;
- edad/capacidad;
- REST;
- EMP;
- CARE;
- salud;
- relaciones;
- herramientas;
- clima;
- distancia.

No es fija.

---

# 3. Resolución automática

En LOD bajo el sistema puede resolver tareas agregadamente si:

- existe persona plausible;
- hay tiempo;
- recursos;
- acceso.

No necesita materializar cada recorrido.

---

# 4. Materialización

Una tarea se vuelve visible cuando:

- jugador está cerca;
- existe conflicto;
- falta recurso;
- produce evento;
- se convierte en interacción.

El resultado debe coincidir con el estado agregado.

---

# 5. Priorización

El hogar puede priorizar:

1. necesidad urgente de dependientes;
2. agua/alimento;
3. combustible esencial;
4. residuos críticos;
5. resto de tareas.

No es una ley universal rígida, sino una lógica por defecto.

---

# 6. Brecha

Si capacidad < necesidad:

el sistema genera backlog.

No inventa un trabajador doméstico.

---

# 7. Ayuda externa

DOM06 debe apuntar a actor o servicio real.

Puede reducir backlog.

---

# 8. Persistencia

El estado doméstico sobrevive save/load.

No se reinicia a “casa limpia y abastecida”.

---

## Regla final

**La simulación puede abstraer el trabajo doméstico, pero nunca fingir que se hizo si nadie tenía tiempo, recursos o acceso para hacerlo.**
