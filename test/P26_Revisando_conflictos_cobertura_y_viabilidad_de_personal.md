---
title: Revisando conflictos, cobertura y viabilidad de personal
shortTitle: Conflictos y cobertura
intro: 'Aprende a revisar la solución de Rostering después del cálculo, identificar conflictos de cobertura, distinguir si el problema viene de reglas, disponibilidad o adscripción, y decidir qué corregir antes de validar la asignación.'
contentType: how-tos
versions:
  - '*'
---

## Entendiendo qué debes revisar después del cálculo de Rostering

Después de ejecutar el primer cálculo de Rostering, el siguiente paso no es validar de inmediato la solución. Primero necesitas revisar si la asignación es realmente viable. En esta fase, el objetivo es comprobar si el sistema logró cubrir el trabajo con personas reales respetando restricciones laborales, disponibilidad y contexto operativo.

Usa esta quick start cuando ya ejecutaste el cálculo de Rostering y necesitas analizar si la solución puede considerarse completa, parcial o conflictiva.

Antes de empezar, asegúrate de que:
1. Ya ejecutaste el primer cálculo de Rostering en P25.
2. Ya sabes qué solución de Scheduling actuó como entrada.
3. Ya tienes claro qué colectivo de conductores participó en el cálculo.
4. Estás preparado para analizar la solución antes de validarla.

Para esta quick start, usa este caso de referencia:

> **Voy a revisar la solución de Rostering de la línea L1 para comprobar si el trabajo quedó cubierto, si hay conflictos de asignación y si el resultado es viable antes de validarlo.**

Para entender qué revisar después del cálculo:
1. Trata la revisión como una fase de diagnóstico, no como una aprobación automática.
2. Revisa siempre tres dimensiones:
   1. **cobertura**,
   2. **conflictos**,
   3. **viabilidad general**.
3. No des por buena una solución solo porque el motor haya terminado el cálculo.
4. Considera que una solución puede:
   1. cubrir todo el trabajo,
   2. cubrirlo parcialmente,
   3. o producir conflictos que obliguen a volver a reglas, disponibilidad o adscripción.

Cuando termines esta sección, deberías tener claro qué significa revisar una solución de personal y qué preguntas debes responder antes de validarla.

## Revisando la cobertura del trabajo asignado

La primera pregunta que debes responder es sencilla: **¿quedó todo el trabajo cubierto?**. Aquí no se trata todavía de por qué falló algo, sino de medir si el sistema consiguió asignar personas al trabajo heredado desde Scheduling.

Antes de empezar esta sección, asegúrate de que:
1. Ya tienes visible la solución calculada.
2. Ya sabes qué trabajo total esperabas cubrir.
3. Ya puedes revisar el resultado por línea, grupo o colectivo.

Para revisar la cobertura:
1. Abre la solución calculada de Rostering.
2. Revisa la vista general del resultado.
3. Identifica:
   1. tareas cubiertas,
   2. tareas no cubiertas,
   3. y asignaciones parciales, si existen.
4. Comprueba si la cobertura es completa o si hay huecos.
5. Si el sistema muestra contadores o resúmenes de cobertura, revísalos.
6. Si la cobertura no es completa, no valides todavía la solución.
7. Marca mentalmente dónde están los huecos para analizarlos después.

Para el caso de referencia, pregúntate:
1. ¿El trabajo de L1 quedó cubierto por completo?
2. ¿Hay días o franjas con huecos?
3. ¿El problema afecta a toda la línea o solo a una parte del servicio?

Cuando termines esta sección, deberías saber si la solución cubre todo el trabajo o si hay tareas sin asignar.

## Detectando conflictos y leyendo su causa probable

Después de revisar la cobertura, necesitas identificar los conflictos. Un conflicto no significa automáticamente que falte personal. Puede significar que una regla es demasiado restrictiva, que una persona está mal adscrita o que una ausencia o cesión se modeló mal.

Antes de empezar esta sección, asegúrate de que:
1. Ya identificaste si existen tareas no cubiertas.
2. Ya estás dispuesto a diferenciar causas en lugar de corregir por intuición.
3. Ya sabes qué parte de la solución revisar primero.

