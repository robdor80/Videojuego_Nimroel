# Norgard — calendario civil, estaciones y fechas v0.1

## Estado

**CANON FUNCIONAL CERRADO — PUNTO 12**

Marcador: `CALENDAR_POINT_12_CLOSED_NORGARD_CIVIL_CALENDAR`

---

## 1. Principio

Norgard utiliza exactamente la estructura civil estándar de Nimroel:

- 12 meses;
- 365 días por año;
- 7 días por semana;
- 24 horas por día;
- 60 minutos por hora;
- 60 segundos por minuto.

No existen años bisiestos.

El objetivo es que el jugador entienda inmediatamente cualquier fecha.

---

## 2. Meses

Los meses se denominan:

1. enero — 31 días;
2. febrero — 28 días;
3. marzo — 31 días;
4. abril — 30 días;
5. mayo — 31 días;
6. junio — 30 días;
7. julio — 31 días;
8. agosto — 31 días;
9. septiembre — 30 días;
10. octubre — 31 días;
11. noviembre — 30 días;
12. diciembre — 31 días.

No existen meses adicionales ni días fuera de mes.

---

## 3. Semana

La semana comienza en lunes:

1. lunes;
2. martes;
3. miércoles;
4. jueves;
5. viernes;
6. sábado;
7. domingo.

No existe un día religioso universal de descanso.

Sábado y domingo no implican automáticamente:

- cierre de tiendas;
- cierre de mercados;
- descanso laboral;
- prohibición de viajar;
- ceremonia.

EMP, AGEN, negocio e institución determinan actividad real.

---

## 4. Año

El año de referencia de la fase actual del proyecto es:

**15375**

Las escenas o hechos ya situados en 15374 siguen perteneciendo al año 15374.

Punto 12 no refecha retroactivamente el lore.

El inicio exacto de cada campaña debe declarar:

- año;
- mes;
- día;
- hora.

---

## 5. Origen del cómputo

Punto 12 no define qué acontecimiento histórico ocurrió en el año 1.

La cronología existe y funciona.

La explicación histórica del origen del cómputo puede desarrollarse posteriormente si aporta valor.

No se inventa un evento fundacional solo para justificar el número 15375.

---

## 6. Estaciones

Para simulación sencilla, Norgard usa cuatro estaciones civiles:

### primavera

- marzo;
- abril;
- mayo.

### verano

- junio;
- julio;
- agosto.

### otoño

- septiembre;
- octubre;
- noviembre.

### invierno

- diciembre;
- enero;
- febrero.

La etiqueta estacional cambia al comenzar el primer día del mes correspondiente.

---

## 7. Estación no significa clima instantáneo

El cambio:

`28 de febrero → 1 de marzo`

cambia la etiqueta civil de invierno a primavera.

No obliga a:

- subir inmediatamente la temperatura;
- secar el suelo;
- cambiar toda la ropa;
- terminar lluvias;
- producir una cosecha;
- abrir rutas.

El clima y el estado ambiental evolucionan mediante sus propios sistemas.

---

## 8. Variación territorial

La misma fecha puede sentirse diferente en:

- norte de Valrik;
- Treskal;
- Galdren;
- Edranor;
- Darovan;
- Hallheim;
- Syvaris/Taramin.

La estación civil es común.

El clima local no.

---

## 9. Hora civil

Norgard utiliza formato de 24 horas.

Ejemplos:

- 06:30;
- 12:00;
- 16:45;
- 23:10.

No existen husos horarios internos de Norgard.

---

## 10. Habla cotidiana

Aunque el motor conozca la hora exacta, una persona puede hablar de:

- madrugada;
- mañana;
- mediodía;
- tarde;
- noche;
- dentro de un rato;
- antes de comer;
- después del trabajo;
- mañana;
- la próxima semana.

El nivel de precisión depende de:

- contexto;
- necesidad;
- acceso a medición;
- oficio;
- costumbre.

---

## 11. Franja narrativa

La documentación narrativa puede usar:

- Madrugada;
- Mañana;
- Mediodía;
- Tarde;
- Noche.

