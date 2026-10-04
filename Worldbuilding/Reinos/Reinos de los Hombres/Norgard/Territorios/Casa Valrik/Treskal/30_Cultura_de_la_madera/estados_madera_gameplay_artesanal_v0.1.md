# Treskal — estados de la madera y gameplay artesanal v0.1

## Estado

**DISEÑO DE GAMEPLAY APROBADO**

## Objetivo

Permitir que la madera sea una mercancía con estado y destino, no un recurso genérico idéntico.

---

# 1. Estados conceptuales

## W01 — tronco o pieza bruta

Recién recibida o apenas preparada.

## W02 — madera transformada primaria

Tablones, vigas o piezas tras aserrado/despiece inicial.

## W03 — en secado/acondicionamiento

Todavía no está lista para todos los usos.

## W04 — preparada para carpintería general

Adecuada para usos ordinarios compatibles.

## W05 — seleccionada para trabajo fino

Material de calidad adecuada para ebanistería/talla.

## W06 — reservada para uso naval

Lote seleccionado para requerimientos navales concretos.

## W07 — componente trabajado

Pieza ya fabricada pero no producto final.

## W08 — producto terminado

Mueble, elemento, pieza decorativa u otro bien acabado.

Los estados son funcionales, no una clasificación botánica.

---

# 2. Cambio de estado

Cada transición necesita:

- trabajo;
- tiempo;
- espacio;
- herramientas;
- condiciones.

No existe transformación instantánea de tronco a mueble.

---

# 3. Lote

La simulación puede manejar madera por lotes.

Un lote puede registrar:

- origen;
- propietario;
- cantidad agregada;
- estado W;
- calidad;
- destino;
- reserva;
- ubicación.

---

# 4. Calidad

No toda madera de un lote tiene calidad idéntica.

Para simulación agregada puede usarse un perfil de calidad.

Solo se individualiza una pieza cuando sea relevante.

---

# 5. Humedad/acondicionamiento

El tiempo de acondicionamiento puede verse afectado por:

- lluvia;
- ventilación;
- protección;
- estación.

No se exige simulación física científica completa.

Sí coherencia causal.

---

# 6. Robo o pérdida

Un lote puede:

- desaparecer parcialmente;
- quemarse;
- mojarse;
- ser desviado;
- cambiar de propietario.

Eso afecta producción posterior.

---

# 7. Encargo

Un encargo puede reservar:

- material W04/W05;
- componente W07.

Mientras esté reservado no aparece como stock libre.

---

# 8. Astilleros

Una demanda naval puede reservar W06.

No toda madera de alta calidad debe convertirse automáticamente en W06.

El destino depende de:

- dimensiones;
- forma;
- requisitos;
- decisión institucional.

---

# 9. Gameplay

El jugador puede encontrarse con problemas como:

- madera disponible pero aún húmeda;
- lote correcto reservado;
- pérdida por incendio;
- retraso forestal;
- material de calidad insuficiente.

Así la escasez no se reduce a “0 unidades”.

---

## Regla final

**En Treskal el valor de la madera depende de su historia física: de dónde vino, cómo fue tratada y para qué está preparada.**
