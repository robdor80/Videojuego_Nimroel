# Treskal — sueño, descanso y disponibilidad cotidiana v0.1

## Estado

**DISEÑO DE VIDA COTIDIANA APROBADO — DESCANSO REAL SIN HORARIOS MODERNOS**

## Objetivo

Definir cómo el descanso afecta a:

- rutina;
- disponibilidad;
- trabajo;
- visitas;
- guardias;
- viajes;
- interrupciones.

Sin fijar:

- horas universales de sueño;
- barra numérica de fatiga;
- fisiología detallada.

---

# 1. Principio

Un NPC no está disponible de forma continua.

Puede encontrarse:

- trabajando;
- comiendo;
- desplazándose;
- descansando;
- durmiendo;
- atendiendo asuntos privados;
- de guardia;
- ausente.

La simulación no debe tratar a los habitantes como servicios 24/7.

---

# 2. Estados conceptuales de descanso

## REST01 — active

Actividad ordinaria.

## REST02 — short_rest

Pausa breve.

## REST03 — off_duty

No está trabajando, aunque puede estar despierto y disponible socialmente.

## REST04 — preparing_sleep

Cierre de actividad y preparación para dormir.

## REST05 — sleeping

Sueño principal.

## REST06 — interrupted

El descanso fue interrumpido.

## REST07 — recovering

Periodo posterior a esfuerzo, noche excepcional o interrupción relevante.

Estos estados no sustituyen al futuro sistema fisiológico.

---

# 3. Sueño

El sueño principal suele ocurrir en:

- hogar;
- habitación de posada;
- alojamiento temporal;
- otro espacio legítimo y razonablemente seguro.

No se presume que toda persona tenga dormitorio individual.

---

# 4. Hogar y descanso

La vivienda debe proporcionar capacidad real para que sus ocupantes descansen.

Puede existir:

- reparto de espacios;
- camas compartidas cuando el canon doméstico lo permita;
- superficies de descanso;
- habitaciones comunes.

No se fija una configuración única.

---

# 5. Oficios con ritmos distintos

Algunos trabajos alteran la rutina ordinaria:

- pescadores;
- panaderos;
- taberneros;
- guardia;
- puerto;
- emergencias;
- viajes.

Eso puede desplazar REST05 a otra franja.

No se obliga a dormir siempre de noche.

---

# 6. Guardia y turnos

Una función que necesita continuidad puede usar relevo.

Este documento no fija:

- número de turnos;
- rangos;
- duración;
- plantilla.

Sí fija que un guardia nocturno no puede simultáneamente estar durmiendo en casa.

---

# 7. Interrupción

REST05 puede interrumpirse por:

- incendio;
- alarma;
- visitante;
- accidente;
- enfermedad familiar;
- mensaje urgente;
- ruido extraordinario;
- evento.

La interrupción debe tener causa.

---

# 8. Disponibilidad social

Un NPC en REST03 puede:

- hablar;
- visitar;
- ir a taberna;
- atender familia.

Un NPC en REST05 normalmente no está disponible salvo:

- emergencia;
- convivencia;
- acceso legítimo.

---

# 9. Negocios

Que el propietario esté despierto no significa que el negocio esté abierto.

BIZ y REST son estados separados.

---

# 10. Posadas

Una posada puede seguir operativa mientras parte del personal descansa.

La capacidad depende de:

- plantilla;
- relevo;
- ocupación;
- hora;
- evento.

No exige personal completo activo toda la noche.

---

# 11. Viaje

Un viajero puede necesitar detenerse para:

- dormir;
- comer;
- cuidar animales;
- recuperar rutina.

Un viaje largo no se resuelve como movimiento ininterrumpido salvo sistema que lo justifique.

---

# 12. Esfuerzo excepcional

Una noche de:

- temporal;
- incendio;
- emergencia;
- guardia prolongada

puede producir REST07.

El efecto fisiológico exacto queda para el sistema de necesidades futuro.

---

# 13. Niños

El descanso infantil debe diferenciarse de actividad adulta.

No se fija horario exacto.

La rutina depende de:

- edad;
- hogar;
- familia;
- evento.

---

# 14. Enfermos

Un NPC enfermo puede pasar más tiempo en:

- REST02;
- REST05;
- REST07.

La salud decide la necesidad.

El descanso no cura automáticamente.

---

# 15. IA

El contexto de diálogo puede incluir:

- rest_state;
- disponibilidad;
- causa de interrupción;
- última actividad importante.

La IA no despierta al NPC por conveniencia del jugador.

---

# 16. LOD

En LOD bajo puede resolverse:

- franja activa;
- descanso;
- ausencia;
- recuperación

de forma agregada.

Al materializar:

el NPC aparece en un lugar compatible con su estado.

---

## Regla final

**Dormir y descansar forman parte del World State: un habitante de Treskal no deja de tener vida privada porque el jugador quiera hablar con él.**
