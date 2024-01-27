from tests.conftest import app

def test_agreagar_dispositivos(app):
    dispositivo_prueba = "dispositivo_prueba"
    
    caso_1= app.tipo.agregar_dispositivo(dispositivo_prueba)
    if dispositivo_prueba in app.tipo.dispositivos:
        caso_1=True
    assert  caso_1==True
def test_eliminar_dispositivos(app):
    indice=0
    antes_de_eliminar=len(app.tipo.dispositivos)
    caso_2 = app.tipo.eliminar_dispositivo(indice)
    despues_de_eliminar=len(app.tipo.dispositivos)
    if antes_de_eliminar > despues_de_eliminar:
        caso_2=True
    assert caso_2==True
def test_eligir_dispositivo(app):
    dispositivo_elegido=app.tipo.elegir_dispositivo()
    if dispositivo_elegido in app.tipo.dispositivos:
        caso_3=True
    assert caso_3 == True
