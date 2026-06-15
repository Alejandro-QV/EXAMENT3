laberinto = [
    ['F', 1, 1, 1, 0, 1, 1, 1, 1],
    [-2, 0, 0, -1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, -1, 0, 0, 0, -1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0],
    [-1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, -1, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 1, 0],
    ['I', 1, -1, 1, 1, 1, 0, 1, 1]
]

filas = len(laberinto)
columnas = len(laberinto[0])

inicio = None
fin = None

for i in range(filas):
    for j in range(columnas):
        if laberinto[i][j] == 'I':
            inicio = (i, j)

        if laberinto[i][j] == 'F':
            fin = (i, j)

print("Inicio:", inicio)
print("Fin:", fin)

for fila in laberinto:
    print(fila)