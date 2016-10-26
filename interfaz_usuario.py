def mostrarMenu():
    print("")
    print("¡Bienvenido a Lights Out!")
    print("")
    print("Para jugar en modo aleatorio, ingrese 'A'")
    print("Para jugar en modo predeterminado, ingrese 'P'")
    print("Para salir del juego, ingrese 'S'")

    modoDeJuego = input("Elija el modo: ")
    modoDeJuegoValido = validarModoDeJuego(modoDeJuego)
    print(modoDeJuegoValido)


def validarModoDeJuego(modo):
    if modo == "A":
        return True
    elif modo == "P":
        return True
    elif modo == "S":
        return True
    else:
        return False