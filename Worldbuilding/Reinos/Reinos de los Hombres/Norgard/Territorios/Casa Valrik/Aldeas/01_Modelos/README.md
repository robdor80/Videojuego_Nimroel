# Modelos de aldeas Valrik

## Propósito

Esta carpeta contiene **perfiles de generación reutilizables** derivados de la aldea tipo Valrik.

Cada modelo define un espacio de posibilidades, no una aldea terminada.

---

## Convención

`V1`, `V2`, `V3`... son **identificadores de modelo**.

No significan versión documental.

Las revisiones internas de un documento, si fueran necesarias, usarán nomenclatura como `v0.1`, `v0.2`, etc.

---

## Qué debe definir un modelo

Cada modelo podrá fijar:

- tipo de entorno;
- relación con carreteras, bosque, río o costa;
- rango de población;
- actividades económicas dominantes;
- servicios obligatorios solo cuando exista una razón funcional;
- servicios opcionales;
- servicios incompatibles;
- probabilidades o pesos relativos;
- límites de cantidad;
- reglas de colocación;
- dependencias con aldeas cercanas.

Debe evitar fijar:

- una distribución única;
- un número exacto de casas;
- un edificio concreto de una o dos plantas;
- una familia concreta;
- un NPC concreto;
- un interior exacto;
- un plano que todas las aldeas deban repetir.

---

## Modelos iniciales

### V1 — Mixta maderera y agrícola

Perfil de aldea interior pequeña vinculada a una ruta de transporte de madera, pero con agricultura y ganadería local.

La actividad maderera aumenta la probabilidad de determinados talleres y servicios ligados al tránsito, sin obligar a que todas las aldeas V1 tengan exactamente los mismos.

### V2 — Agroganadera con servicio de molienda posible

Perfil de aldea interior pequeña con mayor peso agroganadero y alta probabilidad de cubrir necesidades de molienda de la red rural próxima.

El modelo permite que determinadas aldeas del entorno compensen servicios ausentes en otras.

---

## Generación y persistencia

El generador elegirá una configuración concreta respetando el modelo.

Una vez generada, esa configuración debe persistir en la partida.

Las aldeas ordinarias no necesitan archivarse como canon en `02_Instancias/`.

---

## Evolución futura

Cada modelo podrá incorporar cuando sea necesario:

- `modelo.md` — reglas funcionales;
- `layout_rules.md` — restricciones espaciales y rangos, no plano único;
- `Datos operativos/` — representación estructurada para el motor.

No se crearán datos técnicos definitivos antes de cerrar la lógica de generación.
