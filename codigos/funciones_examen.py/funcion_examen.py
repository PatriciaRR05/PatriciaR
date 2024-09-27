def menu():
    print("""Sistema de gestion de notas
          1. Eliminar nota
          2. Modificar nota
          3. Mostrar todas las notas
          4. Calcular promedio de notas
          5. Obtener nota maxima y minima 
          6. Salir
          Elige una opcion: """)
def add_nota(notas):
    a= int(input("Ingrese nota: "))
    notas.append(a)
    return notas

def del_notas(notas):
    ind=len(notas)
    a=int(input("Ingrese un indice: "))
    notas.pop(a)
    return notas

def mod_notas(notas):
    a=int(input("Ingrese indice a modificar: "))
    b =float(input(f"Ingrese el numero a modiciar"))
    notas[a]= b
    return notas

def calc_notas(notas):
    prom= sum(notas)/len(notas)


def nota_maxi_minim(notas):
    maximo= max(notas)
    minimo=min(notas)
    return maximo , minimo

def mostrar_notas(notas):
    print(notas)