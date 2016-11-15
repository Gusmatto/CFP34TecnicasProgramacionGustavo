
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
    coordeana = input("Elija una coordenada(letra, número): ")
    coordenada = coordenada.upper()
    print(coordeana)
    #TODO validar que la coordenada ingresada por el usuario sea valida y en caso negativo volver a pedirsela

def validar_coordenada(rango):
    if rango == "A1", "B1", "C1", "D1", "E1", "A2", "B2", "C2", "D2", "E2", "A3", "B3", "C3", "D3", "E3", "A4", "B4", "C4", "D4", "E4", "A5", "B5", "C5", "D5", "E5":
        return True
    else:
        return False
        print("Las coordenadas ingresadas no son validas. Ingrese coordenadas validas: ")


"""
def coordenadas(letra, numero):

    coordenadas = [[A1: 00, B1: 01, C1: 02, D1: 03, E1: 04], [A2: 10]]
   """
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






