# Treskal — detección, respuesta y propagación de incendios v0.1

## Estado

**DISEÑO URBANO/JUGABLE APROBADO — RESPUESTA PREINDUSTRIAL AL FUEGO**

## Base canónica

Treskal posee:

- abundante madera;
- hornos;
- hogares;
- fraguas;
- talleres;
- serrín;
- almacenes;
- Astilleros Reales;
- iluminación mediante fuentes de fuego.

No existe un cuerpo moderno de bomberos.

La respuesta puede movilizar:

- vecinos;
- trabajadores;
- guardia urbana;
- personal de talleres;
- cuadrillas internas de instalaciones grandes;
- agua;
- recipientes;
- retirada o demolición de material cuando sea imprescindible.

---

# 1. Principio

Un incendio necesita:

- fuente de ignición;
- combustible;
- condiciones de propagación;
- tiempo.

No se genera por cuota dramática.

---

# 2. Estados operativos

## FIRE01 — ignition_or_smoke

Ignición pequeña, humo o señal inicial.

## FIRE02 — localized_fire

Fuego localizado y todavía controlable.

## FIRE03 — growing_fire

La propagación supera la respuesta inmediata local.

## FIRE04 — major_fire

Afecta varias estancias, edificio o área importante.

## FIRE05 — spreading_between_structures

Existe riesgo o propagación real entre edificios/zonas.

## FIRE06 — contained

La propagación está detenida.

## FIRE07 — extinguished

Ya no existe fuego activo relevante.

## FIRE08 — aftermath

Persisten:

- calor;
- humo;
- daño;
- agua;
- desplazamiento;
- reparación;
- investigación;
- residuos.

Extinguido no equivale a resuelto.

---

# 3. Ignición

Puede proceder de:

- hogar;
- horno;
- fragua;
- lámpara/fuente portátil;
- combustible;
- chispa;
- accidente;
- actividad industrial/artesanal;
- acción deliberada futura.

La causa debe poder registrarse cuando sea relevante.

---

# 4. Propagación

Depende de:

- material;
- proximidad;
- ventilación;
- almacenamiento;
- combustible acumulado;
- mantenimiento;
- viento;
- respuesta;
- accesos.

No toda construcción de madera arde al mismo ritmo.

---

# 5. Detección

Puede producirse mediante:

- humo;
- llama;
- olor;
- sonido;
- aviso;
- percepción directa.

La ciudad no recibe alerta omnisciente.

---

# 6. Primera respuesta

Quien detecta puede:

- avisar;
- retirar personas;
- cortar fuente;
- mover material cercano;
- usar agua/arena/u otro medio canónico;
- pedir ayuda.

La acción depende de riesgo y capacidad.

---

# 7. Agua

La eficacia depende de:

- proximidad;
- cantidad;
- recipientes;
- acceso;
- número de personas;
- continuidad.

Un punto de agua cercano reduce tiempo de respuesta.

No crea presión hidráulica moderna.

---

# 8. Cadena de cubos

Puede organizarse cuando:

- existe fuente de agua;
- hay suficientes personas;
- ruta practicable;
- fuego no hace imposible aproximación.

Su rendimiento depende de logística humana real.

---

# 9. Corte de propagación

Puede implicar:

- retirar combustible;
- cerrar accesos;
- mover carga;
- desmontar partes;
- derribar material/estructura cuando sea imprescindible.

La demolición de emergencia debe generar daño persistente.

---

# 10. Evacuación

Puede afectar:

- residentes;
- huéspedes;
- trabajadores;
- animales;
- objetos esenciales.

No todo bien se salva.

La prioridad básica es proteger personas.

---

# 11. Animales

Establos y corrales añaden dificultad.

Los animales pueden necesitar:

- apertura de acceso;
- conducción;
- traslado a zona segura.

No se liberan mágicamente.

---

# 12. Negocios y talleres

Un fuego puede afectar:

- BIZ;
- stock;
- herramientas;
- COM;
- EMP;
- propiedad.

Cada sistema aplica su consecuencia.

FIRE no duplica cambios.

---

# 13. Noche

La detección puede ser:

- más difícil por menor actividad;
- más visible por llama/luz;
- más peligrosa por ocupantes dormidos.

REST puede ser interrumpido si el aviso llega.

---

# 14. Viento

Puede:

- favorecer propagación;
- transportar chispas;
- dificultar respuesta.

No siempre convierte un incendio en FIRE05.

---

# 15. Lluvia

Puede ayudar a reducir propagación exterior.

No apaga automáticamente:

- fuego interior;
- combustible protegido;
- grandes focos.

---

# 16. Astilleros Reales

T08 debe poseer capacidad interna superior por:

- madera;
- valor estratégico;
- trabajo especializado;
- control de acceso.

Este documento no define:

- jerarquía;
- rangos;
- organización militar.

---

# 17. Guardado

Un incendio activo relevante persiste.

Save/load no:

- extingue;
- reinicia;
- cambia de edificio

el fuego.

---

# 18. IA

La IA recibe:

- estado FIRE;
- fuentes visibles;
- rutas;
- conocimiento del actor;
- acciones físicamente posibles.

No declara:

- “el fuego está controlado”;
- “todos han salido”;
- “no queda nadie dentro”

sin validación del World State.

---

## Regla final

**Un incendio en Treskal es una lucha logística contra fuego, humo, tiempo y materiales; se contiene porque la gente actúa, no porque termina la escena.**
