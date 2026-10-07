# Nimroel Core — alimentos, cocina, conservación y comidas v0.1

## Autoridad

**CORE UNIVERSAL — namespace FOOD**

Este sistema define cómo existen, se transforman, conservan, deterioran y consumen los alimentos.

No define:

- cocina propia de un Reino;
- ingredientes culturales concretos;
- recetas regionales;
- especies vegetales o animales;
- etiqueta de mesa;
- horarios de comida.

Esas capas pertenecen a defaults culturales y World State.

---

## 1. Principio

Una receta no crea comida.

Toda preparación necesita:

- ingredientes reales;
- cantidad suficiente;
- recipiente/herramienta compatible;
- combustible cuando proceda;
- tiempo;
- conocimiento o habilidad suficiente;
- espacio de trabajo compatible.

El resultado entra en stock real y puede consumirse, venderse, conservarse, transportarse o perderse.

---

## 2. Estados FOOD

- FOOD01 — raw_or_unprepared;
- FOOD02 — prepared_ready;
- FOOD03 — preserved;
- FOOD04 — aging_or_declining;
- FOOD05 — spoiled_or_unsafe;
- FOOD06 — discarded_or_waste.

El estado no sustituye origen, calidad, cantidad ni método de conservación.

---

## 3. Lote alimentario

Un lote puede registrar:

- food_lot_id;
- ingredient_or_product_ref;
- origin_ref;
- producer_or_supplier_ref;
- owner_ref;
- location_ref;
- aggregate_quantity;
- FOOD_state;
- preparation_method_if_any;
- preservation_method_if_any;
- prepared_at_if_any;
- preserved_at_if_any;
- storage_context;
- quality_band;
- contamination_refs_if_any;
- intended_use_if_any;
- reservation_or_contract_ref_if_any;
- last_update_time.

No es obligatorio rastrear cada pan individual cuando el LOD permita agregación.

---

## 4. Preparación

Métodos universales que una cultura puede conocer:

- raw_service_when_safe_and_canonical;
- boiling;
- simmering;
- stewing;
- roasting;
- grilling;
- frying;
- baking;
- toasting;
- mashing;
- grinding;
- mixing;
- thickening;
- stuffing;
- simple_sauce_or_gravy;
- broth_or_stock;
- brewing_or_fermenting_when_cultural.

La existencia mecánica de un método no obliga a todas las culturas a usarlo.

---

## 5. Conservación

Métodos posibles:

- drying;
- salting;
- brining;
- smoking;
- fermentation;
- pickling;
- cool_storage;
- cellar_storage;
- fat_or_grease_sealing_when_culturally_supported.

Cada método necesita:

- material;
- tiempo;
- instalación o recipiente cuando proceda;
- conocimiento;
- condiciones compatibles.

Conservar no vuelve eterno un alimento.

---

## 6. Deterioro

El deterioro puede depender de:

- tipo de alimento;
- preparación;
- conservación;
- temperatura;
- humedad;
- exposición;
- recipiente;
- almacenamiento;
- daño físico;
- tiempo.

No existe fecha universal de caducidad para todos los lotes.

---

## 7. Seguridad alimentaria

Un alimento:

- puede parecer aceptable y estar contaminado;
- puede oler mal sin ser la única causa de riesgo;
- puede deteriorarse de forma visible;
- puede contaminarse por agua, residuos, manipulación o almacenamiento.

Consumir un alimento inseguro puede generar HCOND cuando exista causa plausible.

No toda comida vieja enferma automáticamente.

Cocinar puede reducir algunos riesgos, pero no reinicia mágicamente un lote deteriorado.

---

## 8. Receta

Una receta canónica define:

- recipe_id;
- culture_or_region_scope;
- required_categories;
- optional_categories;
- permitted_substitutions;
- preparation_methods;
- required_tools_or_installation;
- fuel_required;
- approximate_effort;
- preservation_result_if_any;
- serving_contexts;
- output_food_tags.

La receta no fija automáticamente:

- precio;
- disponibilidad;
- calidad;
- cantidad.

---

## 9. Sustitución

Una sustitución solo es válida si:

- el producto existe;
- es culturalmente plausible;
- cumple función culinaria compatible;
- la receta la permite o el cocinero improvisa con habilidad suficiente.

Escasez no crea sustitutos gratuitos.

---

## 10. Comidas

Una comida puede resolverse:

- detalladamente;
- como consumo agregado del hogar;
- como servicio de negocio;
- como ración institucional;
- como provisión de viaje.

Contextos posibles:

- domestic;
- workday;
- travel;
- camp;
- tavern_or_inn;
- market_or_street;
- military;
- maritime;
- hospitality;
- ceremonial_or_feast;
- scarcity_or_emergency.

No existe obligación universal de tres comidas diarias.

---

## 11. Necesidad física

NEED01 se satisface mediante consumo real.

El motor puede agregar comidas rutinarias cuando:

- hay stock;
- existe acceso;
- la rutina es estable;
- no hay escasez relevante.

Debe bajar a detalle cuando:

- falta comida;
- hay viaje;
- enfermedad;
- conflicto;
- precio/stock es relevante;
- existe una escena o decisión de gameplay.

---

## 12. Cocina doméstica y profesional

La cocina puede ocurrir en:

- hogar;
- taberna;
- posada;
- panadería;
- cocina institucional;
- campamento;
- barco;
- otro lugar compatible.

La capacidad depende de:

- fuego/calor;
- utensilios;
- espacio;
- trabajadores;
- stock;
- agua;
- tiempo.

---

## 13. Restos y reaprovechamiento

Preparar y consumir comida puede generar:

- huesos;
- cáscaras;
- recortes;
- grasa;
- ceniza;
- agua sucia;
- alimento sobrante.

Parte puede reaprovecharse cuando exista uso válido.

Lo demás entra en WASTE.

---

## 14. Comercio y propiedad

FOOD no altera:

- OWN;
- TXN;
- OBL;
- LED.

Una comida vendida requiere transacción o causa válida.

Un ingrediente reservado para una institución no queda disponible para otro negocio solo porque exista en la ciudad.

---

## 15. Estación y clima

La estación y el clima pueden alterar:

- producción;
- llegada;
- frescura;
- velocidad de deterioro;
- precio;
- disponibilidad;
- necesidad de conservación.

La cocina regional debe reaccionar a lo que existe realmente.

---

## 16. Viaje y expedición

La comida de viaje favorece productos:

- transportables;
- estables;
- fraccionables;
- que requieran poca preparación.

Pero el contenido exacto lo define cada cultura.

Viajar no genera raciones automáticas.

---

## 17. Instituciones

Ejército, Armada, Casas, talleres o cuadrillas pueden comprar/producir raciones.

La ración:

- consume stock;
- ocupa transporte;
- puede deteriorarse;
- puede escasear.

---

## 18. IA

La IA puede:

- describir una preparación existente;
- elegir entre opciones disponibles y autorizadas;
- expresar preferencias;
- proponer una sustitución plausible.

No puede:

- inventar un ingrediente;
- materializar una comida;
- ignorar falta de combustible;
- ignorar deterioro;
- crear una receta cultural como canon;
- declarar seguro un alimento que el motor marcó como inseguro.

---

## 19. LOD

En LOD bajo pueden agregarse:

- consumo;
- cocción rutinaria;
- deterioro;
- reposición;
- conservación.

Debe conservarse:

- stock;
- pérdidas;
- escasez;
- lotes relevantes;
- reservas;
- contaminación relevante.

---

## Regla final

**En Nimroel la comida existe porque alguien la produjo, la conservó, la transportó y la cocinó; ninguna receta sustituye esa cadena material.**
