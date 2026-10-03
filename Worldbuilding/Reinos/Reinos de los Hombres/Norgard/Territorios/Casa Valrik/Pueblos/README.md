# Pueblos del territorio de Treskal

## Propósito

Esta carpeta organiza el lore jugable de los pueblos del territorio de Treskal.

Todos los pueblos deben seguir la metodología territorial común definida en:

`../metodologia_generacion_asentamientos_treskal.md`

Secuencia obligatoria:

**esqueleto mínimo → posibilidades → coherencia regional → probabilidades → generación → persistencia**.

## Estado actual

**FASE ACTIVA DE DISEÑO / CAPA OPERATIVA INICIADA**

El diseño base de Aldeas está cerrado.

Para Pueblos ya están definidos:

- esqueleto mínimo;
- posibilidades;
- coherencia regional;
- probabilidades contextuales;
- tres modelos iniciales;
- reglas espaciales;
- hogares y derivación de edificios;
- contrato operativo de generación y persistencia.

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
- `poblacion_hogares_y_edificios_pueblo_treskal.md` — unidades domésticas, ocupación residencial y derivación de viviendas, edificios y anexos.

### Datos operativos

- `pueblo_generation_rules_v0.1.json` — representación estructurada de las reglas estáticas de generación.
- `pueblo_instance_contract_v0.1.json` — contrato mínimo de una instancia persistida en World State.
- `README.md` — separación de responsabilidades y uso de la capa operativa.

## Regla de implementación

El canon no debe almacenar el resultado concreto de cada Pueblo procedural.

**Lore → reglas.  
Generador → instancia.  
World State → persistencia.**

NPC individuales, inventarios dinámicos y estado de misiones se mantienen fuera del contrato estático del Pueblo.

## Siguiente fase

- validar la capa operativa contra todos los documentos humanos;
- definir generación regional coordinada de varios Pueblos y sus aldeas dependientes;
- preparar pruebas deterministas con semillas;
- después trasladar la misma metodología a Villas cuando sea necesario.