Para revisar conflictos de forma útil:
1. Revisa las tareas que quedaron sin asignar o con problema.
2. Observa si el sistema muestra mensajes, indicadores o conflictos asociados.
3. Intenta clasificar la causa probable en uno de estos grupos:
   1. **reglas demasiado restrictivas**,
   2. **disponibilidad insuficiente**,
   3. **adscripción o habilitación incorrecta**,
   4. **estructura heredada desde Scheduling**.
4. Si el conflicto parece afectar a muchas personas del mismo colectivo, revisa primero reglas y adscripción.
5. Si el conflicto afecta a casos individuales, revisa primero disponibilidad, ausencia o cesión.
6. Si el problema parece provenir del trabajo heredado, considera volver a Scheduling.

Para el caso de referencia, hazte estas preguntas:
1. ¿La tarea quedó sin cubrir porque no había persona disponible?
2. ¿La persona existía, pero no estaba habilitada o adscrita al contexto correcto?
3. ¿La regla de Rostering bloqueó una asignación que sí parecía posible?
4. ¿El problema no es de personal, sino del trabajo heredado?

Cuando termines esta sección, deberías tener una hipótesis razonable sobre la causa de los conflictos principales.

## Revisando la viabilidad general de la solución

Una solución puede estar casi cubierta y aun así no ser buena. Por eso, además de cobertura y conflictos, necesitas revisar la **viabilidad general**. Aquí la pregunta no es solo si el sistema asignó personas, sino si la asignación resultante tiene sentido operativo y humano.

Antes de continuar, asegúrate de que:
1. Ya revisaste cobertura.
2. Ya identificaste conflictos principales.
3. Ya estás listo para valorar calidad, no solo cantidad.

Para revisar la viabilidad general:
1. Revisa si la distribución del trabajo parece razonable.
2. Comprueba si hay señales de desequilibrio claro entre personas o grupos.
3. Observa si la solución parece cumplir con:
   1. descansos,
   2. límites,
   3. criterios básicos de equidad,
   4. y consistencia operativa.
4. Si la solución cubre el trabajo, pero lo hace de forma muy forzada, no la valides todavía.
5. Si el resultado parece operativo, equilibrado y explicable, continúa hacia la decisión final.

Para el caso de referencia, pregúntate:
1. ¿La cobertura se logró de forma razonable o demasiado forzada?
2. ¿La asignación parece equilibrada entre conductores?
3. ¿La solución parece aplicable en el mundo real o solo válida en papel?

Cuando termines esta sección, deberías tener una lectura más completa de si la solución merece avanzar o si necesita corrección.

## Decidiendo qué corregir antes de validar

El último paso es convertir el análisis en una decisión práctica. Aquí el objetivo no es arreglarlo todo de una vez, sino identificar la siguiente capa correcta de corrección.

Antes de terminar, asegúrate de que:
1. Ya revisaste cobertura.
2. Ya analizaste conflictos.
3. Ya valoraste la viabilidad general.
4. Ya sabes si la solución puede avanzar o no.

Para decidir qué corregir antes de validar:
1. Si el problema principal es de **reglas**, vuelve a P22.
2. Si el problema principal es de **ausencias, inactividades o disponibilidad**, vuelve a P23.
3. Si el problema principal es de **cesión, transferencia o adscripción**, vuelve a P24 o P21 según corresponda.
4. Si el problema principal es del trabajo heredado, vuelve a Scheduling.
5. Si la solución es suficientemente completa y viable, prepárala para validación.
6. No valides una solución solo porque “casi funciona”. Valídala cuando entiendas por qué funciona y por qué los conflictos restantes son aceptables o están resueltos.

Para el caso de referencia, termina esta quick start solo cuando puedas afirmar una de estas dos cosas:
1. La solución de L1 ya es lo bastante sólida como para validarse.
2. Ya sabes exactamente qué capa debes corregir antes de volver a calcular.

Cuando termines esta sección, deberías tener una lectura clara de cobertura, conflictos y viabilidad, y una decisión práctica sobre el siguiente paso.

## Lecturas adicionales

- [Validando y consolidando la solución de Rostering](P27_Validando_y_consolidando_la_solucion_de_Rostering.md)
