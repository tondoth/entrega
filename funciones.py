import random

def crear_tablero():
    return [['0' for _ in range(10)] for _ in range(10)]

def verificar_espacio(tablero, fila_inicio, col_inicio, tamaño, orientacion):
    for i in range(-1, tamaño + 1):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if orientacion == 'horizontal':
                    col = col_inicio + i
                    fila = fila_inicio + dy
                else:
                    col = col_inicio + dx
                    fila = fila_inicio + i

                if not (0 <= fila < 10 and 0 <= col < 10):
                    continue
                if tablero[fila][col] != '0':
                    return False
    return True

def colocar_barco(tablero, tamaño):
    colocado = False
    while not colocado:
        orientacion = random.choice(['horizontal', 'vertical'])
        fila_inicio = random.randint(0, 9)
        col_inicio = random.randint(0, 9)

        if orientacion == 'horizontal' and col_inicio + tamaño <= 10:
            if verificar_espacio(tablero, fila_inicio, col_inicio, tamaño, orientacion):
                for i in range(tamaño):
                    tablero[fila_inicio][col_inicio + i] = '1'
                colocado = True
        elif orientacion == 'vertical' and fila_inicio + tamaño <= 10:
            if verificar_espacio(tablero, fila_inicio, col_inicio, tamaño, orientacion):
                for i in range(tamaño):
                    tablero[fila_inicio + i][col_inicio] = '1'
                colocado = True

def atacar(tablero, fila, col, intentos):
    if intentos[fila][col] == '0':
        if tablero[fila][col] == '1':
            intentos[fila][col] = 'T'
        else:
            intentos[fila][col] = 'A'
        return intentos[fila][col] == 'T'
    return False

def todos_hundidos(intentos, tablero):
    for fila in range(10):
        for col in range(10):
            if tablero[fila][col] == '1' and intentos[fila][col] != 'T':
                return False
    return True
