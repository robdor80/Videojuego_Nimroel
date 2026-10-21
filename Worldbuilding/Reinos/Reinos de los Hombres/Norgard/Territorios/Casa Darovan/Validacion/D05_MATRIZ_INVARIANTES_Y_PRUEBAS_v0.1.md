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