Formato recomendado de encabezado:

`POV — Lugar, Reino`

`18 de octubre de 15375 — Tarde`

El motor puede conservar debajo una hora exacta.

---

## 12. Cumpleaños y edad

La edad cambia al comenzar la fecha de cumpleaños.

Ejemplo:

una persona nacida:

`14 de mayo de 15357`

cumple 18 años:

`14 de mayo de 15375`

La celebración es opcional y social.

La capacidad jurídica cambia por fecha, no por celebración.

---

## 13. Nacimiento

Todo nacimiento persistente registra:

- fecha;
- hora cuando se conozca;
- lugar;
- npc_id.

El nombre puede registrarse más tarde mediante NAME sin alterar la fecha de nacimiento.

---

## 14. Muerte

Toda muerte persistente registra:

- fecha;
- hora cuando se conozca;
- lugar;
- causa/ref según sistema propietario.

La fecha permite:

- luto;
- herencia;
- aniversarios;
- investigación;
- continuidad laboral;
- memoria.

---

## 15. Luto de tres jornadas

El luto formal de Norgard sigue siendo de **tres jornadas**.

Para calendario:

- Jornada 1 = fecha civil en la que el núcleo responsable conoce, considera cierta y asume la muerte;
- Jornada 2 = día civil siguiente;
- Jornada 3 = segundo día civil siguiente.

El luto formal concluye al terminar la Jornada 3.

La noticia tardía no consume jornadas anteriores.

La cremación puede retrasarse sin extender automáticamente el luto.

---

## 16. Contratos y obligaciones

Un contrato puede utilizar:

- fecha concreta;
- hora concreta;
- número de días;
- semanas;
- meses;
- años;
- ventana temporal.

Debe registrarse el significado exacto.

Ejemplo:

`pagar el 5 de cada mes`

no equivale a:

`pagar cada 30 días`.

---

## 17. Meses civiles

Para una obligación mensual:

- se intenta conservar el número de día;
- si el mes destino no contiene ese día, se usa el último día.

Ejemplo:

`31 de enero + 1 mes = 28 de febrero`

---

## 18. Alquiler

Los alquileres pueden pactarse:

- por día;
- semana;
- mes;
- estación;
- año;
- periodo concreto.

Punto 12 no crea una frecuencia obligatoria.

El calendario solo permite expresarla sin ambigüedad.

---

## 19. Trabajo

Norgard no tiene una semana laboral universal de cinco días.

Un trabajo puede organizarse por:

- jornada;
- tarea;
- turno;
- viaje;
- temporada;
- disponibilidad;
- producción.

Sábado y domingo son días civiles normales salvo que una agenda concreta disponga otra cosa.

---

## 20. Mercados

Los mercados diarios de Treskal siguen activos todos los días.

Punto 12 no los convierte en mercado semanal.

Ferias o mercados especializados futuros pueden usar:

- día de la semana;
- fecha;
- periodicidad.

Deben declararse explícitamente.

---

## 21. Temporada agrícola

La fecha proporciona contexto estacional.

No fija automáticamente:

- siembra;
- cosecha;
- parto de ganado;
- vendimia.

Esos procesos dependen además de:

- región;
- clima;
- cultivo;
- disponibilidad;
- World State.

---

## 22. Gastronomía

FOOD puede consumir:

- fecha;
- estación;
- temperatura;
- almacenamiento.

Una receta no aparece porque «sea otoño».

La estación solo puede modificar disponibilidad plausible.

---

## 23. Navegación y pesca

Fecha/estación puede influir en:

- luz;
- condiciones habituales;
- demanda;
- actividad.

No sustituye:

- clima;
- viento;
- mar;
- visibilidad;
- estado del puerto.

---

## 24. Agenda

AGEN ya puede registrar:

- `15375-10-18T16:30:00`;
- `15375-10-18`;
- `tarde del 18 de octubre`;
- una ventana temporal.

El formato humano puede ser flexible.

El World State debe conservar una representación no ambigua cuando exista obligación real.

