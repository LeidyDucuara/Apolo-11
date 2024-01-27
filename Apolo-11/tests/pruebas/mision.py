from tests.conftest import app
def test_mision(app):

    caso_1= app.mision.generar_nombre_aleatorio()
    lista_misiones = ["OrbitOne", "ColonyMoon", "GalaxyTwo", "VacMars", "Unknown"]
    if caso_1 in lista_misiones:
        caso_1=True
    assert  caso_1 == True

