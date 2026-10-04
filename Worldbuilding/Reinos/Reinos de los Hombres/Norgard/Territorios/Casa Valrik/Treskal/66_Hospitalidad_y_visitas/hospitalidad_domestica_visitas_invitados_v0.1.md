# Treskal — hospitalidad doméstica, visitas e invitados v0.1

## Estado

**DISEÑO SOCIAL/JUGABLE APROBADO — HOSPITALIDAD COMO RELACIÓN TEMPORAL**

## Objetivo

Definir cómo una persona puede:

- visitar un hogar;
- entrar legítimamente;
- compartir comida;
- permanecer unas horas;
- dormir una o varias noches;
- guardar temporalmente pertenencias;

sin convertir una invitación en:

- residencia;
- propiedad;
- acceso permanente;
- derecho sobre todo el edificio.

---

# 1. Principio

La hospitalidad es una autorización social temporal.

Puede ampliar acceso a una vivienda P3 sin cambiar:

- owner_ref;
- household_id;
- resident_state;
- derechos futuros de propiedad.

---

# 2. Estados de hospitalidad

## HOSP01 — invited_visit

Invitado a una visita concreta.

## HOSP02 — welcomed_present

Está dentro y es huésped aceptado.

## HOSP03 — shared_meal

Participa en comida/bebida doméstica.

## HOSP04 — overnight_guest

Puede dormir en el hogar durante una estancia temporal.

## HOSP05 — extended_guest

Permanece varios días sin convertirse en residente.

## HOSP06 — invitation_ended

La autorización terminó.

## HOSP07 — unwelcome_or_revoked

El anfitrión retiró la hospitalidad.

---

# 3. Invitación

Puede proceder de una persona con autoridad doméstica suficiente.

La invitación puede limitarse a:

- persona;
- momento;
- estancia;
- parte del edificio;
- actividad.

No abre automáticamente:

- dormitorios ajenos;
- almacenes;
- taller;
- contenedores;
- zonas restringidas.

---

# 4. Entrada

Una invitación puede conceder permiso social.

Todavía puede ser necesario:

- llamar;
- esperar;
- que alguien abra;
- usar una llave temporal si se presta.

Permiso y acceso físico siguen separados.

---

# 5. Visita ordinaria

Puede incluir:

- conversación;
- comida;
- ayuda;
- celebración futura;
- duelo;
- negocios informales;
- cuidado.

No todas las visitas implican comer o dormir.

---

# 6. Comida compartida

HOSP03 consume recursos reales del hogar.

Puede afectar:

- stock de comida;
- preparación;
- tiempo.

Una visita inesperada no genera comida infinita.

---

# 7. Huésped nocturno

HOSP04 necesita capacidad real para descansar.

Puede usar:

- cama disponible;
- espacio de descanso;
- estancia compartida compatible.

No crea dormitorio nuevo.

---

# 8. Estancia prolongada

HOSP05 puede durar varios días.

Aun así:

- no convierte automáticamente a la persona en RES01;
- no la añade definitivamente al household;
- no altera propiedad de objetos.

Puede ser transición hacia residencia si luego ocurre un cambio real.

---

# 9. Pertenencias del invitado

Un huésped puede dejar:

- ropa;
- bolsa;
- herramienta;
- otros objetos.

Los objetos mantienen owner_ref.

location_ref cambia al hogar.

---

# 10. Custodia

El hogar puede asumir custodia temporal de pertenencias.

Eso no transfiere propiedad.

---

# 11. Privacidad

Un invitado no recibe automáticamente acceso a conversaciones privadas del hogar.

CONV y HEAR siguen aplicándose.

---

# 12. Niños y dependientes

Una visita puede incluir cuidado o supervisión temporal.

Eso puede enlazar con CARE.

No toda visita familiar es un caso de cuidado.

---

# 13. Duelo

Durante las tres jornadas de luto:

el hogar puede recibir:

- familiares;
- amigos;
- vecinos;
- compañeros.

La hospitalidad puede ser más abierta socialmente sin volver pública la vivienda.

---

# 14. Conflicto

La hospitalidad puede terminar por:

- tiempo;
- decisión;
- comportamiento;
- discusión;
- necesidad doméstica;
- evento.

HOSP07 puede afectar relaciones.

No convierte automáticamente al invitado en delincuente; depende de si permanece contra permiso y del futuro sistema legal.

---

# 15. Negativa

Un hogar puede rechazar una visita por:

- descanso;
- enfermedad;
- duelo;
- falta de confianza;
- trabajo;
- privacidad;
- falta de espacio.

No toda negativa es hostilidad.

---

# 16. Horario

No existe horario universal de visita.

La plausibilidad depende de:

- REST;
- rutina;
- relación;
- urgencia;
- contexto.

---

# 17. Invitación abierta

Puede existir una costumbre de:

- “pásate cuando quieras”;
- acceso habitual de familiar o amigo.

Aun así puede revocarse y no equivale a residencia.

---

# 18. Invitado y negocio

En casa-taller:

el invitado puede tener acceso a zona doméstica y no al taller, o al revés.

La invitación debe respetar subespacios.

---

# 19. IA

La IA puede invitar, aceptar o terminar visita.

El motor valida:

- autoridad del anfitrión;
- acceso;
- capacidad;
- estado doméstico.

No crea permisos permanentes por una frase ambigua.

---

## Regla final

**En Treskal ser bienvenido en una casa significa que alguien te abre su vida durante un tiempo; no que la casa pase a pertenecerte ni que todas sus puertas sean tuyas.**
