# Treskal — continuidad de viaje y aprendizaje de rutas v0.1

## Estado

**DISEÑO DE GAMEPLAY APROBADO**

## Objetivo

Hacer que moverse hacia y desde Treskal forme parte del mismo World State que moverse dentro de ella.

---

# 1. Ruta conocida

El jugador puede conocer una ruta en distintos niveles:

- desconocida;
- conocida de oídas;
- recorrida;
- familiar.

Esto puede afectar:

- mapa;
- instrucciones;
- viaje asistido;
- confianza en desvíos.

---

# 2. Conocimiento no equivale a estado actual

Conocer un camino no significa saber:

- si está bloqueado;
- embarrado;
- inundado;
- vigilado;
- en obras.

El estado actual requiere:

- observación;
- información reciente;
- rumor;
- aviso.

---

# 3. Indicaciones

Un NPC puede orientar usando:

- Puente de los Gemelos;
- Bosque Negro;
- Los Corrales;
- costa;
- ríos;
- Pueblos/Villas conocidas.

No necesita coordenadas.

---

# 4. Viaje de NPC

Un NPC que sale de Treskal debe tener:

- origen;
- destino;
- ruta;
- motivo;
- estado de viaje.

No desaparece conceptualmente.

---

# 5. Encuentro

Si jugador y NPC coinciden en:

- ruta;
- intervalo temporal;
- posición compatible;

pueden encontrarse.

No se fuerza el encuentro solo porque ambos viajen por el mismo camino en días distintos.

---

# 6. Retraso

Puede producirse por:

- clima;
- barro;
- accidente;
- carga;
- animal;
- bloqueo;
- evento.

El retraso modifica llegada real.

---

# 7. Información sobre viajeros

Un posadero o familiar puede saber:

- que salió;
- destino previsto;
- hora aproximada.

No conoce su posición exacta salvo mensaje o evidencia.

---

# 8. Seguridad rural

Los caminos importantes reciben patrullas rurales.

Esto puede afectar:

- percepción de seguridad;
- respuesta a incidentes;
- rumores.

No garantiza ausencia de delito.

---

# 9. Mercancía en tránsito

Un convoy conserva:

- origen;
- destino;
- carga agregada;
- ruta;
- estado.

Hasta que llega, la mercancía **no forma parte del stock de destino**.

---

# 10. Llegada

Cuando llega un viajero o convoy:

- actualiza población presente;
- actualiza stock si procede;
- activa actividad;
- puede generar conocimiento/rumor.

---

## Regla final

**Una ruta no es un menú entre mapas: es un espacio causal que conecta el estado de Treskal con el resto de Valrik.**
