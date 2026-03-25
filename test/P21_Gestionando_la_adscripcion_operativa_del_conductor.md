---
title: Gestionando la adscripción operativa del conductor
shortTitle: Adscripción operativa
intro: 'Aprende a vincular cada conductor con su depósito, unidad de negocio y grupo de trabajo, y a entender cómo esa adscripción condiciona su elegibilidad real antes de pasar a reglas, ausencias y cálculo de Rostering.'
contentType: how-tos
versions:
  - '*'
---

## Entendiendo la adscripción operativa del conductor

Antes de definir reglas avanzadas, ausencias o cálculos de Rostering, necesitas entender cómo queda **adscrito** cada conductor dentro de la organización. En GoalBus, la adscripción operativa no se basa en un solo campo. Se construye combinando tres coordenadas principales:
1. **Depósito**
2. **Unidad de negocio**
3. **Grupo de trabajo**

Esa combinación define desde dónde trabaja la persona, a qué división pertenece y qué tipo de tareas puede recibir. También condiciona la visibilidad del recurso para planificadores y gerentes. fileciteturn39file3L1-L20

Usa esta quick start cuando ya tengas cargada la plantilla de conductores y necesites asegurarte de que cada persona está ubicada en el contexto operativo correcto antes de pasar a reglas y disponibilidad.

Antes de empezar, asegúrate de que:
1. Ya cargaste y revisaste los conductores en P20.
2. Ya sabes qué depósitos, unidades y grupos usa tu operación.
3. Tienes claro qué colectivo de personal participará en el cálculo de Rostering.
4. Sabes que una mala adscripción puede volver inelegible a una persona aunque exista en el sistema.

Para esta quick start, usa este caso de referencia:

> **Voy a revisar que los conductores que cubrirán la línea L1 están adscritos al depósito, unidad y grupo de trabajo correctos antes de configurar reglas y disponibilidad.**

Para entender la adscripción operativa:
1. Trata el **depósito** como la ubicación física base del recurso.
2. Trata la **unidad de negocio** como la división estratégica o modal a la que pertenece la persona.
3. Trata el **grupo de trabajo** como la función que determina qué tipo de tareas puede recibir.
4. Usa esta regla de lectura:
   1. el depósito responde a **dónde trabaja**,
   2. la unidad responde a **en qué negocio o modo opera**,
   3. el grupo responde a **qué tipo de trabajo puede hacer**.
5. No mezcles estos tres conceptos como si fueran lo mismo.

Cuando termines esta sección, deberías tener claro que la adscripción operativa es una estructura compuesta y no un único atributo aislado. fileciteturn39file1turn39file3

## Revisando depósito, unidad y grupo de trabajo en el perfil del conductor

Una vez entendida la lógica, necesitas comprobar cómo está configurada en el perfil real del conductor. Estos campos forman parte del “ADN estructural” del empleado y son la base de su contexto operativo. Si están mal definidos, la asignación posterior se contamina desde el origen. fileciteturn39file0turn39file2

Antes de empezar esta sección, asegúrate de que:
1. Ya tienes conductores creados en la plantilla.
2. Ya sabes qué conductor o qué grupo usarás como muestra.
3. Quieres revisar la adscripción estructural, no todavía una cesión temporal.

Para revisar la adscripción en el perfil:
1. En la lista general de conductores, abre el perfil de una persona.
2. Revisa la barra lateral de datos estructurales.
3. Comprueba al menos:
   1. **Depósito principal**
   2. **Unidad de negocio**
   3. **Grupo de trabajo**
   4. **Área**, si tu operación la utiliza
4. Confirma que esos valores coinciden con el contexto real donde la persona debería trabajar.
5. Si un dato es incorrecto, actualízalo en el perfil.
6. Guarda los cambios.
7. Repite la revisión en varios conductores para confirmar que la plantilla es consistente.

Para el caso de referencia, comprueba que:
1. Los conductores de L1 pertenecen al depósito correcto.
2. La unidad de negocio coincide con el modo o negocio esperado.
3. El grupo de trabajo corresponde realmente a **Conductores** y no a otro rol.

Cuando termines esta sección, deberías tener revisada la adscripción estructural de los conductores que participarán en el cálculo. fileciteturn39file1turn39file2

## Entendiendo la diferencia entre adscripción principal, habilitación y cesión

Antes de seguir, necesitas distinguir tres conceptos que suelen confundirse:
1. **Adscripción principal**
2. **Habilitación**
3. **Cesión o transferencia temporal**

La adscripción principal define dónde pertenece la persona de forma estructural. La habilitación responde a si **puede** trabajar legal o técnicamente en otro contexto. La cesión responde a dónde **está trabajando realmente** durante un período temporal. Estas tres capas conviven, pero no significan lo mismo. fileciteturn39file0turn39file4

