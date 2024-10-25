import funciones1 as c 
def mostrar_menu():
    print("\nMenú Principal")
    print("1. Ingresar lista manualmente")
    print("2. Generar lista aleatoria")
    print("3. Ordenar lista")
    print("4. Búsqueda lineal")
    print("5. Búsqueda binaria")
    print("6. Salir")

def main():
    lista_actual = []
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            lista_actual = c.ingresar_lista()
            print("Lista ingresada:", lista_actual)
        
        elif opcion == '2':
            n = int(input("Ingrese el tamaño de la lista aleatoria: "))
            lista_actual = c.generar_lista_aleatoria(n)
            print("Lista aleatoria generada:", lista_actual)
        
        elif opcion == '3':
            if lista_actual:
                lista_actual = c.ordenar_lista(lista_actual)
                print("Lista ordenada:", lista_actual)
            else:
                print("Primero debes generar o ingresar una lista.")
        
        elif opcion == '4':
            if lista_actual:
                numero = int(input("Ingrese el número a buscar (búsqueda lineal): "))
                posicion = c.busqueda_lineal(lista_actual, numero)
                if posicion != -1:
                    print(f"El número {numero} se encontró en la posición {posicion}.")
                else:
                    print(f"El número {numero} no se encontró en la lista.")
            else:
                print("Primero debes generar o ingresar una lista.")
        
        elif opcion == '5':
            if lista_actual:
                numero = int(input("Ingrese el número a buscar (búsqueda binaria): "))
                posicion = c.realizar_busqueda_binaria(lista_actual, numero)
                if posicion != -1:
                    print(f"El número {numero} se encontró en la posición {posicion}.")
                else:
                    print(f"El número {numero} no se encontró en la lista.")
            else:
                print("Primero debes generar o ingresar una lista.")
        
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opcion No Válida. Intente de nuevo.")