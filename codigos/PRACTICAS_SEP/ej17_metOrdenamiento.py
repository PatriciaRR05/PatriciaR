def ordenamiento_burbuja(lista):
    n = len(lista)
    #recorre toda la lista
    for i in range(n):
        # Ultimos i elementos ya estan en cadenma
        for j in range(0,n - i - 1):
            #Intercambia si el elemento actual es mayor que el siguiente
            if lista[j] > lista[j + 1]:
                lista[j], lista[j] + 1 = lista[j + 1], lista[j]
    return lista

    #ejemplo de uso
    lista=[5,3,8,4,2,1]
    print("lista original: ",lista)
    lista_ordenada= ordenamiento_burbuja(lista)
    print("lista ordenada: ", lista_ordenada)