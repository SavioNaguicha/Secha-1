# Caclcular el promedio de temperatura diaria semanal
def calcular_promedio_temperatura(temperatura_diaria, promedio_semanal):
    nuevo_promedio = (promedio_semanal * 7 + temperatura_diaria)/8
    return nuevo_promedio
temperatura_diaria = 15
promedio_semanal = 20
calcular_promedio_semanal = calcular_promedio_temperatura(temperatura_diaria,promedio_semanal)
print(calcular_promedio_semanal)
print(temperatura_diaria)



























