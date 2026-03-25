---
title: Pasando de Scheduling a Rostering
shortTitle: De Scheduling a Rostering
intro: 'Aprende qué debe quedar listo en Scheduling antes de entrar en Rostering, qué información hereda la asignación de personal y qué problemas deben resolverse antes de calcular conductores reales.'
contentType: how-tos
versions:
  - '*'
---

## Confirmando qué debe quedar cerrado en Scheduling antes de pasar a Rostering

Antes de entrar en Rostering, necesitas comprobar que Scheduling ya dejó una base suficientemente estable. Rostering no sustituye a Scheduling. Rostering parte del trabajo ya construido y decide cómo asignarlo a personas reales.

Usa esta quick start cuando ya tengas una solución de Scheduling calculada y validada, y necesites decidir si ya puedes empezar a trabajar con personal real.

Antes de empezar, asegúrate de que:
1. Ya creaste, calculaste y validaste el escenario de Scheduling.
2. Ya revisaste la oferta de servicio y su coherencia general.
3. Ya sabes qué líneas, qué tipo de día y qué solución usarás como referencia.
4. Tienes claro que Rostering no es el lugar para arreglar una mala base estructural de Scheduling.

Para esta quick start, usa este caso de referencia:

> **Voy a confirmar que la solución validada de Scheduling para la línea L1 ya está lo bastante madura como para pasar a Rostering y empezar a asignar trabajo a conductores reales.**

Para confirmar que Scheduling ya está listo:
1. Abre el escenario de Scheduling que usarás como referencia.
2. Comprueba que su estado ya es el correcto para dejar de tratarlo como borrador de trabajo.
3. Revisa que la oferta utilizada sigue siendo la correcta.
4. Revisa que la lógica de vehículos y la lógica de turnos ya fueron aplicadas.
5. Confirma que no quedan incoherencias estructurales evidentes en la solución.
6. Si todavía necesitas rehacer la base de vehículos, tiempos, servicios o reglas, vuelve a Scheduling antes de seguir.
7. Si la solución ya es estable, continúa al siguiente paso.

Para el caso de referencia, no continúes hasta poder afirmar:
1. La solución de L1 ya fue calculada.
2. Ya fue revisada.
3. Ya no necesita correcciones estructurales de Scheduling.
4. Ya puede tratarse como base de trabajo para personal.

Cuando termines esta sección, deberías tener claro si Scheduling ya entregó una base utilizable para Rostering.

## Entendiendo qué hereda Rostering desde Scheduling

Una vez confirmada la base, necesitas entender qué información pasa desde Scheduling a Rostering. Aquí la clave es no pensar que Rostering empieza desde cero. Rostering hereda el trabajo ya estructurado y a partir de ahí decide qué persona real puede asumirlo.

Antes de empezar esta sección, asegúrate de que:
1. Ya identificaste la solución de Scheduling que vas a usar.
2. Ya sabes qué parte de esa solución debe mantenerse estable.
3. Entiendes que Rostering trabaja sobre trabajo ya construido, no sobre una oferta sin estructurar.

Para entender qué hereda Rostering:
1. Revisa la solución validada de Scheduling.
2. Identifica las tareas, bloques o estructuras de trabajo que servirán como base.
3. Comprueba que la solución ya tiene una forma reconocible desde el punto de vista operativo.
4. Ten presente que, al pasar a Rostering, el sistema ya no está creando trabajo abstracto, sino intentando asignar ese trabajo a personas reales.
5. Usa esta regla de lectura:
   1. Scheduling define **qué trabajo existe**.
   2. Rostering define **quién hará ese trabajo**.

Para el caso de referencia, pregúntate:
1. ¿La solución de L1 ya tiene trabajo suficientemente claro como para asignarlo?
2. ¿Los bloques de trabajo son reconocibles y utilizables?
3. ¿El problema que queda por resolver ya es de personas y no de estructura?

Cuando termines esta sección, deberías entender qué hereda Rostering y qué no debería volver a redefinirse ahí.

## Distinguiendo qué problemas se resuelven en Scheduling y cuáles en Rostering

Antes de pasar definitivamente a la capa de personal, necesitas separar muy bien responsabilidades. Esta distinción es fundamental porque muchos errores aparecen cuando se intenta corregir en Rostering algo que debía haberse resuelto antes en Scheduling.

Antes de continuar, asegúrate de que:
1. Ya sabes qué escenario de Scheduling será la base.
2. Ya entiendes que Rostering consume una solución previa.
3. Estás preparado para distinguir problemas estructurales de problemas de personal.

