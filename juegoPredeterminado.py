
import interfaz_usuario

nivelesPredeterminados = []

def jugar():
    print("Usted ha elegido predeterminado")
    #inicializar los niveles predeterminados!
    cargarNivelesPredeterminados()
    print(nivelesPredeterminados)

def cargarNivelesPredeterminados():

    nivelesPredeterminados1 = [["o", "o", ".", "o", "o"], [".", "o", ".", "o", "."], ["o", ".", ".", ".", "o"], ["o", "o", ".", "o", "o"], [".", ".", ".", "o", "o"]]
    nivelesPredeterminados2 = [[".", "o", ".", "o", "."], ["o", "o", ".", "o", "o"], [".", "o", ".", "o", "."], ["o", ".", "o", ".", "o"], ["o", ".", "o", ".", "o"]]
    nivelesPredeterminados3 = [["o", ".", ".", ".", "o"], ["o", "o", ".", "o", "o"], [".", ".", "o", ".", "."], ["o", ".", "o", ".", "."], ["o", ".", "o", "o", "."]]
    nivelesPredeterminados4 = [["o", "o", ".", "o", "o"], [".", ".", ".", ".", "."], ["o", "o", ".", "o", "o"], [".", ".", ".", ".", "o"], ["o", "o", ".", ".", "."]]
    nivelesPredeterminados5 = [[".", ".", ".", "o", "o"], [".", ".", ".", "o", "o"], [".", ".", ".", ".", "."], ["o", "o", ".", ".", "."], ["o", "o", ".", ".", "."]]

    nivelesPredeterminados.append(nivelesPredeterminados1)
    nivelesPredeterminados.append(nivelesPredeterminados2)
    nivelesPredeterminados.append(nivelesPredeterminados3)
    nivelesPredeterminados.append(nivelesPredeterminados4)
    nivelesPredeterminados.append(nivelesPredeterminados5)

def mostrar_tablero_para(nroNivel):
    print(nroNivel)
    #TODO realizar la funcion







