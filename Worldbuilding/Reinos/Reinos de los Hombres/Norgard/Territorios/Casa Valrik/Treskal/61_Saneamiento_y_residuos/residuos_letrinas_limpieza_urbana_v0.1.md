# Treskal — residuos, letrinas y limpieza urbana v0.1

## Estado

**DISEÑO URBANO/JUGABLE APROBADO — SANEAMIENTO PREINDUSTRIAL FUNCIONAL**

## Base canónica

Treskal no dispone de alcantarillado moderno.

La gestión urbana puede combinar:

- pozos negros;
- letrinas;
- recogida periódica;
- retirada de residuos;
- puntos de eliminación fuera del tejido denso;
- reutilización agrícola cuando sea plausible.

La ciudad debe parecer:

- usada;
- trabajada;
- razonablemente mantenida;

no una calle permanentemente cubierta de basura.

---

# 1. Principio

Todo residuo relevante tiene:

- origen;
- tipo;
- ubicación;
- cantidad o carga;
- responsable o usuario cuando proceda;
- vía de retirada;
- destino.

No desaparece simplemente porque cambie el LOD.

---

# 2. Familias de residuo

## WASTE01 — doméstico ordinario

Puede incluir:

- restos de comida;
- ceniza;
- materiales gastados;
- pequeños desperdicios.

## WASTE02 — orgánico de mercado

Especialmente:

- fruta/verdura deteriorada;
- restos alimentarios;
- embalajes orgánicos.

## WASTE03 — pescado y actividad portuaria alimentaria

Requiere retirada especialmente rápida por:

- olor;
- deterioro;
- insectos;
- salubridad.

## WASTE04 — matanza y carnicería

Se genera principalmente en espacios de sacrificio/despiece compatibles.

No debe dominar calles centrales.

## WASTE05 — animales

Incluye:

- estiércol;
- cama sucia;
- residuos de establo/corral.

## WASTE06 — taller/artesanía

Puede incluir:

- recortes;
- serrín;
- viruta;
- ceniza;
- restos de material;
- piezas inservibles.

Parte puede ser reutilizable.

## WASTE07 — sanitario/doméstico humano

Incluye residuos asociados a:

- letrinas;
- pozos negros;
- cuidado de enfermos.

Su manipulación necesita separación de agua potable y alimentos.

## WASTE08 — obra y demolición

Incluye:

- madera;
- piedra;
- yeso/revestimiento compatible;
- piezas rotas;
- material recuperable.

---

# 3. Residuo ≠ basura inútil

Algunos materiales pueden:

- reutilizarse;
- repararse;
- venderse;
- quemarse si es seguro;
- emplearse en agricultura;
- convertirse en materia secundaria.

El sistema debe distinguir:

- recuperable;
- reutilizable;
- combustible;
- orgánico;
- contaminante;
- desecho final.

---

# 4. Hogares

Un hogar puede acumular una carga limitada de residuos.

La retirada puede realizarse mediante:

- residente;
- trabajador;
- recogida;
- traslado a punto permitido.

No se arroja automáticamente a la calle.

---

# 5. Letrinas

Pueden existir en:

- vivienda;
- patio;
- posada;
- negocio;
- instalación.

La forma concreta depende de:

- edificio;
- densidad;
- agua;
- suelo;
- espacio.

No se presupone retrete con descarga moderna.

---

# 6. Pozos negros

Cuando existan:

- tienen capacidad finita;
- necesitan vaciado o gestión;
- deben mantenerse alejados de captaciones potables;
- pueden generar problema si se saturan o dañan.

No es necesario simular volumen litro a litro.

---

# 7. Mercados

Plaza del Abasto y Lonja requieren limpieza frecuente.

La actividad puede producir:

- restos;
- agua sucia;
- envases;
- material de embalaje;
- desperdicio orgánico.

El cierre de puestos no limpia mágicamente el lugar.

---

# 8. Lonja y pescado

WASTE03 debe retirarse con rapidez.

La acumulación puede aumentar:

- olor;
- insectos;
- deterioro;
- presión sanitaria.

No convierte todo Z10 en suciedad permanente.

---

# 9. Corrales y establos

WASTE05 puede acumularse en:

- establos;
- patios;
- rutas de ganado;
- S10/Z14.

La retirada puede conectar con:

- agricultura;
- transporte rural.

No todo estiércol se considera desperdicio sin valor.

---

# 10. Talleres de madera

Serrín, viruta y recortes pueden tener destinos distintos:

- combustible;
- embalaje;
- encendido;
- reutilización;
- desecho.

El serrín acumulado cerca de fuego aumenta riesgo.

---

# 11. Herrería y hornos

Pueden generar:

- ceniza;
- escoria u otros residuos canónicos futuros;
- material roto.

La metalurgia exacta queda pendiente.

No se inventan subproductos técnicos no definidos.

---

# 12. Construcción

BUILD10 y reparaciones pueden generar WASTE08.

Material útil puede recuperarse antes de desechar.

Esto afecta:

- stock;
- transporte;
- obra.

---

# 13. Retirada

La retirada puede necesitar:

- persona;
- recipiente;
- carro;
- ruta;
- destino.

No existe red invisible de eliminación.

---

# 14. Puntos de eliminación

Deben situarse fuera del tejido denso o en posiciones compatibles.

El plano futuro fijará:

- localización;
- distancia;
- accesos;
- relación con agua y viento.

No se inventa vertedero concreto antes del plano.

---

# 15. Reutilización agrícola

Puede existir cuando sea:

- plausible;
- segura según conocimientos del mundo;
- logística y socialmente aceptada.

No se modela como reciclaje moderno perfecto.

---

# 16. Agua sucia

No debe vaciarse indiscriminadamente en:

- pozos;
- fuentes;
- captaciones.

La relación aguas arriba/abajo se fijará con geometría real.

---

# 17. Limpieza de calle

Puede incluir:

- retirada manual;
- barrido;
- recogida;
- drenaje;
- intervención tras mercado/ganado/evento.

No toda calle recibe el mismo nivel de atención.

---

# 18. Prioridad

Puede ser mayor en:

- mercado;
- lonja;
- acceso institucional;
- ruta de mucho tránsito;
- zona de alimentos;
- punto de agua.

---

# 19. Saturación

Si falla la retirada:

puede aumentar:

- suciedad;
- olor;
- obstáculos;
- insectos;
- riesgo sanitario futuro;
- reputación local.

No genera enfermedad automáticamente sin sistema sanitario.

---

# 20. Clima

La lluvia puede:

- mover residuos;
- empeorar barro;
- diluir algunos restos;
- arrastrar contaminación.

No “limpia toda la ciudad” de forma automática.

---

# 21. Evento

D03, D06, D07 u otros eventos pueden generar cargas extraordinarias.

La retirada posterior forma parte de las consecuencias.

---

# 22. Visual

La suciedad urbana debe concentrarse donde exista causa.

Ejemplos:

- salida de establo;
- muelle de pescado;
- obra;
- zona de carga;
- calle embarrada.

No aplicar una capa uniforme de basura medieval.

---

## Regla final

**Treskal permanece funcional porque los residuos se mueven fuera de donde molestan o contaminan; la ausencia de alcantarillado moderno no implica ausencia de organización.**
