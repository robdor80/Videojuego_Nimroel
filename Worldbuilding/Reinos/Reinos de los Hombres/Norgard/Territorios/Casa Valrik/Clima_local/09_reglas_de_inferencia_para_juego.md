# Territorio de Treskal — reglas ambientales de inferencia para el videojuego

## Estado

**BORRADOR DE DISEÑO — PENDIENTE DE VALIDACIÓN**

Este documento actúa como **puente entre el worldbuilding ambiental y el futuro sistema técnico del videojuego**.

No define todavía:

- fórmulas;
- porcentajes;
- pesos;
- clases;
- estructuras de datos;
- frecuencia de actualización;
- lógica de guardado;
- implementación de IA narrativa.

Su función es recoger las **relaciones causales aprobadas** que el futuro sistema deberá respetar.

---

# 1. Principio general

El estado ambiental de un lugar no debe generarse de forma arbitraria ni depender de una única etiqueta.

Debe inferirse a partir de varias capas:

```
localización
+ subzona
+ latitud
+ altitud
+ relieve
+ estación
+ clima regional
+ meteorología reciente
+ nieve/deshielo
+ suelo/drenaje
+ vegetación
+ red hidrográfica
+ exposición
+ uso humano
= estado ambiental plausible y persistente
```

---

# 2. Prioridad de contexto

Cuando varias variables entren en conflicto, el sistema deberá priorizar la coherencia geográfica y causal.

Ejemplo:

Un punto situado en el Bosque Negro no debe asumirse automáticamente como:

- húmedo;
- frío;
- embarrado;
- cubierto de niebla.

Antes debe comprobarse:

- si está en interior o borde;
- si ha llovido recientemente;
- si el suelo drena bien;
- si está en ladera o vaguada;
- si recibe sol;
- si hay viento;
- si existe nieve o deshielo.

La pertenencia a una subzona da un **contexto base**, no un resultado absoluto.

---

# 3. Regla de persistencia

El mundo debe conservar memoria ambiental.

Un estado no debe desaparecer porque cambie una sola variable durante unas horas.

Ejemplo conceptual:

```
estado anterior
+ cambios recientes
- recuperación natural
= nuevo estado
```

Esto se aplica a:

- humedad;
- barro;
- nieve;
- hielo;
- caudal;
- vegetación;
- inundación;
- transitabilidad.

---

# 4. El lugar permanece; su estado cambia

Un mismo elemento persistente del mundo puede presentar estados diferentes en momentos distintos.

## Camino

```
mismo camino
+ varios días secos
= firme, polvoriento, rápido de recorrer
```

```
mismo camino
+ lluvia prolongada
+ suelo de drenaje mediocre
+ tránsito de carros
= blando, con rodadas profundas y barro
```

```
mismo camino
+ deshielo reciente
+ heladas nocturnas
= barro, charcos, hielo residual y firme inestable
```

## Arroyo

```
mismo arroyo
+ verano seco
= caudal bajo
```

```
mismo arroyo
+ varios días de lluvia
= caudal alto
```

```
mismo arroyo
+ primavera
+ deshielo de montaña
= corriente rápida y fuerte
```

Esta misma lógica puede aplicarse a:

- ríos;
- vados;
- bosques;
- campos;
- laderas;
- puentes;
- costas;
- plazas y calles sin pavimentar.

---

# 5. Inferencia de un camino

Un camino debería evaluarse mediante:

```
tipo de suelo
+ drenaje
+ pendiente
+ lluvia acumulada
+ nieve/deshielo
+ temperatura
+ tránsito
+ exposición al sol y viento
= estado del camino
```

Posibles resultados cualitativos:

- seco;
- polvoriento;
- firme;
- húmedo;
- blando;
- embarrado;
- encharcado;
- helado;
- nevado;
- parcialmente transitable;
- impracticable temporalmente.

---

# 6. Inferencia de un río o arroyo

Un curso de agua debería evaluarse mediante:

