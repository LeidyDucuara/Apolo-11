from tests.conftest import app

def test_archivo_nombre(app):
    nombre = tipo.archivo.nombre_archivo('OrbitOne')
    if '-ORBONE' in nombre:
        caso_1=True
    assert  caso_1 == True

