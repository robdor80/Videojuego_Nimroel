# Norgard Defaults — personalidad persistente de NPC humanos v0.1

## Estado

**ACTIVO — SOLO HUMANOS DE NORGARD**

Este bloque activa para Norgard el sistema persistente de personalidad de Nimroel Core.

No define personalidad de:

- elfos;
- enanos;
- otras especies o pueblos no humanos.

Esas capas se crearán cuando su canon sea desarrollado.

---

## 1. Tres niveles

### A — NPC autoral / muy importante

Personalidad escrita específicamente para el personaje.

No se genera ni se sustituye proceduralmente.

### B — NPC persistente / importante

Recibe una personalidad procedural completa, única y persistente.

La receta solo es una estructura inicial; la semilla genera variación determinista y el perfil queda unido al `npc_id`.

### C — NPC random / latente

No necesita perfil completo mientras siga siendo fondo.

Conserva una `personality_seed` y puede usar una firma conductual ligera determinista.

Cuando una interacción lo convierte en persona persistente relevante, promociona **C→B** una sola vez.

---

## 2. Promoción C→B

La promoción puede activarse cuando aparece una consecuencia persistente, por ejemplo:

- recibe o necesita nombre estable;
- interacción repetida con el jugador;
- relación;
- favor;
- promesa;
- conflicto;
- transacción persistente;
- participación en misión;
- testimonio o información importante;
- cualquier otra causa que obligue al World State a recordarlo como individuo.

Una frase incidental no obliga por sí sola a promoverlo.

Si el jugador ya vio comportamiento del NPC antes de la promoción, el perfil generado debe ser compatible con ese comportamiento.

---

## 3. B→A

Si un NPC procedural termina convirtiéndose en personaje muy importante, **no se rerollea**.

La personalidad autoral se construye alrededor de:

- perfil ya existente;
- recuerdos;
- relaciones;
- conducta observada;
- evolución.

Convertirse en protagonista no convierte al NPC en otra persona.

---

## 4. Biblioteca de Norgard

La biblioteca inicial contiene **80 recetas abstractas originales**.

Ninguna receta representa:

- personaje de serie;
- profesión;
- clase social;
- sexo;
- Gran Casa;
- ciudad;
- rango.

Dos NPC pueden compartir receta y seguir siendo distintos por:

- vector PERS;
- variación determinista;
- estilos;
- familia;
- educación;
- experiencias;
- relaciones;
- memoria;
- estado actual.

---

## 5. Cultura no es personalidad

Norgard no recibe un vector psicológico obligatorio.

Ser:

- Valrik;
- Darovan;
- noble;
- campesino;
- herrero;
- soldado;
- marinero

no selecciona una personalidad.

La cultura, Casa, localidad y profesión pueden modificar **expresión, registro, hábitos o normas aprendidas**, nunca el núcleo psicológico por defecto.

---

## 6. IA

La IA recibe una ficha compacta y no tiene autoridad para cambiarla.

Debe combinar:

**PERS + cultura/educación + profesión/rol + relación + memoria + VAL/SELF + EMO/MOOD/STRS + situación actual**

para producir conducta y diálogo.

La IA interpreta. El motor conserva identidad y verdad.

---

## Regla final

**Un random de Norgard puede seguir siendo anónimo toda su vida; pero en el momento en que el juego necesita recordarlo como persona, recibe una personalidad coherente y esa persona ya no se rerollea jamás.**
