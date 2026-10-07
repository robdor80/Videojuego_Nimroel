# Treskal — nacimiento, recién nacido y primera infancia v0.1

> **MIGRADO A NIMROEL CORE — documentación derivada con override local explícito.** La autoridad normativa de PREG reside en `Worldbuilding/Sistemas/Nimroel Core/02_Ciclo_vital_y_hogar/embarazo_nacimiento_primera_infancia_v0.1.md`. Las particularidades de Treskal sobre lugar habitual y asistencia del parto se conservan exclusivamente en `localOverrides` del contrato local; fuera de esas excepciones prevalece el Core.

## Estado

**DISEÑO DE WORLD STATE APROBADO — CADA NACIMIENTO CREA UNA PERSONA PERSISTENTE**

## Objetivo

Definir qué ocurre en Treskal después de un nacimiento vivo y cómo se integra un recién nacido en hogar, demografía, cuidados, descanso, trabajo, alimentación, higiene, viajes y relaciones.

Sin fijar todavía edades exactas de desarrollo ni costumbres formales de nombramiento. La tutela jurídica ya se hereda del Punto 6 de Norgard.

---

# 1. Nuevo NPC

Cada nacimiento vivo crea un npc_id estable.

El recién nacido no es:

- un objeto de inventario;
- una animación temporal;
- un accesorio del NPC adulto;
- un contador abstracto de población.

Es una nueva persona persistente del mundo.

Si hay más de un nacimiento vivo en el mismo parto, cada niño recibe su propio npc_id.

---

# 2. Identidad mínima

Al crearse debe poder vincularse con:

- birth_event_id;
- household_ref;
- home_location_ref;
- relaciones familiares conocidas;
- caso de cuidado;
- etapa vital correspondiente.

El nombre visible puede depender de canon futuro.

La falta temporal de un nombre definitivo no impide que exista identidad técnica estable.

---

# 3. Hogar

El nacimiento modifica el household existente.

No crea automáticamente una vivienda mayor, una habitación adicional, una cama moderna específica ni recursos gratuitos.

La capacidad doméstica debe absorber la nueva realidad o generar presión.

---

# 4. Dependencia

Un recién nacido entra en DEP01 — child_care con dependencia práctica alta.

Necesita cobertura CARE real.

La existencia de progenitores no significa automáticamente que ambos estén presentes, disponibles, sanos, descansados o viviendo en el mismo hogar.

---

# 5. Red de cuidados

Los cuidadores pueden incluir, cuando exista relación y disponibilidad:

- madre;
- otro progenitor;
- abuelos;
- familiares;
- miembros del hogar;
- red de apoyo cercana.

No existe guardería institucional automática.

Los vecinos no se convierten en cuidadores por proximidad.

---

# 6. Tiempo

Cuidar a un recién nacido consume presencia, tiempo, descanso, organización, espacio, alimentos y recursos del hogar.

La intensidad concreta se abstrae según LOD.

---

# 7. Sueño

El recién nacido puede interrumpir el descanso de cuidadores.

REST debe reflejarlo cuando sea relevante.

No todos los miembros del hogar sufren idéntica interrupción. La proximidad, reparto de cuidados y disposición de la vivienda importan.

---

# 8. Trabajo

La nueva carga CARE puede reducir disponibilidad laboral de uno o más cuidadores.

Eso puede producir retrasos, relevos, menor jornada efectiva, ayuda familiar o tensión doméstica.

No existe permiso laboral moderno garantizado por este documento.

---

# 9. Alimentación

El recién nacido requiere alimentación adecuada a su etapa.

Este documento no fija fisiología detallada, cantidades, intervalos, sustitutos concretos ni reglas médicas de lactancia.

La simulación solo debe representar los recursos y cuidados necesarios al nivel apropiado de detalle.

---

# 10. Higiene y ropa

El cuidado aumenta necesidades domésticas relacionadas con lavado, agua, textiles, limpieza y calor según clima.

HYGIENE, GAR, FUEL y CHORE absorben esas consecuencias sin crear tecnología moderna.

---

# 11. Desplazamiento

Viajar con un recién nacido puede requerir más tiempo, protección, pausas, carga adicional y cuidadores disponibles.

No se trata como un objeto que el adulto guarda en inventario.

---

# 12. Espacio público

Un adulto cuidador puede aparecer con el niño en contextos compatibles.

Eso no obliga a materializar siempre al bebé en alto detalle si el sistema de LOD permite una representación simplificada, pero el niño sigue existiendo en World State.

---

# 13. Primera infancia

A medida que el niño crece cambian dependencia, movilidad, juego, supervisión y participación doméstica futura.

Las edades exactas y los hitos se definirán en el sistema de ciclo vital.

Este documento no inventa umbrales numéricos.

---

# 14. Relaciones

El nacimiento puede modificar vínculos familiares, cargas de cuidado, rutinas y planes residenciales.

No cambia automáticamente AFF entre adultos.

Un nacimiento no crea matrimonio, reconciliación ni propiedad compartida.

---

# 15. Conocimiento social

La existencia del niño puede hacerse conocida mediante visitas, familia, vecinos, actividad pública, conversación o rumor.

No toda la ciudad recibe un evento global de nacimiento.

K, CONV y HEAR siguen gobernando la información.

---

# 16. Nombre y reconocimiento formal

El Punto 6 de Norgard ya regula:

- filiación jurídica;
- reconocimiento;
- tutela;
- adopción.

Este documento sigue sin establecer cuándo se asigna nombre, quién lo elige, ceremonia o reglas generales de apellido. Esas materias permanecen para el canon de nombres y apellidos de Norgard.

---

# 17. Salud y mortalidad

El recién nacido puede enfermar o morir si HLTH/HCOND lo determinan.

No se fijan probabilidades universales aquí.

Si muere, MORT se aplica, la familia conserva memoria, el hogar y CARE se recalculan y el NPC no se borra retroactivamente de la historia.

---

# 18. Persistencia offscreen

Un niño continúa creciendo cuando el jugador está lejos si el sistema temporal lo permite.

No desaparece, cambia de familia, alcanza una nueva etapa o aprende capacidades sin que World State y el sistema de ciclo vital lo justifiquen.

---

## Regla final

**En Treskal un nacimiento añade una vida al mundo, no una cifra a una tabla: ese niño ocupa un hogar, necesita personas, altera rutinas y conserva una historia propia desde el primer día.**
