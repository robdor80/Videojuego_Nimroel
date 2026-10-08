# Treskal — validación funcional integral v0.1

## Estado

**PLANO MÉTRICO — PUNTO 9 CERRADO**

Marcador:

`TRESKAL_METRIC_PLAN_POINT_9_INTEGRATED_VALIDATION_CLOSED`

Contrato:

`../Datos operativos/treskal_integrated_functional_validation_contract_v0.1.json`

Batería:

`../Validacion/treskal_metric_plan_point_9_validation_pack_v0.1.json`

---

## 1. Objetivo

El Punto 9 no rediseña Treskal.

Su objetivo es intentar romper el diseño cerrado en los Puntos 2–8 mediante pruebas cruzadas de:

- población;
- movilidad;
- carga;
- mercados;
- incendios;
- agua;
- residuos;
- inundación;
- puerto;
- Armada;
- ejército;
- accesos institucionales;
- crecimiento;
- emergencias.

Cualquier fallo no resuelto bloquearía el Punto 10.

---

## 2. Correcciones detectadas antes de probar

Se detectaron cuatro ambigüedades operativas.

### CFIX01 — población

Los 15.000 habitantes del Punto 8 podían interpretarse erróneamente como techo.

Corrección:

- 12.000–18.000 sigue siendo el rango canónico;
- 15.000 es la referencia de diseño;
- 18.000 es un estado de ocupación alta;
- no requiere regenerar parcelas ni ampliar la geometría macro.

### CFIX02 — agua urbana

W01–W10 tenían posición, pero no fuente segura asignada.

Se resolvieron como:

- pozos protegidos;
- cisternas cubiertas con recogida limpia y reposición por carros.

Existen **10 grupos de fuente independientes**.

El agua cruda del río no se declara potable automáticamente.

### CFIX03 — agua T08 / T12

T08 recibe:

- 2 cisternas limpias controladas;
- 2 puntos de toma de agua portuaria para incendios, no potable.

T12 recibe:

- 2 reservas/cisternas controladas para S11/S12.

### CFIX04 — residuos

Se fija la salida:

- orgánicos/estiércol → reutilización agrícola cuando sea plausible;
- otros residuos → eliminación controlada fuera del tejido denso;
- residuos de pescado → retirada prioritaria;
- río y puerto no son vertederos por defecto.

**Ninguna corrección mueve geometría.**

---

## 3. Población

### 12.000

**PASS**

Densidad sobre 110,7 ha:

~108 hab/ha.

### 15.000

**PASS**

Densidad:

~135,5 hab/ha.

### 18.000

**PASS CON RESTRICCIÓN**

Densidad:

~162,6 hab/ha.

Se consigue mediante mayor ocupación de:

- vivienda;
- edificios multihogar;
- usos residenciales mixtos.

No mediante generación de un barrio nuevo.

---

## 4. Movilidad

Resultado:

**PASS**

Treskal dispone de:

- 12,981 km de red principal/secundaria controlada;
- 18 ejes C;
- 12 vías locales L;
- un único Puente de los Gemelos.

Pueden evitar T03 por defecto:

- madera pesada;
- ganado;
- tráfico militar;
- suministro naval.

---

## 5. Alimentación y mercados

### Entrada de alimentos

**PASS**

Territorio → C02 → T10/T02 → distribución urbana.

### Mercado diario

**PASS CON RESTRICCIÓN**

S06 dispone de capacidad física y accesos.

Puede existir congestión local en horas punta.

Eso es comportamiento válido, no fallo del plano.

### Ganado

**PASS**

C02 → C14 → S10.

No necesita atravesar T03.

---

## 6. Madera

### Talleres urbanos

**PASS**

C03/C10/C13 → S09 → UF05/UF06.

### Astilleros Reales

**PASS**

La madera puede ir a T08 sin atravesar el centro comercial.

---

## 7. Puerto civil

### Mercante con atraques libres

**PASS**

### Mercante con atraques ocupados

**PASS CON RESTRICCIÓN**

El barco espera en CIV_ANCH_01.

No aparece un atraque mágico adicional.

### Retorno simultáneo de pesca

**PASS CON RESTRICCIÓN**

CP01/CP05 → S07 → C12.

La perecibilidad obliga a priorizar la descarga.

---

## 8. Armada

### Retorno de buque dañado

**PASS CON RESTRICCIÓN**

Puede usar:

- NFP02;
- NFP01;
- S08;
- una de las cinco gradas.

La disponibilidad real sigue dependiendo de:

- eslora;
- calado;
- ocupación;
- daño;
- trabajadores;
- materiales.

### Embarque de tropas

**PASS CON RESTRICCIÓN**

