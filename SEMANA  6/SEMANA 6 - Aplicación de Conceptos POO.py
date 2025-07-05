# Definición de herencias que incluyen datos de personas, empleados, seguridad y métodos de recepción de propiedades

class Persona():
    def __init__(self, nombre, apellido, edad, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cedula = cedula

    def saluda(self):
        return f"Hola, me llamo {self.nombre} {self.apellido}"


class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, cedula, sueldo, horario):
        super().__init__(nombre, apellido, edad, cedula)
        self.sueldo = sueldo
        self.horario = horario

    def saluda(self):
        return f"Hola, me llamo {self.nombre} {self.apellido}"

    def fichar(self, ingreso):
        if (ingreso <= self.horario):
            return f" llegue {self.horario - ingreso}minutos temprano"
        else:
            return f"llegue {ingreso - self.horario}minutos tarde"

class Seguridad(Empleado):
    def __init__(self, nombre, apellido, edad, cedula, sueldo, horario, vehiculo, arma):
        super().__init__(nombre, apellido, edad, cedula, sueldo, horario)
        self.vehiculo = vehiculo
        self.arma = arma

    def llamar_policia(self,mensaje):
        return f"hola policia, les quiero decir {mensaje} "


persona1 = Persona("Savio", "Naguicha", 33, 1400883637)
empleado1 = Empleado("Secha", "Sharupi", 40, 16788890, 800, 12)
seguridad1 = Seguridad("Alvaro", "Novoa", 70, 12345678, 1500, 12, "toyota", "calibre 38")

print(persona1.saluda())
print(empleado1.saluda())
print(seguridad1.saluda())
print(seguridad1.fichar(10))
print(seguridad1.llamar_policia("sufri un robo"))
print(seguridad1.llamar_policia("sufri un asalto"))

