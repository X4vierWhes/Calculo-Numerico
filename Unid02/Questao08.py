def polinomio_lagrange():
    print("### Cálculo do Polinômio de Lagrange ###")
    # Definindo os pontos dados no problema
    X = [3.0, 3.2, 3.4]  # Valores de x escolhidos próximos a 3.1
    Y = [20.08, 24.53, 29.96]  # Valores correspondentes de e^x

    print("Pontos escolhidos: ")
    print("X:", X)
    print("Y:", Y)

    # Valor a ser interpolado
    x_interpolado = 3.1

    # Calculando os coeficientes de Lagrange
    coeficientes = []
    for indice in range(len(X)):
        L = 1
        for j in range(len(X)):
            if indice != j:
                L *= (x_interpolado - X[j]) / (X[indice] - X[j])
        coeficientes.append(L)

    # Calculando o valor do polinômio
    pn = 0
    for i in range(len(coeficientes)):
        pn += Y[i] * coeficientes[i]

    # Exibindo o resultado
    print(f"Valor aproximado de e^{x_interpolado} usando Lagrange: {pn:.4f}")

    # Estimativa do erro
    from math import exp

    f_derivada_terceira = exp(3.4)  # Aproximação usando o valor de e^3.4
    erro = abs(f_derivada_terceira / 6 * (x_interpolado - X[0]) * (x_interpolado - X[1]) * (x_interpolado - X[2]))
    print(f"Erro máximo estimado: {erro:.5f}")


# Chamando a função
polinomio_lagrange()
