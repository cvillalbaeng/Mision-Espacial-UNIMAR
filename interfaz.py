def mostrar_intro():
    print("=======================================")
    print("      MISION ESPACIAL - UNIMAR         ")
    print("=======================================")
    print("Objetivo: Llegar al planeta Kepler")
    print("Sobrevive tomando las mejores decisiones.\n")


def mostrar_estado(energia, oxigeno, combustible):
    print("\n--- REPORTE DE SISTEMAS ---")
    print(f"Energía: {energia}%")
    print(f"Oxígeno: {oxigeno}%")
    print(f"Combustible: {combustible}%")
    print("---------------------------\n")


def mostrar_victoria():
    print("\n=======================================")
    print(" ¡MISION EXITOSA! HAS LLEGADO A KEPLER ")
    print("=======================================\n")


def mostrar_derrota():
    print("\n=======================================")
    print(" MISIÓN FALLIDA. LA NAVE ESTÁ PERDIDA. ")
    print("=======================================\n")
