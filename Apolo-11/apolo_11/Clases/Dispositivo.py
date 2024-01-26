"""
Módulo que contiene las clases relacionadas con los dispositivos.
"""

import random
from enum import Enum
from pydantic import BaseModel


class EstadoEnum(str, Enum):
    """
    Enumeración que define los posibles estados de un dispositivo.
    """

    EXCELLENT = "excellent"
    GOOD = "good"
    WARNING = "warning"
    FAULTY = "faulty"
    KILLED = "killed"
    UNKNOWN = "unknown"


class Dispositivo(BaseModel):
    """
    Clase que representa un dispositivo.
    """

    tipo: str
    estado: EstadoEnum

    def __init__(self, tipo: str):
        """
        Inicializa una instancia de Dispositivo con el tipo especificado.
        """
        super().__init__(tipo=tipo, estado=random.choice(list(EstadoEnum)))


class Tipo:
    """
    Clase que define diferentes tipos de dispositivos.
    """

    dispositivos = ["Satelite", "Nave", "Traje", "Vehiculo espacial"]

    @staticmethod
    def agregar_dispositivo(dispositivo: str):
        """
        Agrega un dispositivo a la lista de dispositivos disponibles.
        """
        Tipo.dispositivos.append(dispositivo)

    @staticmethod
    def eliminar_dispositivo(numero: int):
        """
        Elimina un dispositivo de la lista de dispositivos disponibles.
        """
        if 0 <= numero < len(Tipo.dispositivos):
            dispositivo_eliminado = Tipo.dispositivos.pop(numero)
            print(f"Se eliminó el dispositivo: {dispositivo_eliminado}")
        else:
            print("No hay dispositivo en esa posición.")

    @staticmethod
    def mostrar_dispositivos():
        """
        Muestra la lista de dispositivos disponibles.
        """
        print("Los dispositivos son:")
        for n, dispositivo in enumerate(Tipo.dispositivos):
            print(f"{n}-{dispositivo}")

    @staticmethod
    def elegir_dispositivo():
        """
        Elige un dispositivo aleatorio de la lista de dispositivos disponibles.
        """
        return random.choice(list(Tipo.dispositivos))
