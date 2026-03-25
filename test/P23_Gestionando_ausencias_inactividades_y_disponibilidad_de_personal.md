---
title: Gestionando ausencias, inactividades y disponibilidad de personal
shortTitle: Disponibilidad personal
intro: 'Aprende a registrar ausencias, inactividades y restricciones de disponibilidad para que Rostering asigne solo a personas realmente elegibles y no intente cubrir trabajo con conductores no disponibles.'
contentType: how-tos
versions:
  - '*'
---

## Entendiendo la diferencia entre ausencia, inactividad y disponibilidad

Antes de calcular Rostering, necesitas controlar qué personas están realmente disponibles para trabajar. En esta capa ya no basta con que el conductor exista, esté adscrito al contexto correcto y tenga reglas aplicables. También necesitas decirle al sistema si esa persona:
1. está disponible,
2. está ausente,
3. está inactiva,
4. o tiene una disponibilidad parcial o restringida.

Usa esta quick start cuando ya tengas cargados los conductores, revisada su adscripción operativa y preparada la base de reglas de Rostering, y necesites impedir que el cálculo intente asignar trabajo a personas no elegibles.

Antes de empezar, asegúrate de que:
1. Ya cargaste y revisaste conductores en P20.
2. Ya validaste su adscripción operativa en P21.
3. Ya definiste la base de reglas de Rostering en P22.
4. Tienes claro qué colectivo de personal participará en el cálculo.
5. Ya sabes si en tu operación necesitas registrar vacaciones, bajas, permisos, indisponibilidades parciales o estados no operativos.

Para esta quick start, usa este caso de referencia:

> **Voy a registrar ausencias, inactividades y restricciones de disponibilidad sobre los conductores que cubrirán la línea L1 para asegurarme de que Rostering solo asigne trabajo a personas realmente elegibles.**

Para entender correctamente estos conceptos:
1. Usa una **ausencia** cuando la persona existe y pertenece al colectivo, pero no está disponible durante un período concreto.
2. Usa una **inactividad** cuando la persona debe quedar fuera de la operativa durante un período más estructural o no debe participar en el cálculo.
3. Usa una **restricción de disponibilidad** cuando la persona sí puede trabajar, pero no en todo momento o no bajo todas las condiciones.
4. No mezcles estos conceptos como si fueran lo mismo.
5. Usa esta regla de lectura:
   1. **ausencia** = no puede trabajar durante un período concreto,
   2. **inactividad** = no debe tratarse como recurso operativo en ese contexto o período,
   3. **disponibilidad restringida** = puede trabajar, pero con límites.

Cuando termines esta sección, deberías tener una visión clara de qué tipo de registro debes usar en cada situación.

## Registrando ausencias planificadas del conductor

Las ausencias planificadas son uno de los primeros elementos que debes cargar antes del cálculo de Rostering. Aquí entran vacaciones, permisos, incapacidades, licencias o cualquier otro período en el que una persona no deba recibir trabajo.

Antes de empezar esta sección, asegúrate de que:
1. Ya sabes qué conductores tendrán ausencias dentro del horizonte de cálculo.
2. Ya conoces las fechas exactas o aproximadas de esas ausencias.
3. Quieres dejar al sistema sin ambigüedad sobre qué días la persona no puede ser usada.

Para registrar ausencias en el perfil del conductor:
1. En GoalBus, abre la lista general de conductores.
2. Entra al perfil del conductor que quieras revisar.
3. Abre la sección de **ausencias** o **disponibilidad** correspondiente.
4. Crea un nuevo registro de ausencia.
5. Define al menos:
   1. el **tipo de ausencia**,
   2. la **fecha de inicio**,
   3. la **fecha de fin**,
   4. y cualquier observación necesaria.
6. Guarda el registro.
7. Repite el proceso para otros conductores o ausencias relevantes.
8. Revisa que el período de ausencia cubre correctamente el tiempo en el que esa persona no debe recibir trabajo.

Para el caso de referencia, una lógica mínima podría ser:
1. Conductor A: vacaciones del 10 al 20
2. Conductor B: permiso el día 14
3. Conductor C: incapacidad durante una semana concreta

Cuando termines esta sección, deberías tener registradas las ausencias principales que afectan al cálculo de Rostering.

## Registrando inactividades y estados no operativos

Además de las ausencias, puede haber conductores que no deban tratarse como recursos operativos activos, aunque sigan existiendo en la base de datos. Aquí entran estados de inactividad que deben separar a la persona del cálculo sin borrar su trazabilidad histórica.

Antes de empezar esta sección, asegúrate de que:
1. Ya sabes qué personas no deben participar en el cálculo actual.
2. Ya distingues una ausencia puntual de una inactividad más estructural.
3. Quieres mantener el histórico del conductor sin usarlo como recurso elegible.

