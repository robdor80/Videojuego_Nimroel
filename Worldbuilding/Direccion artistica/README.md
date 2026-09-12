# Direccion artistica de Nimroel

Esta carpeta contiene la documentacion artistica canonica del proyecto.

## Estructura

- Biblia visual\General
  Reglas visuales globales que afectan a todas las imagenes.

- Biblia visual\Categorias
  Reglas especificas por tipo de asset. Nunca pueden contradecir la Biblia General.

- Biblia visual\Culturas
  Perfiles visuales culturales y de reino. Deben respetar la Biblia General y las Biblias de categoria.

- Prompts maestros
  Plantillas versionadas para generar imagenes de forma coherente.

- Referencias
  Imagenes de prueba, ejemplos aprobados, comparativas y material de apoyo visual.

## Regla de herencia

Biblia General
> Categoria
> Cultura/Reino
> Perfil especifico
> Prompt final
> Asset

Cada nivel puede especializar el anterior, pero nunca contradecirlo.
