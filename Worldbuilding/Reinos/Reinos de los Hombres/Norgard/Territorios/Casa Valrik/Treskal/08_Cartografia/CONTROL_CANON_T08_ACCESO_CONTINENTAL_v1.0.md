# Treskal — control canónico de acceso continental del Complejo Naval Real

**Estado:** OBLIGATORIO para todos los mapas e imágenes de Treskal.  
**Fecha de aclaración:** 2026-10-08.  
**Naturaleza:** aclaración geométrica y logística; NO cambia la geometría canónica cerrada.

## Veredicto del canon

**T08 (S08 Astilleros Reales + S13 Base Naval Principal) NO ES UNA ISLA.**

T08 pertenece a la **misma masa terrestre continental** que el resto de Treskal y su territorio oriental. **La lectura visual canónica preferente es una línea de costa continental continua, ligeramente curvada**, con las instalaciones S08/S13 extendidas a lo largo de ella. **No existe obligación de península**. La mera posibilidad de un saliente litoral no autoriza inventarlo: solo sería admisible si está sustentado por la línea costera métrica original y mantiene una unión terrestre real, ancha y suficiente.

## Justificación cartográfica

- En el contrato geográfico la costa oriental forma una línea continental continua con curva suave; **no hay una península naval destacada en la geometría base** ni se define ningún canal tras T08.
- El polígono T08 tiene superficie terrestre y un frente naval de 940 m en la costa oriental, no contorno insular.
- Entre T07 y T08 hay una franja costera T04 de 260 m; no un estrecho marino.
- La red de abastecimiento C05 entra por tierra a T08 desde la retaguardia este/noreste.
- La vía interna C16 permite la circulación terrestre pesada hacia S08 y S13.
- Los gradas, muelles, atraques y el rompeolas se proyectan desde esa costa continental; no rodean T08 por la retaguardia.

## Esquema conceptual, NO sustituto de geometría

```text
        INTERIOR / RESTO DEL TERRITORIO (tierra firme)
                  || CAMINOS TERRESTRES ||
                 C05 — acceso controlado
                          |
          ===================================
          = T08 CONTINENTAL (S08 y S13)     =
          =   C16  === tráfico pesado ===   =
          ===================================
               | GRADAS | MUELLES |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    MAR DE SUTHIROS
```

Una imagen debe enseñar **un frente portuario/naval en línea con la costa**, con muelles, gradas y un rompeolas que pueden proyectarse al mar. **No debe dibujar una península monumental, cabo de roca o saliente naval artificial** por razones estéticas, y nunca una masa separada del continente por agua ni acceso exclusivo en barco o puente sobre canal nuevo.

## Lista de verificación visual: cumplimiento obligatorio

- [ ] Se reconoce claramente un **enlace terrestre continuo** entre T08 y el territorio.
- [ ] La **C05** llega a la entrada naval por **suelo**, sin cruzar agua.
- [ ] La **C16** enlaza gradas, talleres, almacenes y base naval en **tierra**.
- [ ] Hay logística plausible para **troncos y grandes vigas en carros**, animales de tiro, obreros y materiales pesados.
- [ ] El espacio intermedio T07–T08 se lee como **frente litoral T04**, sin crear un estrecho insular.
- [ ] No aparece canal, río secundario, foso navegable ni bahía trasera que aísle T08.
- [ ] No se ha añadido un puente/calzamiento sobre agua inexistente para justificar el acceso.
- [ ] La costa, el río, el puente, el puerto civil y T08 siguen las posiciones del **GeoJSON maestro**.
- [ ] El área militar se diferencia por **control de acceso y perímetro institucional**, no por aislamiento geográfico.
- [ ] El puerto naval ocupa un **tramo de costa normal**, sin península grande, nueva bahía trasera ni punta de tierra no documentada.
- [ ] Una persona viendo la imagen completa **no interpreta T08 como isla**, incluso sin conocer el lore.

**Regla de rechazo:** si cualquiera de las condiciones de continuidad terrestre falla, **asset rechazado**: sin aprobación visual ni ZIP NAP.

## Estado de mapas ilustrados anteriores

Las tres imágenes anteriores (**Oficial de la Ciudad**, **Mercantil y de Tránsito**, **Reservado del Complejo Naval Real**) han sido **rechazadas por representar T08 de manera insular o ambigua**. Ninguna constituye referencia geográfica válida ni asset aprobado para producción. No reutilizar su silueta como madre de futuros mapas.

## Fuentes de autoridad en el repositorio

- `Datos operativos/treskal_metric_geography_contract_v0.1.json`
- `Datos operativos/treskal_metric_sector_fit_contract_v0.1.json`
- `Datos operativos/treskal_metric_road_network_contract_v0.1.json`
- `Datos operativos/treskal_metric_waterfront_contract_v0.1.json`
- `Datos operativos/treskal_canonical_map_contract_v1.0.json`
- `08_Cartografia/exports/treskal_canonical_spatial_export_v1.0.geojson`
- `08_Cartografia/mapas/treskal_plano_tecnico_canonico_v1.0.svg`

La aclaración es **vinculante**, y no autoriza modificar las coordenadas canónicas de T08 o los trazados de C05/C16.
