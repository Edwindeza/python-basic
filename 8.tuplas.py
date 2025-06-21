# Tuplas
# Las tuplas son una colección de elementos (almacenar varios valores)
# Las tuplas son inmutables, es decir, no se pueden modificar.
# Las tuplas son definidas con () y los elementos se separan por comas.
# Ejemplo:
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Para acceder a un elemento de la tupla, se usa el índice.
# El índice es la posición del elemento en la tupla.
# El índice comienza en 0.

# Ejemplo:
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])

# Extraer algunos elementos de la tupla
# Estos elementos se guardan en una nueva tupla
new_tuple = tuple[0:2]
print(new_tuple)

# Extraer todos los elementos de la tupla
new_tuple = tuple[:]
print(new_tuple)

# Extraer todos los elementos de la tupla desde el indice 2
new_tuple = tuple[2:]
print(new_tuple)

#Ventajas sobre las listas
# Las tuplas son más rápidas que las listas.
# Las tuplas son más seguras que las listas.
# Las tuplas son más fáciles de usar que las listas.
# Las tuplas son más fáciles de entender que las listas.
# Las tuplas son más fáciles de usar que las listas.
# las tuplas ocupan menos memoria que las listas.

#Convertir una tupla a una lista
new_list2 = list(new_tuple)
print(new_list2)

#Convertir una lista a una tupla
new_tuple2 = tuple(new_list2)
print(new_tuple2)

#Eliminar una tupla
del new_tuple2
#print(my_tuple) # Esto daría error porque my_tuple ya no existe

# Recuerdan el operador in?
# El operador in es un operador de pertenencia, es decir, se usa para saber si un elemento está en una tupla.
# Saber si hay un elemento en la tupla
print(1 in new_tuple)

# Saber si hay un elemento en la tupla
print(1 not in new_tuple)

# Cuantas veces aparece un elemento en la tupla
tuplas_with_element = (1,1,1,2,3,4,1)
print(tuplas_with_element.count(1))

# En que indice aparece un elemento en la tupla
print(tuplas_with_element.index(1))

# Longitud de la tupla
print(len(tuplas_with_element))

#Empaquetado de tuplas
my_tuple = 1, 2, 3, 4, 5
print(my_tuple)

#Desempaquetado de tuplas
pos1, pos2, pos3, pos4, pos5 = my_tuple
print(pos1)
print(pos2)
print(pos3)
print(pos4)
print(pos5)