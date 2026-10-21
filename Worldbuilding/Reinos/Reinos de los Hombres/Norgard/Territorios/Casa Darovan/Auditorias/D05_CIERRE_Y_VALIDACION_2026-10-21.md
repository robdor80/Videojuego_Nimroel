# DAROVAN D05 — Acta de cierre documental, auditoría y validación estática
**Fecha:** 21-10-2026. **Estado:** D05 documentalmente concluida y validada en CI para revisión del autor. **SIN FUSIONAR A MAIN; NO CANON NUEVO; NO RUNTIME.**
**Repositorio:** `robdor80/Videojuego_Nimroel` · **PR:** [#30](https://github.com/robdor80/Videojuego_Nimroel/pull/30).
**Rama:** `feat/darovan-d05-rutas-comunicaciones`, creada desde `main` @ `d4a07ba25f8560d5005a52aafc763699917f2388` tras comprobar PR #20 `merged=true` y el HEAD real.

## 1. Investigación y fuentes
Se revisaron el traspaso D05, registro de fases, bloqueos, plan, actas y datos D01–D04 en `main`; originales de Norgard (Treihord, Grandes Casas, ríos y lagos, mares y costas, bosques, montañas, geografía, regiones, clima y fichas visuales); Nimroel Core (hidrografía, navegación persistente, transacciones y mensajería MSG) y Norgard Defaults E7 navegación civil, E8 aduanas. Se verificó que CoreRPG `main` incluía la fase 4.13 (SHA `4f282863737bcd8f5add401202a9e1064c133672`) y que las fases NIM incorporan preparación nativa GDExtension, pero **no** integración jugable territorial D05. El índice D05 contiene **23 fuentes con rutas reales de checkout**; no modifica ninguno de esos originales.

## 2. Entregables completados
- `Rutas_y_comunicaciones/01_red_modal_y_corredores_v0.1.md`: nodo/corredor y prueba de procedencia; distinción estricta de rutas geográficas no materializadas.
- `Rutas_y_comunicaciones/02_logistica_puertos_y_dependencias_v0.1.md`: cadena de mineral y Belara, carbón Azurios sin itinerario, madera Pilares sin carretera; funciones portuarias de las cuatro ciudades.
- `Rutas_y_comunicaciones/03_mensajeria_riesgos_y_limites_v0.1.md`: Plaza del Camino (mensajeros) y Plaza Vieja (avisos) de Treihord; MSG de Core (entrega distinta de lectura), riesgos condicionales, no eventos.
- `Datos operativos/darovan_d05_mobility_communications_v0.1.json`: **17 nodos** de índice técnico, **3 conexiones físicas acreditadas cualitativamente**, **4 dependencias económicas NO transitables**, **4 puertos/funciones**, **3 anclas/criterios de comunicación**, **5 riesgos potenciales**, **7 decisiones/lagunas persistentes**, **23 referencias**. Sin coordenadas ni tiempos.
- `Validacion/validate_d05.py` y `Validacion/D05_MATRIZ_INVARIANTES_Y_PRUEBAS_v0.1.md`: integridad y **30 alteraciones maliciosas/negativas** para detectar topónimos, rutas, administración o runtime falsos.
- Workflow `.github/workflows/darovan-static-regression.yml` amplía matriz CI D01–D05. Índices, plan, control de canon y `TRASPASO_D06.md` actualizados; D06 NO iniciado.

Las tres conexiones cualitativas son: (1) camino principal **Veldora–Treihord** junto a la Linde sin justificar paso por el bosque; (2) tramo funcional de **barcazas de poco calado por Belara** hacia el puerto industrial Treihord desde puntos de carga sin identificar; (3) **La Vena**, galería fortificada de uso restringido entre Crisol y Bóveda. El inventario **NO** revela su geometría ni asigna una distancia; conexiones económicas no implican carretera adicional.

## 3. Evidencia REAL ejecutada en GitHub Actions
[Run #39587112092](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39587112092), commit D05 validado `54e2e5c3c58a101ba639134360c8c784f9708aa7` (**antes de incorporar esta acta; nueva CI debe verificar el HEAD final**).

| Entorno y job | D01 | D02 | D03 | D04 | D05 |
|---|---|---|---|---|---|
| [Ubuntu 24.04, job 119178643255](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39587112092/job/119178643255) | OK | OK | OK | OK | OK |
| [Windows Server 2022, job 119178643649](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39587112092/job/119178643649) | OK | OK | OK | OK | OK |

Salida **observada en ambos registros**:
```text
D01 STATIC OK: 12 unidades, 4 ciudades, 12 fuentes, sin runtime
D02 STATIC OK: 4 ríos, 3 redes, 13 nodos, 10 aristas, 8 pruebas negativas; NO runtime
D03 STATIC OK: 12 qualitative units, 13 references, 10 negative tests; NOT RUNTIME
D04 STATIC OK: 12 zones, 8 chains, 19 sources, 16 negative tests; NOT RUNTIME
D05 STATIC OK: 17 nodes, 3 attested modal links, 4 non-route supply relations, 23 source paths, 30 negative mutations; NOT RUNTIME
```
Los diez pasos Python D01–D05 en ambas plataformas han concluido `success` con checkout íntegro, incluidos negativos de D02–D05. Estos logs, y no afirmaciones anteriores, certifican el resultado. Al publicar esta acta se añade un nuevo commit: **comprobar la ejecución de CI para ese commit y registrarla en PR antes de autorizar merge**.

## 4. Canon protegido
Treihord/Veldora/Taramin/Syvaris son las cuatro ciudades manuales, Karsath fuera; Arven sin dueño formal acreditado. Belara pasa junto a Treihord sin atravesar casco; su acceso industrial acepta solo barcazas someras. Lhera se bifurca de Belara; Veldora independiente; Thalen único y dividido en dos brazos terminales con Taramin en medio. No alterar la importación de carbón Azurios, el uso de Pilares para minas Valkram, los puertos de Veldora mercantil/Taramin pesquero/Syvaris insular seguro, ni la ausencia de aduanas internas entre Grandes Casas. Ninguna propuesta fue promovida a AUTHORED por inferencia.

## 5. Límites y restricciones pendientes
- **Desconocido/no autorizado:** distancias, kilómetros, coordenadas, alturas, puentes, vados, itinerarios del carbón y de la madera, acceso terrestre Taramin, rutas marítimas entre puertos, cabotaje a Syvaris, rutas Arven, estaciones de postas y plazos de mensajería; tampoco capacidades, caudales, niveles, horario de navegación, caladeros o meteorología cuantificada.
- **Sin ejecutar:** GIS y cartografía métrica, recorrido físico en MSI, Godot, integración C++ CoreRPG/GDExtension aplicada a D05, motores de rutas/navíos, stocks/movimiento de bienes, envío/recepción y conocimiento de mensajes, NPC y persistencia. El éxito Python NO es un certificado jugable.
- **Pendientes de autor, sin resolver ni bloquear cierre estático:** `DAR-P01/P04/P07/P08/P09/P10/P11`, en `DECISIONES_Y_BLOQUEOS.md`. Toda decisión sustantiva espacial, histórica, política o de nuevas vías exige aprobación autoral.

## 6. Responsabilidades siguientes (no ejecutadas)
- **D06:** aldeas/pueblos/villas, modelos y posibilidades procedurales; acceso a vías solo comprobadas, nunca inferir asentamiento por nodo técnico.
- **D07:** diseño manual y operación particular de las cuatro ciudades y puertos; resolver incertidumbres Taramin/Veldora/Syvaris mediante fuente/autor.
- **D08:** población, empleo, mensajeros reales, demanda, servicios y suministros.
- **D11:** grafo ejecutable en CoreRPG/Godot, conexión navegable, viajes y restricciones dinámicas, mensaje con portador/posesión/lectura, inventarios/cargas, persistencia y pruebas cruzadas.
- **D12:** auditoría integral del territorio y decisiones canónicas consolidadas.

## 7. Control de integración y salida
Comparación previa al acta: base `d4a07ba2` → cabeza `54e2e5c3`, **2 commits por delante, 0 detrás, 14 archivos**: 13 exclusivamente bajo `Casa Darovan` y el workflow CI autorizado. Ningún original Norgard, otra Casa, CoreRPG o juego ha sido modificado. La PR #30 queda sometida a revisión humana; el autor autoriza o rechaza fusión. **No iniciar D06 antes de comprobar D05 fusionada en `main`.**
