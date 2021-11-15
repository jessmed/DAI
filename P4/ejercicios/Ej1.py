#Adivina un número entre 1 y 100

import random

r1 = random.randint(0,100)
print(f"Random number between 0 and 100 is {r1}")

while True:
    entrada = int(input("Un numero: "))
    print(f"Has tecleado {entrada}")

    if entrada > r1:
        print("El número es menor")
    elif entrada < r1:
        print("El número es mayor")
    else:
        print("Has acertado")
        break