import math
import time

#variavel caso queira testar se s(x) < epsilon
testar_funcoes_com_x = False

#Funções e suas respectivas iterações
"""
Função 1:
s(x) = x**3 - x - 1
g(x) = (x+1)**(1/3)

Função 2:
s(x) = x * x + x - 6
g(x) = 6 / (x + 1)

Função 3:
s(x) = x**2 - 2*x + 1
g(x) = 2 - (1/x)
"""

# Função s(x)
def s(x):
    return x**3 - x - 1

# Função de iteração g(x)
def g(x):
    return (x+1)**(1/3)

# Método do Ponto Fixo
def metodo_ponto_fixo(a, b, epsilon):
    try:
        tempo_inicial = time.time()
        if(s(a) * s(b) >= 0):
            c = a # Ponto inicial
            gc = g(c)
            max_iter = 2000
            ite = 1
            while (abs(s(gc)) > epsilon and max_iter > 0):
                max_iter -= 1
                ite += 1
                c = gc
                gc = g(c)

            if(s(gc) > epsilon):
                print('Não existem raízes entre o intervalo dado.')
            else:
                print("\n[Método do Ponto Fixo]")
                print(f"Tempo de execução: {time.time() - tempo_inicial:.6f} segundos")
                print(f"Iterações necessárias: {ite}")
                print(f"A raiz aproximada é: {gc:.5f}") 
                if(testar_funcoes_com_x):
                    print(f's(x) é menor que epsilon? {abs(s(gc)) < epsilon}')
        else:
            c = a # Ponto inicial
            gc = g(c)

            ite = 1
            while abs(s(gc)) > epsilon:
                ite+= 1
                c = gc
                gc = g(c)

            print("\n[Método do Ponto Fixo]")
            print(f"Tempo de execução: {time.time() - tempo_inicial:.6f} segundos")
            print(f"Iterações necessárias: {ite}")
            print(f"A raiz aproximada é: {gc:.5f}")
            if(testar_funcoes_com_x):
                    print(f'f(x) é menor que epsilon? {abs(s(gc)) < epsilon}')
    except Exception as e:
        print(f'Erro: {e}')
        print('\nIntervalo inválido no Método do Ponto Fixo, digite outro intervalo.')
        #Recebe um novo intervalo do usuário
        a = float(input('Digite o início do intervalo: '))
        b = float(input('Digite o fim do intervalo: '))

        #Executa o metodo novamente
        metodo_ponto_fixo(a, b, epsilon)

#Método da Bisseção
def metodo_bissecao(a, b, epsilon):
    try:
        tempo_inicial = time.time()
        ite = 0

        # Garantir que s(a) e s(b) não tenham sinais opostos
        if s(a) * s(b) >= 0:
            k = int((math.log10(b - a) - math.log10(epsilon))/math.log10(2)) + 1
            
            while(k):
                k-=1
                ite += 1
                x = (a + b) / 2
                if abs(s(x)) < epsilon:
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

            if(s(x) > epsilon):
                print('Não existe raízes entre o intervalo dado.')
            else:
                print("\n[Método da Bisseção]")
                print(f"Tempo de execução: {time.time() - tempo_inicial:.6f} segundos")
                print(f"Iterações necessárias: {ite}")
                print(f"A raiz aproximada é: {x:.5f}")
                if(testar_funcoes_com_x):
                    print(f's(x) é menor que epsilon? {abs(s(x)) < epsilon}')

        else:
            while abs(b - a) > epsilon:
                ite += 1
                x = (a + b) / 2
                if s(x) == 0:
                    break
                elif s(a) * s(x) < 0:
                    b = x
                else:
                    a = x

            print("\n[Método da Bisseção]")
            print(f"Tempo de execução: {time.time() - tempo_inicial:.6f} segundos")
            print(f"Iterações necessárias: {ite}")
            print(f"A raiz aproximada é: {x:.5f}")
            if(testar_funcoes_com_x):
                    print(f's(x) é menor que epsilon? {abs(s(x)) < epsilon}')

    except Exception as e:
        print(f'Erro: {e}')
        print('\nIntervalo inválido no Método da Bisseção, digite outro intervalo.')
        #Recebe um novo intervalo do usuário
        a = float(input('Digite o início do intervalo: '))
        b = float(input('Digite o fim do intervalo: '))

        #Executa o metodo novamente
        metodo_bissecao(a, b, epsilon)

#Dados iniciais
a = float(input('Digite o início do intervalo: '))
b = float(input('Digite o fim do intervalo: '))
epsilon = float(input('Digite o valor de epsilon: '))

metodo_ponto_fixo(a, b, epsilon)
metodo_bissecao(a, b, epsilon)

 