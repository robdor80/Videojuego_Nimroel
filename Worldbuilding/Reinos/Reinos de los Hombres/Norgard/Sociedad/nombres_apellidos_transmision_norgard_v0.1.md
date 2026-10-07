# Norgard — nombres personales, apellidos y transmisión nominal v0.1

## Estado

**CANON FUNCIONAL CERRADO — PUNTO 11**

Marcador: `NAMING_POINT_11_CLOSED_NORGARD_PERSONAL_NAMES_SURNAMES`

---

## 1. Principio general

Norgard distingue:

- identidad técnica;
- nombre legal;
- apellido;
- alias;
- apodo;
- sobrenombre;
- título;
- tratamiento social.

Compartir apellido no prueba parentesco por sí solo.

Tener parentesco no obliga a compartir apellido.

La identidad real del personaje permanece en `npc_id`.

---

## 2. Estructura nominal ordinaria

La forma legal ordinaria es:

**nombre personal + un apellido familiar**

Ejemplo estructural:

`Nombre Apellido`

Puede existir un segundo nombre personal, pero no es obligatorio ni se utiliza por defecto en conversación cotidiana.

Norgard no utiliza de forma general:

- doble apellido obligatorio;
- patronímico obligatorio;
- apellido distinto por sexo;
- apellido de bastardo;
- partícula nobiliaria obligatoria.

---

## 3. Nombre personal

Toda persona puede recibir al menos un nombre personal.

El nombre:

- no necesita rito religioso;
- no determina clase;
- no determina oficio;
- no determina Casa;
- no crea parentesco;
- no crea derecho sucesorio.

La elección puede estar influida por:

- tradición familiar;
- preferencias de los progenitores;
- memoria de familiares;
- región;
- moda;
- historia personal.

Esas influencias no crean una lista rígida por territorio.

---

## 4. Registro tras nacimiento

Un recién nacido puede permanecer brevemente como NAME02 si todavía no ha sido nombrado.

Cuando se registra el nombre:

- se conserva el mismo `npc_id`;
- se crea NAME01;
- el nacimiento y la filiación siguen siendo los mismos hechos.

No existe bautismo ni rito religioso obligatorio.

---

## 5. Apellido legal

Cada persona posee como máximo **un apellido legal vigente**.

Puede conservarse durante toda la vida o cambiar mediante acto válido.

El apellido:

- identifica una línea familiar o tradición nominal;
- no demuestra por sí solo sangre;
- no demuestra nobleza;
- no demuestra legitimidad;
- no concede propiedad;
- no concede título;
- no concede cargo.

---

## 6. Apellido de nacimiento — un progenitor jurídico

Si al registrar el nacimiento existe un solo progenitor jurídico reconocido, el menor recibe por defecto el apellido legal vigente de ese progenitor.

Si posteriormente se reconoce un segundo progenitor:

- el apellido no cambia automáticamente;
- puede solicitarse cambio conforme a las reglas generales.

Esto evita reescribir retrospectivamente la identidad del menor.

---

## 7. Apellido de nacimiento — dos progenitores jurídicos

Si existen dos progenitores jurídicos reconocidos en el momento del registro:

- pueden elegir de común acuerdo el apellido vigente de cualquiera de los dos;
- no se combinan automáticamente ambos;
- no se crea automáticamente un apellido doble.

La elección no modifica la filiación.

---

## 8. Falta de acuerdo

Si existen dos progenitores jurídicos y no logran acordar el apellido en el momento del registro, se utiliza provisionalmente el apellido de la persona que dio a luz.

Esta regla:

- es procedimental;
- no concede mayor autoridad parental;
- no altera derechos del otro progenitor;
- puede revisarse después mediante cambio válido.

Se utiliza porque el vínculo de parto es el dato jurídico disponible directamente desde PREG.

---

## 9. Filiación desconocida

Si ningún progenitor jurídico es conocido o registrable:

