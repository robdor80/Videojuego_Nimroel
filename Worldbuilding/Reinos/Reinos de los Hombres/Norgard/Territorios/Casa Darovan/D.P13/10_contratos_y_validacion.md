# D.P13 — Contratos operativos y criterios de prueba

**NO RUNTIME / NO CANON NUEVO — 25-10-2026.** Este documento registra la interfaz conceptual para D.P14–D.P18. No promete una implementación C++ o Godot existente.

## Archivos estructurados

- `Datos operativos/darovan_dp13_physical_profiles_v0.1.json`: doce perfiles físicos de estudio, diferenciación territorial por dimensión y fuentes.
- `Datos operativos/darovan_dp13_hydro_overlay_v0.1.json`: cuatro sistemas mayores inmutables, candidatos de red menor, topología protegida y receptores por verificar.
- `Datos operativos/darovan_dp13_environment_causal_v0.1.json`: cadena causal, precedencia, estados potenciales, variables persistibles y ocho casos de rechazo.
- `Tools/DarovanDP13/validate.py`: validación de estructura, fuentes, integración con D01–D03 y mutaciones adversariales.

## Contrato de consulta conceptual

Entrada: `studyUnitId`, geometría física real o `UNKNOWN`, estado meteorológico observable o `UNKNOWN`, temporada si definida, suelo/cubierta si definidos y un registro de cambios previos si existe. Resultado: descripción de condiciones respaldadas, derivaciones **condicionales** y campos no resueltos; nunca entidades canónicas automáticas.

## Autoridad y persistencia

1. El canon de Norgard, decisiones del autor y anclas D00–D12 prevalece.
2. El generador potencial solo evalúa opciones válidas; semilla estable, versión de generador y geometría son futuras precondiciones.
3. Identidad física de un segmento y caudal temporal no son el mismo dato.
4. Versionar definiciones y migraciones antes de cambiar instancias materiales.
5. Solo CoreRPG, una vez implementado, puede convertirse en autoridad del WorldState: ahora ninguna variable se escribe en un savegame.
6. Godot representa resultados validados, no resuelve geografía ni inventa cauces.
7. Gemini/IA narra datos procedentes del sistema; no altera por cuenta propia el estado.

## Pruebas negativas prioritarias

Rechazar ciudad extra, Karsath adscrita, Arven sin Darovan, Belara cruzando Treihord, conexión Veldora-Lhera, Fhalion con boca asignada, Thalen con brazos alterados, bosque Pilares o Taramin dividido, población en interior Agujas, coordenadas o mediciones inventadas y banderas de runtime verdaderas. Rechazar también zonas omitidas, referencias inexistentes, reglas sin requisitos, duplicados y un caso negativo que permita generación incoherente.

## Pruebas posteriores a D.P13

Los contratos solo demostrarán consistencia documental. Para declarar juego real hacen falta terreno de producción, resolución espacial CoreRPG, GDExtension, representación 2D Godot y ensayos físicos Windows x64/Android ARM64; fuera del alcance de esta fase.
