class Mision:
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.dispositivos = ["Satelite", "Nave", "Traje", "Vehiculo espacial"]

    def agregar_dispositivo(self, dispositivo:str):
        self.dispositivos.append(dispositivo)

    def eliminar_dispositivo(self, numero:int):
        if 0 <= numero < len(self.dispositivos):
            dispositivo_eliminado = self.dispositivos.pop(numero)
            print(f"Se elimino el dispositivo: {dispositivo_eliminado}")
        else:
            print("No hay dispositivo en esa posicion:")
    def mostrar_dispositivos(self):
        print(f"Los dispositivos de la mision; {self.nombre} son:")
        n=-1
        for dispositivo in self.dispositivos:
            n=n+1
            print(f"{n}-{dispositivo}")


    