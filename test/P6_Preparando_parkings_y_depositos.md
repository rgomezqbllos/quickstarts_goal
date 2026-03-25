---
title: Preparando parkings y depósitos para la operación
shortTitle: Parkings y depósitos
intro: 'Aprende a configurar parkings y depósitos de forma coherente para que Scheduling pueda usar una infraestructura física realista, minimizar kilometraje en vacío y respetar la jerarquía correcta de datos.'
contentType: how-tos
versions:
  - '*'
---

## Configurando el parking como nodo físico de la red

Antes de pasar a viajes en vacío, flota o reglas de Scheduling, necesitas dejar bien configurado el **parking** que sostendrá tu caso. En GoalBus, un parking no es solo una etiqueta administrativa. Es un nodo físico geolocalizado de la red, y cuando lo creas el sistema genera automáticamente una parada asociada en esas coordenadas para que el motor pueda calcular distancias, tiempos de entrada y tiempos de salida de forma coherente. Además, cada parking debe estar vinculado obligatoriamente a un depósito organizativo. fileciteturn22file0L1-L20

Usa esta quick start cuando ya hayas creado la red base y necesites conectar esa red con la infraestructura física real antes de seguir con desplazamientos y Scheduling.

Antes de empezar, asegúrate de que:
1. Ya preparaste paradas, líneas y rutas en P4.
2. Ya revisaste la red operativa en P5.
3. Tienes claro qué línea o servicio vas a usar como caso de referencia.
4. Sabes desde qué base física debería salir esa operación.

Para esta quick start, usa este caso de referencia:

> **Voy a preparar el parking del Depósito Norte y validar que su relación con el depósito y con la línea L1 es coherente antes de seguir con viajes en vacío y Scheduling.**

Para crear o validar el parking de tu caso:
1. En GoalBus, abre el módulo de **parkings** o **aparcamientos** dentro de la infraestructura de red.
2. Busca si el parking que necesitas ya existe.
3. Si el parking ya existe, ábrelo y revisa su configuración.
4. Si el parking no existe, crea uno nuevo.
5. Define o valida estos campos:
   1. **Código** como identificador breve para vistas compactas.
   2. **Nombre largo** como nombre descriptivo del garaje o patio.
   3. **Coordenadas** para ubicar correctamente el parking en el mapa.
6. Comprueba que el parking queda vinculado al **depósito** correcto.
7. Guarda el parking.
8. Revisa visualmente en el mapa que su ubicación tenga sentido para la operación real.
9. Confirma que el sistema ya puede tratar ese parking como origen o destino logístico de la operación.

Cuando termines esta sección, deberías tener un parking correctamente geolocalizado y correctamente subordinado al depósito adecuado. fileciteturn22file0L1-L20

## Configurando el depósito como estructura operativa y de relevo

Después de dejar listo el parking, necesitas revisar el **depósito**. En GoalBus, el depósito es la base operativa de la organización y es el vínculo obligatorio para vehículos y conductores. Además, su configuración no solo sirve para identificar la unidad, sino también para definir desde dónde pueden comenzar o terminar los turnos, incluyendo cabeceras o terminales autorizadas que permiten relevos eficientes y reducen kilometraje en vacío. fileciteturn22file3L1-L20 fileciteturn22file2L1-L18

Antes de empezar esta sección, asegúrate de que:
1. Ya creaste o validaste el parking principal del caso.
2. Sabes qué depósito es el responsable de la línea o servicio que estás preparando.
3. Entiendes que el depósito es la entidad principal y que el parking depende de él.

Para crear o validar el depósito de tu caso:
1. En GoalBus, abre el módulo de **depósitos**.
2. Busca si el depósito que necesitas ya existe.
3. Si el depósito ya existe, ábrelo y revisa su configuración.
4. Si no existe, crea uno nuevo.
5. Define o valida estos campos:
   1. **Código** como identificador único.
   2. **Nombre corto** para vistas compactas.
   3. **Nombre largo** como nombre principal del depósito.
   4. **ID externo**, si el cliente trabaja con integraciones ERP o RR. HH.
6. Vincula el **parking principal** del depósito.
7. Añade las **ubicaciones de inicio y fin autorizadas**, como cabeceras o terminales donde se permitan relevos o finales de turno.
8. Guarda el depósito.
9. Confirma que el depósito ya puede sostener operativamente el caso que vienes construyendo.

Para el caso de referencia, revisa que:
1. El Depósito Norte es el depósito organizativo correcto.
2. El Parking Norte está vinculado como su parking principal.
3. Las cabeceras o terminales relevantes de la línea L1 están autorizadas como ubicaciones de inicio o fin cuando aplique.

Cuando termines esta sección, deberías tener un depósito correctamente identificado y vinculado a su parking y a sus ubicaciones operativas autorizadas. fileciteturn22file3L1-L20 fileciteturn22file2L1-L18

## Validando la coherencia entre parking, depósito y línea

Ahora que ya tienes configurados parking y depósito, necesitas comprobar que esa infraestructura encaja con la lógica de línea y con la eficiencia logística que GoalBus espera. El propio modelo de línea permite definir **aparcamientos o depósitos permitidos** para obligar al sistema a iniciar servicio desde las bases geográficamente correctas y minimizar kilometraje en vacío. Esto no es una preferencia cosmética: guía directamente al programador cuando construye soluciones. fileciteturn22file4L1-L24

Antes de continuar, asegúrate de que:
1. El parking ya está vinculado al depósito correcto.
2. El depósito ya tiene su parking principal y sus ubicaciones autorizadas.
3. La línea que usarás en tu caso ya existe y está validada.

Para validar la coherencia completa de la infraestructura:
1. Abre la configuración de la **línea** que usarás como referencia.
2. Revisa la sección de **aparcamientos permitidos** o **depósitos permitidos**.
3. Comprueba que el depósito correcto está autorizado para iniciar los servicios de esa línea.
4. Si el depósito correcto no está autorizado, añádelo.
5. Confirma que no estás dejando habilitados depósitos que no tengan sentido geográfico para esa línea.
6. Revisa si la relación entre línea, depósito y parking minimiza conducción sin ingresos.
7. Confirma que la infraestructura física que acabas de preparar podría sostener el servicio que crearás o calcularás después.
8. Si detectas incoherencias, corrígelas antes de seguir.

Para el caso de referencia, pregúntate:
1. ¿La línea L1 está autorizada a salir desde el Depósito Norte?
2. ¿Ese depósito usa como base física el Parking Norte?
3. ¿La lógica resultante reduce kilómetros en vacío en lugar de aumentarlos?

Cuando termines esta sección, deberías poder afirmar que la línea, el depósito y el parking forman una misma lógica operativa y logística. fileciteturn22file4L1-L24

## Lecturas adicionales

- [Cargando viajes en vacío y desplazamientos](P7_Cargar_viajes_en_vacio_y_desplazamientos.md)
