---
title: Creando el primer escenario de Scheduling con el motor Classic
shortTitle: Escenario Classic
intro: 'Aprende a crear tu primer escenario de Scheduling con el motor GoalBus Classic, seleccionar correctamente las entradas del cálculo y distinguir cuándo aplicar reglas de vehículos y cuándo aplicar reglas de turnos.'
contentType: how-tos
versions:
  - '*'
---

## Creando el escenario con la oferta validada como punto de partida

Ahora que ya tienes la oferta validada, la lógica de vehículos y la lógica de turnos, el siguiente paso es crear el **escenario de Scheduling** que usará esa base para calcular una solución ejecutable.

Este escenario es el entorno controlado donde vas a combinar:
1. la **oferta validada**,
2. la **matriz de viajes en vacío**,
3. el **modelo de reglas de vehículos**,
4. y el **modelo de reglas de turnos**.

Usa esta quick start cuando ya tengas cerrada la parametrización base y quieras preparar el escenario definitivo para cálculo con el motor Classic.

Antes de empezar, asegúrate de que:
1. Ya configuraste y validaste la oferta de servicio en P10.
2. Ya revisaste la estructura operativa en P11.
3. Ya definiste las reglas de vehículos en P12.
4. Ya definiste los tipos de turnos y las reglas de turnos en P13.
5. Ya tienes preparada la matriz de viajes en vacío de P7.
6. Ya sabes qué tipo de día y qué líneas formarán parte del cálculo.

Para esta quick start, usa este caso de referencia:

> **Voy a crear el primer escenario de Scheduling para la línea L1, usando la oferta laborable validada, la matriz de viajes en vacío correspondiente y los modelos correctos de reglas de vehículos y turnos, para lanzar el cálculo final con GoalBus Classic.**

Para crear el escenario base de tu caso:
1. En GoalBus, abre el módulo **Planificación**.
2. Haz clic en **Nuevo escenario**.
3. Introduce la identidad básica del escenario:
   1. **Nombre**
   2. **Tipo de día**
4. Selecciona el **servicio comercial validado** que quieres cubrir.
5. Selecciona la **matriz de viajes en vacío** que corresponde al mismo tipo de día.
6. Selecciona las **líneas** que formarán parte del escenario.
7. Guarda o finaliza la creación del escenario.
8. Comprueba que el escenario aparece en la tabla principal de planificación.

Para el caso de referencia, una opción válida podría ser:
- **Scheduling Classic - L1 laborable**

Cuando termines esta sección, deberías tener un escenario creado con sus entradas logísticas y comerciales correctas.

## Entendiendo cuándo usar reglas de vehículos y cuándo usar reglas de turnos

Antes de configurar el motor, necesitas dejar clara una distinción importante: **las reglas de vehículos y las reglas de turnos no resuelven el mismo problema**.

Usa **reglas de vehículos** cuando quieras controlar el comportamiento de la flota. Son las reglas correctas si necesitas modelar:
1. compatibilidad física de los vehículos,
2. límites de capacidad o alcance,
3. restricciones de infraestructura,
4. o políticas operativas ligadas al uso de la flota.

Usa **reglas de turnos** cuando quieras controlar cómo se organiza el trabajo humano. Son las reglas correctas si necesitas modelar:
1. horarios de trabajo,
2. pausas y descansos,
3. horas de inicio y fin,
4. amplitud,
5. o diferencias entre tipos de turno, como mañana, tarde o noche.

Antes de continuar, asegúrate de que:
1. Ya sabes qué restricciones pertenecen al vehículo.
2. Ya sabes qué restricciones pertenecen al turno.
3. No estás intentando resolver un problema de personal con reglas de flota, ni al revés.

Para decidir qué modelo debes usar en cada caso:
1. Pregúntate si la restricción afecta al **autobús** o al **conductor**.
2. Si afecta al **autobús**, usa el **modelo de reglas de vehículos**.
3. Si afecta al **trabajo humano** o al tipo de turno, usa el **modelo de reglas de turnos**.
4. Si una regla debe aplicarse a todos los tipos de turnos, revísala como regla global o con el alcance más amplio disponible.
5. Si una regla solo aplica a un tipo de turno concreto, asígnala solo a ese tipo.

Para el caso de referencia:
1. Si quieres limitar qué flota puede cubrir la L1, usa **reglas de vehículos**.
2. Si quieres controlar cómo se construye un turno de mañana o de noche, usa **reglas de turnos**.
3. Si una restricción mezcla ambas cosas, sepárala y configúrala en el modelo correcto.

Cuando termines esta sección, deberías tener claro qué modelo responde a cada necesidad y evitar configuraciones cruzadas o contradictorias.

## Seleccionando el motor GoalBus Classic para el cálculo final

