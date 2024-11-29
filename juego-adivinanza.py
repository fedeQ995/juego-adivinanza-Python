#Juego de Adivinanzas

import random


numero_secreto = random.randint(1,100)
cantidad_intentos = 0
cantidad_max = 5
adivinado = False

print("bienvenido al juego de adivinar el numero secreto!")

while not adivinado:
    if not cantidad_intentos < cantidad_max:
        print("¡GAME OVER! No has podido adivinar el numero secreto")
        break

    entrada = input("Introduce un numero del 1 al 99: ") # TO DO: Convertir a numero 
    numero = int(entrada) #Con esto casteamos a entrada

    if numero == numero_secreto:
        print("¡Felicitaciones has adivinado el numero secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("El numero secreto es mayor al ingresado")
    else:
        print("El numero secreto es menor al ingresado")
    
    cantidad_intentos += 1 


