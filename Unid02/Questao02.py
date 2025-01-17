import numpy as np

# Definindo a matriz A
A = np.array([
    [2, -1, 1],
    [4, -7, 11],
    [3, -4, 7]
])

print("Matriz A:\n", A)

# Calculando o determinante
Determinante = np.linalg.det(A)
print("O determinante de A é:", Determinante)

# Verificando se a matriz é não singular
if Determinante != 0:
    print("A matriz A é não singular, então é possível encontrar a decomposição LU.")

    n = A.shape[0]  # Dimensão da matriz
    L = np.zeros((n, n))  # Inicializando L com zeros
    U = np.zeros((n, n))  # Inicializando U com zeros

    # Construção das matrizes L e U
    for i in range(n):
        # Preenchendo os elementos de U
        for k in range(i, n):
            U[i, k] = A[i, k] - sum(L[i, j] * U[j, k] for j in range(i))

        # Preenchendo os elementos de L
        for k in range(i, n):
            if i == k:
                L[i, i] = 1  # Elementos da diagonal de L são 1
            else:
                L[k, i] = (A[k, i] - sum(L[k, j] * U[j, i] for j in range(i))) / U[i, i]

    print("Matriz L:\n", L)
    print("Matriz U:\n", U)

else:
    print("A matriz A tem determinante zero e não é possível encontrar sua decomposição LU.")
