import numpy as np
import matplotlib.pyplot as plt
import csv

# Avalia o polinômio interpolador usando polinômios de Lagrange
def interpolL(x, T):
    soma = 0
    for i in range(len(T)):
        produto = 1.0
        denominador = 1.0
        for j in range(len(T)):
            if j != i:
                denominador *= (T[i][0] - T[j][0])
        for j in range(len(T)):
            if j != i:
                produto *= (x - T[j][0]) / denominador
        soma = soma + T[i][1] * produto
    return soma

def ler_dados(arquivo):
    T = []
    with open(arquivo, 'r') as f:
        reader = csv.reader(f)
        for linha in reader:
            x, y = map(float, linha)
            T.append((x, y))
    return T

def salvar_resultados(arquivo, resultados):
    with open(arquivo, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['x', 'p(x)'])
        writer.writerows(resultados)

input_file = 'Unid02\Questao07.csv'

output_file = 'resultados.csv'
T = ler_dados(input_file)

p = lambda x: interpolL(x, T)

x = np.linspace(min(T, key=lambda item: item[0])[0], max(T, key=lambda item: item[0])[0], 500)

resultados = [(xi, p(xi)) for xi in x]
salvar_resultados(output_file, resultados)

# Plota o gráfico
plt.figure(figsize=(6, 6))
y_values = [p(xi) for xi in x]
plt.plot(x, y_values, color='#FF4500', marker='', linewidth=1.0)
# Plota o gráfico
plt.figure(figsize=(6, 6))
plt.plot(x, y_values, color='#FF4500', marker='', linewidth=1.0)
plt.grid()
plt.show()

valor_especifico = 9.7
print(f"O valor interpolado para x = {valor_especifico} é {p(valor_especifico)}")
print(f"O valor interpolado para x = {valor_especifico} é {p(valor_especifico)}")
