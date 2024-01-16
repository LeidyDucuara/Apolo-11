import argparse
from Simulacion import Simulacion_rum
import logging

# configurar el nivel
logging.basicConfig(level=logging.INFO)

class App:
    
    def main():
        # Configurar y obtener parametros
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", "--time", type = int, help="Configurar el intervalo de ejecución (segundos)")
        args = parser.parse_args()
        if args.time:
            logging.info("time on")
    
        # Distribuir y ejecutar el proceso seleccionado
        app = Simulacion_rum()
        app.run(args.time)
                
    if __name__ == "__main__":
            try:
                main()
            except Exception as ex:
                print(f"error generado -->: {ex}")