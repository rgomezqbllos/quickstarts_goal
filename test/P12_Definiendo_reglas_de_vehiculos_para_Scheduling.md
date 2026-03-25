---
title: Definiendo reglas de vehículos para Scheduling
shortTitle: Reglas de vehículos
intro: 'Aprende a configurar las reglas de vehículos que limitarán qué soluciones de flota son válidas en Scheduling, para que el cálculo respete la realidad operativa, la infraestructura y la oferta validada.'
contentType: how-tos
versions:
  - '*'
---

## Preparando la base que usarán las reglas de vehículos

Antes de activar reglas de vehículos, necesitas comprobar que la base que esas reglas van a consumir ya está lista. Las reglas de vehículos no sustituyen una mala parametrización previa. Su función es refinar el comportamiento del cálculo para que el motor descarte combinaciones inviables o no deseadas.

Usa esta quick start cuando ya tengas una oferta de servicio validada, una línea con flota permitida y una estructura operativa coherente, y necesites preparar el caso antes de crear el escenario de Scheduling.

Antes de empezar, asegúrate de que:
1. Ya configuraste la flota permitida por línea en P8.
2. Ya definiste la versión de tiempo y los tiempos de recorrido en P9.
3. Ya creaste y validaste la oferta de servicio en P10.
4. Ya revisaste la estructura operativa y el estado del servicio en P11.
5. Tienes claro qué línea y qué servicio usarás como referencia.

Para esta quick start, usa este caso de referencia:

> **Voy a definir las reglas de vehículos para la línea L1, de forma que Scheduling solo use una flota coherente con la infraestructura, la oferta validada y las restricciones reales del servicio.**

Para preparar la base del caso antes de activar reglas:
1. Abre la línea que usarás como referencia.
2. Comprueba qué tipos de vehículo están permitidos.
3. Revisa desde qué depósito o parking saldrá la operación.
4. Confirma que el servicio que usarás como entrada ya está **Validado**.
5. Comprueba que no estás intentando resolver con reglas un problema que debería haberse corregido antes en línea, flota o infraestructura.
6. Si detectas una incoherencia en esa base, corrígela antes de pasar a la configuración de reglas.

Cuando termines esta sección, deberías tener claro qué caso real estás intentando proteger con las reglas de vehículos.

## Creando o seleccionando el modelo de reglas de vehículos

Una vez revisada la base, necesitas entrar al modelo o catálogo de reglas de vehículos. En este punto no se trata de activar todo. Se trata de elegir o construir un conjunto de restricciones que represente la lógica real del servicio.

Antes de empezar esta sección, asegúrate de que:
1. Ya sabes qué servicio validado usarás como referencia.
2. Ya confirmaste qué tipos de vehículo son válidos para la línea.
3. Ya sabes qué problemas reales quieres evitar.

Para crear o seleccionar el modelo de reglas:
1. En GoalBus, abre el módulo o la sección de **Reglas de vehículos**.
2. Revisa si ya existe un modelo de reglas adecuado para tu caso.
3. Si el modelo ya existe, ábrelo y revisa su configuración.
4. Si no existe, crea un nuevo modelo de reglas.
5. Asigna un **nombre** claro al modelo.
6. Si aplica, añade una **descripción** que te permita distinguir su propósito.
7. Guarda el modelo.
8. Confirma que el modelo ya está disponible para añadirle reglas concretas.

Para el caso de referencia, una opción válida podría ser:
- **Vehículos - L1 laborable**
- **Reglas de flota - Servicio laborable L1**

Cuando termines esta sección, deberías tener un contenedor claro donde configurar las restricciones de vehículos del caso.

## Activando solo las reglas de vehículos que realmente necesitas

Ahora sí puedes empezar a activar reglas. Aquí es importante mantener un criterio claro: una regla debe representar una necesidad real de operación, seguridad, infraestructura o cumplimiento. Si una regla no responde a un problema concreto, no conviene activarla todavía.

Antes de empezar esta sección, asegúrate de que:
1. Ya tienes creado o seleccionado un modelo de reglas.
2. Ya sabes qué flota es válida para la línea.
3. Ya sabes qué combinaciones deberían quedar prohibidas o limitadas.