- el menor recibe un nombre personal;
- la autoridad asigna un apellido ordinario no protegido;
- no se utiliza un apellido que marque bastardía, abandono u orfandad.

Ese apellido puede convertirse en su apellido familiar real.

No crea una falsa relación con una familia concreta.

---

## 10. Nacimiento fuera de matrimonio

Norgard no posee un sistema de apellidos de bastardo.

Un hijo nacido fuera de matrimonio:

- usa las mismas reglas nominales que cualquier otro menor;
- no recibe marca pública obligatoria de ilegitimidad;
- no pierde protección civil;
- no pierde derechos sucesorios civiles ordinarios cuando la filiación está reconocida.

Las reglas especiales Aethros siguen separadas.

---

## 11. Matrimonio

Casarse **no cambia automáticamente el apellido** de ninguno de los cónyuges.

Cada persona puede:

- conservar su apellido;
- solicitar adoptar el apellido legal del cónyuge;
- volver a cambiarlo posteriormente mediante acto válido.

Ningún sexo tiene prioridad.

El matrimonio no crea un apellido común obligatorio.

---

## 12. Disolución, nulidad y viudedad

La terminación del matrimonio no cambia automáticamente el apellido.

Una persona que hubiera adoptado el apellido del cónyuge puede:

- conservarlo;
- recuperar un apellido anterior;
- solicitar otro cambio permitido.

La muerte del cónyuge tampoco obliga a recuperar el apellido anterior.

---

## 13. Cambio voluntario de apellido

Una persona con plena capacidad civil puede solicitar cambio de nombre o apellido.

Requisitos:

- identidad demostrable;
- registro del cambio;
- trazabilidad del nombre anterior;
- ausencia de fraude suficiente para impedir el cambio o para conservar responsabilidad.

El cambio no borra:

- deudas;
- delitos;
- obligaciones;
- contratos;
- propiedad;
- parentesco;
- matrimonio;
- filiación;
- herencia ya nacida.

El nombre anterior queda como NAME03.

---

## 14. Cambio de nombre de menores

Un menor puede cambiar de nombre o apellido mediante:

- solicitud de quien tenga autoridad parental o tutela;
- causa razonable;
- registro válido;
- intervención de autoridad cuando exista conflicto.

El menor con madurez suficiente debe ser escuchado.

La preferencia del menor pesa más conforme aumenta su autonomía.

---

## 15. Adopción

La adopción no borra automáticamente el nombre previo.

La resolución de adopción puede:

- mantener el apellido existente;
- cambiarlo al apellido de uno de los adoptantes;
- establecer otro apellido permitido por la ley.

Cuando el menor tenga madurez suficiente, debe ser escuchado.

El nombre anterior permanece en el historial NAME.

---

## 16. Adopción y sangre

Adoptar el apellido de una familia:

- crea identidad nominal;
- puede reflejar integración jurídica;
- no crea sangre biológica;
- no crea automáticamente derechos dinásticos;
- no crea automáticamente un título.

Punto 6 y Punto 8 conservan autoridad sobre filiación y herencia.

---

## 17. Hijastros

El matrimonio con un progenitor no cambia automáticamente el apellido del hijo previo.

El padrastro o madrastra:

- no puede imponer su apellido solo por matrimonio;
- puede participar en un cambio si existe adopción o resolución válida.

---

## 18. Hermanos

Los hermanos pueden tener apellidos diferentes por:

- progenitores distintos;
- reconocimiento posterior;
- adopción;
- cambios legales;
- decisiones nominales diferentes.

KIN conserva el parentesco.

El motor no debe asumir que apellidos distintos significan que no son hermanos.

---

## 19. Apodos y sobrenombres

Son comunes y pueden surgir de:

- carácter;
- aspecto;
- oficio;
- lugar;
- hazaña;
- reputación;
- costumbre familiar.

Ejemplos estructurales:

