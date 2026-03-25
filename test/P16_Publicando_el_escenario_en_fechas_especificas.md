---
title: Publicando el escenario en fechas específicas
shortTitle: Publicar escenario
intro: 'Aprende a publicar un escenario validado en fechas concretas, controlar qué solución entra en operación y mantener trazabilidad entre planificación, validación y despliegue operativo.'
contentType: how-tos
versions:
  - '*'
---

## Preparando el escenario validado antes de publicarlo

Después de calcular y validar una solución, el siguiente paso es decidir **cuándo** debe entrar en vigor en la operación real. Publicar un escenario no consiste solo en aprobarlo: consiste en insertar esa solución validada en el calendario operativo para unas fechas concretas, sin confundirla con un borrador ni con una versión todavía en revisión.

Usa esta quick start cuando ya tengas un escenario en estado **Validado** y necesites llevarlo a operación para un período específico.

Antes de empezar, asegúrate de que:
1. Ya ejecutaste y validaste el escenario en P15.
2. El escenario que quieres publicar está en estado **Validado**.
3. Ya sabes qué fechas exactas quieres cubrir.
4. Tienes claro que publicar cambia el estado operativo de la solución y la hace visible como versión implantada.

Para esta quick start, usa este caso de referencia:

> **Voy a publicar el escenario validado de la línea L1 para que entre en vigor durante un período laborable concreto sin afectar soluciones que no correspondan a esas fechas.**

Para preparar la publicación del escenario:
1. Abre el módulo de **Escenarios de planificación**.
2. Localiza el escenario que ya validaste.
3. Comprueba que el estado actual es **Validado**.
4. Revisa el nombre del escenario, la línea o líneas incluidas, el tipo de día y la descripción.
5. Confirma que estás a punto de publicar exactamente la solución correcta.
6. Si el escenario todavía no está validado, vuelve atrás y termina P15 antes de seguir.
7. Si el escenario es correcto, continúa con la publicación.

Cuando termines esta sección, deberías tener identificado con claridad el escenario validado que quieres implantar.

## Seleccionando la ventana temporal de publicación

Una vez confirmado el escenario, necesitas decidir **en qué fechas** va a aplicarse. La publicación no debería hacerse de forma ambigua. Debe quedar claro desde cuándo y hasta cuándo esa solución será la referencia operativa.

Antes de empezar esta sección, asegúrate de que:
1. Ya confirmaste qué escenario vas a publicar.
2. Ya sabes si la publicación cubrirá un día, una semana, un rango continuo o un bloque operativo más largo.
3. Ya tienes claro que el período elegido no debe contradecir el tipo de día y la lógica temporal del escenario.

Para seleccionar la ventana temporal de publicación:
1. Desde el escenario validado, abre la acción **Publicar**.
2. En el formulario de publicación, define la **fecha de inicio**.
3. Define la **fecha de fin**, si la publicación cubrirá un rango.
4. Revisa que las fechas tengan sentido para:
   1. el tipo de día del escenario,
   2. la línea o líneas implicadas,
   3. y la ventana operativa real que quieres cubrir.
5. Confirma que no estás dejando un rango demasiado amplio por error.
6. Si el escenario solo debe aplicarse en un período corto, limita la ventana con precisión.
7. Guarda o continúa al siguiente paso de publicación.

Para el caso de referencia, pregúntate:
1. ¿La publicación cubre exactamente los días laborables que quiero implantar?
2. ¿Estoy evitando publicar más días de los necesarios?
3. ¿La solución corresponde de verdad a las fechas seleccionadas?

Cuando termines esta sección, deberías tener definida una ventana temporal clara y controlada para la implantación.

## Confirmando la publicación y cambiando el estado del escenario

Después de seleccionar el rango temporal, necesitas confirmar la acción de publicación. En este punto, la solución deja de ser solo un escenario validado y pasa a tener un papel operativo dentro del calendario.

Antes de continuar, asegúrate de que:
1. Ya seleccionaste correctamente las fechas.
2. Ya revisaste el escenario validado.
3. Ya estás listo para que la solución avance en su ciclo de vida.

