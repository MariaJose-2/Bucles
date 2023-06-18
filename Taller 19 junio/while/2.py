"""2.	Sumar pares desde 0 hasta el número que indique el usuario."""

numero = int(input("Ingrese un número: "))
suma = 0
contador = 0

while contador <= numero:
    if contador % 2 == 0:
        suma += contador
    contador += 1

print(f"La suma de los números pares hasta {numero} es: {suma}")
