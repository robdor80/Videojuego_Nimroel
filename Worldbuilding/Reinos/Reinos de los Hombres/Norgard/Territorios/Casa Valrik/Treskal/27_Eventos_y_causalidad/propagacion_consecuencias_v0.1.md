# Treskal — resolución de consecuencias y propagación entre sistemas v0.1

## Estado

**DISEÑO DE INTEGRACIÓN APROBADO**

## Objetivo

Evitar que cada subsistema interprete un evento de forma independiente y contradictoria.

---

# 1. Una causa, varias capas

Ejemplo:

**temporal marítimo**

puede producir:

- puerto: menos actividad;
- pesca: menor entrada;
- inventario: menos pescado fresco;
- economía: precio mayor;
- NPC: jornadas alteradas;
- posadas: tripulaciones retenidas;
- rumores: retrasos;
- rutas: navegación restringida.

Todos derivan de la misma instancia.

---

# 2. Efectos declarativos

Una instancia puede emitir efectos como:

- route_modifier;
- stock_modifier;
- activity_modifier;
- access_modifier;
- damage;
- injury;
- schedule_modifier;
- reputation_change;
- knowledge_seed;
- displacement;
- business_state_change.

Los sistemas consumen efectos compatibles.

---

# 3. No duplicar consecuencia

Si un temporal ya redujo pesca:

el sistema económico no debe volver a aplicar otra reducción independiente por “mal tiempo” si representa el mismo efecto.

Debe existir trazabilidad mediante event_id.

---

# 4. Orden

Secuencia conceptual:

1. resolver causa;
2. activar evento;
3. calcular efectos directos;
4. aplicar cambios;
5. recalcular estados derivados;
6. generar conocimiento/rumores;
7. evaluar eventos secundarios.

---

# 5. Eventos secundarios

Ejemplo:

temporal → retraso mercante.

El retraso es una consecuencia.

Solo se convierte en nuevo evento si necesita:

- ciclo de vida propio;
- actores;
- resolución;
- efectos adicionales.

---

# 6. Propagación espacial

Los efectos deben tener ámbito.

Un incendio en Z05 puede:

- cerrar una calle local;
- afectar un taller;
- movilizar agua;
- modificar vecinos.

No reduce automáticamente la actividad de Z10.

---

# 7. Propagación social

Los hechos se propagan después por:

- testigos;
- hogares;
- trabajos;
- mercados;
- tabernas;
- instituciones.

No por el simple hecho de existir en World State.

---

# 8. Recursos compartidos

Un evento puede consumir recursos:

- guardia;
- agua;
- carros;
- trabajadores;
- camas;
- almacenamiento.

Esto puede reducir temporalmente capacidad en otro lugar.

---

# 9. Recuperación

La terminación de la causa no restaura todo instantáneamente.

Cada efecto puede tener:

- recuperación inmediata;
- decay;
- reparación;
- reabastecimiento;
- tratamiento;
- resolución social.

---

# 10. Consecuencia irreversible

Algunos efectos no vuelven atrás:

- muerte;
- pérdida de objeto único;
- relación rota;
- edificio destruido si no se reconstruye;
- información ya conocida.

---

# 11. Acción del jugador

Si el jugador interviene:

- puede reducir;
- agravar;
- redirigir;
- resolver.

El sistema actualiza la misma cadena causal.

No crea una “versión de misión” separada del evento real.

---

# 12. Depuración

Debe poder consultarse:

“¿por qué falta pescado?”

y obtener:

- stock bajo;
- menor entrada;
- temporal EVT_X;
- pesca reducida durante X;
- todavía no hubo nueva captura suficiente.

Esta trazabilidad es fundamental para detectar contradicciones.

---

## Regla final

**Cada cambio importante de Treskal debe poder explicar de qué evento o decisión procede.**
