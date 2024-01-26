# pylint: skip-file
# pylint: disable=unused-import

import logging
import random
from Clases.mision import Mision
from Clases.archivo import Archivo
from Clases.dispositivo import Dispositivo, Tipo
from datetime import datetime
import hashlib
import keyboard as kb


class Simulacion_run:

    intervalo: int = 20
    salir_simulacion = False

    def run(self, time_seg: int, rango_menor: int, rango_mayor: int):
        logging.info(time_seg)

        if time_seg is not None:
            self.intervalo = time_seg

        logging.info(int(self.intervalo))
        logging.info(f"El rango menor es: {rango_menor}")
        logging.info(f"El rango Mayor es: {rango_mayor}")

        cantidad_de_ciclos = random.randint(rango_menor, rango_mayor)
        for pos in range(cantidad_de_ciclos):
            # time.sleep(self.intervalo)
            if kb.is_pressed("k"):
                logging.info("Tecla 'K' para salir ...")
                self.salir_simulacion = True
                break

            def llenado_archivo(nombre_mision):
                tipo = Tipo.elegir_dispositivo()
                dispositivo_creado = Dispositivo(tipo)

                fecha_actual = datetime.now()
                fecha_formateada = fecha_actual.strftime("%d-%m-%Y-%H:%M:%S-simulacion#")

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

            for _ in range(cantidad_de_ciclos):
                def crear_y_llenar_archivo(texto):
                    nombre_archivo = Archivo.nombre_archivo(nombre_mision)
                    ruta_archivo = Archivo.crear_archivo(nombre_archivo)
                    Archivo.Escribir_Archivo(ruta_archivo, texto)

                nombre_mision = Mision.generar_nombre_aleatorio()
                texto = llenado_archivo(nombre_mision)
                crear_y_llenar_archivo(texto)

            Archivo.realizar_backup(pos)
