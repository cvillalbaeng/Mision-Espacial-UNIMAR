# Logica de los recursos
def verificar_estado(energia, oxigeno, combustible):
    if energia <= 0 or oxigeno <= 0 or combustible <= 0:
        return False
    else:
        return True


def calcular_puntaje(energia, oxigeno, combustible):
    puntaje = energia + oxigeno + combustible
    return puntaje
