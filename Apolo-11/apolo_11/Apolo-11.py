import argparse
from Simulacion import Simulacion_rum
import logging

# Configurar el nivel de registro
logging.basicConfig(level=logging.INFO)

class App:

    def main():
        # Configurar y obtener parámetros
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", "--time", type=int, help="Configurar el intervalo de ejecución (segundos)")
        args = parser.parse_args()

        if args.time:
            logging.info("time on")

        # Distribuir y ejecutar el proceso seleccionado
        app = Simulacion_rum()
        app.run(args.time)

    if __name__ == "__main__":
        try:
            # Mnu opcion
            while True:
                opciones_menu = input('''Presione:
                                    1. Correr programa por defecto
                                    2. Modificar
                                    3. Agregar dispositivo
                                    4. Cortar ejecución
                        ''')

                try:
                    opcion_seleccionada = int(opciones_menu)
                except ValueError:
                    logging.info("Error: Por favor, ingrese un valor entero.")
                    continue  

                if opcion_seleccionada == 1:
                    logging.info("Corriendo programa por defecto...")
                    break  
                elif opcion_seleccionada == 2:

                    logging.info("Modificar tiempo de ejecución...")
                    break 
                elif opcion_seleccionada == 3:
                    logging.info("Agregar dispositivo...")
                    break  
                elif opcion_seleccionada == 4:
                    logging.info("Cortar ejecución...")
                    break 
                else:
                    logging.info("Opción no válida. Por favor, seleccione una opción válida.")

        except Exception as ex:
            logging.info(f"Error generado: {ex}")
