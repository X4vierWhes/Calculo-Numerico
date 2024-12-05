import time

def f(x):
    """Define a função para a qual queremos encontrar a raiz."""
    return x ** 2 - 4

def derivada(x, epsilon=1e-7):
    """Calcula a derivada numérica da função f em x usando o valor de epsilon."""
    return (f(x + epsilon) - f(x)) / epsilon

def arredondar_raiz(raiz, tolerancia=1e-3):
    """
    Arredonda a raiz para o inteiro mais próximo se a diferença for menor que a tolerância.
    """
    inteiro_mais_proximo = round(raiz)
    if abs(raiz - inteiro_mais_proximo) < tolerancia:
        return float(f"{inteiro_mais_proximo:.4f}")
    return float(f"{raiz:.4f}")

def metodo_newton(x0, epsilon, max_iter=100):
    """
    Implementa o método de Newton para encontrar a raiz da função f.
    Exibe todas as iterações.
    """
    x = x0
    iter_count = 0

    print("\nMétodo de Newton:")
    while abs(f(x)) > epsilon and iter_count < max_iter:
        df = derivada(x, epsilon)
        if abs(df) < 1e-10:  # Evitar divisão por zero ou derivada muito pequena
            raise ValueError("Derivada muito próxima de zero. Método de Newton interrompido.")

        x = x - f(x) / df
        iter_count += 1
        print(f"Iteração {iter_count}: x = {x:.6f}, f(x) = {f(x):.6f}")

    return arredondar_raiz(x), iter_count

def metodo_secante(x0, x1, epsilon, max_iter=100):
    """
    Implementa o método da secante para encontrar a raiz da função f.
    Exibe todas as iterações.
    """
    iter_count = 0

    print("\nMétodo da Secante:")
    while abs(f(x1)) > epsilon and iter_count < max_iter:
        denominator = f(x1) - f(x0)
        if abs(denominator) < 1e-10:  # Evitar divisão por zero ou denominador muito pequeno
            raise ValueError("Denominador muito próximo de zero. Método da Secante interrompido.")

        # Fórmula do método da secante
        x_new = x1 - f(x1) * (x1 - x0) / denominator

        # Atualizar os pontos
        x0, x1 = x1, x_new
        iter_count += 1
        print(f"Iteração {iter_count}: x = {x1:.6f}, f(x) = {f(x1):.6f}")

    return arredondar_raiz(x1), iter_count

def comparar_metodos(raiz_newton, iter_newton, tempo_newton, raiz_secante, iter_secante, tempo_secante):
    """
    Compara os métodos de Newton e Secante com base no número de iterações e tempo de execução.
    """
    if iter_newton < iter_secante:
        print("\nO método de Newton realizou menos iterações.")
    elif iter_newton > iter_secante:
        print("\nO método da Secante realizou menos iterações.")
    else:
        print("\nAmbos os métodos realizaram o mesmo número de iterações.")

    if tempo_newton < tempo_secante:
        print("O método de Newton foi mais rápido.")
    elif tempo_newton > tempo_secante:
        print("O método da Secante foi mais rápido.")
    else:
        print("Ambos os métodos foram igualmente rápidos.")

def main():
    # Entrada do usuário
    print("Escolha uma função para encontrar a raiz: f(x) = x^2 - 4")
    x0 = float(input("Digite o ponto inicial (x0): "))
    x1 = float(input("Digite o segundo ponto inicial (x1) para a secante: "))
    epsilon = float(input("Digite o valor da precisão: "))

    try:
        # Método de Newton
        start_newton = time.time()
        raiz_newton, iter_newton = metodo_newton(x0, epsilon)
        end_newton = time.time()

        # Método da Secante
        start_secante = time.time()
        raiz_secante, iter_secante = metodo_secante(x0, x1, epsilon)
        end_secante = time.time()

        # Resultados
        tempo_newton = end_newton - start_newton
        tempo_secante = end_secante - start_secante

        print("\nResultados:")
        print(
            f"Método de Newton: Raiz = {raiz_newton:.4f}, Iterações = {iter_newton}, Tempo = {tempo_newton:.6f} segundos")
        print(
            f"Método da Secante: Raiz = {raiz_secante:.4f}, Iterações = {iter_secante}, Tempo = {tempo_secante:.6f} segundos")

        # Comparação dos métodos
        comparar_metodos(raiz_newton, iter_newton, tempo_newton, raiz_secante, iter_secante, tempo_secante)

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
