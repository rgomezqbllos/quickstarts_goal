---
title: Definiendo reglas de Rostering para la asignación de personal
shortTitle: Reglas de Rostering
intro: 'Aprende a configurar reglas básicas y avanzadas de Rostering para que la asignación de personal respete límites laborales, criterios de equidad y restricciones operativas reales antes de calcular la plantilla.'
contentType: how-tos
versions:
  - '*'
---

## Entendiendo qué controlan las reglas de Rostering

Antes de calcular asignaciones de personal, necesitas definir las **reglas de Rostering** que guiarán cómo se asignan los empleados a los turnos. Estas reglas no construyen el trabajo, porque ese paso ya lo resolvió Scheduling. Aquí lo que haces es controlar cómo se reparte ese trabajo entre personas reales, respetando políticas operativas, criterios de equidad y límites laborales.

Usa esta quick start cuando ya tengas una solución de Scheduling suficientemente estable, una plantilla de conductores cargada y una adscripción operativa ya revisada.

Antes de empezar, asegúrate de que:
1. Ya cerraste la transición desde Scheduling en P19.
2. Ya cargaste y revisaste conductores en P20.
3. Ya validaste la adscripción operativa en P21.
4. Ya tienes claro qué solución de Scheduling actuará como base.
5. Ya sabes qué colectivo o grupo de empleados estará afectado por el cálculo.

Para esta quick start, usa este caso de referencia:

> **Voy a configurar las reglas de Rostering para la línea L1 y su grupo de conductores, de forma que el cálculo asigne personal real respetando descansos, límites de trabajo y criterios operativos.**

Para entender el papel de estas reglas:
1. Trata las reglas de Rostering como restricciones y preferencias sobre la asignación de personas.
2. Usa estas reglas cuando quieras controlar:
   1. descansos,
   2. tiempo de trabajo,
   3. patrones semanales,
   4. grupo de trabajo,
   5. emparejamientos,
   6. y otros criterios de equidad o política interna.
3. No uses estas reglas para corregir problemas de:
   1. oferta,
   2. tiempos,
   3. flota,
   4. o construcción base de turnos.
4. Si detectas que el problema sigue siendo estructural, vuelve a Scheduling antes de continuar.

Cuando termines esta sección, deberías tener claro que las reglas de Rostering gobiernan a las personas y no a la estructura base del trabajo.

## Distinguiendo entre reglas básicas y reglas avanzadas

Antes de crear un modelo de reglas, necesitas distinguir dos niveles de configuración:
1. **Reglas básicas**
2. **Reglas avanzadas**

Las reglas básicas están pensadas para configurar rápidamente restricciones comunes. Son útiles cuando quieres una parametrización ágil o una prueba inicial. Las reglas avanzadas están pensadas para modelar con mayor precisión restricciones y preferencias mediante límites y penalizaciones.

Antes de empezar esta sección, asegúrate de que:
1. Ya sabes si tu caso necesita rapidez o precisión.
2. Ya entiendes que las reglas básicas tienen menos flexibilidad de modelado que las avanzadas.
3. Ya sabes si vas a necesitar modelos distintos según el uso.

Para elegir el tipo de reglas adecuado:
1. Usa **reglas básicas** si quieres cubrir rápidamente restricciones comunes.
2. Usa **reglas avanzadas** si necesitas modelar con detalle políticas complejas, convenios o condiciones operativas específicas.
3. Ten en cuenta que las reglas básicas activas se aplican tanto en operación diaria como en escenarios de cálculo de asignación.
4. Si necesitas modelos distintos para contextos distintos, por ejemplo uno para operación diaria y otro para un cálculo futuro, trabaja con reglas avanzadas.
5. Decide qué enfoque usarás antes de empezar a parametrizar.

Para el caso de referencia, usa esta lógica:
1. Si estás empezando y quieres una primera capa de control, comienza por reglas básicas.
2. Si ya sabes que necesitarás ajustar preferencias, penalizaciones o modelos por contexto, continúa con reglas avanzadas.

Cuando termines esta sección, deberías tener claro si tu caso se resolverá con reglas básicas, avanzadas o una combinación controlada de ambas.

## Activando las reglas básicas más comunes para una primera asignación

Si tu caso necesita una configuración inicial rápida, puedes empezar por las **reglas básicas**. Estas cubren las restricciones más habituales y permiten poner en marcha el cálculo con una base razonable antes de entrar en niveles más finos de control.

Antes de empezar esta sección, asegúrate de que:
1. Ya decidiste comenzar con reglas básicas.
2. Ya sabes qué restricciones mínimas quieres imponer.
3. Tienes claro que no todas las reglas deben activarse por defecto.

Para activar reglas básicas:
1. En GoalBus, ve a **Configuración** > **Reglas de asignación**.
2. Abre la sección **Reglas básicas**.
3. Revisa el catálogo de reglas disponibles.
4. Activa solo las que correspondan al caso que estás construyendo.
5. Configura, cuando aplique:
   1. límites generales,
   2. límites específicos por propiedades de empleado,
   3. o excepciones para ciertos empleados.
6. Guarda los cambios.
7. Revisa que las reglas activas realmente reflejen las políticas que quieres imponer.

