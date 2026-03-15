def pedir_nombre():
    nombre = input("Comandante, ingrese su nombre: ")
    return nombre


def seleccionar_dificultad():
    print("Seleccione la dificultad de la misión:")
    print("1. Fácil (100% de todos los recursos)")
    print("2. Difícil (50% de todos los recursos)")

    # Iniciamos un bucle infinito para validar la entrada
    while True:
        opcion = input("Indique 1 o 2: ")

        if opcion == "1":
            return 100, 100, 100
        elif opcion == "2":
            return 50, 50, 50
        else:
            # Si escribe cualquier otra cosa, mostramos error y el bucle se repite
            print("Error: Opción no válida. Por favor, ingrese exactamente 1 o 2.\n")
