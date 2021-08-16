# License Manager for ODIS
> Autor: ***Ricardo Ramos***

<br>

# Descripción general del proyecto
Este proyecto almacena licencias con extensión de archivo `.dat` para la utilización del software de diagnóstico para vehículos llamado "Offboard Diagnostic Information System", registra equipos de diagnóstico, actualiza los registros previos y muestra información específica de cada uno de ellos, entre estos elementos te permite descargar su respectivo archivo de licencia.

<br>

## Entrada del proyecto en la organización
Este proyecto ayuda en la operación de la empresa Emporio Automotriz Volkswagen de Tijuana, facilitando el manejo de los recursos tecnológicos que utiliza el taller de servicio cuando se adquieren nuevos equipos de diagnóstico.

<br>

## Modelado de datos
El proyecto cuenta con las siguientes entidades:
- Equipo de diagnóstico (Marca, Modelo, Número de Serie)
- Licencia (Archivo de licencia, fecha de creación)

<br>

## Interacciones de datos
La manera en la que se relacionan nuestras entidades son de la siguiente manera:
### Equipo de diagnóstico
- Permite registro de un equipo.
- Tambien la actualización a esos equipos.
### Licencias
- Cuando se hace un registro nuevo obligatoriamente se solicita de una licencia.
- Para ello solicitamos un archivo con formato `.dat` para asignarlo a un equipo de diagnóstico.

<br>

## Consultas de datos
El presente proyecto puede hacer las siguientes consultas:
- Consulta de un equipo de diagnóstico
  - Muestra los campos basicos del equipo
  - Dentro se encuentra la licencia asignada
- Lista de equipos de diagnóstico
  - Muestra todos los equipos
  - Tambien en especifico por número de Serie

<br>

## Operaciones de datos
A continuación se explica las diferentes maneras en las que se puede interactuar con el servidor:
### Registra nuevo equipo de diagnóstico
- Para hacer un nuevo registro solicitamos la Marca, el Modelo y el Número de Serie del equipo, este último es el identificador.
- En el registo se solicita el archivo de la licencia que se asignara, ademas de la fecha en la que se esta asignando.

### Actualiza registro de equipo de diagnóstico
- Para lograr la actualización primero se da de baja la licencia asignada.
- Seguido se debe reasignar una licencia nueva.

### Muestra información de los equipos de diagnóstico
- En forma de lista  muestra todos los equipos con los que se cuentan, activos e inactivos.

<br>

## Rutas HTTP
En la siguiente tabla se específica cuales son las rutas con las que cuenta este proyecto, ademas del método HTTP que se utiliza, la ruta como tal y una breve descripción de su funcion.
| Método | Path                          | Descripción                                         |
| -------|-------------------------------|-----------------------------------------------------|
| POST   | `/odis-store/new`             | Almacena nuevos registros de equipos de diagnóstico |
| GET    | `/odis-store/list`            | Muestra todos los registros                         |
| GET    | `/odis-store/<serial_number>` | Muestra toda la información del registro deseado    |
| POST   | `/odis-store/<serial_number>` | Actaliza la información del registro deseado        |

<br>

## Ejemplos de mensajes HTTP que aceptara y emitira el servidor
En el primer ejemplo se muestra un mensaje que acepta el servidor, en el segundo ejemplo, si todo fue correctamente completado nos regresa un mensaje de exito, a partir del tercer ejemplo son casos diferentes de error que emite el servidor cuando se interactua con el de manera no planeada.
### 1. registro de un nuevo equipo
```
{
  "brand": "getac",
  "model": "vas 6150e",
  "serial_number" : "1234567",
  "license" : [{
    "file": license.dat,
    "date": "2021-05-01T20:23:22"
  }]
}
```

### 2. Respuesta exitosa de registro de equipo
```
{
 "code": 200,
 "message": "registro exitoso"
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

<br>

## Ejemplos de interacciones con el servidor
En esta seccion se muestra un ejemplo de como recibe los datos el servidor, seguido de una explicacion de los que sucede despues.
```
POST /odis-store/new
```
```
curl -vq http://localhost:8080/odis-store/new \
  -X POST \
  -H 'ORIGIN: http://localhost:1234' \
  -H 'Content-Type: application/json' \
  --data '{ "brand": "getac", "model": "vas 6150e",
  "serial_number": "1324567", "license":[{"file": license.dat,
  "date": "01/01/1970" }]}'
```
- Recibe una estructura de registro de equipo de diagnóstico.
- 200, registrar una nuevo equipo, habilita un estado **Activo** y regresa un mensaje de éxito.
- D.O.M, 500, regresa mensaje de fallo.

<br>

```
GET /odis-store/list
```
```
curl -vq http://localhost:8080/odis-store/list \
  -X GET \
  -H 'Content-Type: application/json' \
  -- data '{"serial_number"}'
