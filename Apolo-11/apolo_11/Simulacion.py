import logging
logging.basicConfig(level=logging.DEBUG)
# ejemplos de registro de mensajes
#logging.debug('este es un mensaje de debug')         # 10 logging.INFO
#logging.info('esto es un mensaje de información')    # 20
#logging.warning('¡cuidado! Esto es una advertencia') # 30 logging.WARNING
#logging.error('ha ocurrido un error')                # 40 logging.ERROR
#logging.critical('este es un error crítico')         # 50

class Simulacion_rum():
    intervalo: int = 20
    
    def run(self,time_seg:int):
        """_summary_

        Args:
            time_seg (int): _description_
        """        
        if time_seg != None:
            self.intervalo = time_seg
        logging.info(time_seg)
