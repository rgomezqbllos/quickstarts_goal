---
title: Analizando y comparando escenarios de Scheduling
shortTitle: Comparar escenarios
intro: 'Aprende a comparar escenarios de Scheduling, revisar KPI y diferencias operativas, y decidir con criterio qué solución debe mantenerse como referencia o avanzar a una nueva iteración.'
contentType: how-tos
versions:
  - '*'
---

## Identificando qué escenarios vas a comparar

Después de crear, calcular, validar y publicar escenarios, el siguiente paso natural es compararlos. Comparar escenarios no consiste solo en ver cuál “salió mejor” de forma intuitiva. Consiste en revisar qué cambió, qué impacto tuvo ese cambio y si la nueva iteración realmente mejora la solución de referencia.

Usa esta quick start cuando ya tengas al menos dos escenarios comparables, por ejemplo una solución publicada y una nueva iteración calculada, y necesites decidir cuál debe mantenerse como referencia operativa o cuál merece avanzar en el ciclo de vida.

Antes de empezar, asegúrate de que:
1. Ya creaste y calculaste al menos un escenario base.
2. Ya tienes una segunda versión, iteración o variante que quieras comparar.
3. Sabes qué línea, qué tipo de día y qué contexto operativo estás revisando.
4. Tienes claro cuál es la versión de referencia actual.

Para esta quick start, usa este caso de referencia:

> **Voy a comparar el escenario publicado de la línea L1 con una nueva iteración calculada para decidir si la nueva solución realmente mejora la programación actual.**

Para identificar correctamente los escenarios a comparar:
1. En GoalBus, abre el módulo de **Escenarios de planificación**.
2. Localiza el escenario que actúa como referencia actual.
3. Localiza el escenario nuevo o la iteración que quieres evaluar.
4. Comprueba que ambos escenarios pertenecen al mismo contexto funcional:
   1. misma línea o conjunto comparable de líneas,
   2. mismo tipo de día,
   3. misma lógica operativa general.
5. Revisa el nombre, descripción y estado de cada escenario.
6. Confirma cuál es:
   1. la versión vigente o publicada,
   2. y cuál es la nueva propuesta.
7. Si los escenarios no son comparables entre sí, no continúes hasta corregir ese punto.

Para el caso de referencia, asegúrate de que:
1. Ambos escenarios pertenecen a la línea L1.
2. Ambos son laborables o responden al mismo contexto temporal.
3. Uno actúa como referencia y el otro como alternativa.

Cuando termines esta sección, deberías tener claramente identificados los escenarios que vas a comparar y el rol que cumple cada uno.

## Revisando KPI, volumen de trabajo y equilibrio general

Una vez seleccionados los escenarios, necesitas empezar por una comparación de alto nivel. Aquí el objetivo es revisar indicadores generales antes de entrar en detalles de tareas o reglas. Esta primera comparación te ayuda a detectar si la nueva solución está realmente mejor equilibrada o si solo cambia el resultado sin aportar valor real.

Antes de empezar esta sección, asegúrate de que:
1. Ya sabes qué dos escenarios vas a comparar.
2. Ya identificaste cuál es la referencia.
3. Ya tienes acceso a los KPI visibles del escenario o a las métricas comparables.

Para revisar los KPI generales de los escenarios:
1. Abre el primer escenario y revisa sus KPI principales.
2. Anota o recuerda al menos:
   1. volumen total de trabajo,
   2. número de tareas,
   3. tiempo total,
   4. distancia o magnitud operativa relevante,
   5. cualquier otro indicador visible en la interfaz.
3. Abre el segundo escenario y revisa los mismos KPI.
4. Compara si la nueva iteración:
   1. reduce complejidad innecesaria,
   2. mejora equilibrio,
   3. o desplaza el problema de un sitio a otro.
5. Evita dar por buena una iteración solo porque cambia los números. Lo importante es que el cambio tenga sentido operativo.

Para el caso de referencia, pregúntate:
1. ¿La nueva iteración reduce tareas innecesarias?
2. ¿El equilibrio general parece más razonable?
3. ¿El volumen total sigue siendo coherente con la oferta validada?
4. ¿La mejora es real o solo es una redistribución sin beneficio claro?

Cuando termines esta sección, deberías tener una lectura global de si la nueva solución merece una revisión más profunda.

## Comparando el impacto en vehículos y en turnos

Después de revisar los KPI globales, necesitas bajar a la lógica funcional. En esta fase, la comparación debe separar dos cosas:
1. el impacto en **vehículos**,
2. y el impacto en **turnos**.

Esto es importante porque una iteración puede mejorar la lógica de flota y empeorar la lógica de turnos, o al revés. Si mezclas ambas dimensiones, la lectura se vuelve confusa.

