# Matriz de autoridad documental — D00
**Revisión GitHub `main`:** 15-10-2026. SHA de blob (prefijo), no SHA de commit.
Las rutas de esta tabla comienzan en `Worldbuilding/`.

| Tema | Ruta | SHA |
|---|---|---|
| Treihord | `Norgard/Ciudades/Casa Darovan/Treihord.md` | `cfc1d664ac87` |
| Grandes Casas | `Norgard/Grandes Casas/grandes_casas.md` | `facbba6374ab` |
| Gobierno de Norgard | `Norgard/Gobierno y leyes/organizacion_del_reino.md` | `227dcba1c800` |
| Geografía general | `Norgard/Geografía/geografia_general.md` | `6b51b6adc30d` |
| Montañas | `Norgard/Geografía/montanas.md` | `7c017e8a5971` |
| Ríos y lagos | `Norgard/Geografía/rios_y_lagos.md` | `4f37f277ca06` |
| Mares e islas | `Norgard/Geografía/mares_y_costas.md` | `1b8a798204aa` |
| Bosques | `Norgard/Geografía/bosques.md` | `1e7716107ecd` |
| Regiones naturales | `Norgard/Geografía/regiones_naturales.md` | `2b6a7544fc33` |
| Clima general | `Norgard/Clima/clima_general.md` | `cf9b4d536f67` |
| Perfiles visuales ciudades | `Direccion artistica/Biblia visual/Culturas/Norgard/Datos operativos/norgard_settlements_v0.2.json` | `b3861c5eb274` |
| Regiones visuales | `Direccion artistica/Biblia visual/Culturas/Norgard/Datos operativos/norgard_regions_v0.1.json` | `49a19750188a` |
| Drenaje Core | `Sistemas/Nimroel Core/Datos operativos/nimroel_physical_geography_drainage_contract_v0.1.json` | `126de9447336` |

## Reglas
- Jerarquía obligatoria: `Nimroel Core → Norgard Defaults → Casa Darovan → Localidad → World State`.
- `Nimroel Core/README.md` centraliza contratos universales; el contrato `nimroel_physical_geography_drainage_contract_v0.1.json` es `active_core_contract`, con drenaje descendente, divisorias, afluentes conectados y persistencia.
- `Norgard Defaults/README.md` contiene E1–E17 **validados estáticamente**, incluidos moneda, justicia, ejército, fiscalidad, navegación civil, toponimia, familia y cultura compartida. No se copiarán a Darovan.
- `Norgard/Territorios/Casa Valrik/` aporta **método**, no cifras ni rasgos locales. La prueba estática no acredita ejecución de juego.
- `norgard_settlements_v0.2.json` ofrece perfiles visuales de cuatro ciudades: no sustituye el diseño urbano completo de Treihord.
- **Belara** es la decisión de autor frente a un manuscrito anterior con «Eshneva».
- **Arven** queda en estudio territorial; su administración no está probada.
- Donde Treihord conserva lenguaje histórico de «revisión militar», aplicar Norgard E5 vigente al construir contratos nuevos sin modificar el canon base a espaldas del autor.

No se han creado nombres o medidas cartográficas nuevos.
