# Treskal — consumo, reposición y circulación cotidiana v0.1

## Estado

**DISEÑO ECONÓMICO APROBADO — SIMULACIÓN AGREGADA**

## Objetivo

Cerrar el ciclo económico cotidiano de Treskal:

**entrada/producción → almacenamiento → distribución → venta/uso → consumo/pérdida → reposición**

No es necesario simular individualmente cada pan, jarra o clavo.

---

# 1. Fuentes de demanda

La demanda urbana procede de:

## Hogares

Consumen:

- alimentos;
- combustible doméstico cuando corresponda;
- ropa y calzado;
- reparación;
- bienes domésticos.

## Negocios

Consumen:

- materias primas;
- herramientas;
- alimentos;
- recipientes;
- suministros.

## Posadas y tabernas

Consumen según:

- huéspedes;
- comidas;
- actividad;
- visitantes.

## Puerto

Consume:

- provisiones;
- reparaciones;
- herramientas;
- materiales.

## Instituciones

La Casa, Justicia, guardia y Astilleros Reales generan demandas propias.

## Visitantes

Aumentan temporalmente:

- alojamiento;
- comida;
- transporte;
- determinados servicios.

---

# 2. Consumo agregado

Para bienes cotidianos de gran volumen se permite resolución agregada.

Ejemplo conceptual:

`stock de cereal + entradas - consumo urbano - pérdidas = stock siguiente`

No se rastrea el destino de cada grano.

---

# 3. Consumo individual relevante

Sí merece persistencia individual cuando afecta a:

- objeto único;
- encargo;
- evidencia;
- mercancía valiosa;
- misión;
- propiedad concreta.

---

# 4. Reposición

El stock puede reponerse por:

- producción local;
- entrega rural;
- convoy;
- barco;
- traslado entre almacenes;
- fabricación;
- devolución.

Toda reposición importante debe tener causa.

---

# 5. Separación de capas

Debe distinguirse:

## Stock de ciudad

Existencia agregada en Treskal.

## Stock logístico

Mercancía en:

- almacenes;
- patios;
- puerto;
- convoyes llegados.

## Stock comercial

Disponible para venta.

## Stock reservado

Comprometido para:

- encargo;
- institución;
- cliente;
- producción.

## Stock en tránsito

Todavía no disponible en destino.

---

# 6. Reserva

Un producto puede existir físicamente pero no estar disponible para compra.

Ejemplos:

- madera reservada para Astilleros Reales;
- encargo de ebanista;
- cargamento de comerciante aún no puesto a la venta.

---

# 7. Demanda extraordinaria

Puede aparecer por:

- evento;
- obra;
- incendio;
- mercante;
- visitantes;
- contrato real;
- reparación naval.

La demanda no debe multiplicarse sin causa.

---

# 8. Sustitución

Cuando un producto escasea pueden existir sustitutos solo si son cultural y funcionalmente plausibles.

No se crea automáticamente una alternativa equivalente.

Ejemplo:

falta pescado fresco puede aumentar consumo de:

- pescado conservado;
- otras proteínas disponibles.

Pero depende del stock real.

---

# 9. Pérdida

Stock puede reducirse por:

- deterioro;
- incendio;
- agua;
- robo;
- accidente;
- desperdicio.

La pérdida pertenece al World State.

---

# 10. Producción

La producción depende de:

- trabajadores;
- materia prima;
- herramientas;
- tiempo;
- capacidad;
- estado del negocio.

Un taller cerrado no produce “por tick” solo porque su receta exista.

---

# 11. Hogares y alimentación

No se requiere simular cada comida.

El sistema puede resolver necesidades agregadas por:

- tamaño de hogar;
- recursos;
- disponibilidad;
- hábitos culturales;
- estación.

Solo baja a detalle cuando exista relevancia jugable.

---

# 12. Instituciones

La demanda institucional debe ser visible en economía.

Ejemplo:

un gran encargo de la Corona puede aumentar temporalmente:

- demanda de madera;
- metal;
- transporte.

Esto puede reducir disponibilidad comercial sin que el producto desaparezca misteriosamente.

---

# 13. Comercio entre negocios

Un negocio puede comprar a otro.

Ejemplo:

- taberna compra cerveza;
- ebanista compra madera;
- carretero paga reparación;
- posada compra alimentos.

No toda mercancía pasa por consumidor final directamente.

---

# 14. Resolución fuera de escena

En LOD-L puede calcularse por periodos agregados.

Debe respetar:

- stock inicial;
- entradas;
- capacidad;
- evento;
- trabajadores;
- demanda.

No usar una media que ignore una interrupción importante.

---

## Regla final

**En Treskal un bien está disponible porque alguien lo produjo o lo trajo, alguien lo almacenó y todavía no se ha consumido ni comprometido.**
