
import interfaz_usuario
import copy

nivelesPredeterminados = []

def nivelGanado(tablero):

    for fila in tablero:
        for elemento in fila:
            if elemento != ".":
                return False
    return True


def hayTurnosDisponibles(intentos):

    if intentos > 0:
        return True
    return False

def jugar():
    print("Usted ha elegido predeterminado")
    cargarNivelesPredeterminados()

    tablero = get_tablero_para(1)
    intentos = 15

    while not nivelGanado(tablero) and hayTurnosDisponibles(intentos):

        print("")
        print("Turnos disponibles: ", intentos)
        interfaz_usuario.mostrar_tablero(tablero)
        print("")

        resultado = validar_coordenada()
        while not resultado['coordenadaValida']:
            resultado = validar_coordenada()

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
        print("Pasaste al siguiente nivel!!!")

        """tablero = get_tablero_para(2)
        print(tablero)"""

    #TODO Pasar al siguiente nivel y mostrarlo

    else:
        print("")
        print("PERDISTEEE"),
        print("")

    interfaz_usuario.mostrarMenu()


    #TODO Poder reiniciar el juego en cualquier momento y volver al primer menú

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
    propuesta = input("Elija una coordenada(letra, número): ")
    propuesta = propuesta.upper()
    coordenadas = obtenerCoordenadas()
    if propuesta in coordenadas:
        return {"coordenadaValida": True, "valor": coordenadas[propuesta]}

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

    niveles_permitidos = (1, 2, 3, 4, 5)

    if nroNivel not in niveles_permitidos:
        return []

    copiaDelNivel = copy.deepcopy(nivelesPredeterminados[nroNivel-1])
    return copiaDelNivel






