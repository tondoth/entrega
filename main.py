import os
import funciones
import time
import random

def mostrar_tablero(tablero):
    print("   " + " ".join(str(i) for i in range(10)))
    for index, fila in enumerate(tablero):
        print(f"{index}  " + " ".join(fila))
    print()

def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if 0 <= value < 10:
                return value
            print("Por favor, introduce un número entre 0 y 9.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número válido.")

def mostrar_bienvenida():
    print("¡Bienvenido a Batalla Naval!")
    print("Instrucciones:")
    print("1. Durante tu turno, elige una fila y una columna para atacar.")
    print("2. Espera a que la computadora realice su turno.")
    print("3. Gana hundiendo todos los barcos de tu oponente.")
    print()

def juego():
    os.system('cls' if os.name == 'nt' else 'clear')
    mostrar_bienvenida()

    tablero_jugador = funciones.crear_tablero()
    funciones.colocar_barco(tablero_jugador, 1)
    funciones.colocar_barco(tablero_jugador, 1)
    funciones.colocar_barco(tablero_jugador, 1)
    funciones.colocar_barco(tablero_jugador, 1)
    funciones.colocar_barco(tablero_jugador, 2)
    funciones.colocar_barco(tablero_jugador, 2)
    funciones.colocar_barco(tablero_jugador, 2)
    funciones.colocar_barco(tablero_jugador, 3)
    funciones.colocar_barco(tablero_jugador, 3)
    funciones.colocar_barco(tablero_jugador, 4)

    tablero_ordenador = funciones.crear_tablero()
    funciones.colocar_barco(tablero_ordenador, 1)
    funciones.colocar_barco(tablero_ordenador, 1)
    funciones.colocar_barco(tablero_ordenador, 1)
    funciones.colocar_barco(tablero_ordenador, 1)
    funciones.colocar_barco(tablero_ordenador, 2)
    funciones.colocar_barco(tablero_ordenador, 2)
    funciones.colocar_barco(tablero_ordenador, 2)
    funciones.colocar_barco(tablero_ordenador, 3)
    funciones.colocar_barco(tablero_ordenador, 3)
    funciones.colocar_barco(tablero_ordenador, 4)

    turno = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Tablero de Ataques:")
        mostrar_tablero(tablero_ordenador)
        print("Tablero de Defensa:")
        mostrar_tablero(tablero_jugador)

        if turno % 2 == 0:
            print("¡Es tu turno!")
            fila = get_valid_input("Elige una fila para atacar (0-9): ")
            col = get_valid_input("Elige una columna para atacar (0-9): ")
            if funciones.atacar(tablero_ordenador, fila, col, tablero_ordenador):
                print("¡Impacto! Has golpeado un barco enemigo.")
            else:
                print("¡Agua! No has golpeado ningún barco enemigo.")
            time.sleep(1)
        else:
            print("Turno de la computadora...")
            fila, col = random.randint(0, 9), random.randint(0, 9)
            if funciones.atacar(tablero_jugador, fila, col, tablero_jugador):
                print(f"La computadora ataca a la fila {fila} y columna {col} y ¡acierta!")
            else:
                print(f"La computadora ataca a la fila {fila} y columna {col} y falla.")
            time.sleep(1)

        if funciones.todos_hundidos(tablero_ordenador, tablero_ordenador):
            print("¡Felicidades! ¡Has ganado la batalla naval!")
            break
        if funciones.todos_hundidos(tablero_jugador, tablero_jugador):
            print("¡Derrota! La computadora ha ganado la batalla naval.")
            break

        turno += 1

if __name__ == "__main__":
    juego()