- `Nombre el Rojo`;
- `Nombre del Vado`;
- `Nombre el Carpintero`.

No se convierten automáticamente en apellido legal.

Pueden persistir durante años como NAME04.

---

## 20. Apellidos ordinarios y origen histórico

Muchos apellidos de Norgard pueden haber surgido históricamente de:

- antepasados;
- lugares;
- oficios;
- rasgos;
- sobrenombres;
- antiguos hogares.

En el presente funcionan como apellidos hereditarios ordinarios.

El significado histórico no obliga al descendiente a:

- vivir en ese lugar;
- ejercer ese oficio;
- poseer ese rasgo.

---

## 21. Apellido y hogar

Hogar y apellido son sistemas distintos.

Un hogar puede contener:

- un solo apellido;
- varios apellidos;
- cónyuges con apellidos distintos;
- hijos con apellido de uno de ellos;
- adoptados con apellido previo;
- otros familiares.

RES/household no reescribe NAME.

---

## 22. Grandes Casas — apellidos protegidos

Los nombres:

- **Aethros**;
- **Darovan**;
- **Edranor**;
- **Galdren**;
- **Valrik**

son apellidos dinásticos protegidos.

El generador procedural ordinario no puede asignarlos.

Portar uno de estos apellidos requiere una relación jurídica o dinástica válida con la Casa correspondiente.

---

## 23. Matrimonio con una Gran Casa

Casarse con un miembro de una Gran Casa:

- no concede automáticamente el apellido de la Casa;
- no concede señorío;
- no concede sangre;
- no concede derecho sucesorio especial.

Cualquier adopción formal del apellido protegido requiere acto expreso conforme a la Casa y a la autoridad competente.

---

## 24. Adopción dentro de una Gran Casa

Una adopción válida puede integrar jurídicamente a una persona en una familia de Gran Casa.

El uso del apellido protegido:

- requiere que la resolución lo establezca expresamente;
- no crea sangre;
- no altera por sí solo la sucesión de títulos cuya regla exija sangre.

La Casa Aethros mantiene además su régimen especial.

---

## 25. Casa Aethros

Se conserva íntegramente el canon previo:

- el soberano de la línea reinante usa **Aethros**;
- los hijos legítimos del monarca usan **Aethros**;
- ramas secundarias pueden usar otros apellidos;
- si una rama secundaria accede legítimamente a la Corona, el nuevo monarca restablece/adopta formalmente **Aethros**;
- sus hijos legítimos usan **Aethros**.

El sistema general de nombres no puede anular estas reglas.

La adopción no crea sangre Aethros.

---

## 26. Grandes Casas no reinantes

Darovan, Edranor, Galdren y Valrik funcionan como apellidos dinásticos de sus familias principales.

El apellido de Casa:

- identifica pertenencia familiar reconocida;
- no convierte automáticamente a cada portador en Lord/Lady;
- no concede automáticamente el señorío;
- no sustituye la sucesión de la Casa.

Las ramas secundarias pueden mantener el apellido o adoptar otro si el canon futuro de esa familia lo establece.

---

## 27. Títulos y tratamientos

No forman parte del apellido:

- Rey;
- Reina;
- Rey Consorte;
- Lord;
- Lady;
- capitán;
- maestro;
- otros cargos.

Formato formal posible:

`Lord Nombre Valrik`

o:

`Nombre Valrik, Lord de la Casa Valrik`

El título se resuelve por autoridad institucional, no por NAME.

---

## 28. Homónimos

Norgard puede tener personas con:

- mismo nombre personal;
- mismo apellido;
- mismo nombre completo.

No se fuerzan nombres artificiales para garantizar unicidad.

El motor distingue mediante `npc_id`.

Cuando sea necesario, el habla puede desambiguar mediante:

- oficio;
- parentesco;
- barrio;
- procedencia;
- edad;
- sobrenombre.

---

## 29. Escritura y alfabetización

