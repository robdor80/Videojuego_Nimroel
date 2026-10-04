# Treskal — batería comparativa de IA v0.1

## Estado

**PAQUETE DE PRUEBAS DE DISEÑO — NO CANON NARRATIVO**

## Propósito

Validar de forma comparable modelos de IA aplicados a Nimroel.

Proveedores objetivo iniciales:

- OpenAI;
- Gemini;
- Mistral.

Los personajes y microescenas de este paquete son **fixtures técnicos**.

No crean NPC, hechos históricos ni eventos canónicos de Treskal.

---

# 1. Regla de igualdad

Cada modelo debe recibir semánticamente:

- misma escena;
- mismo NPC;
- misma personalidad;
- mismo conocimiento;
- mismos secretos;
- misma memoria;
- mismo estado visible;
- misma pregunta del jugador.

Solo cambia:

- proveedor;
- modelo;
- parámetros técnicos necesarios.

---

# 2. Qué se evalúa

## Disciplina de conocimiento

¿Revela algo que el NPC no sabe?

## Disciplina de secretos

¿Cuenta un secreto solo porque estaba disponible en contexto interno?

## Personalidad

¿Mantiene voz y carácter?

## Naturalidad

¿Parece conversación humana y no una ficha de wiki?

## Subtexto

¿Puede insinuar sin explicarlo todo?

## Memoria

¿Recuerda promesas y encuentros relevantes?

## Mentira

¿Puede mentir sin convertir la mentira en verdad del mundo?

## Contradicción

¿Tolera versiones incompatibles?

## Humor

¿Puede usar humor contextual sin romper tono?

## Acción

¿Propone acciones sin ejecutarlas mágicamente?

## Off Story

¿El narrador evita información oculta?

---

# 3. Evaluación

Cada prueba utiliza assertions:

- REQUIRED;
- FORBIDDEN;
- ALLOWED.

No se exige una frase exacta.

Esto permite comparar creatividad sin confundirla con obediencia.

---

# 4. Fallo crítico

Se considera fallo crítico:

- filtrar secreto K0;
- revelar World State oculto;
- inventar parentesco/cargo/lugar persistente;
- convertir rumor en hecho;
- mutar inventario mediante texto;
- ignorar resultado de Percepción;
- teletransportar NPC;
- resolver una investigación sin evidencia.

---

# 5. Pruebas de narrador

Incluyen:

- descripción normal;
- foco perceptivo;
- fracaso o resultado limitado;
- continuidad ambiental;
- objeto cerrado.

---

# 6. Pruebas de diálogo

Incluyen:

- conversación cotidiana;
- personalidad;
- oficio;
- rumor;
- secreto;
- mentira;
- humor;
- memoria;
- tensión;
- desconocimiento;
- contradicción;
- reputación.

---

# 7. Pruebas de acción

Incluyen:

- entrega de objeto;
- acceso;
- movimiento;
- negocio;
- encargo.

La IA debe proponer; el motor valida.

---

# 8. Ejecución

Cada corrida debe registrar:

- test_id;
- proveedor;
- modelo;
- versión si está disponible;
- contexto;
- salida;
- assertions;
- puntuación;
- observaciones.

---

# 9. Repetición

Una sola respuesta no basta para medir consistencia.

Las pruebas importantes deben repetirse varias veces por modelo con el mismo estado semántico.

El número de repeticiones se decidirá al implementar el banco de pruebas.

---

# 10. Criterio de selección

No debe elegirse un modelo solo por:

- prosa bonita;
- respuesta larga;
- espectacularidad.

Para Nimroel tiene prioridad:

1. disciplina de contexto;
2. coherencia;
3. personalidad;
4. naturalidad;
5. coste/latencia según rol técnico.

---

## Regla final

**El mejor modelo para Nimroel no es el que más inventa: es el que mejor interpreta una realidad que ya existe.**
