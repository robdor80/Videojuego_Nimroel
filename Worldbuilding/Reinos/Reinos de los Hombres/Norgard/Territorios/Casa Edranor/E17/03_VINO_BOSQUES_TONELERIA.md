# E17 — Bucles vino–madera–tonelería–mercado

**Clase de autoridad:** diseño delegado, no hecho canónico, historia consumada ni runtime. Fuente de trabajo: `main` tras E16 (`93499f466cbfb5b920b513b817c6185e727db274`). E18 no se ejecuta en esta fase.

## Vino (ED17-V01–V04)
Dorth: tinto; Lumina: blanco y mercado anual; Karsath: producción selecta reducida. Estos rasgos **no** asignan hectáreas, litros, variedades, fechas o propietarios. Pedido no impone vendimia; madurez, suelos, agua y derechos preceden a la cosecha. Dos contratos no reservan el mismo lote. Una bodega requiere recipiente seguro con identidad; feria anual no opera a diario.

## Madera y tonelería (ED17-B01–B04)
La secuencia legal es: permiso y zona real → tala si procede → curado → duelas y aros reales → montaje → verificación → recipiente apto → uso y eventual reparación. Sin autorización, el árbol no entra en inventario; sin piezas, no hay tonel terminado. Una fuga requiere contenedor concreto y pérdida trazada; una reparación mantiene `containerId` e inspección independiente antes de liberar uso.

## Bucles de retorno permitidos solo como diseño
Una rotura podría disminuir capacidad de bodega y exigir materiales; la reparación podría recuperar aptitud, **pero nunca crea el vino perdido**. La falta de toneles puede demorar una entrega sin que el sistema invente un bosque, un herrero o un almacén. Precio futuro en CLAVOS según E15, pero aquí no se proponen tarifas ni tasas.
