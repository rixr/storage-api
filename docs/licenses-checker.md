# Licenses Checker Query and Store for ODIS

Este proyecto **almacena licencias** con extension de archivo `.dat` para la utilización del software de diagnóstico para vehiculos llamado "Offboard Diagnostic Information System", se consulta diferentes elementos, el archivo de licencia, la fecha de creación de la licencia; de los equipos de diagnóstico se consulta la marca, el modelo y el numero asignado al equipo.

Se cuenta con las siguientes entidades:
- Equipo de diagnóstico (Marca, Modelo, Número Asignado, Número de Serie)
- licencia (Archivo de licencia, fecha de creación)



## Operacion para almacenamiento de datos.
#### Operaciones de Equipo de diagnóstico
- Registro de un equipo
: Solicitamos la Marca, el Modelo, el Número Asignado y el Número de Serie del equipo, este último es el identificador.

- Actualización de número asignado de un equipo
: Dar de baja un número Asignado.
: Reasignar nuevo número de asignación.

#### Operaicones de Licencias
- Registro de una licencia
: Solicitamos un archivo con extension `.dat` para asignarlo a un equipo de diagnóstico.



## Operaciones de consulta de datos

 - Solicitar datos de un equipo de diagnóstico
    - Marca
    - Modelo
    - Número Asignado
    - Número de Serie

 - Solicitar datos de una licencia
    - Archivo de licencia
    - Fecha de creación

 - Lista de equipos de diagnóstico
    - Todos



## API
| Path                  | Descripción                                         |
| ----------------------| ----------------------------------------------------|
| `/licenses/login`     | Pagina principal, autenticación de usuarios         |
| `/licenses/new`       | Almacena nuevos registros de equipos de diagnóstico |
| `/licenses/update`    | Actualiza registros                                 |
| `/licenses/info`      | Muestra una lista de todos los equipos              |
| `/licenses/info/<id>` | Muestra toda la información del equipo deseado      |

## Procesos del API
#### Login

#### Registra nuevo equipo de diagnóstico

#### Actualiza registro de equipo de diagnóstico

#### informaciónormacion de los equipos de diagnóstico



## Archivos Relacionados

 - `routes/licenses-checker.py`

Prefijos de almacenamiento:

> Pendiente o Nulo

Tablas de Base de Datos

> Pendiente o Nulo
