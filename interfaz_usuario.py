def mostrarMenu():
    print("")
    print("¡Bienvenido a Lights Out!")
    print("")
    print("Para jugar en modo aleatorio, ingrese 'A'")
    print("Para jugar en modo predeterminado, ingrese 'P'")
    print("Para salir del juego, ingrese 'S'")

    modoDeJuego = input("Elija el modo: ")
    modoDeJuego = modoDeJuego.upper()
    modoDeJuegoValido = validarModoDeJuego(modoDeJuego)
    if modoDeJuegoValido:
        print("Bienvenido")
    elif modoDeJuego == "S":
        print("¡Ha salido del juego!")
    else:
        print("")
        print("ERROR ! La opcion: " + modoDeJuego + " es invalida")
        mostrarMenu()



def validarModoDeJuego(modo):
    if modo == "A":
        return True
    elif modo == "P":
        return True
    else:
        return False