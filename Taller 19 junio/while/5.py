"""5.	Crear un programa que permita al usuario ingresar los valores totales de n facturas (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento."""

montoFactura = float(input("Ingrese el monto de la factura (ingrese 0 para finalizar): "))
totalPagar = 0

while montoFactura != 0:
    totalPagar += montoFactura
    montoFactura = float(input("Ingrese el monto de la factura (ingrese 0 para finalizar): "))

if totalPagar > 1000:
    descuento = totalPagar * 0.1
    totalPagar -= descuento

print("El total a pagar es:", totalPagar)
