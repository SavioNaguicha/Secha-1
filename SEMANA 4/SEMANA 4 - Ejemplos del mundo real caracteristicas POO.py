# Creación de clase  persona

# Se define clase persona el constructor toma tres argumentos, nombre, apellido edad.
class persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

# Se define el metodo saludar, y que devuelva un saludo que incluya nombre ya apellido de la persona.
    def saludar(self):
        return f"hola, mi nombre es {self.nombre} {self.apellido}"

# Se crea una instancia de la clase persona llamado savio
Savio = persona("Savio","Naguicha", 33,)

# Imprimir codigo
print(Savio.saludar())
print(Savio.nombre)
print(Savio.apellido)
print(Savio.edad)

