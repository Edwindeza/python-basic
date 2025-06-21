# Funciones con retorno de valores

def greet(name, lastname):
  return f"Hello, {name} {lastname}"

print(greet("Edwin", "Deza"))

# Funciones con retorno de valores
def addition(a, b):
  return a + b

result = addition(10, 20)
print(result)
#otra forma es:
print(addition(10, 20))

# Para python el resultado es una referencia, ¿Que significa esto?
# Esto significa que el resultado es una referencia a la función, no el valor de la función.
# Por lo tanto, si modificas el resultado, se modificará el valor de la función.
# Ejemplo:
result = addition(10, 20)
print(result)
result = 100
print(result)
print(addition(10, 20))

