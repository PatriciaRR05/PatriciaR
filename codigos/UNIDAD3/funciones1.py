import random
import time

def ingresar_lista():
    lista = []
    print("Ingresa números para la lista ,escribe 'fin' para terminar:")
    while True:
        entrada = input("Número: ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = int(entrada)
            if numero in lista:
                print("El número ya está en la lista. Ingresa otro número.")
            else:
                lista.append(numero)
        except ValueError:
            print("Ingresa un número válido.")
    print(lista)
    return lista

def generar_lista_aleatoria(n):
    print(random.sample(range(1, n * 10), n))
    return random.sample(range(1, n * 10), n)

def ordenar_lista(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

def busqueda_lineal(lista, numero):
    inicio = time.time()
    for i, elemento in enumerate(lista):
        if elemento == numero:
            fin = time.time()
            print(f"Tiempo de ejecución de la búsqueda lineal: {fin - inicio:.8f} segundos")
            return i
    fin = time.time()
    print(f"Tiempo de ejecución de la búsqueda lineal: {fin - inicio:.8f} segundos")
    return -1

def busqueda_binaria(lista, numero):
    inicio = time.time()
    inicio_idx = 0
    fin_idx = len(lista) - 1
    while inicio_idx <= fin_idx:
        medio = (inicio_idx + fin_idx) // 2
        if lista[medio] == numero:
            fin = time.time()
            print(f"Tiempo de ejecución de la búsqueda binaria: {fin - inicio:.8f} segundos")
            return medio
        elif lista[medio] < numero:
            inicio_idx = medio + 1
        else:
            fin_idx = medio - 1
    fin = time.time()
    print(f"Tiempo de ejecución de la búsqueda binaria: {fin - inicio:.8f} segundos")
    return -1

def realizar_busqueda_binaria(lista, numero):
    respuesta = input("¿La lista está ordenada? (s/n): ").lower()
    if respuesta == 'n':
        print("Ordenando la lista antes de realizar la búsqueda binaria.")
        lista = ordenar_lista(lista)
    elif respuesta != 's':
        print("Respuesta no válida. Asumiendo que la lista no está ordenada.")
        lista = ordenar_lista(lista)
    return busqueda_binaria(lista, numero)

