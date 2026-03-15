def evento_asteroides(energia, oxigeno, combustible):
    print("¡ALERTA! Un campo de asteroides bloquea la ruta.")
    print("1. Activar escudos (Seguro, gasta 20"%" de Energía)")
    print("2. Maniobra evasiva (Riesgoso, gasta 20"%" Combustible y 10"%" Oxígeno)")
    decision = input("Decisión (1 o 2): ")

    if decision == "1":
        energia = energia - 20
        print("> Escudos activados. Pasamos sin daños.")
    else:
        combustible = combustible - 20
        oxigeno = oxigeno - 10
        print("> Esquivamos, pero el esfuerzo dañó el soporte vital.")
    
    return energia, oxigeno, combustible

def evento_falla(energia, oxigeno, combustible):
    print("¡ALERTA! Falla en el propulsor principal.")
    print("1. Usar baterías auxiliares (Gasta 30"%" Energía)")
    print("2. Inyectar reservas químicas (Gasta 30"%" Combustible)")
    decision = input("Decisión (1 o 2): ")

    if decision == "1":
        energia = energia - 30
        print("> Energía redirigida al propulsor. Todo estable.")
    else:
        combustible = combustible - 30
        print("> Inyección exitosa. Seguimos en ruta.")
    
    return energia, oxigeno, combustible