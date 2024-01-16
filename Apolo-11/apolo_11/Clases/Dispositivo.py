import random

class Dispositivo:
    lista_estados = ["excellent", "good", "warning", "faulty", "killed", "unknown"]
    def __init__(self, tipo):
        self.tipo = tipo
        #self.lista_estados = ["excellent", "good", "warning", "faulty", "killed", "unknown"]
    @classmethod
    def elegir_estado_random(cls):
        return random.choice(cls.lista_estados)

