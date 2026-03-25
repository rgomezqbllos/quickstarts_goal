---
title: Revisando la red operativa con secuencias y puntos clave
shortTitle: Red operativa
intro: 'Aprende a validar cómo se comporta realmente tu red en operación, revisando secuencias, permisos de parada y puntos de relevo antes de pasar a tiempos y servicios.'
contentType: how-tos
versions:
  - '*'
---

## Revisando la secuencia operativa de las rutas

Ahora que ya tienes creada la red base (paradas, líneas y rutas), el siguiente paso es validar que esa red funciona correctamente desde el punto de vista operativo.

En este punto ya no estás creando estructura, estás validando cómo se comporta en la práctica.

Antes de empezar:
1. Ya creaste paradas, líneas y rutas en P4.
2. Tienes al menos una ruta por sentido.
3. Sabes qué línea estás preparando.

Caso:
> Validar que la ruta L1 tiene una secuencia coherente y operativa antes de definir tiempos.

Pasos:
1. Abre la línea en la que estás trabajando.
2. Accede a la vista de rutas.
3. Selecciona un sentido.
4. Revisa la secuencia de paradas.
5. Verifica que:
   - No faltan paradas clave.
   - No hay duplicados innecesarios.
   - El orden es correcto.
6. Repite para el otro sentido.

Resultado esperado:
- Una secuencia limpia y lógica que represente el recorrido real.

## Validando permisos de parada

No todas las paradas funcionan igual. Algunas permiten subida, otras bajada, y otras ambas.

Antes de continuar:
1. Ya validaste la secuencia.
2. Sabes cómo funciona cada parada en la realidad.

Pasos:
1. Dentro de la ruta, revisa cada parada.
2. Configura si permite:
   - Subida
   - Bajada
   - Ambas
3. Asegúrate de que:
   - Terminales permiten ambas.
   - Paradas intermedias reflejan la operación real.
4. Guarda los cambios.

Resultado esperado:
- Cada parada tiene un comportamiento coherente con la operación.

## Definiendo puntos de relevo

Los puntos de relevo son críticos para rostering y operación.

Antes de empezar:
1. Ya tienes secuencia validada.
2. Sabes dónde ocurren relevos en la operación real.

Pasos:
1. Identifica paradas donde se realizan cambios de conductor.
2. Marca esas paradas como puntos de relevo.
3. Verifica que:
   - Están bien ubicados.
   - Son suficientes para la operación.
4. Guarda.

Resultado esperado:
- La red ya contempla dónde se pueden hacer cambios de conductor.

## Validación final de la red operativa

Antes de avanzar:

1. Revisa toda la ruta nuevamente.
2. Confirma:
   - Secuencia correcta.
   - Permisos coherentes.
   - Relevos definidos.
3. Pregúntate:
   - ¿Podría operar esta línea en la vida real?
   - ¿Falta algún detalle operativo?

Si la respuesta es sí, puedes continuar.

## Lecturas adicionales

- P6 Preparando parkings y depósitos
