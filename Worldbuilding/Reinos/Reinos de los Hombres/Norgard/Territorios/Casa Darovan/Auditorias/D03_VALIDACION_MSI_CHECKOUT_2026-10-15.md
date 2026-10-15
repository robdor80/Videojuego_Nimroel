# Darovan D01–D03 — Validación Python sobre checkout real del MSI (15-10-2026)

**Resultado: SUPERADA — validación estática Python D01, D02 y D03 sobre repositorio completo.**

## Procedencia y entorno
- Evidencia: salida literal de CMD aportada por el autor el **15-10-2026** en esta conversación y capturas previas de GitHub Desktop/Explorador de Windows.
- Directorio de ejecución: `C:\Users\andro\Documents\GitHub\Videojuego_Nimroel` (raíz del checkout).
- Repositorio: `robdor80/Videojuego_Nimroel`.
- Rama activa mostrada en GitHub Desktop: `feat/darovan-d03-clima-ecosistemas`, PR #17; GitHub Desktop mostró 0 cambios locales.
- Ejecución con `python` en CMD de Windows, con tres llamadas encadenadas mediante `&&`, de modo que el segundo/tercer validador solo se ejecuta si el anterior devuelve éxito.
- No se midieron versión exacta de Python ni hash local del HEAD del MSI; no se presume su valor.

## Comandos ejecutados

```cmd
python "Worldbuilding\Reinos\Reinos de los Hombres\Norgard\Territorios\Casa Darovan\Validacion\validate_d01.py" && python "Worldbuilding\Reinos\Reinos de los Hombres\Norgard\Territorios\Casa Darovan\Validacion\validate_d02.py" && python "Worldbuilding\Reinos\Reinos de los Hombres\Norgard\Territorios\Casa Darovan\Validacion\validate_d03.py"
```

## Salida de CMD aportada por el autor (literal)

```text
D01 STATIC OK: 12 unidades, 4 ciudades, 12 fuentes, sin runtime
D02 STATIC OK: 4 ríos, 3 redes, 13 nodos, 10 aristas, 8 pruebas negativas; NO runtime
D03 STATIC OK: 12 qualitative units, 13 references, 10 negative tests; NOT RUNTIME
```

El símbolo del sistema volvió al prompt del repositorio, sin trazas de error. **Tres pruebas estáticas Python OK, incluyendo ocho mutaciones negativas D02 y diez D03.**

## Decisión de cierre y límites
- **RESUELTO:** pendiente de ejecutar los tres validadores Python sobre un checkout completo real con los documentos y JSON de referencia; ya no corresponde conservar el estado `PENDIENTE — CHECKOUT ÍNTEGRO` para estas pruebas.
- **Conservado:** acta de ejecución previa en entorno Python aislado como historial de pruebas complementarias, sin equipararla a esta ejecución íntegra.
- **Fuera de alcance:** no acredita integración de Godot, ejecución CoreRPG, GIS, precisión cartográfica, parámetros medidos, simulación de clima/agua, rendimiento ni persistencia en runtime. Tampoco afirma pruebas CI de GitHub Actions.
- **Administración GitHub:** D03 sigue en PR #17, **no fusionada**. **D04 no iniciada** por decisión del autor. La revisión/fusión sigue siendo decisión exclusiva del autor.

**Conclusión:** D01–D03 superaron su suite estática Python en el MSI sobre el checkout real. D03 puede darse por validada documentalmente en este ámbito, pendiente únicamente de la decisión autoral de fusionar la PR #17. Las pruebas de motor/GIS permanecen asignadas a etapas posteriores.
