
# Representacion diria del clima
class clima:
    def __init__(self, humedad, frio, calido, lluvioso, soleado):
        self._humedad = humedad
        self._frio = frio
        self._calido = calido
        self._lluvioso = lluvioso
        self._soleado = soleado

    def mostrar_datos(self):
        print("humedad:", self._humedad)
        print("frio:", self._frio)
        print("calido:", self._calido)
        print("lluvioso:", self._lluvioso)
        print("soleado:", self._soleado)

    def proporcionar_temperaturas(self):
        print("decir temperaturas")

class ambiente(clima):
    def __init__(self, humedad, frio, calido, lluvioso, soleado, temperaturas):
        super().__init__(humedad, frio, calido, lluvioso, soleado)
        self.temperaturas = temperaturas

    def mostrar_temperaturas(self):
        print(f"temperaturas: {self.temperaturas}")

class tiempo(clima):
    def __init__(self, humedad, frio, calido, lluvioso, soleado, climatologia):
        super().__init__(humedad, frio, calido, lluvioso, soleado)
        self.climatologia = climatologia

    def mostrar_climalogia(self):
        print(f"climatologia: {self.climatologia}")

# Crear objetos
ambiente = ambiente("70%", "20°C", "25°C", "lluvioso", "parcialmente soleado", "22°C")
tiempo = tiempo("60%", "15°C", "28°C", "soleado", "despejado", "soleado")

# Mostrar datos
ambiente.mostrar_temperaturas()
tiempo.mostrar_climalogia()
