import numpy as np

def eliminacao_gauss(A, b):
    n = len(b)
    # Eliminação de Gauss
    for k in range(n-1):
        if A[k,k] == 0:
            raise ValueError(f'O elemento A[{k},{k}] é zero, não é possível continuar a eliminação de Gauss.')

        # Eliminações para transformar em uma matriz triangular superior
        for i in range(k+1, n):
            m = A[i,k] / A[k,k]
            A[i,k:] = A[i,k:] - m * A[k,k:]
            b[i] = b[i] - m * b[k]

    # Resolução do sistema pela substituição reversa
    x = np.zeros(n)
    x[-1] = b[-1] / A[-1,-1]

    #regressive substitution
    for k in range(n-2, -1, -1):
        s = 0
        for j in range(k+1, n):
            s += A[k,j] * x[j]
        x[k] = (b[k] - s) / A[k,k]

    return x

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

# Exemplo 0
A = np.array([[2, 1, -1], 
[-3, -1, 2], 
[-2, 1, 2]], dtype=float)
b = np.array([8, -11, -3], dtype=float)

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

# Main
solution = eliminacao_gauss(A, b)
is_solution = test_solve(A, solution, b, False)

print("-----------------------------------")
print("Solução aproximada:", solution)
print("Solução aproximada é solução do sistema:", is_solution)
print("-----------------------------------")