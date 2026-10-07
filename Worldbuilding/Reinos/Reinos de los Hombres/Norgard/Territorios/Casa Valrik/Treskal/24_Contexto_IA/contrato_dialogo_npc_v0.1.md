# Treskal — contrato de contexto IA para diálogo NPC v0.1

## Estado

**DISEÑO DE IA APROBADO — NPC NO OMNISCIENTE**

## Objetivo

Construir un contexto mínimo y suficiente para que un NPC dialogue como la persona persistente que es, sin acceso al World State completo.

---

# 1. Contexto de identidad

La IA puede recibir:

- npc_id;
- identidad visible;
- edad aparente o datos autorizados;
- hogar;
- profesión;
- cultura;
- relaciones relevantes;
- bloque compacto de personalidad persistente;
- estado emocional actual cuando el sistema lo modele.

No necesita conocer todas las fichas de todos los habitantes.

---

# 2. Contexto inmediato

Debe incluir solo lo que el NPC puede percibir en la escena:

- interlocutores visibles;
- ubicación;
- actividad actual;
- clima perceptible;
- eventos presentes;
- objetos relevantes visibles;
- riesgos evidentes.

Un NPC no reacciona a algo ocurrido detrás de una pared si no tuvo vía de conocimiento.

---

# 3. Conocimiento

Se incluyen solo hechos que el NPC posee mediante K1–K5.

K0 no se envía como hecho disponible.

Cada conocimiento relevante puede incluir:

- contenido;
- estado K;
- fuente;
- antigüedad;
- confianza;
- contradicciones.

---

# 4. Memoria personal

Se prioriza:

- encuentros con jugador;
- promesas;
- favores;
- conflictos;
- encargos;
- pagos;
- información compartida;
- relaciones personales.

No se envía historial infinito.

---

# 5. Reputación

El NPC recibe las reputaciones que realmente le afectan:

- personal;
- familiar;
- profesional;
- vecinal;
- institucional;
- comercial.

No recibe una puntuación global ficticia de Treskal.

---

# 6. Actividad

La conversación debe conocer qué estaba haciendo el NPC:

- trabajando;
- vendiendo;
- cargando;
- descansando;
- patrullando;
- comiendo.

Esto permite respuestas como:

- continuar trabajando;
- pedir que el jugador espere;
- interrumpir por importancia.

---

# 6B. Personalidad persistente

Para un NPC B/A humano de Norgard, el contexto puede incluir:

- `personality_profile_id`;
- rasgos PERS dominantes;
- rasgos secundarios;
- estilo de humor;
- firma social;
- desacuerdo;
- reacción al estrés;
- modificadores relacionales;
- modificadores de estado actual.

La IA puede expresar esos datos, pero no:

- cambiarlos;
- inventar rasgos permanentes;
- inventar historia psicológica;
- promover C→B;
- convertir emoción temporal en personalidad.

# 7. Lo que sabe no es lo que dice

Un NPC puede conocer un hecho y:

- contarlo;
- callarlo;
- evitarlo;
- mentir;
- desviarse;
- pedir algo a cambio.

La decisión depende de:

- personalidad;
- relación;
- riesgo;
- secreto;
- interés;
- autoridad;
- situación.

No revelar automáticamente todos los hechos del contexto.

---

# 8. Mentira

La mentira es una **salida del NPC**, no una alteración del World State.

El sistema conserva:

- verdad real;
- conocimiento del NPC;
- afirmación pronunciada.

Así una mentira puede ser descubierta después.

---

# 9. Secreto conocido

Un secreto puede estar en el conocimiento del NPC pero marcado con reglas de divulgación.

La IA debe conocer:

- que es secreto;
- por qué podría ocultarlo;
- a quién puede decirlo.

No basta con ocultar el hecho del prompt si el NPC necesita razonar sobre él.

---

# 10. Información profesional

El contexto puede recuperar hechos adicionales relevantes a la profesión.

Ejemplo:

un ebanista necesita información sobre:

- talleres;
- madera;
- proveedores;
- encargos.

No necesita todos los procesos judiciales activos de T06.

---

# 11. Ubicación de personas

El NPC solo afirma ubicación actual si dispone de una fuente plausible.

Puede decir:

- dónde suele estar;
- dónde estaba;
- dónde cree que está;
- que no lo sabe.

No consulta posición global de NPC como si fuera GPS.

---

# 12. Preguntas fuera de conocimiento

Respuesta válida:

- no sé;
- no estoy seguro;
- pregunta a X;
- quizá sepan en Y.

La IA no debe rellenar huecos con lore inventado.

---

# 13. Canon nuevo

El diálogo puede generar formulación, opinión o detalle efímero.

No puede establecer automáticamente un hecho persistente nuevo como:

- parentesco;
- guerra;
- ley;
- cargo;
- edificio;
- historia canónica.

Si una salida propone un hecho nuevo relevante, debe pasar por validación del sistema antes de convertirse en canon/World State.

---

# 14. Acciones durante diálogo

El NPC puede proponer acciones:

- entregar objeto;
- cobrar;
- acompañar;
- cerrar puerta;
- avisar guardia.

La IA no debe ejecutarlas directamente.

Debe emitir intención/acción solicitada para que el motor valide:

- capacidad;
- objeto;
- acceso;
- reglas;
- estado.

---

## Regla final

**La IA interpreta al NPC; el motor conserva la verdad, decide lo posible y registra lo que realmente ocurre.**
