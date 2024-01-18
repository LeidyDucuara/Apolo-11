import argparse
from Simulacion import Simulacion_run
import logging

# Configurar el nivel de registro
logging.basicConfig(level=logging.INFO)

class App:

    def main():

        # Configurar y obtener parámetros
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", "--time", type=int, help="Configurar el intervalo de ejecución (segundos)")
        parser.add_argument("-c", "--cant", type=int, help="Configurar la cantidad de archivos generados")
        args = parser.parse_args()

        if args.time:
            logging.info("time on")
        
        if args.cant:
            logging.info("cant on")

        # Distribuir y ejecutar el proceso seleccionado
        app = Simulacion_run()
        app.run(args.time, args.cant)

    if __name__ == "__main__":
        try:
            main()
            # Mnu opcion
            while True:
                opciones_menu = input('''Presione:
                                    1. Iniciar Simulacion
                                    2. Agregar dispositivo
                                    3. Eliminar dispositivo
                                    4. Cortar
                                    
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
