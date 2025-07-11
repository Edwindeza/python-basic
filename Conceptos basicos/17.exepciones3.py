import math

def evaluaEdad(edad):
  if edad < 0:
    raise TypeError("No se permiten edades negativas")
  elif edad < 20:
    return "Eres muy joven"
  elif edad < 40:
    return "Eres joven"
  elif edad < 65:
    return "Eres maduro"
  else:
    return "Eres un anciano"

print(evaluaEdad(15))


def calculaRaiz(num1):
  if num1 < 0:
    raise ValueError("El numero no puede ser negativo")
  else:
    return math.sqrt(num1)

op1=int(input("Ingrese un numero: "))
try:
  print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
  print(ErrorDeNumeroNegativo)
print("Programa terminado")
