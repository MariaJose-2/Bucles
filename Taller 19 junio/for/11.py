"""11.	Elabore un algoritmo que pregunte cuántas temperaturas se van a introducir, pida esas temperaturas, y escriba la temperatura más alta, la más baja y la temperatura promedio."""

cantidadTemperaturas = int(input("Ingrese la cantidad de temperaturas: "))
temperaturaAlta = float('-inf')
temperaturaBaja = float('inf')
sumaTemperaturas = 0

for i in range(cantidadTemperaturas):
    temperatura = float(input("Ingrese la temperatura {}: ".format(i+1)))
    sumaTemperaturas += temperatura

    if temperatura > temperaturaAlta:
        temperaturaAlta = temperatura

    if temperatura < temperaturaBaja:
        temperaturaBaja = temperatura

temperaturaPromedio = sumaTemperaturas / cantidadTemperaturas

print("La temperatura más alta es:", temperaturaAlta)
print("La temperatura más baja es:", temperaturaBaja)
print(F"La temperatura promedio es: {temperaturaPromedio:.2F}")
