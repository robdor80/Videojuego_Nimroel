# E19-R4.01 — Gramática viaria y los tres grafos
**Diseño delegado B2; ninguna arista de la red física está acreditada.**

## 1. Orden causal
Relieve MF → drenaje HC y cruces de cauce comprobados → suelo SO, cubierta CV y memoria ES → demanda productiva/servicios E15–E17 → alternativas de trazado → derecho y conservación → inspección del terreno → **Gp validado** → viaje y estado. Una ruta no se inventa para transportar barricas ni para permitir una misión.

## 2. Grafos distintos
- **Gd DEMAND:** pares de actividad, necesidad, suministro o comunicación, incluso sin camino. Ejemplo: vino de Dorth destinado a compradores; no fija a quién, por dónde ni cómo.
- **Gq QUESTION:** preguntas investigables con extremos conceptuales. E05 reconoce Dorth–Lumina, Lumina–Karsath, Dorth–Karsath y Dorth–Rodas, con precauciones distintas. Un Gq puede quedar sin solución física.
- **Gp PHYSICAL:** aristas continuas levantadas y autorizadas, con geometría, cruces, propietario/servidumbre, clase, modo, capacidad, mantenimiento y proveniencia. **Gp = 0 aristas** ahora y no permite calcular rutas.

La adyacencia natural MF-01→MF-02 no es adyacencia transitable. En especial, MF-08 no es nodo evaluable. No se puede tomar un grafo Gq, asignarle peso arbitrario y llamarlo navegación.

## 3. Ocho clases de diseño TC, no calzadas asignadas
| ID | Clase | Criterio de función | Condición física y prohibición |
|---|---|---|---|
| TC-01 | eje territorial de abastecimiento | conecta nodos comprobados; carros y peatones según ancho | continuidad, fondo, seguridad, cruce y mantenimiento levantados |
| TC-02 | vía rural de vendimia | comunica parcelas reales y recepción legítima | no nace de una etiqueta de vino; conserva muros/suelos |
| TC-03 | servicio forestal condicionado | extracción y labores autorizadas | permiso de corta NO equivale a derecho de camino |
| TC-04 | senda local peatonal | residentes, pastores, mensajeros a pie | no implica aptitud de carro ni uso público |
| TC-05 | acceso de montaña o collado | cruza un relieve transitable demostrado | no fija collado ni traspasa jurisdicción por conjetura |
| TC-06 | paso de agua o acceso ribereño | solo donde existe cruce corroborado | sin puente/vado/barca automática |
| TC-07 | enlace institucional controlado | Corona, guardia, mensajería autorizada | no es peaje ni puesto militar instalado |
| TC-08 | ramal de servicio y emergencia | reparación/evacuación de núcleos probados | no crea redundancia ni capacidad donde no la hay |

Cada futura entidad física puede ejercer varias funciones, pero deberá tener **una identidad estable de tramo** y restricciones por modo y momento. TC es un catálogo de tipos, no una enumeración de obras existentes.

## 4. Jerarquía de decisiones
1. Identificar necesidad y procedencia E05/E16/E17.
2. Determinar si conecta puntos realmente localizables, sin usar distancias imaginadas.
3. Descartar inmediatamente jurisdicción ajena no autorizada, MF-08 y protección forestal incompatible.
4. Exigir continuidad de pendientes y soporte suficiente para el modo propuesto.
5. Resolver cuencas, cauces y receptores, sin multiplicar cruces.
6. Comparar fragilidad y riesgos locales, incluida ruta alternativa **si la hay**.
7. Probar servidumbre, derechos de ribera, acceso a bosque o acuerdo regio.
8. Verificar capacidad estacional e inspección de campo.
9. Solo entonces promover tramos a Gp; recalcular disponibilidad con estado dinámico.

## 5. Red y resiliencia
Una red con una sola vía certificada puede ser frágil; no se la duplica por diseño. Una necesidad de mercancía puede esperar, cambiar de modalidad cuando exista otra, o cancelarse por inaccesibilidad. Una arista desconocida **no se presume cerrada**: sencillamente no se puede planificar con ella. Un cierre real requiere entidad y evento; conocimiento desactualizado del jugador no cambia el mundo. Las cargas pesadas deben evitar áreas cívicas o suelos vulnerables **si existe desvío probado**, jamás con circunvalación automática.

## 6. Paridad Valrik
En Treskal la red prioriza abasto, madera, puerto, militar e institucional y conserva accesos controlados. Edranor adopta el método de **finalidad, modo, conflicto y prueba**, no la geometría urbana de Treskal. No importar anchos de 6,2 m ni clases urbanas R1–R5 al territorio rural.