T12 / red territorial → C04/C05 → C16 → S13 → NFP03.

No existe capacidad infinita.

---

## 9. Inundación

### Crecida de diseño

**PASS CON RESTRICCIÓN**

Permanecen seguras:

- justicia;
- custodia;
- Guardia;
- T12;
- funciones sensibles en terrazas superiores.

Pueden perderse temporalmente:

- bordes de trabajo;
- navegación fluvial;
- instalaciones bajas reparables.

La ciudad no queda mágicamente inmune al agua.

---

## 10. Temporal marítimo

**PASS CON RESTRICCIÓN**

Puede reducirse o cerrarse:

- muelle mercante exterior;
- fondeo;
- determinadas operaciones navales.

NBW01 protege parte de T08.

El retraso de tráfico marítimo es una consecuencia real.

---

## 11. Incendio

### UF05

**PASS CON RIESGO RESIDUAL**

Fuentes próximas:

- primera ~95 m;
- segunda ~108 m.

Existen:

- L05;
- C10;
- C13;
- patios;
- interrupciones de frente.

### UF06

**PASS CON RIESGO RESIDUAL**

Primera fuente:

~205 m.

Segunda:

~284 m.

Es peor que UF05, pero funcional.

Un incendio serio puede causar daños antes de ser controlado.

### S08

**PASS CON RESTRICCIÓN**

Dispone de:

- respuesta interna;
- separación de forjas;
- separación de madera;
- dos puntos de toma de agua para incendios.

No existe brigada moderna.

---

## 12. Agua

### Fallo de un nodo urbano

**PASS**

Quedan otros nueve grupos independientes.

Puede aumentar:

- distancia;
- cola;
- presión sobre fuentes vecinas.

Pero la ciudad no depende de un único suministro.

---

## 13. Residuos

### Retraso de recogida

**PASS CON RESTRICCIÓN**

Los residuos permanecen físicamente.

Pueden aumentar:

- olor;
- plagas;
- presión de servicio.

No desaparecen por cambio de LOD.

---

## 14. Puente bloqueado

**PASS CON RIESGO RESIDUAL**

La ciudad principal de la margen este continúa funcionando internamente.

Se conserva acceso regional norte y este.

Pero el acceso occidental directo queda cortado.

No se crea un segundo puente para eliminar el problema.

---

## 15. Pico simultáneo

Mercado + puerto + talleres:

**PASS CON RESTRICCIÓN**

Pueden aparecer colas locales.

La existencia de:

- C06;
- C07;
- C11;
- C13;
- C18;
- rutas pesadas alternativas;

impide que todo el tráfico tenga que usar una única calle.

---

## 16. Cierre de T08

**PASS**

Un cierre naval puede aislar:

- C05 interior;
- C16;
- S08;
- S13.

T07 y el resto de la ciudad pueden seguir funcionando.

---

## 17. Movilización T12

**PASS CON RESTRICCIÓN**

S12 admite 800–1.200 personas en actividad.

Requiere:

- agua;
- suministros;
- regulación temporal del tráfico.

No genera recursos automáticamente.

---

## 18. Crecimiento

**PASS CON RESTRICCIÓN**

Quedan **25,82 ha** de reserva.

Para ocuparlas deben extenderse:

- vías;
- agua;
- residuos;
- servicios.

No aparecen barrios instantáneos.

---

## 19. Riesgos residuales aceptados

Treskal no es una ciudad diseñada para no fallar.

Conserva cinco riesgos reales:

1. puente permanente único;
2. incendio por concentración de madera;
3. temporales e inundaciones;
4. capacidad portuaria/naval finita;
5. dependencia de trabajo humano para agua, mantenimiento y saneamiento.

Estos riesgos son **parte del mundo**, no errores que deban eliminarse.

---

## 20. Resultado

Escenarios de estrés:

**24**

Fallos sin resolver:

**0**

Correcciones geométricas:

**0**

Clarificaciones operativas:

**4**

Decisiones de autor pendientes:

**0**

Conclusión:

**TRESKAL FUNCIONA A SU ESCALA CANÓNICA.**

---

## Siguiente

**Punto 10 — Mapa canónico definitivo.**

El Punto 10 podrá:

- materializar gráficamente manzanas y parcelas;
- producir el plano técnico;
- producir el plano legible para lore;
- producir el plano operativo para juego.

No podrá rediseñar lo ya validado.

---

## Regla final

**El plano de Treskal ya ha dejado de ser una hipótesis urbana: ha superado su validación funcional integral.**

`TRESKAL_METRIC_PLAN_POINT_9_INTEGRATED_VALIDATION_CLOSED`
