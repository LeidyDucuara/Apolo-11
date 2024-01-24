from Clases.archivo import Archivo
from Clases.dispositivo import Dispositivo, Tipo
from Clases.mision import Mision
from datetime import datetime

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

