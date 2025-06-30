# calcular grados a celsius a fahrenheit
class temperatura():
    def __init__(self, celsius, fahrenhit):
        self.celsius = celsius
        self.fahrenhit = fahrenhit


def grados_a_celsius(celsius,fahrenhit):
    return  (celsius * fahrenhit)/5

# uso
celsius = 24.8
fahrenhit = 7

celsius_a_fahrenhit = grados_a_celsius(celsius, fahrenhit)
print(celsius_a_fahrenhit)