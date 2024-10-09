suma = 0
promedio = 0
cantidad= int(input("Ingrese la cantidad de notas a evaluar: "))
if cantidad > 0:
    for i in range(cantidad):
        notas=int(input("Ingrese las notas: "))
        suma += notas
    promedio = suma/cantidad
else:
    print("La cantidad de notas deben ser mayores a 0")
print("El promedio de las notas es: "+ str(promedio))