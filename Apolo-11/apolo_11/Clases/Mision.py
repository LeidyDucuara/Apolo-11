"""
Este módulo define la clase Mision para representar una misión espacial.
"""

import random
from pydantic import BaseModel


class Mision(BaseModel):
    """
    Clase que representa una misión espacial.

    Esta clase define la estructura de una misión espacial,
    incluyendo el nombre de la misión.
    """

    nombre_mision: str

    @staticmethod
    def generar_nombre_aleatorio():
        """Genera un nombre aleatorio para la misión."""
        lista_misiones = ["OrbitOne", "ColonyMoon", "GalaxyTwo", "VacMars", "Unknown"]
        nombre_mision = random.choice(lista_misiones)
        return nombre_mision
