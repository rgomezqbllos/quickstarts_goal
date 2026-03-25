---
title: Ejecutando el primer cálculo de Rostering
shortTitle: Calcular Rostering
intro: 'Aprende a preparar y ejecutar el primer cálculo de Rostering, revisar si la solución de personal es viable y detectar qué problemas pertenecen a reglas, disponibilidad o adscripción antes de validar la asignación.'
contentType: how-tos
versions:
  - '*'
---

## Preparando la base antes de lanzar el cálculo de Rostering

Antes de ejecutar el cálculo, necesitas comprobar que la base de personal ya está lo suficientemente madura. Rostering no debería usarse para descubrir datos maestros faltantes a última hora. Si la plantilla, la adscripción, las reglas o la disponibilidad no están bien preparadas, el cálculo fallará o producirá una solución engañosa.

Usa esta quick start cuando ya tengas una solución de Scheduling estable y hayas preparado toda la capa de personal necesaria para asignar trabajo real a conductores.

Antes de empezar, asegúrate de que:
1. Ya cerraste la transición desde Scheduling en P19.
2. Ya cargaste y revisaste conductores en P20.
3. Ya validaste la adscripción operativa en P21.
4. Ya configuraste reglas de Rostering en P22.
5. Ya registraste ausencias, inactividades y disponibilidad en P23.
6. Ya registraste cesiones, transferencias o cambios de adscripción en P24.
7. Tienes claro qué solución de Scheduling actuará como entrada del cálculo.

Para esta quick start, usa este caso de referencia:

> **Voy a ejecutar el primer cálculo de Rostering para la línea L1, usando una solución de Scheduling ya estable y una base de conductores correctamente preparada.**

Para preparar la base antes del cálculo:
1. Abre el entorno o módulo de **Rostering**.
2. Revisa qué solución de Scheduling será la entrada del cálculo.
3. Confirma que el colectivo de conductores que participará está disponible y pertenece al contexto correcto.
4. Revisa que las reglas de Rostering activas responden al caso real.
5. Comprueba que las ausencias e inactividades principales ya están registradas.
6. Confirma que las cesiones o transferencias relevantes ya están reflejadas.
7. Si detectas un problema de datos maestros, corrígelo antes de calcular.

Para el caso de referencia, no continúes hasta poder afirmar:
1. La solución de L1 ya no necesita cambios estructurales.
2. El colectivo de conductores ya existe y está listo.
3. Las reglas y disponibilidades ya representan la realidad del período.
4. Ya puedes intentar una asignación real de trabajo.

Cuando termines esta sección, deberías tener una base de cálculo suficientemente estable como para lanzar Rostering.

## Seleccionando la entrada correcta desde Scheduling

Rostering necesita una entrada de trabajo clara. Esa entrada no debería ser una mezcla ambigua de escenarios, sino una solución de Scheduling ya conocida y utilizable. En esta fase, lo importante es confirmar que vas a asignar personas al trabajo correcto.

Antes de empezar esta sección, asegúrate de que:
1. Ya sabes qué escenario o solución de Scheduling usarás.
2. Ya sabes qué línea, tipo de día o contexto vas a cubrir.
3. Ya puedes distinguir entre la solución vigente y una iteración todavía no consolidada.

Para seleccionar correctamente la entrada del cálculo:
1. En el módulo de Rostering, abre la configuración del cálculo o del escenario de asignación.
2. Selecciona la **solución de Scheduling** que actuará como entrada.
3. Revisa que el tipo de día coincide con el cálculo que quieres hacer.
4. Comprueba que la línea o conjunto de líneas corresponden al caso.
5. Si hay varias versiones posibles, elige solo la que realmente quieras usar como base.
6. Guarda la selección.
7. Revisa que el sistema ya muestre con claridad qué trabajo será asignado.

Para el caso de referencia, asegúrate de que:
1. La entrada corresponde a L1 laborable.
2. No estás mezclando una versión publicada con una iteración aún no aprobada.
3. El trabajo que llega a Rostering es exactamente el que quieres cubrir.

Cuando termines esta sección, deberías tener una entrada de Scheduling bien definida para el cálculo de personal.

## Configurando el cálculo de Rostering con las reglas y el colectivo correctos

Una vez elegida la entrada, necesitas revisar que el cálculo usa el colectivo y las reglas correctas. En Rostering, una mala combinación entre colectivo, reglas y disponibilidad puede volver inviable una solución que en Scheduling sí era correcta.

Antes de empezar esta sección, asegúrate de que:
1. Ya seleccionaste la entrada desde Scheduling.
2. Ya sabes qué colectivo de personal participará.
3. Ya definiste si usarás reglas básicas, avanzadas o una combinación controlada.

Para configurar el cálculo de Rostering:
1. Abre la configuración del cálculo de asignación.
2. Selecciona el **colectivo de personal** que participará.
3. Revisa qué **modelo de reglas** se aplicará al cálculo.
4. Confirma que las reglas activas corresponden al grupo correcto.
5. Revisa si el cálculo considerará:
   1. ausencias,
   2. inactividades,
   3. cesiones,
   4. y restricciones de disponibilidad.
6. Guarda la configuración.
7. Comprueba que el cálculo ya tiene:
   1. trabajo de entrada,
   2. colectivo elegible,
   3. reglas aplicables.

