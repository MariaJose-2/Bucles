"""3.	Hacer un programa que imprima la suma de todos los números impares desde 1 hasta n, y diga cuantos números impares hay"""

numero = int(input("Ingrese un número: "))
suma = 0
contador = 1
numImpares = 0

while contador <= numero:
    if contador % 2 != 0:
        suma += contador
        numImpares += 1
    contador += 1

print(f"La suma de los números impares hasta {numero} es: {suma}")
print(f"Cantidad de números impares: {numImpares}")
