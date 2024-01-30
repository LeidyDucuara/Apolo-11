# pragma: no cover
# flake8: noqa: F401, F811

import os
import shutil
from tests.conftest import app


def test_generacion_nombre(app):
    nombre_generado = app.Archivo.nombre_archivo()
    assert nombre_generado.startswith("APL-")
    assert nombre_generado.endswith(".log")


def generar_nombre_archivo():
    return "nombre_prueba.txt"


def test_creacion_archivo():
    directorio_prueba = "Devices_test"
    nombre_archivo = generar_nombre_archivo()

    ruta_directorio_prueba = os.path.join("tests", "pruebas", directorio_prueba)
    os.makedirs(ruta_directorio_prueba, exist_ok=True)

    ruta_archivo = os.path.join(ruta_directorio_prueba, nombre_archivo)
    with open(ruta_archivo, "w"):
        pass

    assert os.path.exists(ruta_archivo)
    shutil.rmtree(ruta_directorio_prueba)
