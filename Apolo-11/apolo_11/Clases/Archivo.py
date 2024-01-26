# pylint: skip-file
from Clases.mision import Mision
import os
import random
from shutil import copy
from datetime import datetime


class Archivo:

    @staticmethod
    def nombre_archivo(nombre_mision):
        Lista_misiones = ["-ORBONE", "-CLNM", "-GALAXONE", "-TMRS", "-UKN"]
        nombre_archivo = "APL"

        if nombre_mision == "OrbitOne":
            mision_elegida = Lista_misiones[0]
            nombre_archivo += mision_elegida
            nombre_archivo += "-" + "0000" + str(random.randint(1, 1000)) + ".log"
            return nombre_archivo
        elif nombre_mision == "ColonyMoon":
            mision_elegida = Lista_misiones[1]
            nombre_archivo += mision_elegida
            nombre_archivo += "-" + "0000" + str(random.randint(1, 1000)) + ".log"
            return nombre_archivo
        elif nombre_mision == "GalaxyTwo":
            mision_elegida = Lista_misiones[2]
            nombre_archivo += mision_elegida
            nombre_archivo += "-" + "0000" + str(random.randint(1, 1000)) + ".log"
            return nombre_archivo
        elif nombre_mision == "VacMars":
            mision_elegida = Lista_misiones[3]
            nombre_archivo += mision_elegida
            nombre_archivo += "-" + "0000" + str(random.randint(1, 1000)) + ".log"
            return nombre_archivo
        elif nombre_mision == "Unknown":
            mision_elegida = Lista_misiones[4]
            nombre_archivo += mision_elegida
            nombre_archivo += "-" + "0000" + str(random.randint(1, 1000)) + ".log"
            return nombre_archivo

    @staticmethod
    def crear_archivo(nombrearchivo):
        os.makedirs('Devices', exist_ok=True)
        ruta_archivo = os.path.join('Devices', nombrearchivo)

        while os.path.exists(ruta_archivo):
            nombre_mision = Mision.generar_nombre_aleatorio()
            nombrearchivo = Archivo.nombre_archivo(nombre_mision)
            ruta_archivo = os.path.join('Devices', nombrearchivo)

        with open(ruta_archivo, 'w'):
            pass
        print(f"Nombre del archivo creado: {nombrearchivo}")
        return ruta_archivo

    @staticmethod
    def Escribir_Archivo(ruta_archivo, texto):
        with open(ruta_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(texto)
            print("se escribio: ", texto)

    @staticmethod
    def realizar_backup():
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
