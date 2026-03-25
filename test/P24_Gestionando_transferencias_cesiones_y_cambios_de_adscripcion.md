---
title: Gestionando transferencias, cesiones y cambios de adscripción
shortTitle: Cesiones y cambios
intro: 'Aprende a gestionar cambios de contexto operativo de los conductores, distinguiendo entre transferencia, cesión y cambio de adscripción para que Rostering use a cada persona en el ámbito correcto sin perder trazabilidad.'
contentType: how-tos
versions:
  - '*'
---

## Entendiendo la diferencia entre transferencia, cesión y cambio de adscripción

Antes de calcular Rostering, necesitas distinguir correctamente los movimientos de personal entre contextos operativos. No todas las situaciones significan lo mismo. Un conductor puede seguir perteneciendo a su depósito principal, pero trabajar temporalmente en otro. También puede cambiar de adscripción de forma más estable. Si mezclas estos conceptos, la elegibilidad del personal se vuelve confusa y el cálculo puede asignar trabajo en el contexto equivocado.

Usa esta quick start cuando ya tengas cargados los conductores, revisada su adscripción principal y modeladas sus ausencias e inactividades, y necesites reflejar movimientos reales entre depósitos, grupos o unidades.

Antes de empezar, asegúrate de que:
1. Ya cargaste y revisaste conductores en P20.
2. Ya validaste la adscripción operativa en P21.
3. Ya configuraste reglas de Rostering en P22.
4. Ya registraste ausencias, inactividades y disponibilidad en P23.
5. Sabes qué personas cambiarán de contexto y durante qué período.

Para esta quick start, usa este caso de referencia:

> **Voy a registrar que uno de los conductores que normalmente pertenece al Depósito Norte trabajará temporalmente en otro contexto, y que otro conductor cambiará de adscripción de forma más estable antes del cálculo de Rostering.**

Para distinguir correctamente cada movimiento:
1. Usa una **cesión** cuando la persona sigue perteneciendo a su contexto principal, pero trabajará temporalmente en otro.
2. Usa una **transferencia** cuando la persona cambia de contexto de forma más estructural o permanente.
3. Usa un **cambio de adscripción** cuando necesitas actualizar formalmente el depósito, grupo o unidad base desde la que el sistema debe tratar al conductor.
4. No uses una ausencia para modelar un cambio de contexto operativo.
5. No uses una cesión para corregir una adscripción principal mal configurada.

Mantén estas preguntas como guía:
1. ¿Dónde pertenece normalmente esta persona?
2. ¿Dónde trabajará realmente durante este período?
3. ¿Ese movimiento es temporal o estructural?

Cuando termines esta sección, deberías tener claro qué tipo de registro corresponde a cada cambio de contexto.

## Registrando una cesión temporal del conductor

La cesión sirve para reflejar que un conductor trabajará temporalmente fuera de su contexto habitual sin perder su adscripción base. Esto es útil cuando una persona sigue perteneciendo a su depósito, unidad o grupo principal, pero operará durante un tiempo en otro entorno.

Antes de empezar esta sección, asegúrate de que:
1. Ya identificaste a la persona que será cedida.
2. Ya sabes cuál es su contexto principal.
3. Ya conoces el contexto temporal de destino y las fechas de aplicación.

Para registrar una cesión temporal:
1. Abre el perfil del conductor en la lista general.
2. Ve a la sección de **movimientos**, **adscripción temporal** o **cesiones**, según la vista disponible.
3. Crea un nuevo registro de cesión.
4. Define:
   1. el **contexto de origen**,
   2. el **contexto de destino**,
   3. la **fecha de inicio**,
   4. la **fecha de fin**,
   5. y cualquier observación necesaria.
5. Guarda el registro.
6. Revisa que el conductor siga conservando su adscripción principal.
7. Comprueba que durante el período de cesión el sistema pueda tratarlo en el contexto temporal correcto.

Para el caso de referencia, una cesión válida sería:
1. conductor adscrito al Depósito Norte,
2. cedido durante dos semanas al Depósito Sur,
3. sin cambiar su adscripción principal histórica.

Cuando termines esta sección, deberías tener correctamente modelada una cesión temporal sin perder trazabilidad estructural.

## Registrando una transferencia o cambio más estable

A diferencia de la cesión, una transferencia responde a un movimiento más estructural. Aquí ya no se trata solo de trabajar temporalmente en otro contexto, sino de mover de forma más estable la pertenencia operativa del conductor.

Antes de empezar esta sección, asegúrate de que:
1. Ya identificaste a la persona que cambiará de contexto de forma más duradera.
2. Ya sabes qué depósito, unidad o grupo pasará a ser su nuevo contexto principal.
3. Ya no estás hablando de una necesidad temporal o excepcional.

