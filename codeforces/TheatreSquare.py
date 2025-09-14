import math

n, m, a = map(int,input("").split())
# Cálculo do número de lajes necessárias
lajesHorizontal = math.ceil(n / a)
lajesVertical = math.ceil(m / a)
# Cálculo do total de lajes necessárias
totalLajes = lajesHorizontal * lajesVertical
print(lajesVertical, lajesHorizontal)
print(totalLajes)