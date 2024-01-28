"""
Este módulo proporciona funcionalidad para la simulación de una misión.
"""

import hashlib
import logging
import time
import random
from datetime import datetime

import keyboard as kb

from Clases.archivo import Archivo
from Clases.dispositivo import Dispositivo, Tipo
from Clases.mision import Mision


class SimulacionRun:
    """
    Clase que representa la simulación de una misión.
    """

    intervalo: int = 20
    salir_simulacion = False

    def run(self, time_seg: int, rango_menor: int, rango_mayor: int):
        """
        Ejecuta la simulación de la misión.
        """
        logging.info(time_seg)

        if time_seg is not None:
            self.intervalo = time_seg

        logging.info(int(self.intervalo))
        logging.info("El rango menor es: %s", rango_menor)
        logging.info("El rango Mayor es: %s", rango_mayor)

        cantidad_de_ciclos = random.randint(rango_menor, rango_mayor)
        logging.info("Cantidad de ciclos: %s", cantidad_de_ciclos)
        for _ in range(cantidad_de_ciclos):
            # time.sleep(self.intervalo)
            if kb.is_pressed("k"):
                logging.info("Tecla 'K' para salir ...")
                self.salir_simulacion = True
                break

            for _ in range(cantidad_de_ciclos):
                nombre_mision = Mision.generar_nombre_aleatorio()
                texto = self.llenado_archivo(nombre_mision)
                self.crear_y_llenar_archivo(texto)

            time.sleep(2)
            Archivo.realizar_backup()

    def llenado_archivo(self, nombre_mision):
        """
        Llena los detalles de la misión en el archivo.
        """
        tipo = Tipo.elegir_dispositivo()
        dispositivo_creado = Dispositivo(tipo)

        fecha_actual = datetime.now()
        fecha_formateada = fecha_actual.strftime("%d-%m-%Y-%H:%M:%S")

        if nombre_mision == "Unknown":
            device_status = "Unknown"
            device_type = "Unknown"
            hash_val = "No aplica"
        else:
            mision_nombre = nombre_mision
            device_status = dispositivo_creado.estado.value
            device_type = dispositivo_creado.tipo
            hash_input = f"{mision_nombre}{device_type}{device_status}"
            hash_val = hashlib.sha256(hash_input.encode()).hexdigest()

        contenido = {
            "Fecha: ": fecha_formateada,
            "Mision: ": nombre_mision,
            "Tipos de dispositivo:": device_type,
            "Estado del dispositivo: ": device_status,
            "Hash: ": hash_val
        }

        return contenido

    def crear_y_llenar_archivo(self, texto):
        """
        Crea y llena el archivo con los detalles de la misión.
        """
        nombre_archivo = Archivo.nombre_archivo(texto["Mision: "])
        ruta_archivo = Archivo.crear_archivo(nombre_archivo)
        Archivo.escribir_archivo(ruta_archivo, texto)