Para registrar una transferencia o cambio estructural:
1. Abre el perfil del conductor.
2. Revisa su adscripción principal actual.
3. Crea el movimiento de transferencia o actualiza la adscripción principal, según el flujo que use tu entorno.
4. Define:
   1. el nuevo **depósito principal**,
   2. la nueva **unidad de negocio**,
   3. el nuevo **grupo de trabajo**, si cambia,
   4. y la fecha de efectividad.
5. Guarda los cambios.
6. Revisa que el perfil ya refleje el nuevo contexto principal.
7. Comprueba que el cambio no haya dejado datos contradictorios entre adscripción principal y habilitaciones.

Para el caso de referencia, una transferencia válida sería:
1. conductor que deja de pertenecer al Depósito Norte,
2. pasa a pertenecer al Depósito Sur de forma estable,
3. y a partir de esa fecha debe tratarse como recurso de esa nueva base.

Cuando termines esta sección, deberías tener correctamente modelado un cambio estructural de contexto.

## Revisando el impacto del movimiento en habilitaciones y elegibilidad

Después de registrar cesiones o transferencias, necesitas revisar su impacto operativo. Mover una persona entre contextos no sirve de nada si sus habilitaciones o su elegibilidad no acompañan el cambio. Aquí debes confirmar que el conductor no solo cambió de contexto en el perfil, sino que también puede ser usado correctamente en ese nuevo entorno.

Antes de continuar, asegúrate de que:
1. Ya registraste al menos una cesión o una transferencia.
2. Ya sabes en qué contexto operativo debería verse la persona a partir de ahora.
3. Entiendes que un cambio de contexto puede requerir revisar habilitaciones vigentes.

Para revisar el impacto operativo del movimiento:
1. Vuelve a la pestaña de **habilitaciones / cualificaciones** del conductor.
2. Comprueba si existen habilitaciones vigentes para el contexto de destino.
3. Si faltan, añádelas con fechas correctas antes del cálculo.
4. Revisa que la persona no quede simultáneamente visible en contextos incompatibles por un error de configuración.
5. Comprueba que el sistema podrá considerar a la persona elegible en el ámbito correcto durante el período correspondiente.
6. Si detectas contradicciones, corrígelas antes de pasar al cálculo de Rostering.

Para el caso de referencia, asegúrate de que:
1. el conductor cedido puede trabajar legal o técnicamente en el contexto de destino,
2. el conductor transferido tiene ya sus habilitaciones acordes al nuevo contexto,
3. la elegibilidad coincide con el movimiento registrado.

Cuando termines esta sección, deberías tener movimientos de personal que también son operativamente utilizables.

## Confirmando que los cambios de contexto ya están listos para el cálculo de Rostering

El último paso es comprobar que la combinación entre adscripción principal, cesiones, transferencias y habilitaciones ya está lo suficientemente clara como para alimentar el cálculo. Aquí el objetivo es evitar dos errores:
1. asignar a una persona en un contexto donde no debería aparecer,
2. o dejar fuera a una persona que sí debería ser elegible por un cambio ya registrado.

Antes de terminar, asegúrate de que:
1. Ya registraste los movimientos temporales o estructurales necesarios.
2. Ya revisaste su impacto en la elegibilidad.
3. Ya sabes qué colectivo participará en el siguiente cálculo.

Para confirmar que esta capa ya está preparada:
1. Vuelve a la lista general de conductores.
2. Revisa varios perfiles afectados por cambios de contexto.
3. Comprueba que:
   1. las cesiones se ven como temporales,
   2. las transferencias se reflejan como cambios estructurales,
   3. y la adscripción principal sigue siendo coherente cuando corresponde.
4. Pregúntate si el sistema ya podría:
   1. usar al conductor correcto en el contexto correcto,
   2. durante el período correcto,
   3. sin confundir pertenencia estructural con desplazamiento temporal.
5. Si la respuesta es sí, continúa con el siguiente quick start.
6. Si la respuesta es no, corrige movimientos o habilitaciones antes de seguir.

Para el caso de referencia, no continúes hasta poder afirmar:
1. Los cambios de contexto de los conductores de L1 ya están correctamente registrados.
2. Sabes quién está cedido, quién fue transferido y quién mantiene su adscripción original.
3. La base ya está lista para ejecutar el primer cálculo de Rostering.

Cuando termines esta sección, deberías tener el contexto organizativo del personal suficientemente claro como para pasar al cálculo de asignación.

## Lecturas adicionales

- [Ejecutando el primer cálculo de Rostering](P25_Ejecutando_el_primer_calculo_de_Rostering.md)
