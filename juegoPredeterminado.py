
import interfaz_usuario
import copy
import usuario

nivelesPredeterminados = []
niveles_permitidos = (1, 2, 3, 4, 5)


def siguiente_nivel():
    proximo_nivel = usuario.nivel_actual+1
    return proximo_nivel in niveles_permitidos

def nivelGanado(tablero):

    for fila in tablero:
        for elemento in fila:
            if elemento != ".":
                return False
    return True

def terminar_juego():
    print("Has terminado todos los niveles. Tu puntaje fue: ")

    puntajeTotal = 0

    for indice,elemento in enumerate(usuario.puntaje_acumulado):
        clave = int(indice + 1)
        puntajeTotal += usuario.puntaje_acumulado[clave]
        print("El puntaje en el nivel " + str(indice+1) + " fue de: " + str(puntajeTotal))

    print("El puntaje total obtenido es de: " + str(puntajeTotal))

    usuario.nivel_actual = 1
    usuario.reiniciarPuntajesAcumulados()

def hayTurnosDisponibles(intentos):

    if intentos > 0:
        return True
    return False

def jugar():
    print("Usted ha elegido predeterminado")
    cargarNivelesPredeterminados()

    tablero = get_tablero_para(usuario.nivel_actual)
    intentos = 15

    while not nivelGanado(tablero) and hayTurnosDisponibles(intentos):

        print("")
        print("Turnos disponibles: ", intentos)
        interfaz_usuario.mostrar_tablero(tablero)
        print("")

        resultado = validar_coordenada()
        while not resultado['coordenadaValida']:
            resultado = validar_coordenada()

        if resultado["reiniciarNivel"]:
            intentos = 15
            tablero = get_tablero_para(usuario.nivel_actual)
            usuario.puntaje_acumulado[usuario.nivel_actual] = -50
            print("Este es el nivel y el puntaje acumulado: ", usuario.puntaje_acumulado)

        else:
            fila = resultado["valor"][0]
            columna = resultado["valor"][1]

            print(tablero[fila][columna])
            intentos -= 1
            cambiar_luces(tablero, fila, columna)

    interfaz_usuario.mostrar_tablero(tablero)
    juegoGanado = nivelGanado(tablero)

    if juegoGanado:
        print("")
        print("GANASTEEE")
        print("")
        print("Pasaste al siguiente nivel!!! Ganaste 500 puntos!!!")
        usuario.puntaje_acumulado[usuario.nivel_actual] += 500

        if siguiente_nivel():
            usuario.nivel_actual += 1
            jugar()
        else:
           terminar_juego()
    else:
        print("")
        print("PERDISTEEE")
        print("")
        print("-300 puntos acumulados")
        print("Probá nuevamente en menos de 15 intentos")
        print("")
        print("")
        usuario.puntaje_acumulado[usuario.nivel_actual] += -300
        jugar()

    interfaz_usuario.mostrarMenu()


def posicion_jugada(fila, columna, tablero):
    filasPermitidas = [0, 1, 2, 3, 4]
    columnasPermitidas = ["A", "B", "C", "D", "E"]


    cambiar_luces(tablero, fila, columna)


def cambiar_luces(tablero, fila, columna):
    if tablero[fila][columna] == ".":
        tablero[fila][columna] = "o"
    else:
        tablero[fila][columna] = "."

    if fila in (1, 2, 3, 4):
        if tablero[fila-1][columna] == ".":
            tablero[fila-1][columna] = "o"
        else:
            tablero[fila-1][columna] = "."

    if fila in (0, 1, 2, 3):
        if tablero[fila+1][columna] == ".":
            tablero[fila+1][columna] = "o"
        else:
            tablero[fila+1][columna] = "."

    if columna in (1, 2, 3, 4):
        if tablero[fila][columna-1] == ".":
            tablero[fila][columna-1] = "o"
        else:
            tablero[fila][columna-1] = "."

    if columna in (0, 1, 2, 3):
        if tablero[fila][columna+1] == ".":
            tablero[fila][columna+1] = "o"
        else:
            tablero[fila][columna+1] = "."

def validar_coordenada():
    propuesta = input("Elija una coordenada(letra, número) o ingrese * para reiniciar el nivel(pierde 50 puntos cada vez): ")
    propuesta = propuesta.upper()
    coordenadas = obtenerCoordenadas()
    if propuesta in coordenadas:
        return {"coordenadaValida": True, "valor": coordenadas[propuesta],"reiniciarNivel": False}

    if propuesta == "*":
        return {"coordenadaValida": True, "reiniciarNivel": True}

    return {"coordenadaValida": False, "valor": ""}

def obtenerCoordenadas():
    return {"A1": (0, 0), "B1": (0, 1), "C1": (0, 2), "D1": (0, 3), "E1": (0, 4), "A2": (1, 0), "B2": (1, 1), "C2": (1, 2),
            "D2": (1, 3), "E2": (1, 4), "A3": (2, 0), "B3": (2, 1), "C3": (2, 2), "D3": (2, 3), "E3": (2, 4), "A4": (3, 0),
            "B4": (3, 1), "C4": (3, 2), "D4": (3, 3), "E4": (3, 4), "A5": (4, 0), "B5": (4, 1), "C5": (4, 2), "D5": (4, 3),
            "E5": (4, 4)}

def cargarNivelesPredeterminados():
    nivelesPredeterminados1 = [["o", "o", ".", "o", "o"], ["o", ".", "o", ".", "o"], [".", "o", "o", "o", "."], ["o", ".", "o", ".", "o"], ["o", "o", ".", "o", "o"]]
    nivelesPredeterminados2 = [[".", "o", ".", "o", "."], ["o", "o", ".", "o", "o"], [".", "o", ".", "o", "."], ["o", ".", "o", ".", "o"], ["o", ".", "o", ".", "o"]]
    nivelesPredeterminados3 = [["o", ".", ".", ".", "o"], ["o", "o", ".", "o", "o"], [".", ".", "o", ".", "."], ["o", ".", "o", ".", "."], ["o", ".", "o", "o", "."]]
    nivelesPredeterminados4 = [["o", "o", ".", "o", "o"], [".", ".", ".", ".", "."], ["o", "o", ".", "o", "o"], [".", ".", ".", ".", "o"], ["o", "o", ".", ".", "."]]
    nivelesPredeterminados5 = [[".", ".", ".", "o", "o"], [".", ".", ".", "o", "o"], [".", ".", ".", ".", "."], ["o", "o", ".", ".", "."], ["o", "o", ".", ".", "."]]

    nivelesPredeterminados.append(nivelesPredeterminados1)
    nivelesPredeterminados.append(nivelesPredeterminados2)
    nivelesPredeterminados.append(nivelesPredeterminados3)
    nivelesPredeterminados.append(nivelesPredeterminados4)
    nivelesPredeterminados.append(nivelesPredeterminados5)

"""
PRE:    Se espera que los niveles predeterminados ya hayan sido cargados
        Se espera que nroNivel sea un entero
        Se validara que nroNivel pasado sea 1,2,3,4 o 5
POST:   Se devuelve una copia de la matriz del nivel pasado por parametro.
        Sino se cumple la precondicion, se devuelve una lista vacia
"""
def get_tablero_para(nroNivel):
    if len(nivelesPredeterminados) == 0:
        return []

    if type(nroNivel) != int:
        return []

    if nroNivel not in niveles_permitidos:
        return []

    copiaDelNivel = copy.deepcopy(nivelesPredeterminados[nroNivel-1])
    return copiaDelNivel






