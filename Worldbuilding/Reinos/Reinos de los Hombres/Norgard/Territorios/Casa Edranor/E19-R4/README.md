# E19-R4 — Pasos, caminos y corredores territoriales de Edranor
**14/11/2026 · Atlas vial causal v0.5 · B2 documental · NO carretera ni ruta materializada**

## Mandato
Aplicar el **estándar Valrik/Treskal**: la comunicación nace del relieve, agua, firmes, jurisdicción, tránsito, producción, mantenimiento y memoria; jamás de la necesidad de unir dos puntos con una raya. La fuente comparada es la geografía de Valrik y las redes urbanas de Treskal, con jerarquías de uso, desvíos logísticos, accesos controlados, conocimiento del viajero y estados persistentes. **No se trasplanta su cartografía, sus 18 ejes, sus anchuras, el Puente de los Gemelos ni sus ríos**.

Se apila sobre E19-R3, PR #91, HEAD **8887445eec5996d18f4c63b849f568ea39c8b0ef**, a su vez sobre R2 #90, R1 #89 y R0 #87. El contenido B2 de E05, E16 y E17 se mantiene como hipótesis y precedentes, no como red comprobada. La PR #84 fue descartada: prohibido reutilizar su geometría.

## Capas y autoridad
- **CANON_AUTOR:** Valkram occidental Darovan/oriental Edranor; Azurios occidental Edranor/oriental Galdren; sur administrativo salvo tramo no localizado del Lurien; norte abierto; Rodas aldea de Corona Aethros.
- **CANON_REPO:** Dorth (sede, tinto), Lumina (pequeña, blanco y feria anual), Karsath (vino selecto); Bosque Alto con corta regulada; Bosque Real regio; Antela al sur de Karsath, Lurien con secuencia mayor y Hallheim fuera.
- **ASSISTANT_DELEGATED_DESIGN:** tipologías viarias, preguntas de corredor, escenarios condicionales, matrices funcionales y puertas de evidencia. No dan título de camino ni derecho.
- **UNKNOWN:** tramos reales, collados, longitudes, pasos, vados, puentes, calzadas, firmes medidos, permisos, tiempos, pendientes, cruces, viajeros activos y redes de mensajería.

## Índice de entrega
1. [01_JERARQUIA_Y_GRAFOS.md](01_JERARQUIA_Y_GRAFOS.md): necesidades Gd, preguntas Gq, red física Gp y ocho clases funcionales.
2. [02_ATLAS_DE_CORREDORES.md](02_ATLAS_DE_CORREDORES.md): **12 expedientes CT**, 11 bajo estudio y CT-12 bloqueado.
3. [03_PASOS_CRUCES_Y_TRANSICIONES.md](03_PASOS_CRUCES_Y_TRANSICIONES.md): collados, agua, divisorias, mínimos físicos y rechazo de atajos.
4. [04_CARGAS_VIAJEROS_Y_HITOS.md](04_CARGAS_VIAJEROS_Y_HITOS.md): siete flujos funcionales, uso humano y consecuencias económicas.
5. [05_JURISDICCION_Y_PROTECCION.md](05_JURISDICCION_Y_PROTECCION.md): derechos, Corona, bosques, mantenimiento, fiscalidad y seguridad.
6. [06_ESTACIONALIDAD_Y_DETERIORO.md](06_ESTACIONALIDAD_Y_DETERIORO.md): 10 mecanismos de riesgo y conservación verificables.
7. [07_VIAJE_CONOCIMIENTO_Y_MEMORIA.md](07_VIAJE_CONOCIMIENTO_Y_MEMORIA.md): viajeros, mensajes, mercancías, conocimiento y estado persistente.
8. [08_CONTRATO_DE_CARTOGRAFIA_2D.md](08_CONTRATO_DE_CARTOGRAFIA_2D.md): pruebas de promoción B2→B3→B4, autoridad y separación datos/estado.
9. [09_PARIDAD_VALRIK_Y_ADVERSARIOS.md](09_PARIDAD_VALRIK_Y_ADVERSARIOS.md): comparativa y negaciones exigibles.
10. [10_ACTA_Y_TRASPASO_R5.md](10_ACTA_Y_TRASPASO_R5.md): estado, deudas, puntos de control y siguiente fase.
11. [routes_v0.5.json](routes_v0.5.json): contrato legible por máquina, **0 caminos/puentes/vados/estaciones reales**.
12. Tools/EdranorE19R4/validate.py y CI Windows/Linux con regresión R0–R3, mutaciones y casos adversariales.

## Convención que impide falsos caminos
CT-01..CT-11 = **expedientes de estudio**; CT-12 = **veto del norte sin evaluar**. No son aristas para pathfinding, carreteras canónicas ni nombres en mapas. Los topónimos EDR-G son contextos de diseño, no puntos topográficos medidos. Los riesgos HZ son reglas, nunca cierres producidos. El potencial logístico no demuestra acceso físico.

**Estado:** paridad metodológica B2 con Valrik en la capa de movilidad, pero sin paridad métrica B3, red jugable B4 ni conexión a World State. El R5 no puede asumir accesibilidad solo por presencia de CT; necesita Gp certificado.