```
tamaño de cuenca
+ pendiente
+ lluvia reciente
+ lluvia acumulada
+ nieve
+ deshielo
+ aportes aguas arriba
+ suelo
+ vegetación
+ estación
= estado hidrológico
```

Posibles resultados:

- seco;
- casi seco;
- caudal bajo;
- normal;
- crecido;
- desbordado;
- torrencial;
- activado temporalmente.

---

# 7. Inferencia de un vado

Un vado no debe ser permanentemente practicable.

Debe depender de:

```
profundidad habitual
+ caudal actual
+ corriente
+ lluvia
+ deshielo
+ sedimentos
+ daños recientes
= practicabilidad
```

Puede pasar de:

- seguro;
- difícil;
- peligroso;
- imposible.

---

# 8. Inferencia de nieve

La nieve local debería depender de:

```
latitud
+ altitud
+ temperatura reciente
+ precipitación
+ orientación
+ sombra
+ vegetación
+ viento
+ estación
= nieve acumulada
```

La nieve residual debería depender además de:

```
nieve previa
+ temperatura acumulada
+ insolación
+ lluvia
+ viento
+ sombra
= nieve restante
```

---

# 9. Inferencia de hielo

La presencia de hielo debería depender de:

- temperatura;
- humedad;
- agua superficial;
- duración del frío;
- viento;
- insolación;
- ciclos de congelación y deshielo.

El hielo puede aparecer en:

- caminos;
- charcos;
- riberas;
- rocas;
- puentes;
- pasos;
- cursos lentos.

---

# 10. Inferencia de niebla

La niebla debería depender de:

```
humedad disponible
+ temperatura
+ hora
+ relieve
+ proximidad al agua
+ viento
+ estabilidad atmosférica
= probabilidad e intensidad de niebla
```

Será más plausible en:

- fondos de valle;
- riberas;
- costa;
- Bosque Negro;
- piedemonte;
- depresiones.

---

# 11. Inferencia de humedad del suelo

La humedad del terreno debe depender de:

```
humedad previa
+ lluvia
+ deshielo
+ inundación
- drenaje
- evaporación
- viento
= humedad actual
```

No debe resetearse inmediatamente al dejar de llover.

---

# 12. Inferencia de barro

El barro requiere más que lluvia.

Debe depender de:

```
agua acumulada
+ tipo de suelo
+ drenaje
+ compactación
+ tránsito
+ pendiente
= barro
```

Un terreno pedregoso puede estar mojado sin convertirse en barro profundo.

Un camino arcilloso y muy transitado puede quedar embarrado durante días.

---

# 13. Inferencia de vegetación

El estado vegetal debe depender de:

```
subzona
+ latitud
+ altitud
+ suelo
+ drenaje
+ agua
+ orientación
+ exposición
+ estación
+ meteorología reciente
+ uso humano
= cobertura y estado vegetal
```

Posibles efectos:

- vegetación exuberante;
- suelo verde;
- hierba seca;
- vegetación dañada por helada;
- follaje otoñal;
- nieve sobre cobertura;
- regeneración tras tala;
- daño por incendio.

---

# 14. Inferencia de microclima forestal

Para un punto situado en bosque:

```
clima regional
+ tipo de bosque
+ interior/borde/claro
+ cercanía al agua
+ altitud
+ orientación
+ lluvia reciente
+ nieve
= microclima local
```

Esto debe modificar:

- temperatura;
- viento;
- humedad;
- niebla;
- nieve residual;
- visibilidad;
- suelo.

---

# 15. Inferencia de viento local

El viento local debería depender de:

```
circulación regional
+ estación
+ costa
+ valle
+ paso
+ altitud
+ orientación
+ cobertura forestal
= dirección e intensidad local
```

Un mismo sistema regional puede generar:

- viento fuerte en un collado;
- corriente canalizada en un valle;
- calma relativa dentro del bosque.

---

# 16. Inferencia de visibilidad

La visibilidad útil debería depender de:

