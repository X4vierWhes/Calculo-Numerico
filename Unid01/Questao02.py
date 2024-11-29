import numpy as np

def f(x):
    return x ** 2  # Função f(x)

# Solicita ao usuário o valor do acréscimo e o ponto de cálculo da derivada
h = float(input("Digite o valor do acréscimo: "))
x = float(input("Digite o ponto para o cálculo da derivada: "))

# Calculando as derivadas de diferentes ordens
derivada1_ordem1 = (f(x + h) - f(x)) / h
derivada2_ordem1 = (f(x) - f(x - h)) / h
derivada3_ordem1 = (f(x + h) - f(x - h)) / (2 * h)
derivada4_ordem1 = (f(x - 2 * h) + 8 * f(x + h) - 8 * f(x - h) - f(x + 2 * h)) / (12 * h)
derivada1_ordem2 = (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)
derivada2_ordem2 = -(f(x + 2 * h) - 16 * f(x + h) + 30 * f(x) - 16 * f(x - h) + f(x - 2 * h)) / (12 * (h ** 2))
derivada1_ordem3 = (f(x + 2 * h) - 2 * f(x + h) + 2 * f(x - h) - f(x - 2 * h)) / (2 * (h ** 3))

# Exibindo os resultados
print(f"A derivada de 1ª ordem (aproximação à frente) no ponto desejado é: {derivada1_ordem1}")
print(f"A derivada de 1ª ordem (aproximação à trás) no ponto desejado é: {derivada2_ordem1}")
print(f"A derivada de 1ª ordem (aproximação central) no ponto desejado é: {derivada3_ordem1}")
print(f"A derivada de 1ª ordem (aproximação de ordem 4) no ponto desejado é: {derivada4_ordem1}")
print(f"A derivada de 2ª ordem no ponto desejado é: {derivada1_ordem2}")
print(f"A derivada de 2ª ordem (aproximação de ordem 4) no ponto desejado é: {derivada2_ordem2}")
print(f"A derivada de 3ª ordem no ponto desejado é: {derivada1_ordem3}")
