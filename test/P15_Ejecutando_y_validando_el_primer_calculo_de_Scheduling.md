---
title: Ejecutando y validando el primer cálculo de Scheduling
shortTitle: Calcular y validar
intro: 'Aprende a ejecutar el primer cálculo de Scheduling, revisar el ciclo de vida del escenario, validar la solución preparada y dejar el escenario listo para publicación o auditoría posterior.'
contentType: how-tos
versions:
  - '*'
---

## Ejecutando el cálculo del escenario

Ahora que ya tienes el escenario creado y configurado con la oferta validada, las matrices correctas y los modelos de reglas de vehículos y turnos, el siguiente paso es ejecutar el cálculo.

En esta fase, el motor toma:
1. la oferta validada,
2. las reglas activas,
3. la logística de viajes en vacío,
4. y la estructura del escenario,

para construir tareas lógicas programables.

Usa esta quick start cuando ya tengas preparado el escenario de Scheduling y necesites obtener la primera solución calculada antes de revisarla y validarla.

Antes de empezar, asegúrate de que:
1. Ya creaste el escenario en P14.
2. Ya seleccionaste el servicio validado correcto.
3. Ya asignaste la matriz de viajes en vacío adecuada.
4. Ya seleccionaste el modelo correcto de reglas de vehículos.
5. Ya seleccionaste el modelo correcto de reglas de turnos.
6. Ya dejaste configurado el motor Classic y los parámetros de cálculo.

Para esta quick start, usa este caso de referencia:

> **Voy a ejecutar el primer cálculo del escenario de Scheduling de la línea L1, revisar si la solución es coherente y dejar el escenario listo para validación.**

Para ejecutar el cálculo del escenario:
1. Abre el escenario que quieres calcular.
2. Revisa una última vez que las entradas del escenario son correctas.
3. Lanza la acción **Calcular** o **Iniciar cálculo**.
4. Comprueba que el estado del escenario cambia de **Solución pendiente** a **Cálculo de la solución**.
5. Espera a que el motor termine el proceso.
6. Revisa el nuevo estado del escenario.
7. Si el cálculo concluye correctamente, confirma que el escenario pasa a **Solución preparada**.
8. Si la solución requiere ajustes manuales, entra al estado **Edición** para refinamiento.
9. Si el motor no devuelve una solución válida, vuelve a revisar:
   1. la oferta,
   2. la matriz de viajes en vacío,
   3. las reglas,
   4. y los parámetros del escenario.

Para el caso de referencia, confirma que:
1. El escenario de L1 sale del estado inicial.
2. El motor termina el cálculo sin bloquearse.
3. El escenario llega a una solución preparada o a una fase de edición razonable.

Cuando termines esta sección, deberías tener una primera solución calculada o una señal clara de qué parte de la parametrización necesita corrección.

## Revisando el estado del escenario y el resultado del cálculo

Después de ejecutar el cálculo, necesitas entender en qué punto del ciclo de vida ha quedado el escenario. Esto es importante porque cada estado tiene un significado operativo distinto y te dice qué acciones puedes hacer a continuación.

Antes de empezar esta sección, asegúrate de que:
1. Ya ejecutaste el cálculo.
2. Ya conoces el nombre del escenario que estás revisando.
3. Ya sabes si esperabas una solución lista o una fase de refinamiento.

Para revisar el estado y el resultado:
1. Vuelve a la tabla principal de escenarios o mantente dentro del escenario.
2. Revisa el estado actual.
3. Interpreta el estado según esta lógica:
   1. **Solución pendiente**: el escenario aún no ha sido calculado.
   2. **Cálculo de la solución**: el motor está procesando la solución.
   3. **Edición**: un usuario está ajustando manualmente la solución.
   4. **Solución preparada**: la fase de cálculo o edición ya terminó y el escenario está listo para revisión.
   5. **Validado**: la solución ya fue aprobada y bloqueada.
   6. **Publicación**: la solución se está incorporando al calendario operativo.
   7. **Publicado**: la solución ya quedó implantada en la operación.
4. Si el escenario está en **Solución preparada**, continúa con la revisión de coherencia.
5. Si el escenario está en **Edición**, termina primero los ajustes manuales necesarios.
6. Si el escenario sigue en **Cálculo de la solución** demasiado tiempo, revisa si hubo una incidencia técnica o una configuración excesivamente restrictiva.

Para el caso de referencia, deberías esperar que el escenario termine al menos en:
1. **Solución preparada**, si ya no necesitas tocar la estructura,
2. o **Edición**, si todavía quieres refinar manualmente.

Cuando termines esta sección, deberías entender con claridad qué significa el estado actual del escenario y qué acción procede después.

