# Treskal — contrato conceptual de World State v0.1

## Estado

**DISEÑO DE INTEGRACIÓN APROBADO**

## Objetivo

Definir qué partes de Treskal son canon estático y qué partes pertenecen al estado mutable de una partida.

---

# 1. Canon estático

No debe cambiar sin migración de diseño:

- topología A;
- sectores T01–T11;
- subzonas Z01–Z14;
- instalaciones S01–S10;
- landmarks L01–L12;
- corredores C01–C08;
- identidad económica base;
- propiedad de Astilleros Reales;
- ausencia de muralla;
- función de Casa Valrik;
- convenciones toponímicas;
- reglas culturales.

---

# 2. World State persistente

Puede cambiar durante juego:

- habitantes vivos;
- hogares;
- relaciones;
- propietarios;
- negocios;
- inventarios;
- precios;
- daños;
- reparaciones;
- obras;
- reputaciones;
- permisos;
- detenciones;
- procesos judiciales;
- barcos presentes;
- visitantes;
- encargos;
- rutas temporalmente bloqueadas.

---

# 3. Estado temporal derivado

Puede calcularse a partir del tiempo y eventos:

- densidad visible;
- actividad de mercado;
- lluvia;
- barro;
- ocupación de tabernas;
- tráfico;
- disponibilidad momentánea de anclas.

No todo necesita guardarse si puede reconstruirse determinísticamente desde estado persistente.

---

# 4. Separación de identidad y estado

Ejemplo:

`S06 = Plaza del Abasto`

permanece.

Pero pueden cambiar:

- puestos activos;
- mercancía;
- NPC presentes;
- precios;
- daños;
- actividad.

---

# 5. Edificios

Cada edificio materializado necesita:

- ID;
- tipología U;
- ubicación;
- propietario;
- ocupantes;
- estado;
- accesos;
- interior seed/materialización.

El edificio puede cambiar de uso sin perder su ID.

---

# 6. Negocios

Cada negocio necesita:

- business_id;
- building_id;
- owner/ref;
- workers;
- activity;
- stock;
- reputation;
- schedule;
- supplier refs.

Puede:

- cerrar;
- cambiar de dueño;
- mudarse;
- desaparecer.

---

# 7. NPC

Los NPC persistentes mantienen:

- identidad;
- hogar;
- relaciones;
- recuerdos relevantes;
- situación laboral;
- estado vital.

No se regeneran por visitar de nuevo la ciudad.

---

# 8. Instituciones

Las instituciones mantienen identidad.

Pueden cambiar:

- personal;
- carga de trabajo;
- responsables;
- estado de edificios;
- nivel de alerta.

---

# 9. Barcos

Un barco presente en puerto debe disponer de referencia persistente mientras sea relevante.

Puede tener:

- tripulación;
- carga;
- origen;
- destino;
- fecha/hora estimada;
- estado.

No todos los barcos necesitan simulación completa fuera de escena.

---

# 10. Mercancías

Las grandes cantidades relevantes deben poder ligarse a:

- proveedor;
- almacén;
- convoy;
- barco;
- negocio;
- institución.

No es necesario rastrear individualmente cada pan.

---

# 11. Daños

Daño persistente:

- incendio;
- inundación;
- derrumbe;
- vandalismo;
- combate.

La reparación requiere:

- tiempo;
- material;
- trabajo

cuando tenga importancia jugable.

---

# 12. Versionado

Los contratos de diseño deben versionarse.

Una partida existente no debe regenerar Treskal al actualizar el juego.

Cambios de canon que afecten datos persistentes necesitan:

- migración;
- compatibilidad;
- decisión explícita.

---

# 13. Carga por nivel de detalle

El motor puede mantener:

## LOD lógico bajo

- conteos;
- estado agregado;
- posiciones aproximadas.

## LOD medio

- rutinas;
- rutas;
- stock;
- ocupación.

## LOD alto

- NPC individual;
- interior;
- diálogo;
- objetos relevantes.

El cambio de LOD no altera hechos.

---

## Regla final

**El canon dice qué es Treskal; el World State recuerda qué le ha ocurrido a esta Treskal concreta.**
