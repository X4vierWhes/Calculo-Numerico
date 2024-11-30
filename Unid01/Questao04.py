import time
import math

#variavel caso queira testar se s(x) < epsilon
testar_funcoes_com_x = False

#Definindo a função
def s(x):
        return (x - 1)**3

#Método da Falsa Posição
def metodo_falsa_posicao(a, b, epsilon):
    try:
        tempo_inicial = time.time()
        ite = 0

        # Garantir que s(a) e s(b) não tenham sinais opostos
        if s(a) * s(b) >= 0:
            k = 100
            while(k > 0):
                k -= 1
                ite += 1
                x =  (a * s(b) - b * s(a)) / (s(b) - s(a))
                if abs(s(x)) < epsilon:
                    break
                elif abs(s(a)) < epsilon:
                    x = a
                    break
                elif abs(s(b)) < epsilon:
                    x = b
                    break
                elif (abs(s(a)) < abs(s(b))): 
                    b = x #Raiz está entre a e x
                else:
                    a = x #Raiz está entre x e b

            if(s(x) > epsilon):
                print('Não existem raízes entre o intervalo dado.')
            else:
                print("\n[Método da Falsa Posição]")
                print(f"Tempo de execução: {time.time() - tempo_inicial:.6f} segundos")
                print(f"Iterações necessárias: {ite}")
                print(f"A raiz aproximada é: {x:.5f}") 
                if(testar_funcoes_com_x):
                    print(f's(x) é menor que epsilon? {s(x) < epsilon}')

        else:
            while (abs(b - a) > epsilon):
                ite += 1
                x = (a * s(b) - b * s(a)) / (s(b) - s(a)) # Fórmula da falsa posição
                if s(x) == 0:
                    break
                elif abs(s(a)) < epsilon:
                    x = a
                    break
                elif abs(s(b)) < epsilon:
                    x = b
                    break
                elif abs(s(a)) < abs(s(b)):
                    b = x # Raiz está entre a e x
                else:
                    a = x # Raiz está entre x e b

            print("\n[Método da Falsa Posição]")
            print(f"Tempo de execução: {time.time() - tempo_inicial:.6f} segundos")
            print(f"Iterações necessárias: {ite}")
            print(f"A raiz aproximada é: {x:.5f}")   
            if(testar_funcoes_com_x):
                    print(f's(x) é menor que epsilon? {s(x) < epsilon}')
    except Exception as e:
        print('\nIntervalo inválido no Método da Falsa Posição, digite outro intervalo.')
        #Recebe um novo intervalo do usuário
        a = float(input('Digite o início do intervalo: '))
        b = float(input('Digite o fim do intervalo: '))

        #Executa o metodo novamente
        metodo_falsa_posicao(a, b, epsilon)

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

            if(s(x) > epsilon):
                print('Não existe raízes entre o intervalo dado.')
            else:
                print("\n[Método da Bisseção]")
                print(f"Tempo de execução: {time.time() - tempo_inicial:.6f} segundos")
                print(f"Iterações necessárias: {ite}")
                print(f"A raiz aproximada é: {x:.5f}")
                if(testar_funcoes_com_x):
                    print(f's(x) é menor que epsilon? {s(x) < epsilon}')

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
                    print(f's(x) é menor que epsilon? {s(x) < epsilon}')

    except Exception as e:
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

#Executa os métodos
metodo_bissecao(a, b, epsilon)
metodo_falsa_posicao(a, b, epsilon)