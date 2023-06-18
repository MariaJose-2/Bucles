"""2.	Digite un número, si el numero supera a 10, multiplique los 10 primeros números, si no, súmelos"""

numero = int(input("Ingrese un número: "))
resultado = 1 if numero > 10 else 0

if numero > 10:
    for i in range(1, 11):
        resultado *= i
else:
    for i in range(1, numero + 1):
        resultado += i

print("El resultado es: ",resultado)

