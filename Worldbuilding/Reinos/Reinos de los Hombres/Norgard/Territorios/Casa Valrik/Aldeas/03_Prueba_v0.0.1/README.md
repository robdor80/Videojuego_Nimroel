# Nimroel RPG — preparación de la prueba v0.0.1 «La primera aldea»

**Estado:** LORE DE LA PRUEBA CERRADO; implementación y validación pendientes.
**Autoridad:** alcance de prueba aprobado; no sustituye el canon general de Norgard ni los contratos existentes.
**Lugar:** una aldea ordinaria procedural del territorio de Treskal, Casa Valrik.
**Modelo:** V1 — mixta maderera y agrícola.
**Situación jugable:** exploración libre; encargo descubrible y opcional «La herramienta rota».
**Plataforma de primer ensayo:** Host Nimroel 2D para Windows; Android se valida por separado.
**No forma parte todavía del Content Pack JSON de CoreRPG.**

## Documentos de este paquete

- [ALCANCE_LORE_V001_v0.1.md](ALCANCE_LORE_V001_v0.1.md): cierre narrativo, canon heredado, límites de generación y responsabilidades.
- [ENCARGO_HERRAMIENTA_ROTA_v0.1.md](ENCARGO_HERRAMIENTA_ROTA_v0.1.md): situación, estados, descubrimiento libre y consecuencias.
- [MATRIZ_ACEPTACION_V001_v0.1.md](MATRIZ_ACEPTACION_V001_v0.1.md): pruebas verificables y criterios de salida.
- [contrato_prueba_v001_v0.1.json](contrato_prueba_v001_v0.1.json): especificación operativa de traspaso, **no** un manifiesto ni definición del Content Contract CoreRPG 0.1.0.

## Autoridades heredadas

1. `../00_Base/aldea_tipo_treskal.md`: esqueleto de aldea; 35–100 habitantes.
2. `../00_Base/posibilidades_aldea_treskal.md`: servicios opcionales.
3. `../01_Modelos/V1_Mixta_maderera_agricola/modelo_v1.md`: perfil V1 y referencia inicial de 40–60 habitantes.
4. `../../metodologia_generacion_asentamientos_treskal.md`: secuencia obligatorio/posible/probable, generación y persistencia.
5. `../../Pueblos/05_Coordinacion_regional/generacion_regional_determinista.md`: semilla mundial, grafo regional, IDs estables y corrección mínima.
6. `Worldbuilding/Sistemas/Nimroel Core/Datos operativos/`: contratos de propiedad, herramientas, reparación, tiempo, memoria y espera (rutas desde raíz del repositorio).
7. CoreRPG: diseño genérico de identidades, población y persistencia; acciones, conocimiento, simulación, contexto y Content Pack serán integraciones posteriores según fase.

## Separación de estados

- **Aprobado por el autor:** concepto de prueba, modelo V1, viajero sin biografía impuesta, exploración libre, encargo voluntario, resolución o abandono y guardado persistente.
- **Diseñado aquí para pruebas:** situación genérica, hitos de aceptación y datos requeridos. Esto no proclama que ya existan en C++.
- **Pendiente técnico:** pesos de generación, algoritmo de layout, esquema de payload Nimroel, Host 2D, Content Pack real, acciones simuladas, calendarios de trabajo concretos, ajuste de rendimiento y pruebas.
- **Sin decisiones de canon pendientes para comenzar:** no se necesitan aldea, hogares, familias ni NPC con identidad fija; el generador los decidirá.

## Criterio rector

La misión prueba los sistemas del mundo, no crea una aldea artificial para una misión. El jugador puede entrar y salir sin aceptar encargos; la generación no debe revelar previamente los resultados concretos.
