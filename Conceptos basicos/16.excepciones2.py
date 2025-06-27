def divide():

  try:
    op1=float(input("Ingrese el primer numero: "))
    op2=float(input("Ingrese el segundo numero: "))

    print("La división es: ", str(op1 / op2))
  except ValueError:
    print("Error: Ingrese un numero valido, intente nuevamente")
    return "Error"
  except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
    return "Error"
  finally:
    print("Fin de la división")

while True:
  try:
    print(divide())
    break
  except ValueError:
    print("Error: Ingrese un numero valido, intente nuevamente")
  except ZeroDivisionError: