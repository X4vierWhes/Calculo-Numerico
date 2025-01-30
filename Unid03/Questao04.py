import numpy as np
import matplotlib.pyplot as plt

# Constantes
g = 9.81  # aceleração da gravidade (m/s²)
L = 1.0   # comprimento do fio do pêndulo (m)

# Condições iniciais
theta0 = np.pi / 3  # ângulo inicial (rad)
omega0 = 0.0  # velocidade angular inicial (rad/s)

# Parâmetros numéricos
dt = 0.01  # passo de tempo (s)
t_max = 10.0  # tempo máximo de simulação (s)

# Vetores para armazenar os resultados
t = np.arange(0, t_max, dt)

theta_euler = np.zeros(len(t))
omega_euler = np.zeros(len(t))

theta_rk4 = np.zeros(len(t))
omega_rk4 = np.zeros(len(t))

# Condições iniciais
theta_euler[0] = theta0
omega_euler[0] = omega0

theta_rk4[0] = theta0
omega_rk4[0] = omega0

# Método de Euler
for i in range(1, len(t)):
    omega_euler[i] = omega_euler[i-1] - (g/L) * np.sin(theta_euler[i-1]) * dt
    theta_euler[i] = theta_euler[i-1] + omega_euler[i] * dt

# Função que define as equações diferenciais
def pendulo_eqs(theta, omega):
    dtheta_dt = omega
    domega_dt = - (g / L) * np.sin(theta)
    return dtheta_dt, domega_dt

# Método de Runge-Kutta de 4ª ordem
for i in range(1, len(t)):
    k1_theta, k1_omega = pendulo_eqs(theta_rk4[i-1], omega_rk4[i-1])
    k2_theta, k2_omega = pendulo_eqs(theta_rk4[i-1] + k1_theta * dt / 2, omega_rk4[i-1] + k1_omega * dt / 2)
    k3_theta, k3_omega = pendulo_eqs(theta_rk4[i-1] + k2_theta * dt / 2, omega_rk4[i-1] + k2_omega * dt / 2)
    k4_theta, k4_omega = pendulo_eqs(theta_rk4[i-1] + k3_theta * dt, omega_rk4[i-1] + k3_omega * dt)
    
    theta_rk4[i] = theta_rk4[i-1] + (dt / 6) * (k1_theta + 2 * k2_theta + 2 * k3_theta + k4_theta)
    omega_rk4[i] = omega_rk4[i-1] + (dt / 6) * (k1_omega + 2 * k2_omega + 2 * k3_omega + k4_omega)

# Plotagem dos resultados
# Cálculo do erro entre os métodos
erro = np.abs(theta_euler - theta_rk4)

# Criar uma nova figura para comparação
plt.figure()

# Gráfico da comparação dos métodos
plt.plot(t, theta_euler, label='Euler')
plt.plot(t, theta_rk4, label='Runge-Kutta 4')
plt.xlabel('Tempo (s)')
plt.ylabel('Ângulo (rad)')
plt.title('Movimento do Pêndulo Simples - Comparação')
plt.legend()
plt.grid()

# Criar uma nova figura para o erro
plt.figure()

# Gráfico do erro ao longo do tempo
plt.plot(t, erro, label='Erro Euler vs RK4', color='red')
plt.xlabel('Tempo (s)')
plt.ylabel('Erro (rad)')
plt.title('Diferença entre Euler e Runge-Kutta')
plt.grid()
plt.legend()

# Mostrar os gráficos
plt.show()

