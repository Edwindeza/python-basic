# Condicionales
#Aqui veremos algo interesante en la sintaxis de python, que es la indentación.

# Condicionales

# if: si la condición es verdadera, se ejecuta el bloque de código.
# elif: si la condición es falsa, se ejecuta el bloque de código. (Necesita un if antes)
# else: si la condición es falsa, se ejecuta el bloque de código. (Necesita un if o elif antes)

if 10 > 5:
  print("10 es mayor que 5")

if 10 < 5:
  print("10 es menor que 5")

# La indentación es el espacio que se deja al inicio de una línea de código.
# En python, la indentación es muy importante, ya que se usa para definir el bloque de código.
# Ejemplo:
if 10 > 5:
  print("10 es mayor que 5")
else:
  print("10 no es mayor que 5")

# En tu VSC, puedes usar el tabulador para indentar el código.
# También puedes usar el espacio para indentar el código.
# Pero, el tabulador es más recomendado, ya que es más preciso.

# Entonces, si queremos que se ejecute un bloque de código, debemos indentarlo.
# Si no queremos que se ejecute un bloque de código, debemos no indentarlo.
# Ejemplo con if y else:
if 10 > 5:
  print("10 es mayor que 5")
else:
  print("10 no es mayor que 5")


# Ejemplo con if, elif y else:
if 10 > 5:
  print("10 es mayor que 5")
elif 10 == 5:
  print("10 es igual a 5")
else:
  print("10 no es mayor que 5")

# Ejemplo practico, desde aquí usaremos inglés para que sea más claro.

age_limit = 18

age = 15

if age >= age_limit:
  print("You are an adult")
else:
  print("You are not an adult")
