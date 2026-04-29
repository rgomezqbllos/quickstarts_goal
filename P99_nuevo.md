---
title: Carga masiva de conductores y propiedades fechadas
shortTitle: Importación CSV de Conductores
intro: 'Optimiza la gestión de tu personal operativo automatizando la creación y actualización de conductores, incluyendo sus asignaciones a depósitos, líneas y grupos mediante archivos CSV.'
contentType: how-tos
versions:
  - '*'
---

## 0. Prerrequisitos

Antes de iniciar el proceso de carga, asegúrate de cumplir con los siguientes puntos:
* El archivo debe estar en formato **CSV** utilizando el punto y coma (`;`) como delimitador.
* Las fechas deben seguir estrictamente el formato **YYYY-mm-dd**.
* Los valores de depósitos, líneas y grupos de trabajo ya deben existir en la base de datos del sistema.
* Contar con el identificador único (`external_code`) para cada conductor.

## 1. Estructura del archivo CSV

Para una carga exitosa, el archivo debe organizar la información en columnas específicas que definen tanto la identidad del conductor como sus atributos temporales:

* **Datos de identidad**: Incluye `external_code` (obligatorio), `name`, `surname`, `username` y `email`.
* **Definición de propiedad**: La columna `property_name` especifica qué atributo se va a asignar.
* **Valor y vigencia**: Las columnas `property_value`, `property_start_date` y `property_end_date` definen el contenido de la propiedad y su rango de validez.

## 2. Tipos de propiedades y asignaciones

El sistema permite gestionar diferentes tipos de vínculos operativos mediante nombres de propiedad predefinidos:

* **Asignaciones de Depósito**: `DEPOT_LINK` para asignaciones fijas y `DEPOT_TRANSFER` para traslados temporales.
* **Operación y Habilitaciones**: `LINE` para asignar líneas de trabajo y `VEHICLE_TYPE` para tipos de vehículo autorizados.
* **Grupos y Unidades**: `WORKING_GROUP_LINK` y `BUSINESS_UNIT_LINK` para organizar al personal en equipos o divisiones de negocio.
* **Propiedades Dinámicas**: Para campos personalizados (como edad o antigüedad), utiliza el prefijo `dp.` seguido del nombre de la propiedad (ej. `dp.Antigüedad`).

## 3. Reglas de validación y continuidad

Para garantizar la integridad de los datos, el sistema aplica validaciones automáticas según el tipo de registro:

* **Registros tipo LINK**: Son asignaciones continuas. No deben existir huecos temporales entre registros del mismo tipo; la fecha de fin de una asignación debe coincidir con la fecha de inicio de la siguiente. Solo se permite un registro activo sin fecha de fin por cada tipo de propiedad.
* **Registros tipo TRANSFER**: Son asignaciones puntuales. Deben tener obligatoriamente fecha de inicio y fin, y se permiten huecos entre distintos registros.
* **Existencia en base de datos**: Los valores cargados en `property_value` deben coincidir exactamente con los nombres registrados en las tablas de `depot`, `line`, `vehicle_type_personal`, `working_group` o `business_unit`.

## Caso de referencia: Conductores ADO

Para cargar un conductor mexicano en la empresa **ADO** asignado al depósito **Estrella de Oro**, el archivo debe estructurarse de la siguiente manera:

| name | surname | email | username | external_code | property_name | property_value | property_start_date | property_end_date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Miguel | Hernández | m.hdez@ado.com.mx | mhernandez | MX-1025 | | | | |
| | | | | MX-1025 | DEPOT_LINK | Estrella de Oro | 2026-01-01 | |
| | | | | MX-1025 | LINE | Ruta_CDMX_Acapulco | 2026-01-01 | 2026-12-31 |

> **Nota**: Puedes repetir el `external_code` en varias filas para asignar múltiples propiedades a un mismo conductor en un solo proceso de carga.

## Pasos para la carga

1. **Preparación**: Genera el archivo CSV con los datos de los conductores respetando el encabezado y el uso de punto y coma.
2. **Validación de Fechas**: Revisa que todas las celdas de fecha sigan el formato **YYYY-mm-dd** para evitar errores de procesamiento.
3. **Carga**: Sube el archivo a través del módulo de importación de conductores.
4. **Corrección**: Si el sistema detecta errores (como nombres de depósitos inexistentes o solapamiento de fechas en registros LINK), revisa el log de errores y ajusta el CSV.

## Cierre de validación

Una vez completada la carga, verifica en el panel de administración que los conductores aparezcan con sus estados actualizados. Las propiedades fechadas deben reflejarse correctamente en la ficha del empleado, asegurando que las asignaciones de depósito y línea coincidan con los periodos definidos en el archivo.

## Lecturas adicionales
- Configuración de Depósitos y Unidades de Negocio.
- Gestión de Propiedades Dinámicas en el Catálogo.
- Guía de resolución de errores comunes en importación CSV.