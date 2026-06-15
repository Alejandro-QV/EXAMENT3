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

solucion = [[0 for _ in range(columnas)] for _ in range(filas)]

visitado = [[False for _ in range(columnas)] for _ in range(filas)]

def es_valido(x, y):
    return (
        0 <= x < filas and
        0 <= y < columnas and
        laberinto[x][y] != 0 and
        not visitado[x][y]
    )

print("Movimiento válido:", es_valido(8, 0))
print("Movimiento válido:", es_valido(0, 4))