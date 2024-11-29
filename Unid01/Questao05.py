import math

def f(x):
    return x ** 4 * math.sin(1 / x) if x != 0 else 0

def g(x):
    if x > 1:
        return x ** 4 - 1
    elif x < 1:
        return -x ** 4 + 1
    else:
        return None  # Caso de indefinição para x = 1


def limite_lateral(func, x, delta, lado="esquerdo"):
    if lado == "esquerdo":
        return func(x - delta)
    elif lado == "direito":
        return func(x + delta)


def limite_bilateral(func, x, epsilon=1e-6):
    delta = 1e-6  # Pequeno valor para calcular os limites laterais
    limite_esq = limite_lateral(func, x, delta, lado="esquerdo")
    limite_dir = limite_lateral(func, x, delta, lado="direito")

    if abs(limite_dir - limite_esq) < epsilon:
        return limite_esq  # Limite bilateral existe
    else:
        return None  # Não existe limite bilateral


def main():
    print("Escolha a função para análise:")
    print("1 - f(x)")
    print("2 - g(x)")
    escolha = int(input("Digite o número da função desejada: "))

    x0 = float(input("Informe o ponto de análise: "))
    epsilon = float(input("Informe a tolerância para a comparação: "))

    if escolha == 1:
        func = f
    elif escolha == 2:
        func = g
    else:
        print("Opção inválida.")
        return

    limite_esq = limite_lateral(func, x0, epsilon, lado="esquerdo")
    limite_dir = limite_lateral(func, x0, epsilon, lado="direito")
    limite_bilat = limite_bilateral(func, x0, epsilon)

    print("Limite pela esquerda:", limite_esq)
    print("Limite pela direita:", limite_dir)
    if limite_bilat is not None:
        print("Limite bilateral:", limite_bilat)
    else:
        print("Não existe limite bilateral para essa função.")


if __name__ == "__main__":
    main()