Para el caso de referencia, confirma que:
1. El grupo de conductores de L1 es el que se va a usar.
2. Las reglas activas corresponden a ese grupo.
3. La configuración no está arrastrando restricciones de otro contexto.

Cuando termines esta sección, deberías tener el cálculo de Rostering correctamente parametrizado antes de ejecutarlo.

## Ejecutando el primer cálculo de asignación

Ahora sí puedes lanzar el cálculo. En este punto, el sistema intentará asignar personas reales al trabajo heredado desde Scheduling, respetando reglas, adscripción y disponibilidad.

Antes de empezar esta sección, asegúrate de que:
1. Ya elegiste la entrada correcta.
2. Ya configuraste el colectivo y las reglas.
3. Ya revisaste la base de disponibilidad y cambios de contexto.
4. Ya no te faltan datos maestros esenciales.

Para ejecutar el cálculo de Rostering:
1. Desde el escenario o módulo de Rostering, lanza la acción **Calcular** o **Iniciar cálculo**.
2. Comprueba que el sistema empieza a procesar la asignación.
3. Espera a que el cálculo termine.
4. Revisa si el sistema devuelve:
   1. una solución asignada,
   2. una solución parcial,
   3. o una señal clara de conflicto.
5. Si el cálculo no genera una solución utilizable, no supongas inmediatamente que falta personal. Revisa primero:
   1. reglas demasiado restrictivas,
   2. adscripción incorrecta,
   3. ausencias mal cargadas,
   4. o cesiones y habilitaciones inconsistentes.

Para el caso de referencia, confirma que:
1. El cálculo de L1 se ejecuta sobre el colectivo esperado.
2. El sistema intenta asignar trabajo real a personas reales.
3. El resultado te permite revisar viabilidad o detectar conflictos concretos.

Cuando termines esta sección, deberías tener una primera solución de Rostering o una señal clara de dónde está el bloqueo.

## Interpretando si el problema es de reglas, disponibilidad o adscripción

Después del cálculo, necesitas interpretar correctamente el resultado. No todos los fallos significan lo mismo. Si no distingues bien la causa, puedes corregir en la capa equivocada.

Antes de continuar, asegúrate de que:
1. Ya ejecutaste el cálculo.
2. Ya viste si la solución salió completa, parcial o con conflicto.
3. Estás dispuesto a diagnosticar antes de tocar datos.

Para interpretar correctamente el resultado:
1. Si faltan muchas asignaciones, revisa primero la **disponibilidad** del personal.
2. Si el sistema deja fuera a personas que deberían ser válidas, revisa su **adscripción** y sus **habilitaciones**.
3. Si la asignación parece demasiado rígida o imposible, revisa las **reglas de Rostering**.
4. Si el trabajo heredado parece inviable para cualquier colectivo, vuelve a revisar si el problema viene desde **Scheduling**.
5. No corrijas por intuición. Localiza primero si el problema pertenece a:
   1. reglas,
   2. disponibilidad,
   3. adscripción,
   4. o estructura heredada.

Para el caso de referencia, hazte estas preguntas:
1. ¿Faltan personas realmente o están mal configuradas?
2. ¿La regla que activé volvió imposible la asignación?
3. ¿Estoy intentando usar un conductor en un contexto donde no pertenece o no está habilitado?
4. ¿El problema existía ya antes de entrar a Rostering?

Cuando termines esta sección, deberías tener una primera lectura diagnóstica del resultado del cálculo.

## Dejando la solución lista para revisión funcional

El objetivo de este quick start no es todavía aprobar definitivamente la solución. El objetivo es ejecutar el primer cálculo y dejar una base lista para revisión funcional: cobertura, conflictos, equilibrio y viabilidad.

Antes de terminar, asegúrate de que:
1. Ya ejecutaste el cálculo.
2. Ya revisaste si la solución es completa o parcial.
3. Ya identificaste si los problemas pertenecen a reglas, disponibilidad, adscripción o Scheduling.

Para cerrar este primer cálculo de forma útil:
1. Conserva el resultado del cálculo como base de revisión.
2. No hagas cambios masivos sin haber identificado antes la causa del problema.
3. Decide si el siguiente paso será:
   1. revisar conflictos de cobertura,
   2. ajustar reglas,
   3. corregir datos de personal,
   4. o volver a Scheduling si el problema es estructural.
4. Trata esta primera ejecución como una validación del modelo completo de asignación.
5. Si la base es razonable, continúa con la revisión de cobertura y conflictos.

Para el caso de referencia, termina esta quick start solo cuando puedas afirmar:
1. Ya ejecutaste el primer cálculo de Rostering para L1.
2. Ya sabes si la solución es viable o parcial.
3. Ya tienes una hipótesis clara sobre dónde están los principales conflictos.
4. Ya estás listo para revisar cobertura y conflictos con más detalle.

Cuando termines esta sección, deberías tener ejecutado el primer cálculo de Rostering y una base clara para la siguiente fase de revisión.

## Lecturas adicionales

- [Revisando conflictos, cobertura y viabilidad de personal](P26_Revisando_conflictos_cobertura_y_viabilidad_de_personal.md)
