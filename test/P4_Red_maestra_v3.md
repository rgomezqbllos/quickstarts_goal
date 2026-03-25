---
title: Preparando la red maestra con paradas, líneas y rutas
shortTitle: Red maestra
intro: "Aprende a crear y validar la base de red que usará tu planificación, incluyendo paradas, líneas y rutas, para que los siguientes pasos de tiempos, servicios y Scheduling partan de una estructura coherente."
contentType: how-tos
versions:
  - "*"
---

## Creando o validando las paradas que usará tu red

Antes de crear líneas o rutas, necesitas asegurarte de que las **paradas** que usarás ya existen y están correctamente definidas. En GoalBus, una parada no es solo un punto geográfico. También es una entidad con identidad operativa y con varias capas de nombre que sirven para distintos públicos, como planificadores, pasajeros y dispositivos internos. Además, el sistema permite desactivar paradas en lugar de eliminarlas de forma brusca, para no romper rutas o viajes activos. fileciteturn20file3L1-L20 fileciteturn20file4L1-L16

Usa esta quick start cuando ya hayas cerrado la base temporal en P2 y P3, y necesites empezar a construir la red base sobre la que después vas a definir rutas, tiempos de recorrido y servicios.

Antes de empezar, asegúrate de que:

1. Ya configuraste los tipos de día y festivos en P2.
2. Ya validaste el año operativo en P3.
3. Tienes acceso al entorno con permisos para consultar o editar infraestructura de red.
4. Ya tienes claro qué línea o corredor quieres preparar como primer caso.

Para esta quick start, usa este caso de referencia:

> **Voy a preparar la línea L1, crear o validar sus paradas base y dejar listas sus rutas de ida y vuelta para usarlas más adelante en mi primer caso de Scheduling.**

Para crear o validar las paradas de tu caso:

1. En GoalBus, ve al módulo de **paradas** dentro de la configuración de infraestructura de red.
2. Busca si las paradas base de tu caso ya existen.
3. Si una parada ya existe, ábrela y confirma que su identidad es correcta.
4. Si una parada no existe, haz clic en **Crear parada**.
5. Introduce o valida estos campos:
   1. **Código** como identificador único.
   2. **Nombre comercial** como nombre visible para el pasajero.
   3. **Nombre largo** como referencia descriptiva interna.
   4. **Nombre corto** si lo necesitas para vistas compactas.
6. Define la ubicación de la parada mediante coordenadas o dirección.
7. Guarda la parada.
8. Repite el proceso hasta que tengas las paradas mínimas necesarias para tu caso.
9. Si detectas una parada antigua que no debería seguir usándose en nueva planificación, cámbiala a **Inactiva** en lugar de eliminarla.

Para el caso de referencia, usa una lógica como esta:

1. Terminal Norte
2. Centro
3. Hospital
4. Universidad
5. Terminal Sur

Cuando termines esta sección, deberías tener las paradas base listas y en un estado coherente para construir la línea y las rutas.

## Creando o validando la línea como contenedor operativo

Después de tener las paradas base, necesitas revisar la **línea**. En GoalBus, una línea es más que un simple número de servicio. Es un contenedor de lógica operativa. Al configurarla correctamente, defines límites físicos y logísticos del servicio, como el tipo de flota permitido o la geografía operativa de depósitos y parkings que después influirá en la optimización. fileciteturn20file2L17-L33

Antes de empezar esta sección, asegúrate de que:

1. Ya revisaste o creaste las paradas base de tu caso.
2. Ya sabes qué servicio quieres representar.
3. Tienes claro que la línea es el contenedor administrativo y no todavía el trayecto físico detallado.

Para crear o validar la línea de tu caso:

1. En GoalBus, ve al módulo de **líneas**.
2. Busca si la línea que necesitas ya existe.
3. Si la línea ya existe, ábrela y revisa su configuración.
4. Si no existe, crea una nueva línea.
5. Define o valida:
   1. **Nombre corto** para vistas compactas.
   2. **Nombre largo** para referencia interna.
   3. **Nombre comercial**, si aplica.
6. Revisa que la línea realmente representa el servicio correcto.
7. Guarda la línea.
8. Confirma que la línea ya puede usarse como contenedor para crear rutas específicas.

Para el caso de referencia, puedes pensar en una línea como:

- **L1**
- **L1: Terminal Norte - Terminal Sur**

Cuando termines esta sección, deberías tener una línea clara y usable sobre la que luego podrás definir rutas por sentido.

## Creando o validando las rutas de ida y vuelta

Con la línea ya lista, ahora sí puedes trabajar con las **rutas**. En GoalBus, una ruta es el trayecto físico real que recorre un vehículo. Una misma línea puede tener varias rutas válidas, por ejemplo giros cortos, desvíos o entradas a depósito. El sistema organiza estas variaciones por dirección o sentido, y protege las rutas “en uso” para evitar cambios peligrosos en servicios ya activos. fileciteturn20file1L1-L20

Antes de empezar esta sección, asegúrate de que:

1. Ya tienes la línea creada o validada.
2. Ya tienes las paradas base que usarás en la secuencia.
3. Sabes si vas a crear una sola ruta por sentido o si tu caso ya necesita variantes.

Para crear o validar las rutas de tu caso:

1. En la tabla principal de líneas, haz clic en la línea que acabas de crear o validar para acceder a la vista de rutas.
2. Usa las pestañas o controles de dirección para trabajar por **Sentido 1** y **Sentido 2**.
3. Revisa si ya existe una ruta adecuada para el sentido que necesitas.
4. Si la ruta no existe, crea una nueva variación de ruta para ese sentido.
5. Define la secuencia de paradas en el orden correcto.
6. Confirma la cabecera de inicio y la cabecera de fin.
7. Guarda la ruta.
8. Repite la lógica para el sentido contrario.
9. Si encuentras una ruta marcada como **En uso**, no intentes alterar su geometría básica sin revisar antes si existe una alternativa desbloqueada.

Para el caso de referencia:

1. Define la ruta de ida:
   1. Terminal Norte
   2. Centro
   3. Hospital
   4. Universidad
   5. Terminal Sur
2. Define la ruta de vuelta:
   1. Terminal Sur
   2. Universidad
   3. Centro
   4. Terminal Norte

Cuando termines esta sección, deberías tener una línea con sus rutas principales por sentido, lista para que en el siguiente quick start revises con más detalle secuencias, puntos relevantes y lógica operativa.

## Lecturas adicionales

- [Revisando la red operativa: secuencias, permisos de parada y puntos de relevo]
