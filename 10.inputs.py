# Inputs

# Inputs sin tipo de dato
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")


print("programa de evaluación de notas")

nota_alumno = int(input("Ingrese la nota del alumno: "))

def evaluacion(nota):
  if nota >= 5:
    print("Aprobado")
  else:
    print("Reprobado")

evaluacion(nota_alumno)