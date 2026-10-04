# Treskal — integración causal entre sistemas urbanos v0.1

## Estado

**CONTRATO TRANSVERSAL APROBADO — ORDEN DE CAUSAS Y EFECTOS**

## Objetivo

Evitar que los sistemas de Treskal funcionen como islas.

Una misma causa puede afectar a:

- clima;
- rutas;
- trabajo;
- stock;
- precios;
- hogares;
- negocios;
- conocimiento;
- reputación;
- IA.

Pero cada efecto debe aplicarse una sola vez y a través del sistema responsable.

---

# 1. Principio central

El World State contiene hechos.

Los sistemas:

1. leen hechos autorizados;
2. calculan cambios propios;
3. escriben únicamente los campos de los que son responsables;
4. emiten efectos para otros sistemas.

No se permite que varios sistemas modifiquen el mismo hecho de manera independiente sin coordinación.

---

# 2. Capas

## Capa A — mundo físico

- edificios;
- accesos;
- objetos;
- clima acumulado;
- daños;
- obras;
- rutas;
- vehículos;
- barcos.

## Capa B — actividad

- trabajo;
- negocios;
- mercados;
- producción;
- consumo;
- entregas;
- encargos;
- construcción.

## Capa C — población

- NPC;
- hogares;
- empleo;
- residencia;
- salud;
- rutinas;
- visitantes.

## Capa D — información social

- conocimiento;
- rumores;
- mensajes;
- reputación;
- pledges.

## Capa E — presentación

- LOD;
- audio;
- visual;
- diálogo;
- narrador IA.

La capa E nunca crea hechos de A–D.

---

# 3. Orden general de actualización

Orden conceptual:

1. tiempo y clima;
2. eventos externos;
3. estado físico;
4. accesos y navegación;
5. movilidad y transporte;
6. trabajo y producción;
7. entregas y almacenamiento;
8. consumo y mercado;
9. negocios y empleo;
10. hogares/residencia/salud;
11. conocimiento y reputación;
12. selección de LOD;
13. contexto IA y presentación.

No implica un único tick global obligatorio.

Sí implica causalidad.

---

# 4. Ejemplo — temporal marítimo

Secuencia posible:

**clima → D01/EVT → puerto → barcos → entregas → pescado/stock → mercado → precio/disponibilidad → negocios → rutinas → conocimiento → diálogo**

No se permite:

- modificar precio directamente desde el clima;
- añadir rumor antes de que exista una fuente;
- vaciar una tienda sin afectar stock real.

---

# 5. Ejemplo — incendio

Secuencia posible:

**ignición → EVT → daño → acceso/ruta → heridos → desplazamiento → stock perdido → negocio reducido/cerrado → reparación → empleo → rumor/reputación**

El incendio no:

- repara automáticamente al resolverse;
- informa a toda la ciudad;
- crea reemplazos instantáneos.

---

# 6. Ejemplo — llegada de mercante

Secuencia:

**barco → atraque → descarga → custodia/almacén → traslado → stock de proveedor → mercado/negocio → visitantes → posadas → rumor**

La mercancía no salta:

**barco → tienda**.

---

# 7. Ejemplo — enfermedad de artesano

Secuencia:

**salud → EMP03/EMP04 → capacidad de negocio → COM → plazos → clientes → pledge si existe → reputación solo si el incumplimiento se conoce y se interpreta**

La reputación no cae automáticamente por enfermedad.

---

# 8. Ejemplo — lluvia prolongada

Secuencia:

**weather → ENV → tráfico/secado → transporte → entrega → stock → actividad**

La lluvia no cambia stock directamente.

---

# 9. Ejemplo — mudanza

Secuencia:

**MOVE → transporte de bienes → home_location → household → rutina → wayfinding → conocimiento de terceros → mapas/IA**

El NPC conserva:

- identidad;
- recuerdos;
- profesión;
- relaciones.

---

# 10. Autoridad de escritura por dominio

## físico

Responsables:

- construcción;
- mantenimiento;
- propiedad;
- accesos;
- clima acumulado.

## economía

Responsables:

- stock;
- consumo;
- mercados;
- negocios;
- encargos.

## población

Responsables:

- NPC;
- empleo;
- residencia;
- salud.

## conocimiento

Responsables:

- información;
- mensajería;
- reputación;
- pledges.

## presentación

Solo lectura autorizada.

---

# 11. Efecto derivado vs hecho persistente

Ejemplo:

**traffic_cost** puede ser derivado.

Pero:

**puente destruido** es persistente.

No guardar de forma redundante un valor derivado si puede reconstruirse con seguridad.

---

# 12. Idempotencia

Un mismo EVT no debe:

- descontar dos veces stock;
- aplicar dos veces daño;
- duplicar rumor;
- duplicar desplazamiento.

Cada efecto importante necesita:

- source_ref;
- application_id o equivalente;
- estado aplicado.

---

# 13. Orden de información

Un hecho puede existir sin ser conocido.

Secuencia:

**hecho → percepción/mensaje/testigo → K → memoria → diálogo**

Nunca:

**hecho oculto → diálogo directo**.

---

# 14. IA

La IA recibe:

- hechos visibles;
- hechos conocidos por el actor;
- relaciones relevantes;
- contexto de escena;
- acciones válidas.

No recibe:

- verdad oculta completa;
- inventario global;
- ubicaciones secretas;
- resultados futuros.

---

# 15. LOD

El cambio de LOD puede modificar:

- granularidad;
- representación;
- frecuencia de actualización.

No puede modificar:

- propietario;
- stock real;
- identidad;
- daño;
- relación;
- conocimiento;
- compromiso;
- evento.

---

# 16. Guardado

El save debe priorizar:

- hechos persistentes;
- deltas;
- identidades;
- relaciones;
- eventos;
- estados relevantes.

No es necesario guardar cada valor visual derivable.

---

# 17. Resolución de conflictos

Si dos sistemas intentan producir cambios incompatibles:

1. se identifica el hecho base;
2. se aplica autoridad del dominio;
3. se conserva la causa;
4. se recalculan derivados.

No se resuelve por orden accidental de ejecución.

---

## Regla final

**En Treskal cada cambio debe poder responder a dos preguntas: qué lo causó y qué sistema tenía autoridad para aplicarlo.**
