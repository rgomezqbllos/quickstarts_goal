---
title: Creando la base de calendario con tipos de día y festivos
shortTitle: Tipos de día y festivos
intro: 'Aprende a configurar los tipos de día y los festivos para que la lógica de planificación aplique el patrón operativo correcto antes de pasar a rutas, tiempos de recorrido y creación de servicios.'
contentType: how-tos
versions:
  - '*'
---

## Creando el tipo de día que usarás para planificar

Antes de crear servicios o lanzar cálculos de planificación, necesitas definir la lógica de calendario que le dice al sistema con qué tipo de día está trabajando. En GoalBus, los tipos de día son las categorías operativas que agrupan días como laborables estándar, viernes, fines de semana o días especiales, para que no tengas que construir la lógica de planificación fecha por fecha.

Usa esta quick start cuando estés preparando tu primer caso de planificación, cuando necesites crear o validar el tipo de día que usará tu escenario, o cuando quieras asegurarte de que la lógica de festivos está lista antes de continuar.

Antes de empezar, asegúrate de que:
1. Tienes acceso al entorno con permisos para ver o editar la configuración de calendario.
2. Ya sabes qué caso de planificación quieres construir.
3. Ya sabes qué período quieres preparar, por ejemplo enero de 2026.
4. Ya revisaste tu rol de planificador y el flujo general en P1.

Para esta quick start, usa este caso de referencia:

> **Estoy preparando la base de calendario para un escenario laborable de enero de 2026, incluyendo el comportamiento correcto de los festivos.**

Para crear o validar el tipo de día de tu caso:
1. En GoalBus, ve a **Configuración** > **General** > **Gestión de tipos de día**.
2. Revisa los tipos de día existentes y comprueba si ya existe uno que represente la lógica operativa que necesitas.
3. Si ya existe un tipo de día adecuado, confirma que:
   1. Su nombre es claro.
   2. Su nombre corto es claro.
   3. Realmente representa el patrón operativo que necesitas.
4. Si no existe un tipo de día adecuado, haz clic en **Crear tipo de día**.
5. Define el **nombre** y el **nombre corto** del nuevo tipo de día.
6. Selecciona los días de la semana que aplican a ese tipo de día.
7. Si el tipo de día también debe aplicarse a festivos, activa la opción para aplicar el tipo de día a festivos.
8. Guarda el tipo de día.
9. Revisa el resultado y confirma que el tipo de día ahora representa claramente el caso que estás preparando.

Cuando termines esta sección, deberías tener un tipo de día que el sistema pueda usar como categoría operativa para tu caso de planificación.

## Registrando los festivos que alteran la lógica normal del calendario

Después de definir el tipo de día general, necesitas indicarle al sistema qué debe hacer con las fechas excepcionales. Los festivos son importantes porque el calendario puede decir que una fecha es martes, mientras que la operación debería comportarse como un domingo o como otro patrón especial. Si no registras bien los festivos, el sistema puede aplicar el plan incorrecto cuando más adelante publiques o calcules escenarios.

Antes de empezar esta sección, asegúrate de que:
1. Ya creaste o confirmaste el tipo de día que tu caso va a usar.
2. Sabes si el período de planificación incluye festivos o fechas especiales.
3. Estás listo para decidir qué patrón operativo debe seguir cada festivo.

Para registrar y validar los festivos de tu caso:
1. En la misma sección de gestión de tipos de día, cambia a la pestaña **Días festivos**.
2. Revisa si el festivo que necesitas ya existe en el sistema.
3. Si el festivo no existe, crea un nuevo registro de festivo.
4. Si el festivo ya existe, ábrelo y revisa su configuración.
5. Introduce o confirma el **nombre** del festivo.
6. Asigna el **tipo de día** correcto a ese festivo.
7. Guarda el registro del festivo.
8. Repite este proceso para cualquier otro festivo que afecte al período que estás preparando.
9. Revisa la lista de festivos y confirma que cada fecha excepcional apunta al patrón operativo correcto.

Para el caso de referencia, hazte estas preguntas:
1. ¿Enero de 2026 incluye algún festivo que deba comportarse distinto de un laborable estándar?
2. ¿Ese festivo debería comportarse como domingo, como sábado o como otro tipo de día especial?
3. Si publicaras un escenario para este período, ¿el sistema sabría exactamente qué patrón aplicar en esa fecha?

Cuando termines esta sección, el sistema debería poder sustituir el comportamiento normal del calendario en las fechas festivas que importan para tu caso.

## Comprobando que tu base de calendario está lista para planificar

Ahora que ya definiste el tipo de día general y las excepciones por festivos, necesitas confirmar que la base de calendario realmente es utilizable. Este es el paso en el que compruebas que la estructura que creaste puede sostener los siguientes quick starts sin introducir errores evitables.

Antes de continuar, asegúrate de que:
1. El tipo de día existe y tiene la lógica semanal correcta.
2. Los festivos relevantes están registrados.
3. Cada festivo está vinculado al tipo de día correcto.
4. Tu caso de planificación sigue siendo claro y concreto.

Para validar tu base de calendario antes de pasar al siguiente quick start:
1. Revisa el caso de planificación que definiste al principio de este artículo.
2. Confirma que el tipo de día que creaste o validaste coincide con ese caso.
3. Confirma que cualquier festivo dentro del período de planificación ha sido registrado y asociado al tipo de día correcto.
4. Comprueba si la opción de aplicación a festivos que activaste en el tipo de día refleja realmente el comportamiento que quieres.
5. Pregúntate si el sistema ya podría distinguir:
   1. los días normales del período, y
   2. las fechas excepcionales que deben seguir otro patrón operativo.
6. Si la respuesta es sí, continúa con el siguiente quick start.
7. Si la respuesta es no, vuelve atrás y corrige el tipo de día o la asociación de festivos antes de seguir.

Al terminar esta sección, deberías poder afirmar que tu caso de planificación tiene una base de calendario fiable y que los siguientes quick starts podrán apoyarse en ella sin heredar un error de lógica temporal.

## Further reading

- [Validando el año operativo antes de planificar](P3_Validar_el_anio_operativo_antes_de_planificar.md)
