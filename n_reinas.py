def solucion(matriz, N):
    for i in range(N):
        for j in range(N):
            print(matriz[i][j], end=" ")
        print()

def valido(matriz, fila, columna, N):
    for i in range(columna): #verificar filas
        if matriz[fila][i] == 1:
            return False

    for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)): #verificar diagonal superior
        if matriz[i][j] == 1:
            return False

    for i, j in zip(range(fila, N, 1), range(columna, -1, -1)): #verificar diagonal inferior
        if matriz[i][j] == 1:
            return False

    return True

def backtraking_Nreinas(matriz, columna, N):
    if columna >= N: #solucion completo
        return True

    solucion(matriz, N)
    print(" ")

    for i in range(N):

        print("Columna")
        print(columna)
        print("Fila")
        print(i)
        print(" ")

        if valido(matriz, i, columna, N) == True:

            print("Fila")
            print(i)
            print("Entro a Valido")
            print(" ")

            matriz[i][columna] = 1
            resultado = backtraking_Nreinas(matriz, columna + 1, N)
            if resultado != False:
                return True
            matriz[i][columna] = 0

    return False

def n_reinas(N):

    matriz = [[0] * N for _ in range(N)]

    resultadoT = backtraking_Nreinas(matriz, 0, N)

    if resultadoT == True:
        solucion(matriz, N)
        return matriz
    else:
        print("La solución no existe")
        return False

