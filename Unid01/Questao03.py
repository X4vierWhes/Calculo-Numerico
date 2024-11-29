import math
import time
from sympy import sympify, symbols

# Receber a função do usuário
user_input = input("Digite uma função matemática de x (ex: x**2 + 2*x + 1): ")


def s(x0):
    x = symbols('x')
    try:
        # Converter a string em uma expressão simbólica
        expr = sympify(user_input)

        return expr.subs(x, x0)
    except Exception as e:
        print(f"Erro ao processar a função: {e}")


def ZeroDaFuncao(a, b):
    tempo_inicial = time.time()
    epsilon = 10 ** -5
    # Garantir que s(a) e s(b) não tenham sinais opostos
    if s(a) * s(b) >= 0:
        ite = int((math.log10(b - a) - math.log10(epsilon)) / math.log10(2)) + 1
        k = ite
        while (k):
            k -= 1
            x = (a + b) / 2
            if s(x) == 0:
                break
            elif abs(s(a)) < epsilon:
                x = a
                break
            elif abs(s(b)) < epsilon:
                x = b
                break
            elif (abs(s(a)) < abs(s(b))):
                b = x
            else:
                a = x

        if (s(x) > epsilon):
            print('Não existe raízes entre o intervalo dado.')
        else:
            tempo_final = time.time()
            print('Tempo em segundos: ', (tempo_final - tempo_inicial))
            print('Iterações necessárias: ', (ite - k))
            print(f'A raiz aproximada é: {x:.5f}')

    else:
        ite = 0
        while abs(b - a) > epsilon:
            ite += 1
            x = (a + b) / 2
            if s(x) == 0:
                break
            elif s(a) * s(x) < 0:
                b = x
            else:
                a = x

        tempo_final = time.time()
        print('Tempo em segundos: ', (tempo_final - tempo_inicial))
        print('Iterações necessárias: ', (ite))
        print(f"A raiz aproximada é: {x:.5f}")


# ...
a = int(input('Digite o início do intervalo: '))
b = int(input('Digite o fim do intervalo: '))

ZeroDaFuncao(a, b)

