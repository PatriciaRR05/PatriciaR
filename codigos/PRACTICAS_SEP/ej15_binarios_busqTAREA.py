#como implementar la busqueda binaria(es un prototipo)
import random
import time
lista= []
def busqueda_binaria(lista,numero): #Prototipo que se nos dio
    izquierda,derecha = 0, len(lista) -1
    while izquierda <= derecha:
        medio= (izquierda + derecha) //2
        if lista [medio] == numero:
            return medio
        elif lista[medio] < numero:
            izquierda = medio + 1
        else:
            derecha= medio -1
    return -1
lista = [] #se crea una lista vacía 
for i in range(0,30): #se limita el rango y con un for para recorrer la lista
    numero_aleatorio= random.randint(0,30)#se genera los numeros
    lista.append(numero_aleatorio) #se adieren los numeros a la lista
lista.sort()  #se ordena la lista
print("La lista generada es: ",lista) # se muestra la lista con los numeros generados
numero= int(input("Ingrese el número que desea buscar: ")) #se pide al usuario ingresar el número a buscar 
resultado= busqueda_binaria(lista,numero) #la condicion de cual sera el resultado
if numero != -1:
    print(f"El número {numero} se encuentra en la posición {resultado}.") # se muestran los resultados
else:
    print(f"El número {numero} no se encuentra en la lista")

inicio= time.time()

fin=time.time()
print(f"Tiempor transcurrido de la generación de la lista \n {(fin-inicio)/1000} ms")