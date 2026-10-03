# Treskal — comercio, proveedores e inventarios dinámicos v0.1

## Estado

**DISEÑO DE GAMEPLAY APROBADO — ECONOMÍA INTERACTIVA**

## Objetivo

Hacer que comprar y encargar objetos dependa de proveedores reales y de las cadenas económicas de Treskal.

---

# 1. No existe tienda universal

Ningún comercio debe vender automáticamente:

- comida;
- armas;
- herramientas;
- ropa;
- pociones;
- materiales;
- objetos raros

en un único inventario genérico.

Cada proveedor vende lo que su actividad explica.

---

# 2. Tipos de proveedor

Un bien puede obtenerse de:

- productor;
- artesano;
- comerciante;
- puesto de mercado;
- almacén;
- taberna;
- posada;
- hogar;
- proveedor institucional cuando proceda.

---

# 3. Inventario derivado

El inventario disponible debe depender de:

- tipo de proveedor;
- oficio;
- estación;
- stock previo;
- entradas recientes;
- demanda;
- escasez;
- encargos;
- capacidad de almacenamiento;
- World State.

No se rerollea completamente cada vez que el jugador abre una tienda.

---

# 4. Stock persistente

Las compras significativas reducen stock.

Las entradas de mercancía pueden reponerlo por:

- producción;
- entrega;
- mercado;
- barco;
- convoy;
- proveedor.

La reposición debe tener causa.

---

# 5. Producción por encargo

Muchos artesanos trabajan principalmente por encargo.

Un ebanista puede no tener “espadas de madera +3” esperando en un menú.

Puede:

- mostrar trabajos terminados;
- aceptar pedido;
- pedir material;
- fijar plazo;
- cobrar anticipo;
- entregar más tarde.

---

# 6. Calidad

La calidad de un objeto depende de:

- artesano;
- material;
- tiempo;
- herramientas;
- especialidad;
- dificultad.

El tamaño de Treskal aumenta opciones de encontrar buenos profesionales, pero no garantiza calidad excepcional en cada tienda.

---

# 7. Reputación del proveedor

Cada negocio puede tener reputación por:

- calidad;
- precio;
- puntualidad;
- honestidad;
- especialidad;
- clientela.

Los NPC pueden recomendar o evitar proveedores según lo que conocen.

---

# 8. Mercado diario

S06 y otros espacios comerciales permiten comprar productos cotidianos sin localizar siempre al productor.

Aun así:

- el puesto tiene proveedor;
- el stock tiene origen;
- la mercancía puede faltar.

---

# 9. Escasez

Cuando una cadena falla:

- pescado puede escasear tras temporal;
- cereal puede subir tras mala cosecha;
- madera puede retrasarse por camino bloqueado;
- vino puede faltar por retraso comercial;
- piezas navales pueden absorber materiales por un gran encargo de la Corona.

La escasez debe ser visible en:

- inventarios;
- precios;
- diálogo;
- actividad urbana.

---

# 10. Encargos y palabra dada

En Valrik, aceptar un encargo crea una relación social.

Pueden importar:

- plazo;
- calidad prometida;
- precio acordado;
- material entregado;
- anticipo.

El incumplimiento puede afectar reputación.

---

# 11. Horarios

Un proveedor no está disponible siempre.

Depende de:

- rutina;
- mercado;
- trabajo;
- descanso;
- viaje;
- evento.

El jugador puede:

- esperar;
- volver;
- preguntar dónde está;
- buscar otro proveedor.

---

# 12. NPC y negocio

El negocio no es una interfaz separada de la persona.

Debe estar asociado a:

- propietario;
- trabajadores;
- hogar cuando corresponda;
- edificio;
- proveedores;
- clientes.

Si cambia el NPC, el negocio puede cambiar.

---

# 13. Robo, incendio y eventos

El World State puede afectar un establecimiento:

- robo;
- incendio;
- cierre;
- enfermedad;
- muerte;
- traslado;
- embargo o conflicto;
- falta de materia prima.

La tienda no debe reaparecer intacta al recargar zona.

---

# 14. Bienes institucionales

Los suministros de:

- guardia;
- administración;
- Astilleros Reales

no forman parte automáticamente de inventarios públicos.

El acceso depende de función, autoridad y contexto.

---

## Regla final

**En Treskal no compras de una lista: compras a alguien que obtiene, fabrica o comercia algo dentro de una economía real.**
