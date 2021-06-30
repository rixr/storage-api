# Licenses Checker Query and Store

Este proyecto almacena licencias en archivos `.dat` para la utilización del software de diagnóstico "Offboard Diagnostic Information System", y consulta la fecha de creación de la licencia y el número serial del equipo asignado a la licencia.

Se cuenta con las siguientes entidades:
- Equipo de diagnóstico (Marca, Modelo, Número Asignado, Número de Serie)
- licencia (Nombre de licencia, fecha de creación)

## Operacion para almacenamiento de datos.

### Operaciones de Equipo de diagnóstico
- Registro de un equipo
: Solicitamos la Marca, el Modelo, el Número Asignado y el Número de Serie del equipo, este ultimo es el identificador.

- Actualización de número asignado de un equipo.
: Dar de baja un número Asignado.
: Reasignar nuevo número de asignación.

### Operaiones de Licencias
- Registro de una licencia
: Solicitamos un archivo con extension `.dat` para asignarlo a un equipo de diagnóstico.


Consiste en:

## API

| Path                  | Descripción                                     |
| --------------------- | ----------------------------------------------- |
| /licenses/login       | Autenticación de usuarios                       |
| /licenses/store       | Agrega un nuevo registro                        |
| /licenses/info/<id>   | Muestra toda la información obtenida del equipo |


# Archivos Relacionados

 - `routes/licenses-checker.py`

Prefijos de almacenamiento:

> Pendiente o Nulo

Tablas de Base de Datos

> Pendiente o Nulo
