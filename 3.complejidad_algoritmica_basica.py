

# usaremos una lista aqui pero la veremos más adelante a detalle
lista = [1, 2, 3, 4, 5]
resultado = 10 in lista
print(resultado) #True
print(type(resultado))

resultado = 10 not in lista
print(resultado)
print(type(resultado))

# Complejidad temporal
# Complejidad temporal es el tiempo que tarda un algoritmo en ejecutarse.
# Aquí una lista es un array, y un array es una estructura de datos que almacena valores en una secuencia contigua.
# Por lo tanto, una lista es una estructura de datos que almacena valores en una secuencia contigua.
# Al recorrer con el operador "in", se recorre la lista completa, por lo tanto, la complejidad temporal es O(n).
# Debemos tener en cuenta esto, ya que en otros lenguajes de programación, la complejidad temporal es O(1).

# Más adelante veremos como medir la complejidad temporal de un algoritmo.
