"""5.	Hacer un programa que imprima la suma de todos los números impares desde 1 hasta n, y diga cuantos números impares hay"""

num = int(input("Ingrese un número: "))
suma = 0
contador = 0
for n in range(1, num + 1, 2):
    suma += n
    contador += 1
print(f"La suma de los números impares hasta {num} es: {suma}")
print(f"Cantidad de números impares es: {contador}")