```
niebla
+ lluvia
+ nieve
+ viento
+ vegetación
+ relieve
+ hora
= visibilidad local
```

Debe distinguirse entre:

- visibilidad reducida por meteorología;
- visibilidad reducida por bosque o relieve.

---

# 17. Inferencia de riesgo de crecida

El riesgo debe aumentar cuando coinciden:

- lluvia acumulada;
- suelo saturado;
- deshielo;
- fuerte pendiente;
- cuenca pequeña;
- cauces estrechos.

La combinación:

```
lluvia intensa
+ deshielo rápido
+ suelo saturado
```

debe considerarse especialmente peligrosa.

---

# 18. Inferencia de incendio

El riesgo de incendio debería depender de:

```
sequedad acumulada
+ temperatura
+ viento
+ tipo de vegetación
+ estación
= riesgo de propagación
```

El Bosque Negro no debe considerarse inmune al fuego.

---

# 19. Inferencia de transitabilidad

La dificultad de viaje debería derivarse de:

- pendiente;
- firme;
- barro;
- nieve;
- hielo;
- agua;
- vegetación;
- viento;
- visibilidad;
- estado de puentes y vados.

No debe ser un valor fijo de cada camino.

---

# 20. Inferencia narrativa

La IA narrativa debe describir el estado ambiental actual y no una versión genérica del lugar.

Ejemplo:

No basta con:

> “El camino atraviesa el valle.”

La descripción debería poder reflejar:

- rodadas secas;
- polvo;
- barro;
- nieve;
- charcos;
- niebla;
- viento;
- vegetación mojada;
- corriente de agua cercana;

según el estado real del mundo.

---

# 21. Coherencia con visitas anteriores

Si el jugador regresa a un lugar, la IA debe mantener continuidad.

Ejemplo:

Si tres días antes:

- llovió intensamente;
- el camino quedó embarrado;

y desde entonces:

- no ha llovido;
- ha habido viento;
- temperaturas suaves;

el camino podrá aparecer parcialmente seco.

No debería describirse como completamente seco o completamente anegado sin una causa.

---

# 22. Escala de inferencia

No todo debe simularse con el mismo nivel de detalle.

Se propone distinguir conceptualmente:

## Escala regional

Define:

- clima;
- estación;
- circulación atmosférica;
- grandes tendencias.

## Escala local

Define:

- valle;
- costa;
- ladera;
- bosque;
- río;
- suelo;
- orientación.

## Escala inmediata

Define:

- charco;
- barro;
- nieve residual;
- niebla puntual;
- estado de un camino;
- estado de un arroyo.

La futura implementación podrá simplificar cada capa según necesidad.

---

# 23. Evitar contradicciones

El sistema debe evitar combinaciones absurdas salvo evento excepcional justificado.

Ejemplos:

- camino cubierto de polvo tras varios días de lluvia intensa;
- arroyo seco durante pleno deshielo tras invierno nivoso;
- nieve persistente en costa meridional tras días templados;
- bosque empapado después de una larga sequía sin fuente local de humedad;
- niebla densa en cresta muy ventilada sin una situación atmosférica que la sostenga.

---

# 24. Excepciones plausibles

Una inferencia no debe convertirse en regla absoluta.

Eventos excepcionales pueden romper tendencias normales:

- ola de frío;
- tormenta extraordinaria;
- sequía;
- temporal;
- año especialmente húmedo;
- nevada tardía;
- deshielo súbito.

La excepción necesita una causa.

---

# 25. Objetivo de diseño

El objetivo no es reproducir una simulación meteorológica científica completa.

El objetivo es conseguir que:

- el mundo sea coherente;
- los lugares evolucionen;
- el jugador perciba continuidad;
- la IA pueda narrar el entorno con fundamento;
- el gameplay reaccione al ambiente;
- el mismo lugar pueda sentirse distinto sin perder identidad.

Principio final:

> **el mundo no cambia de identidad; cambia de estado como consecuencia de lo que le sucede.**
