# Treskal — parentesco persistente y red familiar v0.1

## Estado

**DISEÑO SOCIAL/JUGABLE APROBADO — FAMILIA NO ES LO MISMO QUE HOGAR**

## Objetivo

Formalizar relaciones de parentesco persistentes entre NPC sin convertir:

- convivencia;
- pareja;
- cuidado;
- amistad;
- apellido futuro;
- herencia

en sinónimos de familia biográfica.

---

# 1. Tipos operativos

## KIN01 — parent_child

Relación entre progenitor conocido y descendiente directo.

## KIN02 — sibling

Relación entre hermanos cuando la filiación conocida permite establecerla.

## KIN03 — grandparent_grandchild

Relación entre abuelo/abuela y nieto/nieta derivada de parentesco conocido.

## KIN04 — aunt_uncle_niece_nephew

Relación familiar colateral cuando puede derivarse de vínculos conocidos.

## KIN05 — cousin

Relación entre primos cuando la genealogía relevante está materializada.

## KIN06 — extended_kin

Otro parentesco familiar relevante que no necesita una categoría más específica en la simulación.

## KIN07 — family_role_without_legal_definition

Rol familiar socialmente vivido cuya categoría jurídica exacta todavía no está definida por canon superior.

KIN07 no crea adopción, tutela ni filiación legal.

---

# 2. Parentesco y hogar

Compartir hogar no crea parentesco.

Ser parientes no obliga a compartir hogar.

RES y H describen:

- residencia;
- composición doméstica.

KIN describe vínculo familiar persistente.

---

# 3. Parentesco y pareja

AFF05 no crea por sí solo:

- progenitor;
- hermano;
- parentesco legal;
- relación con familiares de la pareja.

Las reglas formales de matrimonio y afinidad quedan para el canon familiar de Norgard.

---

# 4. Nacimiento

Un nacimiento vivo crea:

- nuevo NPC;
- KIN01 con la madre registrada;
- otros vínculos de filiación solo cuando el sistema autorizado de parentaje los determine.

No se infiere segundo progenitor por:

- pareja;
- convivencia;
- reputación;
- apariencia;
- conveniencia narrativa.

---

# 5. Hermanos

KIN02 puede derivarse cuando dos NPC comparten parentesco parental suficiente según el futuro modelo de filiación.

Compartir hogar durante la infancia no basta por sí solo.

---

# 6. Familia extensa

No es necesario materializar una genealogía completa de cada habitante.

Se materializan vínculos cuando afectan:

- hogar;
- cuidado;
- memoria;
- historia;
- trabajo;
- viaje;
- duelo;
- narrativa;
- futuros derechos legales.

---

# 7. Cuidado

Un familiar puede cuidar a otro.

Eso no ocurre automáticamente.

CARE necesita:

- disponibilidad;
- capacidad;
- presencia;
- relación real.

KIN puede aumentar plausibilidad, no crear cobertura de cuidado.

---

# 8. Amistad y conflicto

Los familiares pueden:

- ser amigos;
- ser distantes;
- estar enfrentados;
- no conocerse bien.

FRI, RIFT, TRUST, VIEW y AFF siguen siendo independientes.

---

# 9. Conocimiento del parentesco

La existencia de un vínculo familiar y quién lo conoce son cosas distintas.

Un NPC puede:

- conocerlo;
- ignorarlo;
- dudar;
- recibir información parcial.

K y CRED gobiernan conocimiento y creencia.

---

# 10. Privacidad

Un vínculo puede existir y no ser públicamente conocido.

CONF puede proteger información de:

- filiación;
- nacimiento;
- identidad familiar

cuando el canon y la historia lo justifiquen.

---

# 11. Muerte

La muerte no elimina KIN.

El vínculo continúa como parte de la historia del superviviente.

MORT y MEM gobiernan:

- duelo;
- recuerdo;
- consecuencias.

---

# 12. Jugador

El jugador puede descubrir relaciones familiares mediante:

- conversación;
- documentos futuros;
- observación;
- reputación;
- investigación;
- presentación social.

No recibe un árbol genealógico global por defecto.

---

# 13. IA

La IA puede usar únicamente vínculos KIN autorizados.

No puede inventar:

- hermanos;
- padres;
- hijos;
- primos;
- parentescos ocultos

para enriquecer diálogo o drama.

---

## Regla final

**En Treskal una familia es una red persistente de personas concretas; puede atravesar hogares, distancias, conflictos y generaciones sin dejar de ser historia real del mundo.**
