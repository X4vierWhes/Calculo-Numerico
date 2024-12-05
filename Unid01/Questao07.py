import time

def f(x):
    """Define a função para a qual queremos encontrar a raiz."""
    return x ** 3 - 9 * x + 3

def derivada(x, epsilon=1e-7):
    """Calcula a derivada numérica da função f em x."""
    return (f(x + epsilon) - f(x)) / epsilon

def metodo_newton(x0, epsilon, max_iter=100):
    """Encontra a raiz usando o Método de Newton."""
    for _ in range(max_iter):
        df = derivada(x0)
        if abs(df) < 1e-10:
            return None, "Derivada muito próxima de zero."
        x1 = x0 - f(x0) / df
        if abs(f(x1)) < epsilon:
            return x1, _
        x0 = x1
    return None, "Número máximo de iterações atingido."

def metodo_secante(x0, x1, epsilon, max_iter=100):
    """Encontra a raiz usando o Método da Secante."""
    for _ in range(max_iter):
        denom = f(x1) - f(x0)
        if abs(denom) < 1e-10:
            return None, "Denominador muito próximo de zero."
        x2 = x1 - f(x1) * (x1 - x0) / denom
        if abs(f(x2)) < epsilon:
            return x2, _
        x0, x1 = x1, x2
    return None, "Número máximo de iterações atingido."

def main():
    print("Função: f(x) = x^3 - 9x + 3")
    x0 = float(input("Digite o ponto inicial (x0): "))
    x1 = float(input("Digite o segundo ponto inicial (x1) para a secante: "))
    epsilon = float(input("Digite a precisão desejada: "))

    # Método de Newton
    start = time.time()
    raiz_newton, msg_newton = metodo_newton(x0, epsilon)
    tempo_newton = time.time() - start

    # Método da Secante
    start = time.time()
    raiz_secante, msg_secante = metodo_secante(x0, x1, epsilon)
    tempo_secante = time.time() - start

    # Resultados
    print("\nResultados:")
    if raiz_newton:
        print(f"Método de Newton: Raiz = {raiz_newton:.6f}, Tempo = {tempo_newton:.6f} segundos")
    else:
        print(f"Método de Newton: {msg_newton}")

    if raiz_secante:
        print(f"Método da Secante: Raiz = {raiz_secante:.6f}, Tempo = {tempo_secante:.6f} segundos")
    else:
        print(f"Método da Secante: {msg_secante}")

if __name__ == "__main__":
    main()
