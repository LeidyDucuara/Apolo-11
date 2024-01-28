import os
from tests.conftest import app

def test_generacion_nombre(app):

    nombre_generado = app.archivo.nombre_archivo()

    assert nombre_generado.startswith("APL-")
    assert nombre_generado.endswith(".log")


