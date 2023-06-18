"""10.	Elaborar un algoritmo que pida las 3 notas de n estudiantes e imprima la nota más alta, la más baja y el promedio."""

numEstud = int(input("Ingrese la cantidad de estudiantes: "))
contadorEstudiantes = 1

notaAlta = float('-inf')
notaBaja = float('inf')
suma_notas_total = 0

while contadorEstudiantes <= numEstud:
    print("Estudiante", contadorEstudiantes)
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))

    suma_notas_estudiante = nota1 + nota2 + nota3
    promedioEstudiante = suma_notas_estudiante / 3

    if promedioEstudiante > notaAlta:
        notaAlta = promedioEstudiante

    if promedioEstudiante < notaBaja:
        notaBaja = promedioEstudiante

    suma_notas_total += suma_notas_estudiante

    contadorEstudiantes += 1

promedioTotal = suma_notas_total / (numEstud * 3)

print(f"Nota más alta: {notaAlta:.3f}")
print(f"Nota más baja: {notaBaja:.3f}")
print(f"Promedio total: {promedioTotal:.3f}")
