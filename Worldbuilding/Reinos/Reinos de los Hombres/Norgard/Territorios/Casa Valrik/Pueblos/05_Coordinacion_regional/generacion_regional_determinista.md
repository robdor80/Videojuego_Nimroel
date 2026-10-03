# Pueblos de Treskal — coordinación regional y generación determinista

## Estado

**CANON DE GENERACIÓN REGIONAL APROBADO — v0.1**

## Objetivo

Definir cómo se generan varios Pueblos y Aldeas como una red territorial coherente sin que cada asentamiento tire sus servicios de forma aislada.

También fija una regla de aleatoriedad determinista para que el mismo World Seed produzca el mismo territorio mientras no cambien las reglas o la versión del generador.

---

# 1. Principio rector

**Un asentamiento se genera dentro de una red, no dentro de una burbuja.**

La generación regional debe conocer antes de resolver servicios:

- posición y accesibilidad;
- caminos y pasos;
- relieve;
- hidrología relevante;
- recursos;
- rutas comerciales;
- asentamientos próximos;
- Villas y centros superiores;
- servicios ya cubiertos.

---

# 2. Grafo territorial

La relación funcional se representa mediante un grafo de accesibilidad.

## Nodos

Pueden ser:

- Aldeas;
- Pueblos;
- Villas;
- Treskal;
- instalaciones estratégicas cuando afecten al tránsito.

## Enlaces

Representan rutas utilizables y almacenan, como mínimo:

- coste normal de viaje;
- tipo de vía;
- aptitud para carros;
- pasos de agua;
- sensibilidad estacional;
- posibles bloqueos dinámicos.

La distancia geométrica puede influir, pero **el coste de viaje decide la accesibilidad funcional**.

---

# 3. Asignación de Pueblo de referencia

Para cada Aldea:

1. localizar Pueblos y Villas accesibles;
2. calcular coste de viaje normal;
3. evaluar servicios disponibles;
4. asignar un **Pueblo de referencia principal** cuando resulte coherente;
5. conservar referencias secundarias si existe solapamiento útil.

No es obligatorio que toda Aldea dependa de un Pueblo si una Villa resulta claramente más accesible.

La referencia principal no impide viajar a otros núcleos.

---

# 4. Orden de generación regional

La generación recomendada es:

1. resolver geografía y red viaria;
2. colocar o identificar asentamientos y su categoría;
3. determinar población aproximada de cada núcleo;
4. asignar modelos económicos plausibles;
5. construir el grafo de accesibilidad;
6. generar primero las capacidades obligatorias;
7. tirar servicios opcionales de Pueblos;
8. tirar servicios opcionales de Aldeas;
9. validar cobertura regional;
10. corregir únicamente vacíos funcionales;
11. coordinar mercados;
12. generar hogares y edificios;
13. generar layout;
14. persistir la red completa.

Este orden evita que una Aldea fuerce decisiones antes de conocer el Pueblo que la atiende.

---

# 5. Cobertura regional

La comprobación de cobertura debe funcionar sobre **tiempo/coste de viaje**, no sobre círculos de kilómetros.

Debe verificar al menos:

- molienda;
- curandera formada;
- acceso razonable a bienes ordinarios;
- reparación de carros;
- mercado periódico;
- alojamiento en corredores donde el tránsito lo requiera.

La herrería básica de Aldea y la herrería de nivel 2 de Pueblo no se resuelven por cobertura porque son capacidades locales obligatorias según su rango.

---

# 6. Corrección de vacíos

Si la red genera un vacío funcional:

1. identificar los nodos capaces de cubrirlo;
2. puntuar coherencia por recursos, población, modelo y acceso;
3. seleccionar el candidato más coherente;
4. añadir solo la función necesaria;
5. registrar que fue una corrección de cobertura.

No se debe:

- rerollear toda la región;
- añadir el mismo servicio a todos los nodos;
- convertir automáticamente el Pueblo más grande en solución universal.

---

# 7. Coordinación de mercados

Todo Pueblo tiene mercado periódico.