Para registrar inactividades:
1. Abre el perfil del conductor correspondiente.
2. Revisa el campo o sección de **estado** del conductor.
3. Si la persona no debe participar en futuros cálculos, ajusta su estado a **inactivo** o al estado no operativo correspondiente.
4. Si tu proceso usa un registro temporal adicional para esa inactividad, crea el registro con:
   1. fecha de inicio,
   2. fecha de fin, si aplica,
   3. y motivo.
5. Guarda los cambios.
6. Comprueba que el conductor sigue existiendo en el sistema, pero ya no será tratado como elegible del mismo modo que un conductor activo.

Para el caso de referencia, pregúntate:
1. ¿Esta persona está realmente ausente unos días o ya no debería ser usada como recurso activo?
2. ¿Necesitas conservar su histórico sin borrarlo?
3. ¿La mejor decisión es marcar inactividad en lugar de crear solo una ausencia?

Cuando termines esta sección, deberías tener claro qué personas quedan fuera del cálculo por estado y no solo por ausencia puntual.

## Configurando disponibilidad parcial o restricciones temporales

No todos los problemas de elegibilidad son ausencias completas. A veces una persona sí puede trabajar, pero no durante todo el día, no en ciertos períodos o no bajo determinadas condiciones. Aquí es donde necesitas modelar la **disponibilidad parcial** o las restricciones temporales.

Antes de empezar esta sección, asegúrate de que:
1. Ya registraste las ausencias completas.
2. Ya identificaste conductores que sí pueden trabajar, pero con límites.
3. Ya sabes si esas restricciones son diarias, semanales o por un rango concreto de fechas.

Para registrar disponibilidad parcial o restringida:
1. Abre el perfil del conductor.
2. Entra en la sección correspondiente a disponibilidad o excepciones temporales.
3. Crea un nuevo registro de restricción.
4. Define:
   1. el período de aplicación,
   2. la franja o condición restringida,
   3. y el motivo, si tu proceso lo necesita.
5. Guarda el registro.
6. Revisa que la persona sigue siendo elegible, pero solo dentro de los límites definidos.
7. No uses una ausencia total si el problema real es solo una restricción parcial.

Para el caso de referencia, una restricción parcial podría ser:
1. un conductor que no puede trabajar en noches durante un período,
2. una persona que solo puede trabajar a partir de cierta hora,
3. o alguien que tiene una limitación temporal específica.

Cuando termines esta sección, deberías tener controladas también las situaciones donde el conductor no está totalmente ausente, pero tampoco plenamente disponible.

## Comprobando que Rostering ya ve correctamente la elegibilidad real

El último paso es validar que la combinación entre conductores, adscripción, reglas y disponibilidad ya refleja la realidad del cálculo. Aquí el objetivo es asegurarte de que Rostering no intentará asignar trabajo a personas ausentes, inactivas o mal restringidas, y tampoco dejará fuera a personas que sí deberían ser elegibles.

Antes de terminar, asegúrate de que:
1. Ya registraste ausencias relevantes.
2. Ya marcaste inactividades cuando correspondía.
3. Ya configuraste disponibilidades parciales si eran necesarias.
4. Ya sabes qué colectivo usará el siguiente cálculo.

Para comprobar que la disponibilidad real ya está bien modelada:
1. Vuelve a la lista general de conductores.
2. Revisa varios perfiles representativos del colectivo.
3. Confirma que las personas ausentes tienen sus períodos correctamente registrados.
4. Confirma que las personas inactivas ya no se tratan como recursos activos.
5. Confirma que las restricciones parciales no están modeladas como ausencias totales por error.
6. Pregúntate si el sistema ya podría:
   1. excluir a quien no debe trabajar,
   2. incluir a quien sí puede trabajar,
   3. y respetar restricciones parciales sin romper el cálculo.
7. Si la respuesta es sí, continúa con el siguiente quick start.
8. Si la respuesta es no, corrige los registros antes de seguir.

Para el caso de referencia, no continúes hasta poder afirmar:
1. Los conductores de L1 ya tienen bien reflejada su disponibilidad real.
2. Las ausencias están cargadas.
3. Las inactividades están diferenciadas.
4. Las restricciones parciales no se confundieron con ausencias completas.

Cuando termines esta sección, deberías tener una base de disponibilidad suficientemente fiable como para pasar a cesiones, transferencias y cambios de adscripción.

## Lecturas adicionales

- [Gestionando transferencias, cesiones y cambios de adscripción](P24_Gestionando_transferencias_cesiones_y_cambios_de_adscripcion.md)
