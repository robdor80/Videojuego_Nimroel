# Treskal — embarazo, parto y recuperación doméstica v0.1

> **MIGRADO A NIMROEL CORE — documentación derivada con override local explícito.** La autoridad normativa de PREG reside en `Worldbuilding/Sistemas/Nimroel Core/02_Ciclo_vital_y_hogar/embarazo_nacimiento_primera_infancia_v0.1.md`. Las particularidades de Treskal sobre lugar habitual y asistencia del parto se conservan exclusivamente en `localOverrides` del contrato local; fuera de esas excepciones prevalece el Core.

## Estado

**DISEÑO SOCIAL/JUGABLE APROBADO — EVENTO VITAL PERSISTENTE, NO DECORATIVO**

## Objetivo

Definir cómo un embarazo y un parto afectan al World State de Treskal.

Siguen fuera de este documento:

- duración exacta de etapas;
- probabilidades médicas;
- mecánica de concepción;
- medicina obstétrica detallada;
- rito de nombramiento.

Matrimonio, filiación jurídica y tutela ya se rigen por el Punto 6 de Norgard.

La fisiología sanitaria y las complicaciones se resuelven ya mediante el Core de salud; la temporización exacta del ciclo reproductivo sigue perteneciendo al futuro sistema de ciclo vital.

---

# 1. El embarazo es World State

Un embarazo relevante existe aunque:

- el jugador no esté presente;
- la persona no lo haya contado;
- no haya señales visibles evidentes;
- la ciudad esté en LOD bajo.

No aparece o desaparece para acomodar una escena.

---

# 2. Estados operativos

## PREG01 — early_pregnancy

Etapa inicial. No se fija duración exacta.

## PREG02 — established_pregnancy

El embarazo está establecido en World State. Quién lo conoce sigue siendo una cuestión separada.

## PREG03 — late_pregnancy

Etapa avanzada. Puede afectar de forma creciente esfuerzo, descanso, desplazamientos, tareas y disponibilidad laboral, sin implicar incapacidad automática.

## PREG04 — active_labor

El parto está en curso. Puede alterar de inmediato rutina del hogar, disponibilidad de cuidadores, prioridad de una curandera, acceso y privacidad.

## PREG05 — resolved_live_birth

El embarazo concluye con uno o más nacimientos vivos. Cada recién nacido se convierte en NPC persistente.

## PREG06 — resolved_without_live_birth

El embarazo concluye sin nacimiento vivo. Las causas y consecuencias médicas exactas pertenecen al sistema de salud.

---

# 3. Origen del embarazo

AFF05, convivencia o matrimonio futuro no generan embarazo automáticamente.

La existencia de embarazo debe proceder de un evento válido del futuro sistema de ciclo vital/reproducción.

La IA narrativa no puede crear un embarazo porque encaje bien en una historia.

---

# 4. Conocimiento y privacidad

La verdad del World State y el conocimiento de los NPC son distintos.

Un NPC puede saberlo porque se lo contaron, inferirlo por signos visibles, sospecharlo o no saberlo.

Una sospecha no equivale a conocimiento cierto.

El narrador tampoco debe revelar un embarazo privado si el jugador no dispone de información perceptible o autorizada.

---

# 5. Trabajo

El embarazo no prohíbe universalmente trabajar.

La actividad puede adaptarse según etapa, salud, oficio, esfuerzo físico, distancia, descanso y apoyo del hogar.

No existe baja maternal legal universal definida en este documento.

EMP, REST y salud conservan su autoridad.

---

# 6. Hogar y apoyo

La carga del hogar puede cambiar por menor disponibilidad para ciertas tareas, necesidad de ayuda, preparación de espacio, reorganización de trabajo y acompañamiento.

CARE y CHORE pueden redistribuir tiempo antes del parto sin crear automáticamente un cuidador disponible.

---

# 7. Lugar del parto

En Treskal, coherentemente con la red sanitaria ya canonizada, el parto puede ocurrir normalmente en vivienda, alojamiento habitual u otro lugar doméstico seguro y plausible si las circunstancias lo requieren.

No se presupone hospital, maternidad ni sala obstétrica central.

---

# 8. Asistencia

Una curandera formada puede tener experiencia en partos.

Su presencia depende de disponibilidad, distancia, aviso, acceso, urgencia y otros casos que esté atendiendo.

La ciudad no teletransporta una especialista al lugar.

Este documento no crea todavía una profesión separada y universal de comadrona.

---

# 9. Red doméstica durante el parto

Pueden participar personas del hogar o red cercana cuando existe relación, están presentes, pueden ayudar y la privacidad lo permite.

No se fuerza una composición ritual fija.

---

# 10. Urgencia

PREG04 puede elevar la prioridad práctica de atención.

No garantiza resultado favorable.

WAIT, desplazamiento de la curandera y capacidad sanitaria siguen siendo reales.

---

# 11. Complicaciones

Este documento admite parto normal, complicaciones, necesidad de atención, recuperación difícil, pérdida gestacional o muerte.

No fija porcentajes universales.

Las consecuencias concretas se resuelven mediante HCOND18 y demás condiciones sanitarias aplicables.

---

# 12. Recuperación

Tras el parto, la madre no retorna automáticamente a su rutina previa.

La recuperación puede afectar REST, EMP, CHORE, CARE, movilidad y ocio.

La duración depende de HLTH/HCOND, gravedad, cuidados, descanso, recursos y tiempo; no existe recuperación instantánea.

---

# 13. Fallecimiento

Si muere la madre o un recién nacido:

- se registra la muerte;
- se aplican MORT y las reglas de duelo;
- el hogar y la red CARE se recalculan;
- no se revierte el evento para proteger una rutina o misión.

---

# 14. LOD

Un parto puede resolverse fuera de cámara únicamente si existía embarazo válido, la progresión temporal lo permite, la persona se encontraba en una ubicación coherente y se resuelve disponibilidad de ayuda y salud conforme a los sistemas propietarios.

No aparece un bebé simplemente porque hayan pasado varios días.

---

## Regla final

**El embarazo y el parto forman parte de la vida persistente de Treskal: suceden a personas reales, consumen tiempo y apoyo reales y dejan consecuencias reales aunque el jugador no esté mirando.**
