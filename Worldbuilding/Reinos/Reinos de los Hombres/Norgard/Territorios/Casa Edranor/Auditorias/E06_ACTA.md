# E06 — Acta de entrega técnica
**12/11/2026 · Rama E06 · estado documental y laboratorio NO RUNTIME.**

Se construyen ocho modelos, matriz de siete sectores E01, clase funcional de aldea/pueblo/villa/enclave, esqueleto de ocho verificaciones, cinco anclas intocables, bloqueos geográficos, contrato JSON, quince fixtures y función pura de identidad/elección. Ninguna entidad nueva se publica como canon; ninguna geografía, parcela, camino, servicio, NPC ni población se materializa.

La CI de fase ejecuta regresiones E00–E05 y `Tools/EdranorE06/validate.py` en Ubuntu 24.04 y Windows 2022. **Las cifras exactas de pruebas y la fusión solo deben consignarse tras comprobar GitHub Actions**; la existencia de este acta no certifica CI.

E07 tratará manualmente Dorth, Lumina, Karsath y Rodas. No decide todavía si Rodas debe denominarse editorialmente aldea o ciudad, ni modifica fiscalidad/mando de la Corona. E08 y E11 necesitan contratos de hogares e integración/persistencia; las reglas de laboratorio E06 no son API runtime validada.

Condiciones de cierre/fusión: CI del commit HEAD exacto verde en dos OS, sin cambio de `main` desde base o conflicto, diff exclusivamente E06 + herramientas + workflow, cero modificación de canones existentes, autorización del autor.
