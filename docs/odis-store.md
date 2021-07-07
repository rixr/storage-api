# Descripcion general del proyecto `DONE`
Este proyecto almacena licencias con extensión de archivo `.dat` para la utilización del software de diagnóstico para vehículos llamado "Offboard Diagnostic Information System", registra equipos de diagnóstico, actualiza los registros previos y muestra información especifica de cada uno de ellos, entre estos elementos te permite descargar su respectivo arrchivo de licencia.

## Entrada del proyecto en la organizacion `DONE`
Este proyecto ayuda en la operacion de la empresa Emporio Automotriz Volkswagen de Tijuana, facilitando el manejo de los recursos tecnologicos que utiliza el taller de servicio cuando se adquieren nuevos equipos de diagnostico.

## Modelado de datos `DONE`
- Equipo de diagnóstico (Marca, Modelo, Número de Serie)
- Licencia (Archivo de licencia, fecha de creación)

## Interacciones de datos `DONE`
### Equipo de diagnóstico
	- Registro de un equipo.
	- Actualización de un equipo.
### Licencias
	- Registro de una licencia.
		- Solicitamos un archivo con extension `.dat` para asignarlo a un equipo de diagnóstico.

## Consultas de datos `DONE`
- De un equipo de diagnóstico
	- Muestra los campos basicos
	- Licencia asignada
- Lista de equipos de diagnóstico
	- Muestra todos los equipos
	- Tambien por numero de Serie

## Operaciones de datos `DONE`
### Registra nuevo equipo de diagnóstico
	- Solicitamos la Marca, el Modelo y el Número de Serie del equipo, este último es el identificador.
	- Se solicita el archivo de la licencia que se asignara, ademas de la fecha en la que se esta asignando.

### Actualiza registro de equipo de diagnóstico
	- Se da de baja la licencia asignada.
	- Reasignar licencia nueva.

### Muestra información de los equipos de diagnóstico
	- En forma de lista  muestra todos los equipos con los que se cuentan, activos e inactivos.

## Rutas HTTP `DONE`
| Método | Path                          | Descripción                                         |
| -------|-------------------------------|-----------------------------------------------------|
| POST   | `/odis-store/new`             | Almacena nuevos registros de equipos de diagnóstico |
| GET    | `/odis-store/list`            | Muestra todos los registros                         |
| GET    | `/odis-store/<serial_number>` | Muestra toda la información del registro deseado    |
| POST   | `/odis-store/<serial_number>` | Actaliza la información del registro deseado        |


## Ejemplos de mensajes HTTP que aceptara y emitira el servidor `DONE`
### registro de un nuevo equipo
```
{
	"brand": "getac",
	"model": "vas 6150e",
	"serial_number": "123467",
	"license": {
		"file": license.dat,
		"date": "01-01-1997"
	}
}
```
#### Respuesta exitosa de registro de equipo
```
{
	"code": 200,
  "message": "registro exitoso",
	"status": "active"
  }
```
#### Mensaje de fallo de almacenamiento por falta de entradas
```
{
    "codigo": 500,
    "estatus": "almacenamiento fallido, revisa tus datos"
  }
```
#### Mensaje de fallo de almacenamiento por tipo de archivo incorrecto
```
{
    "codigo": 500,
    "estatus": "almacenamiento fallido, tipo de archivo incorrecto"
  }
```
#### Mensaje de fallo de almacenamiento por tamaño de archivo > 2MB
```
{
    "codigo": 500,
    "estatus": "almacenamiento fallido, tamaño de archivo excedente"
  }
```

## Ejemplos de interacciones con el servidor
```
POST /odis-store/new
```
- Recibe una estructura de registro de equipo de diagnóstico.
- 200, registrar una nuevo equipo, habilita un estado `Activo` y regresa un mensaje de éxito.
- D.O.M, 500, regresa mensaje de fallo.
```
GET /odis-store/list
```
- 200, regresa una lista de todos los equipos de diagnóstico.
- D.O.M, 500, regresa mensaje de fallo.
```
GET /odis-store/<serial_number>
```
- 200, regresa datos del equipo dado el numero de serie.
- D.O.M, 500, regresa mensaje de fallo.
```
POST /odis-store/<serial_number>
```
- 201, actualizar información de un equipo dado el numero de serie.
- D.O.M, 500, regresa mensaje de fallo.
