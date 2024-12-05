import time


def f(x):
    """Define a função para a qual queremos encontrar a raiz."""
    return x ** 3 - 9 * x + 3


def derivada(x, epsilon=1e-7):
    """Calcula a derivada numérica da função f em x usando o valor de epsilon."""
    return (f(x + epsilon) - f(x)) / epsilon


def metodo_newton(x0, epsilon, max_iter=100):
    """
    Implementa o método de Newton para encontrar a raiz da função f.

    Args:
        x0: Ponto inicial para o método de Newton.
        epsilon: Precisão desejada para a raiz.
        max_iter: Número máximo de iterações.

    Returns:
        A raiz encontrada e o número de iterações realizadas.
    """
    x = x0
    iter_count = 0

    while abs(f(x)) > epsilon and iter_count < max_iter:
        df = derivada(x, epsilon)
        if abs(df) < 1e-10:  # Evitar divisão por zero ou derivada muito pequena
            raise ValueError("Derivada muito próxima de zero. Método de Newton interrompido.")

        x = x - f(x) / df
        iter_count += 1

    return x, iter_count


def metodo_secante(x0, x1, epsilon, max_iter=100):
    """
    Implementa o método da secante para encontrar a raiz da função f.

    Args:
        x0: Primeiro ponto inicial.
        x1: Segundo ponto inicial.
        epsilon: Precisão desejada para a raiz.
        max_iter: Número máximo de iterações.

    Returns:
        A raiz encontrada e o número de iterações realizadas.
    """
    iter_count = 0

    while abs(f(x1)) > epsilon and iter_count < max_iter:
        denominator = f(x1) - f(x0)
        if abs(denominator) < 1e-10:  # Evitar divisão por zero ou denominador muito pequeno
            raise ValueError("Denominador muito próximo de zero. Método da Secante interrompido.")

        # Fórmula do método da secante
        x_new = x1 - f(x1) * (x1 - x0) / denominator

        # Atualizar os pontos
        x0, x1 = x1, x_new
        iter_count += 1

    return x1, iter_count


def main():
    # Entrada do usuário
    print("Escolha uma função para encontrar a raiz: f(x) = x^3 - 9x + 3")
    x0 = float(input("Digite o ponto inicial (x0): "))
    x1 = float(input("Digite o segundo ponto inicial (x1) para a secante: "))
    epsilon = float(input("Digite o valor da precisão: "))

    try:
        # Comparando os métodos
        # Método de Newton
        start_newton = time.time()
        raiz_newton, iter_newton = metodo_newton(x0, epsilon)
        end_newton = time.time()

        # Método da Secante
        start_secante = time.time()
        raiz_secante, iter_secante = metodo_secante(x0, x1, epsilon)
        end_secante = time.time()

        # Resultados
        print("\nResultados:")
        print(
            f"Método de Newton: Raiz = {raiz_newton:.6f}, Iterações = {iter_newton}, Tempo = {end_newton - start_newton:.6f} segundos")
        print(
            f"Método da Secante: Raiz = {raiz_secante:.6f}, Iterações = {iter_secante}, Tempo = {end_secante - start_secante:.6f} segundos")

        # Comparação
        if iter_newton < iter_secante:
            print("\nO método de Newton realizou menos iterações.")
        else:
            print("\nO método da Secante realizou menos iterações.")

        if (end_newton - start_newton) < (end_secante - start_secante):
            print("O método de Newton foi mais rápido.")
        else:
            print("O método da Secante foi mais rápido.")

    except ValueError as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()
