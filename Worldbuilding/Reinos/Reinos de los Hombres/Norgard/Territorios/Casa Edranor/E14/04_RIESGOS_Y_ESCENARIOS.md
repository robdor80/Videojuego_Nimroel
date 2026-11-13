# E14 — Riesgos, causalidad y pruebas negativas
Los diez riesgos de E13 se **reutilizan con los mismos IDs**, sin probabilidades locales ni eventos consumados. Una celda susceptible no está dañada; para pérdida debe existir `trigger ∧ susceptibility ∧ exposure ∧ vulnerability` y después resolver mitigación y severidad con Core.

| Escenario E13 | Desencadenante de estudio | Probabilidad / gravedad | Incidente observado |
|---|---|---|---|
| ED13-F01 | frost_event | UNKNOWN / UNKNOWN | NO |
| ED13-F02 | heavy_storm | UNKNOWN / UNKNOWN | NO |
| ED13-F03 | saturated_soil | UNKNOWN / UNKNOWN | NO |
| ED13-F04 | rapid_thaw | UNKNOWN / UNKNOWN | NO |
| ED13-F05 | summer_drought | UNKNOWN / UNKNOWN | NO |
| ED13-F06 | extreme_wind | UNKNOWN / UNKNOWN | NO |
| ED13-F07 | snow_ice_on_verified_path | UNKNOWN / UNKNOWN | NO |
| ED13-F08 | wildfire_ignition | UNKNOWN / UNKNOWN | NO |
| ED13-F09 | slope_saturation | UNKNOWN / UNKNOWN | NO |
| ED13-F10 | small_channel_rise | UNKNOWN / UNKNOWN | NO |

## Cadena de consecuencias propuesta, no ejecutada
- Helada fenológica: estadio de vid + temperatura local + parcela expuesta → posible pérdida de cosecha; no activa fallo general de mercado.
- Tormenta y erosión: lluvia + suelo descubierto + pendiente + cultivo/taller expuesto → pérdida condicionada de suelo y suministro.
- Encharcamiento: infiltración deficiente + lluvia + raíz vulnerable → riesgo de cultivo, no arroyos creados.
- Deshielo: episodio real + nieve acumulada + flujo + exposición → riesgo localizado; no inundación por latitud.
- Sequedad: balance hídrico negativo + demanda + falta de reservas → restricción de trabajo agrícola, no vino boreal.
- Viento: orientación + racha + edificio vulnerable → afección posible; no daño sin suceso.
- Nieve/hielo vial: **carretera realmente levantada** + episodio + mantenimiento → accesibilidad cambiante, nunca arista ficticia.
- Incendio: ignición + combustible + propagación + exposición → protección forestal; no fuego automático.
- Inestabilidad: saturación y ladera susceptible + instalación → desalojo condicionado; si no hay edificación, no hay víctima inventada.
- Crecida menor: **cauce comprobado** + nivel + instalaciones vulnerables → efecto, no hidrónimo nuevo.

## Pruebas adversariales conceptuales
Cada U1–U6 aporta tres vetos para selección: ver `01_ATLAS` y el JSON de E14. Los 18 contraejemplos son condicionantes, no sucesos históricos. La auditoría técnica inyecta además derechos, agua, pendiente, protección, jurisdicción, U7 y datos sintéticos mal presentados para probar que se rechazan.
