"""
Este módulo proporciona funcionalidad para la simulación de una misión.
"""

import argparse
import logging


from Clases.dispositivo import Tipo
from simulacion import SimulacionRun


class App:
    """
    Clase principal que maneja la lógica de la aplicación.
    """

    if __name__ == "__main__":
        try:
            # Configurar el nivel de registro
            # (apolo-11-py3.11) PS C:\Users\Administrator\Desktop\proyecto\Apolo-11\Apolo-11>
            logging.basicConfig(level=logging.INFO)

            # Configurar y obtener parámetros
            parser = argparse.ArgumentParser()
            parser.add_argument("-t", "--time", type=int, help="Configurar el intervalo de ejecución (segundos) El valor predeterminado es 20s")
            args = parser.parse_args()

            # Menú de opciones
            rango_menor = 1
            rango_mayor = 100
            ejecutar_programa = True

            while ejecutar_programa:
                opciones_menu = input('''Presione:
                                      (Se sugiere antes de eliminar, mostrar dispositivos)
                                    1. Iniciar Simulacion
                                    2. Agregar Dispositivos
                                    3. Eliminar Dispositivos
                                    4. Mostrar Dispositivos
                                    5. Modificar el rango de archivos
                                    6. Cortar
                                    ---->''')

                try:
                    opcion_seleccionada = int(opciones_menu)
                except ValueError:
                    logging.info("Error: Por favor, ingrese un valor entero.")
                    continue

                if opcion_seleccionada == 1:
                    # Distribuir y ejecutar el proceso seleccionado
                    app = SimulacionRun()
                    app.run(args.time, rango_menor, rango_mayor)
                    ejecutar_programa = False

                elif opcion_seleccionada == 2:
                    nuevo_dispositivo = input("Escriba el nombre del nuevo Dispositivo: ")
                    Tipo.agregar_dispositivo(nuevo_dispositivo)

                elif opcion_seleccionada == 3:
                    posicion_dispositivo_eliminar = int(input("Escriba La posición del dispositivo que desea eliminar: "))
                    confirmar_eliminacion = int(input("""
                                                        Presione 1 si está seguro de que desea eliminar.
                                                        Presione 2 si desea cancelar: """))

                    if confirmar_eliminacion == 1:
                        Tipo.eliminar_dispositivo(posicion_dispositivo_eliminar)
                        Tipo.mostrar_dispositivos()
                    else:
                        logging.info("Se canceló la eliminación")

                elif opcion_seleccionada == 4:
                    Tipo.mostrar_dispositivos()

                elif opcion_seleccionada == 5:
                    rango_menor = int(input("Elija el rango Mínimo: "))
                    rango_mayor = int(input("Elija rango Máximo: "))

                elif opcion_seleccionada == 6:
                    break
                else:
                    logging.info("Opción no válida. Por favor, seleccione una opción válida.")

        except ValueError as ex:
            logging.info("Error generado: %s", {ex})