Antes de empezar esta sección, asegúrate de que:
1. Ya revisaste la adscripción principal en el perfil.
2. Ya sabes que algunas personas pueden trabajar fuera de su contexto principal.
3. Quieres evitar errores de interpretación entre “pertenece a”, “puede trabajar en” y “está trabajando en”.

Para distinguir correctamente estos conceptos:
1. Usa la **adscripción principal** para describir el contexto estructural base del conductor.
2. Usa la **habilitación** para indicar que el conductor puede trabajar en otro depósito, grupo o unidad.
3. Usa la **cesión** para indicar que el conductor está temporalmente desplazado a otro contexto.
4. No uses una cesión para corregir una adscripción principal mal definida.
5. No uses una habilitación como si fuera un traslado activo.
6. Mantén estas preguntas como guía:
   1. ¿Dónde pertenece esta persona? → adscripción principal
   2. ¿Dónde podría trabajar legalmente? → habilitación
   3. ¿Dónde está trabajando ahora mismo? → cesión

Para el caso de referencia, pregúntate:
1. ¿El conductor pertenece al Depósito Norte?
2. ¿Puede trabajar en otro depósito si fuese necesario?
3. ¿Está cedido temporalmente a otra base o sigue en su contexto habitual?

Cuando termines esta sección, deberías tener una lectura correcta de la jerarquía entre adscripción, habilitación y cesión. fileciteturn39file0turn39file4

## Validando que la adscripción permite ver y asignar correctamente al conductor

La adscripción no solo sirve para describir el perfil del conductor. También condiciona cómo lo ve el sistema y qué tareas puede recibir. Una persona mal adscrita puede quedar fuera del filtro correcto, aparecer en el lugar equivocado o recibir tareas que no le corresponden. También puede ocurrir lo contrario: que una persona válida quede oculta o inelegible por una adscripción mal definida. fileciteturn39file3L1-L20

Antes de continuar, asegúrate de que:
1. Ya revisaste depósito, unidad y grupo en varios perfiles.
2. Ya entiendes la diferencia entre adscripción y cesión.
3. Ya tienes claro qué colectivo participará en el próximo cálculo.

Para validar el impacto operativo de la adscripción:
1. Revisa qué conjunto de conductores debería estar visible para el contexto de tu cálculo.
2. Comprueba que las personas correctas aparecen bajo el depósito, unidad y grupo correctos.
3. Revisa si hay conductores en el grupo equivocado.
4. Revisa si hay conductores que deberían pertenecer al contexto y no aparecen como tales.
5. Si detectas un error de adscripción, corrígelo antes de pasar a reglas o disponibilidad.
6. Guarda la configuración final de los perfiles afectados.

Para el caso de referencia, asegúrate de que:
1. Los conductores que cubrirán L1 aparecen en el contexto operativo correcto.
2. No se mezclan con colectivos que no deberían recibir tareas de conducción.
3. El sistema podría filtrar y asignar solo al personal relevante.

Cuando termines esta sección, deberías tener una base de adscripción operativa que ayude al sistema a ver y usar a las personas correctas. fileciteturn39file3

## Confirmando que la adscripción operativa ya está lista para la siguiente capa

El último paso es comprobar que la adscripción quedó suficientemente sólida como para continuar con reglas, ausencias y cálculo. Aquí el objetivo no es solo haber rellenado campos, sino haber dejado una estructura clara que el motor pueda interpretar sin ambigüedades.

Antes de terminar, asegúrate de que:
1. Ya revisaste la adscripción estructural de los perfiles clave.
2. Ya distingues adscripción, habilitación y cesión.
3. Ya validaste que el colectivo visible es el correcto.
4. Ya corregiste los desajustes principales.

Para confirmar que la adscripción ya está preparada:
1. Vuelve a la lista general de conductores.
2. Revisa que el colectivo relevante para tu caso aparece en el contexto correcto.
3. Comprueba que no hay errores obvios de depósito, unidad o grupo.
4. Pregúntate si el sistema ya podría:
   1. filtrar correctamente a los conductores del caso,
   2. aplicarles reglas del colectivo correcto,
   3. y tratarlos como base para disponibilidad y cálculo.
5. Si la respuesta es sí, continúa con el siguiente quick start.
6. Si la respuesta es no, corrige la adscripción antes de seguir.

Para el caso de referencia, no continúes hasta poder afirmar:
1. Los conductores de L1 están adscritos al contexto correcto.
2. Sabes distinguir quién pertenece, quién puede trabajar y quién está cedido.
3. La base ya está lista para aplicar reglas de Rostering y disponibilidad.

Cuando termines esta sección, deberías tener una adscripción operativa suficientemente clara como para continuar con la siguiente capa del proceso.

## Lecturas adicionales

- [Definiendo reglas de Rostering para la asignación de personal](P22_Definiendo_reglas_de_Rostering_para_la_asignacion_de_personal.md)
