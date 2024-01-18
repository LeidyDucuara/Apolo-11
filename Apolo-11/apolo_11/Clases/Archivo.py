import os
import random
from dispositivo import Dispositivo

class Archivo():
 
    @staticmethod
    def generar_nombre_aleatorio(Nombre_mision):
        Lista_misiones = ["-ORBONE", "-CLNM", "-GALAXONE", "-UKN"]
        nombre_archivo = "APL"
        mision_elegida = random.choice(Lista_misiones)
        nombre_archivo += mision_elegida
        nombre_archivo += "-" +"0000"+ str(random.randint(1, 1000)) + ".log"
        return nombre_archivo
    @staticmethod
    def crear_archivo(nombrearchivo):
        ruta_archivo = f'Apolo-11\\Apolo-11\\Devices\\{nombrearchivo}'

        while os.path.exists(ruta_archivo):
            nombrearchivo = Archivo.generar_nombre_aleatorio()
            ruta_archivo = f'Apolo-11\\Apolo-11\\Devices\\{nombrearchivo}'

        with open(ruta_archivo, 'w') as archivo:
            pass
        print(f"Nombre del archivo creado: {nombrearchivo}")
        return ruta_archivo

        
    @staticmethod
    def Escribir_Archivo(ruta_archivo, texto):
        with open(ruta_archivo, 'a') as archivo:
            archivo.write(texto)
            print("se escribio: ",texto)

# a=Archivo.generar_nombre_aleatorio()
# b=Archivo.crear_archivo(a)
# texto=Dispositivo.elegir_estado_random()
# C=Archivo.Escribir_Archivo(b,texto)

 