# Aldeas del territorio Valrik

## Propósito

Esta carpeta organiza el lore jugable de las aldeas Valrik desde lo más general hasta los asentamientos concretos del mundo.

La regla es separar claramente:

1. **qué comparten las aldeas Valrik**;
2. **qué modelos reutilizables existen**;
3. **qué aldeas concretas existen realmente en el mapa**.

Esto evita mezclar lore regional, layouts reutilizables, prompts visuales y assets finales.

---

## Estructura

### 00_Base

Contiene la definición genérica de una aldea Valrik.

Aquí se guardan únicamente rasgos comunes y reutilizables: escala rural, relación entre viviendas y oficios, interdependencia entre aldeas, lógica productiva y criterios generales de diseño jugable.

Archivo principal:

- `00_Base/aldea_tipo_valrik.md`

### 01_Modelos

Contiene **modelos reutilizables de distribución y función**.

Los identificadores `V1`, `V2`, `V3`... significan **variantes de modelo**, no revisiones del mismo archivo.

Ejemplos actuales:

- `V1_Mixta_maderera_agricola`
- `V2_Molino_agroganadera`

Cada modelo podrá tener más adelante:

- descripción funcional;
- lógica espacial;
- plano tipo;
- reglas de variación;
- datos operativos para generación procedural o semiprocedural.

### 02_Instancias

Contendrá las **aldeas canónicas concretas y con nombre** que existan en el mundo.

Una instancia podrá basarse en un modelo y modificar detalles locales sin duplicar toda la definición.

Ejemplo futuro:

```text
02_Instancias/
└── Nombre_de_aldea/
    ├── aldea.md
    ├── npc.md
    └── gameplay.md
```

---

## Relación con la v0.0.1

La v0.0.1 utilizará inicialmente:

- **Modelo V1** como aldea principal;
- **Modelo V2** como posible segunda aldea.

La versión del juego no debe formar parte de la identidad permanente del modelo. Así, V1 y V2 podrán reutilizarse posteriormente en otras zonas del territorio Valrik.

---

## Separación de responsabilidades

### Lore y lógica jugable

Se guardan aquí, dentro de `Territorios/Casa Valrik/Aldeas/`.

### Biblia visual

Se guarda en:

`Worldbuilding/Direccion artistica/Biblia visual/Culturas/Norgard/Perfiles locales/Treskal/Aldeas/`

### Prompts maestros

Se guardan en:

`Worldbuilding/Direccion artistica/Prompts maestros/Asentamientos/Norgard/Treskal/Aldeas/`

### Referencias visuales aprobadas

Se guardan en:

`Worldbuilding/Direccion artistica/Biblia visual/Culturas/Norgard/Referencias visuales/Treskal/Aldeas/`

### Assets finales

Los assets generados se almacenan bajo `Worldbuilding/Direccion artistica/Assets/` siguiendo la convención oficial de nombres y empaquetado del repositorio.

---

## Regla principal

**Lore define qué existe y cómo funciona.  
La Biblia visual define cómo debe verse.  
El prompt traduce esas reglas a generación visual.  
La referencia aprobada fija una apariencia.  
El asset es el producto final utilizable.**
