# flake8: noqa: F401, F811
from tests.conftest import app
def test_agregar_dispositivos(app):
    dispositivo_prueba = "dispositivo_prueba"
    app.Tipo.agregar_dispositivo(dispositivo_prueba)
    assert dispositivo_prueba in app.Tipo.dispositivos

def test_eliminar_dispositivos(app):
    indice = 0
    antes_de_eliminar = len(app.Tipo.dispositivos)
    app.Tipo.eliminar_dispositivo(indice)
    despues_de_eliminar = len(app.tipo.dispositivos)
    assert antes_de_eliminar > despues_de_eliminar

def test_eligir_dispositivo(app):
    dispositivo_elegido = app.Tipo.elegir_dispositivo()
    assert dispositivo_elegido in app.tipo.dispositivos
