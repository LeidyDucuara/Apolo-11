import hashlib
from datetime import datetime

def obtener_hash_fecha():
    # Obtener la fecha y hora actual
    fecha_hora_actual = datetime.now()

    # Formatear la fecha y hora según el formato especificado (ddmmyyHHMISS)
    fecha_formateada = fecha_hora_actual.strftime("%d%m%y%H%M%S")

    # Calcular el hash de la fecha formateada
    hash_fecha = hashlib.sha256(fecha_formateada.encode()).hexdigest()

    return hash_fecha

# Ejemplo de uso
hash_fecha = obtener_hash_fecha()
print("Hash de la fecha actual:", hash_fecha)