Para publicar el escenario:
1. Revisa por última vez el resumen de publicación.
2. Confirma:
   1. el nombre del escenario,
   2. el rango temporal,
   3. y el contexto operativo al que se aplicará.
3. Ejecuta la acción **Publicar**.
4. Comprueba que el estado del escenario cambia a **Publicación** mientras el sistema procesa la implantación.
5. Espera a que el proceso termine.
6. Revisa que el estado final cambie a **Publicado**.
7. Si el estado no cambia como esperabas, revisa si hubo una incidencia técnica o un problema de elegibilidad del escenario.

Para el caso de referencia, no des por terminada la publicación hasta que puedas afirmar:
1. El escenario de L1 ya salió de **Validado**.
2. La plataforma procesó la publicación.
3. El estado final del escenario es **Publicado**.

Cuando termines esta sección, deberías tener un escenario ya implantado en el calendario operativo para el período seleccionado.

## Verificando que la solución publicada es la que quedó en vigor

Después de publicar, necesitas comprobar que la solución que quedó activa es realmente la correcta. Publicar no debería ser un paso ciego. Debes poder verificar qué escenario quedó vigente para las fechas elegidas y mantener trazabilidad sobre la solución implantada.

Antes de empezar esta sección, asegúrate de que:
1. El escenario ya llegó a estado **Publicado**.
2. Ya sabes qué fechas cubre.
3. Ya sabes qué servicio o línea debe verse afectado por la publicación.

Para verificar la implantación de la solución:
1. Vuelve a la tabla principal de escenarios.
2. Filtra o revisa los escenarios por estado.
3. Confirma que el escenario publicado aparece como **Publicado**.
4. Revisa sus fechas de aplicación, si la vista lo permite.
5. Comprueba que no estás confundiendo este escenario con otro validado pero no implantado.
6. Si tu proceso interno lo requiere, registra o comunica que esta versión ya es la solución operativa vigente.
7. Conserva el nombre, la descripción y el rango temporal como base de trazabilidad para auditoría posterior.

Para el caso de referencia, asegúrate de que:
1. El escenario publicado corresponde a L1 laborable.
2. Las fechas coinciden con el período que querías implantar.
3. No quedó activo otro escenario distinto por error.

Cuando termines esta sección, deberías tener la certeza de qué solución quedó en vigor y para qué período exacto.

## Manteniendo trazabilidad y preparando la siguiente iteración

Una vez publicado el escenario, el trabajo no desaparece: cambia de foco. A partir de aquí, la solución implantada puede convertirse en referencia para auditoría, comparación o una futura iteración. No conviene reutilizar sin control un escenario ya publicado para experimentar cambios estructurales; lo más seguro es crear una nueva iteración cuando necesites proponer una mejora o una variante.

Antes de terminar, asegúrate de que:
1. El escenario ya está publicado.
2. Ya quedó claro qué rango temporal cubre.
3. Ya sabes si lo siguiente será auditar resultados o preparar una nueva iteración.

Para mantener trazabilidad después de publicar:
1. Conserva el escenario publicado con un nombre y descripción suficientemente claros.
2. Usa el estado **Publicado** como referencia para distinguirlo de escenarios en borrador, cálculo o validación.
3. Si necesitas proponer una mejora, crea un escenario nuevo en lugar de alterar la lógica histórica del escenario implantado.
4. Si tu equipo trabaja con revisión posterior, usa esta versión publicada como línea base de comparación.
5. Mantén un registro interno de:
   1. qué se publicó,
   2. cuándo se publicó,
   3. y para qué fechas quedó vigente.

Para el caso de referencia, termina esta quick start solo cuando puedas afirmar:
1. La solución de L1 ya está publicada.
2. Sabes exactamente desde qué fecha quedó vigente.
3. Puedes distinguir esta versión publicada de cualquier otra iteración futura.

Cuando termines esta sección, deberías tener una solución publicada, trazable y lista para servir como referencia operativa o como punto de partida de una nueva iteración.

## Lecturas adicionales

- [Creando una nueva iteración del escenario a partir de una solución publicada](iteracion-del-escenario)
