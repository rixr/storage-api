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
En la siguiente tabla se específica cuales son las rutas con las que cuenta este proyecto, ademas del método HTTP que se utiliza, la ruta como tal y una breve descripción de su función.
| Método | Path                                            | Descripción                                         |
| -------|-------------------------------------------------|-----------------------------------------------------|
| POST   | `/odis/device/new`                              | Almacena nuevos equipos de diagnóstico              |
| POST   | `/odis/license/new/<license_number>`            | Almacena nuevas licencias                           |
| GET    | `/odis/list`                                    | Muestra todos los equipos de diagnostico            |
| POST   | `/odis/assign/<license_number>/<serial_number>` | Asigna una licencia a un equipo de diagnostico      |
| POST   | `/odis/device/<serial_number>`                  | Muestra toda la información del registro deseado    |

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
1. Correr servidor de ambiente con el siguiente comando:
`winpty pipenv run start`


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

En la ventana `/docs/assets/odis-store_0001_new-visualization.png` se muestra la vista previa de nuevos registros de equipos de diagnóstico, se solicita a traves de campos de entradas los datos necesarios para un almacenamiento exitos, se solictan los siguuientes datos, la marca del equipo, el modelo de este, su número de serie, seleccionar un archivo local que debe tener un formato estricto `.dat` y con un tamaño menor a 2MB, de otro modo no se aceptara el archivo, finalmete seleccionar la fecha en la que se esta guardando ese archivo de licencia. El botón `Registrar` ejecuta la función de almacenamiento.

