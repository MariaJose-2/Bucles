"""1.	Digite un número, si el numero supera a 10, multiplique los 10 primeros números, sino, súmelos"""

numero = int(input("Ingrese un número: "))
resultado=1 if numero >10 else 0

if numero > 10:
    contador = 1
    while contador <= 10:
        resultado *= contador
        contador += 1
else:
    contador = 1
    while contador <= numero:
        resultado += contador
        contador += 1

print("El resultado es: ",resultado)
