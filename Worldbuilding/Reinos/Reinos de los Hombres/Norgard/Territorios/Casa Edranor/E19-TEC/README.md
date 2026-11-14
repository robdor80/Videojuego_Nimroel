# E19-TEC — Puente espacial técnico Edranor → Godot 2D

14/11/2026. **Estado: infraestructura verificable; no B3, no B4, sin geometría de Edranor aprobada.**

## Para qué sirve
La geografía narrativa R0–R6 ya permite razonar sobre montañas, cuencas, suelos, caminos y habitabilidad sin coordenadas. E19-TEC es la fase posterior que transforma **solo evidencias realmente espacializadas** en un paquete de geometría 2D apto para que Godot lo lea. CoreRPG seguirá poseyendo los hechos, permisos, identidades, inventarios y World State. El Host 2D conversacional no precisa dibujar un mapa para jugar.

**Entrega inicial técnica:** contrato de entrada, manifiesto de ausencias, comprobador geométrico, topológico y de procedencia, exportación determinista de sector y pruebas adversariales. No se añade una carretera/aldea/caudal/edificio por rellenar un JSON.

## Archivos y ejecución
- technical_manifest_v0.1.json: inventario de ausencia y puertas de aceptación.
- 01_CONTRATO_ESPACIAL_Y_AUTORIDAD.md: unidad, sector, procedencia, geometrías y validaciones.
- 02_PUERTAS_Y_ENTREGA_AL_MOTOR.md: responsabilidades y criterios.
- 03_PARIDAD_METODOLOGICA_VALRIK_TRESKAL.md: comparación directa con el método de Valrik y sus restricciones, sin condicionar B2 a una cartografía métrica.
- Tools/EdranorE19TEC/spatial.py: verificador y exportador separado de Game/CoreRPG.
- Tools/EdranorE19TEC/test_spatial.py: pruebas positivas sintéticas y rechazos.
- Workflow CI: Linux + Windows con regresiones E19-R0–R6.

Uso local desde raíz del repositorio:
python Tools/EdranorE19TEC/test_spatial.py
python Tools/EdranorE19TEC/spatial.py --input mi_sector_autorizado.json --output sector_para_godot.json

El segundo comando **rechaza** un sector sin autoría, aprobación B3, referencia espacial e información material real. No se incluye aquí ningún mi_sector_autorizado.json porque todavía no existe evidencia para él.

## Criterio de cierre
Código probado != sector cartografiado. B3 exige fuente autoral/medición, escala/transformación y precisión, geometrías coherentes, permisos y acta de aceptación **por sector**; B4 exige carga efectiva Godot 4.7.2 y CoreRPG, save/load, determinismo y pruebas de Windows/Android. No declarar paridad completa de Edranor/Treskal por aprobar este pipeline.

Rama apilada sobre E19-R6 #94, heredera de R0 #87 → R5 #93; nunca reutilizar #84 descartada. No fusionar esta rama directamente a main mientras esté pendiente la genealogía.
