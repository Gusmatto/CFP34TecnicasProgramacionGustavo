
import interfaz_usuario
import copy

nivelesPredeterminados = []

def jugar():
    print("Usted ha elegido predeterminado")
    cargarNivelesPredeterminados()
    #TODO preguntar o conseguir o saber en qué nivel vamos a jugar ?
    tablero = get_tablero_para(1)
    interfaz_usuario.mostrar_tablero(tablero)
    print("")
    propuesta = input("Elija una coordenada(letra, número): ")
    propuesta = propuesta.upper()

    #TODO validar que la coordenada ingresada por el usuario sea valida y en caso negativo volver a pedirsela

def validar_coordenada(rango):
    while propuesta in coordenadas:
        return True
    else:
        print(input("Las coordenadas ingresadas no son validas. Ingrese coordenadas validas: "))


def coordenadas(letra, numero):

    coordenadas = [["A1": nivelesPredeterminados1 [0:0], "B1": nivelesPredeterminados1 [0:1], "C1": nivelesPredeterminados1 [0:2], "D1": 03, "E1": 04], ["A2": 10, "B2": 11, "C2": 12, "D2": 13, "E2": 14],
    ["A3": 20, "B3": 21, "C3": 22, "D3": 23, "E3": 24], ["A4": 30, "B4": 31, "C4": 32, "D4": 33, "E4": 34],
    ["A5": 40, "B5": 41, "C5": 42, "D5": 43, "E5": 44]],

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

    niveles_permitidos = (1,2,3,4,5)

    if nroNivel not in niveles_permitidos:
        return []

    copiaDelNivel = copy.deepcopy(nivelesPredeterminados[nroNivel-1])
    return copiaDelNivel






