# License Manager for ODIS
> Autor: Ricardo Ramos

# Descripcion general del proyecto
Este proyecto almacena licencias con extensión de archivo `.dat` para la utilización del software de diagnóstico para vehículos llamado "Offboard Diagnostic Information System", registra equipos de diagnóstico, actualiza los registros previos y muestra información especifica de cada uno de ellos, entre estos elementos te permite descargar su respectivo arrchivo de licencia.

## Entrada del proyecto en la organizacion
Este proyecto ayuda en la operacion de la empresa Emporio Automotriz Volkswagen de Tijuana, facilitando el manejo de los recursos tecnologicos que utiliza el taller de servicio cuando se adquieren nuevos equipos de diagnostico.

## Modelado de datos
El proyecto cuenta con las siguientes entidades:
- Equipo de diagnóstico (Marca, Modelo, Número de Serie)
- Licencia (Archivo de licencia, fecha de creación)

## Interacciones de datos
La manera en la que se relacionan nuestras entidades son de la siguiente manera:
### Equipo de diagnóstico
	- Permite registro de un equipo.
	- Tambien la actualización a esos equipos.
### Licencias
	- Cuando se hace un registro nuevo obligatoriamente se solicita de una licencia.
		- Para ello solicitamos un archivo con formato `.dat` para asignarlo a un equipo de diagnóstico.

## Consultas de datos
El presente proyecto puede hacer las siguientes consultas:
- Consulta de un equipo de diagnóstico
	- Muestra los campos basicos del equipo
	- Dentro se encuentra la licencia asignada
- Lista de equipos de diagnóstico
	- Muestra todos los equipos
	- Tambien en especifico por numero de Serie

## Operaciones de datos
A continuacion se explica las diferentes maneras en las que se puede interactuar con el servidor:
### Registra nuevo equipo de diagnóstico
	- Para hacer un nuevo registro solicitamos la Marca, el Modelo y el Número de Serie del equipo, este último es el identificador.
	- En el registo se solicita el archivo de la licencia que se asignara, ademas de la fecha en la que se esta asignando.

### Actualiza registro de equipo de diagnóstico
	- Para lograr la Actualización primero se da de baja la licencia asignada.
	- Seguido se debe reasignar una licencia nueva.

### Muestra información de los equipos de diagnóstico
	- En forma de lista  muestra todos los equipos con los que se cuentan, activos e inactivos.

## Rutas HTTP
En la siguiente tabla se especifica cuales son las rutas con las que cuenta este proyecto, ademas del metodo HTTP que se utiliza, la ruta como tal y una breve descripcion de su funcion.
| Método | Path                          | Descripción                                         |
| -------|-------------------------------|-----------------------------------------------------|
| POST   | `/odis-store/new`             | Almacena nuevos registros de equipos de diagnóstico |
| GET    | `/odis-store/list`            | Muestra todos los registros                         |
| GET    | `/odis-store/<serial_number>` | Muestra toda la información del registro deseado    |
| POST   | `/odis-store/<serial_number>` | Actaliza la información del registro deseado        |


## Ejemplos de mensajes HTTP que aceptara y emitira el servidor
En el primer ejemplo se muestra un mensaje que acepta el servidor, en el segundo ejemplo, si todo fue correctamente completado nos regresa un mensaje de exito, a partir del tercer ejemplo son casos diferentes de error que emite el servidor cuando se interactua con el de manera no planeada.
### 1. registro de un nuevo equipo
```
{
    "brand": "getac",
    "model": "vas 6150e",
	"serial_number": "1234567",
	"license": [{
		"file": license.dat,
		"date": "01-01-1970"
		}]
  }
```
### 2. Respuesta exitosa de registro de equipo
```
{
    "code": 200,
    "message": "registro exitoso",
	"status": "active"
  }
```
### 3. Mensaje de fallo de almacenamiento por tipo de archivo incorrecto
```
{
    "code": 500,
    "message": "almacenamiento fallido, formato de archivo incorrecto"
  }
```
### 4. Mensaje de fallo de almacenamiento por tamaño de archivo > 2MB
```
{
    "code": 500,
    "message": "almacenamiento fallido, tamaño de archivo excedente"
  }
```

## Ejemplos de interacciones con el servidor
En esta seccion se muestra un ejemplo de como recibe los datos el servidor, seguido de una explicacion de los que sucede despues.
```
POST /odis-store/new

curl -vq http://localhost:8080/odis-store/new \
    -X POST \
    -H 'ORIGIN: http://localhost:1234' \
    -H 'Content-Type: application/json' \
    --data '{ "brand": "getac", "model": "vas 6150e", "serial_number": "1324567", "license":[{"file": license.dat, "date": "01/01/1970" } ] }'
```
- Recibe una estructura de registro de equipo de diagnóstico.
- 200, registrar una nuevo equipo, habilita un estado **Activo** y regresa un mensaje de éxito.
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
- 200, actualizar información de un equipo dado el numero de serie.
- D.O.M, 500, regresa mensaje de fallo.

## Autenticacion y autorizacion de usuarios
Para este proyecto en especifico existiran dos usuarios, ambos con privilegios de administrador, por lo tanto tendran todos los permisos permitidos.
- Leer, crear y editar todo.
	- administrador: `(app:odis:read:all, app:odis:write:all)`

# Plan de Implementacion (Aspecto General)
Este proyecto resuelve la falta de manejo de las licencias con las que la organizacion cuenta para la utilizacion de sus equipos de diagnostico para vehiculos. Dentro de estos equipos se instala un software que obligatoriamente solicita un archivo de licencia.

Una de las motivaciones para la realizacion de este proyecto es ofrecer una herramienta a la organizacion que le permita administrar estos recursos tecnologicos ya que nunca antes se habia tenido esta posibilidad y que cubre la necesidad de tomar el control dado la regularidad con la que se presentan estas situaciones donde se requiere una herramienta como esta.

Las personas que notaran el impacto que puede tener este proyecto son las involucradas en los departamentos de Sistemas y del taller de Servicio, que son los que diariamente trabajan con estos equipos de diagnostico.

Los recursos necesarios para iniciar a trabajar con este proyecto son basicos, como recurso humano estan los administradores, quienes llevaran el manejo de la aplicacion/herramienta, los recursos de computo necesarios son una computadora, de preferencia portatil y la infraestructura necesaria un pequeño servidor privado para trabajar de manera local.

Al desplegar este proyecto se espera que la empresa beneficiada continue dandole uso y actualizando la aplicacion de manera que se tenga el control de licencias que se busca durante un largo tiempo.

# Plan de Implementacion (Aspecto Tecnico)
## Modulos de codigo necesarios
- Modulos de Rutas
- Modulos de Funciones

## Metodos de almacenamiento requeridos
El metodo optimo para este proyecto es almacenamiento de archivos locales.

## Plan para la codificacion de los modulos


## Plan para la verificacion de la calidad del producto (pruebas manuales de los casos de uso, pruebas automatizadas del caso de uso)

## Plan para el despliegue del proyecto de codigo. `OPCIONAL +++`
## Plan para realizar reportes de opercion y estatus actual del programa. `OPCIONAL +++`
