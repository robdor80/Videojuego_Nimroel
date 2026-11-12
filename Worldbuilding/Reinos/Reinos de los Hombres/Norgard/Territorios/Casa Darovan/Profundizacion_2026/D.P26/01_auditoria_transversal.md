# D.P26/01 — Auditoría transversal de profundidad, identidad y canon

## 1. Autoridades documentales, en orden

`Nimroel/Core → Reino Norgard → Casa Darovan (D00–D12, D.P13) → ciudad/comunidad canónica → propuesta editorial aprobada → eventual WorldState de CoreRPG`. Ningún JSON de planificación transforma esta jerarquía. **Treihord.md (2.374 líneas, blob cfc1d664ac87e1f1521a79b6299cdf1a71b45de5)** es la autoridad urbana de Treihord: D.P23 puede colorear la vida cotidiana, no corregir su plano ni inventar una potestad.

## 2. Comparación horizontal de las fases

| Bloque | Evidencia editorial que se conserva | Límite que no se traspasa |
|---|---|---|
| D00–D12 | Geografía, hidrografía, clima, economía, circulación, modelos D06, cuatro ciudades y contratos D11 | No es runtime; D12 ya cerró esa primera capa |
| D.P13 | Doce zonas, relieve, agua, estaciones, altitudes y decisiones expresas del autor | No es cartografía parcelaria, malla de terreno ni trazado de rutas |
| D.P14–D.P18 | Vida de doce paisajes, ocho cadenas, cuatro anteproyectos urbanos, interacciones y auditoría | Planificación diferente de la autoría concreta D.P20–D.P25 |
| D.P20 — Veldora | Seis nombres de área de uso popular, doce futuros lugares, diez biografías; puerto mercantil | Ni distritos legales ni nuevas aduanas interiores |
| D.P21 — Taramin | Seis áreas, doce lugares, diez biografías; vida pesquera y diversidad social | No puentes, muelles o segunda masa forestal inventados |
| D.P22 — Syvaris | Seis áreas, doce lugares, diez biografías; bahía, diversidad insular y presencia de Armada Real | No armada privada ni nuevas rutas navales o puertos en calas |
| D.P23 — Treihord | Ocho barrios ya canónicos enriquecidos, doce futuros establecimientos, diez biografías | Manuscrito original inmutable; La Vena restringida, El Crisol sin ceca |
| D.P24 — mundo rural | Nueve comunidades **candidatas**, diez cadenas, doce biografías, cuidados y estaciones | Ninguna aldea nueva instanciada; D06 sigue exigiendo sus puertas |
| D.P25 — sociedad territorial | 27 protagonistas de 52, treinta relaciones condicionales, diez conflictos futuros, diez escenas TEST_ONLY | Ninguna relación, genealogía, conflicto, misión o derecho activo |

**Resultado:** amplitud editorial alta y desigualdad geográfica deliberada; no extrapolar que una ciudad esté topológicamente más definida por tener más escenas. Los otros 25 perfiles fuente conservan su identidad y dignidad narrativa.

## 3. Invariantes críticos (revisión y bloqueo automático donde son datos)

- **Política y ciudades:** Treihord capital; Veldora, Taramin y Syvaris las otras tres ciudades canónicas. Karsath fuera de Darovan. Arven pertenece formalmente a Darovan. Justicia del Rey, normativa de Norgard y potestades de Corona no se sustituyen por autoridades imaginadas.
- **Hidrografía:** cinco ríos nombrados y cuatro sistemas: Belara/Lhera, Veldora, Fhalion, Thalen. Belara pasa *junto a* Treihord y su barcaza acreditada es somera/industrial. Thalen es un solo río que se abre en dos brazos terminales alrededor de Taramin. Ninguna desembocadura ni cruce no verificado se convierte en hecho.
- **Recursos:** Valkram suministra mineral; el carbón de Treihord procede de Azurios sin ruta física inventada. El Crisol refina y ensaya, **no acuña**; La Vena no es pasaje libre. No hay stock infinito ni permisos de explotación automática.
- **Ecosistemas:** Bosque de las Agujas sin poblaciones permanentes interiores; Bosque de los Pilares es uno; Taramin conserva un único bosque meridional; Manto Verde ocupa aproximadamente el 90 % de Arven y sus aldeas acreditadas se concentran en costa interior. Syvaris no es una selva uniforme.
- **Demografía:** Treihord ≈32.000; Veldora 29.000–35.000; Taramin 14.000–20.000; Syvaris ciudad 7.000–10.000 (NO población total de isla); Darovan 300.000–450.000. No hay censos puntuales autorizados.
- **Comercio y defensa:** Veldora acoge control exterior de **Corona**, no aduana interna entre Casas. Syvaris cuenta con presencia de **Armada Real de Norgard**; Darovan no se dota de flota propia por inferencia.
- **Narración:** biografía no equivale a NPC presente; recuerdo íntimo no es historia pública; relación propuesta no es contacto verificado; TEST_ONLY no genera eventos. El conocimiento individual no se confunde con la verdad del mundo.

## 4. Prueba de continuidad de las personas

Catálogo verificado por inventarios: Veldora 10 + Taramin 10 + Syvaris 10 + Treihord 10 + rural 12 = **52 identidades editoriales únicas**. Selección D.P25: **27** sin reescritura de procedencia; **25 no seleccionados** siguen disponibles. Sus **30 aristas** tienen pares referenciados y permanecen inactivas; **10 conflictos** requieren precondiciones y no se convierten en acontecimientos por mero diseño. No se otorgan rangos, hogares, parientes ni agendas reales.

## 5. Incidencias que no deben falsear el cierre

La grafía **Eshneva** persiste como discrepancia histórica del borrador de Treihord, no como río autorizado: prevalece **Belara**. El árbol canónico histórico D00–D12 contiene registros cronológicos de `UNKNOWN` anteriores a aprobaciones posteriores; no debe reescribirse como si dichas aprobaciones hubieran existido desde el principio. D.P23, D.P24 y D.P25 tienen branches independientes: **su CI individual no acredita por sí sola que estén juntas en main**.

## 6. Dictamen

**Apto para congelar el diseño editorial** y comenzar especificaciones de materialización; **no apto para afirmar territorio jugable o integración administrativa concluida** antes de resolver las PR y revalidar la combinación. No se incorporan nuevos decretos de canon en D.P26.
