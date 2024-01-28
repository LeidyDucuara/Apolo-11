# flake8: noqa: F401, F811
"""para definir configuración transversal que pueden ser usados 
en las diferentes pruebas unitarias.

todas las pruebas unitarias normalmente se hacen con funciones y asserts
"""
import pytest
# Dentro de conftest.py
from apolo_11.Clases.dispositivo import Dispositivo, Tipo
from apolo_11.Clases.mision import Mision
from apolo_11.Clases.archivo import Archivo


@pytest.fixture(scope="session")
def app(request):

    # truco para crear atributos dinamicos
    class App:
        pass
    app = App()
    app.mision = Mision
    app.dispositivo= Dispositivo
    app.tipo = Tipo
    app.archivo = Archivo
    return app