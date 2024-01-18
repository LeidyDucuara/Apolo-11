from dispositivo import Dispositivo

satelite = Dispositivo(tipo="Satelite")
nave_espacial = Dispositivo(tipo="Nave")
traje_espacial = Dispositivo(tipo="Traje")
vehiculo_espacial = Dispositivo(tipo="Vehiculo espacial")


class Tipo_Dispositivo():
    dispositivos = [satelite, nave_espacial, traje_espacial, vehiculo_espacial]   

    @staticmethod
    def mostrar_dispositivos():
        n=-1
        for dispositivo in Tipo_Dispositivo.dispositivos:
            n=n+1
            print(f"{n}.Tipo: {dispositivo._Dispositivo__tipo}, ID: {dispositivo.id_dispositivo}")
    @staticmethod
    def agregar_dispositivo(tipo):
        nuevo_dispositivo = Dispositivo(tipo=tipo)
        Tipo_Dispositivo.dispositivos.append(nuevo_dispositivo)
        return nuevo_dispositivo
    @staticmethod
    def eliminar_dispositivo_por_indice(indice):
        if 0 <= indice < len(Tipo_Dispositivo.dispositivos):
            dispositivo_eliminado = Tipo_Dispositivo.dispositivos.pop(indice)
            print(f"Dispositivo eliminado: Tipo: {dispositivo_eliminado._Dispositivo__tipo}, ID: {dispositivo_eliminado.id_dispositivo}")
        else:
            print("Índice fuera de rango. No se eliminó ningún dispositivo.")


Tipo_Dispositivo.agregar_dispositivo("Nave Nueva")
Tipo_Dispositivo.mostrar_dispositivos()
Tipo_Dispositivo.eliminar_dispositivo_por_indice(4)