# D06 — Matriz de aceptación estática v0.1

**Contrato bajo prueba:** `darovan_d06_settlement_rules_v0.1.json`, fixtures sintéticos, `d06_generator.py`, `validate_d06.py`.

| Grupo | Invariante | Comprobación |
|---|---|---|
| Autoridad | cadena Core → Defaults → Darovan → Localidad → World State | igualdad exacta |
| Fases | D01–D04: 12 unidades de estudio cualitativas idénticas | comparación de conjuntos |
| Hidrología | D02: cinco ríos, cuatro sistemas, 15 nodos y 11 enlaces simbólicos | referencias cruzadas |
| Movilidad | D05: tres vínculos modales, cuatro relaciones de suministro no rutas | referencias cruzadas |
| Economía | D04: ocho cadenas; no promulgar emplazamientos mineros | comparación origen y estado |
| Ciudad | cuatro ciudades manuales; Karsath excluida | invariantes |
| Arven | soberanía Darovan aprobada; no ruta nueva automática | JSON D01/D03/D04/D05/D06 |
| Agujas | interior sin asentamiento permanente; bloqueo conservador unidad sin geometría | pesos cero y rechazo fixture |
| Agua | potable, habitabilidad, acceso, sustento y derecho local obligatorios | pruebas negativas |
| Especialización | pesca necesita desembarco; mina necesita sitio y titular; bosque regeneración; camino demanda y lugar | modelos + negativos |
| Bosques | no tala industrial Taramin/Syvaris/Arven; Linde sin industria presumida | bloqueos y pesos |
| Semillas | mismo seed+slot mismos datos; distinto seed cambia ID | fixtures |
| Redes | ninguna relación de suministro crea camino; Fhalion/Thalen sin navegabilidad acreditada | semántica y flags |
| Población | sin nuevas cifras/hogares, no stock/empleo/propiedad | campos nulos |
| Integración | no CoreRPG, Godot, GIS ni persistencia afirmados | estado explícito |

## Pruebas positivas

Seis escenarios de laboratorio con base probatoria **supuestamente verificada solo en fixture**; repetición determinista; IDs únicos; derivación estable; salida sin coordenadas ni estado materializado; elección por pesos insensible al orden.

## Pruebas negativas

**20 mutaciones de reglas:** pérdida de ciudad protegida, Arven sin dueño, Fhalion borrado, quinto sistema falso, permitir Agujas, autoselección espacial, peso fuera de escala, ID de modelo inválido, clase ciudad, edificio automático, quitar requisitos de modelo, suministro como carretera, navegación automática, aduana interna, tala industrial Taramin/Syvaris, runtime fingido, referencia inexistente, duplicar unidad D01 y mina Elyra afirmada por inferencia.

**20 mutaciones de sitio:** falta de agua, acceso, competencia, sostenibilidad, sustento o derechos; prueba de interior Agujas; ciudad, identidad urbana, localidad canónica, topónimo oficial, ruta nueva, puerto nuevo, aduana interna, buque profundo Belara, coordenadas fabricadas, fuente no sintética, evidencia duplicada, zona inexistente o modelo ilegítimo.

Toda mutación debe fallar y dejar de servir como fixture. CI ejecuta D01, D02, D03, D04, D05 y D06 en Ubuntu y Windows con checkout completo del repositorio.

### Límite de aceptación

`STATIC OK` solo valida estructura y compatibilidad documental. No verifica comunidad real, pesos demográficos, mapa métrico, Godot, CoreRPG runtime, persistencia o uso real de semilla de partida.
