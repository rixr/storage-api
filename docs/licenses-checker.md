+ Licenses Checker Query and Store for ODIS
Este proyecto **almacena licencias** con extensión de archivo `.dat` para la utilización del software de diagnóstico para vehículos llamado "Offboard Diagnostic Information System", se consulta diferentes elementos, el archivo de licencia, la fecha de creación de la licencia; de los equipos de diagnóstico se consulta la marca, el modelo y el numero asignado al equipo.

## Se cuenta con las siguientes entidades:
	- Equipo de diagnóstico (Marca, Modelo, Número de Serie)
	- Licencia (Archivo de licencia, fecha de creación)

## Operación para almacenamiento de datos.
##### Operaciones de Equipo de diagnóstico
	- Registro de un equipo:
		- Solicitamos la Marca, el Modelo y el Número de Serie del equipo, este último es el identificador.

	- Actualización de un equipo.
    - Dar de baja la licencia asignada
    - Reasignar licencia nueva

##### Operaciones de Licencias
	- Registro de una licencia:
		- Solicitamos un archivo con extension `.dat` para asignarlo a un equipo de diagnóstico.

## Operaciones de consulta de datos
##### Solicitar datos de un equipo de diagnóstico
  - Marca
  - Modelo
  - Número de Serie

##### Solicitar datos de una licencia
  - Identificador de hardaware
  - Archivo de licencia
  - Fecha de creación


## API
| Método | Path               | Descripción                                         |
| -------|--------------------|-----------------------------------------------------|
| POST   | `/odis-store/new`  | Almacena nuevos registros de equipos de diagnóstico |
| GET    | `/odis-store/list` | Muestra todos los registros                         |
| GET    | `/odis-store/<id>` | Muestra toda la información del registro deseado    |
| POST   | `/odis-store/<id>` | Actaliza la información del registro deseado        |


## Procesos del API
##### Registra nuevo equipo de diagnóstico
> Pendiente

##### Actualiza registro de equipo de diagnóstico
> Pendiente

##### Muestra información de los equipos de diagnóstico
> Pendiente

## Estructuras de solicitud y respuesta
##### Registro de alumno
```
{
    "nombre": "Juanito Johns",
    "fecha_de_nacimiento": "1990-01-01"
}
```

#### Respuesta de registro de alumno exitoso
```
{ "matricula": "XX-XX-XX-00" }
```

#### Mensaje de fallo
```
{
    "code": 500,
    "message": "mensaje de error"
}
```

## Archivos Relacionados
 - `routes/licenses-checker.py`
##### Prefijos de almacenamiento:
> Pendiente o Nulo
##### Tablas de Base de Datos
> Pendiente o Nulo
