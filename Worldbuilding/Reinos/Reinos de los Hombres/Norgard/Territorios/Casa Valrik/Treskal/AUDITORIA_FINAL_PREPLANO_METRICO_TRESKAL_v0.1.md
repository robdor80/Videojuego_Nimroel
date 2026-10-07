# Treskal — auditoría final pre-plano métrico v0.1

## Estado

**PUNTO 1 CERRADO — SIN BLOQUEOS EXTERNOS PARA INICIAR ESCALA MÉTRICA**

Marcador:

`TRESKAL_METRIC_PLAN_POINT_1_PREPLAN_AUDIT_CLOSED`

---

## 1. Objetivo

Comprobar, tras el cierre general de Norgard, si existe algún elemento de canon:

- del Reino;
- de Casa Valrik;
- de Treskal;
- militar;
- naval;
- fiscal;
- penal;
- material;
- temporal;

que obligue a reservar suelo, introducir una instalación adicional o modificar la estructura urbana antes de comenzar el plano métrico.

Resultado:

**NO.**

No queda ningún bloqueo externo pendiente.

---

## 2. Autoridades ya cerradas

La auditoría considera resueltos e integrados:

- sistema militar de Norgard;
- Fuerza Territorial Valrik;
- Guardia urbana;
- Armada Real;
- Astilleros Reales;
- Base Naval Principal;
- sistema marítimo;
- fiscalidad y aduanas;
- sistema penal;
- moneda/balance;
- familia y filiación;
- mayoría/capacidad/trabajo;
- propiedad/herencia/alquiler;
- salud;
- gastronomía;
- nombres;
- calendario;
- cultura material.

Norgard declara:

`blockedPendingCanon = []`

Por tanto, el plano de Treskal ya no depende de un canon general pendiente.

---

## 3. Topología obligatoria

Treskal debe mantener:

- desembocadura integrada junto a la ciudad;
- río navegable para embarcaciones pequeñas compatibles;
- muelles fluviales T01;
- masa urbana principal sobre una margen;
- puerto civil T07;
- Complejo Naval Real T08 litoral y separado funcionalmente;
- un puente principal permanente aguas arriba de T01;
- transición territorial sin muralla;
- ciudad no simétrica a ambas márgenes.

La geometría exacta queda para Punto 3.

---

## 4. Sectores T obligatorios

El plano debe poder representar los doce sectores funcionales:

- T01 — interfaz fluvial;
- T02 — logística y almacenes interiores;
- T03 — núcleo comercial y mercados;
- T04 — artesanía de madera;
- T05 — administración Valrik;
- T06 — justicia y guardia urbana;
- T07 — puerto civil y pesquero;
- T08 — Complejo Naval Real;
- T09 — tejido residencial central;
- T10 — periferia rural y abastecimiento;
- T11 — accesos y corredores;
- T12 — recinto militar Valrik.

Los T:

- son IDs de diseño;
- no son nombres de barrios;
- pueden solaparse parcialmente cuando la función lo exige;
- no se convierten automáticamente en distritos amurallados o administrativos.

---

## 5. Relaciones T obligatorias

Deben preservarse al menos estas cadenas:

### madera

`T11 → T02 → T04 / T08`

### alimentos

`T11 → T10 / T02 → T03 → ciudad`

### mercancía fluvial

`río → T01 → T02 / T03 / T04`

### mercancía marítima

`mar → T07 → T02 / T03`

### administración

`territorio → T11 → T05 / T06`

### construcción naval militar

`T11 / T02 / T04 → T08 → mar`

### movilización

`territorio → T11 → T12 → salida territorial`

---

## 6. Instalaciones S obligatorias

El plano debe reservar capacidad real para:

