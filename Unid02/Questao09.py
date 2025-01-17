import numpy as np
# Função para calcular o polinômio interpolador de Lagrange de grau <= 2
def lagrange_grau_2(x, pontos):
    soma = 0
    for i in range(len(pontos)):
        produto = 1.0
        for j in range(len(pontos)):
            if j == i:
                continue
            produto *= (x - pontos[j][0]) / (pontos[i][0] - pontos[j][0])
        soma += pontos[i][1] * produto
    return soma

# fevereiro (0, 0.64), março (1, 0.24), maio (3, 2.94)
pontos = [(1, 0.64), (2, 0.24), (4, 2.94)]  # polinômio de grau 2 = 3 pontos

# Estimar o valor para abril (x = 2)
x_interpolar = 3
inflacao_estimada = lagrange_grau_2(x_interpolar, pontos)

# Resultado
print(f"A inflação estimada para abril (x = {x_interpolar}) é: {inflacao_estimada:.2f}%")









# Função para construir a tabela
def tabela_diferencas_divididas(x, y):
    n = len(x)
    tabela = np.zeros((n, n + 1))
    
    # Preenchendo a primeira coluna com os valores de x e a segunda com os valores de y
    for i in range(n):
        tabela[i, 0] = x[i]
        tabela[i, 1] = y[i]
    
    # Construindo as diferenças divididas
    for j in range(2, n + 1):  # Colunas
        for i in range(n - j + 1):  # Linhas
            tabela[i, j] = (tabela[i + 1, j - 1] - tabela[i, j - 1]) / (x[i + j - 1] - x[i])
    
    return tabela

# Dados de entrada
x = np.array([1, 2, 3, 5, 6], float)
y = np.array([0.75, 0.64, 0.24, 2.94, 0.37], float)

# Gerando a tabela 
tabela = tabela_diferencas_divididas(x, y)

# Mostrando a tabela 
print("Tabela de diferenças divididas:")
for i in range(len(x)):
    print(" ".join(f"{tabela[i, j]:.5f}" for j in range(len(x) + 1 - i)))
    





# Função para calcular o erro da estimativa do polinômio de Lagrange
def erro_estimativa(x_interpolar, pontos, f_n):
    n = len(pontos)  # Número de pontos (n = 3 para grau 2)
    
    # Cálculo do erro utilizando a fórmula do erro para Lagrange
    erro = 1
    for ponto in pontos:
        erro *= (x_interpolar - ponto[0])
    
    # Aproximação do erro com base na fórmula (dividido por 6, já que temos 3 pontos e o grau do polinômio é 2)
    erro /= 6  # Para o grau 2, o fator será 6 (3! = 6)
    
    # Multiplicando pelo valor da derivada f(n)(ξ)
    erro *= f_n
    
    return erro
    
    # Valor da derivada f(n)(ξ)
f_n = -0.47250

# Cálculo do erro da estimativa
erro = erro_estimativa(x_interpolar, pontos, f_n)

# Resultados
print(f"Erro da estimativa: {erro:.5f}")














# Função para calcular o polinômio interpolador de Lagrange de grau <= 2
def polinomio_lagrange_grau_2(x, dados):
    resultado = 0
    for i in range(len(dados)):
        produto = 1.0
        for j in range(len(dados)):
            if j == i:
                continue
            produto *= (x - dados[j][0]) / (dados[i][0] - dados[j][0])
        resultado += dados[i][1] * produto
    return resultado

# Dados dos meses e suas inflações correspondentes
dados_inflacao = [(1, 0.24), (3, 2.94), (4, 0.37)]  # Meses de abril a junho

# Estimativa para o mês de julho (x = 3)
mes_para_estimativa = 5
inflacao_estimativa_julho = polinomio_lagrange_grau_2(mes_para_estimativa, dados_inflacao)

# Resultado
print(f"A inflação estimada para julho (mês {mes_para_estimativa}) é: {inflacao_estimativa_julho:.2f}%")