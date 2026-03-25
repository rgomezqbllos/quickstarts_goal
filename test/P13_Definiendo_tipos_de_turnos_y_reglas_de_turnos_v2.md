---
title: Definiendo tipos de turnos y reglas de turnos
shortTitle: Tipos y reglas
intro: 'Aprende a crear tipos de turnos, organizarlos dentro de modelos de reglas y activar las restricciones o sanciones necesarias para que Scheduling construya tareas legalmente válidas y operativamente coherentes.'
contentType: how-tos
versions:
  - '*'
---

## Creando los tipos de turnos que estructurarán el trabajo

Antes de configurar reglas de turnos, necesitas definir los **tipos de turnos** que el sistema usará para agrupar viajes en trabajo humano coherente. Un tipo de turno no es solo una etiqueta visual. Es la categoría lógica que guía al motor para construir tareas reconocibles y utilizables después en listas, operación diaria e integración con otros sistemas.

Usa esta quick start cuando ya tengas una oferta validada, una lógica de vehículos definida y necesites decirle al sistema qué formas de trabajo son válidas para tu caso.

Antes de empezar, asegúrate de que:
1. Ya creaste y validaste la oferta de servicio en P10.
2. Ya validaste la estructura operativa en P11.
3. Ya definiste las reglas de vehículos en P12.
4. Tienes claro qué servicio y qué contexto operativo usarás como referencia.

Para esta quick start, usa este caso de referencia:

> **Voy a definir los tipos de turnos de la línea L1 para que Scheduling pueda construir tareas coherentes antes de crear el escenario de cálculo.**

Para crear los tipos de turnos de tu caso:
1. En GoalBus, ve a **Configuración** > **Personal** > **Tipos de turnos**.
2. Revisa si ya existen tipos de turnos adecuados para tu caso.
3. Si el tipo ya existe, ábrelo y revisa si sigue siendo válido.
4. Si no existe, crea uno nuevo.
5. Define estos campos:
   1. **Nombre completo**, con un nombre claro y descriptivo.
   2. **Nombre abreviado**, para vistas compactas y tarjetas operativas.
   3. **ID externo**, si el cliente necesita integración con sistemas de RR. HH. o nómina.
6. Marca el tipo como **Activo** si debe participar en cálculos futuros.
7. Guarda el tipo de turno.
8. Repite el proceso para cada categoría de trabajo que realmente necesites en tu caso.

Para el caso de referencia, podrías crear tipos como:
1. **Turno mañana**
2. **Turno tarde**
3. **Turno partido**, si la operación lo requiere

Cuando termines esta sección, deberías tener los tipos de turnos que servirán como “ADN” de las tareas que construirá Scheduling.

## Creando o seleccionando el modelo de reglas de turnos

Después de crear los tipos de turnos, necesitas definir el contenedor donde vivirán las reglas. Las reglas de turnos no se gestionan como una lista plana, sino dentro de **modelos** que agrupan un conjunto coherente de restricciones para un escenario, un período o una simulación concreta. Eso permite mantener varias configuraciones sin mezclar reglas históricas con reglas activas.

Antes de empezar esta sección, asegúrate de que:
1. Ya creaste o validaste los tipos de turnos que usarás.
2. Ya sabes qué servicio o simulación usarás como referencia.
3. Ya tienes claro si este modelo será reutilizable o específico del caso.

Para crear o seleccionar el modelo de reglas:
1. En GoalBus, abre el módulo de **Reglas de programación de turnos**.
2. Revisa si ya existe un **modelo de reglas** adecuado para tu caso.
3. Si el modelo ya existe, ábrelo y revisa si sigue siendo válido.
4. Si no existe, crea un nuevo modelo.
5. Asigna un **nombre** claro al modelo.
6. Si aplica, añade una **descripción** que identifique su uso.
7. Guarda el modelo.
8. Confirma que ya puedes añadir reglas dentro de ese contenedor.

Para el caso de referencia, una opción válida podría ser:
- **Turnos - L1**
- **Reglas de turnos**

Cuando termines esta sección, deberías tener un modelo de reglas preparado para recibir restricciones y sanciones específicas.

## Activando reglas de turnos como restricciones o sanciones

Ahora puedes empezar a configurar las reglas. Aquí es importante distinguir dos lógicas:
1. **Restricciones**, que son obligatorias y bloquean tareas no válidas.
2. **Penalizaciones**, que no bloquean, pero empujan al optimizador hacia soluciones preferidas.

Esta diferencia es clave porque no todo lo que quieres en la operación debe convertirse en una prohibición absoluta. Algunas condiciones deben actuar como guía y no como muro.

