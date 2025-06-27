def return_cities(*cities): # *cities es un parametro variable que puede recibir cualquier numero de argumentos
  for city in cities:
    # yield es una palabra reservada que se utiliza para crear un generador
    # yield f"Llegué a, {city}" # Recordemos como el f es para formatear el string con variables
    #acceder a caracteres de una cadena
    for letter in city:
      #yield letter # basicamente se recorre cada letra de la ciudad y se devuelve
      yield from city # basicamente se recorre cada letra de la ciudad y se devuelve

cities = return_cities("Madrid", "Barcelona", "Valencia", "Sevilla")

# next() es una funcion que se utiliza para obtener el siguiente valor de un generador
print(next(cities))
print(next(cities))
print(next(cities))
print(next(cities))
print(next(cities))
print(next(cities))
print(next(cities))
print(next(cities))
print(next(cities))
print(next(cities))
print(next(cities))
print(next(cities))