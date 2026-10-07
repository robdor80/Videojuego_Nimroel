# Treskal — almacenamiento, perecibilidad y reservas urbanas v0.1

## Estado

**DISEÑO ECONÓMICO APROBADO — SIN CANTIDADES NUMÉRICAS FIJAS**

## Objetivo

Clasificar mercancías por sus necesidades de almacenamiento y su capacidad de resistir interrupciones.

No fija toneladas ni días exactos de reserva.

---

# 1. Clases técnicas de almacenamiento

## ST1 — Muy perecedero

Ejemplos:

- pescado fresco;
- determinados alimentos preparados.

Necesita:

- venta rápida;
- conservación;
- consumo.

Una interrupción se nota pronto.

## ST2 — Perecedero

Ejemplos:

- parte de productos de huerta;
- determinados alimentos.

Tolera almacenamiento limitado según estación y conservación.

## ST3 — Seco / almacenable

Ejemplos:

- cereal;
- harina en condiciones adecuadas;
- legumbres secas;
- determinados productos conservados.

Permite reserva más estable.

## ST4 — Durable comercial

Ejemplos:

- herramientas;
- tejidos;
- calzado;
- cerámica;
- productos terminados.

El principal límite suele ser espacio, valor y demanda.

## ST5 — Material voluminoso

Ejemplos:

- madera;
- grandes piezas;
- materiales de construcción.

Necesita:

- patios;
- cobertizos;
- acceso de carros;
- separación frente a fuego.

## ST6 — Institucional/estratégico

Ejemplos:

- determinados suministros de T08;
- archivos o materiales controlados.

Su acceso y gestión dependen de institución.

---

# 2. Pescado

ST1.

Si la pesca cae por temporal:

- el stock fresco baja rápido;
- puede crecer peso de pescado conservado;
- precio/disponibilidad pueden cambiar.

No se rellena inventario por normalización automática.

---

# 2B. Estado FOOD

El contrato Core añade estado alimentario:

- FOOD01 raw/unprepared;
- FOOD02 prepared;
- FOOD03 preserved;
- FOOD04 aging/declining;
- FOOD05 spoiled/unsafe;
- FOOD06 waste/discarded.

ST describe necesidad de almacenamiento.

FOOD describe el estado del alimento.

Conservar puede alterar su comportamiento de almacenamiento, pero no lo vuelve eterno.

# 3. Cereal

ST3.

Treskal debe disponer de capacidad de almacenamiento suficiente para:

- abastecimiento urbano;
- variación de entregas;
- comercio.

No se fija reserva exacta hasta modelar:

- producción;
- consumo;
- logística;
- calendario.

---

# 4. Madera

ST5.

Los Patios permiten acumular volumen.

La reserva de madera no implica que toda esté lista para cualquier uso.

Puede diferenciarse por:

- especie;
- estado;
- secado;
- tamaño;
- destino.

---

# 5. Mercancía importada

Puede variar mucho.

El sistema debe conservar:

- origen;
- proveedor;
- cantidad agregada;
- destino;
- stock.

Un barco puede cambiar disponibilidad local sin crear producción local.

---

# 6. Stock de negocio vs stock urbano

Un negocio posee su propio stock.

La ciudad puede tener mercancía almacenada en otros puntos.

Que una tienda esté vacía no significa que no exista producto en Treskal.

Puede existir:

- en almacén;
- en otro negocio;
- pendiente de traslado.

---

# 7. Almacén y propietario

Un almacén puede contener mercancía de:

- propietario del edificio;
- comerciante;
- institución;
- múltiples clientes.

La relación exacta se guarda por lote agregado cuando sea relevante.

---

# 8. Capacidad

Cada almacén/patio tiene capacidad finita.

Si se llena:

- nuevas entregas esperan;
- se buscan otros espacios;
- se redirige mercancía;
- aumenta congestión.

No existe almacenamiento infinito invisible.

---

# 9. Daño

Mercancía puede perderse por:

- incendio;
- agua;
- robo;
- deterioro;
- accidente.

La pérdida afecta a:

- stock;
- negocio;
- precios;
- encargos.

---

# 10. Reserva y escasez

La resiliencia depende de:

- clase ST;
- cantidad almacenada;
- ritmo de consumo;
- producción;
- ruta alternativa.

No todas las mercancías reaccionan igual al mismo corte.

---

# 11. Gameplay

El jugador puede encontrar una escasez porque:

- falta el producto;
- existe pero está almacenado y no distribuido;
- el propietario no vende;
- una institución lo ha contratado;
- la ruta está cortada.

Esto produce problemas distintos.

---

## Regla final

**La disponibilidad en Treskal depende tanto de cuánto existe como de dónde está, quién lo posee y si puede llegar a quien lo necesita.**
