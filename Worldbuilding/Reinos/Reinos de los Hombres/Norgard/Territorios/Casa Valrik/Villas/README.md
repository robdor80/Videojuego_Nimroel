# Villas del territorio de Treskal

## Propósito

Esta carpeta organiza el lore jugable de las Villas del territorio de Treskal.

Todas deben seguir la metodología territorial común definida en:

`../metodologia_generacion_asentamientos_treskal.md`

Secuencia obligatoria:

**esqueleto mínimo → posibilidades → perfil funcional → coherencia regional → probabilidades → generación → persistencia**.

## Estado actual

**DISEÑO BASE AVANZADO / CAPA OPERATIVA ACTIVA**

Ya están definidos:

- esqueleto mínimo;
- capacidades comunes;
- tres perfiles funcionales canónicos;
- relación regional con Pueblos, Aldeas y Treskal;
- probabilidades de servicios secundarios;
- reglas espaciales;
- población residente y flotante;
- contratos operativos de generación y persistencia.

Treskal ciudad no se genera proceduralmente: se diseñará manualmente.

## Particularidad del territorio

En el canon existen tres Villas de especial relevancia cuya función principal ya está fijada:

1. Villa costera de los grandes astilleros civiles.
2. Villa de gestión forestal y maderera.
3. Villa agroganadera y comercial del interior.

No son modelos intercambiables elegidos al azar.

La generación decide cómo se materializa cada una, pero no puede cambiar su función principal.

Los nombres, localizaciones exactas y Casas menores permanecen pendientes.

## Estructura

### 00_Base

- `villa_tipo_treskal.md`
- `posibilidades_villa_treskal.md`

### 01_Perfiles_funcionales

- `V1_Costera_astilleros_civiles/perfil_v1.md`
- `V2_Gestion_forestal_maderera/perfil_v2.md`
- `V3_Agroganadera_comercial/perfil_v3.md`

### 02_Coherencia_regional

- `red_villas_pueblos_treskal.md`

### 03_Probabilidades

- `probabilidades_servicios_secundarios_villa_treskal.md`

### 04_Generacion

- `reglas_espaciales_villa_treskal.md`
- `poblacion_hogares_y_edificios_villa_treskal.md`

### Datos operativos

- `villa_generation_rules_v0.1.json`
- `villa_instance_contract_v0.1.json`
- `README.md`

## Límites ya fijados

- la Villa costera construye grandes embarcaciones civiles, no buques de guerra;
- los Astilleros Reales continúan en Treskal y pertenecen a la Corona;
- los grandes astilleros civiles pertenecen a la Casa Valrik;
- la Casa menor administra la Villa, pero no adquiere automáticamente esos astilleros;
- la Villa forestal organiza y expide madera, sin sustituir a Treskal como gran centro de transformación especializada;
- la Villa agroganadera mantiene mercado diario;
- ninguna Villa se convierte en una ciudad equivalente a Treskal.

## Siguiente fase

Antes del cierre formal faltan únicamente:

1. validar coherencia entre documentos humanos y JSON;
2. limpiar estados documentales obsoletos;
3. fijar invariantes de generación de las tres Villas;
4. cerrar el diseño base sin asignar todavía nombres, Casas menores o localizaciones exactas.
