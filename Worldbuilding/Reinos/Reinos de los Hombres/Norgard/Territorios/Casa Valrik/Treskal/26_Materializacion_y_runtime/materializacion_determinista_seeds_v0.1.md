# Treskal — materialización determinista y jerarquía de seeds v0.1

## Estado

**DISEÑO TÉCNICO-CONCEPTUAL APROBADO — CIUDAD AUTORAL CON MICRODETALLE DETERMINISTA**

## Objetivo

Permitir que Treskal sea una ciudad única diseñada manualmente sin tener que definir a mano cada vivienda, hogar, interior y residente antes de que sean necesarios.

Treskal **no es procedural como ciudad**.

Sí puede utilizar generación determinista para completar microdetalle compatible con el canon.

---

# 1. Separación fundamental

## Diseñado manualmente

No se genera:

- topología general;
- sectores T;
- subzonas Z;
- landmarks L;
- instalaciones S;
- corredores C;
- función económica;
- nombres canónicos;
- Astilleros Reales;
- sede Valrik;
- grandes mercados.

## Materializable de forma determinista

Puede completarse cuando sea necesario:

- parcelas secundarias;
- edificios ordinarios;
- hogares;
- NPC Nivel B;
- interiores ordinarios;
- pequeños negocios;
- actividad decorativa coherente.

---

# 2. Jerarquía de seeds

Se propone:

`city_seed → zone_seed → parcel/building_seed → household_seed → npc_seed / interior_seed / business_seed`

La derivación debe ser:

- determinista;
- versionada;
- estable mientras no exista migración explícita.

---

# 3. Seed no es identidad

La seed ayuda a producir una instancia.

Después de materializarse, la identidad real es su ID persistente.

Ejemplo:

- seed genera una vivienda;
- se crea `building_id`;
- desde entonces el edificio se guarda por ID y estado.

No se vuelve a reconstruir ciegamente desde seed si ya existe una instancia persistente.

---

# 4. Prioridad autoral

Orden de precedencia:

1. dato autoral explícito;
2. dato persistente materializado;
3. regla canónica;
4. generación determinista compatible;
5. fallback seguro.

Una seed nunca puede sobrescribir:

- NPC autoral;
- edificio singular;
- nombre aprobado;
- relación escrita;
- evento persistente.

---

# 5. Parcela

Cuando exista cartografía métrica, cada parcela ordinaria debe poder recibir:

- parcel_id;
- sector;
- subzona;
- corredor cercano;
- área aproximada;
- acceso;
- usos compatibles;
- restricciones.

La parcela condiciona qué puede materializarse.

---

# 6. Edificio

La materialización de un edificio ordinario debe resolver:

- building_id;
- tipo U;
- huella compatible;
- plantas;
- materiales;
- entradas;
- unidades residenciales;
- espacios de trabajo;
- propietario/ocupantes cuando proceda.

Debe respetar:

- sector;
- subzona;
- perfil visual;
- altura;
- densidad;
- riesgo de inundación/incendio;
- actividad económica.

---

# 7. Hogar

Un hogar se genera después de conocer:

- unidad residencial;
- capacidad;
- necesidades;
- actividad laboral compatible.

Después recibe:

- household_id;
- plantilla H;
- miembros;
- economía doméstica;
- vínculos.

---

# 8. NPC

Un NPC Nivel B puede surgir desde:

- hogar;
- puesto de trabajo;
- visitante;
- interacción contextual.

Debe recibir:

- npc_id;
- seed de origen;
- identidad;
- hogar;
- profesión;
- relaciones iniciales;
- conocimientos plausibles.

Una vez materializado:

**no se rerollea.**

---

# 9. Negocio

Un negocio materializado debe derivarse de una necesidad real de capacidad urbana.

Recibe:

- business_id;
- building_id;
- actividad;
- propietario;
- trabajadores;
- proveedores;
- stock;
- horario.

No se genera una tienda solo porque exista una fachada disponible.

---

# 10. Interior

El interior puede partir de plantilla por tipo U, pero se adapta a:

- parcela;
- edificio;
- ocupantes;
- oficio;
- riqueza;
- actividad;
- World State.

Una vez materializado y visitado, conserva:

- layout relevante;
- objetos persistentes;
- accesos;
- daños;
- cambios.

---

# 11. Nombres

La generación puede asignar nombres personales solo mediante la futura convención onomástica aprobada.

Hasta entonces, un sistema de materialización no debe inventar nombres norgardianos definitivos.

Puede trabajar internamente con ID temporal técnico si la identidad aún no necesita mostrarse.

---

# 12. Relaciones

Las relaciones iniciales deben tener causa:

- hogar;
- trabajo;
- vecindad;
- parentesco;
- aprendizaje;
- comercio.

No crear redes sociales aleatorias desconectadas del espacio y actividad.

---

# 13. Compatibilidad visual

La materialización debe consultar:

- perfil visual de Treskal;
- perfil de Norgard;
- tipo de edificio;
- riqueza/estado;
- clima y desgaste.

No debe producir una vivienda visualmente incompatible aunque los datos funcionales sean válidos.

---

# 14. Fallo seguro

Si faltan datos suficientes para materializar algo persistente:

- usar abstracción;
- aplazar materialización;
- utilizar placeholder técnico no visible.

No inventar canon para completar el objeto.

---

# 15. Reproducibilidad

Dado:

- misma versión de reglas;
- misma seed;
- mismo canon;
- mismo estado previo;

la materialización inicial debe producir el mismo resultado.

---

## Regla final

**Treskal se diseña a mano; la generación determinista solo rellena aquello que todavía no necesitaba existir con detalle.**
