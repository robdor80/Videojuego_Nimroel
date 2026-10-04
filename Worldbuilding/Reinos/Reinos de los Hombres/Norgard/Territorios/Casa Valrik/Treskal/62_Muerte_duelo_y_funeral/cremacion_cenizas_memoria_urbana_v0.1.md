# Treskal — cremación, cenizas y memoria urbana v0.1

## Estado

**DISEÑO DE WORLD STATE APROBADO**

## Objetivo

Traducir la práctica funeraria ya canónica a estados persistentes sin inventar contenido ritual.

---

# 1. Registro funerario mínimo

Un caso relevante puede mantener:

- death_ref;
- deceased_npc_ref;
- remains_location_ref;
- custody_ref;
- mort_state;
- cremation_site_ref_if_known;
- ashes_destination_type;
- ashes_destination_ref_if_known;
- family_or_responsible_refs;
- known_by;
- related_event_refs.

---

# 2. Destinos de cenizas

## ASH01 — family_land

Tierras familiares.

## ASH02 — personally_linked_territory

Lugar territorial especialmente vinculado a la vida.

## ASH03 — communal_return_ground

Terreno comunal de retorno de Treskal.

## ASH04 — sea_return

Mar de Suthiros bajo variante local aprobada.

## ASH05 — pending

Destino aún no resuelto.

No se inventan destinos religiosos.

---

# 3. Terreno comunal

ASH03:

- no contiene tumbas individuales;
- no conserva cadáveres;
- no funciona como cementerio;
- no requiere sacerdocio.

---

# 4. Ceremonia

Puede variar por:

- familia;
- posición;
- relaciones;
- institución;
- trayectoria.

Este documento no fija:

- discursos;
- símbolos obligatorios;
- duración;
- cantos;
- vestimenta.

---

# 5. Escala social

Una persona de alto rango puede reunir:

- más asistentes;
- guardias;
- representantes;
- símbolos de Casa.

El principio corporal no cambia.

## 5.1. Relación con el luto formal

La despedida y cremación ocurren normalmente durante la **tercera jornada de luto** cuando las circunstancias lo permiten.

Si la cremación debe retrasarse por causa real:

- el luto formal no se vuelve automáticamente indefinido;
- el duelo personal puede continuar;
- MORT08 puede reflejar la interrupción logística;
- la cremación se realiza cuando vuelve a ser posible.

El retorno final de las cenizas puede ocurrir después del tercer día sin contradecir el cierre del luto formal.

---

# 6. Interrupción

MORT08 puede ocurrir por:

- temporal;
- incendio;
- acceso bloqueado;
- ausencia de responsables;
- otro evento real.

La secuencia se retoma cuando sea posible.

---

# 7. Gameplay

El jugador puede participar en:

- aviso;
- traslado;
- preparación;
- ceremonia;
- entrega de cenizas;
- retorno al destino.

No se convierte automáticamente en misión.

---

# 8. Persistencia

Cuando se completa MORT07:

- el NPC sigue muerto;
- los restos ya no están disponibles como cuerpo;
- la memoria/relaciones permanecen;
- objetos y asuntos pendientes siguen sus sistemas.

---

## Regla final

**La ceremonia termina; la historia social de la persona no.**
