# Territorio de Treskal — clima local y medio ambiente

## Estado

**BORRADOR DE DISEÑO — BLOQUE TEMÁTICO CERRADO EN ESTA FASE**

Este bloque desarrolla el **subclima y las bases ambientales del territorio administrado por la Casa Valrik / territorio de Treskal**.

No sustituye al clima general canónico de Norgard.

Las decisiones reunidas aquí se mantendrán como borrador hasta que se hayan cerrado:

- Pueblos del territorio de Treskal;
- Villas del territorio de Treskal;
- ciudad de Treskal.

Después se realizará una revisión territorial conjunta antes de elevar este bloque a canon definitivo.

---

## Objetivo

Definir información ambiental suficiente para que el futuro videojuego pueda inferir de forma coherente características de elementos que nunca hayan sido descritos individualmente.

Ejemplo conceptual:

```
zona
+ relieve
+ estación
+ clima
+ lluvias recientes
+ nieve/deshielo
+ suelo y drenaje
+ vegetación
+ red hidrográfica cercana
= comportamiento ambiental plausible y persistente
```

No se pretende fijar ahora valores técnicos excesivamente precisos como milímetros exactos de lluvia, temperaturas diarias, caudales exactos, porcentajes arbitrarios o fórmulas definitivas de gameplay.

La prioridad es definir **relaciones cualitativas y causales coherentes**.

---

## Método de trabajo

Cada decisión debe distinguir entre:

1. **canon ya existente**;
2. **deducción razonable** a partir de ese canon, del mapa y de principios físicos/climáticos;
3. **propuesta nueva de borrador**, que requiere validación expresa.

Nada de este bloque se convierte automáticamente en canon definitivo.

---

## Alcance territorial aprobado para el borrador

El estudio abarca **todo el territorio Valrik / territorio de Treskal**, no solo el sector meridional poblado.

Incluye:

- costa meridional del Mar de Suthiros;
- entorno de Treskal;
- tierras interiores;
- Bosque Negro;
- Sareno y Theleno;
- Montes Invernos;
- tierras al norte de los Montes Invernos;
- costas orientales y septentrionales del dominio Valrik.

---

## Estructura documental

- `00_encuadre_y_subzonas.md`
- `01_temperatura.md`
- `02_lluvias.md`
- `03_nieve_y_deshielo.md`
- `04_viento.md`
- `05_humedad_nieblas_y_visibilidad.md`
- `06_hidrologia_y_escorrentia.md`
- `07_suelos_y_drenaje.md`
- `08_vegetacion_y_microclimas.md`
- `09_reglas_de_inferencia_para_juego.md`

Los documentos temáticos se irán completando y corrigiendo durante la conversación de diseño.


---

## Estado de los documentos

Todos los bloques temáticos desarrollados en esta carpeta han sido **aprobados dentro del BORRADOR DE DISEÑO**:

- `00_encuadre_y_subzonas.md` — aprobado;
- `01_temperatura.md` — aprobado;
- `02_lluvias.md` — aprobado;
- `03_nieve_y_deshielo.md` — aprobado;
- `04_viento.md` — aprobado;
- `05_humedad_nieblas_y_visibilidad.md` — aprobado;
- `06_hidrologia_y_escorrentia.md` — aprobado;
- `07_suelos_y_drenaje.md` — aprobado;
- `08_vegetacion_y_microclimas.md` — aprobado;
- `09_reglas_de_inferencia_para_juego.md` — aprobado como documento conceptual puente, no como especificación técnica.

Este cierre **no convierte el bloque en canon definitivo**.

---

## Pendientes deliberadamente aplazados

Quedan fuera de esta fase, de forma intencionada:

1. **Nombres propios de vientos locales.**  
   Se definirán durante una revisión posterior de lore y cultura local.

2. **Glaciares o nieve permanente.**  
   No se fija por ahora su existencia. Solo quedan aprobados neveros persistentes y nieve estacional prolongada en altura. La decisión final se tomará al revisar conjuntamente latitud, exposición y cartografía regional de los Montes Invernos.

3. **Localización exacta de la cumbre máxima y grandes cumbres de los Montes Invernos.**  
   La cordillera es compartida por Galdren y Valrik, por lo que no se asignará su pico máximo a ninguno de los dos territorios hasta desarrollar Galdren y disponer de cartografía regional suficiente.

4. **Ubicación y cotas exactas de pasos, valles y accidentes individuales.**  
   Solo existen rangos generales aprobados.

5. **Implementación técnica del sistema ambiental.**  
   Fórmulas, pesos, probabilidades, estructuras de datos, actualización, persistencia en savegame y conexión concreta con IA narrativa se diseñarán en una fase técnica separada.

6. **Elevación a canon definitivo.**  
   Se hará únicamente tras cerrar Pueblos, Villas y ciudad de Treskal y realizar una revisión territorial conjunta.

---

## Documento geográfico relacionado

La estructura altitudinal general de los Montes Invernos, al ser una cordillera compartida entre Galdren y Valrik, se guarda fuera de la carpeta climática local en:

`Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Geografía/Montes Invernos/cotas_y_altitudes_borrador.md`

La aplicación específica al sector Valrik/Treskal se referencia desde:

`Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Valrik/Geografia_local/montes_invernos_cotas_y_altitudes.md`


---

## Auditoría técnica de esta fase

La auditoría técnica realizada al cierre de esta fase se conserva como documento **no canónico** de control y referencia en:

`Auditorias/2026-09-28_auditoria_tecnica_clima_local_treskal_para_motor.md`

Sus observaciones no sustituyen al borrador climático. Sirven para:

- detectar incoherencias documentales;
- conservar recomendaciones para fases futuras;
- orientar la futura traducción del worldbuilding ambiental a sistemas de juego.


### Desarrollo geográfico futuro relacionado

**Microrelieve, cuencas e hidrografía menor** no forman parte del cierre climático actual.

Se desarrollarán después de cerrar:

1. Pueblos;
2. Villas;
3. ciudad de Treskal;

y antes de la revisión territorial conjunta que decidirá qué partes del borrador ambiental pueden elevarse a canon.

Su planificación se mantiene en `../Geografia_local/README.md`.
