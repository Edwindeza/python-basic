def suma(num1, num2):
  return num1 + num2

def resta(num1, num2):
  return num1 - num2

def multiplicacion(num1, num2):
  return num1 * num2

def division(num1, num2):
  try:
    return num1 / num2
  except ZeroDivisionError: #Excepción para dividir por cero
    print("Error: No se puede dividir por cero")
    return "Error"

while True: 
  try: #Bloque de codigo que se ejecuta
    op1=int(input("Ingrese el primer numero: "))
    op2=int(input("Ingrese el segundo numero: "))
    break
  except ValueError: #Excepción para ingresar un valor no numerico
    print("Error: Ingrese un numero valido, intente nuevamente")
  

operacion=input("Ingrese la operacion a realizar (suma, resta, multiplicacion, division): ")

if operacion == "suma":
  print(f"La suma de {op1} y {op2} es {suma(op1, op2)}")

elif operacion == "resta":
  print(f"La resta de {op1} y {op2} es {resta(op1, op2)}")

elif operacion == "multiplicacion":
  print(f"La multiplicacion de {op1} y {op2} es {multiplicacion(op1, op2)}")

elif operacion == "division":
  print(f"La division de {op1} y {op2} es {division(op1, op2)}")

else:
  print("Operacion no valida")

print("Operación ejecutada. Continuando con el programa...")