Para separar correctamente ambos dominios:
1. Trata como problema de **Scheduling** cualquier asunto relacionado con:
   1. estructura del servicio,
   2. lógica de flota,
   3. tiempos,
   4. reglas de vehículos,
   5. tipos de turnos y su construcción base.
2. Trata como problema de **Rostering** cualquier asunto relacionado con:
   1. disponibilidad real del conductor,
   2. adscripción a depósito o grupo,
   3. ausencias,
   4. inactividades,
   5. cesiones o transferencias,
   6. elegibilidad real para recibir un turno.
3. Si detectas una incoherencia de trabajo que afecta a toda la estructura, vuelve a Scheduling.
4. Si detectas una incoherencia de persona, resuélvela en Rostering.

Para el caso de referencia, usa esta lógica:
1. Si el problema es que el trabajo de L1 quedó mal construido, vuelve a Scheduling.
2. Si el problema es que no sabes qué conductor real puede tomar ese trabajo, estás entrando correctamente en Rostering.

Cuando termines esta sección, deberías poder explicar con claridad qué debe corregirse antes de pasar a personal y qué sí pertenece al siguiente módulo.

## Confirmando qué debe estar listo del lado de personal antes de calcular Rostering

Ahora que ya sabes qué recibe Rostering, necesitas revisar qué debe existir del lado de personal para que el siguiente cálculo tenga sentido. No basta con tener un buen Scheduling si todavía no tienes una base mínima de personas, adscripciones y disponibilidad.

Antes de empezar esta sección, asegúrate de que:
1. Ya tienes una base válida desde Scheduling.
2. Ya sabes qué grupos, depósitos o contextos operativos afectan a las personas.
3. Ya estás preparado para revisar la capa de personal.

Para confirmar que la base de personal está lista:
1. Comprueba que ya existe un colectivo de personal que pueda recibir el trabajo.
2. Revisa que las personas estén adscritas al contexto correcto cuando aplique.
3. Comprueba que no estás entrando a Rostering sin información mínima de disponibilidad.
4. Revisa si ya existe la estructura necesaria para:
   1. reglas de Rostering,
   2. ausencias,
   3. inactividades,
   4. transferencias o cesiones, cuando apliquen.
5. Si todavía no tienes esta base, no lances el cálculo de personal.
6. Si la base ya existe o está al menos encaminada, continúa con los siguientes quick starts de Rostering.

Para el caso de referencia, pregúntate:
1. ¿Ya existe el personal que podrá recibir la solución de L1?
2. ¿Ese personal pertenece al ámbito correcto?
3. ¿La base de disponibilidad y adscripción ya está mínimamente preparada?

Cuando termines esta sección, deberías tener claro si el lado de personal ya está preparado para entrar en Rostering.

## Dejando claro el punto de transición entre Scheduling y Rostering

El último paso es cerrar mentalmente la transición. Este quick start no pretende calcular todavía la asignación de personal. Pretende dejar muy claro cuándo termina Scheduling y cuándo empieza Rostering para que no mezcles ambos dominios.

Antes de terminar, asegúrate de que:
1. Ya revisaste la solución de Scheduling.
2. Ya entendiste qué hereda Rostering.
3. Ya separaste problemas estructurales de problemas de personal.
4. Ya comprobaste si existe base mínima de personal.

Para cerrar correctamente la transición:
1. Trata la solución validada de Scheduling como entrada formal de Rostering.
2. No sigas alterando esa base salvo que detectes un problema estructural real.
3. Usa los siguientes quick starts para preparar:
   1. reglas de Rostering,
   2. ausencias e inactividades,
   3. transferencias, cesiones y cambios de adscripción.
4. Considera que el objetivo cambia a partir de aquí:
   1. ya no se trata de construir trabajo,
   2. ahora se trata de asignarlo a personas reales.
5. Si puedes afirmar eso con claridad, la transición está bien hecha.

Para el caso de referencia, termina esta quick start solo cuando puedas afirmar:
1. Scheduling ya dejó una solución estable de L1.
2. El siguiente problema ya no es estructural, sino de asignación de personal.
3. Ya puedes entrar a la capa de reglas de Rostering.

Cuando termines esta sección, deberías tener una transición clara y controlada entre Scheduling y Rostering.

## Lecturas adicionales

- [Definiendo reglas de Rostering para la asignación de personal](P20_Definiendo_reglas_de_Rostering_para_la_asignacion_de_personal.md)
