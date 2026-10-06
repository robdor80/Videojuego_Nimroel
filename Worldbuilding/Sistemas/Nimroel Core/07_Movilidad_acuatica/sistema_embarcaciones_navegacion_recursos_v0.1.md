# Nimroel Core — Sistema universal de embarcaciones, navegación y recursos acuáticos v0.1

## Estado

**CORE UNIVERSAL ACTIVO — FASE 2B**

Este sistema define cómo existe y se simula una embarcación en Nimroel. No define la estética ni la tecnología concreta de una cultura.

## Principio central

**Lo procedural puede crear una entidad compatible; una vez materializada, esa entidad pertenece al World State y no se vuelve a tirar.**

Una embarcación materializada conserva identidad, propietario, tripulación, carga, posición, estado, daños, reparaciones e historial.

## 1. Embarcaciones

Toda embarcación debe derivar de un perfil cultural o institucional que determine qué puede construirse.

El Core controla:

- identidad persistente;
- dimensiones y capacidad;
- propulsión;
- tripulación;
- carga;
- condición y componentes;
- navegación;
- atraque;
- mantenimiento;
- accidentes;
- persistencia y LOD.

El Core no puede inventar tecnología ni clases militares.

## 2. Navegación

Un viaje necesita origen, destino, conexión navegable, embarcación capaz, tripulación suficiente y tiempo plausible.

Influyen:

- calado/profundidad;
- corriente;
- viento;
- estado del agua o mar;
- visibilidad;
- meteorología;
- luz;
- carga;
- condición del buque;
- competencia de tripulación;
- tráfico y acceso portuario.

## 3. Puertos

La llegada y salida utilizan un ciclo común: aproximación → espera si procede → asignación de atraque/fondeo → amarre → operación → estancia → preparación → liberación → salida.

La capacidad de puerto es finita y puede producir espera o desvío.

## 4. Daños

Casco, aparejo, mástiles, velas, gobierno, amarre, espacios de carga y equipo pueden dañarse.

El daño altera prestaciones y persiste. Reparar requiere recursos, tiempo, acceso y trabajo reales conforme a los sistemas Core existentes.

## 5. Encuentros y combate

El sistema universal resuelve detección, identificación incierta, evasión, persecución, intercepción, colisión, combate, abordaje, rendición, captura, rescate y consecuencias.

Las armas disponibles proceden del perfil cultural/institucional. El resolver nunca crea armamento nuevo.

## 6. Pesca y recursos acuáticos

Los caladeros son recursos espaciales persistentes.

La captura depende de recurso disponible, esfuerzo, tripulación, equipo, estación, clima, agua, competencia y presión de otros pescadores.

La pesca excesiva puede reducir rendimientos posteriores. La recuperación no es instantánea.

Si la ecología local no ha definido especies, el motor trabaja con grupos de recurso sin inventar nombres canónicos.

## 7. LOD y simulación off-screen

Alta: individuos, posiciones, objetos, acciones y daños concretos.

Media: grupos de tripulación, maniobra, componentes y carga agrupada.

Baja: identidad del barco, tramo de ruta, misión, estado agregado, carga, tripulación e incidentes.

Cambiar de LOD jamás cambia los hechos.

## 8. Regla de persistencia

Un barco visto hoy no se sustituye mañana por otro procedural. Puede cambiar de dueño, repararse, deteriorarse, ser capturado, hundirse o quedar abandonado, pero conserva continuidad causal.

## Regla final

**El agua no es un decorado ni los barcos son spawns: forman parte persistente del mismo mundo simulado que los NPC, edificios, rutas y mercancías.**
