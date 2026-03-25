---
title: Creando una nueva iteración del escenario a partir de una solución publicada
shortTitle: Nueva iteración
intro: 'Aprende a crear una nueva iteración de un escenario ya publicado para probar mejoras, ajustar parámetros o introducir cambios sin alterar la versión que ya está vigente en operación.'
contentType: how-tos
versions:
  - '*'
---

## Partiendo de una solución publicada sin alterar la versión vigente

Después de publicar una solución, es normal que necesites seguir trabajando sobre ella. Puede que quieras ajustar reglas, probar otra lógica de turnos, incorporar cambios de oferta o preparar una mejora para un período futuro. En ese caso, no deberías modificar directamente la versión ya publicada. Lo correcto es crear una **nueva iteración** del escenario para mantener la trazabilidad y proteger la versión que ya está vigente.

Usa esta quick start cuando ya tengas un escenario en estado **Publicado** y necesites generar una nueva variante sin perder la referencia histórica de la solución implantada.

Antes de empezar, asegúrate de que:
1. Ya publicaste el escenario anterior en P16.
2. El escenario que tomarás como base está en estado **Publicado**.
3. Ya sabes qué aspecto quieres revisar o mejorar en la siguiente iteración.
4. Tienes claro que la nueva iteración no debe reemplazar automáticamente la versión vigente hasta que vuelva a pasar por cálculo, validación y publicación.

Para esta quick start, usa este caso de referencia:

> **Voy a crear una nueva iteración del escenario publicado de la línea L1 para probar mejoras en la solución sin tocar la versión que ya está vigente en operación.**

Para partir de una solución publicada de forma segura:
1. En GoalBus, abre el módulo de **Escenarios de planificación**.
2. Localiza el escenario que ya está en estado **Publicado**.
3. Revisa su nombre, descripción, tipo de día y líneas asociadas.
4. Confirma que realmente es la versión que quieres usar como referencia.
5. Evita editar esa versión directamente como si fuera un borrador nuevo.
6. Decide qué cambio quieres introducir en la nueva iteración:
   1. reglas,
   2. parámetros,
   3. oferta,
   4. o ajustes estructurales permitidos.

Cuando termines esta sección, deberías tener identificado con claridad el escenario publicado que servirá como base de tu nueva iteración.

## Creando la nueva iteración desde el escenario publicado

Una vez identificada la base, el siguiente paso es crear una **nueva iteración**. El objetivo es conservar la versión publicada como referencia histórica y abrir una nueva rama de trabajo controlada sobre la misma lógica operativa.

Antes de empezar esta sección, asegúrate de que:
1. Ya identificaste la solución publicada correcta.
2. Ya sabes por qué necesitas una nueva iteración.
3. Tienes claro que la nueva iteración debe diferenciarse claramente de la versión anterior.

Para crear la nueva iteración:
1. Desde la tabla de escenarios, abre el menú de acciones del escenario publicado.
2. Selecciona la opción para **crear una nueva iteración** o duplicar el escenario como base de trabajo.
3. Introduce un **nuevo nombre** para la iteración.
4. Si aplica, actualiza la **descripción** para reflejar el objetivo del cambio.
5. Guarda la nueva iteración.
6. Comprueba que el nuevo escenario aparece como una entidad separada del escenario publicado.
7. Revisa que la versión original publicada sigue intacta y diferenciada de la nueva.

Para el caso de referencia, una opción válida podría ser:
- **Scheduling Classic - L1 laborable - iteración 2**
- **L1 laborable - mejora de reglas de turnos**

Cuando termines esta sección, deberías tener una nueva iteración creada sin perder la trazabilidad de la versión publicada.

## Definiendo qué cambios pertenecen a la nueva iteración

Después de crear la iteración, necesitas decidir qué vas a cambiar realmente. No todas las iteraciones persiguen el mismo objetivo. Algunas sirven para ajustar reglas, otras para mejorar eficiencia, otras para reflejar una nueva oferta o una variación operativa futura.

Antes de empezar esta sección, asegúrate de que:
1. Ya creaste la nueva iteración.
2. Ya sabes qué aspecto de la solución anterior quieres revisar.
3. Estás dispuesto a limitar el cambio a un objetivo concreto para no mezclar demasiadas variables.

