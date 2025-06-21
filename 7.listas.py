# Lista
# Una lista es una colección de elementos (almacenar varios valores)

# En otros lenguajes de programación, se le conoce como array o bueno cumplen la misma función.

# Ejemplo de una lista:
list = [1, 2, 3, 4, 5]
print(list)

# Para acceder a un elemento de la lista, se usa el índice.
# El índice es la posición del elemento en la lista.
# El índice comienza en 0.
# Ejemplo:
print(list[0])
print(list[1])
print(list[2])

# Diferencias entre listas y arrays
# Una lista es una colección de elementos.
# Un array es una colección de elementos del mismo tipo.
# En python, las listas son más flexibles que los arrays.
list2 = [1, 2, "Edwin", "Deza"]
print(list2)


# Para agregar un elemento al final de la lista, se usa el método append.
# Ejemplo:
list2.append("García")
print(list2)

# Para agregar un elemento a la lista en una posición específica, se usa el método insert.
# Ejemplo:
list2.insert(0, "Edwin")
print(list2)

# Para agregar varios elementos al final de la lista, se usa el método extend (tmb podrias fusionar dos listas).
# Ejemplo:
list2.extend(["García", "Deza"])
print(list2)

# Para eliminar un elemento por valor de la lista, se usa el método remove.
list2.remove("Edwin")
print(list2)

# Para eliminar el último elemento de la lista, se usa el método pop.
list2.pop()
print(list2)

# Para eliminar el primer elemento de la lista, se usa el método pop(0).
list2.pop(0) # El 0 es el índice del elemento a eliminar.
print(list2)

# indice negativo

# Ejemplo:
print(list2[-1])
print(list2[-2])

# Si el indice es menor al tamaño de la lista, se genera una excepción.
# Ejemplo:
print(list2[-5])

# Imprimir la lista completa
print(list2)

# Imprimir algunos elementos de la lista segun el indice
print(list2[0:2])

# Imprimir la lista completa desde el indice 2
print(list2[2:])

# Imprimir la lista completa desde el indice 2 hasta el indice 4
print(list2[2:4])


# El índice negativo es la posición del elemento en la lista, pero contando desde el final.
#print(list2[-6])

#Traceback (most recent call last):
#File "/home/edwindeza/Edwin/estudios/python/7.listas.py", line 77, in <module>
#    print(list2[-6]) # <- Esto genera un error porque el indice es menor al tamaño de la lista.
#          ~~~~~~^^^^
#IndexError: list index out of range

# Para evitar este error, se puede usar el método len() para obtener el tamaño de la lista.
print(len(list2))

# Para obtener el tamaño de la lista, se usa el método len().

# Para repetir una lista, se puede usar el operador *
my_list = [1, 2, 3, 4, 5] * 3
print(my_list)

#ordenar una lista
my_list.sort()
print(my_list)

#ordenar una lista de forma descendente
my_list.sort(reverse=True)
print(my_list)

#ordenar una lista de forma ascendente
my_list.sort(reverse=False)
print(my_list)

#imprimir la lista completa
print(my_list[:])