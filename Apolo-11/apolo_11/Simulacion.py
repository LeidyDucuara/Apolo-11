import logging
import random
from Clases.dispositivo import Dispositivo

# ejemplos de registro de mensajes
#logging.debug('este es un mensaje de debug')         # 10 logging.INFO
#logging.info('esto es un mensaje de información')    # 20
#logging.warning('¡cuidado! Esto es una advertencia') # 30 logging.WARNING
#logging.error('ha ocurrido un error')                # 40 logging.ERROR
#logging.critical('este es un error crítico')         # 50

class Simulacion_run():
    intervalo: int = 20
    tipos_dispositivos : list = ['nave', 'traje', 'satelite']

    def run(self,time_seg:int, cant: int):

        logging.info(time_seg)   
        logging.info(cant)    
        archivos: int = cant
        dispositivos = []

        if time_seg != None:
            self.intervalo = time_seg
        logging.info(self.intervalo)
        if cant == None:
            archivos: int = random.randint(0,100)
        logging.info(archivos)  
        print('hola')
        for i in range (archivos): 
            tipo = random.choice(self.tipos_dispositivos)
            dispo = Dispositivo(tipo)
            dispositivos.append(dispo)

            print(dispositivos)
            
            


        
    

 