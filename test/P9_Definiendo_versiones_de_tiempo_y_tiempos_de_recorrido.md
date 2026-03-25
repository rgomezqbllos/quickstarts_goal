---
title: Definiendo versiones de tiempo y tiempos de recorrido para la operación
shortTitle: Versiones y tiempos
intro: 'Aprende a crear versiones de tiempo, definir tiempos de recorrido y permanencia por tipo de día y franja horaria, y dejar una referencia temporal fiable antes de crear o ajustar servicios en GoalBus.'
contentType: how-tos
versions:
  - '*'
---

## Creando la versión de tiempo que usará tu caso

Antes de definir tiempos de recorrido, necesitas crear una **versión de tiempo**. En GoalBus, una versión no es solo una etiqueta: es la biblioteca de tiempos que agrupa la lógica temporal que se aplicará a rutas concretas y a tipos de día concretos. Esto es importante porque un lunes por la mañana no se comporta igual que un domingo por la mañana, y el sistema no debería reutilizar un único conjunto de tiempos para todo el año.

Usa esta quick start cuando ya tengas una línea y sus rutas definidas, y necesites construir la base temporal que luego servirá para calcular viajes, validar duraciones y comparar desviaciones frente al estándar.

Antes de empezar, asegúrate de que:
1. Ya preparaste la red maestra en P4.
2. Ya revisaste la red operativa en P5.
3. Ya configuraste la base temporal de tipos de día en P2.
4. Ya validaste el año operativo en P3.
5. Ya sabes qué línea, qué rutas y qué tipo de día vas a usar como referencia.

Para esta quick start, usa este caso de referencia:

> **Voy a crear una versión de tiempo para la línea L1 en días laborables y usarla como referencia temporal antes de crear o ajustar servicios.**

Para crear la versión de tiempo de tu caso:
1. En GoalBus, abre la **vista Rutas** de la línea que usarás como referencia.
2. Selecciona el icono o la opción de **Gestión de tiempos de viaje y parada**.
3. En la parte superior de la vista, crea una **nueva versión**.
4. Define un **nombre** claro para la versión.
5. Añade una **descripción** que te ayude a distinguir el contexto operativo.
6. Selecciona los **tipos de día** a los que aplicará esa versión, por ejemplo **Días laborables**.
7. Vincula las **variaciones de ruta** o secuencias concretas que formarán parte de esa versión temporal.
8. Guarda la versión.
9. Revisa que la versión ya está disponible como referencia temporal para esa línea.

Para el caso de referencia, una versión válida podría llamarse:
- **Días laborables de invierno**
- **L1 laborable base**

Cuando termines esta sección, deberías tener creada una versión de tiempo que el sistema podrá usar como referencia temporal para los servicios de esa línea. fileciteturn28file0

## Definiendo tiempos de recorrido entre paradas principales

Después de crear la versión, necesitas introducir los **tiempos de recorrido**. En GoalBus, estos tiempos se definen principalmente entre **paradas principales** o **puntos temporales**, no entre todas las paradas intermedias. Las cabeceras son principales por defecto, y desde ahí se construye la lógica temporal que luego alimentará los servicios.

Además, GoalBus no trabaja con un único valor por segmento. El motor usa una lógica de **mínimo, óptimo y máximo** para dar flexibilidad controlada al cálculo:
1. **Mínimo**: el tiempo más rápido posible.
2. **Óptimo**: el tiempo objetivo al que tenderá el motor.
3. **Máximo**: el tiempo más lento aceptable.

Antes de empezar esta sección, asegúrate de que:
1. Ya creaste la versión de tiempo.
2. Ya sabes qué paradas principales usarás como referencia.
3. Ya identificaste el sentido o dirección que quieres configurar primero.

Para definir los tiempos de recorrido de tu caso:
1. Dentro de la cuadrícula temporal, selecciona el **segmento** entre dos paradas principales.
2. Crea una o más **franjas horarias** para reflejar la realidad operativa.
3. Para cada franja, introduce:
   1. el tiempo **mínimo**,
   2. el tiempo **óptimo**,
   3. el tiempo **máximo**.
4. Guarda el segmento.
5. Repite el proceso para el siguiente segmento principal.
6. Cuando termines un sentido, repite la misma lógica para el sentido contrario.

Para el caso de referencia, una lógica básica podría ser:
1. **Terminal Norte → Centro**
   1. 07:00–09:00
      1. Mínimo: 12 min
      2. Óptimo: 15 min
      3. Máximo: 18 min
   2. 22:00–06:00
      1. Mínimo: 8 min
      2. Óptimo: 10 min
      3. Máximo: 12 min
2. **Centro → Hospital**
3. **Hospital → Universidad**
4. **Universidad → Terminal Sur**

Cuando termines esta sección, deberías tener definidos tiempos de conducción elásticos entre los puntos temporales principales de la ruta. fileciteturn28file1turn28file3

