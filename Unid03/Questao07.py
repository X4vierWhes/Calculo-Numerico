import numpy as np
import matplotlib.pyplot as plt

# Definição dos parâmetros do problema
g0 = 9.81  # Aceleração gravitacional na superfície da Terra (m/s²)
R = 6.37e6  # Raio da Terra (m)
v0 = 1400  # Velocidade inicial (m/s)
x0 = 0  # Altura inicial (superfície da Terra)
h = 0.0001  # Passo de tempo (segundos)
t_max = 500  # Tempo máximo para simulação (segundos)

# Função que define dv/dt
def dv_dt(x):
    return -g0 * (R*2) / ((R + x)*2)

# Método de Euler
t_values = [0]
x_values = [x0]
v_values = [v0]

t = 0
x = x0
v = v0

while v > 0:  # Continua até a velocidade ser zero (altura máxima)
    v_new = v + h * dv_dt(x)
    x_new = x + h * v

    t += h
    v = v_new
    x = x_new

    t_values.append(t)
    x_values.append(x)
    v_values.append(v)

# Plotando os resultados
plt.figure(figsize=(8, 5))
plt.plot(t_values, x_values, label="Altura (m)")
plt.xlabel("Tempo (s)")
plt.ylabel("Altura (m)")
plt.title("Altura x Tempo (Método de Euler)")
plt.legend()
plt.grid()
plt.show()

# Exibindo a altura máxima atingida
print(f"Altura máxima atingida: {max(x_values):.2f} metros")