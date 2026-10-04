# Treskal — entradas, salidas y transición territorio-ciudad v0.1

## Estado

**DISEÑO ESPACIAL/JUGABLE APROBADO — SIN MURALLA NI PUERTA PRINCIPAL**

## Objetivo

Definir cómo se entra y sale de Treskal desde tierra, río y mar respetando su topología y la red territorial Valrik.

---

# 1. Principio

Treskal no posee muralla urbana general.

Por tanto, no existe una única “puerta de la ciudad”.

La transición es gradual:

**territorio → borde productivo/logístico → tejido urbano → destino**

La ciudad se reconoce por aumento de:

- tráfico;
- talleres;
- viviendas;
- almacenes;
- actividad;
- ruido;
- referencias urbanas.

---

# 2. A01 — Aproximación interior principal

No confundir con activity anchors A01–A12; este documento usa el código técnico **APP01** para aproximaciones.

## APP01 — Interior occidental/noroccidental

Ruta conceptual:

**camino territorial bien mantenido → Z01 El Puente → Puente de los Gemelos → C01 → T02/T03**

Uso principal:

- viajeros;
- comerciantes;
- productos rurales;
- mensajes;
- administración;
- tráfico general.

Es la aproximación terrestre más reconocible para quien llega del interior.

---

# 3. APP02 — Corredor forestal y madera

Ruta conceptual:

**rutas del Bosque Negro / centros logísticos → T11 → C02 → T02 / Los Patios / Los Talleres**

Uso:

- madera;
- trabajadores;
- guardabosques en tránsito;
- proveedores;
- carros pesados.

Debe sentirse más laboral y logístico que APP01.

No atraviesa Plaza del Abasto como ruta preferente.

---

# 4. APP03 — Abastecimiento rural y ganado

Ruta conceptual:

**explotaciones / asentamientos rurales → T11 → C06 → Z14 Los Corrales**

Uso:

- ganado;
- productos de huerta;
- cereal;
- carros;
- productores.

La transición urbana comienza antes de llegar al centro.

---

# 5. APP04 — Llegada marítima civil

Ruta conceptual:

**Mar de Suthiros → aproximación portuaria → T07 Puerto de Treskal → Z10 Los Muelles**

Uso:

- mercantes;
- pesca;
- viajeros marítimos;
- tripulaciones.

La primera lectura de ciudad es:

- litoral trabajado;
- muelles;
- almacenes;
- embarcaciones;
- actividad humana.

No Astilleros Reales como única imagen dominante.

---

# 6. APP05 — Llegada fluvial

Ruta conceptual:

**red fluvial compatible → T01 / Z02 → La Ribera de los Gemelos**

Uso:

- pequeñas embarcaciones;
- pescado fluvial;
- carga interior.

La escala y calado concretos quedan subordinados a futura cartografía/hidrología detallada.

---

# 7. APP06 — Suministro autorizado a Astilleros Reales

Ruta conceptual:

**T11/T02/T04 → C07 → acceso controlado T08**

Uso:

- materiales;
- trabajadores;
- proveedores autorizados.

No es acceso público ordinario a Treskal.

---

# 8. Seguridad en la transición

Fuera de ciudad:

- predominan guardias rurales en caminos principales.

Dentro:

- responsabilidad cotidiana de guardia urbana.

El cambio de responsabilidad no necesita una frontera física marcada.

Puede existir coordinación en:

- incidentes;
- persecuciones;
- convoyes;
- eventos.

---

# 9. Sin control universal de entrada

Una ciudad sin muralla no detiene por defecto a cada persona que entra.

No se presupone:

- registro general de viajeros;
- peaje urbano universal;
- inspección de cada carro.

Esas medidas pueden aparecer:

- por institución concreta;
- mercancía concreta;
- emergencia;
- futura regla fiscal/legal.

---

# 10. Primera impresión

La primera impresión depende de aproximación.

## Desde APP01

- tráfico;
- puente;
- río;
- crecimiento urbano;
- mercado al fondo.

## Desde APP02

- madera;
- carros;
- patios;
- talleres.

## Desde APP03

- huertas;
- corrales;
- establos;
- tejido urbano creciente.

## Desde APP04

- agua;
- muelles;
- barcos;
- almacenes;
- ciudad detrás.

## Desde APP05

- ribera;
- almacenes;
- transición fluvial-comercial.

No existe una única cinemática obligatoria que defina la ciudad.

---

# 11. Hora y clima

Una misma llegada puede variar.

Ejemplos:

- amanecer por APP04: pesca y descarga;
- lluvia por APP01: carros, barro y coberturas;
- noche por APP03: menor tránsito y más oscuridad;
- temporal por APP04: actividad reducida y amarres reforzados.

La identidad permanece; el estado cambia.

---

# 12. Materialización progresiva

Al aproximarse el jugador:

1. se carga estado agregado;
2. se elevan subzonas necesarias a LOD-M;
3. aparecen tráficos coherentes;
4. se materializan NPC relevantes;
5. al entrar en alcance interactivo se usa LOD-H.

No aparecen multitudes de golpe en una frontera invisible.

---

# 13. Salida

Al abandonar la ciudad:

- el jugador entra en red territorial;
- NPC que viajan mantienen destino;
- encargos siguen activos;
- eventos continúan;
- negocios siguen funcionando fuera de escena.

Salir no pausa Treskal.

---

# 14. Viaje rápido futuro

Si existe viaje rápido:

debe representar un desplazamiento real.

Debe consumir:

- tiempo;
- cambios ambientales;
- avance de eventos.

No teletransporta el World State al mismo instante temporal salvo modo de diseño específico.

---

# 15. Reentrada

Al volver:

la ciudad refleja lo ocurrido durante ausencia:

- obras;
- daños;
- stock;
- rumores;
- visitantes;
- cambios de NPC.

No reproduce exactamente la escena de salida.

---

## Regla final

**Treskal se entra por caminos, agua y trabajo; no por una puerta monumental que la ciudad nunca necesitó.**