## Definiendo tiempos de permanencia para regulación y recuperación

Además del tiempo de conducción, GoalBus necesita saber cuánto tiempo puede permanecer un vehículo en una parada principal. Estos **tiempos de permanencia** son importantes porque permiten regular la salida, absorber llegadas anticipadas y dejar margen de recuperación en terminales o puntos de conexión.

Antes de empezar esta sección, asegúrate de que:
1. Ya definiste tiempos de recorrido entre los principales segmentos.
2. Ya sabes qué terminales o puntos importantes necesitan regulación.
3. Ya identificaste dónde hace falta margen operativo real.

Para definir los tiempos de permanencia:
1. En la cuadrícula temporal, selecciona la **columna** de una parada principal.
2. Elige una terminal, cabecera o punto de conexión importante.
3. Define:
   1. **Mínimo**, como tiempo obligatorio de espera.
   2. **Máximo**, como margen permitido para regulación o sincronización.
4. Guarda la configuración.
5. Repite el proceso para otras paradas principales donde necesites permanencia controlada.

Para el caso de referencia, una lógica posible sería:
1. **Terminal Norte**
   1. Mínimo: 4 min
   2. Máximo: 10 min
2. **Terminal Sur**
   1. Mínimo: 5 min
   2. Máximo: 12 min

Cuando termines esta sección, deberías tener definidos los márgenes que el motor podrá usar para recuperar o regular sin deformar la lógica del horario. fileciteturn28file1turn28file3

## Revisando franjas horarias, vista ampliada y consistencia visual

Una vez que ya tienes tiempos de recorrido y permanencia, necesitas revisar si la cuadrícula refleja una lógica realista. El documento remarca que GoalBus incluye ayudas visuales para detectar errores cuando manejas muchos puntos de datos, muchas franjas o varias rutas.

Antes de continuar, asegúrate de que:
1. Ya configuraste al menos una franja horaria.
2. Ya introdujiste valores mínimo, óptimo y máximo.
3. Ya añadiste tiempos de permanencia en los puntos relevantes.

Para revisar visualmente la consistencia de la configuración:
1. Revisa la cuadrícula y confirma que cada segmento principal tiene una franja horaria válida.
2. Usa las ayudas visuales disponibles para detectar valores anómalos.
3. Comprueba si las horas punta muestran tiempos más altos que las horas valle.
4. Amplía la vista si necesitas ver más detalle o más paradas intermedias.
5. Corrige cualquier valor anómalo directamente desde la vista o desde el panel de edición.
6. Repite la revisión hasta que la lógica temporal refleje una operación creíble.

Para el caso de referencia, pregúntate:
1. ¿La hora punta aparece con tiempos más altos que la noche?
2. ¿Los tiempos mínimo, óptimo y máximo guardan una relación lógica?
3. ¿Las terminales tienen margen de regulación realista?
4. ¿La cuadrícula ya representa una jornada operativa completa?

Cuando termines esta sección, deberías tener una base temporal revisada visualmente y libre de incoherencias importantes. fileciteturn28file1turn28file3

## Aplicando la versión de tiempo como referencia para servicios

El objetivo final de esta quick start no es solo crear datos temporales, sino dejar una referencia que después pueda usarse al crear o modificar servicios. El documento indica que cada viaje debe medirse contra una **versión temporal de referencia**, y que esa referencia se usa automáticamente cuando creas nuevos viajes o cambias la ruta de un viaje. También permite detectar desviaciones si un viaje fue importado o modificado fuera del estándar.

Antes de terminar, asegúrate de que:
1. Ya creaste una versión temporal válida.
2. Ya definiste tiempos de recorrido y permanencia.
3. Ya revisaste la consistencia de la cuadrícula.
4. Ya sabes qué línea y qué caso usarás para crear servicios.

Para comprobar que tu base temporal ya está lista para los servicios:
1. Revisa la versión de tiempo que acabas de crear.
2. Confirma que está vinculada al tipo de día correcto.
3. Confirma que incluye las rutas o variaciones que vas a usar.
4. Comprueba que esa versión ya podría actuar como referencia temporal para:
   1. crear nuevos viajes,
   2. recalcular tiempos de llegada y salida,
   3. auditar discrepancias frente al estándar.
5. Si la respuesta es sí, continúa con el siguiente quick start.
6. Si la respuesta es no, vuelve atrás y corrige la versión o sus tiempos antes de seguir.

Cuando termines esta sección, deberías poder afirmar que la línea ya tiene una versión temporal de referencia suficiente para crear servicios de forma coherente. fileciteturn28file0turn28file4

## Lecturas adicionales

- [Creando la oferta de servicio base: viajes o grupos de servicios por línea, ruta y sentido](P10_Crear_la_oferta_de_servicio_base_viajes_o_grupo_de_servicios_por_linea_ruta_y_sentido_regenerado.md)