Para activar las reglas de vehículos del caso:
1. Dentro del modelo de reglas, revisa el catálogo de reglas disponibles.
2. Identifica cuáles responden a las necesidades reales de tu servicio.
3. Activa solo las reglas que realmente necesites para el caso.
4. Configura los parámetros específicos de cada regla cuando aplique.
5. Repite el proceso hasta cubrir las restricciones mínimas necesarias.
6. Guarda los cambios.
7. Revisa el modelo completo y confirma que no está sobrerrestricto ni demasiado abierto.

Para el caso de referencia, pregúntate:
1. ¿Qué situaciones de flota debería impedir el sistema?
2. ¿Qué combinaciones serían físicamente posibles pero no deseables?
3. ¿Qué comportamientos deben quedar guiados por la lógica del depósito, parking o línea?

Cuando termines esta sección, deberías tener un conjunto inicial de reglas de vehículos activas y coherentes.

## Relacionando las reglas con la línea, la flota y la infraestructura

Después de activar las reglas, necesitas comprobar que realmente están alineadas con la línea y la infraestructura que sostienen el caso. Una regla de vehículos no debería contradecir la flota permitida por línea ni la geografía de depósitos y parkings.

Antes de continuar, asegúrate de que:
1. Ya activaste el conjunto inicial de reglas.
2. Ya revisaste los tipos de vehículo permitidos.
3. Ya conoces la base física desde la que sale la operación.

Para comprobar la coherencia de las reglas:
1. Revisa nuevamente la configuración de la línea.
2. Confirma que las reglas no contradicen los tipos de vehículo permitidos.
3. Revisa la relación con el depósito y el parking autorizado.
4. Comprueba que las reglas refuerzan esa lógica, en lugar de romperla.
5. Si una regla deja inviable el servicio o contradice la infraestructura, corrígela o desactívala.
6. Guarda la versión final del modelo.

Para el caso de referencia, asegúrate de que:
1. La línea L1 sigue pudiendo usar la flota autorizada.
2. El Depósito Norte sigue siendo una salida coherente para el servicio.
3. Ninguna regla bloquea una operación que debería ser válida según la base ya configurada.

Cuando termines esta sección, deberías tener reglas alineadas con la realidad del servicio, no con un modelo abstracto o genérico.

## Confirmando que la oferta validada sigue siendo calculable

El último paso es comprobar que las reglas de vehículos que acabas de activar siguen permitiendo calcular la oferta validada. Una cosa es restringir con criterio, y otra es cerrar tanto el modelo que el servicio deje de ser viable antes incluso de crear el escenario.

Antes de terminar, asegúrate de que:
1. Ya activaste las reglas necesarias.
2. Ya revisaste su relación con línea, flota e infraestructura.
3. Ya tienes claro qué servicio será la entrada de Scheduling.

Para validar que el caso sigue siendo calculable:
1. Vuelve a revisar el servicio validado que usarás como referencia.
2. Comprueba que la línea sigue teniendo acceso a la flota que necesita.
3. Revisa si las reglas activadas dejan al menos una solución razonable para el caso.
4. Pregúntate si el sistema ya podría crear un escenario de Scheduling sin caer en contradicción.
5. Si la respuesta es sí, continúa con el siguiente quick start.
6. Si la respuesta es no, corrige el modelo de reglas antes de seguir.

Para el caso de referencia, no continúes hasta poder afirmar:
1. La línea L1 mantiene flota válida y autorizada.
2. El servicio laborable validado sigue siendo compatible con las reglas activadas.
3. El modelo de vehículos ya está listo para usarse dentro del escenario de Scheduling.

Cuando termines esta sección, deberías poder afirmar que la lógica de vehículos ya está cerrada y es lo suficientemente consistente como para pasar a la definición de reglas de turnos y a la creación del escenario.

## Lecturas adicionales

- [Definiendo tipos de turnos y reglas de turnos](P13_Definir_tipos_de_turnos_y_reglas_de_turnos.md)
