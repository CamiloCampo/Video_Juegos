import os
import time
import random

def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)

def verificar_3_pares_consecutivos(tiradas_anteriores):
    return len(tiradas_anteriores) >= 6 and tiradas_anteriores[-6:] == [(x, x) for x in tiradas_anteriores[-6:][::2]]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_niveles():
    clear_screen()
    print("Seleccione el nivel de tablero a jugar:")
    print("1. Nivel básico (Tablero de 20 posiciones)")
    print("2. Nivel intermedio (Tablero de 30 posiciones)")
    print("3. Nivel avanzado (Tablero de 50 posiciones)")
    print("4. Nivel experto (Tablero de 100 posiciones)")

    nivel_elegido = input("Ingrese el número correspondiente al nivel deseado: ")
    while nivel_elegido not in ('1', '2', '3', '4'):
        print("Nivel no válido. Inténtelo de nuevo.")
        nivel_elegido = input("Ingrese el número correspondiente al nivel deseado: ")
        
    return int(nivel_elegido)

def jugar():
    clear_screen()
    print("Bienvenido a Carrera Numérica!")
    num_jugadores = int(input("Ingrese el número de jugadores (2-4): "))
    while num_jugadores < 2 or num_jugadores > 4:
        print("Número de jugadores no válido. Inténtelo de nuevo.")
        num_jugadores = int(input("Ingrese el número de jugadores (2-4): "))
    nivel_elegido = mostrar_menu_niveles()
    
    meta = 20 * nivel_elegido
    clear_screen()
    jugadores = [0] * num_jugadores
    tiradas_anteriores = []
    clear_screen()
    while True:
        for i in range(num_jugadores):
            input(f"*JUGADOR {i + 1}*. Presione Enter para lanzar los dados.")
            dado1, dado2 = lanzar_dados()
            clear_screen()
            print(f"*JUGADOR {i + 1}* obtuvo: {dado1}, {dado2}")

            suma_tirada = dado1 + dado2
            jugadores[i] += suma_tirada
            
            print(f"*JUGADOR {i + 1}* está ahora en la posición {jugadores[i]}")
            print("-------------------------------------------------------------------")
            
            tiradas_anteriores.append((dado1, dado2))

            if verificar_3_pares_consecutivos(tiradas_anteriores):
                print(f"¡*JUGADOR {i + 1}* ha obtenido 3 pares consecutivos y ha ganado!")
                return

            if jugadores[i] >= meta:
                print(f"¡*JUGADOR {i + 1}* ha ganado!")
                input("Presiona Enter para continuar...")
                return
def main_menu():
    while True:
        clear_screen()
        print(":::::::::::::::::")
        print("::: MAIN MENU :::")
        print(":::::::::::::::::")
        print("[1]. Play")
        print("[2]. Help")
        print("[3]. About us")
        print("[4]. Exit")
        
        opt = int(input(".::: Press any option: "))
        if opt == 1:
            jugar()
        elif opt == 2:
            print("Help menu...")
            input("Press Enter to return to the main menu...")
        elif opt == 3:
            print("About us...")
            input("Press Enter to return to the main menu...")
        elif opt == 4:
            print("Exiting game...")
            clear_screen()
            return
if __name__ == "__main__":
    main_menu()