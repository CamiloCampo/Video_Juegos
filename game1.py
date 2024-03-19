'''
    Script description:
    Crea un juego que genere a través de una
    función que genere el lanzamiento
    de dos dados, si los dos valores son
    iguales visualice un mensaje de ganador,
    de lo contrario, un mensaje de
    sigue intentando.
'''
from random import randint
import os

def dices():
    d1 = randint(1,6)
    d2 = randint(1,6)
    return d1, d2

os.system('clear')
d = dices()
print("Dice 1: ", d[0])
print(f"Dice 2: {d[1]}")

if d[0] == d [1]:
    print("You win")
else:
    print("Try again")




