"""6.	Un maestro de escuela necesita un algoritmo que capture n notas de un estudiante y calcule el promedio"""

numNotas = int(input("Ingrese la cantidad de notas: "))
contador = 0
sumaNotas = 0

while contador < numNotas:
    nota = float(input("Ingrese la nota: "))
    sumaNotas += nota
    contador += 1

promedio = sumaNotas / numNotas
print(f"El promedio de las {numNotas} notas es: {promedio:.2f}")
