# Funciones

# Reglas semanticas:
# 1. Las funciones deben tener un nombre descriptivo.
# 2. Las funciones deben tener un solo proposito.
# 3. Las funciones deben ser reutilizables.
# 4. Las funciones deben ser legibles.
# 5. Las funciones deben ser testeables.
# 6. Las funciones deben ser documentadas.
# 7. Las funciones deben ser mantenibles.

# Ejemplo de una función sin parámetros.
def saludar():
  print("Hola, mundo")

# Sino llamas las funciones, no se ejecutan.
saludar()


# Ejemplo de una función con parámetros.
def saludar(nombre, apellido):
  print(nombre)
  print(apellido)

  # Si deseas imprimir el nombre y el apellido juntos, puedes usar el placeholder f.
  print(f"Hola, {nombre} {apellido}")
  # que significa esto?
  # f es un placeholder para el nombre y el apellido.
  # {nombre} es el nombre de la variable.
  # {apellido} es el apellido de la variable.
  # f"Hola, {nombre} {apellido}" es el mensaje que se imprime.
  # saludar("Edwin", "García") es el llamado a la función.
  # Edwin y García son los valores de los parámetros.

saludar("Edwin", "García")

# Se dieron cuenta que la función saludar() se puede llamar con diferentes valores ?
# Esto es muy importante, ya que las funciones son reutilizables.
# Ejemplo:
saludar("Edwin", "García")

# Se dieron cuenta que declare "def saludar()" dos veces? 
# Esto es muy importante, ya que estamos redefiniendo la función saludar().
# Al inicio imprime "Hola, mundo", pero al final imprime "Hola, Edwin Deza" y "Hola, Edwin García".
# Si intentas llamar a la función saludar() sin parámetros, no funcionará.
# Debemos tener en cuenta que las funciones pueden ser redefinidas. Por eso la semantica de las funciones es muy importante.

# Ejemplo de una función con parámetros opcionales.
def saludar(nombre=None, apellido = "García"):
  if nombre is None:
    print(f"Hola, {apellido}")
  else:
    print(f"Hola, {nombre} {apellido}")

saludar()
saludar("Edwin")
saludar("Edwin", "Deza")
saludar(apellido="Deza")

# Ejemplo de una función con parámetros opcionales.
def saludar(nombre, apellido = "García"):
  print(f"Hola, {nombre} {apellido}")

