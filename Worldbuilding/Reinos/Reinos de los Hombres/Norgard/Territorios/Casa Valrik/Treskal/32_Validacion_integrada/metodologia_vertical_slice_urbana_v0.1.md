# Treskal — metodología de validación de vertical slice urbana v0.1

## Estado

**PAQUETE DE PRUEBAS DE INTEGRACIÓN — NO CANON NARRATIVO**

## Objetivo

Validar que los sistemas de Treskal funcionan juntos.

Estas pruebas no crean hechos canónicos, NPC canónicos ni eventos históricos.

Son escenarios técnicos reproducibles.

---

# 1. Qué debe cruzar una prueba

Cada escenario puede combinar:

- APP aproximación;
- T sector;
- Z subzona;
- C corredor;
- L landmark;
- U edificio;
- H hogar;
- O ocupación;
- V visitante;
- W estado de madera;
- ST almacenamiento;
- D estado dinámico;
- EVT evento;
- K conocimiento;
- P acceso;
- LOD;
- IA.

---

# 2. Principio

Una prueba de integración no pregunta:

“¿funciona el mercado?”

Pregunta:

“¿funciona el mercado cuando llega un viajero, compra stock real, pregunta a un NPC que no sabe todo, cambia la demanda y luego abandona la ciudad?”

---

# 3. Condiciones reproducibles

Cada caso debe fijar:

- seed técnica;
- World State inicial;
- hora/franja;
- clima;
- actores;
- stocks;
- conocimientos;
- evento;
- entrada del jugador.

---

# 4. Assertions

Se utilizan:

- REQUIRED;
- FORBIDDEN;
- OPTIONAL.

No se exige resultado narrativo textual exacto salvo pruebas de IA.

---

# 5. Fallo crítico

Son fallos críticos:

- reroll de entidad materializada;
- stock creado sin fuente;
- conocimiento omnisciente;
- evento sin causa;
- identidad cambiada por LOD;
- ruta imposible ignorada;
- cargo en tránsito contado como stock;
- interior reseteado;
- secreto filtrado;
- Astilleros Reales tratados como acceso civil.

---

# 6. Repetición

Los casos deterministas deben producir el mismo estado lógico con:

- misma versión;
- misma seed;
- mismo input.

La presentación audiovisual puede variar dentro de reglas sin cambiar hechos.

---

# 7. Snapshot

Cada escenario debería permitir capturar:

- estado antes;
- acciones;
- estado después;
- eventos;
- conocimiento;
- inventarios;
- posiciones lógicas;
- entidades materializadas.

---

# 8. Prueba de regresión

Cuando un contrato cambie, los escenarios se vuelven a ejecutar.

Un cambio de comportamiento debe ser:

- intencional;
- documentado;
- migrable cuando afecte a partidas.

---

## Regla final

**Treskal estará lista para jugar cuando sus sistemas funcionen juntos bajo estados cambiantes, no cuando cada documento sea correcto por separado.**
