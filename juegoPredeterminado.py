
import interfaz_usuario
import copy

nivelesPredeterminados = []

def jugar():
    print("Usted ha elegido predeterminado")
    cargarNivelesPredeterminados()
    #TODO preguntar o conseguir o saber en qué nivel vamos a jugar ?
    tablero = get_tablero_para(1)
    interfaz_usuario.mostrar_tablero(tablero)
    #TODO Se le debe pedir al usuario que ingrese la coordenada que quiere elegir



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






