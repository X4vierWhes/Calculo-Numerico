# Check if the matrix is diagonal dominant
def check_diaDom(A):
    r = len(A)
    diagnl = 0
    non_diagnl = 0

    for i in range(r):
        for j in range(r):
            if i == j:
                diagnl += abs(A[i][j])
            else: 
                non_diagnl += abs(A[i][j])

    if diagnl >= non_diagnl:
        return True
    else:
        return False


def GS_method(A, Y, X):
    n = len(A)  # para encontrar o número de linhas ou colunas da matriz quadrada A
    for j in range(n):
        summ_val = Y[j]
        for i in range(n):
            if j != i:
                summ_val -= A[j][i] * X[i]
        X[j] = summ_val / A[j][j]
    return X


def gauss_seidel_with_tolerance(A, Y, X, tol=1e-6, max_iter=1000):
    n = len(A)
    for k in range(max_iter):
        X_old = X.copy()
        X = GS_method(A, Y, X)

        print(f"Iteração {k + 1}: {X}")


        # Verifica o critério de convergência
        if all(abs(X[i] - X_old[i]) < tol for i in range(n)):
            print(f"Solução convergiu em {k + 1} iterações.")
            return X

    print("O método não convergiu no número máximo de iterações.")
    return X


A = [[8, 3, -3], [-2, -8, 5], [3, 5, 10]]  # Coeficientes das variáveis desconhecidas
Y = [14, 5, -8]  # Termos independentes
X = [0, 0, 0]  # Chute inicial para o método

if check_diaDom(A):
    X = gauss_seidel_with_tolerance(A, Y, X, tol=1e-6, max_iter=1000)
    print(f"Solução aproximada: {X}")
else:
    print('Matriz não é diagonalmente dominante.')
