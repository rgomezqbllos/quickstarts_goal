---
title: Creando la oferta de servicio base con viajes y horarios
shortTitle: Oferta de servicio
intro: "Aprende a crear un servicio comercial, revisar sus viajes por línea y sentido, y dejar una oferta validada y ejecutable antes de pasar a Scheduling en GoalBus."
contentType: how-tos
versions:
  - "*"
---

## Creando el servicio comercial que actuará como contenedor de la oferta

Antes de revisar viajes individuales, necesitas crear el **servicio comercial** que actuará como contenedor de tu oferta. En GoalBus, los servicios comerciales son la capa de gobernanza de la oferta: vinculan líneas y rutas, tipos de día y lógica de calendario, y los viajes que definen el servicio real. La herramienta deja claro que esta estructura evita que horarios incompletos o no revisados lleguen a utilizarse operativamente. fileciteturn29file3L1-L19

Usa esta quick start cuando ya tengas una red validada, una base temporal definida y necesites transformar esa estructura en una oferta real que después pueda validarse, medirse y consumirse en Scheduling.

Antes de empezar, asegúrate de que:

1. Ya configuraste tipos de día y festivos en P2.
2. Ya validaste el año operativo en P3.
3. Ya preparaste la red base y operativa en P4 y P5.
4. Ya definiste parkings, depósitos y desplazamientos en P6 y P7.
5. Ya definiste tipos de vehículo permitidos en P8.
6. Ya creaste la versión de tiempo y los tiempos de recorrido en P9.
7. Tienes claro qué línea, qué tipo de día y qué sentido usarás como caso de referencia.

Para esta quick start, usa este caso de referencia:

> **Voy a crear el servicio comercial laborable de la línea L1, revisar sus viajes de ida y vuelta y dejar la oferta validada antes de pasar a Scheduling.**

Para crear el servicio comercial de tu caso:

1. En GoalBus, ve a la vista **Servicios**.
2. Busca si ya existe un servicio comercial adecuado para tu caso.
3. Si el servicio ya existe, ábrelo y revisa que realmente corresponde al tipo de día y a la oferta que quieres preparar.
4. Si no existe, crea uno nuevo.
5. Define al menos:
   1. un **nombre** claro para el servicio,
   2. el **tipo de día** que aplicará,
   3. las **líneas** que formarán parte de ese servicio.
6. Guarda el servicio.
7. Confirma que ya puedes entrar en su vista de horarios o cuadrícula de viajes.

Para el caso de referencia, una opción válida podría ser:

- **Día laborable estándar - L1**

Cuando termines esta sección, deberías tener un servicio comercial que actúe como contenedor estructurado de la oferta. fileciteturn29file3L1-L19

## Accediendo a la cuadrícula de viajes y cambiando de contexto

Una vez creado el servicio, el siguiente paso es entrar a la cuadrícula de viajes. Esta vista es una “torre de control” centralizada para todos los viajes programados dentro del servicio. Desde aquí puedes cambiar de línea, cambiar de servicio y alternar entre **Sentido 1** y **Sentido 2** sin perder el contexto operativo. fileciteturn29file0L10-L23

Antes de empezar esta sección, asegúrate de que:

1. Ya creaste o validaste el servicio comercial.
2. Ya sabes qué línea quieres revisar primero.
3. Ya sabes qué sentido o dirección usarás como punto de partida.

Para acceder y cambiar de contexto en la cuadrícula de viajes:

1. En la lista de servicios, haz clic en el identificador del servicio o en el icono **Ver horarios**.
2. Una vez dentro, usa el selector de línea para cambiar entre las líneas incluidas en el servicio.
3. Usa el menú desplegable de servicios si quieres comparar con otro servicio comercial.
4. Cambia entre **Sentido 1** y **Sentido 2** para revisar por separado los viajes de ida y vuelta.
5. Mantén el foco en una sola línea y un solo sentido mientras construyes tu caso base.

Para el caso de referencia:

1. Abre el servicio **Día laborable estándar - L1**.
2. Entra primero a **Sentido 1**.
3. Revisa después **Sentido 2**.

Cuando termines esta sección, deberías poder navegar por la oferta sin perder el contexto de línea, servicio y dirección. fileciteturn29file0L10-L23

## Creando o revisando los viajes del servicio

Ahora sí, entra en el detalle de los **viajes**. El documento explica que un horario es una secuencia de eventos y que cada viaje debe estar vinculado a:

1. una variación específica de ruta,
2. una secuencia de paradas,
3. y una referencia temporal.

Esto garantiza que las salidas y llegadas sean físicamente ejecutables. Además, la cuadrícula muestra por defecto solo las paradas principales o puntos temporales para mantener una visión clara, aunque puedes ampliar la vista para ver todas las intermedias. fileciteturn29file2L1-L10 fileciteturn29file0L24-L35

Antes de empezar esta sección, asegúrate de que:

1. Ya tienes una versión de tiempo válida en P9.
2. Ya sabes qué variación de ruta corresponde al viaje que quieres crear o revisar.
3. Ya sabes qué línea y qué sentido estás editando.

Para crear o revisar los viajes del servicio:

1. Dentro del servicio, selecciona una línea y un sentido.
2. Revisa los viajes que ya existen en la cuadrícula.
3. Si necesitas crear un viaje nuevo, utiliza la acción correspondiente para añadir una nueva salida.
4. Asigna al viaje:
   1. la **ruta o variación** correcta,
   2. la **hora de salida**,
   3. y la **referencia temporal** coherente con la versión creada en P9.
5. Si el viaje ya existe, pasa el cursor sobre su identificador para comprobar qué variación de ruta está usando.
6. Revisa que la duración total calculada tenga sentido frente a los tiempos de recorrido definidos.
7. Amplía la secuencia si necesitas revisar todas las paradas intermedias.
8. Repite el proceso hasta que tengas una base mínima de viajes por sentido.

Para el caso de referencia, puedes empezar con una estructura mínima así:

1. L1 - Sentido 1
   1. Viaje 1: salida 06:00
   2. Viaje 2: salida 06:20
2. L1 - Sentido 2
   1. Viaje 1: salida 06:10
   2. Viaje 2: salida 06:30

Cuando termines esta sección, deberías tener una oferta básica de viajes ya vinculada a ruta, sentido y referencia temporal. fileciteturn29file2L1-L10 fileciteturn29file0L24-L35

## Revisando intervalos, duración total y equilibrio de la oferta

Después de crear o revisar los viajes, necesitas comprobar que la oferta tiene sentido como conjunto. La cuadrícula te permite vigilar de forma continua:

1. la **duración total** de cada viaje,
2. el **intervalo** respecto al viaje anterior,
3. y los KPI globales por línea, como recuento de viajes, distancia total y tiempo total de conducción. Esto permite evaluar si la oferta es equilibrada, simétrica y económicamente viable. fileciteturn29file0L24-L43

Antes de continuar, asegúrate de que:

1. Ya tienes al menos algunos viajes creados o revisados.
2. Ya puedes ver la duración total de esos viajes.
3. Ya puedes comparar sentidos y frecuencias.

Para validar el equilibrio de la oferta:

1. En la cuadrícula, revisa la **duración total** de cada viaje.
2. Comprueba que coincide razonablemente con los tiempos de recorrido esperados.
3. Revisa el **intervalo** respecto al viaje anterior y detecta si hay huecos excesivos o salidas demasiado juntas.
4. Compara el número de viajes del **Sentido 1** con el del **Sentido 2**.
5. Revisa los KPI globales de la línea:
   1. **Recuento de viajes**,
   2. **Distancia total**,
   3. **Tiempo total**.
6. Corrige cualquier desequilibrio evidente antes de dar el servicio por listo.

Para el caso de referencia, pregúntate:

1. ¿La ida y la vuelta están equilibradas?
2. ¿Los intervalos entre viajes responden al nivel de oferta que quieres construir?
3. ¿La duración total de cada viaje es coherente con la referencia temporal?
4. ¿La oferta parece económicamente razonable o está sobredimensionada?

Cuando termines esta sección, deberías tener una oferta no solo creada, sino también revisada desde el punto de vista de frecuencia, duración y equilibrio. fileciteturn29file0L24-L43

## Validando el servicio para dejarlo listo para cálculo

El último paso es **validar** el servicio. Validar bloquea los datos del viaje y lo habilita para su programación, mientras que un servicio no validado sigue en fase de edición y no está listo para cálculo. También indica que un servicio validado pasa a estar restringido para edición, deja de ser eliminable y queda listo para su uso en programación. fileciteturn29file0L1-L9

Antes de terminar, asegúrate de que:

1. Ya revisaste los viajes del servicio.
2. Ya comprobaste rutas, duraciones e intervalos.
3. Ya confirmaste que la oferta responde al caso que quieres construir.

Para validar el servicio y dejarlo listo para Scheduling:

1. Revisa una última vez la cuadrícula de viajes del servicio.
2. Confirma que no necesitas seguir editando el servicio.
3. Ejecuta la acción **Validar** sobre el servicio o sobre el conjunto de viajes correspondiente.
4. Comprueba que el estado del servicio cambia a **Validado**.
5. Confirma que:
   1. los viajes quedan bloqueados para cambios accidentales,
   2. el servicio ya está **listo para cálculo**,
   3. y Scheduling podrá leerlo en los siguientes pasos.
6. Si todavía necesitas hacer cambios, usa la lógica de **No validar** solo para devolver el servicio a edición y termina de ajustarlo antes de validarlo de nuevo.

Para el caso de referencia, no continúes a Scheduling hasta que puedas afirmar:

1. La línea L1 tiene una oferta laborable coherente.
2. Los viajes están asociados a la variación de ruta correcta.
3. La duración total y los intervalos tienen sentido.
4. El servicio ya está en estado **Validado**.

Cuando termines esta sección, deberías tener una oferta comercial ya estructurada, revisada y validada, lista para que Scheduling la consuma. fileciteturn29file0L1-L9

## Lecturas adicionales

- [Validando estructura operativa: depósitos, unidades y grupos](P11_Validar_estructura_operativa_depositos_unidades_y_grupos_regenerado_v2.md)
