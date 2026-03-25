---
title: Validando el año operativo antes de planificar
shortTitle: Año operativo
intro: 'Aprende a validar el año operativo que sostendrá tu caso de planificación para evitar huecos, solapamientos o cortes artificiales en los datos antes de pasar a red, infraestructura y servicios.'
contentType: how-tos
versions:
  - '*'
---

## Creando o validando el año operativo que usará tu planificación

Antes de seguir con red, tiempos, servicios o reglas, necesitas comprobar que el período que quieres planificar cae dentro del **año operativo correcto**. En GoalBus, el año operativo existe para adaptar la lógica temporal del sistema a la realidad del negocio. Esto es importante porque muchas operaciones no siguen el año natural de enero a diciembre. Por ejemplo, una operación escolar puede trabajar de septiembre a agosto, y un contrato fiscal o sindical puede necesitar otro rango distinto.

Usa esta quick start cuando ya tengas definida la lógica de tipos de día y festivos, cuando quieras preparar tu primer caso de planificación real, o cuando necesites confirmar que el período que vas a usar está soportado por una línea temporal válida.

Antes de empezar, asegúrate de que:
1. Ya revisaste el rol del planificador en P1.
2. Ya configuraste o validaste los tipos de día y festivos en P2.
3. Sabes exactamente qué período quieres planificar.
4. Tienes acceso al entorno con permisos para consultar o editar la configuración temporal.

Para esta quick start, usa este caso de referencia:

> **Voy a planificar enero de 2026 y necesito confirmar que ese período cae dentro del año operativo correcto antes de seguir con mi primera planificación.**

Para crear o validar el año operativo de tu caso:
1. En GoalBus, ve a **Configuración**.
2. Abre la sección **Años operativos**.
3. Revisa los años operativos existentes y busca cuál debería cubrir el período que quieres planificar.
4. Si no existe un año operativo adecuado, haz clic en la opción para crear uno nuevo.
5. Define un **nombre único** y, si lo necesitas, una **descripción**.
6. Ajusta la **fecha de inicio** y la **fecha de finalización** para que se adapten a la realidad operativa o fiscal de tu caso.
7. Guarda el año operativo.
8. Confirma que el período que quieres planificar queda completamente cubierto por ese año.
9. Si el año ya existía, revisa igualmente que sigue siendo el correcto para tu caso y que sus fechas no generan dudas.

Cuando termines esta sección, deberías haber identificado o creado el año operativo que realmente sostiene tu caso de planificación.

## Revisando la continuidad temporal y evitando huecos o solapamientos

Después de identificar el año operativo correcto, necesitas comprobar que su secuencia temporal es coherente. En GoalBus, la continuidad entre años operativos no es opcional. El sistema está diseñado para evitar que existan **lagunas** o **solapamientos** entre años, porque esos errores terminarían afectando métricas acumuladas, KPI anuales y cálculos posteriores.

Antes de empezar esta sección, asegúrate de que:
1. Ya encontraste el año operativo que debería cubrir tu caso.
2. Ya conoces su fecha de inicio y su fecha de fin.
3. Sabes si hay años anteriores o posteriores que formen parte de la misma secuencia.

Para revisar la continuidad temporal del año operativo:
1. Abre el detalle del año operativo que usarás como referencia.
2. Revisa la **fecha de inicio** y la **fecha de finalización**.
3. Comprueba si el período que quieres planificar cae dentro de ese rango sin ambigüedad.
4. Revisa el año operativo anterior o posterior, si existe, para asegurarte de que no hay:
   1. huecos entre un año y otro, o
   2. solapamientos entre dos rangos temporales.
5. Si necesitas crear un nuevo año al final de la secuencia, añádelo solo al final y revisa que continúe exactamente donde termina el anterior.
6. Si detectas una inconsistencia, corrige las fechas antes de seguir.
7. Confirma que el sistema permite guardar la secuencia sin bloquear el guardado por errores de continuidad.

Para el caso de referencia, hazte estas preguntas:
1. ¿Enero de 2026 está completamente dentro de un año operativo válido?
2. ¿Ese año conecta correctamente con el anterior y el siguiente?
3. ¿El sistema podría acumular datos sin romper la continuidad del período?

Cuando termines esta sección, deberías tener la seguridad de que no existen huecos ni solapamientos que afecten tu caso.

## Comprobando la relación entre el año operativo y la lógica de calendario

Ahora que ya validaste el año operativo y su continuidad, necesitas conectarlo con lo que definiste en P2. No sirve de mucho tener tipos de día y festivos bien configurados si el marco temporal donde vivirán esos datos no está bien construido.

Antes de continuar, asegúrate de que:
1. El año operativo correcto ya está identificado.
2. Los tipos de día y festivos del caso ya están configurados.
3. El período que vas a planificar sigue siendo claro y acotado.

Para comprobar que el año operativo ya está listo para sostener la planificación:
1. Revisa el caso de planificación que definiste al principio de este artículo.
2. Confirma que ese período vive dentro del año operativo correcto.
3. Comprueba que la lógica de calendario definida en P2 también aplica dentro de ese mismo marco temporal.
4. Pregúntate si el sistema ya podría usar simultáneamente:
   1. la categoría correcta de tipo de día,
   2. los festivos correctos, y
   3. el año operativo correcto.
5. Si la respuesta es sí, continúa con el siguiente quick start.
6. Si la respuesta es no, corrige el año operativo o revisa la coherencia con el calendario antes de seguir.

Al terminar esta sección, deberías poder afirmar que tu caso tiene una base temporal completa: calendario correcto y año operativo correcto.

## Lecturas adicionales

- [Preparando la red maestra: paradas, líneas y rutas](P4_Preparar_la_red_maestra_paradas_lineas_y_rutas.md)
