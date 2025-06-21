# Condicionales en Python

# 1. IF simple
edad = 18
if edad >= 18:
    print("Eres mayor de edad")

# 2. IF - ELSE
edad = 16
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# 3. IF - ELIF - ELSE (múltiples condiciones)
nota = 85

if nota >= 90:
    print("Excelente - A")
elif nota >= 80:
    print("Muy bien - B")
elif nota >= 70:
    print("Bien - C")
elif nota >= 60:
    print("Aprobado - D")
else:
    print("Reprobado - F")

# 4. Condicionales anidados
usuario_activo = True
es_admin = False

if usuario_activo:
    if es_admin:
        print("Acceso completo al sistema")
    else:
        print("Acceso limitado al sistema")
else:
    print("Usuario inactivo")

# 5. Operadores de comparación en condicionales
numero = 10

# Igualdad
if numero == 10:
    print("El número es 10")

# Desigualdad
if numero != 5:
    print("El número no es 5")

# Mayor que
if numero > 5:
    print("El número es mayor que 5")

# Menor que
if numero < 20:
    print("El número es menor que 20")

# Mayor o igual
if numero >= 10:
    print("El número es mayor o igual a 10")

# Menor o igual
if numero <= 15:
    print("El número es menor o igual a 15")

# 6. Operadores lógicos en condicionales
edad = 25
tiene_licencia = True
tiene_seguro = False

# AND - ambas condiciones deben ser True
if edad >= 18 and tiene_licencia:
    print("Puede conducir")

# OR - al menos una condición debe ser True
if tiene_licencia or tiene_seguro:
    print("Tiene licencia o seguro")

# NOT - invierte el valor booleano
if not tiene_seguro:
    print("No tiene seguro")

# Combinación de operadores
if edad >= 18 and tiene_licencia and not tiene_seguro:
    print("Puede conducir pero sin seguro")

# 7. Operador ternario (condicional en una línea)
edad = 20
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)

# 8. Verificación de tipos y valores
valor = "Hola"

# Verificar si es string
if isinstance(valor, str):
    print("Es una cadena de texto")

# Verificar si está vacío
if valor:
    print("La variable no está vacía")

# Verificar si está en una lista
colores = ["rojo", "verde", "azul"]
if "rojo" in colores:
    print("El rojo está en la lista")

# 9. Condicionales con rangos
temperatura = 25

if 20 <= temperatura <= 30:
    print("Temperatura agradable")

# 10. Condicionales con múltiples valores
dia = "lunes"

if dia in ["lunes", "martes", "miércoles", "jueves", "viernes"]:
    print("Es día laboral")
elif dia in ["sábado", "domingo"]:
    print("Es fin de semana")
else:
    print("Día no válido")

# 11. Condicionales con None
valor = None

if valor is None:
    print("La variable es None")

if valor is not None:
    print("La variable no es None")

# 12. Condicionales con excepciones (try-except)
try:
    numero = int("abc")
    if numero > 0:
        print("Número positivo")
except ValueError:
    print("No se pudo convertir a número")

# 13. Condicionales con funciones
def es_par(numero):
    return numero % 2 == 0

numero = 10
if es_par(numero):
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")

# 14. Condicionales con diccionarios
estado_civil = "soltero"

mensajes = {
    "soltero": "Eres soltero",
    "casado": "Estás casado",
    "divorciado": "Estás divorciado"
}

if estado_civil in mensajes:
    print(mensajes[estado_civil])
else:
    print("Estado civil no reconocido")

# 15. Condicionales con match (Python 3.10+)
# Nota: Solo funciona en Python 3.10 o superior
puntuacion = 85

match puntuacion:
    case puntuacion if puntuacion >= 90:
        print("Excelente")
    case puntuacion if puntuacion >= 80:
        print("Muy bien")
    case puntuacion if puntuacion >= 70:
        print("Bien")
    case _:
        print("Necesita mejorar") 