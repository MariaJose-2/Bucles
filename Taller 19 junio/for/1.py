""""1.	Suma de los n primeros números, solicite al usuario el numero de elementos a sumar"""

numero = int(input("Ingrese el número de elementos a sumar: "))
suma = 0
for n in range(1, numero+1):
    suma += n
print(f"La suma de los primeros {numero} números es: {suma}")
