---
title: Cargando viajes en vacío y desplazamientos
shortTitle: Viajes en vacío
intro: "Aprende a configurar matrices de viajes en vacío y desplazamientos de conductores para que GoalBus use tiempos logísticos reales, minimice costes no productivos y construya horarios y turnos más realistas."
contentType: how-tos
versions:
  - "*"
---

## Creando la matriz adecuada para el tipo de día correcto

Antes de calcular Scheduling, necesitas definir cómo se mueve físicamente la operación cuando no está generando ingresos. En GoalBus, este módulo cubre dos cosas distintas:

1. **Viajes en vacío**, que representan el movimiento de un autobús con conductor entre el depósito, el parking, el inicio de línea o entre líneas.
2. **Desplazamientos de conductores**, que representan el movimiento del conductor sin vehículo, por ejemplo a pie, en taxi o en lanzadera. fileciteturn23file0turn23file1

GoalBus no trata estos movimientos como una lista única y fija. La Herramienta deja claro que deben organizarse en **matrices por tipo de día**, porque el tráfico cambia según el contexto operativo. Un trayecto puede durar 15 minutos un domingo y 45 minutos un lunes por la mañana, así que la misma conexión no debería reutilizar siempre el mismo tiempo. fileciteturn23file0turn23file2

Usa esta quick start cuando ya hayas configurado parkings y depósitos, y necesites preparar la logística invisible que hará posible una planificación realista.

Antes de empezar, asegúrate de que:

1. Ya preparaste los parkings y depósitos en P6.
2. Ya tienes clara la línea o servicio que usarás como referencia.
3. Ya sabes qué tipo de día estás modelando.
4. Entiendes la diferencia entre un viaje en vacío y un desplazamiento de conductor.

Para esta quick start, usa este caso de referencia:

> **Voy a preparar la matriz de viajes en vacío para un día laborable de la línea L1, conectando el Parking Norte con la Terminal Norte, y también la matriz de desplazamientos de conductores cuando sea necesario para relevos.**

Para crear la matriz correcta para tu caso:

1. En GoalBus, abre el módulo de **viajes en vacío y desplazamientos**.
2. Decide primero si vas a trabajar con:
   1. una matriz de **viajes en vacío**, o
   2. una matriz de **desplazamientos de conductores**.
3. Haz clic en **Crear nuevo**.
4. Introduce un **nombre** claro para la matriz.
5. Añade una **descripción** que te permita reconocer el contexto operativo.
6. Asigna los **tipos de día** a los que aplicará esa matriz.
7. Guarda la matriz.
8. Revisa que la matriz quede claramente asociada al contexto correcto y no a una lógica genérica.

Para el caso de referencia, una matriz válida podría llamarse:

- **Deadhead - Días laborables**
- **Desplazamientos conductores - Días laborables**

Cuando termines esta sección, deberías tener una matriz correctamente creada y vinculada al tipo de día adecuado. fileciteturn23file0turn23file1

## Cargando conexiones mediante importación masiva o edición manual

Una vez creada la matriz, necesitas rellenarla con las conexiones reales entre orígenes y destinos. El documento indica que GoalBus permite dos formas de trabajo:

1. **Importación masiva CSV**, recomendada para redes grandes.
2. **Entrada manual**, útil para casos pequeños o para completar ajustes puntuales. fileciteturn23file0

Antes de empezar esta sección, asegúrate de que:

1. Ya creaste la matriz correcta.
2. Ya identificaste los orígenes y destinos relevantes.
3. Ya sabes si tu caso se puede cargar manualmente o si conviene una importación masiva.

Para cargar datos mediante importación masiva:

1. Prepara un archivo CSV con el formato estándar de GoalBus.
2. Asegúrate de incluir al menos:
   1. orígenes,
   2. destinos,
   3. distancias, y
   4. franjas horarias, cuando apliquen.
3. En GoalBus, selecciona la opción de **carga** o **importación**.
4. Elige el archivo CSV.
5. Revisa la **validación previa** que hace el sistema.
6. Comprueba si el sistema:
   1. detecta errores,
   2. indica cuántos registros se crearán.
7. Si la validación es correcta, confirma la carga.
8. Revisa que la cuadrícula quede rellenada con los registros esperados.

Para cargar datos manualmente:

