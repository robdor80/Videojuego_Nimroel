# E19-R2 — Cuencas, red hidrográfica menor, manantiales y dinámica del agua
**14/11/2026 · Atlas hidrológico v0.3 · Fase documental B2 · Diseño delegado · NO MÉTRICO · NO RUNTIME**

Esta fase hereda R0 (PR #87, HEAD addd767de9bf27ef35e8aef6d68cde00dea79c10) y R1 (PR #89, HEAD 4472e81a88eba7a8e42528043ee426d685c76cef). R2 se apila sobre R1 y no toca canon, CoreRPG, Godot ni main. La PR #84 está descartada y su cartografía no es fuente.

## Resultado
El mapa del agua de Edranor ya tiene **reglas regionales de diseño causal**, no cursos menores declarados existentes. Hay siete familias de drenaje estudiables, catorce escenarios de microcuenca, cinco modalidades de surgencia y tres situaciones de humedal, todos condicionados a relieve, aporte y receptor; el extremo MF-08/U7 permanece NON_EVALUABLE. La única secuencia fluvial mayor confirmada es **Valkram oriental → Lurien → Lago Antela → Lurien → Hallheim → Golfo de Norgard**. El Lurien constituye solo un tramo no localizado de la frontera sur.

## Lectura
1. 01_CUENCAS_Y_DIVISORIAS.md — siete familias de cuenca, fronteras, árbol de receptores y nodos de incertidumbre.
2. 02_RED_MENOR_Y_CONECTIVIDAD.md — catorce escenarios de drenaje, jerarquías, desembocaduras y condiciones de promoción.
3. 03_MANANTIALES_RECARGA_Y_HUMEDALES.md — cinco mecanismos de fuentes, tres depresiones húmedas y protección de acuíferos.
4. 04_BALANCE_ESTACIONAL_RIESGOS.md — ciclo hídrico, nieve, estiaje, avenidas y riesgos sin calendario inventado.
5. 05_AGUA_SUELO_BOSQUE_VINO_Y_ASENTAMIENTOS.md — implicaciones verificables para Bosque Alto, Karsath, Lumina, Dorth, Rodas y R3-R5.
6. 06_CONTRATO_CAUSAL_GENERACION_Y_PERSISTENCIA.md — reglas de generador 2D y futura persistencia sin crear World State.
7. 07_AUDITORIA_PARIDAD_Y_TRASPASO_R3.md — referencia Valrik, incertidumbres, casos negativos y traspaso.
8. hydrology_v0.3.json — contrato machine-readable de estudio, no Content Pack ni catálogo ejecutable.

## Escala de evidencias
**CANON_AUTOR/CANON_REPO**: sistemas mayores, jurisdicciones, bosques y anclas humanas. **DELEGATED_DESIGN_CONDITIONAL**: siete familias hidrológicas y escenarios tipológicos, no localizados ni nombrados como cauces. **UNKNOWN**: divisorias interiores exactas, cauces y confluencias, caudal, permeabilidad real, nacimientos, acuíferos, nombres locales, derechos y concesiones. Toda promoción necesita fuente y comprobación cruzada.

## Controles irrevocables
Valkram: oeste Darovan / este Edranor. Azurios: oeste Edranor / este Galdren. Antela al sur de Karsath, sin ribera urbana demostrada. Dorth sin gran río confirmado. Caleran (canon de Norgard) no se implanta en Dorth por similitud de cordillera. Bosque Alto gestionado, Bosque Real de Corona; Rodas ALDEA de Corona Aethros, Hallheim exterior. Norte sin unión ficticia ni asignación de U7. No confundir aguas naturales con abastecimiento, obras, derechos o caminos.

**Resultado de madurez:** documentación de diseño B2; **cero** cauces menores instanciados, manantiales verificados, geometrías, licencias, puentes, presas, parcelas o entidades de World State. B3/B4 no acreditados.
