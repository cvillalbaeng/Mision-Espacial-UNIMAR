# Configuración
def pedir_nombre():
    nombre = input("Comandante, ingrese su nombre: ")
    return nombre


def seleccionar_dificultad():
    print("Seleccione la dificultad de la misión:")
    print("1. Fácil (100% de todos los recursos)")
    print("2. Difícil (50% de todos los recursos)")

    opcion = input("Indique 1 o 2: ")

    if opcion == "1":
        return 100, 100, 100
    else:
        return 50, 50, 50