Una persona puede poseer nombre legal aunque no sepa escribirlo.

Los registros pueden:

- ser escritos por escribano;
- contener errores;
- perderse;
- reconstruirse.

La ortografía documental no sustituye la identidad oral.

---

## 30. Variación ortográfica

Pueden existir variantes menores en documentos antiguos o poco fiables.

El World State puede distinguir:

- forma legal actual;
- variante documental;
- error;
- alias.

No se crean NPC distintos por una diferencia ortográfica cuando la evidencia identifica a la misma persona.

---

## 31. Generación procedural

Para NPC humanos de Norgard:

- Nivel A → nombre autoral;
- Nivel B → nombre completo persistente;
- Nivel C → `name_seed` latente.

En C→B:

1. se conserva `npc_id`;
2. se deriva `name_seed`;
3. se consulta KIN/filiación;
4. se aplica transmisión de apellido;
5. se elige nombre personal compatible con el repertorio;
6. se crea NAME01;
7. no se rerollea.

Si el NPC ya había revelado un nombre, esa observación es vinculante.

---

## 32. Generación familiar

El motor debe generar primero:

- parentesco;
- situación jurídica;
- hogar.

Después resuelve apellido.

No puede generar por separado:

- madre `X`;
- padre `Y`;
- hijo con apellido aleatorio `Z`

si la ley exige herencia nominal desde un progenitor.

---

## 33. Variación regional

Existe una sonoridad humana común de Norgard.

Las regiones pueden sesgar:

- ciertos sonidos;
- terminaciones;
- frecuencia de algunos nombres.

No existen cinco lenguas personales distintas por Gran Casa.

Un nombre frecuente en Valrik puede aparecer en Darovan por:

- migración;
- parentesco;
- moda;
- comercio;
- elección familiar.

---

## 34. Nombres reservados

Los nombres autorales importantes pueden marcarse como reservados.

El generador no los utiliza por defecto.

Esto evita que un NPC procedural banal comparta nombre con una figura única del canon cuando esa duplicación perjudique legibilidad.

La reserva es de producción, no una prohibición cultural absoluta.

---

## 35. IA

La IA puede usar:

- nombre conocido;
- apellido conocido;
- apodo conocido;
- título conocido.

No puede:

- inventar apellido;
- revelar un apellido no conocido;
- convertir un apodo en nombre legal;
- asumir parentesco por apellido;
- adjudicar apellido de Gran Casa;
- cambiar apellido por matrimonio sin evento;
- renombrar un NPC para resolver una escena.

---

## 36. Interacción con herencia

La herencia se determina por:

- filiación;
- matrimonio;
- testamento;
- reglas legales.

No por apellido.

Cambiar apellido no elimina ni crea derechos hereditarios.

---

## 37. Interacción con reputación

Un apellido puede influir socialmente si es conocido.

Eso puede afectar:

- REP;
- expectativas;
- reacción social.

Pero el efecto procede del conocimiento/reputación real de ese apellido, no de una bonificación universal del sistema NAME.

---

## 38. Registros

Pueden existir registros de:

- nacimiento;
- cambio de nombre;
- matrimonio;
- adopción;
- filiación;
- muerte;
- genealogía noble.

El nombre sirve para localizar personas en documentos, pero `npc_id` conserva autoridad técnica.

---

## 39. No definido aquí

Punto 11 no define:

- calendario;
- día exacto de imposición de nombre;
- festividades nominales;
- onomástica religiosa;
- lenguas élficas;
- nombres de otros pueblos;
- títulos futuros de Casas menores.

No existen dioses ni santoral.

---

## Regla final

**En Norgard un apellido ayuda a contar de dónde viene una persona, pero no decide quién es, quiénes son sus padres ni qué derechos posee: esos hechos pertenecen al World State y a la ley.**

`NAMING_POINT_11_CLOSED_NORGARD_PERSONAL_NAMES_SURNAMES`