## Revisando KPI, errores y consistencia antes de validar

Antes de validar el escenario, necesitas revisarlo. Validar no es un simple clic administrativo. Es la puerta de aprobación formal que congela la solución y evita cambios accidentales posteriores.

Antes de empezar esta sección, asegúrate de que:
1. El escenario ya está en **Solución preparada** o que terminaste la fase de **Edición**.
2. Ya sabes que, después de validar, el escenario dejará de ser editable.
3. Ya estás listo para una revisión final previa a la aprobación.

Para revisar la solución antes de validarla:
1. Abre el escenario en su estado actual.
2. Revisa los KPI disponibles.
3. Revisa si existen errores, avisos o incoherencias visibles.
4. Usa los filtros disponibles para inspeccionar la solución desde distintos ángulos.
5. Comprueba que las asignaciones y la estructura del escenario tienen sentido operativo.
6. Si detectas un problema menor y el escenario aún es editable, corrígelo antes de continuar.
7. Si detectas un problema importante después de haberlo bloqueado más adelante, deberás desbloquearlo con permisos adecuados o volver a un escenario editable.

Para el caso de referencia, asegúrate de que:
1. Los KPI de la solución de L1 son razonables.
2. No hay errores graves que invaliden la solución.
3. La solución ya puede pasar de revisión técnica a aprobación formal.

Cuando termines esta sección, deberías tener la confianza suficiente para validar el escenario.

## Validando el escenario y bloqueando la solución

Ahora sí puedes ejecutar la **validación del escenario**. Este paso marca el cierre oficial de la fase de cálculo y edición. A partir de aquí, la solución pasa a estar protegida, el escenario deja de ser editable y ya no puede recalcularse mientras permanezca validado.

Antes de empezar esta sección, asegúrate de que:
1. El escenario está en **Solución preparada**.
2. Ya terminaste la revisión de KPI y errores.
3. No necesitas hacer más ajustes manuales antes de aprobar la solución.

Para validar el escenario:
1. Desde la tabla de escenarios, abre el menú de acciones del escenario.
2. Selecciona **Validar**.
3. Si prefieres hacerlo desde dentro del escenario, usa el botón **Validar** en la parte superior de la pantalla.
4. Confirma la validación cuando el sistema lo solicite.
5. Comprueba que el estado del escenario cambia a **Validado**.
6. Revisa que:
   1. el escenario ya no es editable,
   2. ya no puede recalcularse,
   3. y sus datos principales quedan protegidos.
7. Si descubres un error de última hora después de validar, usa el flujo de desbloqueo solo con los permisos adecuados.

Para el caso de referencia, no continúes mientras no puedas afirmar:
1. La solución de L1 ya fue revisada.
2. El escenario cambió a estado **Validado**.
3. La organización ya puede tratar ese escenario como una versión aprobada.

Cuando termines esta sección, deberías tener una solución formalmente aprobada y bloqueada para evitar cambios accidentales.

## Dejando el escenario listo para publicación o auditoría posterior

Una vez validado, el escenario ya está preparado para dos caminos:
1. **publicación**, si quieres llevarlo al calendario operativo real,
2. o **auditoría**, si todavía necesitas revisarlo antes de publicarlo.

En este punto, el escenario queda como una solución aprobada y protegida. Todavía puedes consultarlo, revisar KPI, filtrar información y usarlo como referencia, pero ya no deberías tratarlo como un borrador de trabajo.

Antes de terminar, asegúrate de que:
1. El escenario ya está en estado **Validado**.
2. Ya conoces la diferencia entre validar y publicar.
3. Ya sabes si tu siguiente paso será implantar la solución o seguir auditándola.

Para dejar el escenario listo para el siguiente paso:
1. Revisa la tabla de escenarios y confirma el estado **Validado**.
2. Si el plan ya está aprobado para su implantación, prepara el flujo de **Publicar**.
3. Si todavía necesitas revisión interna, mantén el escenario validado como base de auditoría.
4. Usa filtros, iconos informativos y revisión de estados para controlar qué escenarios están pendientes, validados o ya publicados.
5. Si necesitas iterar una nueva versión, considera duplicar el escenario en lugar de alterar uno ya aprobado.

Para el caso de referencia, termina esta quick start solo cuando puedas afirmar:
1. El escenario de L1 ya fue calculado.
2. La solución fue revisada.
3. El escenario está **Validado**.
4. El siguiente paso ya no es calcular, sino decidir si se publica o si se audita.

Cuando termines esta sección, deberías tener un escenario calculado, revisado y validado, listo para su paso a producción o a revisión final.

## Lecturas adicionales

- [Publicando el escenario en fechas específicas](publicacion-del-escenario)
