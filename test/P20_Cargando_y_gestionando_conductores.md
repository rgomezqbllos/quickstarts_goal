---
title: Cargando y gestionando conductores
shortTitle: Conductores
intro: 'Aprende a crear, importar y mantener la base de conductores en GoalBus, revisar su perfil operativo y dejar una plantilla fiable antes de pasar a adscripción, reglas y cálculo de Rostering.'
contentType: how-tos
versions:
  - '*'
---

## Creando o importando la plantilla de conductores

Antes de hablar de reglas de Rostering, ausencias o asignación de turnos, necesitas tener una base fiable de conductores. En GoalBus, la gestión de conductores actúa como la fuente principal de verdad para la operatividad humana: permite combinar creación manual y carga masiva, y concentra identidad, afiliación al depósito y disponibilidad en un mismo directorio. fileciteturn38file2L1-L24

Usa esta quick start cuando ya tengas clara la transición desde Scheduling a Rostering y necesites preparar el colectivo real de personas que participará en la asignación.

Antes de empezar, asegúrate de que:
1. Ya cerraste la transición desde Scheduling en P19.
2. Tienes claro qué colectivo de conductores participará en el cálculo.
3. Sabes si vas a dar de alta unos pocos conductores manualmente o si necesitas una carga masiva.
4. Tienes acceso al entorno con permisos para gestionar personal.

Para esta quick start, usa este caso de referencia:

> **Voy a cargar y revisar la plantilla de conductores que podrá cubrir la solución de L1 antes de entrar en adscripción, reglas y disponibilidad.**

Para crear o importar la plantilla de conductores:
1. En GoalBus, ve al módulo de **Gestión de conductores**.
2. Revisa si los conductores del caso ya existen en la lista general.
3. Si necesitas crear pocos conductores, usa la **creación manual**.
4. Si necesitas cargar muchos conductores, usa la **importación masiva** mediante archivo CSV.
5. Si eliges importación masiva, prepara el archivo con los datos mínimos que tu operación necesita para identificar correctamente a cada persona.
6. Ejecuta la carga y revisa el resultado.
7. Vuelve a la lista general y comprueba que los conductores aparecen correctamente.
8. Si detectas duplicados o registros incompletos, corrígelos antes de seguir.

Para el caso de referencia, termina esta sección solo cuando puedas afirmar:
1. Los conductores de L1 ya están dados de alta o importados.
2. La lista general refleja una única plantilla de referencia.
3. Ya puedes abrir el perfil de cada conductor para revisar su contexto operativo.

Cuando termines esta sección, deberías tener una plantilla de conductores cargada y visible en el sistema. fileciteturn38file0L1-L7 fileciteturn38file2L1-L24

## Revisando el perfil del conductor y sus datos estructurales

Una vez creada la plantilla, necesitas revisar el **perfil del conductor**. El perfil no es solo una ficha de contacto: es el expediente digital completo del empleado dentro de la operación. Ahí conviven datos estáticos, contexto operativo y atributos que el sistema usará más adelante para razonar sobre su elegibilidad. fileciteturn38file0L8-L20 fileciteturn38file2L25-L40

Antes de empezar esta sección, asegúrate de que:
1. Ya tienes conductores visibles en la lista general.
2. Ya sabes qué conductor o qué grupo usarás como muestra.
3. Quieres validar que el registro no es solo administrativo, sino operativo.

Para revisar el perfil del conductor:
1. En la lista general, haz clic en el nombre de un conductor.
2. Revisa la barra lateral de datos estáticos.
3. Comprueba al menos estos grupos de información:
   1. datos básicos, como nombre y código,
   2. datos operativos, como convenio colectivo o tipo de contrato,
   3. enlaces operativos, como depósito principal, grupo de trabajo, área o tipos de vehículos autorizados.
4. Si algún dato estructural clave falta, complétalo antes de seguir.
5. Guarda cualquier cambio necesario.
6. Repite la revisión en varios conductores para confirmar consistencia en la plantilla.

Para el caso de referencia, revisa al menos:
1. El código del conductor.
2. Su depósito principal.
3. Su grupo de trabajo.
4. Las propiedades operativas que condicionarán su asignación posterior.

Cuando termines esta sección, deberías tener claro que cada conductor cuenta con un expediente operativo coherente y utilizable. fileciteturn38file0L8-L20

## Revisando el contexto operativo y los datos dinámicos del conductor

Además de los datos estructurales, el perfil del conductor incluye datos dinámicos que afectan directamente a cómo el sistema razona sobre la persona. En la pestaña de administración puedes revisar contadores y patrones de trabajo, que forman parte del contexto operativo usado más adelante por la lógica de asignación. fileciteturn38file0L12-L17

Antes de empezar esta sección, asegúrate de que:
1. Ya revisaste los datos estáticos del perfil.
2. Ya sabes si tu operación usa contadores o patrones cíclicos.
3. Quieres comprobar que el conductor no solo existe, sino que tiene un contexto operativo interpretable.

