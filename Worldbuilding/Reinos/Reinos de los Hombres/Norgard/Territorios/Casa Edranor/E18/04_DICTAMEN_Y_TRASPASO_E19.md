# E18 — Acta provisional, decisiones y traspaso a E19

## Dictamen de auditoría
**FAVORABLE A CONTINUAR EL DESARROLLO DOCUMENTAL, CON PUERTAS MATERIALES NO SUPERADAS.** No equivale a certificación B3, B4 ni implementación jugable. E13–E17 aportan una base conceptual coherente en las diez dimensiones; la ausencia de georreferencia, censo, rutas y actores reales sigue siendo visible. El cierre técnico de E18 está condicionado al PASS del workflow en el HEAD exacto de su PR, a la revisión del diff y a la ausencia de deriva de main.

## Decisiones adoptadas por delegación
| Código | Decisión | Alternativa descartada |
|---|---|---|
| ED18-DEC-01 | Mantener diez dimensiones B2 hasta evidencia material | Ascenso B3 por número de documentos/tests |
| ED18-DEC-02 | E19 puede adquirir fuentes y diseñar calibración no métrica | Dibujar mapa georreferenciado por intuición |
| ED18-DEC-03 | Conservar 7 EDD abiertas y EDD-06 de Rodas resuelta para diseño | Cerrar deuda por repetición documental |
| ED18-DEC-04 | Separar huecos de evidencia de contradicciones probadas | Declarar canon contradictorio sin dos afirmaciones |
| ED18-DEC-05 | No tocar E00–E17, CoreRPG, Godot ni packs | Corregir fuentes históricas sin autorización |

**Autoridad:** `ASSISTANT_DELEGATED_AUDIT`. Ninguna decisión ratifica soberanía, sucesión o historia consumada.

## Traspaso controlado a E19
**Permitido desde el primer momento:** búsqueda y cotejo de mapas fuente; inventario de hitos, líneas y capas; metodología de CRS 2D; propuesta de puntos de control; informe de calidad; reconstrucción esquemática identificada como NO MÉTRICA.

**Puerta roja para implementar geometría:** no hay perímetro septentrional ratificado ni escala en metros por píxel; no debe atribuirse a Godot un trazado localizado. E19 puede dividirse en adquisición/reconstrucción + ratificación de mapa si faltan fuentes. La ausencia de mapa de autor es una dependencia verdadera, no se desbloquea por delegación genérica.

**Evidencias de salida requeridas para E19:**
- EDD-01: fuente del autor íntegra o vértices de cierre ratificados; polígono topológicamente válido.
- EDD-02: tres controles no colineales, escala y transformación reversible con error documentado.
- EDD-03: DEM/cuencas/receptores con drenaje coherente; permisos y potabilidad son pruebas adicionales donde proceda.
- EDD-07: trazas, pendientes, cruces y derechos, con un grafo físico real separado de preguntas de demanda.

## Condiciones de publicación y fusión E18
PR exclusivamente documental E18 + contrato + validador + CI; revisión contra el SHA base `b4fb1ed9ce114e1532251e28c205eaecf42dbe08`; tests positivos y adversariales; regresiones E00–E17 Windows/Linux; E11 schema locks y consumidor C++20 CTest con Core fijado. Si falla algo, mantener Draft. La siguiente fase E19 se tramita en rama/PR independiente; E18 no la ejecuta.

**Estado administrativo al redactar:** acta editorial favorable con puertas abiertas; no afirmar certificación CI hasta verificarla realmente.
