# Acta G06 — Comunicaciones y redes económicas
**Fecha:** 13/11/2026. **Base**: `8610affd134d3134b8cba17b2b43c483331b127a` (main tras PR #70 G05).

## Alcance entregado
Matriz G01 de seis corredores de estudio; seis modalidades sin servicios operativos; doce enlaces comerciales G04/G05 sin remesas; seis modelos de información sin instancias; ocho riesgos diferenciados por evidencia; protección de Forja regia G05-D01, canon fiscal y monetario único. Documento de traspaso a G07 y contrato no-runtime.

## Alcance deliberadamente no entregado
Ni trazados, ni caminos, ni puentes, ni puertos, ni peajes, ni concesiones, ni estaciones de mensajería, ni horarios, ni latencias, ni contratos reales, ni economía simulada. Nada en Godot, GDExtension o CoreRPG. Las fuentes superiores y G00–G05 históricos no se reescriben.

## Puertas técnicas de cierre (comprobar tras PR)
1. `Tools/GaldrenG06/validate.py`: positiva y mutaciones negativas.
2. Regresión G00–G05 sin fallos, workflow G06 Windows 2022 y Ubuntu 24.04 **en HEAD exacto**.
3. Diff sin modificaciones fuera del alcance.
4. Sin conflictos ni deriva de main; sin afirmar «jugable» por validar JSON.
5. Fusionar solo tras auditoría y autorización de fusión aplicable.

**Estado documental al redactar:** entregables preparados para auditoría, CI y revisión de PR; no declarar SUCCESS antes de observar resultados.
