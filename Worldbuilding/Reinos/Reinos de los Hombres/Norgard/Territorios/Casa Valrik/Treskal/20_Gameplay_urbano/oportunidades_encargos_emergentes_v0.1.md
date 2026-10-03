# Treskal — oportunidades y encargos emergentes v0.1

## Estado

**DISEÑO DE GAMEPLAY APROBADO — GENERACIÓN DESDE WORLD STATE**

## Objetivo

Crear pequeñas oportunidades urbanas que nazcan de necesidades reales sin convertir la ciudad en una fábrica infinita de misiones repetitivas.

---

# 1. Fuente

Una oportunidad emerge cuando existe una diferencia entre:

**estado deseado** y **estado real**.

Ejemplos:

- falta mercancía;
- entrega retrasada;
- trabajador ausente;
- objeto perdido;
- ruta bloqueada;
- daño;
- deuda;
- necesidad de información;
- persona que busca transporte.

---

# 2. Categorías

## Transporte

Mover:

- mercancía;
- carta;
- herramienta;
- persona.

## Suministro

Conseguir:

- madera;
- alimento;
- herramienta;
- material.

## Trabajo

Ayudar en:

- carga;
- reparación;
- búsqueda;
- preparación.

## Información

Localizar:

- persona;
- proveedor;
- testigo;
- origen de problema.

## Mediación

Resolver:

- desacuerdo;
- pago;
- promesa;
- entrega.

## Seguridad

Responder a:

- robo;
- amenaza;
- incidente.

Solo cuando corresponda al rol del jugador y al contexto.

---

# 3. No son infinitas

Una necesidad se resuelve.

El generador no debe recrear la misma falta inmediatamente para producir contenido.

---

# 4. Prioridad

Se pondera por:

- importancia;
- urgencia;
- cercanía;
- relación;
- impacto económico;
- evento dinámico.

---

# 5. Acceso

El jugador solo conoce una oportunidad si existe una vía de información.

Puede descubrirla:

- hablando;
- observando;
- por rumor;
- por contacto;
- mediante anuncio funcional.

---

# 6. Resolución alternativa

Una oportunidad puede ser resuelta por:

- otro NPC;
- paso del tiempo;
- cambio de ruta;
- institución;
- desaparición de necesidad.

El mundo no depende exclusivamente del jugador.

---

# 7. Recompensa

Puede ser:

- dinero;
- mercancía;
- favor;
- información;
- reputación;
- acceso;
- relación.

No toda ayuda tiene recompensa material.

---

# 8. Escalado

Un asunto cotidiano puede revelar uno mayor.

Pero no todo recado debe convertirse en conspiración.

---

# 9. Repetición

Las plantillas pueden reutilizar lógica, pero deben variar por:

- NPC;
- lugar;
- mercancía;
- causa;
- consecuencia;
- relación.

El jugador no debe percibir “misión procedural número 12”.

---

# 10. Registro persistente

Una oportunidad conocida debe tener:

- source_id;
- need;
- created_time;
- state;
- actors;
- deadline si existe;
- resolution.

---

## Regla final

**El contenido emergente de Treskal nace porque algo está ocurriendo en la ciudad, no porque el sistema necesite entretener al jugador cada treinta metros.**
