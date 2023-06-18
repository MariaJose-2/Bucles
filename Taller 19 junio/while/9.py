"""9.	Elabore un algoritmo que permita ingresar n número de temperaturas y escriba la temperatura más alta, la más baja y la temperatura promedio."""

numTemperaturas = int(input("Ingrese la cantidad de temperaturas: "))

contador = 0
temperaturaTotal = 0
temperaturaAlta = float('-inf')
temperaturaBaja = float('inf') 

while contador < numTemperaturas:
    temperatura = float(input("Ingrese la temperatura: "))
    temperaturaTotal += temperatura

    if temperatura > temperaturaAlta:
        temperaturaAlta = temperatura

    if temperatura < temperaturaBaja:
        temperaturaBaja = temperatura

    contador += 1

temperaturaPromedio = temperaturaTotal / numTemperaturas

print("Temperatura más alta:", temperaturaAlta)
print("Temperatura más baja:", temperaturaBaja)
print(F"Temperatura promedio: {temperaturaPromedio:.2F}")
