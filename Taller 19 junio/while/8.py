"""8.	Elabore un algoritmo que pida un número entero mayor que cero y que escriba sus divisores. Validar que el usuario haya ingresado un número mayor a cero."""

numero = int(input("Ingrese un número entero mayor que cero: "))

while numero <= 0:
    numero = int(input("El número debe ser mayor que cero. Ingrese nuevamente: "))
    
divisores=[]
contador = 1

while contador <= numero:
    if numero % contador == 0:
        divisores.append(contador)
    contador += 1

print(f"Los divisores de {numero} son: {divisores}")
