# Treskal — evolución del tejido y reutilización de edificios v0.1

> **MIGRADO A NIMROEL CORE — documentación derivada con override local explícito.** La autoridad normativa de BUILD reside en `Worldbuilding/Sistemas/Nimroel Core/04_Material_y_riesgo/construccion_cambio_edificado_v0.1.md`. Treskal conserva únicamente la protección de su macroestructura e instalaciones singulares; ante conflicto prevalece el Core.

## Estado

**DISEÑO DE WORLD STATE APROBADO**

## Objetivo

Permitir que la ciudad cambie durante una partida sin destruir su macroestructura autoral.

---

# 1. Invariantes macro

Mientras no exista migración de canon, permanecen:

- T;
- Z;
- L;
- S;
- C;
- topología base.

Las obras ordinarias ocurren dentro de esa estructura.

---

# 2. Cambio micro

Puede cambiar:

- building_id materializado;
- uso;
- ocupación;
- fachada funcional;
- acceso;
- subdivisión;
- negocio;
- reparación;
- estado.

---

# 3. Cambio acumulativo

Varias partidas o años de World State pueden producir:

- más subdivisiones;
- negocios trasladados;
- edificios reparados;
- zonas más ocupadas.

No deben convertirse automáticamente en nuevo canon global.

Son historia de esa partida.

---

# 4. Compatibilidad de partida

Una actualización del diseño urbano debe:

- migrar edificios persistentes;
- conservar cambios del jugador;
- no rerollear materializaciones.

---

# 5. Ruina y solar

Si una estructura desaparece:

el site_ref puede permanecer.

Eso permite:

- ruina;
- solar vacío;
- reconstrucción posterior.

El building_id destruido puede conservar referencia histórica.

---

# 6. Reutilización

La reutilización debe preferirse cuando:

- edificio sirve;
- adaptación es viable;
- presión existe.

No toda nueva demanda necesita construcción desde cero.

---

# 7. Rendimiento

En LOD-L la ciudad puede guardar proyectos y cambios como estado agregado.

En LOD-H se materializa la obra visualmente.

---

## Regla final

**La partida puede transformar Treskal sin rediseñar Treskal: el macrocanon permanece y el tejido cotidiano acumula historia.**
