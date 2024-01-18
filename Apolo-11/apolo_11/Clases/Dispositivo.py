import random
from enum import Enum
#dispositivos = 
#class syntax
class Estado(Enum):
    excellent = 1
    good = 2
    warning = 3
    faulty = 4
    killed = 5
    unknown = 6
# functional syntax
Estado = Enum('Estado', ['excellent', 'good', 'warning', 'faulty', 'killed', 'unknown'])

class Mision_enum(Enum):
    OrbitOne = 'ORBONE'
    ColonyMoon = 'CLMN'
    VacMars = 'TMRS'
    GalaxyTwo = 'GALXONE'
    unknown = 'UKN'
# functional syntax
Mision_enum = Enum('Mision_enum', ["OrbitOne", "ColonyMoon", "VacMars", "GalaxyTwo","unknown"])


class Dispositivo():

    id_dispositivo: int = 0
    tipo : str = None
    estado : str = None
    mision : str = None

    def __init__(self, tipo):
        self.id_dispositivo = Dispositivo.generar_id_dispositivo()
        self.tipo = tipo
        
    
    def elegir_estado_random(self):
        self.estado = random.choice(list(Estado))
    
    
    def elegir_mision_random(self):
        self.mision = random.choice(list(Mision_enum))

    @staticmethod
    def generar_id_dispositivo():
        Dispositivo.id_dispositivo += 1
        return Dispositivo.id_dispositivo
    
    
    def mostrar_info(self):
        return f"Tipo: {str(self.tipo)} Mision: {str(self.mision.name)} Estado:  {self.estado.name}"


dispo = Dispositivo("satelite")
dispo.elegir_estado_random()
dispo.elegir_mision_random()
print(dispo.mostrar_info())