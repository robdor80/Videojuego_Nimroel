# Treskal — luz, oscuridad y visibilidad urbana v0.1

## Estado

**DISEÑO AMBIENTAL/JUGABLE APROBADO**

## Base canónica

Treskal no posee alumbrado urbano moderno.

La noche debe ser claramente más oscura.

La iluminación nocturna procede principalmente de:

- edificios;
- tabernas y posadas;
- dependencias activas;
- puerto;
- guardia;
- Astilleros Reales;
- fuentes portátiles.

---

# 1. Estados cualitativos de luz

## daylight

Luz diurna suficiente según clima.

## overcast_daylight

Luz diurna reducida por:

- nubosidad;
- lluvia;
- niebla.

## twilight

Transición amanecer/anochecer.

## dark_night

Oscuridad dominante sin fuente cercana.

## local_source_lit

Zona iluminada por una fuente concreta.

## mixed_night

Contraste entre zonas oscuras y focos de luz.

No se fijan todavía valores fotométricos.

---

# 2. La ciudad nocturna no es uniformemente oscura

Puede haber:

- interiores iluminados;
- entradas activas;
- puestos de guardia;
- tabernas;
- zonas portuarias operativas.

Entre ellos pueden existir tramos claramente oscuros.

Esto produce una ciudad de **islas de luz**, no una malla continua.

---

# 3. Fuente de luz

Toda luz nocturna visible debe tener causa.

Puede proceder de:

- hogar;
- negocio;
- trabajo;
- vigilancia;
- navegación;
- fuente portátil;
- emergencia.

No se colocan luces solo para facilitar navegación al jugador.

---

# 4. Fuente portátil

Una fuente portátil puede:

- mejorar visión local;
- hacer visible al portador;
- proyectar sombras;
- requerir cuidado;
- introducir riesgo de fuego.

No equivale a visión nocturna.

---

# 5. Percepción

La visibilidad depende de:

- luz;
- distancia;
- niebla;
- lluvia;
- obstáculos;
- contraste;
- orientación;
- movimiento.

Un objeto puede existir y seguir sin ser identificable.

---

# 6. Identificación

Distinguir:

## detectar presencia

“Hay alguien al fondo.”

## reconocer forma

“Parece un hombre con carga.”

## identificar persona

“Es X.”

Cada paso requiere condiciones suficientes.

La IA no salta de silueta a identidad porque el World State conozca el npc_id.

---

# 7. Ventanas e interiores

Una ventana iluminada puede revelar:

- luz;
- siluetas;
- actividad visible.

No revela automáticamente:

- conversación;
- identidad;
- objetos fuera de línea de visión;
- contenido completo de la estancia.

---

# 8. Puerto

La iluminación funcional puede concentrarse en:

- operación;
- carga;
- vigilancia;
- embarcaciones activas.

No convierte el puerto en paseo iluminado.

---

# 9. Astilleros Reales

T08 puede mantener iluminación funcional donde exista:

- guardia;
- emergencia;
- trabajo excepcional.

La iluminación no implica acceso público ni actividad industrial continua.

---

# 10. Mercado

La actividad ordinaria depende principalmente de luz diurna.

Una actividad excepcional fuera de horario puede aportar iluminación propia.

No se presupone mercado nocturno cotidiano.

---

# 11. Clima

## Niebla

Reduce alcance y contraste.

Las fuentes cercanas pueden volverse difusas.

## Lluvia

Reduce visibilidad y modifica reflejos sobre superficies mojadas.

## Temporal

Puede reducir iluminación exterior disponible y aumentar dificultad operativa.

---

# 12. Gameplay

La oscuridad puede afectar:

- reconocimiento;
- navegación;
- vigilancia;
- percepción;
- testimonio;
- seguridad.

No debe usarse como filtro puramente estético si el sistema sigue tratando la escena como plenamente visible.

---

# 13. NPC

Los NPC están sujetos a las mismas restricciones conceptuales.

Un guardia no identifica automáticamente a una persona a gran distancia en oscuridad.

Un testigo nocturno puede conservar conocimiento parcial.

---

# 14. Narrador IA

El contexto autorizado debe indicar:

- estado de luz;
- fuentes visibles;
- visibilidad relevante;
- identidades realmente reconocidas.

La IA describe desde esos datos.

---

## Regla final

**En Treskal la noche oculta de verdad: la luz existe donde alguien la necesita y la mantiene.**
