# DAROVAN D05 — Matriz de invariantes y pruebas v0.1
**Estado:** plan y validador Python, no-runtime. Ninguna geometría o servicio de transporte creado por disponer de JSON.

## Trazabilidad de contratos
- Archivo principal: `Datos operativos/darovan_d05_mobility_communications_v0.1.json`.
- `Validacion/validate_d05.py` coteja archivos del **checkout íntegro**: D01 relieve, D02 hidrografía, D03 clima, D04 economía, Core navegación y mensajes, Norgard navegación civil E7 y fiscalidad E8.
- 23 rutas de fuentes verificadas como archivos existentes; clase AUTHORED solo para hechos y funciones confirmados.
- Script reproducible: `python "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan/Validacion/validate_d05.py"`.

## Invariantes positivos
| Área | Requisito controlado |
|---|---|
| Forma y jerarquía | schema/version/fase, fuente de autoridad, no-runtime y etiquetas |
| Cartografía | Sin coordenadas, polilíneas, distancias, tiempos, capacidades, embarcaderos, puentes o vados nuevos |
| Nodos | 17 claves técnicas únicas; cuatro ciudades auténticas, Arven no asignada |
| Aristas físicas | Solo camino Veldora–Treihord, transporte por barcaza Belara y galería protegida La Vena |
| Dependencias | Cuatro relaciones de suministro separadas de aristas transitables; carbón Azurios y madera Pilares sin trayecto |
| Aguas | Belara no atraviesa Treihord, barcazas someras; Lhera escisión; Veldora independiente; Thalen único y dos brazos |
| Puertos | Treihord industrial, Veldora mercantil, Taramin pesquera, Syvaris seguro insular; ninguno conectado arbitrariamente |
| Gobernanza | Sin aduanas internas entre Grandes Casas, Crisol no ceca y Arven UNKNOWN |
| Mensajería | Plazas canónicas de Treihord; no servicio de postas inventado, entrega≠lectura |
| Riesgos | Cinco escenarios de comprobación condicional; ninguno representa suceso o cierre actual |
| Canon | DAR-P01/P04/P07/P08/P09/P10/P11 abiertos; no canon nuevo |
| Runtime | Ninguna ruta dinámica, envío real, simulación, inventario ni persistencia |

## Pruebas negativas incluidas
El script crea **30 copias mutadas**, desde carretera añadida, ruta rectificada, puente y kilómetros inventados, Belara profundo, Vena pública, Arven adjudicada, Thalen reducido, Veldora conectado, carbón convertido en barcaza, madera como carretera, travesía entre puertos no demostrada, falsa posta, cierre climático real, datos de riesgo inventados, fuentes rotas, IDs duplicados, falso runtime y puerto con función reescrita. Todas deben ser rechazadas para que el validador termine con código 0.

## Alcance
GitHub Actions matriz Ubuntu 24.04 / Windows 2022 ejecutará secuencialmente los validadores D01, D02, D03, D04 y D05 en un checkout completo. **Antes de observar la ejecución real, esta matriz no afirma que Python haya pasado.** No hay pruebas de Godot, CoreRPG live, GIS, MSI físico ni Samsung Tab S9+. Esas pertenecen al desarrollo del motor/D11.

## Evidencia tras ejecución real (21-10-2026)
En [run #39587112092](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39587112092) los dos jobs Windows 2022 y Ubuntu 24.04 han terminado `success` en D01–D05. Salida D05 real idéntica: `D05 STATIC OK: 17 nodes, 3 attested modal links, 4 non-route supply relations, 23 source paths, 30 negative mutations; NOT RUNTIME`. El acta nueva requiere repetición CI para su propio commit final. Ningún motor ni GIS ejecutado.


### Anexo canónico aprobado por el autor — 21/10/2026

Las referencias de esta fase que afirmaban **Arven UNKNOWN**, **cuatro ríos** o **río Veldora no identificado** son históricas y se sustituyen por esta decisión expresa del autor:

- **DAR-P01 RESUELTA:** Arven pertenece formalmente a Casa Darovan. No se autoriza por ello puerto, travesía o ruta comercial nueva.
- **DAR-P07 RESUELTA:** el cauce verde junto al sur de Veldora es el **río Veldora**, independiente del sistema Belara/Lhera.
- **DAR-P08 PARCIALMENTE RESUELTA:** cinco ríos nombrados según flechas del mapa confirmado: **Belara** (azul, río principal desde el norte y junto a Treihord), **Lhera** (rojo, rama del Belara hasta el litoral al norte de Veldora), **Veldora** (verde), **Fhalion** (amarillo, nuevo río menor al sur del Veldora), **Thalen** (violeta, al otro lado de las montañas con dos brazos finales alrededor de Taramin). **Cuatro sistemas hidrográficos:** Belara/Lhera, Veldora, Fhalion, Thalen.
- **DAR-P04 aún abierta:** la escala gráfica de **400 millas** aportada por el autor no constituye levantamiento topográfico verificado. Nacimientos exactos, caudales, cotas, recorridos métricos, bifurcación Belara/Lhera, desembocadura precisa del Fhalion, puentes, vados, navegación y accesos siguen pendientes. No deducir rutas a Arven o por Fhalion.

**Corrección retroactiva de las referencias documentales D01–D05, no una reapertura de sus implementaciones ni runtime.** El grafo D02 pasa a 5 ríos / 4 redes / 15 nodos / 11 enlaces topológicos simbólicos, manteniendo D05 sus 17 nodos logísticos y 3 conexiones modales acreditadas. Los hitos documentados anteriormente permanecen como actas de lo que se sabía en aquella fecha.
