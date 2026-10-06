# Treskal — operación del puerto civil y muelles fluviales v0.1

## Estado

**DISEÑO DE SIMULACIÓN APROBADO — OPERACIÓN CIVIL**

## Objetivo

Definir el funcionamiento cotidiano de:

- T01 interfaz fluvial;
- Z02/Z03 muelles y transferencia;
- Z09 frente pesquero;
- T07/Z10 Puerto de Treskal.

Este documento no define la cadena de mando interna de los Astilleros Reales.

---

# 1. Sistemas diferenciados

Treskal mantiene dos sistemas civiles conectados:

## Sistema fluvial

Para:

- pequeñas embarcaciones mercantes;
- pescado de río;
- carga interior;
- transferencia río-tierra.

## Sistema marítimo

Para:

- pesca marítima;
- embarcaciones civiles;
- mercantes;
- transporte;
- carga y descarga.

La desembocadura los conecta, pero no los convierte en el mismo tipo de navegación.

---

# 2. Ciclo de una embarcación civil

Una visita relevante puede recorrer:

1. aproximación;
2. espera si no hay espacio o las condiciones no permiten entrar;
3. asignación de punto de atraque o zona operativa;
4. amarre;
5. descarga/carga;
6. permanencia;
7. preparación de salida;
8. partida.

No toda embarcación necesita completar todas las fases con simulación detallada fuera de la escena del jugador.

---

# 3. Aproximación

La entrada depende de:

- tamaño;
- calado;
- viento;
- oleaje;
- estado de la desembocadura;
- tráfico;
- World State.

No se presupone que cualquier nave pueda remontar el tramo fluvial urbano.

---

# 4. Espera

Una embarcación puede tener que esperar por:

- temporal;
- congestión;
- marea o condición local si el futuro modelo hidrológico la requiere;
- reparación;
- falta de espacio;
- orden de descarga.

La forma concreta de fondeo exterior no se fija hasta cartografía litoral detallada.

---

# 5. Atraque

Cada punto de operación debe ser compatible con:

- tamaño;
- función;
- carga;
- seguridad.

No existe un “muelle universal”.

Pueden existir zonas preferentes para:

- pesca;
- mercancía general;
- pequeñas embarcaciones fluviales;
- reparación;
- carga especializada.

---

# 6. Descarga

La descarga crea una cadena:

**barco → muelle → trabajadores → carro/almacén/mercado**

El destino depende de la mercancía.

Ejemplos:

- pescado → S07 / distribución rápida;
- mercancía comercial → almacén o comerciante;
- material voluminoso → T02 o instalación concreta.

---

# 7. Carga

La carga de salida puede proceder de:

- T02;
- T04;
- mercado;
- comerciantes;
- almacenes;
- productores.

No toda exportación pasa por Plaza del Abasto.

---

# 8. Registro de mercancía

Las operaciones de volumen relevante deben poder generar:

- origen;
- propietario;
- cantidad agregada;
- almacén/destino;
- barco;
- estado.

No es necesario rastrear cada pieza individual si carece de importancia jugable.

---

# 9. Pescado

La pesca tiene prioridad de rapidez.

Cadena preferente:

**barco → descarga → Lonja del Pescado → venta / conservación / distribución**

El tiempo afecta:

- calidad;
- precio;
- desperdicio.

---

# 10. Tripulación

Una tripulación puede:

- permanecer a bordo;
- bajar a puerto;
- comprar;
- comer;
- beber;
- dormir en posada;
- contratar servicio.

Su presencia alimenta V03/V04 y población flotante.

---

# 11. Reparación

Una nave civil puede necesitar:

- carpintería;
- calafateo u operación equivalente según tecnología;
- reparación de aparejos;
- metal;
- provisiones.

La reparación utiliza capacidades de T07 y proveedores de la ciudad.

No convierte T07 en los grandes astilleros civiles del territorio.

---

# 12. Mercante importante

D07 puede provocar:

- más trabajadores;
- comerciantes;
- carros;
- stock nuevo;
- rumores;
- ocupación de posadas.

La mercancía debe corresponder a:

- origen;
- ruta;
- propósito.

---

# 13. Salida

Antes de partir pueden resolverse:

- carga;
- suministros;
- reparaciones;
- tripulación;
- documentación;
- obligaciones portuarias o aduaneras abiertas.

El sistema fiscal vigente distingue:

- **carga interna de Norgard**: sin aduana por origen, aunque puede pagar servicios portuarios;
- **carga que cruza frontera fiscal exterior**: circuito aduanero cuando corresponda;
- **pesca local/interna**: no es importación, aunque puede pagar servicios de desembarco/lonja;
- **operación oficial de la Corona/T08**: fuera de la potestad tributaria Valrik.

El control se integra en T07 y no exige una Casa de Aduanas singular independiente.

---

# 14. Muelles fluviales

T01 maneja principalmente:

- carga interior;
- pescado fluvial;
- embarcaciones pequeñas;
- transferencia a carros.

No debe saturarse con embarcaciones marítimas incompatibles.

---

# 15. Congestión

La congestión es local.

Puede afectar:

- tiempo de descarga;
- disponibilidad de trabajadores;
- carros;
- espacio de almacén.

No paraliza automáticamente toda la ciudad.

---

# 16. Temporal

D01 puede causar:

- cancelación de salida;
- reducción de pesca;
- amarres reforzados;
- cierres parciales;
- daños;
- retrasos.

Las consecuencias pueden continuar después de mejorar el tiempo.

---

# 17. Crecida

D02 afecta más a:

- T01;
- muelles bajos;
- tráfico fluvial.

No implica automáticamente cierre marítimo completo de T07.

---

# 18. Astilleros Reales

El tráfico civil no atraviesa T08 libremente.

Los materiales destinados a la Corona siguen corredores autorizados.

La operación portuaria civil puede interactuar logísticamente con T08 sin compartir autoridad.

---

## Regla final

**El puerto de Treskal funciona como una cadena física de barcos, trabajadores, carros, almacenes y comerciantes; la mercancía no aparece directamente en una tienda al llegar un barco.**
