# Creación de clase  persona

class persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


    def saludar(self):
        return f"hola, mi nombre es {self.nombre} {self.apellido}"


Savio = persona("Savio","Naguicha", 33,)
print(Savio.saludar())
print(Savio.nombre)
print(Savio.apellido)
print(Savio.edad)

