import math

area_superficial = 1200
raio = 17
altura = 20
iteracoes = 0
max_iteracoes = 5
epsilon = 4

def calculo_area(raio, altura):
    return math.pi * raio * (math.sqrt(raio**2 + altura**2))

def funcao_iteracao(raio, altura, valor_desejado):
    return valor_desejado / (math.pi * (math.sqrt(raio**2 + altura**2)))

def metodo_ponto_fixo_cone(raio,altura,valor_desejado,iteracoes,max_iteracoes,epsilon):
    raio_atual = raio

    while iteracoes <= max_iteracoes:
        area_atual = calculo_area(raio_atual, altura)
        if abs(area_atual - valor_desejado) < epsilon:
            return raio_atual

        raio_atual = funcao_iteracao(raio_atual, altura, valor_desejado)
        iteracoes += 1

    return f"Não foi possível encontrar um raio em {max_iteracoes} iterações"



result = metodo_ponto_fixo_cone(raio, altura, area_superficial, iteracoes, max_iteracoes, epsilon)

print(calculo_area(result, altura))
print(result)
