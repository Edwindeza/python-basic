# Diccionario
# Un diccionario es una colección de pares clave-valor.
# Las claves son únicas y las valores pueden ser de cualquier tipo.
# Los diccionarios se definen con {} y los pares clave-valor se separan por comas.
# Ejemplo:
my_dict = {
    "nombre": "Juan",
    "edad": 20,
    "ciudad": "Madrid"
}
print(my_dict)

# Acceder a un valor del diccionario
print(my_dict["nombre"])

# Agregar un nuevo par clave-valor
my_dict["email"] = "juan@gmail.com"
print(my_dict)

# Modificar un valor del diccionario
my_dict["edad"] = 21
print(my_dict)

# Eliminar un par clave-valor
del my_dict["ciudad"]
print(my_dict)

# Eliminar el diccionario completo
del my_dict
#print(my_dict) # Esto daría error porque my_dict ya no existe

# Recorrer un diccionario

# Guardar una tupla en un diccionario
my_tuple = (1, 2, 3, 4, 5)
my_dict = {
    "nombre": "Juan",
    "edad": 20,
    "ciudad": my_tuple
}
print(my_dict)

# Guardar una lista en un diccionario
my_list = [1, 2, 3, 4, 5]
my_dict = {
    "nombre": "Juan",
    "edad": 20,
    "ciudad": my_list
}
print(my_dict)

# Guardar un diccionario en un diccionario
my_dict2 = {
    "nombre": "Juan",
    "edad": 20,
    "otro_dict": my_dict
}
print(my_dict2)

# Obtener las claves de un diccionario
print(my_dict2.keys())

# Obtener los valores de un diccionario
print(my_dict2.values())

# Obtener los pares clave-valor de un diccionario
print(my_dict2.items())
