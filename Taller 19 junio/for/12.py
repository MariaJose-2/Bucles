"""12. Elaborar un algoritmo que pida las 4 notas de n estudiantes e imprima la nota más alta, la más baja y el 
promedio."""
n = int(input("Ingrese la cantidad de estudiantes: "))

notaAlta = float('-inf')
notaBaja = float('inf')
sumaNotas = 0

for i in range(n):
    print("Estudiante", i+1)
    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))
    nota4 = float(input("Ingrese la nota 4: "))

    sumaEstudiante = nota1 + nota2 + nota3 + nota4
    promedioEstudiante = sumaEstudiante / 4

    sumaNotas += sumaEstudiante

    if promedioEstudiante > notaAlta:
        notaAlta = promedioEstudiante

    if promedioEstudiante < notaBaja:
        notaBaja = promedioEstudiante

promedioGeneral = sumaNotas / (4 * n)

print(f"La nota más alta es: {notaAlta:.3f}")
print(f"La nota más baja es: {notaBaja:.3f}")
print(f"El promedio general es: {promedioGeneral:.3f}")


