"""4.	Hacer un programa que pida dos números y muestre todos los números que van desde el primero al segundo, validar que el primer número sea menor que el segundo"""

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

contador =numero1
while contador <= numero2:
    print(contador)
    contador += 1

print("el primer numero debe ser menor que el segundo")