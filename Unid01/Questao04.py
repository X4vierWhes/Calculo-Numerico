import math
import time
from sympy import sympify, symbols

# Receber a função do usuário
user_input = input("Digite uma função matemática de x (ex: x**2 - 4): ")

epsilon = 0.00001

def s(x0):
    x = symbols('x')
    try:
        # Converter a string em uma expressão simbólica
        expr = sympify(user_input)
        return expr.subs(x, x0)
    except Exception as e:
        print(f"Erro ao processar a função: {e}")

# Método da Bisseção
def metodo_bissecao(a, b):
    tempo_inicial = time.time()
    ite = 0

    if s(a) * s(b) >= 0:
        print("Erro: s(a) e s(b) devem ter sinais opostos.")
        return

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
    print("\n[Método da Bisseção]")
    print(f"Tempo de execução: {tempo_final - tempo_inicial:.6f} segundos")
    print(f"Iterações necessárias: {ite}")
    print(f"A raiz aproximada é: {x:.5f}")

# Método da Falsa Posição
def metodo_falsa_posicao(a, b):
    tempo_inicial = time.time()
    ite = 0

    if s(a) * s(b) >= 0:
        print("Erro: s(a) e s(b) devem ter sinais opostos.")
        return

    while abs(s((a * s(b) - b * s(a)) / (s(b) - s(a)))) > epsilon:
        ite += 1
        x = (a * s(b) - b * s(a)) / (s(b) - s(a))
        if s(x) == 0:
            break
        elif s(a) * s(x) < 0:
            b = x
        else:
            a = x

    tempo_final = time.time()
    print("\n[Método da Falsa Posição]")
    print(f"Tempo de execução: {tempo_final - tempo_inicial:.6f} segundos")
    print(f"Iterações necessárias: {ite}")
    print(f"A raiz aproximada é: {x:.5f}")

# Receber intervalo do usuário
a = float(input('Digite o início do intervalo: '))
b = float(input('Digite o fim do intervalo: '))

# Executar os métodos
metodo_bissecao(a, b)
metodo_falsa_posicao(a, b)
