"""6.	Hacer un programa que pida dos números y muestre todos los números que van desde el primero al segundo, validar que el primer número sea menor que el segundo"""

numero1 = int(input("ingrese el primer numero:"))
numero2 = int(input("ingrese el segundo numero:"))
if numero1>=numero2:
    print("el primer numero debe ser menor que el segundo numero.")
else:
    for num in range(numero1, numero2 + 1):
        print(num)
