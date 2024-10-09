suma = 0
promedio = 0
cantidad = int(input("Ingrese la cantidad de estudiantes a evaluar: "))
notas = []

for i in range(cantidad): #en el bucle, de acuerdo a la cantidad se piden las notas 
    numNotas = int(input("Ingrese la cantidad de notas: "))
    for q in range(numNotas):
        nota = int(input("Ingrese la nota del estudiante: "))
        notas.append(nota) #se agrega las notas ingresadas a la lista 

suma = sum(notas) #se suman las notas para luego sacar el promedio 
promedio = suma / cantidad

print("Las notas son:", notas)
print("La suma de las notas es:", suma)
print("El promedio de las notas es:", promedio)
#deberia generar una lista para cada estudiante y un promedio para cada estudiante