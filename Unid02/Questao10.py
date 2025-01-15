import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import csv
import os

def ler_dados(arquivo):
    T = []
    with open(arquivo, 'r') as f:
        reader = csv.reader(f)
        for linha in reader:
            if linha:  
                x, y = map(float, linha[:2])  
                T.append((x, y))
    return T

def salvar_resultados(arquivo, resultados):
    with open(arquivo, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['x', 'p(x)'])  
        writer.writerows(resultados)  

# Caminho do arquivo de entrada
input_file = os.path.join('Unid02', 'Questao10.csv')
output_file = 'resultados_10.csv'
T = ler_dados(input_file)

# Separa os pontos em coordenadas x e y
x_points, y_points = zip(*T)

# Cria a spline cúbica com os pontos fornecidos
spline = CubicSpline(x_points, y_points, bc_type='natural')  

# Calcula o valor de f(0.25)
f_025 = spline(0.25)
print(f"f(0.25) ≈ {f_025}")

# Gera valores para o gráfico da função spline
x_interp = np.linspace(min(x_points), max(x_points), 500)
y_interp = spline(x_interp)

resultados = list(zip(x_interp, y_interp))
salvar_resultados(output_file, resultados)

# Cria o gráfico
plt.figure(figsize=(8, 6))
plt.plot(x_interp, y_interp, color='#FF4500', linewidth=1.5, label="Interpolação Spline Cúbica")
plt.scatter(x_points, y_points, color='blue', s=40, marker='o', label="Pontos originais")  
plt.scatter(0.25, f_025, color='green', s=60, marker='x', label=f"f(0.25) ≈ {f_025:.4f}")  
plt.title('Spline Cúbica Natural')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()

# Mostra o gráfico
plt.show()
