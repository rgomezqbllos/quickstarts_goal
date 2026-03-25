---
title: Validando la estructura operativa y el estado del servicio
shortTitle: Estructura operativa
intro: 'Aprende a revisar depósitos, unidades y grupos operativos, y a validar el servicio creado para que quede realmente elegible para Scheduling antes de pasar a reglas y cálculo.'
contentType: how-tos
versions:
  - '*'
---

## Revisando la estructura operativa que sostiene tu servicio

Antes de pasar a reglas y al escenario de Scheduling, necesitas comprobar que tu oferta no solo existe, sino que está apoyada en una estructura operativa coherente. En esta fase debes revisar si la línea, el depósito, la unidad operativa y los grupos relacionados pertenecen al mismo contexto de negocio y de operación.

Usa esta quick start cuando ya hayas creado la oferta de servicio base y necesites confirmar que el entorno organizativo que la sostiene es correcto antes de calcular.

Antes de empezar, asegúrate de que:
1. Ya creaste la oferta de servicio en P10.
2. Ya configuraste parkings y depósitos en P6.
3. Ya definiste flota y restricciones base de línea en P8.
4. Tienes claro qué línea y qué servicio usarás como referencia.

Para esta quick start, usa este caso de referencia:

> **Voy a validar que la línea L1, el Depósito Norte, la unidad operativa asociada y los grupos relacionados forman una base coherente antes de llevar el servicio a Scheduling.**

Para revisar la estructura operativa de tu caso:
1. Abre la configuración o vista operativa relacionada con el servicio que acabas de crear.
2. Identifica qué **depósito** sostiene el servicio.
3. Comprueba que ese depósito coincide con la base física que definiste antes.
4. Revisa a qué **unidad operativa** pertenece la línea o el servicio.
5. Comprueba si esa unidad encaja con el corredor, la geografía y la organización del caso.
6. Revisa los **grupos** relacionados que afectan a ese contexto, si existen.
7. Confirma que la línea, la unidad y el depósito no pertenecen a estructuras incompatibles.
8. Si detectas una incoherencia, corrígela antes de seguir.

Para el caso de referencia, revisa:
1. Que la línea L1 está asociada al Depósito Norte.
2. Que ese depósito pertenece a la unidad correcta.
3. Que los grupos vinculados no apuntan a otro ámbito operativo.

Cuando termines esta sección, deberías tener claro que la oferta de servicio vive dentro de una estructura operativa consistente.

## Confirmando que el servicio ya está validado y listo para programación

Después de revisar la estructura operativa, necesitas confirmar algo crítico: que el servicio creado en P10 ya está en estado **Validado**. No basta con haber creado viajes, intervalos y rutas. Para que Scheduling pueda leer el servicio y considerarlo elegible, el servicio debe haber pasado por la acción de validación.

Antes de empezar esta sección, asegúrate de que:
1. Ya revisaste el servicio comercial y sus viajes en P10.
2. Ya comprobaste intervalos, rutas y duraciones.
3. Ya no necesitas seguir editando el servicio en esta fase.

Para confirmar que el servicio está listo para programación:
1. Abre el servicio comercial que usarás como referencia.
2. Revisa su **estado** actual.
3. Si el estado ya es **Validado**, confirma que no hay nada pendiente antes de seguir.
4. Si el servicio sigue en edición o en un estado previo, ejecuta la acción **Validar**.
5. Comprueba que el estado cambia correctamente.
6. Revisa que:
   1. el servicio ya no queda como borrador,
   2. los viajes quedan protegidos frente a cambios accidentales,
   3. y el servicio ya puede ser consumido por Scheduling.
7. Si detectas un error de estructura, corrígelo antes de volver a validar.

Para el caso de referencia, no continúes mientras no puedas afirmar:
1. La línea L1 ya tiene su oferta laborable revisada.
2. El servicio ya cambió a estado **Validado**.
3. El sistema ya puede usarlo como entrada de programación.

Cuando termines esta sección, deberías tener un servicio realmente preparado para ser leído por el motor.

## Comprobando la coherencia entre estructura, servicio y elegibilidad

Ahora necesitas hacer una última revisión conjunta. El objetivo no es solo tener un servicio validado, sino confirmar que el servicio validado vive en la estructura correcta y que no arrastra inconsistencias organizativas que después compliquen el cálculo.

Antes de continuar, asegúrate de que:
1. Ya revisaste depósito, unidad y grupos.
2. Ya validaste el servicio o confirmaste su validación.
3. Ya sabes qué caso llevarás al siguiente paso.

Para validar la elegibilidad completa antes de Scheduling:
1. Revisa el servicio validado y confirma qué línea utiliza.
2. Comprueba que esa línea sigue vinculada al depósito correcto.
3. Revisa que la unidad operativa y los grupos no contradicen el contexto del servicio.
4. Pregúntate si el sistema ya podría tomar ese servicio como una entrada válida y coherente para cálculo.
5. Si la respuesta es sí, continúa con el siguiente quick start.
6. Si la respuesta es no, corrige la estructura o devuelve el servicio a edición solo si necesitas rehacer parte de la base antes de volver a validarlo.

Para el caso de referencia, asegúrate de que:
1. L1 pertenece al contexto organizativo correcto.
2. El Depósito Norte es realmente la base que sostiene el servicio.
3. El servicio laborable ya está validado y no tiene contradicciones con su estructura.

Cuando termines esta sección, deberías poder afirmar que la oferta ya no solo está creada, sino también estructuralmente alineada y elegible para Scheduling.

## Lecturas adicionales

- [Definiendo reglas de vehículos para Scheduling](P12_Definir_reglas_de_vehiculos_para_Scheduling_regenerado.md)
