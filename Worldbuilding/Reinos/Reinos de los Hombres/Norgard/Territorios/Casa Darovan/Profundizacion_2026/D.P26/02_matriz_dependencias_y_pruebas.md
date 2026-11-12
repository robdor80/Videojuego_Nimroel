# D.P26/02 — Matriz de dependencias y protocolo de cierre verificable

## Estado de GitHub comprobado el 12/11/2026, inicio de D.P26

- `main`: **512434957f248f2513761615a9685ddd6c49c65f**, con PR #45 D.P22 fusionada.
- PR #46 D.P23: **6ee4f4a672a138e29feefb558e41bbf10fbce64e**, Draft abierta, CI Windows/Linux SUCCESS (run **43192926403**; otras regresiones verdes).
- PR #47 D.P24: **b0b14db66f1cf1ca0e9eb27f28cde403e3e16a89**, Draft abierta, CI Windows/Linux SUCCESS (run **43195991648**; otras regresiones verdes).
- PR #48 D.P25: **2288d79ab03ed7d5a7509943ec140d3387b8f76f**, Draft abierta, CI Windows/Linux SUCCESS (run **43199586229**; otras regresiones verdes). Esta CI verificó #46 y #47 por SHA, pero **no fusionó las ramas**.

## Dependencia y fusión

| Orden | Trabajo | Verificación exigida antes de avanzar |
|---|---|---|
| 1 | Fusionar #46, **si el autor lo ordena expresamente** | Releer HEAD definitivo y confirmar CI/estado compatible |
| 2 | Reconciliar y fusionar #47 con el nuevo main | Comparar invariantes Treihord/rural y repetir regresión tras base actualizada si procede |
| 3 | Reconciliar y fusionar #48 | Revalidar las 52 bases/27 selecciones contra las versiones efectivamente fusionadas |
| 4 | Reconciliar y fusionar D.P26 | Ejecutar la auditoría con fuentes ya integradas, sustituir anclajes temporales sin borrar la evidencia histórica y confirmar CI final |
| 5 | Acta postmerge | Comprobar SHA final de `main`, workflows y ausencia de ramas previas en conflicto |

**No está permitido adelantar el paso 4 aunque la PR D.P26 esté verde por lectura de fuentes externas.** No fusionar, cambiar la base ni marcar como completo el trámite sin permiso de autor.

## Cómo se certifica D.P26 antes del merge

El workflow sobre Ubuntu 24.04 y Windows 2022 recupera por SHA inmutable las PR #46, #47 y #48, y ejecuta:
1. `Tools/DarovanDP26/validate.py`: fuentes, SHA de checkout, Treihord original, cinco lotes biográficos, 52 nombres/IDs únicos, 27 referencias y 30/10 grafo narrativo; UNKNOWN, materialización y autorizaciones.
2. Validadores D.P23, D.P24 y D.P25 **sobre sus árboles originales**, con D.P25 enlazado a sus dos fuentes.
3. Regresiones desde `main` D.P20, D.P21, D.P22, D.P14–D.P18 y D.P13.
4. Regresión estática D01–D12 ejecutada por su propio workflow disparado en PR.

Las pruebas por SHA externa **no prueban** una integración mergeada y no reemplazan la nueva ejecución de CI tras cambiar `main`.

## Clasificación de hallazgos

- **CRÍTICO — bloquea dictamen:** contradicción con Treihord/Norgard, nombre/ID de persona perdido o duplicado, relaciones activadas sin prueba, world state alterado, ruta/puerto/mina inventados, desconocido convertido en dato, fusión no autorizada, HEAD de dependencia desalineado.
- **MAYOR — exige corregir o aplazar materialización:** documentación de persona sin origen, trazas de permisos incompletas, escenas con acceso indebido a secretos, propuesta de comunidad confundida con emplazamiento.
- **DEUDA DE IMPLEMENTACIÓN — NO bloquea el cierre editorial:** malla, itinerario, edificio instanciado, población concreta, actor CoreRPG, agenda, persistencia o interfaz Godot pendientes pero honestamente declarados.

## Criterios de aceptación final

- Auditoría cruzada y adversarial verde en ambos sistemas sobre HEAD final.
- Sin modificación del texto original de Treihord ni contratos de CoreRPG/Godot.
- Ningún archivo fuente de D.P20–D.P25 reescrito para ocultar incompatibilidades.
- Todas las reservas persistentes visibles y clasificadas.
- Resolución expresa e individual de autorizaciones de fusión; CI postmerge confirmada.

**Esta fase deja lista una recomendación técnica; la autorización de integrar las cuatro PR sigue separada.**
