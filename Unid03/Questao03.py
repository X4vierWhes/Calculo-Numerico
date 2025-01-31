import numpy as np

def f(x):
    return x**2  # Função a ser integrada

# Entrada do usuário
a = float(input("Digite o intervalo inferior: "))
b = float(input("Digite o intervalo superior: "))
n = int(input("Digite o número de partições (múltiplo de 4): "))

# Garantir que n seja múltiplo de 4
if n % 4 != 0:
    raise ValueError("O número de partições deve ser múltiplo de 4 para a regra de Boole.")

deltax = (b - a) / n  # Tamanho do subintervalo

# Aplicação da Regra de Boole Repetida
soma = 0

for i in range(0, n + 1, 4):
    x0 = a + i * deltax
    x1 = x0 + deltax
    x2 = x0 + 2 * deltax
    x3 = x0 + 3 * deltax
    x4 = x0 + 4 * deltax
    x5 = x0 + 5 * deltax

    soma += (19 * f(x0) + 75 * f(x1) + 50 * f(x2) + 50 * f(x3) + 75 * f(x4) + 19 * f(x5))

integral = (b - a) * soma / (288 * (n / 4))

print(f"Resultado da integral: {integral}")