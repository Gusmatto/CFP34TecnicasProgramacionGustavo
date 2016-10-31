pantalla = []
for x in range(0, 5):
    pantalla.append(["0"] * 5)

def mostrar_cuadro(pantalla):
    for fila in pantalla:
        print(" ".join(fila))

mostrar_cuadro(pantalla)