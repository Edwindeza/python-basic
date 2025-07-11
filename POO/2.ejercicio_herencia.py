
class Persona(): 
  def __init__(self, nombre, edad, lugar_residencia):
    self.nombre = nombre
    self.edad = edad
    self.lugar_residencia = lugar_residencia

  def descripcion(self):
    print("Nombre:", self.nombre, " Edad:", self.edad, " Residencia: ", self.lugar_residencia)

# Que caracteristicas tiene un empleado?
class Empleado(Persona):
  def __init__(self, nombre, edad, lugar_residencia, salario, antiguedad):
    super().__init__(nombre, edad, lugar_residencia)
    self.salario = salario
    self.antiguedad = antiguedad

  def descripcion(self):
    super().descripcion()
    print("Salario:", self.salario, " Antigüedad:", self.antiguedad, "años")

Antonio = Empleado("Antonio", 55, "Perú", 1500, 15)

Antonio.descripcion()

# Principio de sustitucion

# Un objeto de una clase hija puede ser sustituido por un objeto de la clase padre sin que se altere el funcionamiento del programa.

# Ejemplo:

class Persona2:
  def __init__(self, nombre, edad, lugar_residencia):
    self.nombre = nombre
    self.edad = edad
    self.lugar_residencia = lugar_residencia

  def descripcion(self):
    print("Nombre:", self.nombre, " Edad:", self.edad, " Residencia: ", self.lugar_residencia)

class Empleado2(Persona2):
  def __init__(self, nombre, edad, lugar_residencia, salario, antiguedad):
    super().__init__(nombre, edad, lugar_residencia)
    self.salario = salario
    self.antiguedad = antiguedad

  def descripcion(self):
    super().descripcion()
    print("Salario:", self.salario, " Antigüedad:", self.antiguedad, "años")

class Gerente(Empleado2):
  def __init__(self, nombre, edad, lugar_residencia, salario, antiguedad, equipo):
    super().__init__(nombre, edad, lugar_residencia, salario, antiguedad)
    self.equipo = equipo

  def descripcion(self):
    super().descripcion()
    print("Equipo:", self.equipo)

Antonio = Gerente("Antonio", 55, "Perú", 1500, 15, "Equipo de ventas")
#Clase padre
Edwin = Empleado2("Edwin", 30, "Perú", 1000, 5)

Antonio.descripcion()