# Treskal — cadenas causales de referencia v0.1

## Estado

**GUÍA DE IMPLEMENTACIÓN Y REGRESIÓN**

## Objetivo

Proporcionar cadenas cortas que permitan revisar una implementación sin depender de escenas narrativas concretas.

---

# Cadena A — temporal y pescado

weather
→ ENV local
→ D01/EVT si umbral extraordinario
→ salida/entrada de pesca
→ pescado descargado
→ ST1 disponible
→ vendedores
→ presión de mercado
→ consumo
→ conocimiento NPC
→ diálogo

---

# Cadena B — carro averiado

TR04
→ daño
→ bloqueo local
→ grafo/ruta
→ retraso de carga
→ stock pendiente
→ negocio
→ reparación
→ liberación de ruta

---

# Cadena C — puerta forzada

DOOR
→ daño persistente
→ acceso físico
→ entrada
→ posible OWN/theft
→ evidencia
→ K de testigos/investigación
→ justicia futura

---

# Cadena D — prenda dañada

GAR03
→ necesidad de reparación
→ O10/COM
→ materiales
→ GAR04
→ tiempo/trabajo
→ GAR01/GAR02 según resultado
→ visual

---

# Cadena E — incendio doméstico

fuel_stock
→ ignición
→ EVT
→ COND del edificio/objetos
→ salud
→ RES05
→ MOVE/alojamiento temporal
→ repair job/BUILD si necesario
→ retorno o nueva residencia

---

# Cadena F — nuevo negocio

demanda
→ BIZ01
→ BUILD/adaptación si necesaria
→ empleo/vacantes
→ stock/proveedores
→ señalización
→ BIZ02
→ conocimiento local
→ mercado/reputación

---

# Cadena G — carta urgente

MSG
→ portador
→ ruta/TR
→ attempted/delivered
→ lectura
→ K
→ decisión NPC
→ nueva acción/evento

---

# Cadena H — lluvia y colada

weather
→ ENV
→ wetness
→ drying_conditions
→ ropa disponible
→ presentación NPC
→ rutina doméstica

---

# Regla de prueba

En cada cadena comprobar:

- causa inicial;
- sistema responsable;
- estado intermedio;
- efecto final;
- conocimiento;
- persistencia;
- no duplicación.

---

## Regla final

**Si no puede dibujarse la cadena causal de un cambio importante, el cambio no está suficientemente definido.**
