import os
import random


class Archivo():
 
    @staticmethod
    def nombre_archivo(nombre_mision):
        Lista_misiones = ["-ORBONE", "-CLNM", "-GALAXONE","-TMRS", "-UKN"]
        nombre_archivo = "APL"

        if nombre_mision == "OrbitOne":
            mision_elegida = Lista_misiones[0]
            nombre_archivo += mision_elegida
            nombre_archivo += "-" +"0000"+ str(random.randint(1, 1000)) + ".log"
            return nombre_archivo
        elif nombre_mision == "ColonyMoon":
            mision_elegida = Lista_misiones[1]
            nombre_archivo += mision_elegida
            nombre_archivo += "-" +"0000"+ str(random.randint(1, 1000)) + ".log"
            return nombre_archivo
        elif nombre_mision == "GalaxyTwo":
            mision_elegida = Lista_misiones[2]
            nombre_archivo += mision_elegida
            nombre_archivo += "-" +"0000"+ str(random.randint(1, 1000)) + ".log"
            return nombre_archivo
        elif nombre_mision == "VacMars":
            mision_elegida = Lista_misiones[3]
            nombre_archivo += mision_elegida
            nombre_archivo += "-" +"0000"+ str(random.randint(1, 1000)) + ".log"
            return nombre_archivo
        elif nombre_mision == "Unknown":
            mision_elegida = Lista_misiones[4]
            nombre_archivo += mision_elegida
            nombre_archivo += "-" +"0000"+ str(random.randint(1, 1000)) + ".log"
            return nombre_archivo

    
    @staticmethod
    def crear_archivo(nombrearchivo):
        ruta_archivo = f'Apolo-11\\Apolo-11\\Devices\\{nombrearchivo}'

        while os.path.exists(ruta_archivo):
            nombrearchivo = Archivo.nombre_archivo()
            ruta_archivo = f'Apolo-11\\Apolo-11\\Devices\\{nombrearchivo}'

        with open(ruta_archivo, 'w') as archivo:
            pass
        print(f"Nombre del archivo creado: {nombrearchivo}")
        return ruta_archivo

        
    @staticmethod
    def Escribir_Archivo(ruta_archivo, texto):
        with open(ruta_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(texto)
            print("se escribio: ",texto)

