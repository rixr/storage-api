import os
import datetime as dt
import json
import re
from modules.storage import (
    store_string,
    store_bytes,
    query_storage
)

def store_new_license(license_number = None, license_file = None):
    """
    Registra una nueva licencia

    Recibe diferentes parametros para que se pueda ejecutar exitosamente debe
    de contener los siguientes datos:
    - brand, cadena de texto que específica la marca del equipo de diagnostico
    - license_number, cadena de texto que especifica el numero o nombre que
    llevara la licencia
    - license_file, cadena de texto que especifica en donde se encuentra el
    archivo, es decir la ruta, que contiene los datos de la licencia

    Curl para registrar un nuevo dispositivo
    curl http://localhost:8080/odis/license/new/license_12 \
      -X POST \
      -H 'Content-Type: multipart/form-data' \
      -F 'license_file=@C:/Users/Ricardo/license.txt'

      Regresa un diccionario con los datos anteriormente especificados, con un
      mesaje de "Datos validos".
    """
    date = dt.date.today().isoformat()
    filename = f"{license_number}_{date}.dat"
    store_bytes(
        "odis/license", # ruta en donde se almacenaran las licencias
        filename,
        license_file.read()
    )
    return f"odis/license/{filename}"



def store_new_device(brand = None, model = None, serial_number = None, date = None):
    """
    Registra un nuevo equipo de diagnostico

    Recibe diferentes parametros para que se pueda ejecutar exitosamente
    - brand, cadena de texto que específica la marca del equipo de diagnostico
    - model, cadena de texto que específica el modelo del equipo de diagnostico
    - serial_number, cadena de texto que específica el umero de serie del equipo
    - date, cadena de texto que específica la fecha en la que se esta haciendo
    el registro del equipo con el formato yyyy-mm-dd

    Curl para registrar un nuevo dispositivo
    curl http://localhost:8080/odis/device/new \
      -X POST \
      -H 'Content-Type: application/json' \
      -d '{"brand": "getac", "model": "vas6150c", "serial_number": "123456", "date": "2021-07-29"}'

      Regresa un diccionario con los datos anteriormente especificados, con un
      mesaje de "Datos validos".
    """

    filename = f"{serial_number}.json"
    data = dict(brand = brand, model = model, serial_number = serial_number, date = date) # Datos que seran escritos dentro del json
    # Ejecuta el guardado de los nuevos archivos json, en la nueva carpeta
    store_string(
        "odis/device", # ruta en donde se almacenaran los equipos
        filename,
        json.dumps(data)
    )
    return f"odis/device/{filename}"



# TODO
def get_storage_device(path = None):
    """
    busca todos los equipos registrados

    CURL PARA OBTENER UNA LISTA DE TODOS LOS EQUIPOS REGISTRADOS
    curl http://localhost:8080/odis/list -X GET

    Regresa un diccionario con todos los equipos.
    """
    query_result = query_storage(
        "odis/device", #ruta en donde estan almacenadas los equipos
    )
    print(query_result)
    return query_result['content']



# ESPECIFICO
def get_license_by_sn(serial_number = None):
    """
    busca equipos registrados dado un numero de serie

    CURL PARA OBTENER LAS LICENCIAS DADO UN NUMERO DE SERIE
    curl http://localhost:8080/odis/device/license1 -X GET

    Regresa un diccionario con el equipo deseado.
    """
    query_result = query_storage(
        "odis/license", # ruta donde se almacenan las licencias
    )

    # Busqueda del numero de serie especificado en el URL
    if serial_number is not None:
        return [
            r
            for r in query_result["content"]
            if serial_number in r
        ]



def assign_license2device(license_number = None, serial_number = None):
    """
    Asigna una licencia a un equipo de diagnostico.

    Recibe dentro del URL los datos para poder hacer la asignacion correctamente.
    - license_number, numero o nombre de la licencia
    - serial_number, numero de serie del equipo de diagnóstico

    CURL PARA ASIGNAR LICENCIA A EQUIPOS
    curl http://localhost:8080/odis/assign/101187_2021-07-31.dat/getac_vas6150c_123456.json \
      -X POST \
      -H 'Content-Type: application/json' \
      -d '{"license_number": "101187_2021-07-31.dat", "serial_number": "getac_vas6150c_123456.json"}'

    Regresa un diccionario con los datos anteriormente especificados, con un
    mesaje de "Datos validos".
    """

    date = dt.date.today().isoformat()

    # Hace una consulta a la ruta de almacenamiento de equipos de diagnostico
    device_query = get_storage_file(
        "odis/device",
    )
    # Hace una consulta a la ruta de almacenamiento de licencias
    license_query = get_storage_file(
        "odis/license",
    )

    # Evalua si los datos solicitados en el URL existen
    if (license_number in license_query.values() and serial_number in device_query.values()):
        filename = f"{license_number}_to_{serial_number}_at_{date}.json"
        data = dict(license_number = license_number, serial_number = serial_number, date = date) # Datos que seran escritos dentro del json
        # Ejecuta el guardado de los nuevos archivos json, en la nueva carpeta
        store_string(
            "odis/assign",
            filename,
            json.dumps(data)
        )
        return f"odis/assign/{filename}"
