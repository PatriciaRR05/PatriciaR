import random

def genlista(t,vmin,vamx, lista):
    for i in range(t):
        ale=random.randint(vmin,vamx)
        lista.append(ale)
    return lista

def encNum(lista, num):
    for i in range(len(lista)):
        if(num==lista[i]):
            print(f"Número encontrado en el índice{i}: ")
            return 1
        else:
            return -1
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