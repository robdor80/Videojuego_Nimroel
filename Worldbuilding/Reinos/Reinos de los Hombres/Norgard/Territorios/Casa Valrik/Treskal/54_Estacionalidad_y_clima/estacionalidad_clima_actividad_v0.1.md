# Treskal — estacionalidad, clima acumulado y actividad urbana v0.1

## Estado

**DISEÑO AMBIENTAL/JUGABLE APROBADO — CALENDARIO PUNTO 12 INTEGRADO**

## Base territorial

El sur de Valrik, incluida Treskal, posee clima oceánico suave:

- veranos moderados;
- inviernos relativamente templados;
- influencia marítima;
- lluvia, viento y humedad como factores habituales.

El calendario exacto se resuelve mediante Nimroel Core + Punto 12 de Norgard.

---

# 1. Principio

El clima afecta a Treskal de dos formas:

## estado inmediato

Qué ocurre ahora:

- lluvia;
- viento;
- niebla;
- temporal;
- tiempo estable.

## memoria ambiental

Qué ha ocurrido durante horas o días:

- suelo mojado;
- barro;
- madera húmeda;
- ropa húmeda;
- reservas de combustible afectadas;
- secado retrasado.

El estado inmediato no borra automáticamente la memoria ambiental.

---

# 2. Contexto estacional

La estación futura puede modificar probabilidades y necesidades:

- lluvia;
- temperatura;
- duración de luz;
- demanda de combustible;
- ropa;
- actividad exterior;
- oferta agrícola;
- pesca;
- secado.

Punto 12 fija:

- primavera: marzo–mayo;
- verano: junio–agosto;
- otoño: septiembre–noviembre;
- invierno: diciembre–febrero.

La estación civil no fuerza un cambio meteorológico instantáneo.

---

# 3. Estados ambientales acumulados

## ENV01 — dry_or_stable

Superficies razonablemente secas.

## ENV02 — damp

Humedad visible, sin barro dominante.

## ENV03 — wet

Lluvia reciente o humedad persistente.

## ENV04 — muddy

Tránsito y agua han degradado suelo no pavimentado.

## ENV05 — saturated_or_waterlogged

Condición local severa con drenaje insuficiente o lluvia prolongada.

## ENV06 — drying

Mejora progresiva tras periodo húmedo.

Estos estados son locales.

No toda Treskal comparte necesariamente el mismo ENV.

---

# 4. Localidad

El estado depende de:

- firme;
- drenaje;
- sombra;
- exposición;
- tránsito;
- pendiente;
- proximidad al río/mar;
- mantenimiento.

Una calle principal drenada puede secarse antes que un patio de tierra.

---

# 5. Lluvia

Puede producir:

- reducción de visibilidad;
- superficies mojadas;
- menor actividad exterior;
- ropa húmeda;
- carga protegida;
- barro si persiste;
- secado lento.

Una lluvia breve no convierte toda la ciudad en lodazal.

---

# 6. Viento

Puede afectar:

- sensación térmica;
- secado;
- navegación;
- humo;
- toldos;
- ropa;
- fuentes portátiles de luz.

No siempre tiene efecto negativo.

---

# 7. Niebla

Afecta principalmente:

- visibilidad;
- orientación;
- puerto;
- reconocimiento.

No genera humedad extrema por sí sola en todos los sistemas.

---

# 8. Temporal

D01 sigue siendo un evento extraordinario.

Puede añadir:

- daños;
- interrupción portuaria;
- lluvia intensa;
- viento;
- retrasos.

El temporal no sustituye al sistema climático ordinario.

---

# 9. Suelo y tráfico

ENV03–ENV05 pueden elevar coste de:

- carro;
- ganado;
- peatón;
- convoy.

El efecto depende del tipo de superficie.

No todo camino urbano responde igual.

---

# 10. Trabajo exterior

Actividades especialmente sensibles:

- carga;
- mercado expuesto;
- construcción;
- madera en patio;
- pesca;
- transporte;
- secado.

Pueden:

- continuar;
- reducirse;
- pausarse;
- trasladarse parcialmente.

---

# 11. Mercado

La lluvia puede cambiar:

- afluencia;
- número de puestos expuestos;
- tiempo de permanencia;
- necesidad de protección.

No cancela automáticamente el mercado diario.

---

# 12. Construcción

La obra puede ralentizarse si:

- materiales deben permanecer secos;
- el suelo se degrada;
- el trabajo es inseguro.

No toda fase se detiene por lluvia.

---

# 13. Madera

La cultura de madera debe considerar:

- almacenamiento cubierto;
- secado;
- humedad superficial;
- transporte bajo lluvia.

La madera no cambia de W-state útil automáticamente por mojarse unas horas.

El sistema detallado decide consecuencias cuando proceda.

---

# 14. Combustible

Periodos húmedos pueden:

- dificultar secado;
- aumentar demanda térmica;
- reducir calidad práctica de leña mal protegida.

El stock sigue existiendo aunque esté húmedo.

---

# 15. Ropa

El clima puede alterar:

- wetness;
- contextual_soiling;
- drying_time;
- necesidad de cambio.

No cambia base_patina.

---

# 16. Puerto

El puerto puede operar con lluvia ordinaria.

La limitación aumenta con:

- viento;
- oleaje;
- visibilidad;
- temporal;
- seguridad de carga.

No se usa “llueve = puerto cerrado”.

---

# 17. Pesca

La actividad puede variar por:

- estado del mar;
- viento;
- visibilidad;
- seguridad.

No toda lluvia reduce captura.

---

# 18. Estación cálida

Sin fijar fechas, puede tender a:

- más actividad exterior;
- secado más rápido;
- menor demanda térmica;
- fiestas locales estivales cuando el calendario las defina.

No se presupone calor extremo.

---

# 19. Estación fría

Puede tender a:

- mayor demanda de combustible;
- ropa más pesada;
- más actividad interior;
- secado más lento.

En Treskal sigue siendo relativamente templada frente al norte de Valrik.

---

# 20. Transiciones

Los cambios estacionales deben ser graduales.

No existe un “tick de estación” que:

- cambie toda la ropa;
- seque/ensucie calles;
- altere stock instantáneamente.

---

# 21. IA

El contexto puede recibir:

- tiempo actual;
- ENV local;
- tendencia reciente;
- estación;
- visibilidad;
- temperatura cualitativa.

La IA describe consecuencias ya autorizadas.

No decide que una calle está embarrada solo porque “es otoño”.

---

## Regla final

**El tiempo en Treskal deja rastro: la lluvia puede parar, pero el barro, la humedad y sus consecuencias necesitan tiempo para desaparecer.**


---

## Integración Punto 12

Treskal utiliza enero–diciembre y lunes–domingo como el resto de Norgard.

El cambio de estación modifica contexto y probabilidades, no el estado ambiental por decreto.

`1 de marzo` puede activar la etiqueta civil `primavera`, pero ENV, lluvia, barro, temperatura, combustible y ropa siguen respondiendo a causas reales.
