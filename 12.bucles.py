#Bucles

# Bucle determinado
for i in range(10): #range(10) es 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. Es un metodo de python que genera una secuencia de numeros.
    print(i)

# Bucle indeterminado
while True:
  print("Hola")
  break

# Bucle indeterminado con condición
count = 0 #contador es una variable que se incrementa en 1 en cada iteracion.
while True: #Cuidado, un bucle que nunca termina se llama bucle infinito y se debe evitar.
  print(f"Hola {count}") 
  count += 1 # contador = contador + 1
  if count == 10:
    break #break es una palabra reservada que termina el bucle.

# Bucle indeterminado con condición

count = 0
while count < 10:
  print(f"Hola {count}")
  count += 1

# Bucle determinado con condición
for i in range(10):
  print(f"Hola {i}")
  if i == 5:
    break

# lista de un numero a otro

for i in range(1, 10):
  print(f"Indice: {i}")

# lista de un numero a otro con paso
for i in range(1, 10, 2): # 1, 3, 5, 7, 9. El 2 es el paso. (1, 10) es el rango.
  print(f"Indice2: {i}")

# Recorrer una lista
my_list = [1, 2, 3, 4, 5]
for i in my_list:
  print(f"Hola {i}")

# Recorrer un diccionario
my_dict = {"nombre": "Juan", "edad": 20, "ciudad": "Madrid"}
for key, value in my_dict.items():
  print(f"{key}: {value}")

# for con index y elementos
my_list = [1, 2, 3, 4, 5]
for index, element in enumerate(my_list):
  print(f"El elemento {element} tiene el indice {index}")

# for con index y elementos
my_dict = {"nombre": "Juan", "edad": 20, "ciudad": "Madrid"}
print(my_dict.items())
for index, element in enumerate(my_dict):
  print(f"El elemento {element} tiene el indice {index}")

# While
condition = True
while condition:
  print("Hola")
  condition = False

# While con break
condition = True
while condition:
  print("Hola")
  condition = False
  break

# continue, pass y else
condition = True
while condition:

  print("Hola")
  condition = False
  continue #continue es una palabra reservada que termina la iteracion actual y continua con la siguiente.
  # si no se usa continue, el bucle se ejecutara infinitamente.
  pass #pass es una palabra reservada que no hace nada.
  else:
    print("Fin del bucle")


for letra in "Edwin Deza":

  if letra == "e":
    continue

  print(f"Letra: {letra}")

# Contar caracteres de una cadena

cadena = "Edwin Deza"
print(len(cadena)) # cuenta espacios y caracteres.
count = 0
for letra in cadena:
  if(letra == " "):
    continue
  count += 1 # count = count + 1. Cuenta solo los caracteres
print(f"La cadena tiene {count} caracteres")

# Formas de declarar un bucle sin hacer nada
while True:
  pass

for i in range(10):
  pass

# Formas de declarar un bucle con break
while True:
  break # break es una palabra reservada que termina el bucle.

email = input("Ingrese su email: ")
for i in range(len(email)):
  if email[i] == "@":
    print("Email valido")
    break
else:
  print("Terminamos de recorrer el bucle")
  
# Formas de declarar un bucle con continue
