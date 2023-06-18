"""""7.	Algoritmo que pregunte al usuario que tabla de multiplicar quiere ver, debe generar la tabla de multiplicar desde cero hasta 10. """

tabla = int(input("ingrese el numero de la tabla de multiplicar que quiere ver:"))
print("tabla de multiplicar del", tabla, ":")
for num in range(11):
    resultado = tabla * num
    print(tabla, "x", num, "=", resultado)