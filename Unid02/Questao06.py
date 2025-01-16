import numpy as np

def matriz_hilbert(n):
    mh = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            mh[i][j] = (1/(i+1 + j+1 - 1))
    return mh

def termos_independentes(n):
    id = np.zeros(n)
    for i in range(n):
        id[i] = sum(1/(i+1 + j+1 - 1) for j in range(n))
    return id

#Sistemas
#Matriz do Sistema 1
A1 = np.array([[1, -1], [1, -1.00001]])

#Matriz do Sistema 2
A2 = np.array([[1, -1], [1, -0.99999]])

#Vetor dos termos independentes
b1 = np.array([1, 0])

#Resolução do Primeiro Sistema
print("\n[Sistema 1]")
print("x -        y = 1")
print("x - 1.00001y = 0")
print(f"Solução :{np.linalg.solve(A1, b1)}")

#Resolução do Segundo Sistema
print("\n[Sistema 2]")
print("x -        y = 1")
print("x - 0.99999y = 0")
print(f"Solução :{np.linalg.solve(A2, b1)}")

#Condidionamento da Matrizes de Hilbert
print("\n[Matrizes de Hilbert]")
print(f"Condicionamento da MH de Ordem 2: {np.linalg.cond(matriz_hilbert(2)):.5f}")
print(f"Condicionamento da MH de Ordem 3: {np.linalg.cond(matriz_hilbert(3)):.5f}")
print(f"Condicionamento da MH de Ordem 4: {np.linalg.cond(matriz_hilbert(4)):.5f}")
print(f"Condicionamento da MH de Ordem 5: {np.linalg.cond(matriz_hilbert(5)):.5f}")
print(f"Condicionamento da MH de Ordem 6: {np.linalg.cond(matriz_hilbert(6)):.5f}")

#Resolução de um sistema de H₇*x = b₇
print("\n[Resolução do Sistema H₇*x = b₇]")
H = matriz_hilbert(7)
b = termos_independentes(7)
solve = np.linalg.solve(H, b)
print(f"Solução: {solve}")