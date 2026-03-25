---
title: Definiendo tipos de vehículo y flota permitida por línea
shortTitle: Flota por línea
intro: 'Aprende a configurar los tipos de vehículo y las restricciones de flota permitida por línea para que GoalBus bloquee asignaciones inviables, respete límites físicos y ambientales, y prepare una base coherente antes de definir tiempos y servicios.'
contentType: how-tos
versions:
  - '*'
---

## Definiendo los tipos de vehículo permitidos para una línea

Antes de pasar a tiempos de recorrido, servicios o reglas de Scheduling, necesitas dejar claro qué **tipos de vehículo** pueden operar cada línea. En GoalBus, esta restricción no es decorativa: actúa como un filtro de seguridad, cumplimiento y viabilidad física. El objetivo es evitar que el sistema proponga un vehículo que no cabe en una calle, que incumple una restricción ambiental o que no debería circular en ese servicio.

Usa esta quick start cuando ya tengas red, parkings y depósitos preparados, y necesites cerrar la base de flota que usará tu caso antes de definir tiempos y oferta de servicio.

Antes de empezar, asegúrate de que:
1. Ya preparaste la red maestra en P4.
2. Ya revisaste la red operativa en P5.
3. Ya configuraste parkings y depósitos en P6.
4. Tienes claro qué línea usarás como caso de referencia.
5. Ya sabes, al menos a nivel básico, qué restricciones físicas o ambientales afectan esa línea.

Para esta quick start, usa este caso de referencia:

> **Voy a definir qué tipos de vehículo puede operar la línea L1 para asegurarme de que mi primera planificación solo use una flota coherente con la realidad física y normativa del servicio.**

Para definir los tipos de vehículo permitidos de tu caso:
1. En GoalBus, abre la configuración de la **línea** que vas a usar como referencia.
2. Busca la sección **Tipos de vehículos permitidos**.
3. Revisa si la línea ya tiene tipos asignados.
4. Si la línea ya tiene tipos definidos, confirma que siguen siendo correctos para el caso.
5. Si todavía no están definidos, revisa primero si el **tipo de vehículo** que necesitas ya existe en la configuración general de vehículos.
6. Si el tipo **sí existe**, selecciónalo como permitido para esa línea.
7. Si el tipo **no existe**, sal de la configuración de la línea y ve a la configuración general de **vehículos** para crear o completar primero el catálogo de tipos disponible.
8. Crea el tipo de vehículo que necesitas usando una categoría clara y entendible para el negocio, por ejemplo:
   1. Minibús
   2. Estándar eléctrico
   3. Diésel articulado
9. Guarda el nuevo tipo de vehículo.
10. Vuelve a la configuración de la línea.
11. Marca los tipos de vehículo específicos que sí están autorizados para operar en esa línea.
12. Deja sin marcar los tipos que no deban operar ese servicio.
13. Guarda la configuración.
14. Vuelve a revisar la línea y confirma que el filtro ya representa correctamente la realidad operativa.

Para el caso de referencia, pregúntate:
1. ¿La línea L1 admite un autobús estándar, un minibús o ambos?
2. ¿Hay un tipo de vehículo que deba quedar excluido por tamaño o entorno?
3. Si no existía el tipo que necesitas, ¿ya lo creaste antes de intentar asignarlo a la línea?
4. ¿El sistema debería bloquear una asignación manual si intentaras usar un vehículo no autorizado?

Cuando termines esta sección, deberías tener definida una restricción de flota por línea que ya sirva como base para el cálculo posterior.

## Relacionando la línea con los depósitos o parkings permitidos

Después de definir qué flota cabe o no cabe en la línea, necesitas revisar desde qué bases físicas puede salir ese servicio. GoalBus permite definir **aparcamientos o depósitos permitidos** por línea para obligar al sistema a iniciar servicio desde ubicaciones geográficamente correctas y reducir el kilometraje en vacío.

Antes de empezar esta sección, asegúrate de que:
1. Ya configuraste los tipos de vehículo permitidos de la línea.
2. Ya preparaste los parkings y depósitos del caso en P6.
3. Ya sabes desde qué base operativa debería comenzar realmente el servicio.

Para relacionar la línea con sus depósitos o parkings permitidos:
1. Dentro de la misma configuración de la línea, localiza la sección **Aparcamientos permitidos** o **Depósitos permitidos**.
2. Revisa si la línea ya tiene depósitos autorizados.
3. Selecciona únicamente los depósitos o cocheras que sí estén geográficamente autorizados para iniciar los servicios de esa línea.
4. Deja fuera las bases que no tengan sentido operativo para ese corredor.
5. Guarda la configuración.
6. Revisa que la línea ahora tenga una lógica coherente de salida desde la base más razonable.

Para el caso de referencia, comprueba que:
1. La línea L1 puede salir desde el Depósito Norte.
2. El parking principal asociado es el correcto.
3. No estás dejando permitido un depósito lejano que obligue a recorrer muchos kilómetros en vacío para iniciar el primer viaje.

Cuando termines esta sección, deberías tener alineadas la línea, la flota permitida y la geografía de salida del servicio.

## Validando que la línea ya tiene una base de flota coherente

Ahora que ya definiste los tipos de vehículo permitidos y los depósitos o parkings autorizados, necesitas hacer una validación final.

Antes de continuar, asegúrate de que:
1. La línea ya tiene tipos de vehículo permitidos.
2. Si no existía el tipo de vehículo necesario, ya fue creado previamente en la configuración general.
3. La línea ya tiene depósitos o parkings autorizados.
4. La configuración refleja la realidad del caso que estás construyendo.

Para validar que la base de flota ya está lista:
1. Revisa nuevamente la configuración completa de la línea.
2. Confirma que los tipos de vehículo seleccionados representan la flota que realmente debería operar ese servicio.
3. Confirma que los depósitos o parkings autorizados minimizan el kilometraje en vacío.
4. Pregúntate si el sistema, con esta configuración, ya evitaría:
   1. asignaciones físicamente imposibles,
   2. incumplimientos ambientales,
   3. salidas desde bases geográficamente ineficientes.
5. Si la respuesta es sí, continúa con el siguiente quick start.
6. Si la respuesta es no, corrige la línea o crea el tipo de vehículo faltante antes de seguir.

Cuando termines esta sección, deberías poder afirmar que la línea ya tiene una base de flota suficientemente madura como para sostener tiempos de recorrido, servicios y reglas de Scheduling.

## Lecturas adicionales

- [Definiendo tiempos de recorrido y tiempos asociados a la operación](P9_Definiendo_tiempos_de_recorrido_y_tiempos_asociados_a_la_operacion.md)