- S01 — sede principal Casa Valrik;
- S02 — administración territorial;
- S03 — sede judicial;
- S04 — custodia temporal;
- S05 — guardia urbana;
- S06 — mercado principal de abastos;
- S07 — lonja/mercado de pescado;
- S08 — Astilleros Reales;
- S09 — almacenamiento principal de madera;
- S10 — recepción principal de ganado;
- S11 — Cuartel Territorial Valrik;
- S12 — campo de instrucción/movilización;
- S13 — Base Naval Principal.

Los S pueden ser:

- edificios;
- complejos;
- patios;
- capacidades distribuidas;

según su canon.

---

## 7. Restricciones de S01/S02

T05 debe permitir:

- residencia Valrik;
- administración;
- audiencias;
- archivo;
- fiscalidad territorial;
- recepción de Casas menores;
- asiento regio de recepción;
- Aposentos Regios;
- acceso público/administrativo separado del privado.

No debe convertirse en:

- castillo;
- palacio monumental;
- fortaleza.

---

## 8. Restricciones de T06 / S03–S05

Debe:

- quedar fuera de cota inundable;
- conectarse a T05;
- conectarse a T03;
- acceder a vías principales;
- separar público, funcionarios, guardia y detenidos.

S04:

- es custodia temporal;
- no es prisión de larga duración.

S05:

- sirve a una Guardia urbana de 140–190 miembros;
- no necesita alojarlos a todos;
- no es cuartel territorial.

---

## 9. Restricciones de T12 / S11–S12

T12 debe situarse:

- en borde norte/nordeste interior;
- próximo a T10;
- tocando T11;
- fuera de cota inundable;
- con salida territorial rápida;
- conectado razonablemente con T05/T06;
- separado de T08;
- sin obligar a cruzar T03.

S11:

- capacidad ordinaria 260–340 profesionales.

S12:

- capacidad simultánea 800–1.200 personas en instrucción/movilización;
- no es alojamiento permanente para toda la reserva.

---

## 10. Restricciones de T07

Puerto civil/pesquero:

- separado de T08;
- conectado con T02/T03;
- acceso de carros;
- pesca;
- carga/descarga;
- viajeros y mercantes;
- reparación civil compatible;
- capacidad de control fiscal/aduanero integrada.

No requiere:

- Casa de Aduanas separada;
- gran recinto fiscal;
- control universal de viajeros.

---

## 11. Restricciones de T08 / S08 / S13

T08:

- pertenece a la Corona;
- no pertenece a Casa Valrik;
- tiene acceso controlado;
- no está bajo control ordinario de Guardia urbana;
- debe disponer de frente de agua propio;
- debe recibir materiales sin atravesar innecesariamente T03.

S08 necesita:

- gradas;
- patios de madera;
- talleres;
- almacenamiento;
- administración;
- respuesta a incendio.

S13 necesita:

- atraque militar;
- mando;
- apoyo a tripulaciones;
- embarque de tropas;
- suministros;
- preparación de convoyes.

No existen:

- polvorines;
- baterías de pólvora;
- arsenal independiente de cañones.

---

## 12. Mercados/logística obligatorios

S06:

- T03;
- mercado diario;
- abastos y bienes cotidianos;
- acceso de carga.

S07:

- transición T01–T07;
- flujo rápido pescado → venta/conservación.

S09:

- T02/T04;
- patios/almacenes/secado;
- conexión T08;
- control de incendio.

S10:

- T10;
- corrales;
- agua;
- acceso amplio;
- ganado no atraviesa T03 por defecto.

---

## 13. Arquitectura y altura

El plano debe respetar:

- piedra;
- madera;
- pizarra;
- uno/dos pisos comunes;
- tres pisos minoritarios;
- baja altura en talleres/almacenes/astilleros;
- ausencia de skyline fantástico de torres;
- ausencia de muralla general.

La riqueza modifica:

- calidad;
- acabado;
- material;
- tamaño;

no el nivel tecnológico.

---

## 14. Cultura material

Punto 13 cierra el último bloqueo material.

El plano puede asumir:

