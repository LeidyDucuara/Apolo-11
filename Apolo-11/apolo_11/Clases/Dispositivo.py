import random
from pydantic import BaseModel
from enum import Enum

class EstadoEnum(str, Enum):
    excellent = "excellent"
    good = "good"
    warning = "warning"
    faulty = "faulty"
    killed = "killed"
    unknown = "unknown"

class Dispositivo(BaseModel):
    tipo: str
    estado: EstadoEnum

    def __init__(self, tipo: str):
        super().__init__(tipo=tipo, estado=random.choice(list(EstadoEnum)))


class Tipo:
    
    dispositivos = ["Satelite", "Nave", "Traje", "Vehiculo espacial"]

    @staticmethod
    def agregar_dispositivo(dispositivo: str):
        Tipo.dispositivos.append(dispositivo)

    @staticmethod
    def eliminar_dispositivo(numero: int):
        if 0 <= numero < len(Tipo.dispositivos):
            dispositivo_eliminado = Tipo.dispositivos.pop(numero)
            print(f"Se eliminó el dispositivo: {dispositivo_eliminado}")
        else:
            print("No hay dispositivo en esa posición.")

    @staticmethod
    def mostrar_dispositivos():
        print("Los dispositivos son:")
        for n, dispositivo in enumerate(Tipo.dispositivos):
            print(f"{n}-{dispositivo}")
    @staticmethod
    def elegir_dispositivo():
        return random.choice(list(Tipo.dispositivos))
