# Treskal — orientación, direcciones y direcciones postales no modernas v0.1

## Estado

**DISEÑO DE GAMEPLAY APROBADO — CIUDAD LEGIBLE SIN NUMERACIÓN MODERNA**

## Objetivo

Permitir que habitantes y jugador encuentren lugares usando:

- landmarks;
- áreas conocidas;
- oficio;
- negocio;
- relaciones espaciales;
- instrucciones verbales.

Sin exigir:

- numeración de calles;
- sistema postal moderno;
- señalización urbana continua.

---

# 1. Dos capas de localización

## Localización técnica

El motor puede utilizar:

- building_id;
- entrance_id;
- parcel_id futuro;
- Z;
- T;
- C;
- coordenadas futuras.

## Localización humana

Los habitantes utilizan:

- nombres;
- landmarks;
- cruces;
- negocios;
- descripciones;
- relaciones espaciales.

La capa técnica no debe aparecer automáticamente como conocimiento del NPC.

---

# 2. Sin dirección moderna universal

No se presupone una dirección tipo:

**Calle X, número 24.**

Antes del callejero detallado y sin canon postal específico, una vivienda puede localizarse mediante:

- área;
- referencia cercana;
- negocio;
- posición relativa;
- descripción de fachada/entrada.

---

# 3. Estructura verbal

Una dirección puede seguir:

**referencia mayor → recorrido → referencia menor → destino**

Ejemplo conceptual:

“Desde el Abasto, tira hacia Los Talleres; pasa los Patios y busca la casa-taller junto al pozo pequeño.”

La frase concreta depende del mapa materializado y conocimiento del NPC.

---

# 4. Landmarks fuertes

Los landmarks L sirven como anclas de orientación.

Especialmente:

- Puente de los Gemelos;
- Plaza del Abasto;
- Lonja del Pescado;
- La Casa;
- la Justicia;
- Los Patios;
- Astilleros Reales;
- Los Corrales.

No todos son visibles desde cualquier punto.

---

# 5. Áreas populares

Los topónimos permiten ubicar de forma aproximada:

- El Puente;
- la Ribera;
- Los Talleres;
- Los Patios;
- Los Muelles;
- Los Corrales.

Decir:

“vive por Los Talleres”

no equivale a conocer la puerta exacta.

---

# 6. Señales funcionales

Puede existir señalización donde sea útil:

- institución;
- posada;
- taberna;
- taller;
- negocio;
- puerto;
- acceso restringido.

La señal puede utilizar:

- texto;
- símbolo;
- emblema;
- objeto representativo;
- combinación.

No existe obligación de rótulo en todo edificio.

---

# 7. Alfabetización

La orientación no debe depender exclusivamente de lectura.

Un rótulo puede ayudar a quien sabe leer.

Un símbolo o actividad visible puede ayudar a otros.

Ejemplos conceptuales:

- herramienta;
- animal;
- jarra;
- pieza de oficio;
- heráldica institucional contextual.

No se fija un catálogo universal de iconos.

---

# 8. Instituciones

La Casa, la Justicia y Astilleros Reales pueden usar:

- identificación funcional;
- guardia;
- heráldica cuando corresponda.

La heráldica no debe decorar indiscriminadamente toda la ciudad.

---

# 9. Negocio materializado

Un negocio persistente puede tener:

- nombre comercial si existe;
- propietario;
- oficio;
- señal visible;
- entrada;
- área.

Si todavía no tiene nombre canónico, el jugador puede recordarlo como:

- “el taller de X”;
- “la posada junto a Y”.

No se genera nombre ornamental obligatorio.

---

# 10. Dirección de vivienda

Un hogar puede localizarse por:

- nombre de residente;
- oficio;
- vecindad;
- referencia.

Ejemplo:

“la casa de la familia de X, detrás del taller de Y”.

La información solo es útil si el interlocutor conoce esas referencias.

---

# 11. Calidad de indicaciones

Depende de:

- conocimiento;
- familiaridad;
- capacidad de explicar;
- complejidad de ruta;
- cambios recientes.

Un NPC puede dar una dirección:

- exacta;
- aproximada;
- incompleta;
- desactualizada.

No debe equivocarse arbitrariamente sin causa.

---

# 12. Cambios del World State

Una referencia puede dejar de servir si:

- edificio ardió;
- negocio cerró;
- calle se bloqueó;
- persona se mudó.

Los NPC pueden seguir usando una referencia antigua si su conocimiento está desactualizado.

---

# 13. Preguntar de nuevo

El jugador puede encadenar orientación:

1. alguien indica Los Talleres;
2. allí pregunta por un ebanista;
3. un trabajador señala la calle o edificio;
4. finalmente identifica la entrada.

Esto convierte conocimiento social en navegación.

---

# 14. Mapa

Cuando el jugador descubre una localización:

el mapa puede registrar un marcador derivado de conocimiento real.

Puede distinguir:

- área aproximada;
- edificio localizado;
- entrada conocida.

---

# 15. Wayfinding visual

La arquitectura y actividad deben ayudar a orientarse.

Ejemplos:

- más madera y patios hacia Z06;
- mayor actividad portuaria hacia Z10;
- concentración comercial en Z04;
- transición ganadera hacia Z14.

No todo depende del HUD.

---

# 16. Noche y clima

La orientación puede degradarse por:

- oscuridad;
- niebla;
- lluvia;
- visibilidad.

Un landmark conocido puede no ser visible.

El conocimiento de ruta sigue existiendo, pero aumenta dificultad perceptiva.

---

# 17. Visitante

Un visitante reciente puede conocer:

- puente;
- puerto;
- posada;
- Abasto.

No se le otorga conocimiento completo del callejero.

---

## Regla final

**En Treskal una dirección es una historia corta sobre cómo llegar; los IDs son para el motor, las referencias son para la gente.**
