# Importamos los módulos creados por el equipo
import interfaz
import configuracion
import eventos
import recursos


# Funciones
def reiniciar_juego():
    respuesta = input("¿Deseas intentar otra misión? (s/n): ").lower()
    if respuesta == "s":
        return True
    else:
        return False


def main():
    jugando = True

    while jugando:
        interfaz.mostrar_intro()
        capitan = configuracion.pedir_nombre()
        print(f"\nBienvenido al mando, Capitán {capitan}.")

        # 1. Obtenemos recursos iniciales
        energia, oxigeno, combustible = configuracion.seleccionar_dificultad()

        # 2. Mostramos estado y lanzamos Evento 1
        interfaz.mostrar_estado(energia, oxigeno, combustible)
        energia, oxigeno, combustible = eventos.evento_asteroides(
            energia, oxigeno, combustible
        )

        # Verificamos si sobrevivió al Evento 1
        if recursos.verificar_estado(energia, oxigeno, combustible) == False:
            interfaz.mostrar_derrota()
            jugando = reiniciar_juego()
            continue

        # 3. Mostramos estado y lanzamos Evento 2
        interfaz.mostrar_estado(energia, oxigeno, combustible)
        energia, oxigeno, combustible = eventos.evento_falla(
            energia, oxigeno, combustible
        )

        # Verificamos si sobrevivió al Evento 2
        if recursos.verificar_estado(energia, oxigeno, combustible) == False:
            interfaz.mostrar_derrota()
            jugando = reiniciar_juego()
            continue

        # 4. Si llega hasta aquí, ganó el juego
        interfaz.mostrar_victoria()
        puntaje = recursos.calcular_puntaje(energia, oxigeno, combustible)
        print(f"Puntaje de eficiencia: {puntaje} puntos.\n")

        # Preguntamos si quiere repetir el bucle while
        jugando = reiniciar_juego()

    print("Cerrando simulador de vuelo...")


# Esta línea asegura que el programa arranque automáticamente por la función main()
if __name__ == "__main__":
    main()
