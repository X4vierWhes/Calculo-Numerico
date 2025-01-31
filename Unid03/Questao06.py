import matplotlib.pyplot as plt

# Função 
def dvdt(v, g, cd, m):
    return g - (cd / m) * v**2

# Método de Euler
def euler(g, cd, m, y0, v0, t0, dt):
    t = t0
    y = y0
    v = v0
    t_array = [t0]
    y_array = [y0]
    v_array = [v0]

    while y > 0:
        dv = dvdt(v, g, cd, m) * dt
        v += dv
        y -= v * dt
        t += dt
        t_array.append(t)
        y_array.append(y)
        v_array.append(v)

    return t_array, y_array, v_array

# Método de Runge-Kutta
def rk4(g, cd, m, y0, v0, t0, dt):
    t = t0
    y = y0
    v = v0
    t_array = [t0]
    y_array = [y0]
    v_array = [v0]

    while y > 0:
        k1 = dvdt(v, g, cd, m)
        k2 = dvdt(v + 0.5 * dt * k1, g, cd, m)
        k3 = dvdt(v + 0.5 * dt * k2, g, cd, m)
        k4 = dvdt(v + dt * k3, g, cd, m)

        v += (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        y -= v * dt
        t += dt

        t_array.append(t)
        y_array.append(y)
        v_array.append(v)

    return t_array, y_array, v_array

# Parâmetros
g = 9.81
cd = 0.225
m = 90
y0 = 1000
v0 = 0
t0 = 0
dt = 0.1  

# Executando os métodos
t_euler, y_euler, v_euler = euler(g, cd, m, y0, v0, t0, dt)
t_rk4, y_rk4, v_rk4 = rk4(g, cd, m, y0, v0, t0, dt)

# Plotando os resultados
plt.figure(figsize=(6, 6))

# Gráfico da altura em função do tempo
plt.subplot(2, 1, 1)
plt.plot(t_euler, y_euler, label='Euler')
plt.plot(t_rk4, y_rk4, label='RK4')
plt.title('Altura em função do tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Altura (m)')
plt.legend()
plt.grid(True)

# Gráfico da velocidade em função do tempo
plt.subplot(2, 1, 2)
plt.plot(t_euler, v_euler, label='Euler')
plt.plot(t_rk4, v_rk4, label='RK4')
plt.title('Velocidade em função do tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Exibindo os resultados finais
print(f"Tempo até o chão (Euler): {t_euler[-1]} s")
print(f"Velocidade final (Euler): {v_euler[-1]} m/s")
print(f"Tempo até o chão (RK4): {t_rk4[-1]} s")
print(f"Velocidade final (RK4): {v_rk4[-1]} m/s")