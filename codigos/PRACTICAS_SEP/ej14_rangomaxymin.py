import random
lista=[]
rango= 50
Vmin=5      #En el caso en el que se asignen los valores
Vmax=50
def geneList(rango,Vmin,Vmax,lista):
    for i in range(rango):
        y= random.randint(Vmin,Vmax)
        lista.append(y)
    return lista
geneList(50,5,50, lista) #En el caso donde no se asignen los valores
print(lista) #El rango indica cuantos numeros habra en la lista
print(len(lista))