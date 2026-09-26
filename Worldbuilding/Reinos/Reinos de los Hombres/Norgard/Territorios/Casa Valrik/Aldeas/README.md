# Aldeas del territorio de Treskal

## Propósito

Esta carpeta organiza el lore jugable de las aldeas del territorio de Treskal desde lo más general hasta los asentamientos concretos del mundo.

Todas las aldeas deben seguir la metodología territorial común definida en:

`../metodologia_generacion_asentamientos_treskal.md`

La secuencia obligatoria es:

**esqueleto mínimo → posibilidades → coherencia regional → probabilidades → generación → persistencia**.

La regla es separar claramente:

1. **qué comparten las aldeas del territorio de Treskal**;
2. **qué modelos de generación reutilizables existen**;
3. **qué aldeas concretas deben quedar fijadas por necesidades narrativas o de mapa**.

El objetivo no es diseñar previamente cada aldea, sino proporcionar al juego límites suficientes para que pueda **generar asentamientos variados, coherentes y persistentes** sin que el jugador conozca de antemano su composición exacta.

---

## Principio de sorpresa del jugador

Las aldeas ordinarias del territorio de Treskal **no deben preconstruirse una a una en el lore**.

El lore define las reglas.

El modelo define probabilidades, límites y relaciones plausibles.

El juego decide la instancia concreta.

Por tanto, antes de descubrir una aldea el jugador no tiene por qué saber:

- si posee herrero;
- si posee posada;
- cuántos talleres tiene;
- qué edificios son de una o dos plantas;
- la disposición exacta de casas y caminos;
- qué familias y oficios concretos encontrará.

Una vez generada una aldea, su configuración debe **persistir**: volver a visitarla no debe regenerar arbitrariamente edificios, habitantes ni servicios.

---

## Estructura

### 00_Base

Contiene la definición genérica y las reglas comunes de generación de una aldea del territorio de Treskal.

Archivo principal:

- `00_Base/aldea_tipo_treskal.md`

### 01_Modelos

Contiene **modelos de generación reutilizables**.

Los identificadores `V1`, `V2`, `V3`... significan variantes de modelo, no revisiones del mismo archivo.

Un modelo no es un plano prefabricado ni una aldea concreta. Define:

- contexto territorial;
- función económica dominante;
- rango de población;
- elementos obligatorios mínimos;
- elementos opcionales;
- elementos incompatibles o poco plausibles;
- pesos o tendencias de aparición;
- reglas espaciales;
- relaciones con otros asentamientos.

### 02_Instancias

Se reserva para asentamientos concretos que necesiten quedar fijados por razones de:

- historia;
- narrativa;
- misión;
- cartografía;
- personaje canónico;
- localización única.

Las aldeas procedurales ordinarias **no necesitan convertirse en documentos individuales del repo**.

Su composición concreta pertenece al estado de la partida, no al lore estable.

---

## Relación con la v0.0.1

La v0.0.1 utilizará inicialmente modelos rurales del territorio de Treskal y permitirá validar la generación de aldeas a pequeña escala.

La prueba debe priorizar que el jugador descubra la aldea en lugar de conocerla previamente durante su diseño.

Si una mecánica necesita garantizar un servicio concreto, debe bloquearse solo esa **necesidad mínima de gameplay**, evitando fijar el resto de la aldea.

---

## Separación de responsabilidades

### Lore y lógica jugable

Se guardan aquí, dentro de `Territorios/Casa Valrik/Aldeas/`.

### Biblia visual

Se guarda en:

`Worldbuilding/Direccion artistica/Biblia visual/Culturas/Norgard/Perfiles locales/Treskal/Aldeas/`

### Prompts maestros

Se guardan en:

`Worldbuilding/Direccion artistica/Prompts maestros/Asentamientos/Norgard/Treskal/Aldeas/`

### Referencias visuales aprobadas

Se guardan en:

`Worldbuilding/Direccion artistica/Biblia visual/Culturas/Norgard/Referencias visuales/Treskal/Aldeas/`

### Assets finales

Los assets generados se almacenan bajo `Worldbuilding/Direccion artistica/Assets/` siguiendo la convención oficial de nombres y empaquetado del repositorio.

---

## Regla principal

**Lore define los límites.  
El modelo define el espacio de posibilidades.  
El generador crea la aldea concreta.  
El estado de partida conserva lo generado.  
La Biblia visual define cómo puede verse.  
Los assets proporcionan las piezas con las que construirla.**


---

## Generación regional coordinada

Las aldeas no deben generarse como unidades independientes.

Antes de decidir servicios locales, el sistema debe consultar la **red de asentamientos próximos** y comprobar qué necesidades ya están cubiertas.

La presencia de herrería, molino, posada, carpintería u otros servicios se decidirá mediante **azar condicionado por contexto**, teniendo en cuenta:

- distancia o tiempo de viaje a otros asentamientos;
- servicios ya existentes en pueblos, villas y aldeas cercanas;
- población y capacidad económica del núcleo;
- tipo de ruta y volumen de tránsito;
- recursos disponibles en el entorno;
- función económica del modelo;
- necesidades mínimas de cobertura de la zona.

El sistema debe impedir resultados incoherentes como una amplia zona habitada sin acceso razonable a un herrero o a un molino.

La solución preferida es una generación en varias fases:

1. crear la red de asentamientos y sus relaciones;
2. asignar funciones y servicios mediante pesos variables;
3. validar la cobertura regional;
4. corregir únicamente los huecos necesarios;
5. generar la distribución concreta de cada asentamiento;
6. guardar el resultado en el estado persistente de la partida.

Por tanto, **random no significa independiente**: cada asentamiento se genera teniendo en cuenta lo que ya existe a su alrededor.


---

## Fase actual de diseño

El desarrollo se realizará en este orden:

1. fijar el **esqueleto mínimo** de cada tipo de asentamiento;
2. añadir después las **posibilidades opcionales**;
3. definir por último **probabilidades, pesos y reglas de cobertura regional**.

Orden de trabajo previsto:

**Aldea → Pueblo → Villa → Treskal.**

Los puestos de guardia fronterizos se tratarán como instalaciones funcionales separadas, no como asentamientos civiles.
