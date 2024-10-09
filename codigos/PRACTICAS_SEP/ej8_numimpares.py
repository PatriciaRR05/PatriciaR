#La lista imprime desde el 0, ya que los indices se enumeran desde el 0
lista=[ 1,2,3,4,5]
print(lista)
print(lista[2]) #indico el lugar que quiero que imprima
#MATRICES
matriz=[ 
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matriz[1][2])#Llamamos a la mtriz en el indice(caja) 1 (fila 2)

listastring=["a","b","c","d"]
print(listastring[3]) #type me devuelve tipo de dato

listastring=["a",2.2,"c",10]
print(type(listastring)[1])

listastring= ["a",2.2,"c",10, ["z","x","9"]]#el corchete que esta destro del corchete es un solo indice (caja)
print(listastring [4] [2])
print(type(listastring [4] [2]))