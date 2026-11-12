# E08 — Fuentes, reglas de precedencia y cuestiones abiertas

## Referencias superiores CANON_REPO
- `Norgard/Sociedad/aldeas_servicios_y_economia_local.md`: cadena de provisión, infraestructura de agua de origen físico, horno comunal frecuente, molinos opcionales y servicios no idénticos.
- `Norgard/Gobierno y leyes/familia_matrimonio_filiacion_tutela_adopcion_v0.1.md`: familia jurídica separada de hogar; matrimonio civil monógamo y consentimiento; cuidado/tutela reglados.
- `Norgard/Gobierno y leyes/mayoria_edad_capacidad_trabajo_aprendizaje_v0.1.md`: adultez a los 18; bandas 0–7, 8–11, 12–14, 15–17; límites laborales y de aprendizaje.
- `Norgard/Gobierno y leyes/propiedad_herencia_alquiler_v0.1.md`: ocupante, custodio, poseedor, dueño y administrador distintos; no propiedad universal de Casa.
- `Norgard/Sociedad/salud_curanderia_norgard_v0.1.md`: salud y curandería como base, sin presuposición de hospital local.
- `Norgard/Gobierno y leyes/moneda_y_acunacion.md`: moneda regia, sin ceca Edranor.
- `Norgard/Grandes Casas/grandes_casas.md`, `Norgard/Geografía/rios_y_lagos.md`, `Norgard/Geografía/bosques.md`: Dorth/Lumina/Karsath, Rodas real, lago y bosques protegidos.

## Continuidad local
E00–E07 documentos y manifiestos. En particular E04 oficios solo propuestos, E05 sin carretera física, E06 sin asentamiento instanciado y E07 con cuatro anclas y áreas manuales. `VISUAL_APROBADO` solo habilita *tipos* y rasgos: la posada en Lumina, las herrerías y Casa Druídica de Rodas no tienen empleados, inventarios, derechos ni camas definidos.

## Estado de cada afirmación
- **CANON_REPO:** edad civil, separación de entidades, obligaciones y normas comunes de servicios.
- **VISUAL_APROBADO:** hechos visuales de E07 y perfiles Norgard.
- **AUTOR_2026_11_12/OBSERVACION_MAPA:** Rodas está en el recorte de Edranor, pero su jurisdicción es Corona; Hallheim fuera.
- **PROPUESTA:** catálogo de puestos, identificadores de diseño, procedimientos de cierre, agrupaciones de servicios y posibles vínculos sociales.
- **UNKNOWN:** población, medias por hogar, censos, caudales, potabilidad local, saneamiento, cantidad de camas, profesionales efectivamente disponibles, empleadores, horarios, producción, precios, rutas y permisos.

## Deuda con referencia explícita
`EDD-01` norte; `EDD-02` escala/geometría; `EDD-03` agua local; `EDD-04` censo total y por localidad; `EDD-05` señor/herederos; `EDD-06` **resuelta solo la escala editorial ALDEA de Rodas**; `EDD-07` caminos físicos; `EDD-08` historia de disputa sobre Rodas. No convertir EDD-04 en un valor arbitrario ni en población general de Darovan. E09 necesitará competencias concretas sin inventar guardias ni tasas.

## Alcance de pruebas
Python comprueba estructura documental y 13 supuestos positivos/negativos de laboratorio; no demuestra capacidad de servicio real, cálculo de población efectiva, motor, guardado/carga, simulación offscreen, geolocalización, red de transporte ni funcionamiento de empleo persistido. Tests con números **sintéticos**, nunca de canon.