Antes de empezar esta sección, asegúrate de que:
1. Ya revisaste los KPI generales.
2. Ya sabes qué reglas de vehículos y de turnos están implicadas en el cambio.
3. Ya tienes claro cuál fue el objetivo de la iteración.

Para comparar el impacto en vehículos:
1. Revisa cómo se comporta la solución respecto a:
   1. flota utilizada,
   2. compatibilidades,
   3. salidas desde depósitos o parkings,
   4. y kilometraje no productivo, si es visible o deducible.
2. Comprueba si la iteración mejora la coherencia entre línea, flota e infraestructura.
3. Detecta si el nuevo escenario fuerza soluciones que antes eran más realistas.

Para comparar el impacto en turnos:
1. Revisa cómo se construyen las tareas o bloques de trabajo.
2. Comprueba si los tipos de turno activos siguen teniendo sentido.
3. Observa si la nueva solución:
   1. mejora la claridad del trabajo,
   2. empeora la estructura,
   3. o introduce rigideces innecesarias.
4. Relaciona el cambio con el modelo de reglas de turnos que hayas usado.

Para el caso de referencia, pregúntate:
1. ¿La nueva iteración mejora la lógica de vehículos sin castigar la lógica de turnos?
2. ¿Mejora la lógica de turnos sin empeorar la flota?
3. ¿Cuál de las dos dimensiones sale ganando o perdiendo?
4. ¿El resultado global es más robusto o solo más distinto?

Cuando termines esta sección, deberías entender dónde mejora y dónde empeora cada escenario.

## Decidiendo si la nueva iteración aporta valor real

Ahora necesitas convertir la comparación en una decisión. No todo escenario nuevo merece avanzar. A veces una nueva iteración solo sirve como aprendizaje interno y la mejor decisión es mantener la versión vigente. Otras veces la mejora sí es suficientemente clara como para justificar un nuevo ciclo de validación y publicación.

Antes de continuar, asegúrate de que:
1. Ya comparaste KPI generales.
2. Ya revisaste impacto en vehículos y en turnos.
3. Ya sabes cuál era el objetivo original de la nueva iteración.

Para decidir si la iteración aporta valor real:
1. Resume mentalmente cuál fue el propósito del nuevo escenario.
2. Comprueba si ese objetivo se logró de forma clara.
3. Pregúntate si la mejora es:
   1. operativamente visible,
   2. técnicamente defendible,
   3. y suficientemente estable como para seguir avanzando.
4. Si la iteración mejora de forma clara la referencia, prepárala para validación o publicación según corresponda.
5. Si la iteración no mejora la referencia, consérvala como aprendizaje y mantén la versión actual.
6. No promociones una iteración solo porque es más nueva. Promuévela solo si es mejor para el caso.

Para el caso de referencia, termina esta sección solo cuando puedas afirmar una de estas dos cosas:
1. La nueva iteración de L1 mejora de forma clara la solución publicada y merece avanzar.
2. La solución publicada sigue siendo la mejor referencia y la iteración nueva queda como análisis.

Cuando termines esta sección, deberías tener una decisión clara y justificable sobre qué escenario debe mantenerse como referencia.

## Dejando trazabilidad de la comparación para futuras iteraciones

El último paso es dejar rastro de la comparación. Comparar escenarios sin dejar trazabilidad obliga a repetir el análisis en el futuro y hace más difícil explicar por qué una versión fue promovida o descartada.

Antes de terminar, asegúrate de que:
1. Ya tomaste una decisión sobre el escenario.
2. Ya sabes cuál queda como referencia.
3. Ya tienes claro cuál fue el motivo principal de la decisión.

Para dejar trazabilidad de la comparación:
1. Revisa el nombre y la descripción de ambos escenarios.
2. Si hace falta, actualiza la descripción del escenario nuevo para reflejar mejor su propósito o resultado.
3. Conserva identificada la versión de referencia como:
   1. publicada,
   2. validada,
   3. o mantenida como base oficial.
4. Mantén la iteración no promovida como referencia comparativa si aporta valor histórico.
5. Si tu proceso interno lo requiere, registra qué cambió entre ambos escenarios y por qué se tomó la decisión final.

Para el caso de referencia, asegúrate de que:
1. Puedes explicar por qué el escenario nuevo sí o no mejora a L1 vigente.
2. La decisión queda reflejada en nombres, descripciones o proceso interno.
3. La siguiente iteración, si existe, no partirá desde una confusión.

Cuando termines esta sección, deberías tener no solo una comparación hecha, sino una decisión trazable y útil para futuras iteraciones.

## Lecturas adicionales

- [Pasando de Scheduling a Rostering](P19_Pasando_de_Scheduling_a_Rostering.md)
