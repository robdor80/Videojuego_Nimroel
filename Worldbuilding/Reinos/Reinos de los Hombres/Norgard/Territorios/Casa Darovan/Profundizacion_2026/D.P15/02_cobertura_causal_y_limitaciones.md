# D.P15 — Política de cobertura, capacidad y cola

**Regla principal:** necesidad de un habitante ≠ prestación garantizada. Una solicitud pasa por: identidad y conocimiento → necesidad → derecho/legalidad → desplazamiento físico válido → proveedor existente → capacidad, herramientas y stock → espera/atención → mutación del motor.

## Casos de planificación

| Contexto | Qué investigar | Qué no afirmar |
|---|---|---|
| Treihord | suministro industrial, salud laboral, Crisol, custodia y movilidad, ocho barrios canónicos | hospitales modernos universales, nuevos barrios o cambios en 32.000 habitantes |
| Veldora | almacenamiento, inspección de comercio exterior, higiene de muelles, alojamiento y oficios | aduanas entre Casas, muelles nuevos o su capacidad |
| Taramin | residuos pesqueros, agua, empleo marítimo y acceso de descarga desde zona pesquera principal | puente o navegación de brazos Thalen, capturas o flotas |
| Syvaris | refugio en bahía, abastecimiento insular, cuidados, presencia de Armada Real | rutas regulares, armada Darovan, muelles de calas |
| Arven | aldeas costeras existentes y Manto Verde ~90 %, equilibrios de abastecimiento | quinta ciudad, nuevas aldeas o tala intensiva |
| Agujas | interior sin residencia permanente | puestos fijos dentro del bosque |
| La Linde | servicio posible del corredor de camino donde se confirme acceso y demanda | posada ya existente ni horario de convoy |
| Pilares | explotación forestal documentada y recuperación | un segundo bosque, aserraderos/aldeas sin autorización |

## Orden de resolución

1. Obtener `SettlementInstance` persistido y `ServiceProvider` existente si algún día hay runtime.
2. Comprobar que el proveedor **puede** cubrir la demanda: suministros, agenda, capacidad, habilidad y derecho de acceso.
3. Calcular coste y ruta solamente desde grafo físico **comprobado**, no de un vínculo económico.
4. Si no hay capacidad, mantener pendiente/espera/carencia sin instanciar magia.
5. Persistir deltas únicamente en CoreRPG; narrativa IA puede describirlos pero nunca certifica prestaciones no ejecutadas.

## Traspaso

Las cifras de población aprobadas son **bandas**, salvo el ancla aproximada de Treihord; no equivalen a plantilla de guardia, número de tiendas, camas ni número de curanderas. `UNKNOWN` permanece. D.P16 consumirá este modelo para las cuatro ciudades manuales.
