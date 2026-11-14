# E19-R2.04 — Dinámica estacional del agua y riesgos por cadena causal

## Balance de conservación
Para una cuenca en un intervalo: **precipitación líquida + deshielo + aportes entrantes + descarga subterránea = escorrentía saliente + evapotranspiración + infiltración neta exportada + cambio de almacenamiento**, con entradas y salidas subterráneas contabilizadas una sola vez. Esta ecuación es **conceptual**: no hay mm de lluvia, km², litros/segundo ni duración de estaciones verificadas. El agua no puede surgir por un evento narrativo sin fuente ni desaparecer por cruzar el borde de una escena 2D.

## Seis estados de proceso observables a diseñar
1. **Recarga húmeda:** lluvia efectiva aumenta humedad del suelo si capacidad/infiltración lo permiten; no convierte todos los cauces en permanentes.
2. **Tormenta concentrada:** alta intensidad en cabecera/abanico permite crecida rápida, arrastre y erosión; su área afectada depende del cauce real.
3. **Acumulación de nieve:** solo con frío y precipitación compatibles por altura y microclima; la franja norte no está nevada siempre.
4. **Deshielo o lluvia sobre nieve:** aporte rápido/retardado según temperatura, cubierta, suelo helado y capacidad de salida; no copiar calendario terrestre.
5. **Estiaje:** baja el flujo de base si la recarga disminuye; un cauce efímero puede secarse sin romper su identidad persistente.
6. **Infiltración y descarga:** depósitos de pie de monte pueden perder caudal superficial, alimentar acuíferos o liberar surgencias; nunca cerrar el balance con agua invisible no trazada.

## Evaluación de peligros, nunca desastres consumados
| Riesgo condicional | Desencadenante | Terreno susceptible | Exposición a demostrar | Mitigación investigable |
|---|---|---|---|---|
| avenida torrencial | tormenta/deshielo intenso | HC-01/HC-06 barranco con energía | senda/edificio real junto al cauce | no ubicar en cauce activo |
| erosión del abanico | transporte sólido | HC-02 salida y depósitos sueltos | cultivo/obra verificada | conservar cubierta y salida |
| anegamiento | lluvia persistente o nivel alto | HC-03/04/05 concavidad poco drenante | viña, vivienda o bosque legal | evaluar suelo y drenaje |
| helada/hielo | temperatura y agua superficiales compatibles | HC-05/07 zona húmeda | camino existente, cultivo | señalización y previsión |
| estiaje/estrés hídrico | déficit de entradas/almacenaje | cualquier HC según acuífero | abastecimiento o viñedo activo | demanda y reserva verificadas |
| contaminación por escorrentía | carga transportada + conexión | ladera/acequia real y receptor | captación/uso humano | franjas protectoras y saneamiento |

En E03 ya se separaron **amenaza → susceptibilidad → exposición → vulnerabilidad**. R2 mantiene ese orden; no genera un suceso histórico ni cierra un camino. Las diez familias de riesgo E13 permanecen como referencias de estudio, no frecuencias de evento.

## Memoria de la simulación futura
Identidad de cauce y clase de cuenca son datos estables de contenido; **caudal presente, nivel, hielo, humedad, actividad temporal y sedimento** son estado dinámico futuro con fecha/calendario. Una actualización no cambia por sí sola la jurisdicción, posición o nombre canónico. Se necesita continuidad entre visitas y guardar/cargar: nunca tirar un dado nuevo y hacer aparecer un río distinto en el mismo valle.

## Escenarios adversariales
Río permanente sin recarga regular; crecida sin lluvia/nieve/afluencia; nieve perpetua en Rodas por pertenencia septentrional; humedal en cresta seca; fuente inagotable sin balance; lago Antela con salida que precede a su entrada; acuífero que descarga en ambas laderas sin conectar estructura geológica; secado que elimina el ID; sequía que automáticamente habilita riego no autorizado. Todos deben bloquear materialización.
