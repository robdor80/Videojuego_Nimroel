# Darovan 4 — Traspaso a D03 (Clima y ecosistemas)

**D03 NO INICIADA.** D02 documental, PR propia pendiente de revisión/merge autorizado; D01 integrada por PR #15 (merge 9f3f723b0e7b2b78567c6397bba7099bfe658b0a). No confundir canon, documentación, validación estática y runtime.

## Puerta de entrada obligatoria
1. Verificar en GitHub **merged=true** de la PR D02 y HEAD `main` actualizado; si no está fusionada **no abrir D03 desde main**.
2. Leer `00_Control_del_proyecto/{REGISTRO_FASES,DECISIONES_Y_BLOQUEOS,PROTOCOLO_RAMAS_COMMITS_PR}.md`, acta D02, los tres archivos de `Hidrografia/`, el JSON D02, los perfiles D01 y `Cartografia/01_dependencias_cartograficas_D01_v0.1.md`.
3. Volver a fuentes ORIGINALES Norgard (Clima/clima_general.md, Geografía/geografia_general.md, regiones_naturales.md, montanas.md, bosques.md, rios_y_lagos.md, mares_y_costas.md) y Nimroel Core (documento físico y contrato JSON).
4. Crear rama separada para D03 desde `main` y PR propia sin fusión automática. No iniciar D03 en Darovan 3.

## Propósito de D03
Caracterizar cualitativamente gradientes climáticos y ecológicos (oeste oceánico, norte frío, Valkram/Elyra, Agujas/Linde/Pilares, transición seca norte/centro y más húmeda al sur de península Taramin, isla Syvaris cálida pero diversa). Relacionar lluvias/deshielo/infiltración/recarga y posibles riesgos, sin atribuir números ni emplazamientos nuevos. El clima modula agua disponible y estacionalidad; **la posición espacial del cauce requiere relieve**.

## Invariantes del traspaso
- Belara nace al oeste/norte Valkram, pasa junto a Treihord sin atravesarla, Golfo Norgard, barcazas industriales someras.
- Lhera procede de Belara, junto al Bosque Agujas, Golfo Veldora; Veldora es **río independiente** que también termina en Golfo Veldora.
- Thalen, un río con dos brazos terminales, Taramin entre ambos, Golfo Norgard.
- 4 ciudades manuales, Karsath fuera; Syvaris Darovan; Arven UNKNOWN, ningún poblado permanente dentro de Agujas.
- Grafo D02 13 nodos/10 aristas no cartográficos; no fijar cabeceras Veldora/Thalen, divisorias, pendientes, rutas, puentes o caudales; no fijar régimen perenne de los ríos nombrados por simple presencia.
- Core: preservar identidades/geometría materializada, estados de agua cambiantes por WorldState y UNKNOWN cuando faltan datos.

## Deudas y validación
DAR-P01 Arven, DAR-P04 escala/cotas/fronteras, DAR-P07 río visual Veldora, DAR-P08 orden separación Lhera frente a Treihord y trazados/afluentes/regímenes desconocidos. D03 puede desarrollarse cualitativamente sin resolverlas por ficción.
Desde un checkout completo, repetir `python "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan/Validacion/validate_d02.py"`: **aún no se ha ejecutado**. D05/D07 deberán precisar cruces y ciudades cuando exista mapa; D11 integrará y probará runtime.

**No elevar hipótesis D03 a canon sin el autor; no modificar fuentes originales ni comenzar fase en esta conversación.**
