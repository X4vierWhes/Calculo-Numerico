import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do modelo
N = 1000  # Total de computadores na rede
beta = 0.002  # Taxa de infecção (probabilidade de um computador infectar outro)
alpha = 0.001  # Taxa de proteção (instalação de antivírus)
gamma = 0.1  # Taxa de recuperação (computadores que são limpos ou formatados)
dt = 0.1  # Passo de tempo para a simulação
T = 50  # Tempo total da simulação (dias)

# Condições iniciais
S, I, R, P = N - 10 - 200, 10, 0, 200  # Inicialização das categorias:
# S = Suscetíveis (ainda não infectados)
# I = Infectados (espalhando o vírus)
# R = Removidos (formatados ou limpos, não podem mais ser infectados)
# P = Protegidos (antivírus ativo, imunes ao vírus)

# Vetores para armazenar os valores ao longo do tempo
t_values = np.arange(0, T, dt)  # Criando um vetor com os instantes de tempo
S_values, I_values, R_values, P_values = [], [], [], []  # Listas vazias para armazenar os resultados

# Simulação usando o método de Euler
for t in t_values:
    # Salvamos os valores atuais antes de calcular os novos
    S_values.append(S)
    I_values.append(I)
    R_values.append(R)
    P_values.append(P)

    # Cálculo das variações de cada grupo de computadores
    dS = -beta * S * I - alpha * S * P  # Redução dos suscetíveis por infecção e proteção
    dI = beta * S * I - gamma * I  # Aumento de infectados menos os que se recuperam
    dR = gamma * I  # Removidos aumentam proporcionalmente aos infectados que se recuperam
    dP = alpha * S * P  # Protegidos aumentam pela taxa de instalação de antivírus

    # Atualização dos valores usando o método de Euler
    S += dS * dt
    I += dI * dt
    R += dR * dt
    P += dP * dt

# Plotando os resultados
plt.plot(t_values, S_values, label='Suscetíveis')
plt.plot(t_values, I_values, label='Infectados')
plt.plot(t_values, R_values, label='Removidos')
plt.plot(t_values, P_values, label='Protegidos')

# Configuração do gráfico
plt.xlabel('Tempo (dias)')
plt.ylabel('Número de Computadores')
plt.title('Propagação de um Vírus em uma Rede de Computadores')
plt.legend()  # Adiciona legenda
plt.grid()  # Adiciona grade ao gráfico
plt.show()  # Exibe o gráfico
