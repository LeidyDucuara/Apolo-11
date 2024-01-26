# pylint: skip-file
import logging
import time
import random
import keyboard as kb
from Clases.mision import Mision
from Clases.archivo import Archivo
from Clases.dispositivo import Dispositivo, Tipo
from datetime import datetime
import hashlib

class Simulacion_run():
    intervalo: int = 20
    
    def run(self,time_seg: int, rango_menor: int, rango_mayor: int):

        logging.info(time_seg)   
        if time_seg != None:
            self.intervalo = time_seg
        logging.info(int(self.intervalo))
        logging.info(f"El rango menor es: {rango_menor}")
        logging.info(f"El rango Mayor es: {rango_mayor}")
        for _ in range(random.randint(rango_menor, rango_mayor)):
            #time.sleep(self.intervalo)

            def llenado_archivo(nombre_mision):
                tipo = Tipo.elegir_dispositivo()
                dispositivo_creado = Dispositivo(tipo)
                
                fecha_actual = datetime.now()
                fecha_formateada = fecha_actual.strftime("%d-%m-%Y-%H:%M:%S")
                
                if nombre_mision == "Unknown":
                    device_status = "Unknown"
                    device_type = "Unknown"
                    hash = "No aplica"
                else:
                    mision_nombre = nombre_mision
                    device_status = dispositivo_creado.estado.value
                    device_type = dispositivo_creado.tipo
                    hash_input = f"{mision_nombre}{device_type}{device_status}"
                    hash=hashlib.sha256(hash_input.encode()).hexdigest()


                return f"Fecha: {fecha_formateada}\nMision: {nombre_mision}\nTipo de dispositivo: {device_type}\nEstado del dispositivo: {device_status}\nHash: {hash}"



            def crear_y_llenar_archivo(Texto):
                nombre_archivo = Archivo.nombre_archivo(nombre_mision)
                ruta_archivo = Archivo.crear_archivo(nombre_archivo)
                Archivo.Escribir_Archivo(ruta_archivo, Texto)


            nombre_mision = Mision.generar_nombre_aleatorio()  
            texto = llenado_archivo(nombre_mision)
            crear_y_llenar_archivo(texto)
        
        Archivo.realizar_backup()



 