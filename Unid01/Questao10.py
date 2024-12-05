import math

L = 3
E = 70
I = 52.9 * (10 ** (-6))
w0 = 15
x0 = 1.5  
epsilon = 1e-7  

def f(x):
    """Define a função para a qual queremos encontrar a raiz."""
    return L*w0*(48*L**3*math.cos(math.pi*x/(2*L)) - 48*L**3 + 3*math.pi**3*L*x**2 - math.pi**3*x**3)/(3*math.pi**4*E*I)

def g(x):
    return f(x) - 0.009

def derivada(x, epsilon):
    """Calcula a derivada numérica da função f em x usando o valor de epsilon."""
    return (f(x + epsilon) - f(x)) / epsilon

def metodo_newton(x0, epsilon, max_iter=100):
    """
    Implementa o método de Newton para encontrar a raiz da função g.

    Args:
        x0: Ponto inicial para o método de Newton.
        epsilon: Precisão desejada para a raiz.
        max_iter: Número máximo de iterações.

    Returns:
        A raiz encontrada e o número de iterações realizadas.
    """
    x = x0
    iter_count = 0

    while abs(g(x)) > epsilon and iter_count < max_iter:
        df = derivada(x, epsilon)
        if abs(df) < 1e-10:  # Evitar divisão por zero ou derivada muito pequena
            raise ValueError("Derivada muito próxima de zero. Método de Newton interrompido.")

        x = x - g(x) / df
        iter_count += 1

    return x, iter_count

def metodo_secante(x0, x1, epsilon, max_iter=100):
    """
    Implementa o método da secante para encontrar a raiz da função g.

    Args:
        x0: Primeiro ponto inicial.
        x1: Segundo ponto inicial.
        epsilon: Precisão desejada para a raiz.
        max_iter: Número máximo de iterações.

    Returns:
        A raiz encontrada e o número de iterações realizadas.
    """
    iter_count = 0

    while abs(g(x1)) > epsilon and iter_count < max_iter:
        denominator = g(x1) - g(x0)
        if abs(denominator) < 1e-10:  # Evitar divisão por zero ou denominador muito pequeno
            raise ValueError("Denominador muito próximo de zero. Método da Secante interrompido.")

        # Fórmula do método da secante
        x_new = x1 - g(x1) * (x1 - x0) / denominator

        # Atualizar os pontos
        x0, x1 = x1, x_new
        iter_count += 1

    return x1, iter_count

try:
    raiz_newton, iteracoes_newton = metodo_newton(x0, epsilon)
    print(f"A raiz encontrada pelo método de Newton é x = {raiz_newton} após {iteracoes_newton} iterações.")
except ValueError as e:
    print(e)


try:
    x1 = x0 + 0.1  
    raiz_secante, iteracoes_secante = metodo_secante(x0, x1, epsilon)
    print(f"A raiz encontrada pelo método da Secante é x = {raiz_secante} após {iteracoes_secante} iterações.")
except ValueError as e:
    print(e)
