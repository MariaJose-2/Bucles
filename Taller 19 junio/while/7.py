"""7.	Leer números enteros del teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados."""

numero = int(input("Ingrese un número entero (ingrese 0 para finalizar): "))
suma = 0

while numero != 0:
    suma += numero
    numero = int(input("Ingrese un número entero (ingrese 0 para finalizar): "))

print("La sumatoria de los números ingresados es:", suma)
