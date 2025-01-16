import numpy as np
#PG 155 do Livro Métodos Numéricos
#Problemas do Código
#1) Testar os coeficientes do vetor b(se forem iguais sistema impossível) OK
#2) Diagonal principal nao pode ser 0 OK
#3) Sistemas podem ser SPI ou SI, ou seja, devemos testar isso antes OK
#4) Determinante != de 0 OK
#5) Testar se a matriz é diagonal dominante OK
#6) Testar se a soluçao encontrada realmente está correta OK
#7) Dízima breka o código OK
def gauss_jacobi(A, b, x0, epsilon=1e-6, max_iter=100):
    n = len(b) #Ordem da Matriz
    x = x0.copy() #Cópia do vetor de solução inicial
    x_new = np.zeros_like(x) #Vetor que armazenará a resposta final
    
    #Testes para saber se o sistema dado é possivel por esse método

    #1) Coeficientes de b iguais
    have_duplicate = len(b) != len(np.unique(b))
    if(have_duplicate): raise ValueError("Erro! Vetor b possui valores duplicados. Sistema Impossível.")

    #2) Todos os elementos da diagonal principal != 0
    for i in range(n): 
        if(A[i][i] == 0):
            raise ValueError("Erro! A matriz dada possui zero(s) diagonal principal!")
    
    #3) Matriz é diagonal principal
    for i in range(n):
        # Soma dos elementos fora da diagonal para a linha i
        sum_of_others = np.sum(np.abs(A[i])) - np.abs(A[i, i])
        # Verifica se o elemento diagonal é maior que a soma dos outros
        if np.abs(A[i, i]) <= sum_of_others:
            raise ValueError("Erro! A matriz dada não é diagonal dominante!")

    #4) Teste se o sistema é SPD
    # Dimensões da matriz
    l, m = A.shape
    # Cálculo do posto (rank) da matriz A
    rank_A = np.linalg.matrix_rank(A)
    # Cálculo do posto da matriz aumentada [A | b]
    A_increased = np.hstack((A, b.reshape(-1, 1)))
    rank_A_increased = np.linalg.matrix_rank(A_increased)
    
    # Determinar o tipo de sistema
    if rank_A != rank_A_increased:
        raise ValueError("Erro! O sistema dado é impossível(SI)!")
    elif rank_A == rank_A_increased:
        if rank_A == m:
            is_spd = True
        else:
            raise ValueError("Erro! O sistema dado é possível e indeterminado(SPI)!")
    
    if(is_spd):
        for k in range(max_iter):
            for i in range(n):
                sigma = sum(-A[i][j] * x[j] for j in range(n) if j != i)
                x_new[i] = (b[i] + sigma) / A[i][i]
            dist = (x_new - x)

            if (abs(np.max(dist)) < epsilon):
                return x_new, k + 1
            x = x_new.copy()
        
    raise ValueError("O método de Gauss-Jacobi não convergiu dentro do número máximo de iterações.")

def test_solve(A, solution, b, print_results, epsilon=1e-3, ):
    n = len(A)
    approximate_result = np.zeros_like(b)

    for i in range(n):
        approximate_result[i] = sum(A[i][j] * solution[j] for j in range(n))

    if(print_results):
        print("-----------------------------------")
        print("Resultado aproximado:", approximate_result)
        print("Resultado real:", b)
        print("-----------------------------------\n")
    dist = (approximate_result - b)
    if(abs(np.max(dist)) < epsilon):
        return True
    else:
        return False
        
# Exemplo 0:
A = np.array([[9, -2, 3, 2],
[2, 8, -2, 3],
[-3, 2, 11, -4],
[-2, 3, 2, 10]], dtype=float)
b = np.array([54.5, -14, 12.5, -21], dtype=float)


# Exemplo 1:
A1 = np.array([[12, 2, 1],
[1, 15, 2],
[2, 3, 13]], dtype=float)
b1 = np.array([7, -8, 6], dtype=float)

# Exemplo 2
A2 = np.array([[14.439, 0.978, 2.797, -3.915, -1.007],
[1.169, 15.782, -3.084, -0.114, 2.679],
[-1.761, 0.292, 14.665, -1.642, 3.319],
[-1.871, 2.531, -0.539, 12.992, -2.889],
[-0.056, 0.542, -2.434, -3.407, 13.031]], dtype=float)
b2 = np.array([16.473, -39.866, 45.32, -10.577, -25.248], dtype=float)

#Exemplo 3
A3 = np.array([[16.771, -3.672, -1.962, 1.757, 1.621, 3.179],
[1.589, 20.821, -0.152, -3.583, 2.208, -2.895],
[0.255, 3.393, 19.422, 1.177, -1.219, 2.273],
[-0.194, -2.426, 1.607, 16.91, -2.132, 1.127],
[0.721, 1.68, 1.36, 1.486, 15.402, -2.693],
[3.42, -2.716, -1.902, -3.608, -1.017, 21.313]], dtype=float)
b3 = np.array([7.882, -30.711, 44.324, 25.366, -11.973, 38.756], dtype=float)

#Exemplo 4(Não é diagonal Dominante)
A4 = np.array([[-2.928, -0.151, -2.973, -2.554, 0.149],
[4.827, -1.715, -3.278, 3.151, -1.211],
[-0.925, -1.974, -3.268, 0.484, -4.784],
[4.569, -4.271, 4.632, -2.824, -3.914],
[4.578, -0.957, -0.603, 3.745, -1.359]
], dtype=float)
b4 = np.array([-16.612, -33.651, 8.572, 29.415, 17.258], dtype=float)

#Main
x0 = np.array([0, 0, 0, 0], dtype=float)
solution, iterations = gauss_jacobi(A, b, x0)
is_solution = test_solve(A, solution, b, False)

print("-----------------------------------")
print("Solução aproximada:", solution)
print("Número de iterações:", iterations)
print("Solução aproximada é solução do sistema:", is_solution)
print("-----------------------------------")