# E13 → E14 — Traspaso operativo de habitabilidad y ocupación
**No se inicia E14 en esta rama.** Este documento establece entradas, criterios y secuencia para la siguiente conversación.

## Entradas disponibles
1. Siete IDs E01 fijos y siete perfiles E13 de paisaje, clima/agua/suelo. El perfil de extremo norte es NON-APPLICABLE hasta cerrar EDD-01.
2. Referencias altitudinales de prototipo, con banderas NOT_MEASURED y NO_GEOREFERENCE; no son cotas de celdas.
3. Seis expedientes de cuenca con receptores UNKNOWN; ninguna hidrografía local validada.
4. Diez riesgos condicionales y registros de aptitud UNASSESSED; ninguno activa desastre.
5. Dorth, Lumina, Karsath, Rodas (aldea real), Hallheim fuera; cuatro preguntas de ruta sin aristas.
6. Herramienta Tools/EdranorE13/validate.py, contrato físico y esquema SVG semántico.
7. Autoridad de reglas compartidas Core/Defaults, no copiar ecosistemas ni mapas Darovan/Valrik.

## Trabajo a ejecutar en E14
- Crear **unidades de habitabilidad por reglas**, no polígonos cartografiados si siguen sin puntos de control.
- Separar asentamiento permanente, estación de trabajo, explotación agrícola/forestal, paso temporal y zona excluida.
- Cruzar suelo, pendiente, protección de bosque, agua, acceso, peligro y derechos de propiedad; un buen suelo sin agua o derechos no significa asentamiento viable.
- Para cada U1–U6: proponer 3–5 combinaciones de entorno/habitabilidad y 3 escenarios negativos; U7 marcado NO_EVALUABLE.
- Priorizar entorno Dorth–Lumina–Karsath y contacto rural de Rodas, sin decidir números de habitantes ni introducir poblaciones dentro del enclave regio por inferencia.
- Entregar registro de capacidad y limitaciones para E15, E16, E19 y E26. Toda densidad, hectárea o intervalo poblacional debe tener procedencia y autoridad.

## Criterios de aceptación propuestos
**H01** siete IDs completos; **H02** cinco anclas protegidas; **H03** EDD-01/02 visibles; **H04** ningún cultivo boreal por defecto; **H05** sin construcción/uso en bosque protegido sin derechos; **H06** ningún camino/arroyo declarado por aptitud; **H07** escenarios de riesgo causales; **H08** clasificación de ocupación legible y condicionada; **H09** validación de errores y matriz de fuentes; **H10** no materialización en CoreRPG/Godot sin prueba real.

## Orden de arranque de la próxima conversación
Leer PR/merge E13 y HEAD main; revisar deudas; crear rama E14; preparar atlas de habitabilidad con reglas, contrato y tests; publicar PR, validar y auditar; solo fusionar si autorización y gates se satisfacen. Mantener E15 sin iniciar.
