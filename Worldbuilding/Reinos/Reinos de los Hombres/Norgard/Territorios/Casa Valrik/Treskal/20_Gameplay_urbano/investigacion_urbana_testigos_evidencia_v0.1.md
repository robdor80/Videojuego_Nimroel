# Treskal — investigación urbana, testigos y evidencia v0.1

## Estado

**DISEÑO DE GAMEPLAY APROBADO — INVESTIGACIÓN NO OMNISCIENTE**

## Objetivo

Permitir investigaciones urbanas basadas en:

- testigos;
- memoria;
- rumores;
- lugares;
- objetos;
- documentos;
- contradicciones.

---

# 1. Hecho real y conocimiento son capas distintas

El World State contiene lo que ocurrió.

Los NPC contienen versiones parciales.

El jugador solo puede conocer:

- lo que percibe;
- lo que descubre;
- lo que le cuentan;
- lo que documenta.

---

# 2. Testigos

Un NPC puede ser:

- testigo directo;
- testigo parcial;
- testigo posterior;
- receptor de rumor;
- persona sin conocimiento.

El diálogo debe respetar esa posición.

---

# 3. Campo de percepción

Un testigo solo puede recordar lo que pudo:

- ver;
- oír;
- reconocer;
- interpretar.

No conoce automáticamente:

- identidad de desconocidos;
- intención;
- contenido de bolsillos;
- hechos detrás de una puerta.

---

# 4. Memoria

La calidad puede variar por:

- tiempo transcurrido;
- atención;
- iluminación;
- distancia;
- estrés;
- familiaridad;
- importancia personal.

No se introduce un porcentaje universal de memoria perfecta.

---

# 5. Contradicciones

Dos testigos pueden discrepar sin que uno mienta.

Causas:

- posición;
- atención;
- confusión;
- tiempo;
- interpretación.

El sistema debe permitir contradicciones naturales.

---

# 6. Mentira

Un NPC puede mentir si tiene:

- motivo;
- conocimiento suficiente;
- decisión narrativa o sistémica.

La IA no decide arbitrariamente mentir solo para complicar una misión.

---

# 7. Evidencia física

Puede incluir:

- objeto;
- huella o daño;
- mercancía;
- puerta;
- documento;
- rastro de incendio;
- posición de elementos.

La evidencia debe existir en World State.

No se genera retroactivamente porque el jugador pregunte.

---

# 8. Documentos

Pueden aportar:

- contratos;
- registros;
- cuentas;
- entradas;
- permisos;
- expedientes.

El acceso depende de:

- institución;
- privacidad;
- autoridad;
- relación.

---

# 9. Guardia

La guardia puede:

- recibir denuncia;
- recoger testimonios;
- custodiar lugares;
- buscar personas;
- mantener información interna.

No resuelve automáticamente el caso para el jugador.

---

# 10. Rumor y evidencia

Un rumor puede orientar.

No equivale a prueba.

El jugador debe poder distinguir:

- testimonio directo;
- rumor;
- documento;
- observación propia.

---

# 11. Cronología

Una investigación puede reconstruir:

- quién estuvo;
- cuándo;
- por dónde;
- qué cambió.

Las rutinas y grafo urbano permiten comprobar plausibilidad.

---

# 12. NPC persistente

Si un testigo fue materializado, su versión debe persistir.

No cambia de historia porque la misión necesite una pista distinta.

Puede cambiar de opinión, pero no su percepción pasada sin razón.

---

# 13. Conocimiento del jugador

El journal puede registrar:

- hecho confirmado;
- hipótesis;
- testimonio;
- rumor;
- contradicción.

No debe convertir automáticamente cada pista en verdad.

---

# 14. Fallo

Una investigación puede:

- quedar incompleta;
- llegar tarde;
- acusar erróneamente;
- descubrir solo parte.

El mundo continúa.

---

## Regla final

**Investigar Treskal significa reconstruir un hecho a partir de personas y mundo persistente, no seguir una secuencia prefabricada de marcadores.**