La planificación regional debe evitar que varios Pueblos próximos y dependientes de la misma población celebren mercado de forma sistemáticamente incompatible.

La coordinación debe buscar:

- escalonar mercados cercanos cuando resulte útil;
- permitir a comerciantes itinerantes recorrer varios mercados;
- evitar que todas las aldeas de una misma zona tengan que elegir entre mercados simultáneos;
- conservar excepciones cuando una tradición o necesidad local las justifique.

La **cadencia y nombres concretos de los días** no se fijan en este documento.

El calendario debe integrarse con el sistema temporal general de Nimroel.

---

# 8. Aleatoriedad determinista

Cada partida utiliza un **World Seed** estable.

No debe usarse una única secuencia aleatoria global para toda la generación.

Cada decisión importante deriva su propia semilla mediante:

**World Seed + ID estable del asentamiento + subsistema + versión de reglas**

Ejemplos de subsistema:

- population;
- model;
- services;
- households;
- buildings;
- layout;
- npc_population;
- market;
- craftsmanship.

Esto permite que modificar el algoritmo de un subsistema no cambie innecesariamente los demás.

---

# 9. IDs estables

Todo asentamiento procedural necesita un ID estable antes de generar sus detalles.

El ID no debe depender del nombre visible que posteriormente reciba.

Puede derivarse de:

- celda o región de generación;
- posición cuantizada;
- índice persistente de nodo;
- identificador del mapa.

Regla:

**nombre visible != identidad técnica**

Cambiar el nombre de un Pueblo no debe regenerar su contenido.

---

# 10. Versionado del generador

Cada instancia debe guardar:

- World Seed;
- versión de reglas;
- versión de generador;
- semilla derivada o claves suficientes para reconstruirla.

Si las reglas cambian en una versión futura del juego, una partida existente no debe regenerar silenciosamente el Pueblo.

Opciones válidas:

- conservar el resultado persistido;
- ejecutar una migración explícita;
- regenerar solo en partidas nuevas.

---

# 11. Estabilidad de subresultados

Dentro de un Pueblo, cada servicio opcional debe poder usar una clave estable propia.

Ejemplo conceptual:

`seed(world, pueblo_0042, services, bakery)`

y no:

`tercera_tirada_de_la_lista_de_servicios`

Así, añadir en el futuro un oficio nuevo a la tabla no cambia por desplazamiento todas las tiradas posteriores.

La misma regla se aplica a:

- hogares;
- edificios;
- talleres;
- calidad artesanal;
- NPC.

---

# 12. Correcciones deterministas

Una corrección de cobertura también debe ser determinista.

Si dos Pueblos son candidatos, el sistema aplica:

1. puntuación de coherencia;
2. menor coste de acceso a población no cubierta;
3. capacidad del asentamiento;
4. desempate por semilla estable.

El resultado debe repetirse con el mismo World Seed y la misma versión.

---

# 13. Estado dinámico de rutas

El grafo base representa accesibilidad estructural.

El barro, nieve, hielo, crecidas, daños o eventos pueden alterar temporalmente:

- coste;
- disponibilidad;
- ruta preferente.

Estos cambios pertenecen al estado dinámico del mundo.

No deben rerollear los servicios permanentes del Pueblo.

Sí pueden cambiar temporalmente:

- mercado accesible;
- ruta usada;
- flujo de comerciantes;
- Pueblo de referencia práctico durante una emergencia.

---

# 14. Validación regional final

Antes de cerrar la generación se comprueba:

- todos los asentamientos tienen ID estable;
- todas las Aldeas tienen al menos una salida funcional de la red;
- los Pueblos actúan como nodos reales de servicio;
- no existen desiertos funcionales injustificados;
- no existe duplicación absurda de servicios especializados;
- los mercados son territorialmente utilizables;
- las rutas necesarias existen;
- las correcciones de cobertura son mínimas;
- toda la configuración es reproducible desde las claves persistidas.

---

## Principio final

**El World Seed crea variedad; los IDs estables aíslan las decisiones; la red territorial aporta coherencia; la persistencia convierte el resultado en mundo.**