Para definir el alcance de la iteración:
1. Abre el nuevo escenario.
2. Revisa qué elementos quieres mantener exactamente igual que en la versión publicada.
3. Decide qué elemento vas a cambiar primero:
   1. **reglas de vehículos**,
   2. **reglas de turnos**,
   3. **parámetros del motor**,
   4. **oferta de servicio**,
   5. **matrices logísticas**.
4. Evita cambiar demasiadas cosas a la vez en la primera iteración, salvo que sea estrictamente necesario.
5. Documenta en el nombre o en la descripción el objetivo de la iteración.
6. Guarda los cambios descriptivos antes de pasar al cálculo.

Para el caso de referencia, usa una lógica como esta:
1. Mantener la misma oferta laborable de L1.
2. Ajustar solo el modelo de reglas de turnos.
3. Recalcular para comparar la nueva solución con la publicada.

Cuando termines esta sección, deberías tener una nueva iteración con un objetivo claro y acotado.

## Recalculando la iteración y comparándola con la versión anterior

Una vez definido el alcance, necesitas recalcular la iteración. Aquí la ventaja es que ya no partes desde cero: partes desde una solución conocida y puedes comparar mejor el impacto del cambio.

Antes de empezar esta sección, asegúrate de que:
1. Ya creaste la iteración nueva.
2. Ya definiste el objetivo del cambio.
3. Ya revisaste qué reglas, parámetros o entradas vas a modificar.

Para recalcular la nueva iteración:
1. Revisa el escenario iterado y confirma que sus entradas siguen siendo coherentes.
2. Ajusta el elemento que quieres modificar.
3. Guarda la configuración.
4. Ejecuta el cálculo del nuevo escenario.
5. Espera a que el escenario complete la fase de cálculo.
6. Revisa si la iteración pasa a **Solución preparada** o a **Edición**.
7. Compara el resultado con la versión anterior usando:
   1. KPI,
   2. estructura general,
   3. lógica de tareas,
   4. y coherencia operativa.
8. Si el cambio mejora el resultado, continúa con la revisión formal.
9. Si el cambio empeora el resultado, conserva la versión publicada como referencia y decide si quieres corregir o descartar esta iteración.

Para el caso de referencia, compara:
1. La solución publicada de L1.
2. La nueva iteración con ajuste de reglas.
3. Qué cambió en calidad, viabilidad o equilibrio.

Cuando termines esta sección, deberías tener una nueva solución calculada y una base clara para compararla con la versión ya publicada.

## Decidiendo si la nueva iteración sustituirá a la versión vigente

El último paso es decidir si esta iteración merece convertirse en la nueva versión operativa. Una iteración nueva no sustituye automáticamente a la publicación anterior. Para llegar a producción, debe volver a pasar por revisión, validación y publicación con su propio ciclo de vida.

Antes de terminar, asegúrate de que:
1. Ya calculaste la nueva iteración.
2. Ya comparaste el resultado con la solución publicada.
3. Ya sabes si el cambio aporta una mejora real o solo una variante sin valor operativo.

Para cerrar la decisión sobre la iteración:
1. Revisa la nueva solución desde el punto de vista técnico y operativo.
2. Si la iteración mejora claramente la solución vigente, prepárala para:
   1. validación,
   2. y publicación posterior.
3. Si la iteración no mejora el resultado, conserva la versión publicada actual como referencia vigente.
4. No elimines la publicación anterior solo porque exista una nueva iteración.
5. Mantén ambas versiones bien identificadas para auditoría y comparación histórica.
6. Si decides seguir adelante, trata la iteración como un nuevo escenario que debe recorrer su propio flujo hasta llegar a **Publicado**.

Para el caso de referencia, termina esta quick start solo cuando puedas afirmar una de estas dos cosas:
1. La nueva iteración de L1 mejora la versión publicada y merece continuar su ciclo.
2. La versión publicada actual sigue siendo mejor y la iteración quedará solo como ensayo o referencia.

Cuando termines esta sección, deberías tener una nueva iteración calculada, comparada y lista para convertirse en nueva versión o para conservarse como variante de análisis.

## Lecturas adicionales

- [Ejecutando y validando el primer cálculo de Scheduling](P15_Ejecutando_y_validando_el_primer_calculo_de_Scheduling.md)
