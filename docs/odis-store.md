# Licenses Checker Query and Store for ODIS
Este proyecto **almacena licencias** con extensión de archivo `.dat` para la utilización del software de diagnóstico para vehículos llamado "Offboard Diagnostic Information System", se consulta diferentes elementos, el archivo de licencia, la fecha de creación de la licencia; de los equipos de diagnóstico se consulta la marca, el modelo y el numero asignado al equipo.

## Se cuenta con las siguientes entidades:
	- Equipo de diagnóstico (Marca, Modelo, Número de Serie)
	- Licencia (Archivo de licencia, fecha de creación)

## Operación para almacenamiento de datos.
##### Operaciones de Equipo de diagnóstico
	- Registro de un equipo:
	- Actualización de un equipo.

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
	- Solicitamos la Marca, el Modelo y el Número de Serie del equipo, este último es el identificador.
	- Se solicita el archivo de la licencia que se asignara ademas de la fecha en la que se esya asignando.

##### Actualiza registro de equipo de diagnóstico
	- Se da de baja la licencia asignada.
	- Reasignar licencia nueva.

##### Muestra información de los equipos de diagnóstico
	- En forma de lista  muestra todos los equipos con los que se cuentan, activos e inactivos.

## Estructuras de solicitud y respuesta
### Registro de un equipo
```
{
    "marca": "getac",
    "modelo": "vas 6150e",
    "numero_serie": "123467"
    "licencia": {
      "archivo": license.dat,
      "fecha": "01-01-1997"
    }
}
```
##### Respuesta exitosa de registro de equipo
```
{
  "estatus": "registro exitoso"
  }
```
##### Mensaje de fallo de registro
```
{
    "codigo": 500,
    "estatus": "registro fallido"
  }
```

### Registro de un archivo de licencia
##### Respuesta exitosa de almacenamiento de archivo `.dat`
```
{
  "estatus": "almacenamiento exitoso"
  }
```
##### Mensaje de fallo de almacenamiento por tipo de archivo incorrecto
```
{
    "codigo": 500,
    "estatus": "almacenamiento fallido, tipo de archivo incorrecto"
  }
```
##### Mensaje de fallo de almacenamiento por tamaño de archivo > 2MB
```
{
    "codigo": 500,
    "estatus": "almacenamiento fallido, tamaño de archivo excedente"
  }
```

## Archivos Relacionados
 - `routes/licenses-checker.py`
##### Prefijos de almacenamiento:
> Pendiente o Nulo
##### Tablas de Base de Datos
> Pendiente
