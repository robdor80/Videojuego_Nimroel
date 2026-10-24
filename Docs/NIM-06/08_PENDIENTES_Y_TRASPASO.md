# Pendientes y traspaso

Estado vigente y evidencia: [cierre final](12_CIERRE_FINAL.md).

## Completado

Puente funcional y persistencia de CoreRPG, según evidencia automatizada histórica
referenciada en 04/05 y la verificación actual enlazada en 12. El propietario comunica
validación funcional física satisfactoria de la versión anterior en MSI Raider Windows 11
y Samsung Galaxy Tab S9+ Android ARM64: 129/129, cero errores, consultas/acciones,
guardado/restauración, persistencia tras reabrir y no_change esperado.

Main 028ea86 integrado sin conflictos. Corregidos scroll JSON y adaptación del laboratorio.
CoreRPG, godot-cpp, motor, contratos, persistencia y autoridad conservados.

## Pendiente real de esta entrega

Comprobar físicamente la interfaz corregida: leer hasta el final de un JSON largo;
rueda/barra en Windows y arrastre en Tab S9+; legibilidad y pulsación en pantalla completa
y dividida; ausencia de solapamientos al cambiar el tamaño; volver al Host con su escala.
No se declara realizada esa comprobación ni se extrapola la prueba anterior.
Consultar la conclusión real de CI y sus enlaces en 12 antes de aceptar la entrega.
Fusión reservada al propietario. La PR permanece abierta y en borrador.

## Fuera del cierre NIM-06

Catálogo/definiciones/ContentJson, Inspector completo, grants temporales, eventos
públicos y sistemas RPG futuros conservan los límites de 02/03/06; no se desarrollan.
La cadena conversacional continúa bloqueada sin capacidad y validación de dominio.
No se inicia NIM-07 ni sincronización Windows/Android, ni se modifica IA/voz/proveedores.
No se ejecutan llamadas de pago ni pruebas masivas con ZIP.

Los paquetes de Actions tienen retención de 30 días. La clave debug Android cambia
por job; conservar los saves necesarios antes de sustituir una instalación cuya
firma difiera. No atribuir a la CI ejecución Android ni pruebas físicas del propietario.