Una base inicial de reglas básicas puede incluir:
1. **Patrón de trabajo**
2. **Descanso entre días**
3. **Tiempo de trabajo mensual**
4. **Tiempo de trabajo semanal**
5. **Día libre por semana**
6. **Días laborables consecutivos**
7. **Grupo de trabajo**
8. **Emparejamiento**
9. **Activación de la línea**, cuando aplique

Para el caso de referencia, no actives una regla solo porque exista. Actívala solo si:
1. responde a una necesidad real,
2. puedes explicar por qué la necesitas,
3. y sabes cómo afectará a la asignación.

Cuando termines esta sección, deberías tener una primera base de control para la asignación de personal.

## Creando un modelo de reglas avanzadas cuando necesites más precisión

Si las reglas básicas no son suficientes, el siguiente paso es crear un **modelo de reglas avanzadas**. Este enfoque te permite controlar con precisión cómo se generan las asignaciones, ajustando límites y preferencias según políticas de empresa, acuerdos laborales y condiciones reales de operación.

Antes de empezar esta sección, asegúrate de que:
1. Ya identificaste qué parte del caso no puede resolverse bien con reglas básicas.
2. Ya sabes qué comportamientos deben ser obligatorios y cuáles solo preferidos.
3. Ya necesitas un modelo más fino que pueda reutilizarse por escenario o contexto.

Para crear un modelo de reglas avanzadas:
1. En **Configuración** > **Reglas de asignación**, abre la sección **Reglas avanzadas**.
2. Crea un nuevo modelo de reglas.
3. Asigna un **nombre** claro al modelo.
4. Añade una **descripción** que te permita distinguirlo de otros modelos.
5. Guarda el modelo.
6. Empieza a añadir reglas avanzadas una por una.
7. Para cada regla, decide:
   1. si actúa como límite obligatorio,
   2. o si actúa como preferencia mediante penalización.
8. Guarda la configuración del modelo.
9. Revisa que el modelo ya pueda asignarse al cálculo de Rostering adecuado.

Para el caso de referencia, una opción válida podría ser:
- **Rostering L1 laborable**
- **Asignación conductores L1 - reglas avanzadas**

Cuando termines esta sección, deberías tener un modelo avanzado listo para representar restricciones y preferencias más complejas.

## Relacionando las reglas con el colectivo correcto y con el cálculo real

Después de activar reglas básicas o crear un modelo avanzado, necesitas comprobar que las reglas aplican al colectivo correcto y que no estás imponiendo restricciones abstractas sin relación con el cálculo real.

Antes de continuar, asegúrate de que:
1. Ya activaste reglas básicas o creaste un modelo avanzado.
2. Ya sabes qué empleados, grupos o depósitos participarán en el cálculo.
3. Ya tienes claro qué solución de Scheduling servirá como entrada.

Para relacionar correctamente las reglas con el contexto de cálculo:
1. Revisa el colectivo de personal al que se aplicará Rostering.
2. Comprueba si las reglas afectan:
   1. a toda la plantilla implicada,
   2. a un grupo específico,
   3. o a empleados con propiedades concretas.
3. Confirma que no estás imponiendo reglas sobre personas que ni siquiera participarán en ese cálculo.
4. Revisa si la lógica del escenario de Scheduling sigue siendo compatible con estas reglas.
5. Si una regla vuelve inviable el reparto del trabajo, ajusta su límite o su ámbito.
6. Guarda la versión final de la configuración.

Para el caso de referencia, pregúntate:
1. ¿Estas reglas están pensadas para los conductores que realmente cubrirán L1?
2. ¿El grupo de trabajo afectado es el correcto?
3. ¿La asignación sigue siendo viable después de activar estas reglas?

Cuando termines esta sección, deberías tener una configuración de reglas conectada con personas reales y con un cálculo de Rostering concreto.

## Confirmando que la base de reglas ya está lista para calcular Rostering

El último paso es asegurarte de que tu configuración ya está lista para alimentar el cálculo de personal. No se trata solo de haber activado reglas, sino de haber dejado una base coherente, comprensible y aplicable.

Antes de terminar, asegúrate de que:
1. Ya elegiste entre reglas básicas y avanzadas según el caso.
2. Ya activaste o modelaste las restricciones necesarias.
3. Ya vinculaste la lógica al colectivo correcto.
4. Ya comprobaste que la asignación sigue siendo viable.

Para validar que la base de reglas ya está lista:
1. Revisa el conjunto final de reglas activas.
2. Confirma que cada una responde a una necesidad real.
3. Pregúntate si el sistema ya podría:
   1. bloquear asignaciones no válidas,
   2. respetar descansos y límites,
   3. reflejar criterios de equidad y grupo de trabajo,
   4. y seguir generando una solución utilizable.
4. Si la respuesta es sí, continúa con el siguiente quick start.
5. Si la respuesta es no, ajusta las reglas antes de seguir.

Para el caso de referencia, no continúes hasta poder afirmar:
1. Las reglas de Rostering para L1 ya están claras.
2. Sabes por qué activaste cada regla.
3. El sistema todavía puede asignar personas reales con esa configuración.
4. La base ya está preparada para tratar disponibilidad y excepciones de personal.

Cuando termines esta sección, deberías tener una base de reglas de Rostering suficientemente sólida como para pasar al tratamiento de ausencias, inactividades y disponibilidad.

## Lecturas adicionales

- [Gestionando ausencias, inactividades y disponibilidad de personal](P23_Gestionando_ausencias_inactividades_y_disponibilidad_de_personal.md)