---

## 25. Expresiones relativas

Al crear consecuencias persistentes:

- «mañana» se resuelve a fecha;
- «el lunes» se resuelve a un lunes concreto;
- «en dos semanas» se resuelve a fecha;
- «esta tarde» se resuelve a ventana del día actual.

No debe persistirse únicamente texto ambiguo.

---

## 26. Festividades

Norgard no importa las festividades de la Tierra.

No existen por defecto:

- Navidad;
- Semana Santa;
- santos;
- fiestas religiosas terrestres.

Punto 12 tampoco obliga a inventar un calendario nacional lleno de festividades.

---

## 27. Celebraciones propias

Pueden existir eventos:

- locales;
- de Gran Casa;
- civiles;
- históricos;
- familiares;
- profesionales;
- comerciales.

Ejemplos de categorías válidas:

- feria;
- aniversario de fundación;
- coronación;
- victoria;
- boda;
- cumpleaños;
- celebración de cosecha;
- conmemoración de muerte;
- apertura extraordinaria de mercado.

Solo son canon cuando están definidos o nacen de World State.

---

## 28. Eventos dinámicos

Una partida puede crear aniversarios históricos.

Ejemplo:

una coronación ocurrida el:

`9 de abril de 15375`

puede ser recordada el 9 de abril de años posteriores si:

- la institución;
- la población;
- o la narrativa

la conserva como acontecimiento relevante.

El calendario no crea automáticamente una fiesta.

---

## 29. Corona y Grandes Casas

La Corona o una Gran Casa puede declarar:

- jornada de celebración;
- conmemoración;
- duelo institucional;
- feria;
- cierre;
- recepción.

La declaración debe:

- existir en World State;
- tener alcance;
- tener fechas;
- tener autoridad.

No altera el calendario físico.

---

## 30. Registros

Los registros administrativos pueden utilizar fechas para:

- nacimiento;
- matrimonio;
- adopción;
- cambio de nombre;
- propiedad;
- alquiler;
- impuestos;
- sentencia;
- empleo;
- contrato;
- deuda;
- muerte;
- herencia.

La fecha registrada puede ser:

- correcta;
- incompleta;
- errónea;
- falsificada.

El evento real sigue perteneciendo a su sistema propietario.

---

## 31. Error y conocimiento

Un personaje puede:

- no saber qué día exacto nació;
- recordar mal una fecha;
- desconocer la hora;
- confundir una fecha antigua.

TIME conserva la verdad cuando el World State la conoce.

K conserva lo que sabe cada persona.

---

## 32. Calendario y religión

Los nombres de meses y días son etiquetas civiles en castellano para el juego.

No implican:

- Jano;
- Marte;
- Mercurio;
- Júpiter;
- Venus;
- Saturno;
- Sol;
- Luna;
- santoral.

Nimroel sigue sin dioses.

---

## 33. Objetos de medición — resuelto por Punto 13

Punto 13 cierra la cultura material temporal de Norgard:

- **no existen relojes**;
- no existen relojes de torre, bolsillo o pulsera;
- relojes de agua o arena no funcionan como sistema civil de hora;
- no existe una red urbana de relojes de sol;
- las campanas son señales, no relojes horarios.

El motor puede conocer la hora exacta aunque una persona no disponga de instrumento capaz de medirla.

Los personajes se orientan mediante luz, posición del sol, rutina, comidas, guardias, señales y experiencia.

---

## 34. IA

La IA puede hablar de tiempo con la precisión que su personaje razonablemente conoce.

No puede:

- mover la fecha;
- adelantar una cita;
- declarar festivo un día;
- inventar un aniversario;
- afirmar que es domingo si el motor indica otro día.

---

## Regla final

**Norgard utiliza un calendario deliberadamente igual de fácil de leer que el nuestro: enero sigue a diciembre, lunes sigue a domingo y la dificultad del mundo está en vivir esos días, no en aprender a contarlos.**

`CALENDAR_POINT_12_CLOSED_NORGARD_CIVIL_CALENDAR`
