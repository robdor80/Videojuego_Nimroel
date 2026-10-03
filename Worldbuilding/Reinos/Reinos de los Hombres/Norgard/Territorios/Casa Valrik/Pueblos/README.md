# Pueblos del territorio de Treskal

## Propósito

Esta carpeta organiza el lore jugable de los pueblos del territorio de Treskal.

Todos los pueblos deben seguir la metodología territorial común definida en:

`../metodologia_generacion_asentamientos_treskal.md`

Secuencia obligatoria:

**esqueleto mínimo → posibilidades → coherencia regional → probabilidades → generación → persistencia**.

## Estado actual

**DISEÑO BASE DE PUEBLOS CERRADO — CAPA OPERATIVA v0.1**

Para Pueblos ya están definidos:

- esqueleto mínimo;
- posibilidades;
- coherencia regional;
- probabilidades contextuales;
- tres modelos iniciales;
- reglas espaciales;
- hogares y derivación de edificios;
- coordinación regional;
- aleatoriedad determinista;
- contrato operativo de generación y persistencia;
- invariantes de prueba para la implementación futura.

Treskal ciudad queda fuera del sistema procedural y se desarrollará manualmente.

## Estructura

### 00_Base

- `pueblo_tipo_treskal.md`
- `posibilidades_pueblo_treskal.md`

### 01_Coherencia_regional

- `relacion_pueblos_aldeas.md`
- `distribucion_servicios_y_autosuficiencia.md`
- `comercio_cotidiano_y_mercado.md`

### 02_Probabilidades

- `probabilidades_servicios_pueblo_treskal.md`

### 03_Modelos

- `V1_Agroganadero_mercado/modelo_v1.md`
- `V2_Maderero_logistico/modelo_v2.md`
- `V3_Fluvial_pesquero/modelo_v3.md`

### 04_Generacion

- `reglas_espaciales_pueblo_treskal.md`
- `poblacion_hogares_y_edificios_pueblo_treskal.md`

### 05_Coordinacion_regional

- `generacion_regional_determinista.md` — grafo de accesibilidad, cobertura, coordinación de mercados, semillas estables y persistencia.

### Datos operativos

- `pueblo_generation_rules_v0.1.json`
- `pueblo_instance_contract_v0.1.json`
- `regional_generation_rules_v0.1.json`
- `generation_invariants_v0.1.json`
- `README.md`

## Regla de implementación

**Lore → reglas.  
Generador → instancia.  
World State → persistencia.**

NPC individuales, inventarios dinámicos y estado de misiones se mantienen fuera del contrato estático del Pueblo.

## Cierre de diseño base

La base jugable y procedural de los **Pueblos del territorio de Treskal se considera CERRADA**.

Quedan cubiertos:

- escala y esqueleto mínimo;
- servicios obligatorios y opcionales;
- autosuficiencia cotidiana;
- relación funcional con Aldeas;
- comercio y mercado periódico;
- probabilidades y modificadores contextuales;
- modelos económicos iniciales;
- hogares, viviendas y edificios;
- crecimiento espacial orgánico;
- cobertura regional;
- aleatoriedad determinista;
- persistencia;
- contratos operativos;
- invariantes de prueba.

Los asuntos deliberadamente pospuestos —como metalurgia especializada de mayor escala, porcentajes demográficos generales de todo Valrik o instancias concretas con nombre— **no mantienen abierta esta fase**.

Solo se reabrirá el diseño de Pueblos cuando exista una necesidad concreta de gameplay, implementación, narrativa, arte o datos.

## Siguiente nivel de diseño

El siguiente nivel procedural del territorio es **Villa**.

La implementación futura del generador de Pueblos deberá consumir los contratos de `Datos operativos/` y superar los invariantes definidos antes de generar instancias persistentes.
