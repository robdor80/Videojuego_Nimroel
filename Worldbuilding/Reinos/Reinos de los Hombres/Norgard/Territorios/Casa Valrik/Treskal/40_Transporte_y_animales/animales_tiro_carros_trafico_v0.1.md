# Treskal — animales de tiro, carros y tráfico urbano v0.1

## Estado

**DISEÑO URBANO/JUGABLE APROBADO — MOVILIDAD PREINDUSTRIAL**

## Objetivo

Integrar de forma realista:

- carros;
- animales de tiro;
- monturas;
- ganado;
- carga;
- peatones

en la circulación de Treskal.

Sin fijar todavía una taxonomía exhaustiva de vehículos.

---

# 1. Principio

La movilidad urbana depende de:

- ancho de vía;
- carga;
- animal;
- destino;
- tráfico;
- clima;
- estado del firme;
- evento.

No todos los actores utilizan la misma ruta.

---

# 2. Clases técnicas de movimiento

## TR01 — peatón

Mayor flexibilidad espacial.

Puede usar:

- calles;
- pasos locales;
- conexiones estrechas.

## TR02 — montura individual

Requiere:

- espacio;
- cuidado;
- control.

No entra automáticamente en cualquier calle o interior.

## TR03 — carro ligero

Adecuado para:

- carga ligera;
- reparto;
- abastecimiento urbano.

## TR04 — carro pesado

Adecuado para:

- madera;
- grandes lotes;
- carga voluminosa.

Debe favorecer:

- C02;
- C06;
- C07;
- rutas anchas.

## TR05 — ganado en tránsito

Debe usar recorridos compatibles.

Preferencia:

- C06;
- Z14;
- áreas periféricas.

Evita T03 cuando exista alternativa.

## TR06 — convoy

Conjunto de:

- varios carros;
- animales;
- trabajadores;
- carga.

Puede generar congestión y evento D05 u otro estado compatible.

---

# 3. Animales

Treskal necesita animales para:

- tiro;
- montura;
- transporte;
- abastecimiento;
- ganado de mercado.

No se fijan aquí:

- razas;
- pelajes;
- estándares de cría;
- estadísticas.

Esos detalles pertenecen al futuro canon animal.

---

# 4. Caballos

El canon territorial confirma uso de caballos en guardias rurales montados.

En Treskal pueden aparecer como:

- montura;
- tiro cuando sea compatible;
- animal de visitante;
- transporte institucional.

No se presupone que todo carro use caballo.

---

# 5. Otros animales de tiro

El sistema permite otros animales de tiro coherentes con el futuro canon ganadero.

No se inventan especies concretas si no están definidas.

---

# 6. Estabulación

Los animales necesitan:

- agua;
- alimento;
- descanso;
- espacio;
- limpieza.

La ciudad requiere capacidad de estabulación asociada a:

- posadas terrestres;
- carreteros;
- T10/Z14;
- negocios de transporte;
- determinadas instalaciones.

No se aparcan animales indefinidamente en la calle.

---

# 7. Agua

Los puntos de agua urbanos deben contemplar consumo animal donde corresponda.

No todo punto potable para personas debe permitir uso animal simultáneo.

La configuración final depende de plano y saneamiento.

---

# 8. Alimentación

El mantenimiento de animales consume:

- forraje;
- cereal u otros alimentos compatibles.

La logística animal forma parte de la demanda urbana.

No funciona gratis fuera del sistema de stock.

---

# 9. Residuos

Animales y ganado generan residuos.

Debe existir retirada o limpieza suficiente en:

- establos;
- corrales;
- rutas de mucho tránsito;
- zonas de carga.

La presencia animal no justifica representar toda calle cubierta de estiércol.

---

# 10. Descanso

Un convoy largo puede necesitar:

- parar;
- descargar parcialmente;
- dar agua;
- alimentar animales.

Eso puede ocupar espacio urbano real.

---

# 11. Congestión

Puede aumentar por:

- convoy;
- ganado;
- mercado;
- lluvia;
- accidente;
- calle bloqueada;
- descarga.

La congestión incrementa coste de navegación.

No desaparece porque el jugador necesite pasar.

---

# 12. Prioridad de ruta

## C01

Tráfico general y carros compatibles.

## C02

Madera y carga pesada.

## C03

Mixto, con prioridad humana/comercial.

## C05

Carga fluvial ligera/media y trabajadores.

## C06

Ganado y abastecimiento periférico.

## C07

Suministro autorizado de Astilleros.

## C08

Redistribución y desvío.

---

# 13. Mercado

Un carro puede:

- entregar;
- recoger;
- esperar en espacio de carga.

No debe estacionarse indefinidamente bloqueando Plaza del Abasto.

---

# 14. Puerto

El tráfico terrestre del puerto debe coordinarse con:

- descarga;
- almacenes;
- trabajadores;
- espacio.

Un mercante grande puede elevar demanda de TR03/TR04 temporalmente.

---

# 15. Madera

Los lotes voluminosos requieren:

- TR04;
- TR06;
- patios;
- maniobra.

Esto refuerza por qué C02 y Z06 tienen identidad distinta del centro comercial.

---

# 16. Seguridad

Un animal asustado, un carro roto o carga caída puede crear:

- bloqueo;
- accidente;
- evento;
- heridos.

No se utiliza como incidente aleatorio obligatorio.

Necesita causa y contexto.

---

# 17. Noche

El tráfico pesado ordinario puede reducirse por:

- visibilidad;
- ruido;
- actividad.

Puede continuar cuando exista:

- urgencia;
- puerto;
- encargo;
- operación institucional.

No se fija prohibición nocturna universal.

---

# 18. Clima

## Lluvia

Puede aumentar:

- barro;
- frenado deficiente;
- lentitud;
- desgaste.

## Temporal

Afecta especialmente a interacción puerto-tierra.

---

# 19. NPC

Un carretero necesita:

- origen;
- destino;
- vehículo;
- carga;
- animal;
- ruta.

No es una animación ambiental independiente de mercancía.

---

# 20. Desaparición en LOD

Al bajar de LOD:

un convoy conserva:

- carga;
- ruta;
- progreso;
- animales;
- estado.

No se “evapora” y reaparece en destino.

---

## Regla final

**Mover mercancías por Treskal exige espacio, animales, tiempo y rutas; un carro forma parte de la economía, no del decorado.**
