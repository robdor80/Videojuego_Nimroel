# Treskal — disponibilidad de curanderas y gameplay de cuidados v0.1

## Estado

**DISEÑO DE GAMEPLAY APROBADO**

## Objetivo

Integrar cuidados, disponibilidad y desplazamientos en World State sin crear un dispensador de curación.

---

# 1. Proveedor persistente

Cada curandera formada relevante puede disponer de:

- npc_id;
- hogar;
- área habitual;
- conocimientos;
- materiales;
- rutina;
- relaciones;
- estado.

No es un servicio abstracto sin persona.

---

# 2. Capacidad

Una curandera no atiende infinitas personas al mismo tiempo.

La demanda puede producir:

- espera;
- desplazamiento;
- búsqueda de otra especialista;
- prioridad de urgencia.

---

# 3. Solicitud

El jugador puede:

- preguntar dónde encontrarla;
- acudir;
- pedir visita;
- llevar materiales;
- acompañar;
- solicitar ayuda para otro NPC.

La respuesta depende de:

- disponibilidad;
- relación;
- gravedad;
- distancia;
- World State.

---

# 4. Tratamiento

El tratamiento puede consumir:

- tiempo;
- materiales;
- reposo.

No se modela necesariamente como restauración instantánea.

---

# 5. Resultado

El motor de salud futuro resuelve:

- mejora;
- estabilidad;
- empeoramiento;
- recuperación.

La IA puede describir.

No decide por sí sola el resultado fisiológico.

---

# 6. Ausencia

Si el jugador llega y la curandera no está:

el mundo debe tener una explicación coherente.

No se teletransporta de regreso.

---

# 7. Accidente público

Un accidente en:

- mercado;
- taller;
- puerto

puede generar:

- testigos;
- ayuda inicial;
- búsqueda de especialista;
- evento EVT;
- conocimiento/rumor.

No crea automáticamente una misión.

---

# 8. Stock sanitario

Los materiales relevantes pueden pertenecer a stock real.

Si falta un material:

- se busca sustituto plausible;
- se espera reposición;
- cambia tratamiento posible.

No aparece por interfaz.

---

# 9. Aprendiz

Un aprendiz puede:

- ayudar;
- preparar material;
- transmitir recado;
- aplicar tareas compatibles.

No posee automáticamente capacidad completa de la maestra.

---

# 10. LOD

Fuera de escena:

- visitas;
- recuperación;
- demanda

pueden resolverse agregadamente.

Los hechos importantes persisten.

---

# 11. Información

Un NPC puede saber:

- que una curandera es buena;
- dónde vive;
- que está fuera.

Eso no significa conocer:

- diagnóstico de paciente;
- contenido de sus reservas;
- toda su agenda.

---

## Regla final

**Buscar curación en Treskal significa buscar a una persona disponible y capaz, no pulsar un servicio urbano.**
