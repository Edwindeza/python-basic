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

# Formatear
str(input("Ingrese su nombre: "))
int(input("Ingrese su edad: "))
print(f"Hola {nombre} tienes {edad} años")


validations = 1
email = input("Ingrese su email: ")
for i in range(len(email)): 
  if email[i] == "@":
    validation +=1
    break
  else email[i] == ".":
    validation +=1
    break

if validation == 2:
  print("Email valido")
else:
  print("Email invalido")