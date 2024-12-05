import numpy as np

def f(x):
    return x**2  # Função a ser derivada

def erro_percentual(valor_calculado, valor_exato):
    if valor_exato != 0:
        return abs((valor_calculado - valor_exato) / valor_exato) * 100
    else:
        return abs(valor_calculado) * 100  # Caso especial para derivadas de ordem 3

def main():
    # Entrada do usuário
    h = float(input("Digite o valor do acréscimo (h): "))
    x = float(input("Digite o ponto para o cálculo da derivada (x): "))

    # Valores exatos das derivadas
    valor_exato_1ordem = 2 * x
    valor_exato_2ordem = 2
    valor_exato_3ordem = 0

    # Cálculo das derivadas de 1ª ordem
    derivada1_ordem1 = (f(x + h) - f(x)) / h  # Diferença para frente
    derivada1_ordem2 = (f(x) - f(x - h)) / h  # Diferença para trás
    derivada1_ordem3 = (f(x + h) - f(x - h)) / (2 * h)  # Diferença central
    derivada1_ordem4 = (f(x - 2 * h) + 8 * f(x + h) - 8 * f(x - h) - f(x + 2 * h)) / (12 * h)  # Fórmula de 5 pontos

    # Cálculo das derivadas de 2ª ordem
    derivada2_ordem1 = (f(x + h) - 2 * f(x) + f(x - h)) / (h**2)  # Diferença central
    derivada2_ordem2 = (f(x + 2 * h) - 2 * f(x + h) + f(x)) / (h**2)  # Diferença para frente
    derivada2_ordem3 = (f(x) - 2 * f(x - h) + f(x - 2 * h)) / (h**2)  # Diferença para trás
    derivada2_ordem4 = -(f(x + 2 * h) - 16 * f(x + h) + 30 * f(x) - 16 * f(x - h) + f(x - 2 * h)) / (12 * (h**2))  # Fórmula de 5 pontos

    # Cálculo das derivadas de 3ª ordem
    derivada3_ordem1 = (f(x + 2 * h) - 2 * f(x + h) + 2 * f(x - h) - f(x - 2 * h)) / (2 * (h**3))  # Diferença central
    derivada3_ordem2 = (f(x + 3 * h) - 3 * f(x + 2 * h) + 3 * f(x + h) - f(x)) / (h**3)  # Diferença para frente
    derivada3_ordem3 = (f(x) - 3 * f(x - h) + 3 * f(x - 2 * h) - f(x - 3 * h)) / (h**3)  # Diferença para trás
    derivada3_ordem4 = (f(x + 2 * h) - 2 * f(x + h) + 2 * f(x - h) - f(x - 2 * h)) / (2 * (h**3))  # Fórmula de 5 pontos

    # Cálculo do erro percentual
    erros_1ordem = [
        erro_percentual(derivada1_ordem1, valor_exato_1ordem),
        erro_percentual(derivada1_ordem2, valor_exato_1ordem),
        erro_percentual(derivada1_ordem3, valor_exato_1ordem),
        erro_percentual(derivada1_ordem4, valor_exato_1ordem),
    ]

    erros_2ordem = [
        erro_percentual(derivada2_ordem1, valor_exato_2ordem),
        erro_percentual(derivada2_ordem2, valor_exato_2ordem),
        erro_percentual(derivada2_ordem3, valor_exato_2ordem),
        erro_percentual(derivada2_ordem4, valor_exato_2ordem),
    ]

    erros_3ordem = [
        erro_percentual(derivada3_ordem1, valor_exato_3ordem),
        erro_percentual(derivada3_ordem2, valor_exato_3ordem),
        erro_percentual(derivada3_ordem3, valor_exato_3ordem),
        erro_percentual(derivada3_ordem4, valor_exato_3ordem),
    ]

    # Exibição dos resultados
    print("\n=== Derivadas de 1ª ordem e Erros ===")
    print(f"Diferença para frente: {derivada1_ordem1}, Erro: {erros_1ordem[0]}%")
    print(f"Diferença para trás: {derivada1_ordem2}, Erro: {erros_1ordem[1]}%")
    print(f"Diferença central: {derivada1_ordem3}, Erro: {erros_1ordem[2]}%")
    print(f"Fórmula de 5 pontos: {derivada1_ordem4}, Erro: {erros_1ordem[3]}%")

    print("\n=== Derivadas de 2ª ordem e Erros ===")
    print(f"Diferença central: {derivada2_ordem1}, Erro: {erros_2ordem[0]}%")
    print(f"Diferença para frente: {derivada2_ordem2}, Erro: {erros_2ordem[1]}%")
    print(f"Diferença para trás: {derivada2_ordem3}, Erro: {erros_2ordem[2]}%")
    print(f"Fórmula de 5 pontos: {derivada2_ordem4}, Erro: {erros_2ordem[3]}%")

    print("\n=== Derivadas de 3ª ordem e Erros ===")
    print(f"Diferença central: {derivada3_ordem1}, Erro: {erros_3ordem[0]}%")
    print(f"Diferença para frente: {derivada3_ordem2}, Erro: {erros_3ordem[1]}%")
    print(f"Diferença para trás: {derivada3_ordem3}, Erro: {erros_3ordem[2]}%")
    print(f"Fórmula de 5 pontos: {derivada3_ordem4}, Erro: {erros_3ordem[3]}%")

if __name__ == "__main__":
    main()