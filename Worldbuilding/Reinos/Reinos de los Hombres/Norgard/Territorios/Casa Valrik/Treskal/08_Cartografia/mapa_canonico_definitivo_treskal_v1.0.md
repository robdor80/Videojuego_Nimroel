# Treskal — mapa canónico definitivo v1.0

## Estado

**PLANO MÉTRICO — PUNTO 10 CERRADO**

Marcador:

`TRESKAL_METRIC_PLAN_POINT_10_CANONICAL_MAP_CLOSED`

Contrato:

`../Datos operativos/treskal_canonical_map_contract_v1.0.json`

---

## 1. Qué queda cerrado

El mapa de Treskal deja de ser una suma de contratos parciales.

A partir de v1.0 existe una única geometría espacial canónica que integra:

- geografía;
- sectores;
- instalaciones;
- red viaria;
- puerto y Armada;
- tejido urbano;
- bloques;
- parcelas;
- agua;
- residuos;
- reservas;
- accesos marítimos.

No se modifica ninguna decisión geométrica validada en Puntos 2–9.

---

## 2. Sistema métrico

Referencia:

**TRESKAL_LOCAL_METRIC_V1**

Unidad:

**metro**

Norte:

**+Y**

La referencia es local y ficticia.

No es geodesia terrestre.

---

## 3. Export espacial maestro

Archivo:

`exports/treskal_canonical_spatial_export_v1.0.geojson`

Contiene:

**2.404 features con ID único.**

Entre ellas:

- 1 envolvente de planificación;
- río y costa;
- 1 Puente de los Gemelos;
- 11 polígonos de sector;
- S01–S13, con S09 materializado en sus dos componentes;
- C01–C18;
- L01–L12;
- UF01–UF12;
- B001–B110;
- P0001–P2175;
- W01–W10;
- WR01–WR06;
- PFA01;
- muelles fluviales;
- puerto civil;
- gradas;
- atraques navales;
- rompeolas;
- fondeadero civil;
- rada naval;
- accesos marítimos;
- agua naval restringida;
- bandas de transición;
- GR1–GR3.

---

## 4. Parcelas

Punto 10 materializa por primera vez las líneas visibles de las parcelas.

Se mantienen:

- **110 bloques/agrupaciones**;
- **2.175 parcelas**;
- los rangos exactos de IDs fijados en Punto 8.

La materialización es:

- determinista;
- fuera del runtime;
- estable;
- no procedural durante la partida.

Una parcela no recibe necesariamente un negocio u hogar fijo.

Su uso compatible sigue pudiendo depender del estado del mundo.

---

## 5. Plano técnico maestro

Archivo:

`mapas/treskal_plano_tecnico_canonico_v1.0.svg`

Es la referencia humana más detallada.

Muestra:

- T;
- S;
- C;
- L;
- UF;
- bloques;
- líneas parcelarias;
- fuentes;
- muelles;
- fondeaderos;
- rutas marítimas;
- reservas de crecimiento;
- bandas de transición.

Los IDs de parcela están en el SVG/GeoJSON, pero no se imprimen 2.175 textos encima del mapa.

---

## 6. Plano operativo de juego

Archivo:

`mapas/treskal_plano_operativo_juego_v1.0.svg`

Está pensado para:

- navegación;
- sistemas;
- IA;
- misiones;
- logística;
- depuración.

Reduce el ruido parcelario sin cambiar la geometría.

---

## 7. Mapa legible para lore

Archivo:

`mapas/treskal_mapa_legible_lore_v1.0.svg`

Es una versión limpia.

No inventa:

- nombres oficiales de barrios;
- nombres de calles.

Los rótulos como:

- Mercado y comercio;
- Puerto civil;
- Carpinteros y talleres;
- Barrios residenciales;

son descripciones funcionales.

No son topónimos canónicos.

Esta versión servirá como base para crear después mapas diegéticos.

---

## 8. Escala

En la geometría SVG:

**1 unidad = 1 metro del sistema local.**

Incluye barra de:

**500 m**.

Las dimensiones visuales de pantalla o impresión pueden cambiar.

Las distancias canónicas deben obtenerse de las coordenadas, no de píxeles de una captura.

---

## 9. Identidad espacial

El modelo permite consultas del tipo:

**posición → Pxxxx → Bxxx → UFxx → Txx → Treskal**

Ejemplo conceptual:

un NPC puede vivir en `P1452`, dentro de `B075`, dentro de `UF08`.

El nombre visible de la calle puede cambiar o incluso no estar definido todavía sin romper su identidad espacial.

---

## 10. Agua

El export incluye geometría real de:

- CP01–CP04;
- CP05/CP06;
- CIV_ANCH_01;
- MR_TRESKAL_CIVIL_APPROACH;
- NSW01–NSW05;
- NFP01–NFP03;
- NBQ01/NBQ02;
- NBW01;
- NAV_ROADSTEAD_01;
- NAV_SEC_WATER_01;
- MR_TRESKAL_NAVAL_APPROACH.

No hay marcadores falsos en el origen.

---

## 11. Reserva de crecimiento

GR1–GR3 se representan de forma explícita.

Total preservado:

**25,82 ha**.

No son barrios construidos.

---

## 12. Toponimia

Punto 10 no resuelve nombres oficiales de calles o barrios porque no eran necesarios para cerrar la geometría.

Los IDs técnicos:

- T;
- C;
- L;
- UF;
- B;
- P;

no son nombres diegéticos.

---

## 13. Qué puede hacerse ahora

El plano métrico de Treskal queda completo.

A partir de esta misma geometría pueden crearse productos distintos:

- mapa de mercader;
- mapa oficial Valrik;
- plano naval restringido;
- mapa viejo o incompleto;
- mapa de exploración del jugador.

Esos mapas podrán:

- ocultar información;
- simplificarla;
- estar desactualizados;
- contener errores diegéticos.

Pero no cambiarán la Treskal real.

---

## Certificación

**TRESKAL_CANONICAL_MAP_V1_PUBLISHED**

**TRESKAL_METRIC_PLAN_COMPLETE**

`TRESKAL_METRIC_PLAN_POINT_10_CANONICAL_MAP_CLOSED`

---

## Regla final

**Desde este punto, cualquier mapa de Treskal es una representación de la ciudad canónica; ya no una nueva interpretación de su geometría.**