Antes de empezar esta sección, asegúrate de que:
1. Ya tienes un modelo de reglas creado o seleccionado.
2. Ya sabes qué comportamiento de trabajo quieres impedir.
3. Ya sabes qué comportamiento quieres favorecer sin volverlo obligatorio.

Para activar las reglas de turnos de tu caso:
1. Dentro del modelo de reglas, revisa las **plantillas de reglas** disponibles.
2. Selecciona la plantilla que corresponda al control que quieres aplicar, por ejemplo:
   1. horas de inicio,
   2. horas de fin,
   3. descansos,
   4. pausas,
   5. tiempo de conducción o tiempo de trabajo.
3. Crea una **regla específica** a partir de esa plantilla.
4. Decide si esa regla actuará como:
   1. **Restricción**, si debe bloquear cualquier tarea que la incumpla.
   2. **Penalización**, si solo debe penalizar soluciones no deseadas.
5. Introduce los parámetros concretos de la regla.
6. Guarda la regla.
7. Repite el proceso solo para las reglas que realmente necesita tu caso.

Para el caso de referencia, piensa en ejemplos como:
1. El turno de mañana debe empezar dentro de una ventana concreta.
2. Un turno partido no debería superar cierto nivel de amplitud.
3. Una secuencia poco deseable puede penalizarse en vez de prohibirse.

Cuando termines esta sección, deberías tener un conjunto inicial de reglas que refleje tanto límites obligatorios como preferencias operativas.

## Aplicando las reglas al tipo de turno correcto

Una vez activadas las reglas, necesitas decidir **a qué tipos de turnos se aplica cada una**. No todas las reglas deben aplicarse a todos los tipos. Algunas pueden ser globales y otras deben dirigirse a categorías concretas, como mañana, tarde o partido.

Antes de continuar, asegúrate de que:
1. Ya activaste al menos una regla dentro del modelo.
2. Ya definiste los tipos de turnos que participan en el caso.
3. Ya sabes si la regla debe ser global o específica.

Para asignar correctamente el ámbito de aplicación:
1. Abre cada regla que hayas creado.
2. Revisa la sección **Tipos de turnos aplicables**.
3. Selecciona los tipos concretos a los que debe aplicarse la regla.
4. Si la regla debe afectar a todos los tipos del escenario, configúrala como **global** cuando la plantilla lo permita.
5. Revisa que no existan dos reglas activas de la misma plantilla aplicándose al mismo tipo de turno si eso generaría un conflicto lógico.
6. Guarda la configuración.
7. Repite la revisión para cada regla del modelo.

Para el caso de referencia:
1. Una ventana de inicio temprana puede aplicarse solo a **Turno mañana**.
2. Una regla de descanso puede aplicarse a varios tipos.
3. Una preferencia general podría ser global.

Cuando termines esta sección, deberías tener reglas con un ámbito de aplicación claro y sin conflictos lógicos entre sí.

## Comprobando que la lógica de turnos sigue siendo compatible con el servicio

El último paso es comprobar que los tipos de turnos y las reglas que acabas de definir siguen siendo compatibles con la oferta validada y con la lógica de vehículos que ya cerraste. No sirve de mucho tener reglas “bonitas” si el resultado deja al servicio sin una forma realista de ser programado.

Antes de terminar, asegúrate de que:
1. Ya creaste los tipos de turnos necesarios.
2. Ya activaste y asignaste las reglas correspondientes.
3. Ya tienes claro qué servicio será la entrada del escenario de Scheduling.

Para validar que el caso sigue siendo calculable:
1. Revisa el servicio validado que usarás como referencia.
2. Comprueba que los tipos de turnos que creaste sí pueden organizar ese trabajo.
3. Revisa si alguna regla de turnos deja el caso demasiado rígido.
4. Comprueba que no existe una contradicción fuerte con las reglas de vehículos ya activadas.
5. Pregúntate si el sistema ya podría construir tareas legales y operativamente coherentes con esta base.
6. Si la respuesta es sí, continúa con el siguiente quick start.
7. Si la respuesta es no, corrige los tipos o las reglas antes de seguir.

Para el caso de referencia, no continúes hasta poder afirmar:
1. La oferta validada de L1 sigue siendo compatible con los tipos de turnos definidos.
2. Las reglas no bloquean innecesariamente el caso.
3. El modelo ya está listo para entrar en el escenario de Scheduling.

Cuando termines esta sección, deberías poder afirmar que la lógica de turnos ya está suficientemente cerrada para pasar a la creación del escenario de Scheduling.

## Lecturas adicionales

- [Creando el primer escenario de Scheduling](P14_Creando_el_primer_escenario_de_Scheduling.md)