![New register visualization](https://github.com/rixr/storage-api/blob/master/docs/assets/odis-store_0001_new-visualization.png?raw=true)

<br>
<br>

En el mockup `/docs/assets/odis-store_0002_list-visualization.png` se observa una tabla que contiene todos los equipos registrados con anterioridad, su respectiva licencia asignada, esta licencia puede ser descargada dandole un click en el archivo de la licencia, finalmete en la ultima columna hay botones para editar el registro deseado;

![List of registers visualization](https://github.com/rixr/storage-api/blob/master/docs/assets/odis-store_0002_list-visualization.png?raw=true)

<br>
<br>

Esos botones de edición nos redirigen hacia otra ventana, a la ventana de `/docs/assets/odis-store_0003_update-visualization.png` aca se muestran los datos basicos del equipo seleccionado, pero los campos de `Licencia` y `Fecha` son modificables; El proposito de esta ventan es, ademas de ver los datos individuales del equipo poder actualizar los campos anteriormente mencionados. Para cambiar un archivo de licencia debes de buscarla en tu computadora, seleccionarlo y notaras que se reemplaza el archivo, despues debes de cambiar el campo de fecha, una vez realizado el proceso da click al botón de `Actualizar`, este ejecuta una función que hace los cambios y los guarda. Si el archivo que se intenta cambiar cumple las validaciones de formato y tamaño el cambio sera exito, de otro modo arrojara un mensaje de fallo.

![Updete register visualization](https://github.com/rixr/storage-api/blob/master/docs/assets/odis-store_0003_update-visualization.png?raw=true)

**Señalar el commit-hash que contiene la inclusión de estas Descripciones al documento, junto con los commits que contienen las imagenes.**

| Concepto                 | Commit Hash                                   |
| ------------------------ | --------------------------------------------- |
| Inclusión de mockups     | d37838c05276e244d79a4364ab49dd8ed6f0ece2      |
| Descripción de mockups   | git b97ce392a9b7472cf4eaa7180d8a389ea63a49d1  |

<br>

# Casos de uso

## El usuario desea agregar un equipo de diagnóstico.
- Para lograr exitosamente la acción se deben de ingresar los campos requeridos de marca, modelo, número de serie y la fecha de registro. La estructura en la que se debe solicitar la acción es de la siguiente manera:
- Curl para registrar un nuevo dispositivo
 ```
  curl http://localhost:8080/odis/device/new \
    -X POST \
    -H 'Content-Type: application/json' \
    -d '{"brand": "getac", "model": "vas6150c", "serial_number": "123456", "date": "2021-08-17"}'
 ```

<br>

## El usuario desea registrar una licencia.
- Para ello se requiere especificar una ruta que contiene el archivo de la licencia que sera almacenada. Tambien se solicita el nombre que llevara la licencia, este es especificado en el enlace, es decir, "http://localhost:8080/odis/license/new/{NOMBRE_DE_LA_LICENCIA}"
- Curl para registrar un nuevo dispositivo
 ```
  curl http://localhost:8080/odis/license/new/license_214 \
    -X POST \
    -H 'Content-Type: multipart/form-data' \
    -F 'license_file=@C:/Users/Ricardo/license.txt'
 ```

<br>

## El usuario desea ver todos los equipos registrados.
- Obtendremos lo deseado haciendo la consulta a la direccion "http://localhost:8080/odis/list", se mostrara una lista con todos los registros previos.
- Curl para obtener una lista de todos los equipos.
 ```
  curl http://localhost:8080/odis/list -X GET
 ```

<br>

## El usuario desea ver la informacion de un equipo especifico.
- Se podra consultar lo deseado a traves de la siguente direccion, donde se especifica cual es el número de serie del equipo que se busca, por ejemplo, "http://localhost:8080/device/{NUMERO_DE_SERIE_DEL_EQUIPO}".
- Curl para obtener equipo especifico.
 ```
  curl http://localhost:8080/odis/device/123456 -X GET
 ```

 <br>

## El usuario desea asignar una licencia a un equipo de diagnostico.
- Para realizarlo de manera correcta se debe de especificar dentro del URL el numeor de licencia y el número de serie del equipo.
- Curl para asignar una licencia a un equipo de diagnóstico.
 ```
  curl http://localhost:8080/odis/assign/101187_2021-07-31.dat/getac_vas6150c_123456.json \
    -X POST \
    -H 'Content-Type: application/json' \
    -d '{"license_number": "101187_2021-07-31.dat", "serial_number": "getac_vas6150c_123456.json"}'
 ```

 <br>

# Documentación para futuros cambios en el backend
- El primero de los cambios y que es una de las funciones mas utiles del proyecto es la de asignar una licencia registrada a un equipo de diagnóstico que al igual esta registrado previamente, esto es obligatorio puesto a que se trata solo de relacionar ambos registros. A continuación se explica la funcionalidad que se desea:
  - Esta función recibe en el URL dos datos, el nombre de la licencia y el número de serie del equipo al que se relacionará.
  - Una vez que estos datos son recibidos se debe de validar su existencia dentro de los directorios de almacenamiento, ubicados en _`./storage/odis/device/`_ para los equipo de diagnóstico y en el directorio _`./storage/odis/license/`_ para las licencias.
- Si ambos registros existen entonces un nuevo archivo `.json` será almacenado dentro de la nueva ruta _`./storage/odis/assign/`_, el contenido del archivo .json será un diccionario con:
  - license_number, el número o nombre de licencia que se asignará
  - serial_number, el equipo a la cual se ligara la licencia
  - date, la fecha en la que se esta haciendo la asignación

En caso de que uno de los dos datos solicitados no exita se regresará un de error con el mensaje de "Invalid data".

La función "assign_license2device" se encuentra en el siguiente archivo _`./modules/odis_store.py`_, ya esta estructurada y con un breve docstring que detalla un poco mas de lo que se desea. Su función _dummy_ "assign_license" esta escrito en el archivo _`./routes/odis_store.py`_.

<br>

Otro de los cambios son las validaciones alrededor del archivo de la licencia, básicamente seria la validación de extensioón y la validación del tamaño del archivo.
- Para la validación de extensión de archivo, unicamente se aceptaran archivo con la extensión `.dat`, de lo contrario se levantara un error con el mensaje de ¨Invalid data - File Type¨.
- Para la validación de tamaño de archivo se requiere que este no exceda los 2MB, de lo contrario se levantara un error con el mensaje de ¨Invalid data - File Size¨.

Estas validaciones deberan estar implementadas en la función ¨store_new_license¨ que es la encargada de el almacenamiento de los archivos de licencia, esta se encuentra dentro del archivo _`./modules/odis_store.py`_.

<br>

# Planeación de desarrollo del frontend
Primeramente mecionar que sin el correcto funcionamiento del backend no se puede avanzar al desarrollo de frontend, sin embargo, la planeación del mismo es de suma importancia para este proyecto debido a que se espera hacer el despliegue en nube para el futuro.

La pagina principal del proyecto sera una ventana en la cual se presentan tres botones, uno para ¨agregar equipos¨, uno para ¨agregar licencias¨ y otro para ¨consultar registros¨, cada uno de ellos nos lleva a ventanas diferente y con acciones diferentes:
- **Agregar equipo**  
Al dar clic en este botón nos redirecciona a una ventana donde se presenta un formulario con campos de cadena de texto, todos obligatorios, estos son, Marca, Modelo, Número de Serie y Fecha en el que se esta haciendo el registro. En la parte inferior se encuentra un botón que procede a guardar los campos requeridos. Si alguno de los datos no es ingresado se levantará un error con el mensajes "Invalid data"

<br>

- **Agregar licencia**  
Se presenta un formulario con un campo para anadir archivos, en el cual se indica la ruta donde se encuentra el archivo de licencia. En la parte inferior se encuentra un botón que procede a guardar el archivo seleccionado. De no seleccionar algun archivo que cumpla con las vaidaciones necesarias se levantara un error con su respectivo mensaje de error.

<br>

- **Consultar registros**  
Se muestra una lista con todos los registros previos de los equipos de diagnóstico, mostrando la fecha en la que se registraron y la licencia que se le fue asignada.
