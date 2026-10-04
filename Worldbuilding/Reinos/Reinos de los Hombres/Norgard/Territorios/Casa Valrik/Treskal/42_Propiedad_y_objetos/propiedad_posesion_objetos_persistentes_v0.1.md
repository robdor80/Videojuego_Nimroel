# Treskal — propiedad, posesión y objetos persistentes v0.1

## Estado

**DISEÑO DE WORLD STATE APROBADO — OBJETOS CON PROPIEDAD Y CONTEXTO**

## Objetivo

Distinguir entre:

- propiedad;
- posesión física;
- ubicación;
- permiso de uso;
- reserva;
- custodia.

Para que objetos, mercancías y pertenencias no cambien de dueño solo porque alguien los recoja o mueva.

---

# 1. Propietario ≠ poseedor

Un objeto puede tener:

## owner_ref

Persona, hogar, negocio o institución propietaria.

## possessor_ref

Persona o entidad que lo lleva o controla físicamente.

## location_ref

Lugar actual.

## custody_ref

Persona o entidad responsable de guardarlo.

Estos campos pueden coincidir o no.

---

# 2. Ejemplos

## Herramienta prestada

- owner_ref: maestro;
- possessor_ref: aprendiz;
- permission: uso autorizado.

## Equipaje en posada

- owner_ref: huésped;
- possessor_ref: huésped;
- location_ref: habitación;
- custody_ref: posada cuando corresponda.

## Mercancía en almacén

- owner_ref: comerciante;
- location_ref: almacén;
- custody_ref: almacenista.

## Llave institucional

- owner_ref: institución;
- possessor_ref: funcionario;
- use_scope: acceso concreto.

---

# 3. Estados de relación con objeto

## OWN01 — propio

El actor es propietario.

## OWN02 — prestado

Uso temporal autorizado.

## OWN03 — bajo custodia

Se guarda para otro.

## OWN04 — reservado

Existe pero está comprometido.

## OWN05 — institucional

Pertenece a entidad/institución.

## OWN06 — abandonado

No tiene propietario conocido o ha sido dejado de forma que el sistema lo considere abandonado.

No debe asignarse este estado automáticamente solo porque no haya NPC cerca.

## OWN07 — disputado

Dos o más partes reclaman derechos.

La resolución legal futura queda fuera de este documento.

---

# 4. Recoger no cambia propiedad

Si el jugador toma un objeto ajeno:

- cambia posesión;
- puede cambiar ubicación;
- no cambia automáticamente owner_ref.

La propiedad solo cambia mediante:

- venta;
- regalo;
- transferencia autorizada;
- resolución futura del sistema jurídico;
- otro mecanismo canónico.

---

# 5. Permiso de uso

Puede ser:

- none;
- personal;
- household;
- workplace;
- role_based;
- public.

Ejemplo:

una herramienta de taller puede ser usada por trabajadores sin pertenecerles.

---

# 6. Préstamo

Un préstamo relevante puede registrar:

- lender;
- borrower;
- item_ref;
- start_time;
- expected_return;
- conditions;
- state.

Puede estar ligado a:

- pledge;
- relación;
- negocio.

---

# 7. Consumo

Un objeto consumible autorizado puede:

- desaparecer;
- reducir cantidad;
- transformarse.

La propiedad se resuelve antes del consumo.

Consumir algo ajeno sin permiso no convierte el objeto en propio retroactivamente.

---

# 8. Contenedor

Un contenedor puede tener:

- propietario;
- acceso;
- contenido.

Abrir un contenedor no transfiere propiedad de lo que contiene.

---

# 9. Stock comercial

Un objeto o lote a la venta sigue siendo del vendedor hasta que se complete la transacción.

Estar expuesto en un puesto no significa acceso libre.

---

# 10. Stock reservado

Si un bien está reservado para:

- encargo;
- institución;
- cliente

no es stock libre.

Puede seguir físicamente en almacén o tienda.

---

# 11. Objeto encontrado

Encontrar un objeto puede producir estados distintos:

- perdido por alguien;
- abandonado;
- dejado temporalmente;
- robado previamente;
- evidencia.

El sistema no debe asumir “sin dueño” por falta de contexto.

---

# 12. Robo

El robo requiere como mínimo:

- objeto ajeno;
- ausencia de permiso suficiente;
- toma o apropiación.

La clasificación jurídica exacta pertenece a la Ley del Rey.

El World State conserva el hecho físico aunque nadie lo haya visto.

---

# 13. Testigos

El conocimiento del robo depende de:

- testigos;
- evidencia;
- denuncia;
- investigación.

Un robo secreto no actualiza reputación global.

---

# 14. Regalo

Una transferencia voluntaria puede cambiar owner_ref.

La IA que diga:

“te lo regalo”

debe emitir intención de transferencia.

El motor valida:

- que el NPC sea propietario o tenga autoridad;
- que el objeto exista;
- que pueda transferirse.

---

# 15. Compra

Una transacción completa puede cambiar:

- owner_ref;
- possessor_ref;
- stock.

No se ejecuta solo por texto.

---

# 16. Objeto de hogar

Puede pertenecer a:

- individuo;
- hogar compartido;
- negocio familiar.

No todo objeto doméstico necesita propietario individual.

---

# 17. Objeto institucional

Puede pertenecer a:

- Casa Valrik;
- Justicia;
- guardia;
- Corona/Astilleros.

El funcionario que lo porta no se convierte en propietario.

---

# 18. Evidencia

Un objeto puede recibir flag de evidencia.

Esto no cambia su propietario.

Puede cambiar:

- custody_ref;
- access;
- ubicación.

---

# 19. Destrucción

Si un objeto se destruye:

- sale del inventario;
- conserva referencia histórica si era relevante.

No reaparece por recarga.

---

# 20. LOD

En LOD bajo:

objetos ordinarios pueden agregarse.

Los objetos persistentes relevantes mantienen:

- identidad;
- owner;
- location;
- state.

---

## Regla final

**En Treskal mover una cosa no significa poseerla; el mundo recuerda de quién era, quién la tenía y por qué.**
