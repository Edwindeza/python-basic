# Generador

def generateNums(limit):
  num = 1
  
  while num<limit:
    yield num*2 # Construye un objeto iterable
    num=num+1

returnPairs = generateNums(10) # Guardamos el objeto iterable

#for pair in returnPairs: # Recorremos el objeto iterable
#  print(pair)

print(next(returnPairs))
print(next(returnPairs))
print(next(returnPairs))


# Explicación con IA del beneficio de generadores

# ===== DEMOSTRACIÓN DE MEMORIA =====

import sys # sys es una libreria que nos permite calcular el peso en bytes de un objeto 

# 1. Generador - memoria mínima
def generador_grande(limite):
    for i in range(limite):
        yield i * 2

# 2. Lista - memoria completa
def lista_grande(limite):
    return [i * 2 for i in range(limite)]

# Comparación de memoria
print("\n=== COMPARACIÓN DE MEMORIA ===")

# Generador
gen = generador_grande(1000000)
print(f"Tamaño del generador: {sys.getsizeof(gen)} bytes")

# Lista
lista = lista_grande(1000000)
print(f"Tamaño de la lista: {sys.getsizeof(lista)} bytes")

# El generador solo guarda el estado, no los datos
print(f"El generador usa {sys.getsizeof(gen)} bytes vs {sys.getsizeof(lista)} bytes de la lista")

# ===== EJEMPLO PRÁCTICO =====

print("\n=== EJEMPLO PRÁCTICO ===")

def leer_archivo_grande():
    """Simula leer un archivo grande línea por línea"""
    for i in range(1000):
        yield f"Línea {i}: Datos importantes..."

# Con generador - eficiente en memoria
print("Usando generador:")
archivo_gen = leer_archivo_grande()
for i, linea in enumerate(archivo_gen):
    if i < 3:  # Solo mostramos las primeras 3 líneas
        print(linea)
    else:
        break

# Sin generador - ineficiente en memoria
print("\nSin generador (simulado):")
# Esto cargaría todo en memoria de una vez
# archivo_completo = [f"Línea {i}: Datos importantes..." for i in range(1000)]

# ===== GENERADOR INFINITO =====

print("\n=== GENERADOR INFINITO ===")

def numeros_infinitos():
    """Generador que produce números infinitamente"""
    num = 0
    while True:
        yield num
        num += 1

# Esto es posible porque no genera todos los números de una vez
infinito = numeros_infinitos()
print("Primeros 5 números del generador infinito:")
for i in range(5):
    print(next(infinito))

# Si fuera una lista, esto sería imposible:
# lista_infinita = [i for i in range(infinito)]  # ❌ Error de memoria


