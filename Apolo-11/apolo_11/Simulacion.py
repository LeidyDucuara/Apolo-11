# pylint: skip-file
import logging
import time
import random
import keyboard as kb
from Clases.mision import Mision
from Clases.archivo import Archivo
from Clases.dispositivo import Dispositivo, Tipo
from datetime import datetime





# ejemplos de registro de mensajes
#logging.debug('este es un mensaje de debug')         # 10 logging.INFO
#logging.info('esto es un mensaje de información')    # 20
#logging.warning('¡cuidado! Esto es una advertencia') # 30 logging.WARNING
#logging.error('ha ocurrido un error')                # 40 logging.ERROR
#logging.critical('este es un error crítico')         # 50

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
                    Hash = "No se todavía"
                else:
                    mision_nombre = nombre_mision
                    device_status = dispositivo_creado.estado.value
                    device_type = dispositivo_creado.tipo
                    Hash = "No se todavía"

                return f"Fecha: {fecha_formateada}\nMision: {nombre_mision}\nTipo de dispositivo: {device_type}\nEstado del dispositivo: {device_status}\nHash: {Hash}"



            def crear_y_llenar_archivo(Texto):
                nombre_archivo = Archivo.nombre_archivo(nombre_mision)
                ruta_archivo = Archivo.crear_archivo(nombre_archivo)
                Archivo.Escribir_Archivo(ruta_archivo, Texto)


            nombre_mision = Mision.generar_nombre_aleatorio()  
            texto = llenado_archivo(nombre_mision)
            crear_y_llenar_archivo(texto)
        
        Archivo.realizar_backup()



 