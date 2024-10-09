import random
contador_error=0
num_secret= random.randint(1,101)
while True:
    num=int(input("Ingrese un número: ")) #Se pide al usuario que ingrese un número dentro del buble
    if num < num_secret:
        print ("Demasiado Bajo. Intente de nuevo")
        contador_error +=1 #El contador se coloca en cada if para que cuente los intentos
    elif num > num_secret:
        print ("Demasiado alto.Intente de nuevo")
        contador_error +=1
    else:
        print("--- ¡FELICIDADES! --- Usted realizo "+ str(contador_error) +" intentos")
        contador_error +=1
        break #Para que detenga el buble una vez el usuario adivina el número