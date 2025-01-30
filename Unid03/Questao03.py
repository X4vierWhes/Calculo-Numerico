import numpy as np

def f(x):
    return np.exp(x)

a = float(input("Digite o intervalo inferior: "))
b = float(input("Digite o intervalo superior: "))
n = int(input("Digite o número de partições (múltiplo de 4): "))

# Garantindo que n seja múltiplo de 4
if n % 4 != 0:
    print("O número de partições deve ser múltiplo de 4 para a Regra de Boole.")
    exit()

deltax = (b - a) / n

soma1 = 0
soma2 = 0
soma3 = 0
soma4 = 0
soma5 = 0

for i in range(n + 1):
    x = a + deltax * i
    if i == 0 or i == n:
        soma1 = (soma1 + 7 * f(x))
    elif i % 4 == 1 or i % 4 == 3:
        soma2 = (soma2 + 32 * f(x))
    elif i % 4 == 2:
        soma3 = (soma3 + 12 * f(x))
    elif i % 4 == 0:
        soma4 = (soma4 + 14 * f(x))

soma = (2 * deltax / 45) * (soma1 + soma2 + soma3 + soma4)

print("O valor aproximado da integral é:", soma)
