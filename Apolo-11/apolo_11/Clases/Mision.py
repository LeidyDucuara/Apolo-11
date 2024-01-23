from pydantic import BaseModel
import random

class Mision(BaseModel):
    nombre_mision: str

    @staticmethod
    def generar_nombre_aleatorio():
        lista_misiones = ["OrbitOne", "ColonyMoon", "VacMars", "GalaxyTwo"]
        nombre_mision = random.choice(lista_misiones)
        return nombre_mision

