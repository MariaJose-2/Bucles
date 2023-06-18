"""8.	Un maestro de escuela necesita un algoritmo que capture n notas de un estudiante y calcule el promedio"""

numeroNota = int(input("Ingrese la cantidad de notas: "))
suma = 0
for i in range(numeroNota):
    nota = float(input("Ingrese la nota {}: ".format(i+1)))
    suma += nota
promedio = suma / numeroNota
print(f"El promedio de las {numeroNota} notas es: {promedio:.2f}")
