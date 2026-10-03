# Treskal — interiores funcionales y transición exterior-interior v0.1

## Estado

**DISEÑO DE GAMEPLAY APROBADO — INTERIORES URBANOS**

## Objetivo

Definir cómo deben funcionar los interiores sin construir miles de edificios únicos manualmente.

La prioridad es que cada interior sea coherente con:

- edificio;
- ocupantes;
- oficio;
- riqueza;
- actividad;
- World State.

---

# 1. Principio de acceso

Un edificio puede ser:

- público;
- semipúblico;
- privado;
- restringido;
- institucional controlado.

La puerta no implica permiso automático de entrada.

---

# 2. Exterior conectado con interior

Cada interior persistente debe referenciar:

- building_id;
- entrance_id;
- sector/subzona;
- ocupantes;
- función;
- propiedad;
- estado.

La entrada visible debe corresponder con la posición real del edificio.

---

# 3. U01 — Casa urbana

Interior mínimo:

- estancia doméstica principal;
- zona de cocina o preparación;
- dormitorios o espacios de descanso;
- almacenamiento.

Puede variar por:

- tamaño;
- familia;
- riqueza;
- oficio.

---

# 4. U02 — Casa-taller

Debe conectar claramente:

**calle/cliente → taller → zona doméstica**

con separación variable.

El jugador debe poder entender:

- qué se fabrica;
- dónde trabaja el artesano;
- dónde vive la familia.

---

# 5. U03 — Comercio con vivienda

Debe incluir:

- espacio de atención;
- stock accesible o de muestra;
- almacenamiento;
- vivienda privada.

El inventario de UI no sustituye la existencia física razonable del negocio.

---

# 6. U05 — Posada

Debe poder contener:

- sala común;
- cocina;
- habitaciones;
- dependencias del propietario;
- almacén;
- patio/establo si procede.

No todas las habitaciones necesitan ser accesibles siempre.

---

# 7. U06 — Taberna

Debe priorizar:

- sala;
- cocina;
- almacenamiento;
- espacio del propietario.

Puede ser pequeña y muy integrada en vivienda.

---

# 8. U07 — Taller especializado

Interior dependiente del oficio.

Debe reflejar:

- herramientas;
- materiales;
- proceso;
- riesgo;
- número de trabajadores.

No reutilizar un “taller genérico” sin adaptar el contenido.

---

# 9. U08/U09 — Almacenes y graneros

Deben tener:

- lógica de carga;
- apilado;
- control de humedad;
- acceso de trabajadores;
- stock ligado a World State.

El contenido visual debe cambiar si el almacén está vacío, lleno o dañado.

---

# 10. U11/U12 — Administración y justicia

Necesitan jerarquía de acceso:

- recepción;
- trabajo ordinario;
- archivo;
- dependencias restringidas.

No todo ciudadano puede caminar libremente hasta el archivo.

---

# 11. U13 — Puerto

Los interiores portuarios pueden incluir:

- almacenes;
- pequeños despachos;
- talleres;
- dependencias de intercambio.

Deben conectarse con flujo real de mercancías.

---

# 12. U14 — Astilleros Reales

Acceso restringido.

Los interiores y talleres deben formar parte del recinto T08 y respetar:

- seguridad;
- autoridad de la Corona;
- trabajo naval;
- riesgo de incendio.

---

# 13. Persistencia

Un interior visitado debe conservar cambios relevantes:

- puerta forzada;
- objeto robado;
- mercancía comprada;
- incendio;
- cadáver;
- reparación;
- cambio de propietario.

No se resetea al salir.

---

# 14. Generación por plantilla

Se permiten plantillas de base.

Pero la materialización concreta debe derivarse de:

- tipo U;
- parcela;
- ocupantes;
- profesión;
- riqueza;
- seed estable.

Una vez materializado un interior persistente, no se rerollea.

---

# 15. Decoración

Los objetos deben responder a:

- uso;
- familia;
- oficio;
- capacidad económica;
- costumbre.

No llenar interiores con “clutter medieval” arbitrario.

---

# 16. Privacidad

La IA y el jugador deben reconocer diferencias entre:

- sala pública de tienda;
- vivienda;
- dormitorio;
- almacén privado;
- archivo;
- zona restringida.

Entrar en una zona privada puede generar reacción social o legal.

---

# 17. Horarios

Un interior público puede:

- abrir;
- cerrar;
- funcionar parcialmente;
- estar temporalmente ocupado.

El acceso depende de World State y rutina.

---

## Regla final

**Un interior de Treskal no es una instancia decorativa: pertenece a alguien, sirve para algo y recuerda lo que ocurrió dentro.**
