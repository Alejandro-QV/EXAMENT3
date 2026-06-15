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

def backtracking(x, y, vidas):

    if vidas <= 0:
        return False

    if (x, y) == fin:
        solucion[x][y] = 1
        return True

    visitado[x][y] = True
    solucion[x][y] = 1

    movimientos = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    ]

    for dx, dy in movimientos:

        nx = x + dx
        ny = y + dy

        if es_valido(nx, ny):

            nueva_vida = vidas

            if laberinto[nx][ny] == -1:
                nueva_vida -= 1

            elif laberinto[nx][ny] == -2:
                nueva_vida -= 2

            if backtracking(nx, ny, nueva_vida):
                return True

    solucion[x][y] = 0

    return False

resultado = backtracking(inicio[0], inicio[1], 3)

print("Resultado:", resultado)