Ahora necesitas configurar el motor de cálculo. Para este quick start, el enfoque es trabajar con **GoalBus Classic** como motor principal del escenario. Este es el motor de optimización profunda orientado a obtener la mejor solución final cuando la parametrización ya está suficientemente madura. fileciteturn34file0L1-L20 fileciteturn34file2L1-L20

Antes de empezar esta sección, asegúrate de que:
1. Ya tienes el escenario creado.
2. Ya seleccionaste correctamente servicio, líneas y matriz de viajes en vacío.
3. Ya tienes claros los modelos de reglas que vas a usar.
4. Estás listo para un cálculo final o casi final, no solo para una prueba táctica rápida.

Para seleccionar el motor Classic:
1. Abre el escenario que acabas de crear.
2. En la barra superior, haz clic en **Configuración de cálculo**.
3. En el panel lateral, selecciona **Motor GoalBus Classic**.
4. Confirma que el escenario ya no está configurado con el motor de aprendizaje automático.
5. Guarda la configuración.

Para el caso de referencia:
1. Usa **GoalBus Classic** como motor principal.
2. Reserva el motor de aprendizaje automático solo para validaciones rápidas previas, no como motor del cálculo final. fileciteturn34file0L1-L20 fileciteturn34file2L1-L20

Cuando termines esta sección, deberías tener el escenario preparado para un cálculo final con el motor Classic.

## Ajustando la flexibilidad inicial y el tiempo máximo de cálculo

Una vez seleccionado el motor Classic, necesitas revisar dos parámetros clave:
1. la **flexibilidad de programación para la primera solución**,
2. y el **tiempo máximo de cálculo**.

La flexibilidad inicial solo aplica al motor GoalBus Classic y sirve para que la primera solución no se bloquee si las restricciones son demasiado rígidas desde el principio. El tiempo máximo de cálculo actúa como garantía de entrega y obliga al sistema a devolver la mejor solución válida que haya encontrado dentro del plazo disponible. fileciteturn34file0L1-L20 fileciteturn34file2L1-L20

Antes de empezar esta sección, asegúrate de que:
1. Ya elegiste GoalBus Classic.
2. Ya sabes si tu caso es muy rígido o necesita algo de libertad inicial.
3. Ya tienes una expectativa razonable sobre cuánto tiempo puedes dedicar al cálculo.

Para ajustar los parámetros avanzados del escenario:
1. Dentro de **Configuración de cálculo**, localiza la sección de parámetros avanzados.
2. Ajusta la **Flexibilidad de programación para la primera solución**.
3. Usa un valor prudente que permita encontrar una solución inicial sin desvirtuar el caso.
4. Define el **Tiempo máximo de cálculo**.
5. Guarda la configuración.
6. Revisa que ambos parámetros quedan asociados al escenario antes de lanzar el cálculo.

Para el caso de referencia:
1. Usa una flexibilidad inicial moderada si sospechas que las restricciones podrían bloquear la primera solución.
2. Define un tiempo máximo realista para que el equipo reciba una solución viable dentro del plazo esperado. fileciteturn34file0L1-L20

Cuando termines esta sección, deberías tener el motor Classic configurado con un marco de cálculo controlado y realista.

## Revisando el escenario antes de lanzarlo

Antes de calcular, necesitas hacer una revisión final del escenario completo. El objetivo es confirmar que no estás entrando al cálculo con entradas contradictorias.

Antes de continuar, asegúrate de que:
1. Ya elegiste el servicio validado correcto.
2. Ya seleccionaste la matriz de viajes en vacío del tipo de día correcto.
3. Ya asignaste los modelos correctos de reglas de vehículos y de turnos.
4. Ya seleccionaste GoalBus Classic como motor.
5. Ya ajustaste flexibilidad y tiempo máximo.

Para revisar el escenario antes de lanzar el cálculo:
1. Revisa el nombre y el tipo de día del escenario.
2. Confirma que el **servicio comercial** corresponde exactamente al que quieres programar.
3. Confirma que la **matriz de viajes en vacío** corresponde al mismo contexto temporal.
4. Revisa el **modelo de reglas de vehículos** y confirma que protege la lógica de flota.
5. Revisa el **modelo de reglas de turnos** y confirma que protege la lógica de trabajo humano.
6. Comprueba que no estás omitiendo un modelo obligatorio para tu caso.
7. Si todo es coherente, deja el escenario listo para el cálculo.

Para el caso de referencia, no continúes hasta poder afirmar:
1. La L1 laborable usa su servicio validado correcto.
2. La matriz laborable es la correcta.
3. El modelo de vehículos limita la flota de forma realista.
4. El modelo de turnos organiza el trabajo de forma coherente.
5. GoalBus Classic ya está seleccionado.

Cuando termines esta sección, deberías tener un escenario limpio, coherente y listo para cálculo final.

## Lecturas adicionales

- [Ejecutando y validando el primer cálculo de Scheduling](P15_Ejecutando_y_validando_el_primer_calculo_de_Scheduling.md)
