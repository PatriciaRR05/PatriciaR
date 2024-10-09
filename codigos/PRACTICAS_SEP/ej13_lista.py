import random
lista=[]
for i in range(100):
    x= random.randint(0,100)
    lista.append(x)
valor= int(input("Ingrese el valor que desea encontrar en la lista: "))
def busqueda_lineal (lista,valor):
    for i in range(len(lista)):
        if lista [i] == valor:
            return i
        return -1
print(lista)
print(len(lista))
print (type(lista))