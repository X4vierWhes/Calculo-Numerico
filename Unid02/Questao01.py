import numpy as np

def lu_decomposition(A):
    """Realiza a decomposição LU da matriz A."""
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))  

    for i in range(n):
        U[i][i] = 1 # Diagonal da U é 1
        for j in range(i, n):
            L[j][i] = A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))
        
        for j in range(i + 1, n):
            U[i][j] = (A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))) / L[i][i]

    return L, U

def forward_substitution(L, b):
    """Resolve Ly = b usando substituição direta."""
    n = len(b)
    y = np.zeros_like(b)

    for i in range(n):
        y[i] = (b[i] - sum(L[i][j] * y[j] for j in range(i))) / L[i][i]
    return y

def backward_substitution(U, y):
    """Resolve Ux = y usando substituição retroativa."""
    n = len(y)
    x = np.zeros_like(y)

    for i in range(n - 1, -1, -1):
        x[i] = y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))
    return x

def solve_linear_system_crout(A, B):
    """Resolve o sistema linear Ax = B usando a decomposição LU."""
    L, U = lu_decomposition(A)
    y = forward_substitution(L, B)
    x = backward_substitution(U, y)
    return x

# Exemplo de uso
A = np.array([[2, 3, 1],
              [1, 2, 3],
              [3, 1, 2]], dtype=float)
B = np.array([1, 2, 3], dtype=float)

L, U = lu_decomposition(A)
print("Matriz L:")
print(L)
print("Matriz U:")
print(U)

x = solve_linear_system_crout(A, B)
print("Solução x:", x)
