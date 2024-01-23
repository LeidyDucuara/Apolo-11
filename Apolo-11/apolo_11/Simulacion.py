import logging
import random


# ejemplos de registro de mensajes
#logging.debug('este es un mensaje de debug')         # 10 logging.INFO
#logging.info('esto es un mensaje de información')    # 20
#logging.warning('¡cuidado! Esto es una advertencia') # 30 logging.WARNING
#logging.error('ha ocurrido un error')                # 40 logging.ERROR
#logging.critical('este es un error crítico')         # 50

class Simulacion_run():
    intervalo: int = 20
    
    def run(self,time_seg:int, valor_range: str):

        logging.info(time_seg)   
        logging.info(valor_range)    
        #Cantidad_archivos: int = cant
        

        if time_seg != None:
            self.intervalo = time_seg
        logging.info(self.intervalo)
        #if cant == None:
        #    Cantidad_archivos: int = random.randint(1,100)
        #logging.info(Cantidad_archivos)  
        #print(Cantidad_archivos)


        
        
        
            
            


        
    

 