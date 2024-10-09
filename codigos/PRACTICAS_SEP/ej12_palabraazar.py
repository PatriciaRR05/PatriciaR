import random
intentos = 5 #contador de intentos
lista = ["higo", "pera", "kiwi", "lima"] #palabras para adivinar
palabra_azar = random.choice(lista) #seleccionar lista aleatoria
progreso = ["_"] * len(palabra_azar)  # Progreso de la palabra con guiones bajos
letras_intentadas = [] #lista para almacenar las letras ya intentadas 

while intentos > 0:
    print("Progreso: "+ str (progreso)) 
    print("Intentos restantes: " + str(intentos))
    print("Letras intentadas: " + str(letras_intentadas))

    pedir_letra = input("Ingrese una letra: ").lower()

    if pedir_letra in letras_intentadas: #verifica si la letra ya ha sido utilizada
        print("Ya intentaste esa letra. Intenta con otra.")
        continue

    letras_intentadas.append(pedir_letra) #añade la letra a la lista de letras intentadas

    if pedir_letra in palabra_azar: # verifica si la letra esta en la palabra secreta
        for i in range(len(palabra_azar)): #recorre la palabra para ver las posiciones donde esta la letra
            if palabra_azar[i] == pedir_letra:
                progreso[i] = pedir_letra #actualiza el progreso del jugador
        print("¡La letra está en la palabra!")
    else:
        intentos -= 1 #reduce el numero de intentos
        print("La letra no está en la palabra")

    if "_" not in progreso:
        print("¡Felicidades! Adivinaste la palabra: " + str (progreso))
        break

if intentos == 0:
    print("Perdiste. La palabra era: " + str (palabra_azar))