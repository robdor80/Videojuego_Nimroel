# Territorio de Treskal — geografía local

## Estado

**BORRADOR DE DISEÑO**

Este bloque desarrolla detalles geográficos locales del territorio de Treskal que no necesitan formar parte todavía de la geografía general de Norgard.

La carpeta administrativa se mantiene bajo `Casa Valrik`, pero el ámbito geográfico es el **territorio de Treskal**.

---

## Objetivo

Definir únicamente elementos geográficos necesarios para:

- clima local;
- hidrología;
- generación ambiental;
- viajes;
- asentamientos;
- navegación;
- narrativa;
- gameplay.

No se pretende describir exhaustivamente cada accidente geográfico.

---

## Documentos iniciales

- `montes_invernos_cotas_y_altitudes.md`

Las decisiones permanecen como borrador hasta la revisión territorial final.


---

## Fase desarrollada — microrelieve, cuencas e hidrografía menor

### Estado

**BORRADOR DE DISEÑO — FASE COMPLETADA PARA CONTEXTO DE GENERACIÓN**

La auditoría técnica del clima local detectó que el sistema ya podía inferir **cómo se comporta un curso de agua si existe**, pero faltaba una base geográfica que permitiera responder:

- dónde es razonable que aparezcan arroyos y manantiales;
- de qué microcuenca proceden;
- en qué dirección drenan;
- qué cauces reciben afluentes;
- qué sectores drenan hacia Sareno;
- qué sectores drenan hacia Theleno;
- qué zonas drenan directamente al mar;
- dónde aparecen vaguadas, barrancos, pequeñas depresiones y terrazas fluviales.

### Momento de desarrollo

La fase se desarrolla ahora, una vez cerrado funcionalmente Treskal y antes de fijar el plano urbano definitivo.

### Forma de trabajo

Se ha desarrollado como una **fase específica de worldbuilding/geografía local de Treskal**, separada de:

- la conversación climática actual;
- la futura conversación de implementación técnica del motor.

En esta fase se han definido relaciones y restricciones geográficas cualitativas.

La conversión futura a:

- algoritmos;
- mapas de altura;
- reglas de generación;
- estructuras de datos;
- código;

pertenece a una fase técnica distinta.

### Objetivo

No dibujar manualmente cada arroyo, sino establecer suficientes causas espaciales para que el futuro motor pueda generar una red hidrográfica menor plausible y conectada.


## Documentos añadidos en esta fase

- `microrelieve_y_unidades_de_drenaje_v0.1.md`
- `cuencas_manantiales_red_hidrografica_menor_v0.1.md`
- `reglas_espaciales_generacion_motor_v0.1.md`
- `Datos operativos/territorio_treskal_geografia_hidrologia_profile_v0.1.json`

La autoridad física universal se hereda desde:

`Worldbuilding/Sistemas/Nimroel Core/Datos operativos/nimroel_physical_geography_drainage_contract_v0.1.json`

Con esta fase queda resuelto el hueco conceptual de **por qué puede existir un arroyo en un punto y no en otro**. Las posiciones exactas se concretarán mediante el terreno/plano, no mediante lore arbitrario.
