class Mision:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dispositivos = ["Satelite", "Nave", "Traje", "Vehiculo espacial"]

    def agregar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)

    def eliminar_dispositivo(self, dispositivo):
        if dispositivo in self.dispositivos:
            self.dispositivos.remove(dispositivo)
        else:
            print(f"{dispositivo} no encontrado en la lista de dispositivos.")
    def mostrar_dispositivos(self):
        print(f"Los dispositivos de la mision; {self.nombre} son:")
        for dispositivo in self.dispositivos:
            print(f"-{dispositivo}")

# class Mision:
#     def _init_(self, nombre):
#         self.nombre = nombre
#         ["Satelite", "Nave", "Traje", "Vehiculo espacial"]
#         self.dispositivos = {
#             "{cod_dispositivo}" : "Traje",
#             "{cod_dispositivo}" : "Satelite",
#             "{cod_dispositivo}" : "Nave",
#             "{cod_dispositivo}" : "Vehiculo espacial",
#             }

#     def agregar_dispositivo(self, dispositivo):
#         self.dispositivos.append(dispositivo)
#     def eliminar_dispositivo(self, dispositivo):