```
- 200, regresa una lista de todos los equipos de diagnóstico.
- D.O.M, 500, regresa mensaje de fallo.

<br>

```
GET /odis-store/<serial_number>
```
```
curl -vq http://localhost:8080/odis-store/1234567 \
  -X GET \
  -H 'Content-Type: application/json' \
  -- data '{"brand", "model", "serial_number", "license"}'
```
- 200, regresa datos del equipo dado el número de serie.
- D.O.M, 500, regresa mensaje de fallo.

<br>

```
POST /odis-store/<serial_number>
```
```
curl -vq http://localhost:8080/odis-store/1234567 \
  -X POST \
  -H 'Content-Type: application/json' \
  -- data '{"brand":"foo", "model":"foo",
  "serial_number":"1234567", "license":[{"file": license2.dat,
  "date": "02/02/1970" } ]}'
```
- 200, actualizar información de un equipo dado el número de serie.
- D.O.M, 500, regresa mensaje de fallo.

<br>

## Autenticacion y autorizacion de usuarios
Para este proyecto en especifico existiran dos usuarios, ambos con privilegios de administrador, por lo tanto tendran todos los permisos permitidos.
- Leer, crear y editar todo.
- administrador: `(app:odis:read:all, app:odis:write:all)`

<br>
<br>

# Plan de Implementacion (Aspecto General)
Este proyecto resuelve la falta de manejo de las licencias con las que la organización cuenta para la utilizacion de sus equipos de diagnóstico para vehiculos. Dentro de estos equipos se instala un software que obligatoriamente solicita un archivo de licencia.

Una de las motivaciones para la realizacion de este proyecto es ofrecer una herramienta a la organización que le permita administrar estos recursos tecnológicos ya que nunca antes se habia tenido esta posibilidad y que cubre la necesidad de tomar el control dado la regularidad con la que se presentan estas situaciones donde se requiere una herramienta como esta.

Las personas que notaran el impacto que puede tener este proyecto son las involucradas en los departamentos de Sistemas y del taller de Servicio, que son los que diariamente trabajan con estos equipos de diagnóstico.

Los recursos necesarios para iniciar a trabajar con este proyecto son basicos, como recurso humano estan los administradores, quienes llevaran el manejo de la aplicacion/herramienta, los recursos de computo necesarios son una computadora, de preferencia portatil y la infraestructura necesaria un pequeño servidor privado para trabajar de manera local.

Al desplegar este proyecto se espera que la empresa beneficiada continue dandole uso y actualizando la aplicacion de manera que se tenga el control de licencias que se busca durante un largo tiempo.

<br>
<br>

# Plan de Implementacion (Aspecto Tecnico)
## Módulos de codigo necesarios
- Almacenamiento de archivos
- Almacenamiento de texto
- Llamado de archivos y texto.
- Módulos de Rutas
- Módulos de Funciones

<br>

## Métodos de almacenamiento requeridos
El método optimo para este proyecto es almacenamiento de archivos locales dado a que estos no superan el tamaño de 2MB.

<br>

## Plan para la codificación de los módulos
Para la codificación de los módulos del proyecto primero se revisan los requerimieentos, seguido se construyen las rutas o funciones que se lleguen a necesitar, a medida que se avanza se necesitaran módulos especificos los cuales se tendrán que construir, al momento se cuenta con los módulos más básicos, por decir un ejemplo, almacenamiento de archivos.

<br>

## Plan para la verificación de la calidad del producto (pruebas manuales de los casos de uso, pruebas automatizadas del caso de uso)
Estas pruebas se realizarán almacenando nuevos registros, algunos de ellos con diferentes entradas erroneas para ver que es lo que se necesita reparar, por ejemplo, la validación de formatos de archivos que se podran recibir, los formatos de fecha, el tamaño máximo de los archivos de licencia, entre otros casos que se realizarán para probar la funcionalidad y calidad del proyecto.

<br>

## Plan para el despliegue del proyecto de codigo

# HOW TO RUN SGI SERVER
winpty pipenv run start


<br>

## Plan para realizar reportes de operación y estatus actual del programa.
> Pendiente

<br>

##

# Commit-hashes
1. Crear un fork del proyecto storage-api
**Señalar cual es el commit-hash a partir de haber realizado el fork**

| Concepto                       | Commit Hash                               |
| ------------------------------ | ----------------------------------------- |
| Creación de Fork del proyecto  | 828c4fe16e7ca2dd34fc983c698bffeed8be0980  |

<br>

2. Crear los archivos correspondientes a su proyecto, y someterlos a control de versiones.  
**Señalar el commit-hash que contiene la creación de dichos archivos.**

| Concepto                                      | Commit Hash                               |
| --------------------------------------------- | ----------------------------------------- |
| Creación del archivo `/docs/odis-store.md`    | 828c4fe16e7ca2dd34fc983c698bffeed8be0980  |
| Creación del archivo `/routes/odis-store.py`  | d743ef7775714eb988457aa3ae39ffc75596106f  |
| Creación del archivo `/modules/odis-store.py` | de564db1b86ab52787ce7ecf5382d34af0a2a633  |
| Creación del archivo `/models/odis-store.py`  | ed17aa264fbaf14a02c94c7cad015f99c957d905  |

<br>

3. Crear todas las rutas especificadas en su archivo de documentación dentro de su archivo en la carpeta routes, y todas deben de responder 501, con `Content-Type: application/json`, y un cuerpo de respuesta en formato json con 2 llaves, code y message, el message debe contener el mensaje, `Not Implemented`.
 **Señalar el commit-hash que contiene la codificación de las rutas.**

 | Concepto                                            | Commit Hash                               |
 | --------------------------------------------------- | ----------------------------------------- |
 | Creación de rutas dentro de `/routes/odis-store.py` | e8294bf9153d9f6269a9a99a5f200ede7d6cb68d  |

<br>

4. Crear en su carpeta de módulos funciones que emulen las interacciones con el almacén de archivos o datos, es decir que si necesitas una función de consulta, crear una función que retorne una consulta simulada con datos codificados como constantes, y si necesitas crear objetos funciones que retornen simulando una creación exitosa.
**Señalar el commit-hash que contiene la codificación de estas funciones asistentes.**

| Concepto                  | Commit Hash                               |
| ------------------------- | ----------------------------------------- |
| Codificación de funciones | daefabf5db345e913b9729b719660a2e0f797562  |

<br>

5. Crear mock ups, de las vistas que desean implementar, utilizando MoqUps (conectar a su google drive).
– Una vez concluidas las propuestas de vistas exportar a imagen, e incluir en el documento una explicación de los datos expresados en las vistas emparejandolos con que endpoints contienen dicha información o a cual endpoint de su proyecto, estos activan.
– Las imagenes deberan ser nombradas como `./docs/assets/<slug>_<No. w/4 digits>_<description>.png`

<br>

## Descripción de mockups.

En la ventana `/docs/assets/odis-store_0001_new-visualization.png` se muestra la vista previa de nuevos registros de equipos de diagnóstico, se solicita a traves de campos de entradas los datos necesarios para un almacenamiento exitos, se solictan los siguuientes datos, la marca del equipo, el modelo de este, su número de serie, seleccionar un archivo local que debe tener un formato estricto `.dat` y con un tamaño menor a 2MB, de otro modo no se aceptara el archivo, finalmete seleccionar la fecha en la que se esta guardando ese archivo de licencia. El botón `Registrar` ejecuta la funcion de almacenamiento.

![New register visualization](https://github.com/rixr/storage-api/blob/master/docs/assets/odis-store_0001_new-visualization.png?raw=true)

<br>
<br>

En el mockup `/docs/assets/odis-store_0002_list-visualization.png` se observa una tabla que contiene todos los equipos registrados con anterioridad, su respectiva licencia asignada, esta licencia puede ser descargada dandole un click en el archivo de la licencia, finalmete en la ultima columna hay botones para editar el registro deseado;

![List of registers visualization](https://github.com/rixr/storage-api/blob/master/docs/assets/odis-store_0002_list-visualization.png?raw=true)

<br>
<br>

Esos botones de edición nos redirigen hacia otra ventana, a la ventana de `/docs/assets/odis-store_0003_update-visualization.png` aca se muestran los datos basicos del equipo seleccionado, pero los campos de `Licencia` y `Fecha` son modificables; El proposito de esta ventan es, ademas de ver los datos individuales del equipo poder actualizar los campos anteriormente mencionados. Para cambiar un archivo de licencia debes de buscarla en tu computadora, seleccionarlo y notaras que se reemplaza el archivo, despues debes de cambiar el campo de fecha, una vez realizado el proceso da click al botón de `Actualizar`, este ejecuta una funcion que hace los cambios y los guarda. Si el archivo que se intenta cambiar cumple las validaciones de formato y tamaño el cambio sera exito, de otro modo arrojara un mensaje de fallo.

![Updete register visualization](https://github.com/rixr/storage-api/blob/master/docs/assets/odis-store_0003_update-visualization.png?raw=true)

**Señalar el commit-hash que contiene la inclusión de estas Descripciones al documento, junto con los commits que contienen las imagenes.**

| Concepto                 | Commit Hash                               |
| ------------------------ | ----------------------------------------- |
| Inclusión de mockups     | d37838c05276e244d79a4364ab49dd8ed6f0ece2  |
| Descripción de mockups   | b97ce392a9b7472cf4eaa7180d8a389ea63a49d1  |

<br>

# Casos de uso

## El usuario desea agregar un equipo de diagnóstico.
- Para lograr exitosamente la accion se deben de ingresar los campos requeridos de marca, modelo, numero de serie y la fecha de registro. La estructura en la que se debe solicitar la accion es de la siguiente manera:
- Curl para registrar un nuevo dispositivo
 ```
  curl http://localhost:8080/odis/device/new \
    -X POST \
    -H 'Content-Type: application/json' \
    -d '{"brand": "getac", "model": "vas6150c", "serial_number": "123456", "date": "2021-07-29"}'
 ```

2.
3.
4.
5.
6.
