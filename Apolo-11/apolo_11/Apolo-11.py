# pylint: skip-file
import argparse
from Simulacion import Simulacion_run
import logging
from Clases.dispositivo import Dispositivo, Tipo, EstadoEnum
#from apolo_11.Clases.archivo import Archivo

#from apolo_11.Clases.mision import Mision

# Configurar el nivel de registro
logging.basicConfig(level=logging.INFO)

class App:

    if __name__ == "__main__":
        try:
            # Configurar y obtener parámetros
            parser = argparse.ArgumentParser()
            parser.add_argument("-t", "--time", type=int, help="Configurar el intervalo de ejecución (segundos) El valor predeterminado es 20s")
            args = parser.parse_args()

            # Mnu opcion
            rango_menor: int = 1
            rango_mayor: int = 100

            ejecutar_programa=True
            while ejecutar_programa:

                opciones_menu = input('''Presione:
                                      (Se sugiere antes de eliminar, mostrar dispositivos)
                                    1. Iniciar Simulacion
                                    2. Agregar Dispositivos
                                    3. Eliminar Dispositivos
                                    4. Mostrar Dispositivos
                                    5. Modfica el rango archivos
                                    6. Cortar
                                    
                        ''')

                try:
                    opcion_seleccionada = int(opciones_menu)
                except ValueError:
                    logging.info("Error: Por favor, ingrese un valor entero.")
                    continue

                if opcion_seleccionada == 1:

                    # Distribuir y ejecutar el proceso seleccionado
                    app = Simulacion_run()
                    app.run(args.time, rango_menor, rango_mayor)
                   
                    ejecutar_programa= False
                          
                elif opcion_seleccionada == 2:
                    Nuevo_Dispositivo=input("Escriba el nombre del nuevo Dispositivo: ")      
                    Tipo.agregar_dispositivo(Nuevo_Dispositivo)
                     
                elif opcion_seleccionada == 3:
                    
                    
                    Posicion_Dispositivo_Eliminar=int(input("Escriba La posicion del dispositivo que que deseas eliminar:"))      
                    confrimar_eliminacion=int(input("""
                                                        Presione 1 si esta seguro de que desea eliminar.
                                                        Presione 2 si desea cancelar: """))
                    
                    if confrimar_eliminacion==1:
                       
                       Tipo.eliminar_dispositivo(Posicion_Dispositivo_Eliminar)
                       Tipo.mostrar_dispositivos()

                    else:
                        
                        logging.info("Se cancelo la eliminacion")
                        
                      
                elif opcion_seleccionada == 4:
                         
                    Tipo.mostrar_dispositivos()
                    

                elif opcion_seleccionada == 5:
                    rango_menor=int(input("Elija el rango Minimo: "))
                    rango_mayor=int(input("Elija rango Maximo: "))
                    
                elif opcion_seleccionada==6:
                    break
                else:
                    logging.info("Opción no válida. Por favor, seleccione una opción válida.")
        #Fin del while
        
        except Exception as ex:
            logging.info(f"Error generado: {ex}")