Para revisar el contexto operativo dinámico:
1. Dentro del perfil del conductor, abre la pestaña de **Detalles de administración**.
2. Revisa los **contadores** o KPI asociados al conductor si existen.
3. Comprueba si el conductor está vinculado a algún **patrón de trabajo**.
4. Si tu operación usa patrones cíclicos, revisa también el desfase o posición actual del conductor dentro del patrón.
5. Confirma que estos datos tienen sentido para el contexto real.
6. Si la información dinámica no es correcta, ajústala antes de pasar a reglas o cálculo.

Para el caso de referencia, pregúntate:
1. ¿Este conductor tiene el patrón que debería tener?
2. ¿Sus contadores o KPI están disponibles si el proceso los necesita?
3. ¿El sistema podría razonar correctamente sobre esta persona en un cálculo de asignación?

Cuando termines esta sección, deberías tener validada no solo la identidad del conductor, sino también su contexto operativo dinámico. fileciteturn38file0L12-L17

## Validando habilitaciones antes de usar al conductor en Rostering

Antes de considerar a un conductor como elegible, necesitas revisar sus **habilitaciones**. Estas habilitaciones responden a la pregunta “¿puede esta persona trabajar legal o técnicamente en este depósito, grupo o unidad?”. Se gestionan en una línea temporal con fecha de inicio y fin, y el sistema muestra estados como activo, futuro, caducado o próximo a caducar para facilitar la lectura. Si una persona no está habilitada para el contexto requerido, el motor genera un error al intentar asignarla. fileciteturn38file0L17-L34

Antes de empezar esta sección, asegúrate de que:
1. Ya revisaste el perfil del conductor.
2. Ya sabes qué depósito, grupo o unidad necesitará para tu caso.
3. Entiendes que una habilitación no es lo mismo que una cesión o una adscripción temporal.

Para revisar y validar las habilitaciones:
1. Dentro del perfil del conductor, abre la pestaña **Habilitaciones / Cualificaciones**.
2. Revisa si existen registros vigentes para:
   1. depósitos,
   2. grupos de trabajo,
   3. unidades de negocio.
3. Comprueba el estado visual de cada habilitación:
   1. activa,
   2. futura,
   3. próxima a caducar,
   4. caducada.
4. Si falta una habilitación necesaria, añádela con sus fechas correctas.
5. Si una habilitación ya caducó y no debería usarse, déjala como histórico sin intentar reescribir el pasado.
6. Guarda los cambios.
7. Confirma que el conductor ya está habilitado para el contexto donde esperas usarlo.

Para el caso de referencia, no continúes hasta poder afirmar:
1. El conductor está habilitado para el depósito correcto.
2. El grupo de trabajo requerido está cubierto.
3. No hay caducidades que rompan la elegibilidad actual.

Cuando termines esta sección, deberías tener conductores que no solo existen en la plantilla, sino que también son elegibles desde el punto de vista operativo y normativo. fileciteturn38file0L17-L34

## Confirmando que la plantilla ya está lista para la siguiente capa de Rostering

El último paso es comprobar que la base de conductores ya está lista para entrar en la siguiente capa: adscripción operativa, reglas, ausencias y cálculo. Aquí el objetivo no es solo tener nombres cargados, sino una plantilla coherente, trazable y utilizable por el motor.

Antes de terminar, asegúrate de que:
1. Ya cargaste o importaste la plantilla.
2. Ya revisaste los perfiles principales.
3. Ya comprobaste datos estructurales y dinámicos.
4. Ya validaste habilitaciones esenciales.

Para confirmar que la plantilla ya está preparada:
1. Vuelve a la lista general de conductores.
2. Revisa que el colectivo necesario para tu caso está presente.
3. Comprueba que los perfiles críticos no tienen huecos de información importantes.
4. Asegúrate de que las personas que esperas usar están habilitadas para el contexto correcto.
5. Pregúntate si el sistema ya podría usar esta base como punto de partida para:
   1. adscripción operativa,
   2. reglas de Rostering,
   3. y disponibilidad real.
6. Si la respuesta es sí, continúa con el siguiente quick start.
7. Si la respuesta es no, corrige la base de conductores antes de seguir.

Para el caso de referencia, termina esta quick start solo cuando puedas afirmar:
1. La plantilla de conductores de L1 ya está cargada.
2. Los perfiles clave ya fueron revisados.
3. Las habilitaciones esenciales ya están vigentes.
4. La base ya está lista para pasar a adscripción operativa.

Cuando termines esta sección, deberías tener una plantilla de conductores suficientemente sólida como para continuar con la siguiente capa de Rostering.

## Lecturas adicionales

- [Gestionando la adscripción operativa del conductor](P21_Gestionando_la_adscripcion_operativa_del_conductor.md)