- carros;
- carretas;
- establos;
- depósitos;
- talleres manuales;
- iluminación preindustrial;
- archivos físicos;
- cerraduras;
- herramientas;
- mobiliario;
- recipientes.

**No existen relojes.**

Esto no bloquea el plano.

---

## 15. Movilidad obligatoria

El plano debe admitir:

- peatones;
- monturas;
- carros ligeros;
- carros pesados;
- ganado;
- convoyes.

Los flujos pesados deben poder:

- evitar T03 cuando exista alternativa;
- alcanzar T02/T04/T07/T08/T10/T12.

La red viaria exacta se resuelve en Punto 6.

---

## 16. Entradas obligatorias

Deben mantenerse las seis aproximaciones conceptuales:

- APP01 — interior general;
- APP02 — corredor forestal/madera;
- APP03 — abastecimiento rural/ganado;
- APP04 — marítima civil;
- APP05 — fluvial;
- APP06 — suministro autorizado T08.

No son puertas urbanas.

---

## 17. Población

Canon vigente:

**12.000–18.000 residentes.**

Esto condicionará Punto 2.

No se fija aquí:

- superficie exacta;
- densidad final;
- habitantes por hectárea;
- número de edificios.

Esas decisiones pertenecen a escala/huella.

---

## 18. Crecimiento

Debe quedar:

- periferia no amurallada;
- transición gradual;
- reserva de expansión ordinaria;
- espacio compatible junto a T10/T11 y más allá de T12 según topografía.

No se reserva suelo para una instalación inventada.

---

## 19. Elementos que NO deben añadirse

Sin nuevo canon, el plano no crea:

- muralla urbana;
- ceca;
- prisión penitenciaria;
- Casa de Aduanas independiente;
- arsenal de pólvora;
- segundo complejo naval real;
- aduanas internas entre Casas;
- castillo Valrik;
- catedral/templo;
- universidad;
- academia;
- gran hospital institucional;
- banco moderno;
- gran biblioteca pública;
- teatro monumental;
- reloj de torre.

---

## 20. Decisiones abiertas — no bloqueantes

Quedan deliberadamente abiertas porque pertenecen a puntos posteriores:

### Punto 2

- anchura/longitud total;
- hectáreas urbanas;
- densidad;
- huella T08/T12;
- tamaño de periferia.

### Punto 3

- geometría del río;
- anchura/profundidad por tramo;
- litoral;
- cotas;
- pendiente;
- inundabilidad;
- forma del puente;
- necesidad de cruces menores.

### Punto 4

- polígonos exactos T01–T12.

### Punto 5

- parcelas y huellas S01–S13.

### Punto 6

- anchos y trazado de calles/corredores.

### Punto 7

- muelles, dársenas, gradas y recinto T08.

### Punto 8

- manzanas, parcelas y tejido.

### Punto 9

- comprobación causal.

### Punto 10

- mapa canónico final.

Estas aperturas no son huecos de canon general.

Son el propio trabajo del plano métrico.

---

## 21. Decisiones de autor necesarias ahora

**Ninguna.**

El Punto 1 puede cerrarse sin elegir:

- tamaño final;
- forma final;
- trazado final.

Esas decisiones se tomarán con evidencia funcional en sus puntos correspondientes.

---

## 22. Certificación

Estado:

**TRESKAL_PREPLAN_FINAL_AUDIT_PASSED**

Condiciones:

- canon superior general cerrado;
- sectores obligatorios conocidos;
- edificios/capacidades obligatorios conocidos;
- prohibiciones conocidas;
- flujos conocidos;
- decisiones abiertas correctamente asignadas;
- no existen dependencias externas que deban cerrar antes de Punto 2.

---

## Regla final

**Treskal ya no espera al lore para poder dibujarse: a partir de aquí las decisiones pendientes son decisiones de geometría urbana, no huecos del mundo.**

`TRESKAL_METRIC_PLAN_POINT_1_PREPLAN_AUDIT_CLOSED`
