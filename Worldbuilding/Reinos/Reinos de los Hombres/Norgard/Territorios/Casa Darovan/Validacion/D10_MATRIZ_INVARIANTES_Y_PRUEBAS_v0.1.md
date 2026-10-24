# D10 — Matriz de pruebas estáticas y mutaciones negativas

**Fecha:** 23/10/2026. **Objeto:** 17 decisiones autorales, canon superior, seis perfiles culturales y 16 casos ficticios TEST_ONLY. **No runtime.**

| Ámbito | Verificación positiva | Mutación negativa |
|---|---|---|
| Opciones autor | 16×B y D10-09C, sin materializar | cambiar cualquiera de las 17 opciones |
| Jerarquía | Core→Norgard→Darovan→Localidad→World State | invertir precedencia |
| Fuentes | 34 ficheros existentes, únicos y trazables | ruta inexistente o duplicada |
| Ciudades | Treihord, Veldora, Taramin, Syvaris | quinta ciudad |
| Treihord | ocho barrios, Belara externo | barrio noveno o río atravesando |
| Veldora | comercio externo, aduana Corona | inventar contacto individual |
| Taramin | dos brazos del único Thalen | presuponer navegación/puente |
| Syvaris | Armada de la Corona | armada particular |
| Arven | pertenece a Darovan, cultura UNKNOWN | inventar identidad insular |
| Rural | D06 condicional, sin nueva aldea | instancia automática |
| Feria | existe feria de metales, sin nombre/fecha | asignar denominación nueva |
| Funerales | cremación/retorno/tres días | días alterados, rito obligatorio |
| Material | tecnologías Norgard sin relojes | inventar reloj/stock |
| Familia | vínculos separados, derechos de Norgard | parentesco/ayuda obligatoria |
| Persona | PERS no se deduce de oficio o residencia | estereotipo automático |
| Escenarios | 16 casos TEST_ONLY, sin NPC/eventos | promover escenario a canon |
| Regresión | fuentes D07, D08, D09 coherentes | alterar demografía/justicia/Armada |

**Ejecutar:** `python "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan/Validacion/validate_d10.py"`. En GitHub Actions, la matriz Windows 2022 / Ubuntu 24.04 ejecuta además D01–D09 en la misma revisión.

Las mutaciones se producen exclusivamente en memoria de prueba; no modifican ficheros ni World State. No se infiere resultado de ejecución antes de consultar el workflow del commit final.
