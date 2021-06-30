# Licenses Checker Query and Store

Este proyecto almacena licencias en archivos `.dat` para la utilización del software de diagnóstico "Offboard Diagnostic Information System", y consulta la fecha de creación de la licencia y el número serial del equipo asignado a la licencia.

Se cuenta con las siguientes entidades:
- Equipo de diagnóstico (Marca, Modelo, Numero de Serie)
- licencia (Nombre de licencia, fecha de creacion)


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
