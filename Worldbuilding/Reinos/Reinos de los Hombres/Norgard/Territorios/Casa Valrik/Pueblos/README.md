# Pueblos del territorio de Treskal

## Propósito

Esta carpeta organiza el lore jugable de los pueblos del territorio de Treskal.

Todos los pueblos deben seguir la metodología territorial común definida en:

`../metodologia_generacion_asentamientos_treskal.md`

Secuencia obligatoria:

**esqueleto mínimo → posibilidades → coherencia regional → probabilidades → generación → persistencia**.

## Estado actual

**DISEÑO BASE AVANZADO / CAPA OPERATIVA ACTIVA**

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

## Próximos pasos

El siguiente trabajo útil ya no consiste en añadir oficios por completitud, sino en:

1. validar automáticamente la coherencia entre documentos humanos y JSON;
2. preparar un prototipo de generador con semillas deterministas cuando exista el módulo de código correspondiente;
3. utilizar las pruebas de invariantes antes de generar instancias canónicas;
4. trasladar después la metodología a Villas cuando el desarrollo del juego lo necesite.
