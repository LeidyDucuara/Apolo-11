"""
Este módulo proporciona funcionalidad para trabajar con archivos relacionados con misiones.
"""

import os
import random
import json
from datetime import datetime
from shutil import copy


class Archivo:
    """
    Esta clase proporciona funciones para trabajar con archivos relacionados con misiones.
    """

    @staticmethod
    def nombre_archivo(nombre_mision=None):
        """
        Genera un nombre de archivo basado en el nombre de la misión.
        Si no se proporciona ningún nombre de misión, se genera uno aleatorio.
        """
        lista_misiones = ["OrbitOne", "ColonyMoon", "GalaxyTwo", "VacMars", "Unknown"]

        if nombre_mision is None:
            nombre_mision = random.choice(lista_misiones)

        lista_misiones_abreviadas = ["-ORBONE", "-CLNM", "-GALAXONE", "-TMRS", "-UKN"]
        nombre_archivo = "APL"

        if nombre_mision == "OrbitOne":
            mision_elegida = lista_misiones_abreviadas[0]
        elif nombre_mision == "ColonyMoon":
            mision_elegida = lista_misiones_abreviadas[1]
        elif nombre_mision == "GalaxyTwo":
            mision_elegida = lista_misiones_abreviadas[2]
        elif nombre_mision == "VacMars":
            mision_elegida = lista_misiones_abreviadas[3]
        else:
            mision_elegida = lista_misiones_abreviadas[4]

        nombre_archivo += mision_elegida
        nombre_archivo += "-" + "0000" + str(random.randint(1, 1000)) + ".log"
        return nombre_archivo

    @staticmethod
    def crear_archivo(nombrearchivo=None):
        """
        Crea un archivo con el nombre especificado.
        Si no se proporciona ningún nombre de archivo, se generará uno aleatorio.
        """
        os.makedirs('Devices', exist_ok=True)

        if nombrearchivo is None:
            nombrearchivo = Archivo.nombre_archivo()

        ruta_archivo = os.path.join('Devices', nombrearchivo)

        while os.path.exists(ruta_archivo):
            nombrearchivo = Archivo.nombre_archivo()
            ruta_archivo = os.path.join('Devices', nombrearchivo)

        # No es necesario abrir el archivo y no hacer nada, eliminar esto.
        print(f"Nombre del archivo creado: {nombrearchivo}")
        return ruta_archivo

    @staticmethod
    def escribir_archivo(ruta_archivo, texto):
        """
        Escribe el texto en el archivo especificado.
        """
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(texto, archivo, indent=4)
            print("se escribio: ", texto)

    @staticmethod
    def realizar_backup():
        """
        Realiza una copia de seguridad de los archivos en la carpeta 'Devices'.
        """
        fecha_hora_actual = datetime.now().strftime("%d-%m-%Y-%#H_%M%S")
        ruta_devices = os.path.join('Devices')
        archivos_en_devices = os.listdir(ruta_devices)

        nombre_carpeta_backup = os.path.join('Backup', fecha_hora_actual)
        os.makedirs(nombre_carpeta_backup, exist_ok=True)

        for archivo in archivos_en_devices:
            ruta_origen = os.path.join(ruta_devices, archivo)
            ruta_destino = os.path.join(nombre_carpeta_backup, archivo)

            copy(ruta_origen, ruta_destino)

            os.remove(ruta_origen)
