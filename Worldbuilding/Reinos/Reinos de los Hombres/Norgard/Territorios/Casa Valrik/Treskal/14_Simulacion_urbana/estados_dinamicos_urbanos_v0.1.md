# Treskal — estados dinámicos urbanos v0.1

## Estado

**DISEÑO DE GAMEPLAY APROBADO — WORLD STATE URBANO**

## Objetivo

Definir situaciones que alteran temporalmente Treskal sin regenerar su estructura.

Un estado dinámico puede modificar:

- rutas;
- densidad de NPC;
- inventarios;
- precios;
- horarios;
- diálogo;
- disponibilidad de servicios;
- sonido y ambientación.

No cambia automáticamente el canon permanente.

---

# D01 — Temporal marítimo

## Efectos posibles

- menor pesca;
- menos pequeñas embarcaciones;
- retraso de barcos;
- actividad reducida en T07;
- mayor trabajo de amarre y seguridad;
- escasez posterior de pescado;
- daños menores en muelles.

## No provoca automáticamente

- destrucción masiva;
- inundación de toda la ciudad;
- cierre permanente del puerto.

---

# D02 — Crecida del río

## Efectos posibles

- T01 afectado;
- navegación alterada;
- caminos ribereños embarrados;
- vigilancia del puente;
- cambios de ruta;
- daños en instalaciones bajas.

## Restricción

T05, T06 y archivos críticos no deben estar colocados en zona expuesta por defecto.

---

# D03 — Incendio urbano

## Origen posible

- vivienda;
- horno;
- taller;
- almacén;
- accidente.

## Efectos

- guardia;
- vecinos;
- cuadrillas;
- corte de calles;
- consumo de agua;
- daños persistentes;
- posible pérdida de stock o vivienda.

## Regla

El daño se persiste.

No desaparece al recargar la zona.

---

# D04 — Incendio o emergencia en Astilleros Reales

Estado específico de T08.

Puede provocar:

- cierre de accesos;
- movilización interna;
- demanda de agua;
- guardia reforzada;
- interrupción de trabajo;
- escasez temporal de ciertos materiales.

La respuesta principal corresponde al recinto de la Corona.

---

# D05 — Gran convoy de madera

## Efectos

- aumento de carros en T11/T02;
- ocupación de patios;
- mayor actividad T04/T08;
- congestión localizada;
- nuevos contratos o entregas.

No convierte toda la ciudad en un atasco.

---

# D06 — Gran día de ganado

## Efectos

- mayor actividad T10/S10;
- más comerciantes rurales;
- más demanda de posadas;
- más guardia periférica;
- ruido y barro contextuales.

El ganado sigue evitando T03.

---

# D07 — Llegada importante de barco mercante

## Efectos

- mayor actividad T07;
- cargadores;
- comerciantes;
- inventarios nuevos;
- rumores;
- visitantes;
- ocupación de posadas.

La mercancía depende del origen real del barco.

---

# D08 — Botadura o hito naval real

## Efectos

- actividad excepcional en T08;
- posible presencia institucional;
- trabajadores;
- logística;
- observadores en zonas permitidas.

No convierte automáticamente la botadura en fiesta pública masiva.

El contexto narrativo decide su importancia.

---

# D09 — Mala cosecha o retraso cerealista

## Efectos

- menor stock;
- subida de precios;
- cambios en S06;
- diálogo;
- presión sobre importaciones.

No cambia la estructura de mercados.

---

# D10 — Corte o deterioro de ruta terrestre

## Efectos

- llegada menor de ciertos productos;
- desvíos;
- aumento de costes;
- retraso de viajeros;
- cambios de rutas NPC.

Puede afectar especialmente:

- madera;
- cereal;
- ganado.

---

# D11 — Jornada de alta actividad judicial

## Efectos

- más visitantes en T05/T06;
- guardia;
- representantes de Villas;
- posadas ocupadas;
- rumores.

No implica crisis política.

---

# D12 — Día urbano ordinario

Debe existir como estado normal.

El sistema no debe buscar constantemente un acontecimiento extraordinario.

La mayor parte del tiempo Treskal funciona con:

- mercado;
- trabajo;
- puerto;
- hogares;
- administración;
- talleres.

---

# Persistencia

Algunos estados son temporales.

Sus consecuencias pueden persistir.

Ejemplo:

**incendio termina → edificio sigue dañado → reparación posterior**

o:

**temporal termina → pescado sigue escaso hasta nueva captura**

---

# Comunicación al jugador

Los estados deben percibirse mediante:

- NPC;
- actividad;
- mercancías;
- rutas;
- sonido;
- clima;
- precios;
- edificios.

No mediante mensajes omniscientes obligatorios.

---

## Regla final

**El World State cambia cómo funciona Treskal hoy sin convertir cada día en una crisis y sin borrar lo ocurrido ayer.**
