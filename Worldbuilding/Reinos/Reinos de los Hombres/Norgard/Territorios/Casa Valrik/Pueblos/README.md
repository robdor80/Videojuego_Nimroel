# Pueblos del territorio de Treskal

## Propósito

Esta carpeta organiza el lore jugable de los pueblos del territorio de Treskal.

Todos los pueblos deben seguir la metodología territorial común definida en:

`../metodologia_generacion_asentamientos_treskal.md`

Secuencia obligatoria:

**esqueleto mínimo → posibilidades → coherencia regional → probabilidades → generación → persistencia**.

## Estado actual

**FASE ACTIVA DE DISEÑO**

El diseño base de Aldeas está cerrado. Para Pueblos ya están definidos el esqueleto, posibilidades, coherencia regional, primera matriz de probabilidades, modelos iniciales y reglas espaciales base.

Treskal ciudad queda fuera del sistema procedural y se desarrollará manualmente.

## Estructura

### 00_Base

- `pueblo_tipo_treskal.md` — esqueleto mínimo obligatorio.
- `posibilidades_pueblo_treskal.md` — servicios, oficios y variantes posibles.

### 01_Coherencia_regional

- `relacion_pueblos_aldeas.md` — áreas de servicio por accesibilidad real.
- `distribucion_servicios_y_autosuficiencia.md` — cobertura cotidiana y distribución de servicios.
- `comercio_cotidiano_y_mercado.md` — comercio ordinario y mercado periódico.

### 02_Probabilidades

- `probabilidades_servicios_pueblo_treskal.md` — bandas de población, probabilidades base, modificadores, cobertura y reequilibrio.

### 03_Modelos

- `V1_Agroganadero_mercado/modelo_v1.md`
- `V2_Maderero_logistico/modelo_v2.md`
- `V3_Fluvial_pesquero/modelo_v3.md`

Los modelos modifican pesos y condiciones, pero no fijan una instancia ni un plano único.

### 04_Generacion

- `reglas_espaciales_pueblo_treskal.md` — densidad, crecimiento orgánico, red viaria, ubicación funcional y persistencia espacial.

## Siguiente fase

- reglas de composición de población y hogares;
- cantidades orientativas de edificios y anexos derivadas de esa población;
- capa operativa estructurada para el motor;
- generación y persistencia de instancias.
