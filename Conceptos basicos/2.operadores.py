# Operadores comunes

# Suma
resultado = 10 + 10
print(resultado)
print(type(resultado))

# Resta
resultado = 10 - 10
print(resultado)
print(type(resultado))

# Multiplicación
resultado = 10 * 10
print(resultado)
print(type(resultado))

# División
resultado = 10 / 10
print(resultado)
print(type(resultado))

# Módulo (resto de la división)
resultado = 10 % 2
resultado2 = 10 % 3
print(resultado)
print(type(resultado))
print(resultado2)
print(type(resultado2))

# Potencia
resultado = 10 ** 2
print(resultado)
print(type(resultado))

# División entera
resultado = 10 // 3 # Normalmente nos da un float, pero con el operador // nos da un int (redondea hacia abajo) = 3
print(resultado)
print(type(resultado))

# Operadores de comparación
resultado = 10 == 10
print(resultado)
print(type(resultado))

# Operadores de asignación
resultado = 10
resultado += 10
print(resultado)
print(type(resultado))

# Operadores lógicos
resultado = True and True
print(resultado)
print(type(resultado))

resultado = True and False
print(resultado)
print(type(resultado))

resultado = True or False
print(resultado)
print(type(resultado))

resultado = not True
print(resultado)
print(type(resultado))

# Operadores de pertenencia
resultado = 10 in [10, 20, 30]
print(resultado)

# Operadores de identidad
resultado = 10 is 10
print(resultado)
print(type(resultado))

resultado = 10 is not 10
print(resultado)
print(type(resultado))

x = 5
y = 5
resultado = x is y
print(resultado)
print(type(resultado))

resultado = x is not y
print(resultado)
print(type(resultado))

# usaremos una lista aqui pero la veremos más adelante a detalle
lista = [1, 2, 3, 4, 5]
resultado = 10 in lista
print(resultado) #True
print(type(resultado))

resultado = 10 not in lista
print(resultado)
print(type(resultado))

# is y is not son operadores de identidad, es decir, se comparan los valores y las referencias de las variables.

# Eso significa que si creamos una lista y la asignamos a otra variable, ambas variables tendrán la misma referencia.
# Por lo tanto, is y is not serán False.
# Pero si creamos una lista y la asignamos a otra variable, ambas variables tendrán distinta referencia.
# Por lo tanto, is y is not serán True.

# Esto es muy importante, ya que en otros lenguajes de programación, is y is not se comparan los valores y las referencias de las variables.
# Eso significa que si creamos una lista y la asignamos a otra variable, ambas variables tendrán la misma referencia.
# Por lo tanto, is y is not serán False.

lista2 = [1, 2, 3, 4, 5]
resultado = lista is lista2
print(resultado) #False
print(type(resultado))

resultado = lista is not lista2
print(resultado) #True
print(type(resultado))

# Operadores de identidad