1. Abre la cuadrícula de la matriz.
2. Añade una nueva fila.
3. Define el **origen**.
4. Define el **destino**.
5. Introduce el tiempo o distancia correspondiente.
6. Si aplica, define la franja horaria.
7. Guarda el registro.
8. Repite el proceso hasta completar las conexiones mínimas necesarias para tu caso.

Para el caso de referencia, empieza con conexiones como estas:

1. Parking Norte → Terminal Norte
2. Terminal Sur → Parking Norte

Cuando termines esta sección, deberías tener una matriz con conexiones reales, ya sea cargadas por archivo o introducidas manualmente. fileciteturn23file0

## Diferenciando viajes en vacío de desplazamientos de conductores

Ahora necesitas comprobar que no estás mezclando dos lógicas distintas. El documento remarca que GoalBus trata los **viajes en vacío** y los **desplazamientos de conductores** de forma parecida en configuración, pero con un propósito de negocio diferente:

1. El viaje en vacío usa **autobús + conductor** y modela la logística de mover un vehículo donde se necesita.
2. El desplazamiento usa **solo conductor** y modela el tiempo que necesita una persona para llegar a un relevo o punto de inicio sin mover flota. fileciteturn23file1turn23file2

Antes de continuar, asegúrate de que:

1. Ya cargaste al menos las conexiones esenciales de tu caso.
2. Puedes identificar si cada conexión corresponde a un vehículo o solo a una persona.
3. No has mezclado ambas lógicas en una misma matriz equivocada.

Para validar que cada matriz representa el recurso correcto:

1. Revisa una conexión de **viaje en vacío** y confirma que su lógica responde a:
   1. mover un vehículo desde depósito o parking hacia la línea, o
   2. mover un vehículo entre líneas.
2. Revisa una conexión de **desplazamiento** y confirma que su lógica responde a:
   1. trasladar a un conductor sin vehículo, o
   2. permitir un relevo en una terminal o cabecera.
3. Comprueba que la matriz de viajes en vacío está modelando tiempos dependientes del tráfico.
4. Comprueba que la matriz de desplazamientos de conductores refleja el modo de traslado real, como caminar, taxi o lanzadera.
5. Corrige cualquier conexión mal ubicada antes de seguir.

Para el caso de referencia, pregúntate:

1. ¿Estoy modelando aquí un autobús que sale del parking o solo un conductor que va a una cabecera?
2. ¿El tiempo que he puesto corresponde al tráfico real o al modo de desplazamiento del conductor?
3. ¿El motor usaría esta información correctamente al construir el horario y los turnos?

Cuando termines esta sección, deberías tener claro qué parte de tu configuración pertenece a la logística del vehículo y qué parte pertenece a la logística del conductor. fileciteturn23file1turn23file2

## Comprobando que la matriz está lista para Scheduling

El objetivo final de este quick start no es solo llenar una tabla, sino preparar una base logística que Scheduling pueda consumir. El documento explica que un modelado preciso de estas matrices mejora tres cosas:

1. la **transparencia de costes**,
2. la **creación realista de turnos**,
3. y la **precisión de la optimización**. fileciteturn23file2

Antes de terminar, asegúrate de que:

1. La matriz correcta existe.
2. Está asociada al tipo de día correcto.
3. Las conexiones mínimas del caso ya están cargadas.
4. Has separado correctamente viajes en vacío y desplazamientos de conductores.

Para validar que la matriz ya está lista para el siguiente paso:

1. Revisa el caso de referencia que vienes construyendo.
2. Confirma que GoalBus ya sabe:
   1. desde dónde sale físicamente el vehículo,
   2. hacia dónde entra en la línea,
   3. cómo vuelve cuando corresponde,
   4. y cómo se movería un conductor para un relevo si aplica.
3. Pregúntate si el sistema ya podría minimizar tiempos y distancias no productivas en ese caso.
4. Si la respuesta es sí, continúa con el siguiente quick start.
5. Si la respuesta es no, vuelve atrás y añade o corrige conexiones antes de seguir.

Cuando termines esta sección, deberías poder afirmar que tu base logística ya es lo suficientemente realista como para sostener tiempos, servicios y Scheduling.

## Lecturas adicionales

- [Definiendo tipos de vehículo y flota permitida por línea](P8_Definir_tipos_de_vehiculo_y_flota_permitida_por_linea_regenerado.md)
