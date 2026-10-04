# Treskal — mensajería, cartas y comunicación urbana v0.1

## Estado

**DISEÑO SOCIAL/JUGABLE APROBADO — COMUNICACIÓN FÍSICA Y NO INSTANTÁNEA**

## Objetivo

Definir cómo viaja información intencionada dentro y fuera de Treskal mediante:

- recados;
- cartas;
- mensajeros;
- documentos;
- avisos institucionales.

Sin presuponer una red postal pública moderna.

---

# 1. Principio

Un mensaje necesita:

- emisor;
- contenido;
- destino;
- medio;
- tiempo.

La información no “aparece” en el destinatario por existir en World State.

---

# 2. Formas de comunicación

## MSG01 — recado oral

Una persona transmite verbalmente un mensaje.

Ventajas:

- no requiere escritura;
- rápido a corta distancia.

Riesgos:

- olvido;
- deformación;
- interpretación;
- falta de entrega.

## MSG02 — nota o carta privada

Mensaje escrito dirigido a persona concreta.

Requiere:

- capacidad de escribir propia o de tercero;
- soporte físico;
- portador.

## MSG03 — documento comercial

Puede incluir:

- encargo;
- cuenta;
- recibo futuro si el sistema lo define;
- lista;
- instrucción.

No se fija todavía formalidad jurídica.

## MSG04 — comunicación institucional

Procedente de:

- La Casa;
- Justicia;
- guardia;
- Astilleros Reales cuando corresponda.

Puede tener mayor formalidad y portador identificado.

## MSG05 — aviso público

Información colocada o anunciada en lugar concreto.

Solo la conoce quien:

- la ve;
- la oye;
- recibe después el contenido por otra persona.

---

# 3. No existe correo instantáneo

No se presupone:

- buzón universal;
- reparto diario público;
- dirección postal numérica;
- entrega garantizada.

Si en el futuro Norgard desarrolla un servicio organizado, se integrará como sistema superior.

---

# 4. Entrega urbana

Una entrega dentro de Treskal puede depender de:

- distancia;
- conocimiento de dirección;
- tráfico;
- clima;
- disponibilidad del destinatario;
- acceso.

Un mensajero puede llegar al edificio y no poder hablar con la persona.

---

# 5. Entrega territorial

Una carta fuera de Treskal puede viajar mediante:

- mensajero dedicado;
- viajero de confianza;
- comerciante;
- miembro de Casa;
- convoy;
- otro portador plausible.

No existe garantía uniforme.

---

# 6. Destinatario ausente

Si el destinatario no está:

el portador puede:

- esperar;
- dejar el mensaje con persona autorizada;
- volver después;
- regresar al emisor;
- continuar viaje si se acordó.

No se marca “entregado” automáticamente al tocar la puerta.

---

# 7. Cadena de custodia

Un mensaje importante puede registrar:

- sender_ref;
- carrier_ref;
- recipient_ref;
- created_time;
- departure_time;
- delivery_time;
- current_holder;
- state;
- confidentiality;
- related_event_or_pledge.

---

# 8. Estados

## drafted

Creado, aún no enviado.

## entrusted

Entregado al portador.

## in_transit

En desplazamiento.

## attempted

Se intentó entrega sin completarla.

## delivered

Llegó al destinatario o receptor autorizado.

## returned

Volvió al emisor.

## lost

Se perdió.

## intercepted

Cambió de manos de forma no prevista.

---

# 9. Lectura

Un mensaje escrito puede ser:

- leído por destinatario;
- leído por persona autorizada;
- leído por tercero si obtiene acceso.

Entrega ≠ lectura.

---

# 10. Alfabetización

Una persona que no lee puede:

- pedir a alguien de confianza que lea;
- usar recado oral;
- acudir a escribano.

Eso crea dependencia social y posibles problemas de privacidad.

---

# 11. Escribanos

Un escribano puede:

- redactar;
- copiar;
- leer;
- registrar.

No conoce automáticamente el contenido de documentos que nunca manejó.

---

# 12. Confidencialidad

Un mensaje puede ser:

- ordinario;
- privado;
- institucional restringido.

La confidencialidad afecta:

- quién puede recibirlo;
- quién puede leerlo;
- consecuencias de interceptación.

No se fija aquí una ley postal inexistente.

---

# 13. Rumor vs mensaje

Un recado intencional no es rumor por definición.

Pero después puede:

- repetirse;
- deformarse;
- convertirse en K3 para terceros.

---

# 14. Aviso público

Puede existir en:

- mercado;
- institución;
- puerto;
- lugar de reunión.

La forma puede ser:

- escrita;
- proclamada;
- ambas.

No se presupone tablón oficial en cada barrio.

---

# 15. Mensajeros institucionales

La Casa, Justicia y otras instituciones pueden usar personas para llevar:

- citaciones;
- instrucciones;
- documentos;
- avisos.

No se fijan rangos ni cuerpo profesional independiente.

---

# 16. Gameplay

El jugador puede:

- llevar un mensaje;
- contratar portador futuro si el sistema económico lo permite;
- buscar destinatario;
- perder/interceptar carta;
- recibir información tarde.

El mundo sigue avanzando durante el trayecto.

---

# 17. IA

La IA de un NPC solo conoce el mensaje cuando:

- lo recibió;
- lo leyó/oyó;
- otra fuente se lo contó.

No recibe mensajes en tránsito como conocimiento.

---

## Regla final

**En Treskal las palabras viajan con personas, papel y tiempo; comunicar algo también es mover algo por el mundo.**
